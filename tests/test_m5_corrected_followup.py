"""Amendment/accounting controls use local snapshots and mocked transport only."""
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
import run_m5_corrected_followup as f

class FollowupAccounting(unittest.TestCase):
    def test_explicit_amendment_preserves_history_and_refuses_repeat(self):
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'ledger.json';path.write_bytes((f.BASE/'ledger.json').read_bytes())
            original=f.ai.corpus.read(path)
            f.amend(directory);after=f.ai.corpus.read(path)
            for key in ['attempts','reservedUSD','httpRequests','generationCalls','id']:
                self.assertEqual(original[key],after[key])
            self.assertEqual(after['limits']['generationCalls'],22)
            self.assertEqual(after['limits']['httpRequests'],44)
            self.assertEqual(after['followupAuthorization']['priorLimits'],original['limits'])
            with self.assertRaises(ValueError):f.amend(directory)

    def test_followup_mock_call_keeps_old_attempts_and_requires_existing_ledger(self):
        p=f.plan.prepare('Q07')
        def fake(route,payload,key):
            if route=='responses/input_tokens':return b'{"input_tokens":100}'
            return f.ai.corpus.encode(dict(id='synthetic',model=f.ai.MODEL,status='completed',usage=dict(input_tokens=100,output_tokens=10),output=[dict(type='message',content=[dict(type='output_text',text=json.dumps(dict(answer_text='Synthetic control',claims=[],unanswered=['Synthetic'])))])]))
        with patch.dict(os.environ,{'OPENAI_API_KEY':'TEST_ONLY_KEY'},clear=True),tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):f.adapter.run(p,'model_only',directory,True,fake,corrected_followup=True)
            path=Path(directory)/'ledger.json';path.write_bytes((f.BASE/'ledger.json').read_bytes());f.amend(directory)
            f.adapter.run(p,'model_only',directory,True,fake,reviewed_failure_ids=f.REVIEWED,corrected_followup=True)
            ledger=f.ai.corpus.read(path)
            self.assertEqual(ledger['attempts'][:14],f.ai.corpus.read(f.BASE/'ledger.json')['attempts'])
            self.assertEqual((ledger['generationCalls'],ledger['httpRequests']),(15,30))
            self.assertEqual(ledger['reservedUSD'],'0.848882')

    def test_recorded_followup_replays_offline_and_keeps_timeout_visible(self):
        import replay_m5_corrected_followup as r
        with patch('urllib.request.OpenerDirector.open',side_effect=AssertionError('Network forbidden')):
            result=r.replay()
        self.assertEqual(result,f.ai.corpus.read(r.DIRECTORY/'summary.json'))
        self.assertEqual((result['completedNewGenerations'],result['failedNewGenerations']),(7,1))
        self.assertFalse(result['rows'][-1]['comparableDevelopmentOutputs'])
        self.assertEqual(result['failures'][0]['diagnostic']['category'],'timeout')
