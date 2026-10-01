"""Offline challenge freeze and negative controls. No paid calls or private gold."""
import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
import m7_challenge_freeze as m

class ChallengeFreeze(unittest.TestCase):
    def test_public_frozen_replay(self):
        result=m.verify()
        self.assertEqual(result['questions'],12)
        self.assertEqual(result['apiCalls'],0)
        self.assertEqual(result['privateIntegrity'],'not-checked')

    def test_no_holdout_or_gold_fields_in_public_questions(self):
        original=m.read(m.BASE/'questions.json')
        for key,value in [('heldOut',True),('referenceFacts',['invented']),('designation','held-out benchmark')]:
            bad=copy.deepcopy(original);bad[key]=value
            with self.assertRaises(ValueError):m.validate_public(bad)
        bad=copy.deepcopy(original);bad['items'][0]['scoringRubric']={}
        with self.assertRaises(ValueError):m.validate_public(bad)

    def test_allocation_and_scope_not_silently_repaired(self):
        original=m.read(m.BASE/'questions.json')
        for field,value in [('rootIds',[]),('intendedCategory','insufficient'),('question','')]:
            bad=copy.deepcopy(original);bad['items'][0][field]=value
            with self.assertRaises(ValueError):m.validate_public(bad)
        bad=copy.deepcopy(original);bad['items'].pop()
        with self.assertRaises(ValueError):m.validate_public(bad)

    def test_missing_and_changed_artifacts_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'control.json';path.write_text('synthetic control')
            digest=hashlib.sha256(path.read_bytes()).hexdigest();m.check_digest(path,digest)
            path.write_text('changed')
            with self.assertRaises(ValueError):m.check_digest(path,digest)
            path.unlink()
            with self.assertRaises(FileNotFoundError):m.check_digest(path,digest)

    def test_budget_failure_and_review_limits_remain_explicit(self):
        p=m.read(m.BASE/'protocol.json')
        self.assertEqual(m.metrics.budget(p)['formalUSD'],'5.78304')
        self.assertEqual(p['formalRetries'],0)
        self.assertFalse(p['executionAuthorized'])
        self.assertFalse(p['reviewers']['independentReviewCompleted'])
        self.assertEqual(p['reviewers']['interRaterAgreement'],'not calculated or claimed')
        self.assertEqual(p['formalBudget']['generations'],24)
