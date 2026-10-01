"""Finite, owner-authorized Mondo pilot. No ingestion, RDF generation or M1 edits."""
import argparse
import hashlib
import json
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

TERMS = ('0004975','0017276','0008243','0010857','0017160','0007088','0015140','0100087')
PARENTS = {'0010857':'0017160','0017160':'0017276','0007088':'0015140',
           '0015140':'0100087','0100087':'0004975'}
EDITION = '2026-09-01'
VERSION_IRI = 'http://purl.obolibrary.org/obo/mondo/releases/2026-09-01/mondo-international.owl'
API = 'https://www.ebi.ac.uk/ols4/api/ontologies/mondo'
BASE = 'https://github.com/subramanyaprasad21/dementia-kg-ai/id/'
MAX_REQUESTS, MAX_BYTES = 100, 10485760
LICENSE = {'identifier':'CC-BY-4.0','url':'https://creativecommons.org/licenses/by/4.0/',
           'source':'https://mondo.monarchinitiative.org/#license',
           'attribution':'Mondo Disease Ontology contributors; delivered by EMBL-EBI OLS',
           'changes':'Raw responses unchanged; bounded JSON projection excludes transport links and out-of-scope parent records.'}
FIELDS = ('iri','obo_id','label','description','synonyms','annotation','obo_synonym','obo_xref',
          'is_obsolete','ontology_name')

class Stop(ValueError):
    pass

class Number(str):
    """Lossless JSON numeric token; never a binary float."""


def canonical(x):
    """JCS string/null/container subset. Source values are typed before this step."""
    if x is None: return b'null'
    if isinstance(x,str):
        x.encode('utf-8','strict')
        return json.dumps(x,ensure_ascii=False,separators=(',',':')).encode('utf-8')
    if isinstance(x,list): return b'['+b','.join(canonical(v) for v in x)+b']'
    if isinstance(x,dict):
        return b'{'+b','.join(canonical(k)+b':'+canonical(x[k]) for k in
                             sorted(x,key=lambda k:k.encode('utf-16-be')))+b'}'
    raise Stop('Receipt has an untyped number/boolean')


def sha(b): return hashlib.sha256(b).hexdigest()
def identity(receipt): return BASE+receipt['profile']+'/'+sha(canonical(receipt))
def utc(): return datetime.now(timezone.utc).isoformat()


def parse(raw):
    def pairs(items):
        result={}
        for k,v in items:
            if k in result: raise Stop('Duplicate JSON key')
            result[k]=v
        return result
    def bad(x): raise Stop('Non-finite number')
    return json.loads(raw.decode('utf-8'),object_pairs_hook=pairs,parse_int=Number,
                      parse_float=Number,parse_constant=bad)


def typed(x):
    if x is None: return {'type':'null'}
    if isinstance(x,Number): return {'type':'number','lexeme':str(x)}
    if isinstance(x,bool): return {'type':'boolean','lexeme':'true' if x else 'false'}
    if isinstance(x,str): return {'type':'string','value':x}
    if isinstance(x,list): return {'type':'array','value':[typed(v) for v in x]}
    if isinstance(x,dict): return {'type':'object','value':{k:typed(v) for k,v in x.items()}}
    raise Stop('Unsupported value')


def field(obj,key):
    return {'state':'present','value':typed(obj[key])} if key in obj else {'state':'absent'}


def term_url(identifier):
    from urllib.parse import quote
    return API+'/terms/'+quote(quote('http://purl.obolibrary.org/obo/MONDO_'+identifier,safe=''),safe='')


def plan():
    return [('metadata-before',API)]+[('term-'+t,term_url(t)) for t in TERMS]+[
        ('parents-'+t,term_url(t)+'/parents') for t in PARENTS]+[('metadata-after',API)]


def edition(data):
    result={'edition':data.get('version'),'versionIri':data.get('config',{}).get('versionIri'),
            'loaded':data.get('loaded'),'updated':data.get('updated')}
    if result['edition']!=EDITION or result['versionIri']!=VERSION_IRI:
        raise Stop('Edition mismatch')
    if data.get('status')!='LOADED' or not result['loaded'] or not result['updated']:
        raise Stop('Missing service-load context')
    return result


def term_projection(data):
    return {key:field(data,key) for key in FIELDS}


def project(slot,data):
    if slot.startswith('metadata'):
        edition(data)
        return {key:field(data,key) for key in ('ontologyId','version','loaded','updated','status','config')},{}
    if slot.startswith('term-'):
        t=slot[5:]
        if data.get('obo_id')!='MONDO:'+t or data.get('iri')!='http://purl.obolibrary.org/obo/MONDO_'+t:
            raise Stop('Requested term does not match response')
        if data.get('ontology_name')!='mondo' or data.get('is_obsolete') is not False or not data.get('label'):
            raise Stop('Term scope/obsolescence/label requires review')
        return term_projection(data),{'id':data['obo_id'],'label':data['label']}
    child=slot[8:]
    rows=data.get('_embedded',{}).get('terms')
    page=data.get('page',{})
    if not isinstance(rows,list): raise Stop('Parent response terms missing')
    if (str(page.get('number'))!='0' or str(page.get('totalPages')) not in ('0','1') or
        str(page.get('totalElements'))!=str(len(rows)) or data.get('_links',{}).get('next')):
        raise Stop('Incomplete/paginated parent response; no automatic expansion')
    selected=[]
    for row in rows:
        if row.get('obo_id') in {'MONDO:'+t for t in TERMS}:
            if row.get('iri')!='http://purl.obolibrary.org/obo/'+row['obo_id'].replace(':','_'):
                raise Stop('Parent identifier mismatch')
            selected.append(term_projection(row))
    expected='MONDO:'+PARENTS[child]
    verified=any(r.get('obo_id')==expected and r.get('ontology_name')=='mondo' and
                 r.get('is_obsolete') is False for r in rows)
    result={'child':'MONDO:'+child,'expectedParent':expected,
            'verified':'yes' if verified else 'no','responseRows':str(len(rows)),
            'projectedRows':str(len(selected))}
    if not verified: raise Stop('Expected parent assertion absent: '+str(result))
    # Preserve upstream order and duplicates. No set sorting or implicit closure.
    return {'child':'MONDO:'+child,'parents':selected,'excludedRows':str(len(rows)-len(selected)),
            'extent':'complete-single-response'},result


def description(slot,payload,context):
    return {'profile':'m2-source-description-1','provider':'EMBL-EBI-OLS','dataset':'Mondo',
            'edition':context['edition'],'versionIri':context['versionIri'],
            'locator':'ontology-metadata' if slot.startswith('metadata') else slot,'projectionVersion':'mondo-ols-minimum-1',
            'payloadSha256':sha(canonical(payload))}


def save(path,obj): path.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,*args,**kwargs): return None

class Batch:
    def __init__(self,directory):
        self.root=Path(directory).resolve()
        repo=Path(__file__).resolve().parents[1]
        if self.root==repo or repo in self.root.parents: raise Stop('Raw storage must be outside repository')
        # Exclusive creation prevents restart/reset or execution-label reuse.
        self.root.mkdir(parents=True,exist_ok=False)
        self.state={'profile':'m2-capture-1','batch':self.root.name,'started':utc(),
                    'requests':0,'bytes':0,'status':'running','license':LICENSE,'records':[]}
        self.opener=urllib.request.build_opener(NoRedirect)
        self.persist()

    def persist(self): save(self.root/'ledger.json',self.state)

    def fetch(self,slot,url):
        if self.state['requests']>=MAX_REQUESTS or self.state['bytes']>=MAX_BYTES:
            raise Stop('G05 budget exhausted')
        request={'method':'GET','url':url,'headers':{'Accept':'application/json',
                 'Accept-Encoding':'identity','User-Agent':'DementiaGraph-Mondo-Pilot/1'},'bodySha256':sha(b'')}
        ordinal=self.state['requests']+1
        receipt={'profile':'m2-capture-1','execution':self.root.name+'/'+str(ordinal),
                 'slot':slot,'request':request,'requestSha256':sha(canonical(request)),
                 'started':utc(),'ended':None,'status':None,'responseHeaders':[],
                 'rawSha256':None,'receivedBytes':'0','complete':'no','error':None,
                 'license':LICENSE,'sourceContext':None}
        entry={'receipt':receipt,'rawFile':f'{ordinal:02d}-{slot}.json','captureId':None,
               'descriptionReceipt':None,'descriptionId':None,'payload':None,'result':None}
        self.state['requests']=ordinal
        self.state['records'].append(entry)
        self.persist()  # Count an attempt even if connection fails.
        response=None
        try:
            try:
                response=self.opener.open(urllib.request.Request(url,headers=request['headers']),timeout=45)
            except urllib.error.HTTPError as error:
                response=error  # Retain/count error and redirect bodies, then stop.
            receipt['status']=str(response.code)
            receipt['responseHeaders']=[[k,v] for k,v in response.headers.items()]
            if response.headers.get('Content-Encoding','identity').lower()!='identity':
                raise Stop('Server ignored identity encoding; stop before receiving body')
            raw=bytearray()
            with (self.root/entry['rawFile']).open('xb') as target:
                while self.state['bytes']<MAX_BYTES:
                    chunk=response.read1(min(16384,MAX_BYTES-self.state['bytes']))
                    if not chunk: break
                    target.write(chunk);raw.extend(chunk);self.state['bytes']+=len(chunk)
                receipt['rawSha256']=sha(bytes(raw));receipt['receivedBytes']=str(len(raw))
            if self.state['bytes']>=MAX_BYTES: raise Stop('Byte ceiling reached; response not accepted complete')
            if response.headers.get('Content-Encoding','identity').lower()!='identity':
                raise Stop('Unexpected compression; no unmeasured decompression accepted')
            length=response.headers.get('Content-Length')
            if length is not None and int(length)!=len(raw): raise Stop('Truncated response')
            if response.code!=200: raise Stop('HTTP '+str(response.code)+'; no retry or redirect followed')
            receipt['complete']='yes'
            return parse(bytes(raw)),entry
        except Exception as error:
            receipt['error']=type(error).__name__+': '+str(error)
            # Partial bodies are retained and hashed, including interrupted reads.
            path=self.root/entry['rawFile']
            if path.exists():
                b=path.read_bytes();receipt['rawSha256']=sha(b);receipt['receivedBytes']=str(len(b))
            raise
        finally:
            if response is not None: response.close()
            receipt['ended']=utc()
            entry['captureId']=identity(receipt)
            self.persist()

    def run(self):
        context=None
        try:
            for slot,url in plan():
                data,entry=self.fetch(slot,url)
                if slot=='metadata-before': context=edition(data)
                if slot=='metadata-after' and edition(data)!=context:
                    raise Stop('Edition or service-load context changed during batch')
                payload,result=project(slot,data)
                entry['receipt']['sourceContext']=context
                entry['captureId']=identity(entry['receipt'])
                rec=description(slot,payload,context)
                for old in self.state['records'][:-1]:
                    if old['descriptionId']==identity(rec) and (old['descriptionReceipt']!=rec or old['payload']!=payload):
                        raise Stop('Identity collision/conflicting immutable payload')
                entry.update(descriptionReceipt=rec,descriptionId=identity(rec),payload=payload,result=result)
                self.persist()
            self.state['status']='complete'
        except Exception as error:
            self.state['status']='stopped';self.state['stopReason']=type(error).__name__+': '+str(error)
        self.state['ended']=utc();self.persist()
        return self.state


def replay(directory):
    root=Path(directory);state=json.loads((root/'ledger.json').read_text())
    if state['status']!='complete' or len(state['records'])!=15: raise Stop('Batch incomplete')
    context=None;total=0
    for (slot,url),entry in zip(plan(),state['records']):
        rec=entry['receipt'];raw=(root/entry['rawFile']).read_bytes();total+=len(raw)
        if rec['slot']!=slot or rec['request']['url']!=url: raise Stop('Wrong capture slot/route')
        if rec['rawSha256']!=sha(raw) or rec['receivedBytes']!=str(len(raw)): raise Stop('Raw integrity failure')
        if rec['requestSha256']!=sha(canonical(rec['request'])) or entry['captureId']!=identity(rec):
            raise Stop('Capture integrity failure')
        if rec['complete']!='yes' or rec['status']!='200': raise Stop('Unsuccessful capture')
        data=parse(raw)
        if slot=='metadata-before': context=edition(data)
        if slot=='metadata-after' and edition(data)!=context: raise Stop('Edition/load mismatch')
        payload,result=project(slot,data);desc=description(slot,payload,context)
        if entry['payload']!=payload or entry['result']!=result or entry['descriptionReceipt']!=desc or entry['descriptionId']!=identity(desc):
            raise Stop('Description replay differs')
        if rec['sourceContext']!=context: raise Stop('Capture context differs')
    if total!=state['bytes'] or state['requests']!=15 or total>MAX_BYTES: raise Stop('Accounting mismatch')
    return {'status':'pass','requests':state['requests'],'bytes':total,'descriptions':len(state['records']),
            'sourceContext':context,'results':[e['result'] for e in state['records'] if e['result']]}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('operation',choices=['capture','replay']);p.add_argument('directory');a=p.parse_args()
    if a.operation=='replay': print(json.dumps(replay(a.directory),indent=2))
    else:
        s=Batch(a.directory).run();print(json.dumps({k:v for k,v in s.items() if k!='records'},indent=2))
        raise SystemExit(0 if s['status']=='complete' else 1)
