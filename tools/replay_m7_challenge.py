"""Offline execution replay and unchanged local verification; no human labels inferred."""
from collections import Counter
from decimal import Decimal
from pathlib import Path
import json
import m7_challenge_freeze as freeze
import run_m7_challenge as runner

DIRECTORY=freeze.corpus.ROOT/'experiments/m7-portfolio-challenge-001'


def replay(directory=DIRECTORY):
    directory=Path(directory)
    rows=runner.requests()
    manifest=freeze.read(directory/'artifact-manifest.json')
    for name,digest in manifest['rawFiles'].items():
        assert Path(name).name==name
        assert freeze.corpus.digest((directory/name).read_bytes())==digest
    ledger=freeze.read(directory/'ledger.json')
    if ledger['status']=='running':raise ValueError('Execution is not finished')
    assert ledger['baseline']==runner.BASELINE
    assert ledger['generations']<=24 and ledger['httpRequests']<=48
    assert Decimal(ledger['reservedUSD'])<=Decimal('7.50')
    assert Decimal(ledger['priorReservationUSD'])==Decimal('1.544974')
    assert Decimal(ledger['reservedUSD'])==Decimal('1.544974')+sum((Decimal(a.get('reservedUSD','0')) for a in ledger['attempts']),Decimal(0))
    items={i['id']:i for i in freeze.read(freeze.BASE/'questions.json')['items']}
    outcomes=[];inputs=outputs=0;actual=Decimal(0);unknown=0
    for n,row in enumerate(rows,1):
        item=items[row['questionId']]
        outcome=dict(id=item['id'],condition=row['condition'],status='not-attempted',humanScoring='PENDING-OWNER-REVIEW')
        if n>len(ledger['attempts']):
            outcomes.append(outcome);continue
        a=ledger['attempts'][n-1]
        assert a['index']==n and a['questionId']==row['questionId'] and a['condition']==row['condition']
        for t in a['transport']:
            suffix='count' if t['route'].endswith('input_tokens') else 'generation'
            for kind,field,ext in [('request','requestSha256','json'),('response','responseSha256','bin')]:
                raw=(directory/f'{n:02d}.{suffix}.{kind}.{ext}').read_bytes()
                assert freeze.corpus.digest(raw)==t[field]
        request=directory/f'{n:02d}.generation.request.json'
        if request.exists():assert request.read_bytes()==freeze.corpus.encode(row['request'])
        outcome['executionStatus']=a['status']
        rawpath=directory/f'{n:02d}.generation.response.bin'
        if not rawpath.exists():
            outcome['status']='no-generation-response'
            if a.get('reservedUSD'):unknown+=1
            outcomes.append(outcome);continue
        try:response=json.loads(rawpath.read_bytes())
        except ValueError:
            outcome['status']='invalid-output';unknown+=1;outcomes.append(outcome);continue
        usage=response.get('usage')
        if isinstance(usage,dict) and all(type(usage.get(k))==int for k in ('input_tokens','output_tokens')):
            assert usage==a['usage']
            inputs+=usage['input_tokens'];outputs+=usage['output_tokens'];outcome['usage']=usage
        if a.get('actualCostUSD') is None:unknown+=1
        else:
            details=usage['input_tokens_details']
            cached,written=details['cached_tokens'],details['cache_write_tokens']
            plain=usage['input_tokens']-cached-written
            assert plain>=0
            recomputed=(Decimal(plain)*2+Decimal(cached)*Decimal('.2')+Decimal(written)*Decimal('2.5')+Decimal(usage['output_tokens'])*10)/1000000
            assert recomputed==Decimal(a['actualCostUSD'])
            actual+=recomputed
        prepared=freeze.ai.prepare(item['question'],allowed_roots=item['rootIds'],k=8,max_bytes=196608)
        try:candidate=freeze.ai.parse_response(prepared,response)
        except (ValueError,TypeError,KeyError):
            outcome['status']='invalid-output-or-refusal';outcomes.append(outcome);continue
        outcome.update(status='completed',candidate=candidate)
        if row['condition']=='retrieval':
            outcome['grounded']=freeze.ai.verify(prepared,candidate,False)
            outcome['verified']=freeze.ai.verify(prepared,candidate,True)
            assert outcome['grounded']['generatedText']==outcome['verified']['generatedText']==candidate['answer_text']
        outcomes.append(outcome)
    summary=dict(designation=freeze.DESIGNATION,generations=ledger['generations'],httpRequests=ledger['httpRequests'],
        successfulStructuredGenerations=sum(o['status']=='completed' for o in outcomes),
        recordedResponses=sum('usage' in o for o in outcomes),
        notAttempted=sum(o['status']=='not-attempted' for o in outcomes),
        knownInputTokens=inputs,knownOutputTokens=outputs,
        exactKnownCostUSD=str(actual),unknownCostGenerations=unknown,
        totalActualCostUSD=(str(actual) if not unknown else None),cumulativeReservationUSD=ledger['reservedUSD'],
        humanScoring='PENDING: sole owner reviewer; automated RDF support is not prose scoring',
        perCondition={c:dict(Counter(o['status'] for o in outcomes if o['condition']==c)) for c in ('model_only','retrieval')},
        rdfAccepted=sum(len(o['verified']['acceptedAssertions']) for o in outcomes if 'verified' in o),
        rdfRejected=sum(d['status']=='REJECTED' for o in outcomes if 'verified' in o for d in o['verified']['decisions']),
        limitations=['Development-overlapping challenge, not unseen generalization',
          'No clinical or independent validation; no superiority inference',
          'Human prose, relevance, required-fact and qualification metrics remain unscored'])
    summary['perCondition']['verified']=dict(Counter(o['status'] for o in outcomes if o['condition']=='retrieval'))
    summary['verifiedUsesAdditionalGenerations']=False
    summary['conditionUsage']={c:dict(inputTokens=sum(o.get('usage',{}).get('input_tokens',0) for o in outcomes if o['condition']==c),outputTokens=sum(o.get('usage',{}).get('output_tokens',0) for o in outcomes if o['condition']==c)) for c in ('model_only','retrieval')}
    return dict(summary=summary,outcomes=outcomes)

if __name__=='__main__':print(freeze.corpus.encode(replay()).decode(),end='')
