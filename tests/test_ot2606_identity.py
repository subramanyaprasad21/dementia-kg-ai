import copy
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'tools'))
import ot2606_source as s
import ot2606_identity as i
import ot2606_rdf as r

class LiveIdentity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.data=s.load(s.OUTPUT);cls.graph,cls.bundle,cls.info=r.build(cls.data)
    def test_replay_and_source_payload_revision(self):
        self.assertEqual(r.build(self.data)[1],self.bundle)
        original=next(x for x in self.bundle['records'].values() if x['receipt']['kind']=='SourceSnapshot');rec=original['receipt']
        payload=copy.deepcopy(original['payload']);payload.append(r.A('limitationText','Synthetic changed description'))
        changed=i.receipt('SourceSnapshot',rec['origin'],rec['inputs'],payload)
        self.assertNotEqual(i.core.identify(changed),original['iri'])
    def test_wrong_origin_kind_and_old_snapshot_rejected(self):
        entry=next(x for x in self.bundle['records'].values() if x['receipt']['kind']=='EvidenceOccurrence');rec=entry['receipt']
        with self.assertRaises(ValueError):i.receipt('EvidenceOccurrence','audit-transcription',rec['inputs'],entry['payload'])
        with self.assertRaises(ValueError):i.receipt('MechanismRecord','live-source-derived',{},[])
        bad=dict(rec['inputs'],snapshotKey='urn:old-audit-snapshot')
        with self.assertRaises(ValueError):i.Registry(self.data).add('EvidenceOccurrence',bad,entry['payload'])
    def test_collision_and_conflicting_supplied_iri(self):
        e=next(x for x in self.bundle['records'].values() if x['receipt']['kind']=='SourceSnapshot');reg=i.Registry(self.data);rec=e['receipt']
        with self.assertRaises(ValueError):reg.add('SourceSnapshot',rec['inputs'],e['payload'],iri='urn:wrong')
        iri=reg.add('SourceSnapshot',rec['inputs'],e['payload']);reg.entries[iri]['payload']=[]
        with self.assertRaises(ValueError):reg.add('SourceSnapshot',rec['inputs'],e['payload'])
    def test_description_integrity_and_capture_separation(self):
        data=copy.deepcopy(self.data);data['records'][0]['sourceValues']['value']['id']['value']='changed'
        with self.assertRaises(ValueError):i.Registry(data)
        data=copy.deepcopy(self.data);data['records'][0]['lineage']['captureId']='urn:new-encounter-control'
        self.assertEqual(r.build(data)[1]['records'],self.bundle['records'])
        self.assertNotEqual(r.build(data)[1]['extractionSha256'],self.bundle['extractionSha256'])
    def test_membership_explanation_identity_and_collision(self):
        e=next(x for x in self.bundle['records'].values() if x['receipt']['kind']=='SelectionMembership');rec=e['receipt'];payload=e['payload']+[r.A('rationale','Later explanation control')]
        self.assertEqual(i.core.identify(i.receipt(rec['kind'],rec['origin'],rec['inputs'],payload)),e['iri'])
        reg=i.Registry(self.data);reg.entries=copy.deepcopy(self.bundle['records'])
        with self.assertRaises(ValueError):reg.add(rec['kind'],rec['inputs'],payload)
    def test_roles_and_contextual_references_remain_distinct(self):
        v=[x for x in self.info.values() if x['row'].get('diseaseFromSourceId')=='OMIM:600274']
        self.assertEqual(len(v),2);self.assertNotEqual(v[0]['original'],v[1]['original']);self.assertNotEqual(v[0]['normalized'],v[1]['normalized'])
        self.assertEqual({x['row']['diseaseId'] for x in v},{'MONDO_0017276','MONDO_0010857'})
        self.assertEqual(len({x['occurrence'] for x in self.info.values()}),8)
