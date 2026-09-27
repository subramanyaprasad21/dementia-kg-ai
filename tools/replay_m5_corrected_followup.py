"""Offline audit of the corrected development follow-up, including failures."""
from collections import Counter
from decimal import Decimal
import json
import m5_corrected_retrieval as plan
ai=plan.ai
DIRECTORY=ai.corpus.ROOT/'experiments/m5-corrected-followup-001'
OLD=ai.corpus.ROOT/'experiments/m5-development-pilot-001'

def replay(directory=DIRECTORY):
    ledger=ai.corpus.read(directory/'ledger.json');prior=ai.corpus.read(OLD/'ledger.json')
    frozen=ai.corpus.read(ai.corpus.ROOT/plan.OUTPUT)
    assert frozen==plan.build()
    assert ledger['attempts'][:14]==prior['attempts']
    assert ledger['followupAuthorization']['priorLedgerSha256']==ai.corpus.digest((OLD/'ledger.json').read_bytes())
    assert ledger['followupAuthorization']['planSha256']==ai.corpus.digest((ai.corpus.ROOT/plan.OUTPUT).read_bytes())
    assert ledger['generationCalls']==22 and ledger['httpRequests']==44
    additional=Decimal(ledger['reservedUSD'])-Decimal(prior['reservedUSD'])
    assert additional<=Decimal('1.92768') and Decimal(ledger['reservedUSD'])<5
    lookup={v['sha256']:(q['questionId'],c) for q in frozen['questions'] for c,v in q['requests'].items()}
    outcomes={};tokens_in=tokens_out=0;failures=[];new_attempts=ledger['attempts'][14:]
    for index,a in enumerate(ledger['attempts']):
        number=index+1; old=number<=14
        if old and (a['status']!='completed' or a['condition']!='model_only'):continue
        base=OLD if old else directory;prefix=f'{number:03d}'
        request=ai.corpus.read(base/(prefix+'.request.json'));prepared=ai.corpus.read(base/(prefix+'.prepared.json'))
        assert ai.corpus.digest(ai.corpus.encode(request))==a['requestSha256']
        q,c=lookup[a['requestSha256']]
        assert request==ai.request_for(prepared,c)
        if a['status']!='completed':
            failures.append(dict(question=q,condition=c,attempt=number,diagnostic=a.get('diagnostic'),reservedUSD=a['reservedUSD'],countedInputTokens=a['countedInputTokens']))
            outcomes[(q,c)]=dict(status='FAILED-NO-OUTPUT',reused=False,attempt=number)
            continue
        raw=(base/(prefix+'.response.json')).read_bytes()
        assert ai.corpus.digest(raw)==a['responseSha256']
        response=json.loads(raw);assert response['model']==ai.MODEL and response.get('service_tier') in (None,'default')
        assert response['usage']==a['usage']
        candidate=ai.parse_response(prepared,response)
        saved=ai.corpus.read(base/(prefix+'.result.json'))
        if c=='model_only':
            expected=dict(status='UNVERIFIED-MODEL-ONLY',candidate=candidate,acceptedAssertions=[])
            accepted=rejected=None;reasons={}
        else:
            expected=dict(retrieval=ai.verify(prepared,candidate,False),verified=ai.verify(prepared,candidate,True))
            accepted=len(expected['verified']['acceptedAssertions']);rejected=sum(d['status']=='REJECTED' for d in expected['verified']['decisions'])
            reasons=dict(Counter(v for d in expected['verified']['decisions'] for v in d['reasons']))
        assert saved==expected
        outcomes[(q,c)]=dict(status='COMPLETED',reused=old,attempt=number,claims=len(candidate['claims']),unanswered=len(candidate['unanswered']),
                            rdfAccepted=accepted,rejected=rejected,rejectionReasons=reasons)
        if not old:tokens_in+=response['usage']['input_tokens'];tokens_out+=response['usage']['output_tokens']
    assert len(new_attempts)==8
    assert sum(a.get('countedInputTokens',100000) for a in new_attempts)<=800000
    assert sum(a.get('usage',{}).get('output_tokens',4096) for a in new_attempts)<=32768
    assert sum(Decimal(a['reservedUSD']) for a in ledger['attempts'])==Decimal(ledger['reservedUSD'])
    rows=[]
    for q in plan.questions():
        baseline=outcomes[(q,'model_only')];ground=outcomes[(q,'retrieval')]
        rows.append(dict(question=q,modelOnly=baseline,grounded=ground,
                         verifiedStatus=('AVAILABLE-EXACT-RDF-CHECKS-ONLY' if ground['status']=='COMPLETED' else 'UNAVAILABLE-NO-GENERATION'),
                         comparableDevelopmentOutputs=ground['status']==baseline['status']=='COMPLETED'))
    return dict(profile='m5-corrected-development-results-1',newGenerationAttempts=8,completedNewGenerations=sum(a['status']=='completed' for a in new_attempts),
                failedNewGenerations=len(failures),failures=failures,rows=rows,knownNewInputTokens=tokens_in,knownNewOutputTokens=tokens_out,
                estimatedKnownNewTokenCostUSD=str((Decimal(tokens_in)*2+Decimal(tokens_out)*10)/1000000),
                newReservedUSD=str(additional),cumulativeReservedUSD=ledger['reservedUSD'],actualFailedCallUsageAndBilling='UNKNOWN',
                cumulativeAttemptCount=22,cumulativeHTTPRequests=44,
                conservativeNewInputTokens=sum(a['countedInputTokens'] for a in new_attempts),
                conservativeNewOutputTokens=sum(a.get('usage',{}).get('output_tokens',4096) for a in new_attempts),
                sourceArtifacts={p.name:ai.corpus.digest(p.read_bytes()) for p in sorted(directory.glob('*.json')) if p.name!='summary.json'},
                interpretation='Development only. Literal RDF support does not establish prose support, relevance, clinical correctness or superiority.')

if __name__=='__main__':print(ai.corpus.encode(replay()).decode(),end='')
