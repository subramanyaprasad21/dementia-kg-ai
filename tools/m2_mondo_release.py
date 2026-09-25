"""Offline in-place release manifest; no duplicate dataset or source download."""
import argparse
import json
from importlib.metadata import version
from pathlib import Path
import m2_mondo_provenance as provenance
rdf=provenance.rdf
OUT=rdf.ROOT/'manifests/mondo-pilot-001.kg-release.json'
VALIDATED_BASELINE='1adcd3ac513bae6f16482b1ccb7a7c35de98dd0a'
FILES=[
 'ontology/dementiagraph-v.ttl','validation/m1_shapes.ttl',
 'manifests/mondo-pilot-001.freeze.json','extractions/mondo-pilot-001.json',
 'assessments/mondo-pilot-001.normalization.json',
 'kg/mondo-pilot-001/records.ttl','kg/mondo-pilot-001/record-identities.json','kg/mondo-pilot-001/provenance.ttl',
 'tools/m1_fixture_identity.py','tools/m2_mondo_capture.py','tools/m2_mondo_freeze.py',
 'tools/m2_mondo_extract.py','tools/m2_rdf_identity.py','tools/m2_mondo_rdf.py',
 'tools/m2_mondo_provenance.py','tools/validate_m1_fixtures.py','tools/validate_m2_mondo.py','tools/m2_mondo_release.py',
 'tests/test_m2_mondo_reference_consistency.py','tests/test_m2_rdf_identity.py',
 'tests/test_m2_mondo_rdf.py','tests/test_m2_mondo_provenance.py',
 'tests/test_m2_mondo_validation.py','tests/test_m2_mondo_release.py',
 'docs/m1_implementation_mechanics.md','docs/m1_implementation_readiness.md',
 'docs/m1_conceptual_model_contract.md','docs/m1_owl_reasoning.md',
 'docs/m2_mondo_pilot.md','docs/m2_mondo_freeze.md','docs/m2_mondo_extraction.md',
 'docs/m2_mondo_normalization.md','docs/m2_mondo_reference_consistency.md',
 'docs/m2_rdf_identity.md','docs/m2_mondo_rdf.md','docs/m2_mondo_provenance.md','docs/m2_mondo_validation.md']


def build(root=None):
    data,freeze=rdf.load(root)
    rdf.verify(root=root);provenance.verify(root=root)
    graph,_=rdf.build(root);graph+=provenance.build(root)
    return dict(profile='mondo-kg-slice-release-1',sliceId='mondo-pilot-001',
                scope='Mondo-only source-backed KG slice; not full dementia KG or complete M2 corpus',
                validatedBaseline=VALIDATED_BASELINE,
                files=[dict(path=p,sha256=rdf.extract.capture.sha((rdf.ROOT/p).read_bytes())) for p in FILES],
                sourceContext=freeze['sourceContext'],terms=freeze['terms'],
                parents=[dict(child=c,parent=p) for c,p in rdf.extract.freeze.PARENTS],
                inventory=dict(externalConcepts='8',acceptedParents='5',excludedRawRows='6',
                               scopedDiseaseReferences='13',snapshots='13',hierarchySteps='5',
                               sourceDescriptions='14',captures='15',resources='60',triples=str(len(graph))),
                graphParts=['kg/mondo-pilot-001/records.ttl','kg/mondo-pilot-001/provenance.ttl'],
                graphSha256=rdf.extract.capture.sha(rdf.serialize(graph)),
                externalArtifacts=dict(freezePath='manifests/mondo-pilot-001.freeze.json',
                                       freezeSha256=rdf.extract.MANIFEST_HASH,ledger=freeze['ledger'],
                                       responses=[dict(artifact=e['artifact'],sha256=e['sha256']) for e in freeze['responses']],
                                       relocation='MONDO_PILOT_ARTIFACTS points to unchanged local batch directory; no network fallback'),
                permissions=freeze['permissions'],
                dependencies={name:version(name) for name in ['rdflib','owlrl','pyshacl','packaging','prettytable','pyparsing','html5rdf','wcwidth']},
                limitations=freeze['limitations']+[
                    'RDF/source fidelity and structural acceptance are not independent biomedical validation.',
                    'Full-corpus M2 remains incomplete; no M3/M4 implementation is authorized by this release.',
                    'Graph advantage remains NOT YET DEMONSTRATED.',
                    'Raw response bodies and acquisition ledger remain outside Git; Git checkout alone cannot verify original bytes.'])


def verify(path=OUT, root=None):
    raw=Path(path).read_bytes()
    value=rdf.identity.core.strict_load(raw.decode('utf-8'))
    rdf.identity.require(raw==rdf.extract.freeze.serialize(value),'Noncanonical release manifest')
    expected=build(root)
    rdf.identity.require(value==expected,'Release inventory, dependencies or artifact integrity differs')
    return dict(status='pass',sha256=rdf.extract.capture.sha(raw),resources=60,triples=317)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('operation',choices=['build','verify']);args=p.parse_args()
    if args.operation=='build':
        raw=rdf.extract.freeze.serialize(build())
        with OUT.open('xb') as f:f.write(raw)
    print(json.dumps(verify(),sort_keys=True))
