"""Finite 28-file OT26.06 range probe; one persistent 64-MiB/100-request ledger."""
from pathlib import Path
import struct,json
class Compact:
 def __init__(self,b): self.b=b; self.i=0
 def byte(self): x=self.b[self.i]; self.i+=1; return x
 def var(self):
  n=s=0
  while True:
   x=self.byte(); n|=(x&127)<<s
   if x<128:return n
   s+=7
 def val(self,t):
  if t in (1,2):return t==1
  if t==3:return self.byte()
  if t in (4,5,6):
   x=self.var();return (x>>1)^-(x&1)
  if t==7:
   x=struct.unpack('<d',self.b[self.i:self.i+8])[0];self.i+=8;return x
  if t==8:
   n=self.var();x=self.b[self.i:self.i+n];self.i+=n
   return x.decode('utf8',errors='backslashreplace')
  if t in (9,10):
   x=self.byte();n=x>>4
   if n==15:n=self.var()
   return [self.val(x&15) for _ in range(n)]
  if t==12:return self.obj()
  raise ValueError(t)
 def obj(self):
  out={};last=0
  while True:
   x=self.byte()
   if x==0:return out
   d=x>>4;field=last+d if d else self.val(4);last=field
   out[field]=self.val(x&15)
import urllib.request,urllib.error,hashlib,time
import duckdb
import ot2606_source as source
ROOT=source.DEFAULT.parent/'ot2606-association-001'
LIMIT=64*1024*1024
class NoRedirect(urllib.request.HTTPRedirectHandler):
 def redirect_request(self,*args,**kwargs):return None

def run():
 ROOT.mkdir(exist_ok=False)
 state={'status':'running','requests':0,'bytes':0,'maxBytes':LIMIT,'maxRequests':100,'records':[],'files':[],'rows':[]}
 def save():
  (ROOT/'ledger.json').write_bytes(source.serialize(state))
 opener=urllib.request.build_opener(NoRedirect());db=duckdb.connect();db.execute('SET threads=1')
 def fetch(url,range_text,expected,tag,etag=None):
  source.require(state['requests']<100 and state['bytes']+expected<=LIMIT,'Budget stop before request')
  record={'url':url,'range':range_text,'started':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'bytes':0,'artifact':tag}
  state['requests']+=1;state['records'].append(record);save()
  headers={'Range':range_text,'Accept-Encoding':'identity'}
  if etag:headers['If-Match']=etag
  try:r=opener.open(urllib.request.Request(url,headers=headers),timeout=60)
  except urllib.error.HTTPError as e:r=e
  raw=bytearray()
  try:
   record['status']=r.status;record['headers']=dict(r.headers)
   if r.status!=206:
    raw.extend(r.read(min(65536,expected)));state['bytes']+=len(raw);record['bytes']=len(raw)
    raise ValueError('Range request failed; no retry/full-file fallback')
   while len(raw)<expected:
    b=r.read1(min(65536,expected-len(raw)))
    if not b:break
    raw.extend(b);state['bytes']+=len(b);record['bytes']+=len(b)
   source.require(len(raw)==expected,'Truncated range')
   return bytes(raw),dict(r.headers)
  finally:
   r.close();(ROOT/tag).write_bytes(raw);record['sha256']=source.sha(raw);save()
 try:
  tables=source.load(source.ROOT/'assessments/remaining-m2-plan.json')['archiveMetadata'][3:]
  for table in tables:
   for name in table['files']:
    url=table['url']+name;index=len(state['files']);prefix=str(index).zfill(2)
    tail,h=fetch(url,'bytes=-65536',65536,prefix+'.tail')
    content_range=h.get('Content-Range','');size=int(content_range.split('/')[-1])
    source.require(content_range==f'bytes {size-65536}-{size-1}/{size}' and tail[-4:]==b'PAR1','Wrong range/file trailer')
    n=int.from_bytes(tail[-8:-4],'little');source.require(n<=65528,'Footer larger than bounded probe; stop')
    parser=Compact(tail[-8-n:-8]);meta=parser.obj();source.require(parser.i==n,'Unparsed footer')
    sparse=ROOT/'inspection-only.sparse.parquet'
    with sparse.open('wb') as out:out.truncate(size);out.write(b'PAR1');out.seek(size-65536);out.write(tail)
    info={'table':table['partition'],'file':name,'url':url,'bytes':size,'rowGroups':len(meta[4]),'matches':[]};state['files'].append(info);save()
    # Read only disease/target columns first. Raw column chunks stay immutable.
    for gi,group in enumerate(meta[4]):
     for ci,column in enumerate(group[1]):
      col=column[3]
      if col[3] not in (['diseaseId'],['targetId']):continue
      start=min(x for x in [col.get(9),col.get(11)] if x is not None);length=col[7]
      b,bh=fetch(url,f'bytes={start}-{start+length-1}',length,f'{prefix}.{gi}.{ci}.keys',h.get('ETag'))
      source.require(bh.get('Content-Range')==f'bytes {start}-{start+length-1}/{size}','Wrong key range')
      with sparse.open('r+b') as out:out.seek(start);out.write(b)
    targets=['ENSG00000186868'] if table['partition']=='association_overall_direct' else ['ENSG00000176884','ENSG00000116032']
    matches=db.execute('SELECT file_row_number,diseaseId,targetId FROM read_parquet(?,file_row_number=true) WHERE diseaseId=? AND list_contains(?,targetId)',[str(sparse),'MONDO_0017276',targets]).fetchall()
    info['matches']=matches;save()
    if matches:
     wanted={m[0] for m in matches};offset=0
     for gi,group in enumerate(meta[4]):
      count=group[3];selected=any(offset<=i<offset+count for i in wanted);offset+=count
      if not selected:continue
      for ci,column in enumerate(group[1]):
       col=column[3]
       if col[3] in (['diseaseId'],['targetId']):continue
       start=min(x for x in [col.get(9),col.get(11)] if x is not None);length=col[7]
       b,bh=fetch(url,f'bytes={start}-{start+length-1}',length,f'{prefix}.{gi}.{ci}.values',h.get('ETag'))
       source.require(bh.get('Content-Range')==f'bytes {start}-{start+length-1}/{size}','Wrong value range')
       with sparse.open('r+b') as out:out.seek(start);out.write(b)
     cur=db.execute('SELECT * FROM read_parquet(?,file_row_number=true) WHERE diseaseId=? AND list_contains(?,targetId)',[str(sparse),'MONDO_0017276',targets]);cols=[a[0] for a in cur.description]
     for row in cur.fetchall():state['rows'].append({'table':table['partition'],'file':name,'sourceValues':source.typed(dict(zip(cols,row)))})
    sparse.unlink();save()
    print(json.dumps({'files':len(state['files']),'requests':state['requests'],'bytes':state['bytes'],'matched':len(matches)}),flush=True)
  state['status']='complete'
 except Exception as error:
  state['status']='stopped';state['error']=str(error)
 finally:
  db.close();save()
 return state
if __name__=='__main__':
 s=run();print(json.dumps({k:v for k,v in s.items() if k not in ('records','files','rows')},indent=2))

def recover_projection(directory=ROOT):
 """Recover the needed scalar columns already captured; never reads zero-filled columns."""
 import tempfile
 root=Path(directory);ledger=source.load(root/'ledger.json')
 matches=[f for f in ledger['files'] if f['matches']]
 source.require(len(matches)==1,'Expected one located bounded association file')
 item=matches[0];records=[r for r in ledger['records'] if r['url']==item['url']]
 tailrec=next(r for r in records if r['artifact'].endswith('.tail'))
 def raw(r):
  b=(root/r['artifact']).read_bytes();source.require(source.sha(b)==r['sha256'] and len(b)==r['bytes'],'Corrupt/missing captured range');return b
 tail=raw(tailrec);n=int.from_bytes(tail[-8:-4],'little');meta=Compact(tail[-8-n:-8]).obj()
 needed={'diseaseId','targetId','aggregationType','aggregationValue','associationScore','evidenceCount'}
 source.require(len(meta[4])==1,'Unverified multi-group projection')
 selected=[]
 for column in meta[4][0][1]:
  col=column[3]
  if len(col[3])!=1 or col[3][0] not in needed:continue
  start=min(x for x in [col.get(9),col.get(11)] if x is not None);length=col[7]
  ranges=[r for r in records if r['range']==f'bytes={start}-{start+length-1}']
  source.require(len(ranges)==1,'Required column was not captured')
  selected.append((start,raw(ranges[0]),col[3][0],ranges[0]['sha256']))
 source.require({x[2] for x in selected}==needed,'Incomplete required column projection')
 with tempfile.TemporaryDirectory() as tmp:
  sparse=Path(tmp)/'projection-only.parquet'
  with sparse.open('wb') as f:
   f.truncate(item['bytes']);f.write(b'PAR1');f.seek(item['bytes']-len(tail));f.write(tail)
   for start,b,_,_ in selected:f.seek(start);f.write(b)
  db=duckdb.connect()
  try:
   cur=db.execute('SELECT diseaseId,targetId,aggregationType,aggregationValue,associationScore,evidenceCount FROM read_parquet(?) WHERE diseaseId=? AND targetId=?',[str(sparse),'MONDO_0017276','ENSG00000186868']);cols=[x[0] for x in cur.description];values=cur.fetchall()
  finally:db.close()
 source.require(len(values)==1,'Ambiguous/missing located association')
 return dict(edition='26.06',table=item['table'],url=item['url'],fileRowNumber=item['matches'][0][0],
             sourceValues=source.typed(dict(zip(cols,values[0]))),ledgerSha256=source.sha((root/'ledger.json').read_bytes()),
             columnRanges=[dict(column=name,start=start,bytes=len(b),sha256=digest) for start,b,name,digest in selected],
             footerSha256=tailrec['sha256'],scope='One located scalar association projection; 11/28 files reached. No full-table uniqueness, timeseries or datasource-composition claim.')
