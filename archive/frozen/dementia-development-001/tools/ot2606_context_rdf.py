"""Approved context identity successor; finite mechanisms/indications, no new schema."""
from pathlib import Path
from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDF, XSD, OWL
import ot2606_context as context
import ot2606_source as source
import m1_fixture_identity as core
import m2_mondo_rdf as common
A=common.assertion
D=common.DKG
P=common.PROV
PROFILE='m2-context-record-1'
DESCRIPTION='m2-ot-context-description-1'
OUT=source.ROOT/'kg/ot2606-context-001'
KINDS={'SourceSnapshot','DiseaseConceptReference','MechanismRecord','ClinicalIndicationRecord'}
TARGETS={'CHEMBL807':{'ENSG00000176884','ENSG00000116032'},'CHEMBL4298021':{'ENSG00000186868'},'CHEMBL3990042':{'ENSG00000186868'},'CHEMBL3833321':{'ENSG00000142192'}}

def text(x):return core.canonical(x).decode()

def describe(record, schema):
    loc=record['lineage']
    receipt=dict(profile=DESCRIPTION,provider='Open Targets Platform',edition='26.06',table=record['partition'],
                 schema=[[c[0],c[1]] for c in schema],locator=dict(url=loc['url'],fileSha256=loc['fileSha256'],fileRowNumber=str(loc['fileRowNumber'])),
                 contentSha256=source.sha(core.canonical(record['sourceValues'])))
    source.require(receipt['contentSha256']==record['sourceValueSha256'],'Changed source projection')
    return source.identify(DESCRIPTION,receipt),receipt

class Registry:
    def __init__(self):self.entries={};self.descriptions={}
    def add(self,kind,inputs,payload):
        payload=core.normalized_payload(payload)
        if kind in {'Drug','Target','Publication'}:receipt=core.receipt(kind,'referent',inputs,payload)
        else:
            source.require(kind in KINDS,'Unsupported context kind')
            if kind=='SourceSnapshot':
                source.require(set(inputs)=={'descriptionId','edition','datasource','locator'} and inputs['edition']=='26.06','Invalid snapshot inputs')
                source.require(inputs['descriptionId'].startswith(source.BASE+DESCRIPTION+'/'),'Wrong source description profile')
                desc=self.descriptions.get(inputs['descriptionId'])
                source.require(desc is not None and source.identify(DESCRIPTION,desc)==inputs['descriptionId'],'Unverified source description')
                source.require(inputs['datasource']==desc['table'] and inputs['locator']==text(desc['locator']),'Snapshot/description mismatch')
                values=inputs
            else:
                values=core.normalize_inputs(kind,inputs)
                source.require(values['snapshotKey'] in self.entries and self.entries[values['snapshotKey']]['receipt']['kind']=='SourceSnapshot','Unregistered context snapshot')
                source.require(values['locator']==self.entries[values['snapshotKey']]['receipt']['inputs']['locator'],'Conflicting row locator')
                for key,value in values.items():
                    if key.endswith('Key'):source.require(value in self.entries,'Unregistered participant')
            receipt=dict(profile=PROFILE,kind=kind,origin='live-source-derived',inputs=values,contentRevision=source.sha(core.canonical(payload)))
        iri=core.identify(receipt);entry=dict(iri=iri,receipt=receipt,payload=payload)
        source.require(iri not in self.entries or self.entries[iri]==entry,'Immutable collision')
        self.entries[iri]=entry;return iri

def build(data=None):
    if data is None:
        data=context.extract()
        source.require(source.serialize(data)==(source.ROOT/'extractions/ot2606-context-001.json').read_bytes(),'Changed frozen context')
    source.require(data['edition']=='26.06','Wrong edition')
    reg=Registry();provenance=Graph();descriptions={}
    schema={s['file']:s['schema'] for s in data['schemas']}
    def referent(kind,authority,ident):return reg.add(kind,dict(authority=authority,identifier=ident,disambiguator=None),[A('identifierAuthority',authority),A('externalIdentifier',ident)])
    for record in data['records']:
        if record['partition']=='disease':continue # kept as selection input, not automatically expanded RDF
        row=source.untyped(record['sourceValues']);desc,receipt=describe(record,schema[record['lineage']['file']]);descriptions[desc]=receipt;reg.descriptions[desc]=receipt
        locator=text(receipt['locator']);raw=source.BASE+'raw-file/'+record['lineage']['fileSha256']
        for iri in [desc,raw]:provenance.add((URIRef(iri),RDF.type,P.Entity))
        provenance.add((URIRef(desc),D.sourceText,Literal(text(record['sourceValues']),datatype=XSD.string)))
        provenance.add((URIRef(desc),D.sourceLocator,Literal(locator,datatype=XSD.string)))
        provenance.add((URIRef(desc),P.wasDerivedFrom,URIRef(raw)))
        provenance.add((URIRef(raw),D.sourceLocator,Literal(record['lineage']['url'],datatype=XSD.string)))
        provenance.add((URIRef(raw),D.sourceText,Literal(text({'fileSha256':record['lineage']['fileSha256'],'ledgerSha256':record['lineage']['ledgerSha256'],'captureIndex':str(record['lineage']['captureRecordIndex']),'permission':'CC0-1.0','attribution':'Open Targets Platform'}),datatype=XSD.string)))
        snapshot=reg.add('SourceSnapshot',dict(descriptionId=desc,edition='26.06',datasource=record['partition'],locator=locator),[A('sourceAuthority','Open Targets Platform / '+record['partition']),A('snapshotVersion','26.06'),A('sourceLocator',locator),A('artifactDescription',text(receipt)),A('prov:wasDerivedFrom',desc,True)])
        base=[A('inSnapshot',snapshot,True),A('sourceLocator',locator),A('contextRecord',desc,True)]
        if record['partition']=='drug_mechanism_of_action':
            for drugid in sorted(set(row['chemblIds']) & set(TARGETS)):
                drug=referent('Drug','CHEMBL',drugid)
                for targetid in sorted(set(row['targets']) & TARGETS[drugid]):
                    target=referent('Target','ENSEMBL',targetid)
                    pubs=[referent('Publication','PMID',p) for ref in row['references'] if ref['source']=='PubMed' for p in ref['ids']]
                    reg.add('MechanismRecord',dict(snapshotKey=snapshot,locator=locator,drugKey=drug,targetKey=target),base+[A('hasDrug',drug,True),A('hasTarget',target,True),A('sourceText',row['mechanismOfAction']),A('limitationText','Source gene-indexed mechanism; shared original row and molecular target context retained. No efficacy, gene-wide action or independent confirmation inferred.')]+[A('citesPublication',p,True) for p in pubs])
        else:
            drug=referent('Drug','CHEMBL',row['drugId'])
            disease=reg.add('DiseaseConceptReference',dict(snapshotKey=snapshot,locator=locator,role='normalized',authority='MONDO',identifier=row['diseaseId'],label=None),[A('inSnapshot',snapshot,True),A('sourceLocator',locator),A('identifierAuthority','MONDO'),A('externalIdentifier',row['diseaseId']),A('limitationText','Source normalized indication identifier; original condition label absent. No equivalence asserted.')])
            reg.add('ClinicalIndicationRecord',dict(snapshotKey=snapshot,locator=locator,drugKey=drug,diseaseKey=disease),base+[A('hasDrug',drug,True),A('hasDiseaseReference',disease,True),A('sourceRecordIdentifier',row['id']),A('trialPhaseText',row['maxClinicalStage']),A('limitationText','Source maximum indication stage only. Report locators retained in the linked source description; registry population/status and efficacy not acquired.')])
    graph=common.graph_of(reg)+provenance
    return graph,dict(profile=PROFILE,descriptions=descriptions,records=reg.entries)

def outputs():
    graph,receipts=build()
    return {'records.ttl':common.serialize(graph),'record-identities.json':source.serialize(receipts)}

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('operation',choices=['build','verify']);a=p.parse_args()
    expected=outputs()
    if a.operation=='build':
        OUT.mkdir(parents=True,exist_ok=False)
        for name,b in expected.items():(OUT/name).write_bytes(b)
    for name,b in expected.items():source.require((OUT/name).read_bytes()==b,'Context RDF replay mismatch')
    print({name:source.sha(b) for name,b in expected.items()})
