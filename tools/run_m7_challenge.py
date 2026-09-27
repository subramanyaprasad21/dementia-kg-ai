"""Execution only; default offline plan. Never parses or scores answer claims."""
import argparse
import json
import os
from decimal import Decimal
from pathlib import Path
import urllib.error
import urllib.request
import uuid

import m7_challenge_freeze as freeze
import m5_openai_adapter as shared

BASELINE = '259af039b034fbd9753e4f69c214459b3fcf5049'
FREEZE_SHA = 'b520428e3e75347bebaa51f1c121fe7afdc80196452f57b53e3d02d5b795b8ee'
PRIOR = freeze.corpus.ROOT / 'experiments/m5-corrected-followup-001/ledger.json'
CAP = Decimal('7.50')
PRICES = dict(input='2.00', cached='0.20', write='2.50', output='10.00',
              verifiedDate='2026-09-28', source='https://developers.openai.com/api/docs/models/gpt-6-sol')


def cost(tokens, output=4096):
    if type(tokens) is not int or not 0 <= tokens <= 100000:
        raise ValueError('Invalid input count or frozen input ceiling exceeded')
    return (Decimal(tokens)*Decimal(PRICES['write']) + Decimal(output)*Decimal(PRICES['output']))/1000000


def requests(private=None):
    freeze.check_digest(freeze.BASE/'freeze.json', FREEZE_SHA)
    freeze.verify(private)
    rows=[]
    receipts=freeze.read(freeze.BASE/'retrieval-checks.json')
    for item, receipt in zip(freeze.read(freeze.BASE/'questions.json')['items'], receipts):
        prepared=freeze.ai.prepare(item['question'], allowed_roots=item['rootIds'], k=8, max_bytes=196608)
        for condition, field in [('model_only','modelOnlyRequestSha256'),('retrieval','groundedRequestSha256')]:
            payload=freeze.ai.request_for(prepared, condition)
            shared.validate_request('responses', payload)
            raw=freeze.corpus.encode(payload)
            if freeze.corpus.digest(raw)!=receipt[field]:
                raise ValueError('Frozen request changed')
            rows.append(dict(questionId=item['id'], condition=condition, request=payload, sha256=receipt[field]))
    return rows


def prior_reservation(path):
    # The reviewed ledger is immutable; a changed development ledger needs review.
    raw=Path(path).read_bytes()
    if raw != PRIOR.read_bytes():
        raise ValueError('Prior ledger differs from approved development reservation')
    ledger=json.loads(raw)
    if Decimal(ledger['reservedUSD']) != Decimal('1.544974'):
        raise ValueError('Unexpected prior reservation')
    return Decimal(ledger['reservedUSD'])


def plan(rows, prior):
    details=[]
    for row in rows:
        # Byte-based offline estimate, NOT a claim about provider-hidden framing.
        n=len(freeze.corpus.encode(row['request']))
        details.append(dict(questionId=row['questionId'], condition=row['condition'],
                            requestSha256=row['sha256'], serializedBytes=n,
                            offlineInputEstimate=min(n,100000),
                            estimatedReservationUSD=str(cost(min(n,100000)))))
    new=sum((Decimal(x['estimatedReservationUSD']) for x in details),Decimal(0))
    return dict(mode='dry-run', apiCalls=0, baseline=BASELINE, requests=details,
                inputTokenStatus='BYTE-BASED ESTIMATE; exact provider counts unavailable offline',
                inputEstimate=sum(x['offlineInputEstimate'] for x in details),
                outputCeiling=24*4096, prices=PRICES, priorReservationUSD=str(prior),
                estimatedNewMaximumUSD=str(new), estimatedCumulativeMaximumUSD=str(prior+new),
                estimatedFits=prior+new<=CAP,
                exactLiveAdmission='Mandatory server count and cache-write reservation before every generation')


def transport(route, payload, key):
    """Shared validation and redirect policy; raw HTTP error bodies retained safely."""
    body=shared.validate_request(route,payload)
    if not key or key.encode() in body:
        raise ValueError('Unsafe credential content')
    req=urllib.request.Request('https://api.openai.com/v1/'+route,data=body,
        headers={'Authorization':'Bearer '+key,'Content-Type':'application/json'},method='POST')
    opener=urllib.request.build_opener(urllib.request.ProxyHandler({}),shared.NoRedirect())
    try:
        response=opener.open(req,timeout=120)
    except urllib.error.HTTPError as error:
        response=error
    with response:
        raw=response.read(4*1024*1024+1)
        status=response.code
        request_id=response.headers.get('x-request-id')
    if len(raw)>4*1024*1024 or key.encode() in raw:
        raise ValueError('Unsafe or oversized response; stop')
    if not isinstance(request_id,str) or len(request_id)>256 or not all(c.isalnum() or c in '_-' for c in request_id) or key in request_id:
        request_id=None
    return dict(raw=raw,status=status,requestId=request_id)


def write_new(path, raw):
    with Path(path).open('xb') as f:
        os.chmod(path,0o600)
        f.write(raw)
        f.flush()
        os.fsync(f.fileno())


def execute(rows, directory, prior, call, key):
    """Called only after authorization/integrity gates. No resume/retry/reset."""
    if len(rows)!=24 or [(r['questionId'],r['condition']) for r in rows] != [(f'M7-{i:02d}',c) for i in range(1,13) for c in ('model_only','retrieval')]:
        raise ValueError('Exactly 24 ordered frozen requests required')
    for row in rows:
        shared.validate_request('responses',row['request'])
        if freeze.corpus.digest(freeze.corpus.encode(row['request'])) != row['sha256']:
            raise ValueError('Request integrity failure')
    directory=Path(directory).resolve()
    if directory==freeze.corpus.ROOT or freeze.corpus.ROOT in directory.parents:
        raise ValueError('Raw run artifacts must stay outside Git')
    # A fixed directory under the prior ledger parent prevents accidental reruns.
    directory.mkdir(mode=0o700,parents=False,exist_ok=False)
    ledger=dict(profile='m7-execution-only-1',runId=str(uuid.uuid4()),baseline=BASELINE,
                created=shared.now(),prices=PRICES,priorReservationUSD=str(prior),
                reservedUSD=str(prior),httpRequests=0,generations=0,inputTokens=0,
                outputReserved=0,attempts=[],status='running')
    def checkpoint():
        shared.save(directory/'ledger.json',ledger)
        os.chmod(directory/'ledger.json',0o600)
    checkpoint()
    for index,row in enumerate(rows,1):
        record=dict(index=index,questionId=row['questionId'],condition=row['condition'],
                    started=shared.now(),requestSha256=row['sha256'],status='counting',usage=None,
                    actualCostUSD=None,actualCostStatus='unknown',transport=[])
        ledger['attempts'].append(record)
        checkpoint()
        def invoke(route,payload,suffix):
            # Check budget even before non-generating token-count requests.
            if Decimal(ledger['reservedUSD'])>CAP or (route.endswith('input_tokens') and Decimal(ledger['reservedUSD'])==CAP) or ledger['httpRequests']>=48:
                raise ValueError('Cumulative budget/request cap reached')
            body=shared.validate_request(route,payload)
            if key.encode() in body:raise ValueError('Unsafe credential content')
            write_new(directory/f'{index:02d}.{suffix}.request.json',body)
            ledger['httpRequests']+=1
            checkpoint() # attempt persisted before transmission
            result=call(route,payload,key)
            raw=result['raw']
            if not isinstance(raw,bytes) or len(raw)>4*1024*1024 or key.encode() in raw:
                raise ValueError('Unsafe response')
            write_new(directory/f'{index:02d}.{suffix}.response.bin',raw)
            record['transport'].append(dict(route=route,status=result['status'],requestId=result.get('requestId'),
                requestSha256=freeze.corpus.digest(body),responseSha256=freeze.corpus.digest(raw),received=shared.now()))
            checkpoint()
            if result['status']!=200:raise RuntimeError('HTTP failure; zero retries')
            return json.loads(raw)
        try:
            if ledger['generations']>=24:raise ValueError('Generation ceiling')
            payload=row['request']
            count=invoke('responses/input_tokens',{k:payload[k] for k in ('model','input','instructions','tools','text')},'count')['input_tokens']
            reserve=cost(count)
            if ledger['inputTokens']+count>2400000 or ledger['outputReserved']+4096>98304:
                raise ValueError('Aggregate token ceiling')
            if Decimal(ledger['reservedUSD'])+reserve>CAP or Decimal(ledger['reservedUSD'])+reserve-prior>Decimal('6'):
                raise ValueError('Cumulative budget cap; generation not sent')
            record.update(countedInputTokens=count,reservedUSD=str(reserve),status='generation-attempted')
            ledger['reservedUSD']=str(Decimal(ledger['reservedUSD'])+reserve)
            ledger['generations']+=1;ledger['inputTokens']+=count;ledger['outputReserved']+=4096
            checkpoint()
            result=invoke('responses',payload,'generation')
            record['modelReturned']=result.get('model');record['responseId']=result.get('id')
            record['usage']=result.get('usage')
            # Accounting only. No answer parsing, local verification or scoring.
            usage=result.get('usage',{})
            a,b=usage.get('input_tokens'),usage.get('output_tokens')
            if type(a)!=int or type(b)!=int or not 0<=a<=count or not 0<=b<=4096:
                raise ValueError('Usage missing or exceeds reservation')
            if result.get('model')!='gpt-6-sol' or result.get('service_tier','default')!='default':
                raise ValueError('Returned model/service tier requires review')
            detail=usage.get('input_tokens_details',{})
            cached,writes=detail.get('cached_tokens'),detail.get('cache_write_tokens')
            if all(type(x)==int and x>=0 for x in (cached,writes)) and cached+writes<=a:
                record['actualCostUSD']=str((Decimal(a-cached-writes)*Decimal('2')+Decimal(cached)*Decimal('.2')+Decimal(writes)*Decimal('2.5')+Decimal(b)*Decimal('10'))/1000000)
                record['actualCostStatus']='reported-token-cost'
            record['status']='response-recorded'
            record['finished']=shared.now();checkpoint()
        except Exception:
            record['status']='stopped-review-required';record['finished']=shared.now()
            ledger['status']='stopped-review-required';checkpoint()
            return ledger # no retry; full reservation retained, even on unknown outcome
    ledger['status']='execution-completed-unscored';checkpoint()
    return ledger


def run(private=None, prior_path=PRIOR, live=False, authorization=None, pricing_confirmed=False, call=None):
    rows=requests(private)
    prior=prior_reservation(prior_path)
    report=plan(rows,prior)
    if not live:return report
    if authorization!='EXECUTE-FROZEN-M7-24-ZERO-RETRIES' or not pricing_confirmed or private is None:
        raise PermissionError('Separate owner live authorization, private verification and current standard-pricing confirmation required')
    expected_prior=freeze.corpus.ROOT.parent/'dementia-kg-ai-model-runs/m5-pilot-001/ledger.json'
    if Path(prior_path).resolve()!=expected_prior.resolve():
        raise ValueError('Live execution requires the existing canonical cumulative ledger location')
    key=os.environ.get('OPENAI_API_KEY')
    if not key:raise RuntimeError('OPENAI_API_KEY unavailable')
    # Lock the cumulative ledger location for the full batch; never mutate M5.
    parent=Path(prior_path).resolve().parent
    lock=parent/'m7-execution.lock'
    with lock.open('x') as handle:
        handle.write('Interrupted execution requires review; do not reset budgets.\n')
    # Lock deliberately remains even after completion/failure. No automatic rerun.
    return execute(rows,parent/'m7-portfolio-challenge-001',prior,call or transport,key)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--private-directory');p.add_argument('--prior-ledger',type=Path,default=PRIOR)
    p.add_argument('--live',action='store_true');p.add_argument('--authorization')
    p.add_argument('--current-standard-pricing-confirmed',action='store_true')
    args=p.parse_args()
    try:
        result=run(args.private_directory,args.prior_ledger,args.live,args.authorization,args.current_standard_pricing_confirmed)
        print(json.dumps(result,indent=2))
    except Exception:
        raise SystemExit('M7 stopped; no automatic retry. Check offline integrity or sanitized run ledger.') from None
