"""No networking: all provider results are labelled synthetic test controls."""
import copy
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import uuid
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'tools'))
import m5_openai_adapter as adapter
ai = adapter.ai


class OpenAIAdapter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prepared = ai.prepare('gosuranemab mechanism', ['CHEMBL3990042'], 'graph', [str(ai.retrieval.D.MechanismRecord)])

    def fake(self, route, payload, key):
        if route == 'responses/input_tokens':
            return ai.corpus.encode(dict(input_tokens=100, object='response.input_tokens'))
        candidate = dict(answer_text='Synthetic test response, not real model output.', claims=[], unanswered=['Synthetic'])
        return ai.corpus.encode(dict(id='synthetic-response', model=ai.MODEL, status='completed',
                                    usage=dict(input_tokens=100, output_tokens=20),
                                    output=[dict(type='message', content=[dict(type='output_text', text=json.dumps(candidate))])]))

    def test_approval_and_missing_key_fail_before_transport(self):
        with patch.dict(os.environ, {}, clear=True), tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(PermissionError):
                adapter.run(self.prepared, 'retrieval', directory, transport=self.fake)
            with self.assertRaisesRegex(RuntimeError, 'OPENAI_API_KEY is unavailable'):
                adapter.run(self.prepared, 'retrieval', directory, True, self.fake)
            self.assertEqual(list(Path(directory).iterdir()), [])

    def test_three_conditions_preserve_separation(self):
        baseline = ai.request_for(self.prepared, 'model_only')
        retrieved = ai.request_for(self.prepared, 'retrieval')
        self.assertNotIn('packets', json.loads(baseline['input']))
        self.assertEqual(retrieved, ai.request_for(self.prepared, 'verified'))
        self.assertEqual(baseline['model'], retrieved['model'])
        self.assertEqual(baseline['text'], retrieved['text'])

    def test_success_metadata_and_no_credential_persistence(self):
        fake_key = 'TEST_ONLY_'+uuid.uuid4().hex
        with patch.dict(os.environ, {'OPENAI_API_KEY': fake_key}, clear=True), tempfile.TemporaryDirectory() as directory:
            result = adapter.run(self.prepared, 'retrieval', directory, True, self.fake)
            self.assertEqual(result['status'], 'completed')
            self.assertEqual(set(result['result']), {'retrieval', 'verified'})
            ledger = ai.corpus.read(Path(directory)/'ledger.json')
            self.assertEqual((ledger['httpRequests'], ledger['generationCalls']), (2, 1))
            self.assertEqual(ledger['attempts'][0]['usage']['output_tokens'], 20)
            self.assertEqual(ledger['attempts'][0]['promptVersion'], ai.PROMPT_VERSION)
            for path in Path(directory).iterdir():
                self.assertNotIn(fake_key.encode(), path.read_bytes())

    def test_failed_generation_keeps_reservation_and_stops_resume(self):
        fake_key = 'TEST_ONLY_'+uuid.uuid4().hex
        def fail(route, payload, key):
            if route == 'responses/input_tokens':
                return self.fake(route, payload, key)
            raise RuntimeError(key)
        with patch.dict(os.environ, {'OPENAI_API_KEY': fake_key}, clear=True), tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(RuntimeError) as error:
                adapter.run(self.prepared, 'retrieval', directory, True, fail)
            self.assertNotIn(fake_key, str(error.exception))
            ledger = ai.corpus.read(Path(directory)/'ledger.json')
            self.assertEqual(ledger['generationCalls'], 1)
            self.assertGreater(float(ledger['reservedUSD']), 0)
            with self.assertRaisesRegex(RuntimeError, 'Prior incomplete/failed'):
                adapter.run(self.prepared, 'retrieval', directory, True, self.fake)

    def test_input_cap_blocks_generation(self):
        routes = []
        def large(route, payload, key):
            routes.append(route)
            return ai.corpus.encode(dict(input_tokens=100001))
        with patch.dict(os.environ, {'OPENAI_API_KEY': 'TEST_ONLY_'+uuid.uuid4().hex}, clear=True), tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(RuntimeError):
                adapter.run(self.prepared, 'retrieval', directory, True, large)
            self.assertEqual(routes, ['responses/input_tokens'])

    def test_credential_echo_response_is_not_retained(self):
        fake_key = 'TEST_ONLY_'+uuid.uuid4().hex
        def echo(route, payload, key):
            return json.dumps(dict(error=key)).encode()
        with patch.dict(os.environ, {'OPENAI_API_KEY': fake_key}, clear=True), tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(RuntimeError):
                adapter.run(self.prepared, 'retrieval', directory, True, echo)
            for path in Path(directory).iterdir():
                self.assertNotIn(fake_key.encode(), path.read_bytes())

    def test_no_redirects_or_automatic_retry(self):
        self.assertIsNone(adapter.NoRedirect().redirect_request(None, None, 302, '', {}, 'https://other.invalid'))
        with patch.object(adapter.urllib.request, 'build_opener') as opener:
            opener.return_value.open.side_effect = RuntimeError('synthetic provider error')
            with self.assertRaisesRegex(RuntimeError, 'no retry'):
                adapter.post('responses', {}, 'TEST_ONLY_'+uuid.uuid4().hex)
            self.assertEqual(opener.return_value.open.call_count, 1)

    def test_secret_paths_ignored_without_creating_files(self):
        import subprocess
        names = ['.env', '.env.local', 'credentials/local.json', 'local-runs/output.json', 'openai_api_key.txt']
        run = subprocess.run(['git', 'check-ignore', '--stdin'], input='\n'.join(names)+'\n', text=True,
                             capture_output=True, cwd=ai.corpus.ROOT, check=True)
        self.assertEqual(set(run.stdout.splitlines()), set(names))

    def test_call_ceiling_is_cumulative(self):
        with patch.dict(os.environ, {'OPENAI_API_KEY': 'TEST_ONLY_'+uuid.uuid4().hex}, clear=True), tempfile.TemporaryDirectory() as directory:
            adapter.run(self.prepared, 'model_only', directory, True, self.fake)
            path = Path(directory)/'ledger.json'
            ledger = ai.corpus.read(path)
            ledger['generationCalls'] = adapter.LIMITS['generationCalls']
            adapter.save(path, ledger)
            with self.assertRaisesRegex(RuntimeError, 'ceiling'):
                adapter.run(self.prepared, 'retrieval', directory, True, self.fake)

    def test_cost_ceiling_blocks_next_generation(self):
        routes = []
        def counted(route, payload, key):
            routes.append(route)
            return self.fake(route, payload, key)
        with patch.dict(os.environ, {'OPENAI_API_KEY': 'TEST_ONLY_'+uuid.uuid4().hex}, clear=True), tempfile.TemporaryDirectory() as directory:
            adapter.run(self.prepared, 'model_only', directory, True, self.fake)
            path = Path(directory)/'ledger.json'
            ledger = ai.corpus.read(path)
            ledger['reservedUSD'] = '4.99999'
            adapter.save(path, ledger)
            with self.assertRaises(RuntimeError):
                adapter.run(self.prepared, 'retrieval', directory, True, counted)
            self.assertEqual(routes, ['responses/input_tokens'])
