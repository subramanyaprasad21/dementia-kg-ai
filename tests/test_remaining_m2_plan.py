"""Offline planning evidence: no source acquisition or KG mutation."""
import json
from pathlib import Path
import sys
import unittest
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import duckdb
import ot2606_source as source

class RemainingM2Plan(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plan = source.load(ROOT / 'assessments/remaining-m2-plan.json')

    def test_authorities_and_exact_slot_coverage(self):
        for path, digest in self.plan['authorities'].items():
            self.assertEqual(source.sha((ROOT / path).read_bytes()), digest)
        original = source.load(ROOT / 'contracts/dementia-evidence-readiness.json')['sourceSlots']
        previous = source.load(ROOT / 'assessments/ot2606-evidence-001.readiness.json')['slots']
        self.assertEqual(len(self.plan['slots']), 56)
        self.assertEqual([s['id'] for s in self.plan['slots']], [s['id'] for s in original])
        self.assertEqual([s['priorStatus'] for s in self.plan['slots']], [s['status'] for s in previous])
        for actual, expected in zip(self.plan['slots'], original):
            self.assertEqual(actual['locator'], expected['locator'])
            self.assertEqual(actual['questions'], expected['questions'])

    def test_offline_query_replay_and_absent_locator_control(self):
        source.verify_inputs()
        db = duckdb.connect()
        try:
            for query in self.plan['offlineQueries']:
                path = source.artifacts() / query['file']
                self.assertEqual(source.sha(path.read_bytes()), query['sha256'])
                actual = db.execute(query['sql'], [str(path)] + query['parameters']).fetchall()
                self.assertEqual([list(row) for row in actual], query['results'])
                changed = list(query['parameters'])
                # Change all bounded identifiers. This exercises the query itself,
                # not merely an artifact hash failure or a fixed rejection label.
                changed = ['nonexistent-planning-control' for _ in changed]
                self.assertEqual(db.execute(query['sql'], [str(path)] + changed).fetchall(), [])
        finally:
            db.close()

    def test_locator_satisfaction_does_not_promote_claims(self):
        fulfilled = [s for s in self.plan['slots'] if s['locatorOnlySatisfied']]
        self.assertEqual(len(fulfilled), 21)
        self.assertTrue(all(s['operation'] == 'reference' for s in fulfilled))
        self.assertTrue(all(s['questionAcceptance'] == 'NOT ASSESSED BY SLOT PRESENCE' for s in self.plan['slots']))
        self.assertEqual({s['id'] for s in self.plan['slots'] if s['operation'] == 'panel'}, {'panel-265', 'panel-474', 'panel-540'})
        self.assertFalse(any(s['locatorOnlySatisfied'] for s in self.plan['slots'] if s['operation'] in {'registry', 'mechanism', 'indication', 'association', 'selection', 'passage'}))
