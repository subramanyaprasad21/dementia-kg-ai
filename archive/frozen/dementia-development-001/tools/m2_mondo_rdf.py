"""Offline deterministic RDF of the frozen Mondo projection; no network or inference."""
import argparse
import json
import os
from pathlib import Path
from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, XSD
import m2_mondo_extract as extract
import m2_rdf_identity as identity

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'kg/mondo-pilot-001'
DKG = Namespace(identity.DKG)
PROV = Namespace('http://www.w3.org/ns/prov#')
EXTRACTION_SHA = '43d7537f1f8e14340160d9581e8891db7f2dbe60a903c3910648295aae091882'
DECISION_SHA = '0df85aa9649a0318015732c8fa5bcecb4fd549dc0a67f6c76a8ee795992bafa7'


def artifacts():
    return Path(os.environ.get('MONDO_PILOT_ARTIFACTS', str(extract.freeze.DEFAULT_ARTIFACTS)))


def load(root=None):
    root = artifacts() if root is None else Path(root)
    identity.require(extract.capture.sha(extract.OUTPUT.read_bytes()) == EXTRACTION_SHA, 'Extraction changed')
    identity.require(extract.capture.sha((ROOT/'assessments/mondo-pilot-001.normalization.json').read_bytes()) == DECISION_SHA, 'Assessment changed')
    extract.verify(artifacts=root)
    return json.loads(extract.OUTPUT.read_bytes()), json.loads(extract.freeze.DEFAULT_MANIFEST.read_bytes())


def lexical(fields, key):
    v = fields[key]
    identity.require(v['state'] == 'present' and v['value']['type'] == 'string', 'Missing source string')
    return v['value']['value']


def canonical(value):
    return identity.core.canonical(value).decode('utf-8')


def assertion(field, value, iri=False):
    return dict(field=field, form='iri' if iri else 'literal', value=str(value),
                datatype=None if iri else str(XSD.string), language=None)


def predicate(field):
    return PROV.wasDerivedFrom if field == 'prov:wasDerivedFrom' else DKG[field]


def graph_of(registry):
    graph = Graph()
    for iri, entry in registry.entries.items():
        s = URIRef(iri)
        graph.add((s, RDF.type, DKG[entry['receipt']['kind']]))
        for a in entry['payload']:
            o = URIRef(a['value']) if a['form'] == 'iri' else Literal(a['value'], datatype=URIRef(a['datatype']) if a['datatype'] else None, lang=a['language'], normalize=False)
            graph.add((s, predicate(a['field']), o))
    return graph


def serialize(graph):
    # Sorted N-Triples subset is valid Turtle; no blank nodes or unstable prefixes.
    identity.require(all(isinstance(s, URIRef) and isinstance(p, URIRef) and isinstance(o, (URIRef, Literal)) for s,p,o in graph), 'Unsupported RDF term')
    return ('\n'.join(sorted(f'{s.n3()} {p.n3()} {o.n3()} .' for s,p,o in graph))+'\n').encode('utf-8')


def build(root=None):
    data, freeze = load(root)
    byslot = {e['slot']: e for e in freeze['responses']}
    descriptions = {e['descriptionId']: dict(freeze['sourceContext'], locator=e['descriptionReceipt']['locator']) for e in freeze['responses']}
    registry = identity.Registry(descriptions)
    snapshots, refs, source_links = {}, {}, {}
    for slot, entry in byslot.items():
        if slot.startswith('metadata'):
            continue
        inputs = dict(descriptionId=entry['descriptionId'], **descriptions[entry['descriptionId']])
        payload = [assertion('sourceAuthority', 'EMBL-EBI-OLS / Mondo'),
                   assertion('snapshotVersion', freeze['sourceContext']['edition']),
                   assertion('sourceLocator', entry['captureReceipt']['request']['url']),
                   assertion('artifactDescription', canonical(dict(description=entry['descriptionReceipt'], sourceContext=freeze['sourceContext'], permissions=freeze['permissions'], scope='Projected response slice, not full ontology release'))),
                   assertion('prov:wasDerivedFrom', entry['descriptionId'], True)]
        snapshots[slot] = registry.add('SourceSnapshot', inputs, payload)
        source_links[snapshots[slot]] = [slot]

    def reference(values, lineage, role):
        slot = lineage['responseSlot']; locator = canonical(lineage['sourceRecordLocator'])
        inputs = dict(snapshotKey=snapshots[slot], locator=locator, role=role,
                      authority='MONDO', identifier=lexical(values,'obo_id'), label=lexical(values,'label'))
        payload = [assertion('inSnapshot', snapshots[slot], True), assertion('identifierAuthority','MONDO'),
                   assertion('externalIdentifier',inputs['identifier']), assertion('sourceLabel',inputs['label']),
                   assertion('sourceLocator',locator)]
        iri = registry.add('DiseaseConceptReference', inputs, payload)
        source_links[iri] = [slot]
        return iri

    for concept in data['concepts']:
        refs[concept['recordKey']] = reference(concept['sourceValues'], concept['lineage'], 'reported-participant')
    for record in data['parentAssertions']:
        child_slot = record['childLineage']['responseSlot']
        child = refs[child_slot]
        # Explicit exact endpoint correspondence is checked, not label-based merge.
        candidates = [c for c in data['concepts'] if all(c['sourceValues'][k] == record['parent'][k] for k in ('obo_id','iri'))]
        identity.require(len(candidates) == 1, 'Parent reference unresolved')
        parent = reference(record['parent'], record['lineage'], 'hierarchy-endpoint')
        slot = record['lineage']['responseSlot']; locator = canonical(record['lineage']['sourceRecordLocator'])
        inputs = dict(snapshotKey=snapshots[slot], locator=locator, childKey=child, parentKey=parent)
        payload = [assertion('inSnapshot',snapshots[slot],True), assertion('childReference',child,True),
                   assertion('parentReference',parent,True), assertion('sourceLocator',locator),
                   assertion('scopeText','Source-reported immediate OLS parent navigation; no inferred closure or equivalence.')]
        iri = registry.add('HierarchyStep',inputs,payload)
        source_links[iri] = [child_slot, slot]
    receipts = dict(profile=identity.PROFILE, extractionSha256=EXTRACTION_SHA,
                    freezeSha256=extract.MANIFEST_HASH, records=registry.entries,
                    sourceSlots=source_links)
    return graph_of(registry), receipts


def outputs(root=None):
    graph, receipts = build(root)
    return {'records.ttl': serialize(graph), 'record-identities.json': extract.freeze.serialize(receipts)}


def verify(directory=OUT, root=None):
    expected = outputs(root)
    for name, raw in expected.items():
        identity.require((Path(directory)/name).read_bytes() == raw, 'RDF/receipt replay differs: '+name)
    graph = Graph().parse(data=expected['records.ttl'],format='turtle')
    return {'records': len(set(graph.subjects())), 'triples':len(graph)}


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation',choices=['build','verify'])
    args=parser.parse_args()
    if args.operation=='build':
        values=outputs()
        OUT.mkdir(parents=True,exist_ok=True)
        for name, raw in values.items():
            with (OUT/name).open('xb') as f: f.write(raw)
    print(json.dumps(verify(),sort_keys=True))
