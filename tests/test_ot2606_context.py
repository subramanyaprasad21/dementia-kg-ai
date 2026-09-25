"""Offline capture controls; synthetic bytes are not biomedical evidence."""
import copy
import io
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
import ot2606_context as c

class Response(io.BytesIO):
    def __init__(self, body, code=200):
        super().__init__(body);self.code=code;self.headers={'Content-Length':str(len(body))}

class ContextCapture(unittest.TestCase):
    def test_finite_authorized_plan(self):
        self.assertEqual(len(c.files()),4)
        self.assertEqual(sum(x['bytes'] for x in c.files()),12702710)
        self.assertTrue(all('/26.06/output/' in x['url'] for x in c.files()))
        self.assertEqual(c.MAX_BYTES,20*1024*1024)
        self.assertEqual(c.MAX_REQUESTS,100)

    def synthetic(self, directory, bodies=None, code=200):
        body=b'PAR1synthetic-controlPAR1'
        plan=[dict(partition='synthetic',name=str(i)+'.parquet',url='https://example.invalid/'+str(i),bytes=len(body)) for i in range(4)]
        responses=[Response(b,code) for b in (bodies or [body]*4)]
        with patch.object(c,'files',return_value=plan),patch.object(c.urllib.request,'build_opener') as opener:
            opener.return_value.open.side_effect=responses
            result=c.capture(directory)
            c.verify(directory)
        return result

    def test_capture_replay_and_no_reset(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/'capture';state=self.synthetic(root)
            self.assertEqual(state['requests'],4)
            self.assertEqual(state['receivedBodyBytes'],4*len(b'PAR1synthetic-controlPAR1'))
            with self.assertRaises(FileExistsError):c.capture(root)

    def test_failed_response_body_counted(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/'capture'
            with self.assertRaisesRegex(ValueError,'HTTP failure'):self.synthetic(root,code=503)
            state=c.source.load(root/'ledger.json')
            self.assertEqual(state['requests'],1)
            self.assertEqual(state['receivedBodyBytes'],len(b'PAR1synthetic-controlPAR1'))
            self.assertEqual(state['status'],'stopped')

    def test_budget_and_truncation_stop(self):
        with tempfile.TemporaryDirectory() as tmp:
            with patch.object(c,'MAX_BYTES',1):
                with self.assertRaisesRegex(ValueError,'Byte ceiling'):self.synthetic(Path(tmp)/'budget')
            with self.assertRaisesRegex(ValueError,'size mismatch'):
                self.synthetic(Path(tmp)/'truncated',bodies=[b'PAR1xPAR1']*4)

    def test_request_digest_and_body_tampering(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/'capture';self.synthetic(root)
            state=c.source.load(root/'ledger.json');plan=[dict(partition='synthetic',name=str(i)+'.parquet',url='https://example.invalid/'+str(i),bytes=len(b'PAR1synthetic-controlPAR1')) for i in range(4)]
            with patch.object(c,'files',return_value=plan):
                changed=copy.deepcopy(state);changed['records'][0]['request']['headers']['X']='altered'
                (root/'ledger.json').write_bytes(c.source.serialize(changed))
                with self.assertRaisesRegex(ValueError,'Request digest'):c.verify(root)
                (root/'ledger.json').write_bytes(c.source.serialize(state))
                (root/'0.parquet').write_bytes(b'changed')
                with self.assertRaisesRegex(ValueError,'digest/size'):c.verify(root)

class HistoricalContext(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=c.extract()

    def test_exact_capture_and_extraction_replay(self):
        state=c.verify()
        self.assertEqual(state['requests'],4)
        self.assertEqual(state['receivedBodyBytes'],12702710)
        self.assertEqual(c.source.serialize(state),(ROOT/'manifests/ot2606-context-001.capture.json').read_bytes())
        self.assertEqual(c.source.serialize(self.data),(ROOT/'extractions/ot2606-context-001.json').read_bytes())
        self.assertEqual(len(self.data['records']),16)
        terms=[c.source.untyped(r['sourceValues'])['id'] for r in self.data['records'] if r['partition']=='disease']
        self.assertEqual(set(terms),set(c.TERMS))
        readiness=c.source.load(ROOT/'assessments/ot2606-context-001.readiness.json')
        contract=c.source.load(ROOT/'contracts/dementia-evidence-readiness.json')
        self.assertEqual([s['id'] for s in readiness['slots']],[s['id'] for s in contract['sourceSlots']])
        self.assertFalse(readiness['fullCorpusAccepted'])
        locators=set()
        old=c.source.load(ROOT/'extractions/ot2606-evidence-001.json')
        for rec in old['records']:
            row=c.source.untyped(rec['sourceValues'])
            locators.add(row['targetId']);locators.add(row.get('drugId'))
            locators.update(row['literature'])
        for rec in self.data['records']:
            row=c.source.untyped(rec['sourceValues'])
            if rec['partition']=='drug_mechanism_of_action':
                locators.update(row['chemblIds'])
                for ref in row['references']:
                    if ref['source']=='PubMed':locators.update(ref['ids'])
        references=[s for s in contract['sourceSlots'] if s['provider']=='reported-authority-reference']
        self.assertEqual(len(references),24)
        self.assertTrue(all(s['locator'] in locators for s in references))

    def test_mechanisms_and_indications_are_separate(self):
        mechanisms=[c.source.untyped(r['sourceValues']) for r in self.data['records'] if r['partition']=='drug_mechanism_of_action']
        indications=[c.source.untyped(r['sourceValues']) for r in self.data['records'] if r['partition']=='clinical_indication']
        self.assertEqual(len(mechanisms),4);self.assertEqual(len(indications),4)
        mem=next(r for r in mechanisms if 'CHEMBL807' in r['chemblIds'])
        self.assertEqual(mem['targetType'],'protein complex group')
        self.assertTrue({'ENSG00000176884','ENSG00000116032'} <= set(mem['targets']))
        self.assertNotIn('id',mem) # No invented upstream mechanism ID.
        gos=next(r for r in indications if r['drugId']=='CHEMBL3990042')
        self.assertEqual(gos['id'],'c680c47a8cc2571635e1d5c629e51834273a3e67d25ebedfa9e58b729ad65189')
        self.assertEqual(gos['clinicalReportIds'],['nct03658135'])
        zago=[r['diseaseId'] for r in indications if r['drugId']=='CHEMBL4298021']
        self.assertEqual(set(zago),{'MONDO_0004975','MONDO_0005574'})
        self.assertFalse(any('efficacy' in r for r in indications))

    def test_local_selection_extent_and_diagnostic_membership(self):
        selections=c.selections()
        self.assertEqual(c.source.serialize(selections),(ROOT/'assessments/ot2606-context-001.selections.json').read_bytes())
        self.assertEqual([r['count'] for r in selections],[0,1,3,10])
        self.assertEqual(selections[1]['members'][0]['id'],'8bac3794c7e23d4dc3e7b44e3b2e1af8dcccc4fe')
        self.assertIn('019b39b2b176f9e7df8536022682738d12e32f39',{r['id'] for r in selections[3]['members']})
        self.assertNotIn('019b39b2b176f9e7df8536022682738d12e32f39',{r['id'] for r in selections[2]['members']})

    def test_relocation_and_corrupt_capture_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            for f in c.files():(root/f['name']).symlink_to(c.DEFAULT/f['name'])
            ledger=(c.DEFAULT/'ledger.json').read_bytes();(root/'ledger.json').write_bytes(ledger)
            self.assertEqual(c.extract(root),self.data)
            state=c.source.load(root/'ledger.json');state['edition']='26.09'
            (root/'ledger.json').write_bytes(c.source.serialize(state))
            with self.assertRaisesRegex(ValueError,'edition'):c.extract(root)
            (root/'ledger.json').write_bytes(ledger)
            (root/c.files()[0]['name']).unlink()
            with self.assertRaises(FileNotFoundError):c.extract(root)
