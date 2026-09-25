"""Offline review-dossier checks, not a historical export parser or ingestion API."""
import hashlib
import json
from pathlib import Path

CONTRACT=Path(__file__).resolve().parents[1]/'contracts/dementia-evidence-readiness.json'
STATES={'present','source-null','source-absent','unknown'}
CORE={'datasource','datatype','targetIdentifier','normalizedDiseaseIdentifier','sourceRecordLocator'}
ORIGINAL={'originalDiseaseIdentifier','originalDiseaseLabel'}
SPECIFIC={'europepmc':{'publicationReferences','extractionSpanAvailability'},
          'genomics_england':{'panelOrStudyReference','sourceTargetIdentifier','publicationReferenceAvailability'},
          'clinical_precedence':{'drugIdentifier','clinicalReportIdentifier','clinicalStageAvailability','publicationReferenceAvailability'}}
CONTEXT={'association','selection','mapping','mechanism-indication-clinical'}


def load_dossier(raw):
    def unique(pairs):
        out={}
        for k,v in pairs:
            if k in out:raise ValueError('Duplicate dossier key')
            out[k]=v
        return out
    return json.loads(raw,object_pairs_hook=unique)


def evaluate(dossier, artifacts):
    """artifacts is a map of local artifact names to bytes, supplied without I/O.

    The dossier records explicit manual review assertions; matching hashes cannot
    prove provider authenticity or biomedical truth. No raw response projection is
    executed, no source contract is approved and no identities are generated here.
    """
    blocked=[];partial=[];qualifications=[]
    scope='unclassified'
    def need(ok,reason):
        if not ok:blocked.append(reason)
    def proof(item, role):
        need(isinstance(item,dict),role+': malformed review')
        if not isinstance(item,dict):return
        if item.get('status')!='reviewed':
            blocked.append(role+': unresolved review');return
        need(bool(item.get('reviewer')) and bool(item.get('basis')),role+': missing review attribution')
        ref=item.get('artifact');raw=artifacts.get(ref)
        need(isinstance(raw,bytes),role+': missing artifact')
        if isinstance(raw,bytes):need(hashlib.sha256(raw).hexdigest()==item.get('sha256'),role+': digest mismatch')
    try:
        need(set(dossier)=={'profile','materialKind','release','schema','permissions','export','accounting','records','contexts'},'Wrong dossier keys')
        need(dossier['profile']=='historical-evidence-review-1','Wrong dossier profile')
        kind=dossier['materialKind'];need(kind in {'synthetic-control','provider-material'},'Unknown material kind')
        synthetic=kind=='synthetic-control';scope='synthetic-control-only' if synthetic else 'review-dossier-only'
        contract=json.loads(CONTRACT.read_bytes())
        evidence={s['locator']:s for s in contract['sourceSlots'] if s['kind']=='evidence'}
        expected={'CONTROL-E1','CONTROL-E2'} if synthetic else set(evidence)
        for key in ('release','schema','permissions','export'):proof(dossier[key],key)
        need(dossier['release'].get('edition')=='26.06','Incorrect or ambiguous release; no substitution')
        need(dossier['release'].get('binding')=='export-bound','Release label not bound to export')
        need(dossier['schema'].get('binding')=='historical-export','Current or unknown schema binding')
        rights=dossier['permissions']
        need(rights.get('retention')=='permitted' and rights.get('use')=='permitted','Unresolved use/retention permission')
        need(rights.get('redistribution') in {'permitted','restricted'},'Redistribution conditions unknown')
        need(bool(rights.get('attribution')),'Attribution requirements missing')
        if rights.get('redistribution')=='restricted':qualifications.append('No source redistribution authorized by this review')
        accounting=dossier['accounting']
        attempts=accounting['attempts']
        need(isinstance(attempts,list) and bool(attempts),'Missing or invalid attempt list')
        need(accounting['complete'] is True and accounting['automaticReset'] is False,'Incomplete accounting or budget reset')
        need(bool(accounting.get('batch')),'Batch identity missing')
        total=0
        for a in attempts:
            need(set(a)=={'kind','receivedBytes'},'Invalid attempt keys')
            need(a['kind'] in {'metadata','request','retry','redirect','unsuccessful'},'Unknown request category')
            n=a['receivedBytes'];need(type(n) is int and n>=0,'Invalid byte count')
            if type(n) is int and n>=0:total+=n
        need(len(attempts)<=100 and total<=10485760,'Protective budget exceeded')
        export_bytes=artifacts.get(dossier['export'].get('artifact'))
        if isinstance(export_bytes,bytes):need(total>=len(export_bytes),'Received-byte accounting smaller than retained export')
        need(accounting['stopReason'] in {'complete','request-limit','byte-limit','incomplete-response'},'Invalid stop status')
        if accounting['stopReason']!='complete':partial.append('Compliant stop: '+accounting['stopReason'])
        if not dossier['export'].get('complete',False):partial.append('Incomplete or truncated export: no acceptance of unverified rows')
        rows=dossier['records'];need(isinstance(rows,list),'Records must be a list')
        seen=set()
        for row in rows:
            identifier=row['id'];need(identifier not in seen,'Duplicate/ambiguous evidence ID');seen.add(identifier)
            need(identifier in expected,'Unexpected evidence ID: '+identifier)
            need(bool(row.get('locator')),'Missing record locator')
            if not synthetic and identifier in evidence:need(row['datasource']==evidence[identifier]['datasource'],'Conflicting datasource for named evidence')
            source=row['datasource'];need(source in SPECIFIC,'Unsupported evidence source')
            required=CORE|ORIGINAL|SPECIFIC.get(source,set())
            fields=row['fields'];need(isinstance(fields,dict),'Malformed field review')
            for field in sorted(required):
                item=fields.get(field)
                if item is None:
                    partial.append(identifier+': field review missing: '+field);continue
                need(set(item)=={'state','basis'},'Malformed field-state review')
                state=item['state'];need(state in STATES and bool(item['basis']),'Invalid field state/basis')
                if state=='unknown':partial.append(identifier+': unverified '+field)
                elif state in {'source-null','source-absent'}:
                    if field in CORE:partial.append(identifier+': required value unavailable: '+field)
                    else:qualifications.append(identifier+': '+field+' '+state)
            need(row.get('originalNormalizedSeparate') is True,'Original and normalized values conflated')
        if expected-seen:partial.append('Missing requested IDs: '+', '.join(sorted(expected-seen)))
        contexts=dossier['contexts'];need(set(contexts)==CONTEXT,'Wrong context categories')
        for name,state in contexts.items():
            need(set(state)=={'state','basis'},'Malformed context review')
            need(state['state'] in {'verified','partial','unavailable','unresolved'} and bool(state['basis']),'Invalid context state/basis')
            if state['state']!='verified':partial.append(name+': '+state['state'])
    except (KeyError,TypeError,AttributeError,ValueError) as exc:
        blocked.append('Malformed dossier: '+type(exc).__name__)
    return dict(outcome='BLOCKED' if blocked else 'PARTIAL' if partial else 'PASS',
                scope=scope,blocked=sorted(set(blocked)),partial=sorted(set(partial)),
                qualifications=sorted(set(qualifications)),
                activatesSourceContract=False,authorizesAcquisition=False,
                biomedicalSupport='NOT ASSESSED',
                meaning='Completeness/consistency of an attributed review dossier, not independent verification of reviewer assertions')
