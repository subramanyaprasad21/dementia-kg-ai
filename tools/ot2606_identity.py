"""Bounded successor identities for verified historical OT rows and local operations."""
import re
from rdflib import Graph, URIRef
from rdflib.namespace import RDF, OWL
import ot2606_source as source
import m1_fixture_identity as core
PROFILE='m2-evidence-record-1'
SOURCE_KINDS={'SourceSnapshot','DiseaseConceptReference','EvidenceOccurrence','MappingRecord','StudyRecord'}
OP_KINDS={'SelectionContext','SelectionMembership','DiseaseTargetAssociation','DerivedStatement','MissingnessRecord'}
DKG=core.BASE+'ontology#'

def receipt(kind,origin,inputs,payload):
    source.require(kind in SOURCE_KINDS|OP_KINDS,'Inactive record kind')
    source.require(origin==('live-source-derived' if kind in SOURCE_KINDS else 'project-operation'),'Unsupported origin')
    if kind=='SourceSnapshot':
        source.require(set(inputs)=={'descriptionId','edition','datasource','locator'},'Snapshot keys')
        source.require(all(isinstance(x,str) and x for x in inputs.values()),'Missing snapshot lineage')
        source.require(inputs['edition']=='26.06','Wrong edition')
        source.require(inputs['descriptionId'].startswith(source.BASE+source.DESCRIPTION+'/'),'Wrong description profile')
        values=dict(inputs)
    else:values=core.normalize_inputs(kind,inputs)
    if kind=='EvidenceOccurrence':source.require(values['sourceRecordId'] is not None,'Missing source evidence ID')
    if kind=='DiseaseTargetAssociation':source.require(values['originRole']=='project-grouping','Source aggregates not available')
    if kind=='DiseaseConceptReference':source.require(values['role'] in {'original','normalized','project-anchor'},'Unsupported role')
    payload=core.normalized_payload(payload)
    schema=Graph().parse(core.ROOT/'ontology/dementiagraph-v.ttl',format='turtle')
    props=set(schema.subjects(RDF.type,OWL.ObjectProperty))|set(schema.subjects(RDF.type,OWL.DatatypeProperty))
    for a in payload:
        iri='http://www.w3.org/ns/prov#wasDerivedFrom' if a['field']=='prov:wasDerivedFrom' else DKG+a['field']
        source.require(URIRef(iri) in props,'Unsupported property')
    return {'profile':PROFILE,'kind':kind,'origin':origin,'inputs':values,'contentRevision':None if kind=='SelectionMembership' else source.sha(core.canonical(payload))}

class Registry:
    def __init__(self,extraction):
        self.entries={};self.descriptions={r['description']['id']:r for r in extraction['records']}
        for r in extraction['records']:
            desc=r['description'];source.require(desc['id']==source.identify(source.DESCRIPTION,desc['receipt']),'Corrupt description identity')
            source.require(desc['receipt']['contentSha256']==source.sha(core.canonical(r['sourceValues'])),'Description payload mismatch')
    def add(self,kind,inputs,payload,origin=None,iri=None):
        if kind in {'Target','Publication','Study','Drug'}:
            rec=core.receipt(kind,'referent',inputs,payload)
        else:
            origin=origin or ('live-source-derived' if kind in SOURCE_KINDS else 'project-operation')
            rec=receipt(kind,origin,inputs,payload)
            if kind=='SourceSnapshot':
                row=self.descriptions.get(inputs['descriptionId']);source.require(row is not None,'Unverified source description')
                source.require(inputs['edition']==row['description']['receipt']['edition'] and inputs['datasource']==row['description']['receipt']['datasource'] and inputs['locator']==core.canonical(row['lineage']['locator']).decode(),'Snapshot/source mismatch')
            elif 'snapshotKey' in inputs:
                entry=self.entries.get(inputs['snapshotKey']);source.require(entry and entry['receipt']['profile']==PROFILE and entry['receipt']['kind']=='SourceSnapshot','Unregistered live snapshot; M1 reuse forbidden')
                source.require(inputs['locator']==entry['receipt']['inputs']['locator'],'Source row locator mismatch')
        for key,val in rec['inputs'].items():
            if key.endswith('Key') or key.endswith('Keys'):
                for link in val if isinstance(val,list) else [] if val is None else [val]:source.require(link in self.entries or (key=='observationKey' and link in self.descriptions),'Unregistered identity participant: '+key)
        computed=core.identify(rec);source.require(iri is None or iri==computed,'Conflicting supplied identity')
        entry={'iri':computed,'receipt':rec,'payload':core.normalized_payload(payload)}
        source.require(computed not in self.entries or self.entries[computed]==entry,'Immutable identity collision')
        self.entries[computed]=entry
        return computed
