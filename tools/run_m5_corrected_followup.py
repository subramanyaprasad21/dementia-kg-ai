"""Finite owner-approved follow-up. No API calls without --approved-followup."""
import argparse
from pathlib import Path
from decimal import Decimal
import m5_corrected_retrieval as plan
import m5_openai_adapter as adapter
ai=plan.ai
BASE=ai.corpus.ROOT/'experiments/m5-development-pilot-001'
REVIEWED=('651e8c9c-8a34-4748-a103-df25f98d5dba','2fc2bc08-6da1-4a92-9fad-75b9bc0b02ba')

def amend(directory):
    """One explicit amendment; preserve old entries/counters and snapshot hash."""
    path=Path(directory)/'ledger.json'
    if (Path(directory)/'run.lock').exists(): raise ValueError('Run active or interrupted')
    ledger=ai.corpus.read(path)
    original=ai.corpus.read(BASE/'ledger.json')
    if ledger!=original: raise ValueError('Expected exact original pilot ledger; no reset or automatic resume')
    ledger['followupAuthorization']=dict(profile='m5-corrected-followup-1',
        baseline='18ddd6444a8391abebbe210f2c9ba9b5e97d2bb1',
        priorLedgerSha256=ai.corpus.digest(path.read_bytes()),priorLimits=ledger['limits'],
        priorGenerationAttempts=14,priorHTTPRequests=28,priorReservedUSD=ledger['reservedUSD'],
        maxNewGenerations=8,maxNewInputTokens=800000,maxNewOutputTokens=32768,maxAdditionalUSD='1.92768',
        planSha256=ai.corpus.digest((ai.corpus.ROOT/plan.OUTPUT).read_bytes()))
    ledger['limits']=dict(adapter.LIMITS,generationCalls=22,httpRequests=44)
    adapter.save(path,ledger)

def run(directory, approved=False):
    if not approved: raise PermissionError('Explicit corrected follow-up approval required')
    directory=Path(directory).resolve()
    if ai.corpus.ROOT==directory or ai.corpus.ROOT in directory.parents: raise ValueError('Use external existing run directory')
    frozen=ai.corpus.read(ai.corpus.ROOT/plan.OUTPUT)
    if frozen!=plan.build():raise ValueError('Corrected retrieval plan changed')
    amend(directory)
    for row in frozen['questions']:
        prepared=plan.prepare(row['questionId'])
        for condition in (('model_only','retrieval') if row['questionId']=='Q07' else ('retrieval',)):
            assert ai.corpus.digest(ai.corpus.encode(ai.request_for(prepared,condition)))==row['requests'][condition]['sha256']
            print(row['questionId'],condition,'starting',flush=True)
            adapter.run(prepared,condition,directory,True,reviewed_failure_ids=REVIEWED,corrected_followup=True)
            ledger=ai.corpus.read(directory/'ledger.json'); new=ledger['attempts'][14:]
            response=ai.corpus.read(directory/f"{len(ledger['attempts']):03d}.response.json")
            if response['model']!=ai.MODEL or response.get('service_tier') not in (None,'default'):
                raise ValueError('Model/tier differs; stop')
            assert sum(a['usage']['input_tokens'] for a in new)<=800000
            assert sum(a['usage']['output_tokens'] for a in new)<=32768
            assert Decimal(ledger['reservedUSD'])-Decimal(ledger['followupAuthorization']['priorReservedUSD'])<=Decimal('1.92768')
            assert Decimal(ledger['reservedUSD'])<5
            print(row['questionId'],condition,'completed',flush=True)
    print('FOLLOWUP COMPLETED',flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('directory');p.add_argument('--approved-followup',action='store_true');a=p.parse_args()
    try:run(a.directory,a.approved_followup)
    except Exception:
        print('STOPPED: inspect sanitized ledger; no automatic retry',flush=True)
        raise SystemExit(1)
