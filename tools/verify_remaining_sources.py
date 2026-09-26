"""Offline checks and bounded inspection locators for the approved capture attempts."""
import re
import xml.etree.ElementTree as ET
from pathlib import Path
import ot2606_source as source
import ot2606_association_probe as association
import primary_evidence_capture as primary
PATTERNS={'PMC7852392':r'PSEN|presenilin','PMC6742707':r'presenilin|frontotemporal','PMC6298197':r'healthy|N-terminal|efficacy','PMC4054967':r'protofibril|BAN2401'}

def inspect(directory=primary.ROOT):
 root=Path(directory);ledger=source.load(root/'ledger.json');total=0
 source.require(ledger['requests']==len(ledger['records'])<=100,'Request accounting')
 for rec in ledger['records']:
  b=(root/rec['artifact']).read_bytes();source.require(len(b)==rec['bytes'] and source.sha(b)==rec['sha256'],'Changed captured primary artifact');total+=len(b)
 source.require(total==ledger['bytes']<=primary.LIMIT,'Byte accounting')
 metadata=source.load(root/'publication-metadata.json');records=metadata['resultList']['result']
 expected={s['locator'] for s in source.load(source.ROOT/'contracts/dementia-evidence-readiness.json')['sourceSlots'] if s['kind']=='Publication'}
 source.require(metadata['hitCount']==15 and {r['id'] for r in records}==expected,'Wrong publication set')
 out=[]
 for pmc,pattern in PATTERNS.items():
  row=next(r for r in records if r.get('pmcid')==pmc)
  rights=[r for r in ledger['rights'] if r['id']==pmc and r.get('provider')=='Europe PMC']
  source.require(len(rights)==1 and rights[0]['license']==row.get('license') and rights[0]['status']=='LOCAL-ACADEMIC-INSPECTION-ONLY','Unresolved article permissions')
  path=root/(pmc+'.article.xml');tree=ET.fromstring(path.read_bytes())
  ids=[''.join(x.itertext()) for x in tree.findall('.//article-id') if x.attrib.get('pub-id-type') in {'pmc','pmcid'}]
  source.require(pmc in ids or pmc[3:] in ids,'Article identity mismatch')
  paragraphs=list(tree.find('body').iter('p'))
  selected=[(i,' '.join(p.itertext())) for i,p in enumerate(paragraphs) if re.search(pattern,' '.join(p.itertext()),re.I)][:4]
  source.require(bool(selected),'No selected passage')
  out.append(dict(pmcid=pmc,pmid=row['id'],license=row['license'],rawSha256=source.sha(path.read_bytes()),
                  selection=dict(pattern=pattern,flags='IGNORECASE',maximum=4,scope='body descendant p elements in document order; zero-based index; join itertext with spaces'),
                  passages=[dict(bodyParagraphIndex=i,textSha256=source.sha(t.encode())) for i,t in selected],
                  inspection='Selected passages technically inspected by assistant; not exhaustive review or independent biomedical adjudication. Full text retained locally only.'))
 return dict(ledgerSha256=source.sha((root/'ledger.json').read_bytes()),requests=ledger['requests'],bytes=ledger['bytes'],publicationLocators=sorted(expected),articles=out,
             historicalRegistry='Two official history-route probes returned 403; no current version substituted.',panelApp='Exact OT input editions remain unresolved; prior failed endpoint not repeated.')

if __name__=='__main__':
 print(source.serialize(inspect()).decode(),end='')
