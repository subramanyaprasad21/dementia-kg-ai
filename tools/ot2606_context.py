"""Four-file authorized OT26.06 context capture and offline bounded inspection.

No RDF identity activation. Raw files and the transport ledger stay outside Git.
"""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import urllib.error
import urllib.request
import duckdb
import ot2606_source as source

ROOT = source.ROOT
PLAN = ROOT / 'assessments/remaining-m2-plan.json'
DEFAULT = Path.home() / 'dementia-kg-ai-source-captures/ot2606-context-001'
MAX_BYTES = 20 * 1024 * 1024
MAX_REQUESTS = 100
DRUGS = ['CHEMBL807', 'CHEMBL4298021', 'CHEMBL3990042', 'CHEMBL3833321']
TERMS = ['MONDO_0004975', 'MONDO_0017276', 'MONDO_0008243', 'MONDO_0010857',
         'MONDO_0017160', 'MONDO_0007088', 'MONDO_0015140', 'MONDO_0100087']

def utc():
    return datetime.now(timezone.utc).isoformat()

def files():
    return [dict(partition=p['partition'], name=f['file'], url=p['url']+f['file'], bytes=int(f['bytes']))
            for p in source.load(PLAN)['archiveMetadata'][:3] for f in p['headSizes']]

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

def capture(directory):
    root = Path(directory)
    # An existing ledger is never reset, even if the earlier run stopped.
    root.mkdir(parents=True, exist_ok=False)
    state = dict(batch='ot2606-context-001', edition='26.06', status='running',
                 started=utc(), requests=0, receivedBodyBytes=0, records=[],
                 maxRequests=MAX_REQUESTS, maxBodyBytes=MAX_BYTES,
                 permission={'identifier':'CC0-1.0','source':'https://platform-docs.opentargets.org/licence',
                             'attribution':'Open Targets Platform; cite provider publication'},
                 planSha256=source.sha(PLAN.read_bytes()))
    def persist():
        tmp=root/'ledger.tmp'; tmp.write_bytes(source.serialize(state)); tmp.replace(root/'ledger.json')
    opener=urllib.request.build_opener(NoRedirect())
    persist()
    try:
        for item in files():
            source.require(state['requests'] < MAX_REQUESTS, 'Request ceiling')
            source.require(state['receivedBodyBytes'] + item['bytes'] <= MAX_BYTES, 'Byte ceiling')
            request={'method':'GET','url':item['url'],'headers':{'Accept-Encoding':'identity','User-Agent':'DementiaGraph-V-bounded-context-capture/1'}}
            rec=dict(file=item['name'], partition=item['partition'], request=request,
                     requestSha256=source.sha(source.core.canonical(request)), started=utc(), complete=False)
            state['records'].append(rec); state['requests']+=1; persist()
            response=None
            try:
                try:
                    response=opener.open(urllib.request.Request(item['url'],headers=request['headers']),timeout=60)
                except urllib.error.HTTPError as error:
                    response=error
                rec['status']=response.code
                rec['responseHeaders']=list(response.headers.items())
                # No retry or redirect is followed; its body is still accounted.
                with (root/item['name']).open('xb') as out:
                    while state['receivedBodyBytes'] < MAX_BYTES:
                        chunk=response.read1(min(65536,MAX_BYTES-state['receivedBodyBytes']))
                        if not chunk: break
                        out.write(chunk); state['receivedBodyBytes']+=len(chunk)
                    source.require(state['receivedBodyBytes'] < MAX_BYTES,'Budget exhausted; completeness unverified')
                b=(root/item['name']).read_bytes()
                source.require(response.code == 200, 'HTTP failure/redirect; stopped without retry')
                source.require(response.headers.get('Content-Encoding','identity')=='identity','Unexpected encoding')
                source.require(len(b)==item['bytes'],'Expected size mismatch/truncation')
                source.require(response.headers.get('Content-Length') is None or int(response.headers['Content-Length'])==len(b),'Content-Length mismatch')
                source.require(b[:4]==b'PAR1' and b[-4:]==b'PAR1','Not complete Parquet')
                rec['complete']=True
            finally:
                if response is not None: response.close()
                p=root/item['name']
                if p.exists():
                    b=p.read_bytes();rec.update(sha256=source.sha(b),bytes=len(b))
                rec['ended']=utc();persist()
        state['status']='complete'
    except Exception as error:
        state['status']='stopped'; state['error']=type(error).__name__+': '+str(error)
        raise
    finally:
        state['ended']=utc();persist()
    return state

def verify(directory=DEFAULT):
    root=Path(directory);state=source.load(root/'ledger.json')
    source.require(state['status']=='complete' and state['edition']=='26.06','Incomplete/wrong edition')
    source.require(state['planSha256']==source.sha(PLAN.read_bytes()),'Changed plan')
    source.require(len(state['records'])==4 and state['requests']==4,'Unexpected capture count')
    total=0
    for item, rec in zip(files(),state['records']):
        b=(root/item['name']).read_bytes();total+=len(b)
        source.require(rec['request']['url']==item['url'] and rec['file']==item['name'],'Route mismatch')
        source.require(rec['requestSha256']==source.sha(source.core.canonical(rec['request'])),'Request digest mismatch')
        source.require(rec['sha256']==source.sha(b) and rec['bytes']==len(b)==item['bytes'],'Source digest/size mismatch')
        source.require(rec['complete'] and rec['status']==200,'Unsuccessful response')
    source.require(total==state['receivedBodyBytes'] and total<=MAX_BYTES and state['requests']<=MAX_REQUESTS,'Accounting mismatch')
    source.require(state['permission']['identifier']=='CC0-1.0','Unresolved permission')
    return state

def schemas(directory=DEFAULT):
    verify(directory);db=duckdb.connect()
    try:
        return [dict(file=f['name'], partition=f['partition'],schema=db.execute('DESCRIBE SELECT * FROM read_parquet(?)',[str(Path(directory)/f['name'])]).fetchall(),rows=db.execute('SELECT count(*) FROM read_parquet(?)',[str(Path(directory)/f['name'])]).fetchone()[0]) for f in files()]
    finally:
        db.close()


def extract(directory=DEFAULT):
    """Source-faithful intermediate only; row ordinal is a file locator, not a semantic ID."""
    state=verify(directory);db=duckdb.connect();records=[];schema_records=[]
    try:
        for f, rec in zip(files(),state['records']):
            path=str(Path(directory)/f['name'])
            schema=db.execute('DESCRIBE SELECT * FROM read_parquet(?)',[path]).fetchall()
            schema_records.append(dict(file=f['name'],schema=schema))
            if f['partition']=='drug_mechanism_of_action':
                where='list_has_any(chemblIds, ?)';params=[DRUGS]
            elif f['partition']=='clinical_indication':
                where="drugId=? OR (drugId=? AND diseaseId=?) OR (drugId=? AND diseaseId=?)"
                params=['CHEMBL4298021','CHEMBL3833321','MONDO_0004975','CHEMBL3990042','MONDO_0017276']
            else:
                where='id IN ('+','.join('?' for _ in TERMS)+')';params=TERMS
            query='SELECT * FROM read_parquet(?, file_row_number=true) WHERE '+where+' ORDER BY file_row_number'
            cursor=db.execute(query,[path]+params);keys=[x[0] for x in cursor.description]
            rows=cursor.fetchall()
            for values in rows:
                row=dict(zip(keys,values));ordinal=row.pop('file_row_number')
                records.append(dict(partition=f['partition'],sourceValues=source.typed(row),
                    lineage=dict(url=f['url'],file=f['name'],fileSha256=rec['sha256'],fileRowNumber=ordinal,
                                 captureRecordIndex=state['records'].index(rec),ledgerSha256=source.sha((Path(directory)/'ledger.json').read_bytes())),
                    sourceValueSha256=source.sha(source.core.canonical(source.typed(row)))))
        return dict(contract='ot2606-context-inspection-1',edition='26.06',status='source-intermediate-not-rdf-identity-activation',
                    ledgerSha256=source.sha((Path(directory)/'ledger.json').read_bytes()),schemas=schema_records,records=records,
                    exclusions='Other drug/target IDs and hierarchy context inside raw rows remain source context, not additional accepted graph entities.')
    finally:
        db.close()

def selections(directory=DEFAULT):
    """New local selection, not an assertion that a historical GraphQL call was replayed."""
    verify(directory);old=source.verify_inputs();ge=next(f for f in old['files'] if f['datasource']=='genomics_england')
    db=duckdb.connect();out=[]
    try:
        for anchor,target in [('MONDO_0004975','ENSG00000142192'),('MONDO_0017276','ENSG00000186868')]:
            rows=db.execute('SELECT descendants FROM read_parquet(?) WHERE id=?',[str(Path(directory)/'disease.parquet'),anchor]).fetchall()
            source.require(len(rows)==1 and rows[0][0] is not None,'Ambiguous/missing anchor hierarchy')
            for mode,ids in [('direct',[anchor]),('inclusive',[anchor]+rows[0][0])]:
                values=db.execute('SELECT id,diseaseId FROM read_parquet(?) WHERE targetId=? AND list_contains(?,diseaseId) ORDER BY id',[str(source.artifacts()/ge['name']),target,ids]).fetchall()
                source.require(len({r[0] for r in values})==len(values),'Duplicate evidence identity')
                out.append(dict(anchor=anchor,target=target,mode=mode,members=[dict(id=r[0],diseaseId=r[1]) for r in values],count=len(values),
                                hierarchyFileSha256=next(r['sha256'] for r in verify(directory)['records'] if r['partition']=='disease'),
                                evidenceFileSha256=ge['sha256'],method='exact anchor union source descendants; GE targetId equality; ID sort',
                                completeness='complete for these files and explicit predicate, not historical GraphQL execution'))
        return out
    finally:
        db.close()


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('operation',choices=['capture','verify','schemas','extract','selections'])
    parser.add_argument('--directory',default=str(DEFAULT))
    args=parser.parse_args()
    result={'capture':capture,'verify':verify,'schemas':schemas,'extract':extract,'selections':selections}[args.operation](args.directory)
    print(json.dumps(result,indent=2))
