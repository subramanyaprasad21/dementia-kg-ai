"""Field-level comparison to pinned audit; no adjudication or audit modification."""
from collections import Counter
import ot2606_source as source
ROOT=source.ROOT
OUTPUT=ROOT/'assessments/ot2606-evidence-001.readiness.json'

def assess(extraction):
    spec=source.load(ROOT/'fixtures/m1/audit_fixture_spec.json');byalias={r['alias']:r for r in spec['records']}
    rows={r['id']:source.untyped(r['sourceValues']) for r in extraction['records']}
    checks=[]
    def compare(alias,field,expected,actual,basis):
        status='VERIFIED' if actual==expected else 'PARTIALLY VERIFIED' if expected is None else 'DISCREPANT'
        checks.append({'auditRecord':alias,'field':field,'expected':source.typed(expected),'actual':source.typed(actual),'status':status,'basis':basis})
    for audit in spec['records']:
        if audit['kind']!='EvidenceOccurrence':continue
        ident=audit['inputs']['sourceRecordId'];row=rows[ident];alias=audit['alias'];basis={'recordId':ident,'file':next(x['lineage']['file'] for x in extraction['records'] if x['id']==ident),'auditSpec':'fixtures/m1/audit_fixture_spec.json'}
        compare(alias,'id',ident,row['id'],basis)
        for assertion in audit['assertions']:
            if assertion['field']=='hasTarget':compare(alias,'targetId',byalias[assertion['value'][1:]]['inputs']['identifier'],row['targetId'],basis)
            if assertion['field']=='evidenceSourceType':compare(alias,'datasourceId',assertion['value'],row['datasourceId'],basis)
        citations=[byalias[a['value'][1:]]['inputs']['identifier'] for a in audit['assertions'] if a['field']=='citesPublication']
        compare(alias,'literature-non-null-locators',sorted(citations),sorted(x for x in row['literature'] if x is not None),basis)
        mapping=next(r for r in spec['records'] if r['kind']=='MappingRecord' and r['inputs']['occurrenceKey']=='@'+alias)
        inputs=mapping['inputs']
        for reference,role in [(inputs['inputKey'],'original'),*( (v,'normalized') for v in inputs['destinationKeys'])]:
            if reference is None:continue
            ref=byalias[reference[1:]]['inputs']
            identifier='diseaseFromSourceId' if role=='original' else 'diseaseId'
            compare(alias,identifier,ref['identifier'],row.get(identifier),basis)
            if role=='original' and ref['label'] is not None:compare(alias,'diseaseFromSource',ref['label'],row.get('diseaseFromSource'),basis)
        if inputs['panel'] is not None:compare(alias,'studyId',inputs['panel'],row.get('studyId'),basis)
        if row['datasourceId']=='clinical_precedence':
            for key,value in [('clinicalReportId','nct00594737'),('drugId','CHEMBL807'),('clinicalStage','PHASE_3')]:compare(alias,key,value,row.get(key),basis)
    contract=source.load(ROOT/'contracts/dementia-evidence-readiness.json');slots=[]
    for slot in contract['sourceSlots']:
        status='UNAVAILABLE';detail='No separately recovered supporting record; unchanged audit is not source reproduction.';support=[]
        if slot['id']=='mondo':status='VERIFIED';detail='Reuse unchanged frozen Mondo release.'
        elif slot['kind']=='evidence':status='VERIFIED';support=[slot['locator']];detail='Exact historical row only; no historical query, aggregate or clinical validation.'
        elif slot['kind'] in ('Target','Drug','Publication'):
            key={'Target':'targetId','Drug':'drugId','Publication':'literature'}[slot['kind']]
            support=[i for i,r in rows.items() if slot['locator'] in (r.get(key,[]) if key=='literature' else [r.get(key)])]
            if support:status='PARTIALLY VERIFIED';detail='Authority-qualified locator observed; labels, source metadata and article interpretation not independently acquired.'
        elif slot['kind']=='panel-gene':
            panel,gene=slot['locator'].split('/');support=[i for i,r in rows.items() if r.get('studyId')==panel and r['targetFromSourceId']==gene]
            if support:status='PARTIALLY VERIFIED';detail='OT studyId/gene reference recovered; historical PanelApp edition and original panel/gene record unavailable.'
        elif slot['id']=='NCT00594737':status='PARTIALLY VERIFIED';support=[i for i,r in rows.items() if r.get('clinicalReportId')=='nct00594737'];detail='Lowercase source locator recovered; registry record, population, status and results not acquired.'
        elif slot['id'] in ('source-composition','clinical-linkage'):status='PARTIALLY VERIFIED';detail='Only row datasource/datatype or shared report/drug/stage fields recovered; upstream transformation and joins not reconstructed.'
        elif slot['id'] in ('PMC7852392','PMC6742707'):status='PARTIALLY VERIFIED';detail='OT text-mining snippets and offsets recovered; not an independently acquired full-text article or adjudicated passage.'
        slots.append({'id':slot['id'],'kind':slot['kind'],'status':status,'scope':detail,'supportingEvidenceIds':support})
    states={i:{k:source.field(r,k) for k in ['diseaseFromSourceId','diseaseFromSource','diseaseFromSourceMappedId','diseaseId','studyId','clinicalReportId','trialWhyStopped','literature','textMiningSentences']} for i,r in rows.items()}
    return {'profile':'ot2606-readiness-assessment-1','extractionSha256':source.sha(source.serialize(extraction)),
            'requiredSlotContractSha256':source.sha((ROOT/'contracts/dementia-evidence-readiness.json').read_bytes()),'slots':slots,'slotCounts':dict(Counter(s['status'] for s in slots)),
            'auditComparisons':checks,'comparisonCounts':dict(Counter(c['status'] for c in checks)), 'fieldStates':states,
            'questions':{q:{'status':'PARTIALLY VERIFIED','fullSourceBackedAcceptance':False,'reason':'Recovered rows support bounded field checks only. Retain separate panel, mechanism, indication, selection, aggregate, registry and primary-publication obligations.'} for q in contract['questionRequirements']},
            'normalization':'No source-value transformations. Colon versus underscore and abbreviated labels are retained and explicitly flagged; no source mappings repaired.',
            'alignment':'Only exact source-scoped participant/reference resolution. No semantic equivalence or source-description merge.',
            'auditLimit':'Entire historical audit NOT reproduced. Previously unrecorded source snippets are newly recovered OT material, not retrospective audit inspection.'}

if __name__=='__main__':
    result=assess(source.verify())
    with OUTPUT.open('xb') as out:out.write(source.serialize(result))
    print(result['slotCounts'],result['comparisonCounts'])
