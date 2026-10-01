"""Attach existing capture/description identities using only approved PROV/local terms."""
import argparse
import json
from pathlib import Path
from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDF, XSD
import m2_mondo_rdf as rdf

OUT = rdf.OUT / 'provenance.ttl'


def build(root=None):
    data, freeze = rdf.load(root)
    graph = Graph()
    groups = {}
    for e in freeze['responses']:
        groups.setdefault(e['descriptionId'], []).append(e)
    for description, entries in groups.items():
        s = URIRef(description)
        source_values = []
        exclusions = []
        for e in entries:
            slot = e['slot']
            for c in data['concepts']:
                if c['lineage']['responseSlot'] == slot:
                    source_values.append(dict(locator=c['lineage']['sourceRecordLocator'], values=c['sourceValues']))
            for a in data['parentAssertions']:
                if a['lineage']['responseSlot'] == slot:
                    source_values.append(dict(locator=a['lineage']['sourceRecordLocator'], child=a['child'], parent=a['parent']))
            exclusions.extend(x['lineage']['sourceRecordLocator'] for x in data['excludedRawRows'] if x['lineage']['responseSlot'] == slot)
        graph.add((s, RDF.type, rdf.PROV.Entity))
        graph.add((s, rdf.DKG.sourceLocator, Literal(rdf.canonical(dict(freeze=data['freeze'], responseSlots=[e['slot'] for e in entries])), datatype=XSD.string)))
        text = dict(descriptionReceipt=entries[0]['descriptionReceipt'], sourceContext=freeze['sourceContext'],
                    extractedSourceValues=source_values, excludedRawRowLocators=exclusions,
                    projectionNotice='Attributed extraction values, not a copy of the whole description projection or raw response.',
                    permissions=freeze['permissions'])
        graph.add((s, rdf.DKG.sourceText, Literal(rdf.canonical(text), datatype=XSD.string)))
        graph.add((s, rdf.DKG.scopeText, Literal('Mondo source-description context; xrefs and source annotations are attributed text, not project equivalence assertions.',datatype=XSD.string)))
    for e in freeze['responses']:
        s = URIRef(e['captureId'])
        graph.add((s,RDF.type,rdf.PROV.Entity))
        graph.add((s,rdf.DKG.contextRecord,URIRef(e['descriptionId'])))
        graph.add((s,rdf.DKG.sourceLocator,Literal(rdf.canonical(dict(freeze=data['freeze'], artifact=e['artifact'], requestUrl=e['captureReceipt']['request']['url'])),datatype=XSD.string)))
        graph.add((s,rdf.DKG.sourceText,Literal(rdf.canonical(e['captureReceipt']),datatype=XSD.string)))
        graph.add((s,rdf.DKG.scopeText,Literal('Capture encounter metadata, not another independent source assertion. Raw bytes remain outside Git.',datatype=XSD.string)))
    return graph


def verify(path=OUT, root=None):
    expected = rdf.serialize(build(root))
    rdf.identity.require(Path(path).read_bytes() == expected, 'Provenance replay differs')
    return {'resources':29,'triples':len(build(root))}


if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('operation',choices=['build','verify']);args=p.parse_args()
    if args.operation=='build':
        raw=rdf.serialize(build())
        with OUT.open('xb') as f:f.write(raw)
    print(json.dumps(verify(),sort_keys=True))
