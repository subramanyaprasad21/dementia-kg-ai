"""Recorded development outputs only; no live calls."""
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
import replay_m5_pilot as pilot

class PilotReplay(unittest.TestCase):
    def test_recorded_outputs_and_accounting_replay_offline(self):
        with patch('urllib.request.OpenerDirector.open',side_effect=AssertionError('Network forbidden')):
            result=pilot.replay()
        self.assertEqual(result,pilot.ai.corpus.read(pilot.DIRECTORY/'summary.json'))
        self.assertEqual(result['completedGenerations'],12)
        self.assertEqual(result['generationAttempts'],14)
        self.assertEqual(sum(r['rdfAccepted'] or 0 for r in result['rows']),24)
        self.assertEqual(result['unrunQuestions'],['Q07'])

    def test_changed_saved_request_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            for name in ['ledger.json','001.prepared.json','001.request.json']:
                (root/name).write_bytes((pilot.DIRECTORY/name).read_bytes())
            request=pilot.ai.corpus.read(root/'001.request.json')
            request['model']='changed-model'
            (root/'001.request.json').write_bytes(pilot.ai.corpus.encode(request))
            with self.assertRaises(AssertionError): pilot.replay(root)
