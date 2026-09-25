"""Reproducible bounded OT + unchanged Mondo release; never a full corpus claim."""
import argparse
import sys
from pathlib import Path
from importlib.metadata import version
from rdflib.namespace import RDF
import ot2606_source as source
import ot2606_rdf as rdf
import validate_ot2606 as validation
import validate_m2_mondo as mondo
import validate_m1_fixtures as structural
MANIFEST=source.ROOT/'manifests/ot2606-evidence-001.kg-release.json'
PATHS=[
 'manifests/ot2606-evidence-001.freeze.json','manifests/ot2606-evidence-001.operations.json',
 'extractions/ot2606-evidence-001.json','assessments/ot2606-evidence-001.readiness.json',
 'kg/ot2606-evidence-001/records.ttl','kg/ot2606-evidence-001/provenance.ttl','kg/ot2606-evidence-001/record-identities.json',
 'manifests/mondo-pilot-001.kg-release.json','kg/mondo-pilot-001/records.ttl','kg/mondo-pilot-001/provenance.ttl',
 'ontology/dementiagraph-v.ttl','validation/m1_shapes.ttl','contracts/dementia-evidence-readiness.json',
 'tools/ot2606_source.py','tools/ot2606_assess.py','tools/ot2606_identity.py','tools/ot2606_rdf.py','tools/validate_ot2606.py','tools/ot2606_release.py',
 'tests/test_ot2606_source.py','tests/test_ot2606_identity.py','tests/test_ot2606_validation.py','tests/test_ot2606_release.py']

def build():
    results=validation.validate();mg=mondo.load_graph();mondo.semantic(mg)
    ot=structural.load_graph(rdf.OUT/'records.ttl')+structural.load_graph(rdf.OUT/'provenance.ttl');union=mg+ot
    shacl,_,_=structural.validate_graph(union)
    source.require(shacl['result_counts']=={'Warning':2},'Unexpected combined SHACL result')
    sys.path.insert(0,str(source.ROOT/'tests'))
    from test_m1_owl_reasoning import reason,unexplained_additions
    schema=structural.load_graph(source.ROOT/'ontology/dementiagraph-v.ttl');closure,errors=reason(schema+union)
    unexpected=unexplained_additions(schema+union,closure)
    source.require(not errors and not unexpected,'Unexpected reasoning diagnostic/assertion')
    m=source.load(source.MANIFEST)
    return {'profile':'ot2606-bounded-kg-release-1','scope':'Eight historical OT evidence rows plus unchanged Mondo source slice; incomplete full corpus',
            'files':{p:source.sha((source.ROOT/p).read_bytes()) for p in PATHS},
            'sourceFiles':[{'name':f['name'],'bytes':f['bytes'],'sha256':f['sha256'],'url':f['url']} for f in m['files']],
            'dependencies':{p:version(p) for p in ['duckdb','rdflib','pyshacl','owlrl']},
            'ot':{k:v for k,v in results.items() if k!='answers'},
            'combined':{'resources':len(set(union.subjects())),'triples':len(union),'assertedGraphSha256':source.sha(rdf.common.serialize(union)),
                        'rawSHACLConforms':shacl['raw_shacl_conforms'],'structuralAcceptance':shacl['project_structural_acceptance'],'findings':shacl['result_counts'],
                        'owlInputTriples':len(schema+union),'owlClosureTriples':len(closure),'owlDiagnostics':errors,'unexpectedSubstantiveAssertions':len(unexpected)},
            'availability':source.load(source.ROOT/'assessments/ot2606-evidence-001.readiness.json')['slotCounts'],
            'interpretation':['No independent biomedical adjudication or efficacy result','No historical aggregate, query totals, ranks or mapping algorithm reconstruction','Q01-Q07 exposed design material; wider source-backed acceptance remains partial','Local grouping completeness is limited to its enumerated IDs','No mechanisms, clinical indications or populations invented','No equivalence between Mondo and source-scoped OT references asserted','M3-M8 not started; missing source contexts and later evaluation decisions remain'],
            'replay':'Provide unchanged external OT artifacts under OT2606_ARTIFACTS and Mondo artifacts under MONDO_PILOT_ARTIFACTS; run tools/ot2606_release.py verify. No network.'}

def verify(path=MANIFEST):
    expected=build();source.require(source.serialize(expected)==Path(path).read_bytes(),'Release manifest/replay differs');return expected
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('operation',choices=['build','verify']);a=p.parse_args()
    if a.operation=='build':
        value=build()
        with MANIFEST.open('xb') as out:out.write(source.serialize(value))
    result=verify();print(source.serialize(result['combined']).decode())
