"""Offline replay integrity, not human or biomedical scoring."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import shutil
import unittest
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
import replay_m7_challenge as m

class ResultsReplay(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows=m.runner.requests()

    def test_recorded_results_reproduce_without_human_scores(self):
        with patch.object(m.runner,'requests',return_value=self.rows):
            actual=m.replay()
        self.assertEqual(actual,m.freeze.read(m.DIRECTORY/'verification.json'))
        self.assertIn('PENDING',actual['summary']['humanScoring'])
        for o in actual['outcomes']:
            self.assertEqual(o['humanScoring'],'PENDING-OWNER-REVIEW')
            if 'verified' in o:
                self.assertEqual(o['grounded']['generatedText'],o['verified']['generatedText'])

    def test_changed_raw_response_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/'run';shutil.copytree(m.DIRECTORY,path)
            response=sorted(path.glob('*.generation.response.bin'))[0]
            response.write_bytes(response.read_bytes()+b' ')
            with patch.object(m.runner,'requests',return_value=self.rows):
                with self.assertRaises(AssertionError):m.replay(path)

    def test_changed_reservation_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/'run';shutil.copytree(m.DIRECTORY,path)
            ledger=m.freeze.read(path/'ledger.json');ledger['reservedUSD']='0'
            (path/'ledger.json').write_bytes(m.freeze.corpus.encode(ledger))
            with patch.object(m.runner,'requests',return_value=self.rows):
                with self.assertRaises(AssertionError):m.replay(path)
