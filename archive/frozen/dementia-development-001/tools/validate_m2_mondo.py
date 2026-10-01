"""Bounded Mondo RDF fidelity, semantic checks and unchanged M1 SHACL."""
import json
from collections import Counter
from rdflib import Graph, URIRef
from rdflib.namespace import RDF, OWL
import m2_mondo_rdf as rdf
import m2_mondo_provenance as provenance
import validate_m1_fixtures as structural


def load_graph():
    # Verify original source artifacts and exact record/receipt/provenance replay.
    rdf.verify(); provenance.verify()
    graph=structural.load_graph(rdf.OUT/'records.ttl')
    graph+=structural.load_graph(provenance.OUT)
    return graph


def one(graph, subject, predicate):
    values=list(graph.objects(subject,predicate))
    rdf.identity.require(len(values)==1, 'Expected one '+str(predicate))
    return values[0]


def semantic(graph):
    data,freeze=rdf.load()
    counts=Counter(str(t).split('#')[-1] for _,t in graph.subject_objects(RDF.type))
    rdf.identity.require(counts==dict(SourceSnapshot=13,DiseaseConceptReference=13,HierarchyStep=5,Entity=29), 'Record inventory differs')
    allowed_schema=structural.load_graph(rdf.ROOT/'ontology/dementiagraph-v.ttl')
    allowed=set(allowed_schema.subjects(RDF.type,OWL.ObjectProperty))|set(allowed_schema.subjects(RDF.type,OWL.DatatypeProperty))|{RDF.type}
    rdf.identity.require(set(graph.predicates())<=allowed, 'Unsupported predicate/inference')
    pairs=[]
    for step in graph.subjects(RDF.type,rdf.DKG.HierarchyStep):
        ids=[]
        snapshots=[]
        for field in ('childReference','parentReference'):
            ref=one(graph,step,rdf.DKG[field])
            rdf.identity.require((ref,RDF.type,rdf.DKG.DiseaseConceptReference) in graph, 'Endpoint type')
            authority=str(one(graph,ref,rdf.DKG.identifierAuthority))
            identifier=str(one(graph,ref,rdf.DKG.externalIdentifier))
            rdf.identity.require(authority=='MONDO', 'Endpoint authority')
            snapshot=one(graph,ref,rdf.DKG.inSnapshot)
            rdf.identity.require(str(one(graph,snapshot,rdf.DKG.snapshotVersion))==freeze['sourceContext']['edition'], 'Incompatible snapshot edition')
            ids.append(identifier);snapshots.append(snapshot)
        rdf.identity.require(one(graph,step,rdf.DKG.inSnapshot)==snapshots[1], 'Parent response context lost')
        pair=tuple(ids);pairs.append(pair)
        rdf.identity.require(pair in rdf.extract.freeze.PARENTS, 'Unapproved directed assertion')
        original=next(a for a in data['parentAssertions'] if (rdf.lexical(a['child'],'obo_id'),rdf.lexical(a['parent'],'obo_id'))==pair)
        rdf.identity.require(str(one(graph,step,rdf.DKG.sourceLocator))==rdf.canonical(original['lineage']['sourceRecordLocator']), 'Source row locator differs')
    rdf.identity.require(sorted(pairs)==sorted(rdf.extract.freeze.PARENTS), 'Missing or duplicated parent assertion')
    ids={str(o) for o in graph.objects(None,rdf.DKG.externalIdentifier)}
    rdf.identity.require(ids==set(rdf.extract.freeze.TERMS), 'Concept scope differs')
    # Full assertion fidelity is stronger than structural conformance; it also
    # protects annotations, identity payloads, qualifiers, receipt and capture edges.
    expected,_=rdf.build();expected+=provenance.build()
    rdf.identity.require(set(graph)==set(expected), 'Source/identity/provenance fidelity differs')
    return dict(concepts=8, scopedReferences=13, acceptedParents=sorted(pairs), excludedRawRows=6,
                interpretation='Qualified OLS navigation only; no equivalence, inferred closure or biomedical validation')


def validate(graph=None):
    graph=load_graph() if graph is None else graph
    result=semantic(graph)
    summary,_,_=structural.validate_graph(graph)
    rdf.identity.require(summary['raw_shacl_conforms'] and not summary['results'], 'Unexpected structural finding')
    return dict(resources=len(set(graph.subjects())),triples=len(graph),semantic=result,
                raw_shacl_conforms=summary['raw_shacl_conforms'],result_counts=summary['result_counts'],
                project_acceptance='bounded-Mondo-source-fidelity-pass',configuration=summary['configuration'])


if __name__=='__main__':print(json.dumps(validate(),indent=2,sort_keys=True))
