"""Approved finite primary-source batch: metadata and permission-gated articles.

No current PanelApp/registry record substitutes for an unknown historical version.
"""
from pathlib import Path
from urllib.parse import urlencode
import urllib.request,urllib.error
import xml.etree.ElementTree as ET
import json
from datetime import datetime,timezone
import ot2606_source as source
ROOT=source.DEFAULT.parent/'primary-evidence-001'
LIMIT=10*1024*1024
PMCS=['PMC7852392','PMC6742707','PMC6298197','PMC4054967']
class NoRedirect(urllib.request.HTTPRedirectHandler):
 def redirect_request(self,*args,**kwargs):return None

def run(resume_metadata=False, history_metadata=False):
 if not (resume_metadata or history_metadata):ROOT.mkdir(exist_ok=False)
 state={'batch':'primary-evidence-001','status':'running','requests':0,'bytes':0,'maxBytes':LIMIT,'maxRequests':100,'records':[],'rights':[],'limitations':['New publication captures, not historical HTTP response reproduction.','PanelApp and registry historical versions/permissions unresolved; no current record substituted.']}
 if resume_metadata or history_metadata:
  state=source.load(ROOT/'ledger.json')
  source.require(state['status']=='complete-bounded-attempt' and state['requests']==(9 if history_metadata else 4),'Unexpected resume state; no reset')
  state['status']='running'
 def save():(ROOT/'ledger.json').write_bytes(source.serialize(state))
 opener=urllib.request.build_opener(NoRedirect())
 def fetch(url,name):
  source.require(state['requests']<100 and state['bytes']<LIMIT,'Budget exhausted')
  rec={'url':url,'method':'GET','started':datetime.now(timezone.utc).isoformat(),'artifact':name,'bytes':0};state['requests']+=1;state['records'].append(rec);save()
  try:response=opener.open(urllib.request.Request(url,headers={'Accept-Encoding':'identity','User-Agent':'DementiaGraph-V-finite-academic-source-inspection/1'}),timeout=60)
  except urllib.error.HTTPError as e:response=e
  raw=bytearray()
  try:
   rec['status']=response.code;rec['headers']=dict(response.headers)
   while state['bytes']<LIMIT:
    b=response.read1(min(65536,LIMIT-state['bytes']))
    if not b:break
    raw.extend(b);state['bytes']+=len(b);rec['bytes']+=len(b)
   source.require(state['bytes']<LIMIT,'Byte ceiling: response completeness not established')
   rec['complete']=True
   # Failed/redirect bodies count, but no automatic retry or substitute follows.
   return bytes(raw) if response.code==200 else None
  finally:
   response.close();rec['sha256']=source.sha(raw);(ROOT/name).write_bytes(raw);save()
 try:
  # Europe PMC is an approved alternative metadata provider. Resume preserves
  # all four failed NCBI calls and cumulative bytes; no automatic reset.
  if history_metadata:
   for nct in ['NCT00594737','NCT03658135']:
    fetch('https://clinicaltrials.gov/api/int/studies/'+nct+'/history',nct+'.history-metadata.json')
  if resume_metadata:
   slots=source.load(source.ROOT/'contracts/dementia-evidence-readiness.json')['sourceSlots']
   pmids=[x['locator'] for x in slots if x['kind']=='Publication']
   query='SRC:MED AND ('+' OR '.join('EXT_ID:'+p for p in pmids)+')'
   body=fetch('https://www.ebi.ac.uk/europepmc/webservices/rest/search?'+urlencode({'query':query,'format':'json','resultType':'core','pageSize':'100'}),'publication-metadata.json')
   if body:
    data=json.loads(body);records=data.get('resultList',{}).get('result',[])
    source.require(data.get('hitCount')==len(pmids) and {r['id'] for r in records}==set(pmids),'Partial/ambiguous publication metadata')
    for pmc in PMCS:
     matches=[r for r in records if r.get('pmcid')==pmc]
     license=matches[0].get('license') if len(matches)==1 else None
     allowed=isinstance(license,str) and license.lower().replace('-',' ').strip() in {'cc by','cc0','cc by sa','cc by nc','cc by nc sa','cc by nd','cc by nc nd'}
     state['rights'].append({'id':pmc,'provider':'Europe PMC','license':license,'status':'LOCAL-ACADEMIC-INSPECTION-ONLY' if allowed else 'UNRESOLVED'})
     save()
     if allowed:
      article=fetch('https://www.ebi.ac.uk/europepmc/webservices/rest/'+pmc+'/fullTextXML',pmc+'.article.xml')
      if article:
       root=ET.fromstring(article);ids=[''.join(x.itertext()) for x in root.findall('.//article-id') if x.attrib.get('pub-id-type') in {'pmc','pmcid'}]
       source.require(pmc in ids or pmc[3:] in ids,'Article identity mismatch')
  # OA metadata is the permission gate; no full-text content retrieved first.
  for pmc in ([] if (resume_metadata or history_metadata) else PMCS):
   body=fetch('https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?'+urlencode({'id':pmc}),pmc+'.rights.xml')
   if body is None:
    state['rights'].append({'id':pmc,'status':'UNRESOLVED','reason':'Official OA metadata response unsuccessful'});save();continue
   tree=ET.fromstring(body);records=tree.findall('.//record');match=[r for r in records if r.attrib.get('id')==pmc]
   if len(match)!=1:
    state['rights'].append({'id':pmc,'status':'UNRESOLVED','reason':'No unique official OA record'});save();continue
   license=match[0].attrib.get('license');permitted=license in {'CC BY','CC0','CC BY-SA','CC BY-NC','CC BY-NC-SA','CC BY-ND','CC BY-NC-ND'}
   state['rights'].append({'id':pmc,'license':license,'status':'LOCAL-ACADEMIC-INSPECTION-ONLY' if permitted else 'UNRESOLVED','redistribution':'Not authorized by this batch; article-specific terms remain attached.'});save()
   if permitted:
    article=fetch('https://www.ebi.ac.uk/europepmc/webservices/rest/'+pmc+'/fullTextXML',pmc+'.article.xml')
    if article:
     root=ET.fromstring(article)
     ids=[''.join(x.itertext()) for x in root.findall('.//article-id') if x.attrib.get('pub-id-type') in {'pmc','pmcid'}]
     source.require(pmc in ids or pmc[3:] in ids,'Article identity mismatch')
  state['status']='complete-bounded-attempt'
 except Exception as error:state['status']='stopped';state['error']=str(error)
 finally:save()
 return state
if __name__=='__main__':
 import argparse
 p=argparse.ArgumentParser();p.add_argument('--resume-metadata',action='store_true');p.add_argument('--history-metadata',action='store_true');args=p.parse_args()
 s=run(args.resume_metadata,args.history_metadata);print(json.dumps(s,indent=2))
