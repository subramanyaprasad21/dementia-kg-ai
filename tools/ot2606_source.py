"""Finite offline OT 26.06 freeze/extraction. Never contacts a source."""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import duckdb
import m1_fixture_identity as core
import frozen_snapshots as frozen

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT/'manifests/ot2606-evidence-001.freeze.json'
OUTPUT = ROOT/'extractions/ot2606-evidence-001.json'
DEFAULT = Path.home()/'dementia-kg-ai-source-captures/ot2606-evidence-001'
BASE = core.BASE+'id/'
DESCRIPTION = 'm2-ot-parquet-description-1'
AUTHORITY_ROOT = frozen.snapshot_root('ot2606-evidence-001')

def require(ok, message):
    if not ok: raise ValueError(message)

def sha(b): return hashlib.sha256(b).hexdigest()
def serialize(v): return (json.dumps(v, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False)+'\n').encode()
def load(p): return core.strict_load(Path(p).read_text())
def artifacts(): return Path(os.environ.get('OT2606_ARTIFACTS',str(DEFAULT)))
def typed(v):
    if v is None: return {'type':'null','value':None}
    if isinstance(v,str): return {'type':'string','value':v}
    if isinstance(v,bool): return {'type':'boolean','value':'true' if v else 'false'}
    if isinstance(v,int): return {'type':'integer','value':str(v)}
    if isinstance(v,float):
        require(math.isfinite(v),'Nonfinite numeric source value')
        return {'type':'double','value':v.hex()}
    if isinstance(v,list): return {'type':'array','value':[typed(x) for x in v]}
    if isinstance(v,dict): return {'type':'object','value':{k:typed(x) for k,x in v.items()}}
    raise ValueError('Unsupported source type')
def untyped(v):
    t,x=v['type'],v['value']
    if t in ('null','string'):return x
    if t=='integer':return int(x)
    if t=='double':return float.fromhex(x)
    if t=='boolean':return x=='true'
    if t=='array':return [untyped(a) for a in x]
    if t=='object':return {k:untyped(a) for k,a in x.items()}
    raise ValueError('Unsupported encoded type')
def field(row,key):
    return {'state':'source-absent'} if key not in row else {'state':'source-null' if row[key] is None else 'present','value':typed(row[key])}
def identify(profile,receipt):return BASE+profile+'/'+sha(core.canonical(receipt))
def description(row,schema,edition,datasource):
    require(edition=='26.06','Wrong historical release')
    require(row['datasourceId']==datasource,'Wrong datasource')
    require(set(row)=={x[0] for x in schema},'Schema/record mismatch')
    receipt={'profile':DESCRIPTION,'provider':'Open Targets Platform','edition':edition,'datasource':datasource,
             'sourceRecordId':row['id'],'schema':schema,'projection':'all-columns-ordered-nested-values-1',
             'contentSha256':sha(core.canonical(typed(row)))}
    return {'id':identify(DESCRIPTION,receipt),'receipt':receipt}
def verify_inputs(root=None,manifest=None,verify_scan=True):
    root=artifacts() if root is None else Path(root);m=load(MANIFEST) if manifest is None else manifest
    require(m['edition']=='26.06' and m['profile']=='ot2606-freeze-1','Wrong edition/profile')
    frozen.verify_mapping(m['authorities'], AUTHORITY_ROOT)
    for f in m['files']:
        p=root/f['name'];require(p.is_file(),'Missing source file: '+f['name'])
        require(p.stat().st_size==f['bytes'] and sha(p.read_bytes())==f['sha256'],'Changed source file: '+f['name'])
        require(f['url']==m['archive']+'evidence_'+f['datasource']+'/'+f['name'],'Wrong source route')
        require(f['url'] in f['downloadOrigins'],'Missing observed download provenance')
        require(f['permissions']['identifier']=='CC0-1.0','Unreviewed permissions')
    if verify_scan:
        directory=root/'ot2606-ep-selective-001';ledger=load(directory/'ledger.json')
        require(sha((directory/'ledger.json').read_bytes())==m['selectiveScan']['ledgerSha256'],'Changed scan ledger')
        require(ledger['status']=='complete' and len(ledger['files'])==125,'Incomplete scan')
        require(ledger['requests']==250 and ledger['body_bytes']==1027119970,'Scan accounting mismatch')
        for r in ledger['records']:
            b=(directory/r['artifact']).read_bytes();require(len(b)==r['body_bytes'] and sha(b)==r['sha256'],'Changed scan range')
        for f in m['files']:
            if f['datasource']!='europepmc':continue
            index=next(i for i,x in enumerate(ledger['files']) if x['filename']==f['name'])
            with (root/f['name']).open('rb') as source:
                for rec in ledger['records'][2*index:2*index+2]:
                    start,end=map(int,rec['range'][6:].split('-'));source.seek(start)
                    require(sha(source.read(end-start+1))==rec['sha256'],'Downloaded file differs from original remote range')
    return m

def extract(root=None,manifest=None,verify_scan=True):
    root=artifacts() if root is None else Path(root);m=verify_inputs(root,manifest,verify_scan)
    con=duckdb.connect();out=[]
    try:
        for f in m['files']:
            path=str(root/f['name']);schema=[list(x[:2]) for x in con.execute('describe select * from read_parquet(?)',[path]).fetchall()]
            require(schema==f['schema'],'Historical schema changed')
            q=con.execute('select * from read_parquet(?) where id in (select unnest(?))',[path,f['evidenceIds']]);names=[x[0] for x in q.description];rows=[dict(zip(names,v)) for v in q.fetchall()]
            require(sorted(r['id'] for r in rows)==sorted(f['evidenceIds']),'Missing or duplicate evidence ID')
            require(con.execute('select count(*) from read_parquet(?)',[path]).fetchone()[0]==f['rows'],'Row inventory changed')
            for row in rows:
                desc=description(row,schema,m['edition'],f['datasource'])
                out.append({'id':row['id'],'description':desc,'sourceValues':typed(row),
                            'lineage':{'file':f['name'],'fileSha256':f['sha256'],'captureId':f['localReceiptId'],
                                       'locator':{'url':f['url'],'recordId':row['id']},'manifestSha256':sha(serialize(m))}})
    finally:con.close()
    require(len(out)==8 and len({r['id'] for r in out})==8,'Wrong finite evidence inventory')
    return {'profile':'ot2606-extraction-1','edition':m['edition'],'manifestSha256':sha(serialize(m)),
            'records':sorted(out,key=lambda r:r['id']), 'scope':'Eight exact evidence occurrences; no historic selection, aggregate, mechanism or registry reconstruction',
            'interpretation':'Source values unchanged. Original field absence, null and empty arrays differ. No clinical or equivalence inference.'}

def verify(root=None):
    value=extract(root);require(serialize(value)==OUTPUT.read_bytes(),'Extraction replay differs');return value

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('operation',choices=['build','verify']);a=p.parse_args()
    if a.operation=='build':
        b=serialize(extract())
        with OUTPUT.open('xb') as f:f.write(b)
    print(json.dumps({'records':len(verify()['records']),'sha256':sha(OUTPUT.read_bytes())}))
