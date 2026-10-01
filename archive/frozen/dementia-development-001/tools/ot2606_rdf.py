"""Finite source-backed OT RDF projection using unchanged ontology vocabulary."""
import argparse
from collections import defaultdict
from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDF, XSD
import ot2606_source as source
import ot2606_identity as identity
import m2_mondo_rdf as common
A=common.assertion
DKG=common.DKG
PROV=common.PROV
OUT=source.ROOT/'kg/ot2606-evidence-001'

def text(v):return identity.core.canonical(v).decode()
def build(data=None):
    data=source.verify() if data is None else data
    operations=source.load(source.ROOT/'manifests/ot2606-evidence-001.operations.json')
    reg=identity.Registry(data);anchors={};info={}
    def referent(kind,authority,identifier):
        return reg.add(kind,dict(authority=authority,identifier=identifier,disambiguator=None),[A('identifierAuthority',authority),A('externalIdentifier',identifier)])
    for rec in data['records']:
        row=source.untyped(rec['sourceValues']);desc=rec['description']['id'];locator=text(rec['lineage']['locator'])
        snapshot=reg.add('SourceSnapshot',dict(descriptionId=desc,edition='26.06',datasource=row['datasourceId'],locator=locator),[
            A('sourceAuthority','Open Targets Platform / '+row['datasourceId']),A('snapshotVersion','26.06'),A('sourceLocator',locator),
            A('artifactDescription',text(rec['description']['receipt'])),A('prov:wasDerivedFrom',desc,True)])
        def disease(role,identifier,label,authority):
            inputs=dict(snapshotKey=snapshot,locator=locator,role=role,authority=authority,identifier=identifier,label=label)
            payload=[A('inSnapshot',snapshot,True),A('sourceLocator',locator)]
            if identifier is not None:payload.extend([A('identifierAuthority',authority),A('externalIdentifier',identifier)])
            if label is not None:payload.append(A('sourceLabel',label))
            if label is None or identifier is None:payload.append(A('limitationText','Only observed source identity fields retained; absent label/identifier/authority is not inferred from normalized values.'))
            return reg.add('DiseaseConceptReference',inputs,payload)
        normalized=disease('normalized',row['diseaseId'],None,'MONDO')
        original=None
        if row.get('diseaseFromSourceId') is not None or row.get('diseaseFromSource') is not None:
            identifier=row.get('diseaseFromSourceId');authority='OMIM' if identifier and identifier.startswith('OMIM:') else None
            source.require(identifier is None or authority,'Unresolved source authority')
            original=disease('original',identifier,row.get('diseaseFromSource'),authority)
        target=referent('Target','ENSEMBL',row['targetId'])
        pubs=[referent('Publication','PMID',p) for p in row['literature'] if p is not None]
        context=[];study=None
        if row['datasourceId']=='clinical_precedence':
            study=referent('Study','NCT',row['clinicalReportId'])
            report=reg.add('StudyRecord',dict(studyKey=study,snapshotKey=snapshot,locator=locator,arm=None,sourceDate=None),[
                A('inSnapshot',snapshot,True),A('sourceLocator',locator),A('refersToStudy',study,True),A('trialPhaseText',row['clinicalStage']),
                A('contextRecord',desc,True),A('limitationText','OT clinical-report context only; arm and registry-version date absent. studyStartDate/publicationDate are not status dates. No acquired population, outcome, approval or efficacy claim.')])
            context.append(report)
        payload=[A('inSnapshot',snapshot,True),A('sourceLocator',locator),A('sourceRecordIdentifier',row['id']),A('evidenceSourceType',row['datasourceId']),A('hasTarget',target,True),A('contextRecord',desc,True)]
        payload += [A('citesPublication',p,True) for p in pubs]+[A('contextRecord',p,True) for p in context]
        if study:payload.append(A('refersToStudy',study,True))
        occurrence=reg.add('EvidenceOccurrence',dict(snapshotKey=snapshot,locator=locator,sourceRecordId=row['id']),payload)
        mappingPayload=[A('inSnapshot',snapshot,True),A('sourceLocator',locator),A('mappingContext',occurrence,True),A('reportedDestination',normalized,True),A('mappingStatus','validity-unreviewed'),A('contextRecord',desc,True),
                        A('limitationText','Source-reported assignment only. Upstream method, methodVersion and execution unavailable; no reported candidate inventory or biomedical equivalence. studyId is a panel locator, not its historical edition.')]
        if original:mappingPayload.append(A('mappingInput',original,True))
        mapping=reg.add('MappingRecord',dict(snapshotKey=snapshot,locator=locator,occurrenceKey=occurrence,panel=row.get('studyId'),inputKey=original,destinationKeys=[normalized],candidateKeys=[],method=None,methodVersion=None,execution=None),mappingPayload)
        if original is None:
            scope='Original disease input columns absent in the historical Europe PMC Parquet schema; not evidence of biological absence or a reproduced GraphQL null.'
            reg.add('MissingnessRecord',dict(ownerKey=mapping,expectedField='field:mappingInput',observationKey=desc,reason='source-omission',scope=scope),[
                A('aboutRecord',mapping,True),A('expectedField','field:mappingInput'),A('observationContext',desc,True),A('missingnessReason','source-omission'),A('rationale',scope)])
        anchor=None
        if row['diseaseId'] in {'MONDO_0004975','MONDO_0017276'}:
            if row['diseaseId'] not in anchors:anchors[row['diseaseId']]=disease('project-anchor',row['diseaseId'],None,'MONDO')
            anchor=anchors[row['diseaseId']]
        info[row['id']]=dict(row=row,snapshot=snapshot,normalized=normalized,original=original,target=target,occurrence=occurrence,mapping=mapping,anchor=anchor,study=study)
    # This is the actual local fixed-ID operation. It does not reproduce an OT query.
    for destination in ['MONDO_0004975','MONDO_0017276']:
        members=[v for v in info.values() if v['row']['diseaseId']==destination];anchor=members[0]['anchor'];snapshots=sorted({v['snapshot'] for v in members});ids=sorted(v['row']['id'] for v in members)
        scope='Only the enumerated recovered IDs with exact normalized '+destination+' in OT 26.06; not complete disease coverage or historical rankings.'
        filters=text({'recipe':'fixed-ID exact destination selection','variables':text({'ids':ids,'diseaseId':destination}),'pagination':'not-applicable','sort':'id','limit':str(len(ids)),'defaults':'none'})
        context=reg.add('SelectionContext',dict(execution='ot2606-evidence-001/2',anchorKey=anchor,snapshotKeys=snapshots,selectionMode='direct-only',filters=filters,method='fixed-id-local-selection',methodVersion='1',scope=scope),[
            dict(A('observedAt',operations['selection']['observedAt']),datatype=str(XSD.dateTime)),A('queryAnchor',anchor,True),A('selectionMode','direct-only'),A('filterSpecification',filters),A('operationMethod','fixed-id-local-selection'),A('methodVersion','1'),A('executionReference','ot2606-evidence-001/2'),A('scopeText',scope),A('completenessStatus','complete-for-declared-scope')]+[A('inSnapshot',s,True) for s in snapshots])
        grouped=defaultdict(list)
        for v in members:
            reg.add('SelectionMembership',dict(occurrenceKey=v['occurrence'],contextKey=context),[A('selectedOccurrence',v['occurrence'],True),A('inSelectionContext',context,True),A('inclusionKind','exact-anchor'),A('limitationText',scope)])
            grouped[v['target']].append(v['occurrence'])
        for target,occurrences in grouped.items():
            reg.add('DiseaseTargetAssociation',dict(originRole='project-grouping',execution='ot2606-evidence-001/2',diseaseKey=anchor,targetKey=target,method='fixed-id-local-grouping',methodVersion='1',occurrenceKeys=occurrences,selectionKeys=[context],scope=scope),[
                A('originRole','project-grouping'),A('hasTarget',target,True),A('hasDiseaseReference',anchor,True),A('inSelectionContext',context,True),A('operationMethod','fixed-id-local-grouping'),A('methodVersion','1'),A('scopeText',scope),A('limitationText','No historical source aggregate, score, rank or complete target intersection is claimed.')]+[A('prov:wasDerivedFrom',o,True) for o in occurrences])
    clinical=[v for v in info.values() if v['row']['datasourceId']=='clinical_precedence'];left,right=clinical
    source.require(left['study']==right['study'],'Shared-study comparison failed')
    scope='Compare only these two source clinicalReportId fields; no independence or efficacy inference.'
    reg.add('DerivedStatement',dict(execution='ot2606-evidence-001/3',method='exact-source-study-locator-comparison',methodVersion='1',inputKeys=[v['occurrence'] for v in clinical],subjectKey=left['occurrence'],comparatorKey=right['occurrence'],selectionKeys=[],scope=scope),[
        A('subjectRecord',left['occurrence'],True),A('comparatorRecord',right['occurrence'],True),A('sharedInput',left['study'],True),A('dependencyStatus','shared-source-established'),A('operationMethod','exact-source-study-locator-comparison'),A('methodVersion','1'),A('executionReference','ot2606-evidence-001/3'),A('scopeText',scope),A('completenessStatus','complete-for-declared-scope'),A('resultSummary','Both source rows reference nct00594737.'),A('rationale',scope)]+[A('prov:wasDerivedFrom',v['occurrence'],True) for v in clinical])
    return common.graph_of(reg),{'profile':identity.PROFILE,'extractionSha256':source.sha(source.serialize(data)),'records':reg.entries},info

def provenance(data=None):
    data=source.verify() if data is None else data;m=source.load(source.MANIFEST);graph=Graph()
    def entity(iri,payload):
        s=URIRef(iri);graph.add((s,RDF.type,PROV.Entity))
        for a in payload:graph.add((s,common.predicate(a['field']),URIRef(a['value']) if a['form']=='iri' else Literal(a['value'],datatype=XSD.string,normalize=False)))
    for f in m['files']:
        fileid=source.BASE+'raw-file/'+f['sha256']
        entity(fileid,[A('sourceLocator',f['url']),A('sourceText',text({'sha256':f['sha256'],'bytes':str(f['bytes']),'edition':'26.06','fileName':f['name'],'permissions':f['permissions']}))])
        entity(f['localReceiptId'],[A('sourceText',text(f['localReceipt'])),A('prov:wasDerivedFrom',fileid,True)]+[A('contextRecord',r['description']['id'],True) for r in data['records'] if r['lineage']['file']==f['name']])
    for r in data['records']:
        row=source.untyped(r['sourceValues']);payload=[A('sourceText',text(r['sourceValues'])),A('sourceLocator',text(r['lineage']['locator'])),A('prov:wasDerivedFrom',source.BASE+'raw-file/'+r['lineage']['fileSha256'],True)]
        payload += [A('sourceText',p['text']) for p in row.get('textMiningSentences',[])]
        payload.append(A('limitationText','Original OT row projection; snippets and offsets do not constitute independent article review. Nulls/absent columns/array order are retained in sourceText.'))
        entity(r['description']['id'],payload)
    return graph

def outputs():
    data=source.verify();graph,receipts,_=build(data)
    return {'records.ttl':common.serialize(graph),'record-identities.json':source.serialize(receipts),'provenance.ttl':common.serialize(provenance(data))}
def verify():
    expected=outputs()
    for name,b in expected.items():source.require((OUT/name).read_bytes()==b,'RDF/provenance replay differs: '+name)
    return expected
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('operation',choices=['build','verify']);a=p.parse_args()
    if a.operation=='build':
        OUT.mkdir(exist_ok=True,parents=True)
        for name,b in outputs().items():
            with (OUT/name).open('xb') as out:out.write(b)
    print({name:source.sha(b) for name,b in verify().items()})
