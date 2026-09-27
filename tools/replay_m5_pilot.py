"""Offline replay of retained development outputs; never calls an API."""
from collections import Counter
from decimal import Decimal
import json
from pathlib import Path
import m5_evidence_answers as ai

DIRECTORY = ai.corpus.ROOT/'experiments/m5-development-pilot-001'

def replay(directory=DIRECTORY):
    ledger=ai.corpus.read(directory/'ledger.json')
    prior=ai.corpus.read(ai.corpus.ROOT/'assessments/m5-diagnostic-retry.json')['ledger']
    assert ledger['attempts'][:2]==prior['attempts']
    assert ledger['limits']==prior['limits']
    assert ledger['generationCalls']==len(ledger['attempts'])<=14
    assert ledger['httpRequests']<=28
    assert sum(Decimal(a['reservedUSD']) for a in ledger['attempts'])==Decimal(ledger['reservedUSD'])<=Decimal('5')
    assert sum(a.get('usage',{}).get('input_tokens',a['countedInputTokens']) for a in ledger['attempts'])<=1400000
    assert sum(a.get('usage',{}).get('output_tokens',4096) for a in ledger['attempts'])<=57344
    plan=ai.corpus.read(ai.corpus.ROOT/'assessments/m5-pilot-plan.json')
    lookup={v['sha256']:(q['questionId'],c) for q in plan['questions'] for c,v in q['requests'].items()}
    rows=[]; tokens_in=tokens_out=cached=0
    for i,a in enumerate(ledger['attempts'],1):
        prefix=f'{i:03d}'
        request=ai.corpus.read(directory/(prefix+'.request.json'))
        prepared=ai.corpus.read(directory/(prefix+'.prepared.json'))
        assert ai.corpus.digest(ai.corpus.encode(request))==a['requestSha256']
        q,c=lookup[a['requestSha256']]
        assert c==a['condition']
        assert request==ai.request_for(prepared,c)
        if a['status']!='completed':
            continue
        raw=(directory/(prefix+'.response.json')).read_bytes()
        assert ai.corpus.digest(raw)==a['responseSha256']
        response=json.loads(raw)
        assert response['model']==ai.MODEL and response.get('service_tier') in (None,'default')
        assert response['usage']==a['usage']
        candidate=ai.parse_response(prepared,response)
        expected=(dict(status='UNVERIFIED-MODEL-ONLY',candidate=candidate,acceptedAssertions=[]) if c=='model_only' else dict(retrieval=ai.verify(prepared,candidate,False),verified=ai.verify(prepared,candidate,True)))
        assert expected==ai.corpus.read(directory/(prefix+'.result.json'))
        usage=response['usage']; tokens_in+=usage['input_tokens'];tokens_out+=usage['output_tokens']
        cached+=usage.get('input_tokens_details',{}).get('cached_tokens',0)
        reasons=Counter()
        if c=='retrieval':
            for d in expected['verified']['decisions']: reasons.update(d['reasons'])
        rows.append(dict(question=q,condition=c,claims=len(candidate['claims']),unanswered=len(candidate['unanswered']),
                         rdfAccepted=len(expected['verified']['acceptedAssertions']) if c=='retrieval' else None,
                         rejected=sum(d['status']=='REJECTED' for d in expected['verified']['decisions']) if c=='retrieval' else None,
                         rejectionReasons=dict(reasons),inputTokens=usage['input_tokens'],outputTokens=usage['output_tokens']))
    files={p.name:ai.corpus.digest(p.read_bytes()) for p in sorted(directory.glob('*.json')) if p.name!='summary.json'}
    return dict(profile='m5-development-observations-1',rows=rows,generationAttempts=ledger['generationCalls'],completedGenerations=len(rows),
                httpRequests=ledger['httpRequests'],inputTokens=tokens_in,outputTokens=tokens_out,cachedInputTokens=cached,
                successfulGenerationCostUpperEstimateUSD=str((Decimal(tokens_in)*2+Decimal(tokens_out)*10)/1000000),
                reservedUSD=ledger['reservedUSD'],failedAttemptBilling='UNKNOWN; reservations retained',unrunQuestions=['Q07'],
                stopReason='Original 14-generation-attempt ceiling; two prior failures counted',artifactSha256=files,
                interpretation='Operational development observations only. No clinical accuracy, held-out results or superiority claim.')

if __name__=='__main__':
    print(ai.corpus.encode(replay()).decode(),end='')
