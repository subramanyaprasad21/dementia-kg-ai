"""Source-fidelity checks and RDF-only bounded answers, separate from clinical truth."""
from collections import Counter
from rdflib import Graph,URIRef
from rdflib.namespace import RDF,OWL
import ot2606_source as source
import ot2606_rdf as rdf
import validate_m1_fixtures as structural
D=rdf.DKG

def one(g,s,p):
    values=list(g.objects(s,p));source.require(len(values)==1,'Expected one RDF value for '+str(p));return values[0]
def answers(g):
    results={}
    for e in g.subjects(RDF.type,D.EvidenceOccurrence):
        ident=str(one(g,e,D.sourceRecordIdentifier));source.require(ident not in results,'Duplicate source occurrence')
        maps=list(g.subjects(D.mappingContext,e));source.require(len(maps)==1,'Missing/ambiguous mapping context')
        mapping=maps[0];dest=one(g,mapping,D.reportedDestination);source.require((dest,RDF.type,D.DiseaseConceptReference) in g,'Wrong destination type')
        original=list(g.objects(mapping,D.mappingInput));source.require(len(original)<=1,'Ambiguous original reference')
        target=one(g,e,D.hasTarget);snapshot=one(g,e,D.inSnapshot)
        source.require(str(one(g,snapshot,D.snapshotVersion))=='26.06','Incompatible snapshot')
        source.require(one(g,mapping,D.inSnapshot)==snapshot and one(g,dest,D.inSnapshot)==snapshot,'Incompatible mapping context')
        item={'targetId':str(one(g,target,D.externalIdentifier)),'datasource':str(one(g,e,D.evidenceSourceType)),'normalized':str(one(g,dest,D.externalIdentifier)),
              'originalIdentifier':None,'originalLabel':None,'publications':sorted(str(one(g,p,D.externalIdentifier)) for p in g.objects(e,D.citesPublication)),
              'studyLocators':sorted(str(one(g,p,D.externalIdentifier)) for p in g.objects(e,D.refersToStudy)),
              'phases':sorted(str(v) for c in g.objects(e,D.contextRecord) if (c,RDF.type,D.StudyRecord) in g for v in g.objects(c,D.trialPhaseText)),
              'mappingStatus':str(one(g,mapping,D.mappingStatus))}
        if original:
            source.require(one(g,original[0],D.inSnapshot)==snapshot,'Incompatible original source context')
            ids=list(g.objects(original[0],D.externalIdentifier));labels=list(g.objects(original[0],D.sourceLabel));source.require(len(ids)<=1 and len(labels)<=1,'Ambiguous original values')
            item['originalIdentifier']=str(ids[0]) if ids else None;item['originalLabel']=str(labels[0]) if labels else None
        results[ident]=item
    return results

def semantic(g,data=None):
    data=source.verify() if data is None else data
    actual=answers(g);source.require(len(actual)==8,'Missing/extra evidence')
    for rec in data['records']:
        row=source.untyped(rec['sourceValues']);a=actual[rec['id']]
        expected={'targetId':row['targetId'],'datasource':row['datasourceId'],'normalized':row['diseaseId'],'originalIdentifier':row.get('diseaseFromSourceId'),'originalLabel':row.get('diseaseFromSource'),
                  'publications':sorted(p for p in row['literature'] if p is not None),'studyLocators':[row['clinicalReportId']] if 'clinicalReportId' in row else [],'phases':[row['clinicalStage']] if 'clinicalStage' in row else [],'mappingStatus':'validity-unreviewed'}
        source.require(a==expected,'RDF answer differs from exact source values: '+rec['id'])
    schema=structural.load_graph(source.ROOT/'ontology/dementiagraph-v.ttl');allowed=set(schema.subjects(RDF.type,OWL.ObjectProperty))|set(schema.subjects(RDF.type,OWL.DatatypeProperty))|{RDF.type}
    source.require(set(g.predicates())<=allowed,'Unsupported schema predicate')
    for kind in ['MechanismRecord','ClinicalIndicationRecord','PopulationScope']:
        source.require(not list(g.subjects(RDF.type,D[kind])),'Unavailable source context promoted')
    source.require(not list(g.triples((None,D.aggregateScore,None))),'Fabricated historical aggregate')
    expected,_,_=rdf.build(data);expected+=rdf.provenance(data)
    source.require(set(g)==set(expected),'Source/identity/provenance fidelity differs')
    return actual

def validate():
    rdf.verify();g=structural.load_graph(rdf.OUT/'records.ttl')+structural.load_graph(rdf.OUT/'provenance.ttl')
    result=semantic(g);v,_,_=structural.validate_graph(g)
    source.require(v['result_counts']=={'Warning':2},'Unexpected structural findings')
    source.require(all(x['source_shape'].endswith('RecordedSourceOmission') for x in v['results']),'Unexpected warnings')
    return {'resources':len(set(g.subjects())),'triples':len(g),'inventory':dict(Counter(str(t).split('#')[-1] for t in g.objects(None,RDF.type))),
            'rawSHACLConforms':v['raw_shacl_conforms'],'structuralAcceptance':v['project_structural_acceptance'],'findings':v['result_counts'],
            'answers':result,'scope':'Eight-row source fidelity; broader Q01-Q07 remains partial. No biomedical adjudication or full-corpus completion.'}

if __name__=='__main__':print(source.serialize(validate()).decode())
