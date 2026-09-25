"""Finite m2-rdf-record-1 identity extension; existing profiles are untouched."""
import re
from rdflib import Graph, URIRef
from rdflib.namespace import RDF, OWL
import m1_fixture_identity as core

PROFILE = 'm2-rdf-record-1'
ORIGIN = 'live-source-derived'
BASE = core.BASE + 'id/'
DKG = core.BASE + 'ontology#'
KEYS = {
    'SourceSnapshot': {'descriptionId', 'edition', 'versionIri', 'loaded', 'updated', 'locator'},
    'DiseaseConceptReference': {'snapshotKey', 'locator', 'role', 'authority', 'identifier', 'label'},
    'HierarchyStep': {'snapshotKey', 'locator', 'childKey', 'parentKey'},
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def is_record(iri, kind):
    return isinstance(iri, str) and re.fullmatch(re.escape(BASE + kind + '/') + '[0-9a-f]{64}', iri) is not None


def receipt(kind, inputs, payload, origin=ORIGIN):
    require(origin == ORIGIN and kind in KEYS, 'Unsupported origin or kind')
    require(set(inputs) == KEYS[kind], 'Wrong receipt input keys')
    require(all(isinstance(v, str) and v for v in inputs.values()), 'Incomplete identity lineage')
    if kind == 'SourceSnapshot':
        require(re.fullmatch(re.escape(BASE + 'm2-source-description-1/') + '[0-9a-f]{64}', inputs['descriptionId']), 'Not an M2 source description')
    else:
        require(is_record(inputs['snapshotKey'], 'SourceSnapshot'), 'Invalid snapshot reference')
    if kind == 'DiseaseConceptReference':
        require(inputs['role'] in {'reported-participant', 'hierarchy-endpoint'}, 'Unsupported role')
        require(inputs['authority'] == 'MONDO' and re.fullmatch(r'MONDO:[0-9]{7}', inputs['identifier']), 'Invalid Mondo reference')
    if kind == 'HierarchyStep':
        require(all(is_record(inputs[k], 'DiseaseConceptReference') for k in ('childKey', 'parentKey')), 'Invalid endpoint reference')
    schema = Graph().parse(data=(core.ROOT / 'ontology/dementiagraph-v.ttl').read_bytes(), format='turtle')
    properties = set(schema.subjects(RDF.type, OWL.ObjectProperty)) | set(schema.subjects(RDF.type, OWL.DatatypeProperty))
    payload = core.normalized_payload(payload)
    for a in payload:
        iri = 'http://www.w3.org/ns/prov#wasDerivedFrom' if a['field'] == 'prov:wasDerivedFrom' else DKG + a['field']
        require(URIRef(iri) in properties, 'Unapproved payload property')
    return {'profile': PROFILE, 'kind': kind, 'origin': origin,
            'inputs': dict(inputs), 'contentRevision': core.digest(core.canonical(payload))}


def identify(value):
    require(set(value) == {'profile', 'kind', 'origin', 'inputs', 'contentRevision'}, 'Wrong receipt keys')
    require(value['profile'] == PROFILE and value['origin'] == ORIGIN and value['kind'] in KEYS, 'Wrong identity profile')
    return BASE + value['kind'] + '/' + core.digest(core.canonical(value))


class Registry:
    def __init__(self, descriptions):
        # Caller supplies only offline-verified description receipts/context.
        self.descriptions = descriptions
        self.entries = {}

    def add(self, kind, inputs, payload, iri=None, origin=ORIGIN):
        rec = receipt(kind, inputs, payload, origin)
        if kind == 'SourceSnapshot':
            expected = self.descriptions.get(inputs['descriptionId'])
            require(expected is not None, 'Unverified description identity')
            require(all(inputs[k] == expected[k] for k in ('edition', 'versionIri', 'loaded', 'updated', 'locator')), 'Source context mismatch')
        else:
            snapshot = self.entries.get(inputs['snapshotKey'])
            require(snapshot and snapshot['receipt']['kind'] == 'SourceSnapshot', 'Unregistered snapshot (M1 reuse forbidden)')
            if kind == 'HierarchyStep':
                for key in ('childKey', 'parentKey'):
                    endpoint = self.entries.get(inputs[key])
                    require(endpoint and endpoint['receipt']['kind'] == 'DiseaseConceptReference', 'Unregistered endpoint')
        computed = identify(rec)
        require(iri is None or iri == computed, 'Conflicting supplied identity')
        value = {'iri': computed, 'receipt': rec, 'payload': core.normalized_payload(payload)}
        require(computed not in self.entries or self.entries[computed] == value, 'Identity collision')
        self.entries[computed] = value
        return computed
