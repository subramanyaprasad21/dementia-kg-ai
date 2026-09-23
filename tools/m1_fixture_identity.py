"""Finite m1-id-1 receipts; offline audit fixtures, not production ingestion."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://github.com/subramanyaprasad21/dementia-kg-ai/'
XSD = 'http://www.w3.org/2001/XMLSchema#'


def canonical(value):
    """RFC 8785 subset: string/null/array/object only, UTF-16 key ordering.

    The approved receipt/payload profile excludes numbers and booleans. Never
    use this function to canonicalize arbitrary upstream API JSON.
    """
    if value is None:
        return b'null'
    if isinstance(value, str):
        value.encode('utf-8', 'strict')
        return json.dumps(value, ensure_ascii=False, separators=(',', ':')).encode()
    if isinstance(value, list):
        return b'[' + b','.join(canonical(v) for v in value) + b']'
    if isinstance(value, dict):
        if not all(isinstance(k, str) for k in value):
            raise ValueError('Non-string key')
        keys = sorted(value, key=lambda k: k.encode('utf-16-be', 'strict'))
        return b'{' + b','.join(canonical(k) + b':' + canonical(value[k]) for k in keys) + b'}'
    raise ValueError('Profile permits strings, null, arrays and objects only')


def strict_load(text):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError('Duplicate JSON key: ' + key)
            result[key] = value
        return result
    return json.loads(text, object_pairs_hook=pairs)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def catalogue():
    text = (ROOT / 'docs/m1_implementation_mechanics.md').read_text()
    table = text.split('| Kind / variant | Exact keys in inputs |')[1].split('For referents,')[0]
    result = {}
    for line in table.splitlines():
        cells = [c.strip() for c in line.split('|')[1:-1]]
        if len(cells) != 2 or cells[0].startswith('---'):
            continue
        title = cells[0]
        if title.startswith('DiseaseTargetAssociation /'):
            names = [title.replace(' / ', ':')]
        else:
            names = title.split(' / ')
        for name in names:
            result[name] = cells[1].split(', ')
    return result


def normalize_inputs(kind, inputs):
    variant = kind
    if kind == 'DiseaseTargetAssociation':
        variant += ':' + inputs.get('originRole', '')
    definitions = catalogue().get(variant)
    if definitions is None:
        raise ValueError('Unapproved kind/variant')
    keys = {d.replace('[]S', '').replace('[]O', '').rstrip('?') for d in definitions}
    if set(inputs) != keys:
        raise ValueError('Wrong receipt keys for ' + kind)
    result = {}
    for definition in definitions:
        nullable = definition.endswith('?')
        key = definition.replace('[]S', '').replace('[]O', '').rstrip('?')
        value = inputs[key]
        if value is None and nullable:
            result[key] = None
            continue
        if '[]' in definition:
            if not isinstance(value, list) or not all(isinstance(v, str) and v for v in value):
                raise ValueError('Bad array: ' + key)
            if definition.endswith('[]S'):
                value = sorted(set(value), key=lambda v: v.encode())
        elif not isinstance(value, str) or not value:
            raise ValueError('Required nonempty string: ' + key)
        result[key] = value
    if 'execution' in result and result['execution'] is not None:
        if not re.fullmatch(r'[a-z][a-z0-9-]*/[1-9][0-9]*', result['execution']):
            raise ValueError('Invalid execution reference')
    if kind == 'DiseaseConceptReference':
        if not result['label'] and not (result['authority'] and result['identifier']):
            raise ValueError('No observed disease identity')
    if kind in {'Target', 'Drug', 'Publication', 'Study'} and result['disambiguator'] is not None:
        raise ValueError('Initial authority identifiers require null disambiguator')
    return result


def normalized_payload(assertions):
    unique = {}
    for a in assertions:
        if set(a) != {'field', 'form', 'value', 'datatype', 'language'}:
            raise ValueError('Wrong payload assertion keys')
        if a['form'] == 'iri':
            if a['datatype'] is not None or a['language'] is not None or not re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', a['value']):
                raise ValueError('Malformed IRI assertion')
        elif a['form'] == 'literal':
            if (a['datatype'] is None) == (a['language'] is None):
                raise ValueError('Literal needs exactly datatype or language')
        else:
            raise ValueError('Invalid assertion form')
        if not isinstance(a['value'], str):
            raise ValueError('Lexical values must be strings')
        unique[canonical(a)] = a
    return [unique[k] for k in sorted(unique)]


def receipt(kind, origin, inputs, payload):
    inputs = normalize_inputs(kind, inputs)
    referents = {'Target', 'Drug', 'Publication', 'Study'}
    operations = {'SelectionContext', 'SelectionMembership', 'DerivedStatement', 'InspectionRecord', 'MissingnessRecord'}
    allowed = {'referent'} if kind in referents else {'project-operation'} if kind in operations else {'audit-transcription', 'project-operation'} if kind in {'MappingRecord', 'HierarchyPath', 'DiseaseTargetAssociation'} else {'audit-transcription'}
    if origin not in allowed:
        raise ValueError('Invalid origin route')
    if kind == 'DiseaseTargetAssociation' and origin != ('project-operation' if inputs['originRole'] == 'project-grouping' else 'audit-transcription'):
        raise ValueError('Association origin mismatch')
    if kind in {'MappingRecord', 'HierarchyPath'} and origin == 'project-operation':
        if not all(inputs.get(k) for k in ['execution', 'method', 'methodVersion']):
            raise ValueError('Missing project method/execution')
    payload = normalized_payload(payload)
    if kind in referents | {'SelectionMembership'}:
        revision = None
    elif kind == 'SourceSnapshot':
        revision = inputs['artifactDigest']
        if not re.fullmatch('[0-9a-f]{64}', revision):
            raise ValueError('Invalid artifact digest')
    else:
        revision = digest(canonical(payload))
    return dict(profile='m1-id-1', kind=kind, origin=origin, inputs=inputs, contentRevision=revision)


def identify(record):
    return BASE + 'id/' + record['kind'] + '/' + digest(canonical(record))


class Registry:
    def __init__(self):
        self.entries = {}

    def add(self, rec, payload, iri=None):
        iri = iri or identify(rec)
        value = (canonical(rec), canonical(normalized_payload(payload)))
        if iri in self.entries and self.entries[iri] != value:
            raise ValueError('Identity collision or conflicting immutable payload; quarantine')
        self.entries[iri] = value
        return iri
