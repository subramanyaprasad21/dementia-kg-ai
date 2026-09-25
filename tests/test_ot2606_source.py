import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
import ot2606_source as s
import ot2606_assess as a

class HistoricalSource(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.data=s.verify();cls.manifest=s.load(s.MANIFEST)
    def test_exact_eight_and_partition_scope(self):
        expected={x['locator'] for x in s.load(ROOT/'contracts/dementia-evidence-readiness.json')['sourceSlots'] if x['kind']=='evidence'}
        self.assertEqual({r['id'] for r in self.data['records']},expected)
        scan=s.load(s.artifacts()/'ot2606-ep-selective-001/ledger.json')
        self.assertEqual(len(scan['files']),125)
        self.assertEqual(sorted(i for f in scan['files'] for i,n in f['matches'] for _ in range(n)),sorted(i for f in self.manifest['files'] if f['datasource']=='europepmc' for i in f['evidenceIds']))
    def test_deterministic_replay(self):self.assertEqual(s.serialize(s.extract()),s.OUTPUT.read_bytes())
    def test_relocation_and_missing_file(self):
        with tempfile.TemporaryDirectory() as t:
            root=Path(t)
            for f in self.manifest['files']:(root/f['name']).symlink_to(s.artifacts()/f['name'])
            (root/'ot2606-ep-selective-001').symlink_to(s.artifacts()/'ot2606-ep-selective-001',target_is_directory=True)
            self.assertEqual(s.extract(root),self.data)
            (root/self.manifest['files'][0]['name']).unlink()
            with self.assertRaisesRegex(ValueError,'Missing source'):s.verify_inputs(root)
    def test_wrong_release_digest_route_and_permissions(self):
        for key,val in [('edition','26.09')]:
            m=copy.deepcopy(self.manifest);m[key]=val
            with self.assertRaises(ValueError):s.verify_inputs(manifest=m)
        for key,val in [('sha256','0'*64),('url','https://example.invalid/file'),('permissions',{'identifier':'unknown'})]:
            m=copy.deepcopy(self.manifest);m['files'][0][key]=val
            with self.assertRaises(ValueError):s.verify_inputs(manifest=m)
    def test_extra_or_duplicate_requested_record_rejected(self):
        for ident in [self.manifest['files'][0]['evidenceIds'][0],'nonexistent']:
            m=copy.deepcopy(self.manifest);m['files'][0]['evidenceIds'].append(ident)
            with self.assertRaisesRegex(ValueError,'Missing or duplicate'):s.extract(manifest=m,verify_scan=False)
    def test_source_null_absence_and_nested_values(self):
        rows=[s.untyped(r['sourceValues']) for r in self.data['records']]
        ep=next(r for r in rows if r['datasourceId']=='europepmc');cp=next(r for r in rows if r['datasourceId']=='clinical_precedence')
        self.assertEqual(s.field(ep,'diseaseFromSourceId')['state'],'source-absent')
        self.assertEqual(s.field(cp,'trialWhyStopped')['state'],'source-null')
        self.assertIn(None,cp['literature']);self.assertEqual(cp['qualityControls'],[])
        self.assertTrue(ep['textMiningSentences']);self.assertEqual(s.untyped(s.typed(ep)),ep)
        for value in [0.0,-0.0,0.7,2019,[None,'','x']]:self.assertEqual(s.typed(s.untyped(s.typed(value))),s.typed(value))
        with self.assertRaises(ValueError):s.typed(float('nan'))
    def test_description_excludes_capture_and_changes_with_payload(self):
        f=self.manifest['files'][0];r=next(x for x in self.data['records'] if x['lineage']['file']==f['name']);row=s.untyped(r['sourceValues'])
        self.assertEqual(s.description(row,f['schema'],'26.06',f['datasource']),r['description'])
        row['confidence']='synthetic-control'
        self.assertNotEqual(s.description(row,f['schema'],'26.06',f['datasource'])['id'],r['description']['id'])
        with self.assertRaises(ValueError):s.description(row,f['schema'],'26.09',f['datasource'])
    def test_reconciliation_not_full_question_acceptance(self):
        result=a.assess(self.data);self.assertEqual(s.serialize(result),a.OUTPUT.read_bytes())
        self.assertEqual(len(result['slots']),56);self.assertFalse(any(x['fullSourceBackedAcceptance'] for x in result['questions'].values()))
        self.assertEqual(result['comparisonCounts'],{'VERIFIED':53,'DISCREPANT':6})
        mutated=copy.deepcopy(self.data);row=s.untyped(mutated['records'][0]['sourceValues']);row['targetId']='ENSG-invalid-control';mutated['records'][0]['sourceValues']=s.typed(row)
        self.assertGreater(a.assess(mutated)['comparisonCounts']['DISCREPANT'],6)
