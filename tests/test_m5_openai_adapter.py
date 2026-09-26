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
                adapter.post('responses', ai.request_for(self.prepared, 'model_only'), 'TEST_ONLY_'+uuid.uuid4().hex)
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


class SafeDiagnostics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prepared = ai.prepare('gosuranemab mechanism', ['CHEMBL3990042'], 'graph', [str(ai.retrieval.D.MechanismRecord)])
        cls.request = ai.request_for(cls.prepared, 'model_only')

    def test_serialization_and_schema(self):
        from jsonschema import Draft202012Validator
        Draft202012Validator.check_schema(self.request['text']['format']['schema'])
        raw = adapter.validate_request('responses', self.request)
        self.assertEqual(json.loads(raw), self.request)
        self.assertEqual(raw, ai.corpus.encode(self.request))

    def test_invalid_contract_fields_block_http(self):
        cases = [('model', 'other', 'model_not_approved'),
                 ('reasoning', {'effort': 'invalid'}, 'reasoning_not_approved'),
                 ('text', {'format': {'type': 'json_schema'}}, 'structured_output_invalid'),
                 ('tools', [{}], 'tools_not_approved'),
                 ('max_output_tokens', 0, 'configuration_not_approved'),
                 ('input', None, 'payload_invalid'),
                 ('input', object(), 'serialization_invalid')]
        for field, value, expected in cases:
            request = copy.deepcopy(self.request)
            request[field] = value
            with self.subTest(field=field, expected=expected), patch.object(adapter.urllib.request, 'build_opener') as opener:
                with self.assertRaises(adapter.DiagnosticError) as caught:
                    adapter.post('responses', request, 'TEST_ONLY_KEY')
                self.assertEqual(caught.exception.diagnostic['category'], expected)
                opener.assert_not_called()
        request = dict(self.request, max_tokens=4096)
        with self.assertRaises(adapter.DiagnosticError) as caught:
            adapter.validate_request('responses', request)
        self.assertEqual(caught.exception.diagnostic['category'], 'request_fields_invalid')
        with self.assertRaises(adapter.DiagnosticError) as caught:
            adapter.validate_request('chat/completions', self.request)
        self.assertEqual(caught.exception.diagnostic['category'], 'endpoint_invalid')

    def test_construction_failure_is_pretransmission(self):
        with patch.object(adapter.urllib.request, 'Request', side_effect=ValueError('SECRET')):
            with self.assertRaises(adapter.DiagnosticError) as caught:
                adapter.post('responses', self.request, 'TEST_ONLY_KEY')
        self.assertEqual(caught.exception.diagnostic['transmission'], 'not_started')
        self.assertNotIn('SECRET', str(caught.exception.diagnostic))

    def test_http_metadata_allowlist_and_secret_suppression(self):
        import io
        for body, expected in [({'error': {'code': 'unsupported_parameter', 'type': 'invalid_request_error', 'param': 'reasoning.effort', 'message': 'PRIVATE MESSAGE'}}, 'unsupported_parameter'),
                               ({'error': {'code': 'SECRET', 'message': 'TEST_ONLY_KEY'}}, 'unclassified')]:
            error = adapter.urllib.error.HTTPError('https://api.openai.com/v1/responses', 400, 'PRIVATE', {'Authorization': 'PRIVATE'}, io.BytesIO(json.dumps(body).encode()))
            with patch.object(adapter.urllib.request, 'build_opener') as opener:
                opener.return_value.open.side_effect = error
                with self.assertRaises(adapter.DiagnosticError) as caught:
                    adapter.post('responses', self.request, 'TEST_ONLY_KEY')
                opener.return_value.open.assert_called_once()
            diag = caught.exception.diagnostic
            self.assertEqual(diag['httpStatus'], 400)
            self.assertEqual(diag['api_code'], expected)
            for secret in ['PRIVATE', 'SECRET', 'TEST_ONLY_KEY', 'Authorization']:
                self.assertNotIn(secret, json.dumps(diag))

    def test_network_failures_are_not_overstated_as_unsent(self):
        for error, category in [(TimeoutError('PRIVATE'), 'timeout'), (adapter.urllib.error.URLError('PRIVATE'), 'connection_error')]:
            with patch.object(adapter.urllib.request, 'build_opener') as opener:
                opener.return_value.open.side_effect = error
                with self.assertRaises(adapter.DiagnosticError) as caught:
                    adapter.post('responses', self.request, 'TEST_ONLY_KEY')
            self.assertEqual(caught.exception.diagnostic['category'], category)
            self.assertEqual(caught.exception.diagnostic['transmission'], 'unknown')

    def test_method_endpoint_timeout_and_serialized_body(self):
        with patch.object(adapter.urllib.request, 'build_opener') as opener:
            opener.return_value.open.return_value.__enter__.return_value.read.return_value = b'{}'
            adapter.post('responses', self.request, 'TEST_ONLY_KEY')
            args, kwargs = opener.return_value.open.call_args
            self.assertEqual(args[0].full_url, 'https://api.openai.com/v1/responses')
            self.assertEqual(args[0].get_method(), 'POST')
            self.assertEqual(args[0].data, ai.corpus.encode(self.request))
            self.assertEqual(kwargs['timeout'], 120)
            opener.return_value.open.assert_called_once()

    def test_diagnostic_persisted_without_refund_or_retry(self):
        def transport(route, payload, key):
            if route == 'responses/input_tokens':
                return b'{"input_tokens":224}'
            raise adapter.DiagnosticError('http_rejection', 'http_response', httpStatus=400)
        with patch.dict(os.environ, {'OPENAI_API_KEY': 'TEST_ONLY_KEY'}, clear=True), tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(RuntimeError):
                adapter.run(self.prepared, 'model_only', directory, True, transport)
            ledger = ai.corpus.read(Path(directory)/'ledger.json')
            self.assertEqual(ledger['attempts'][0]['diagnostic']['httpStatus'], 400)
            self.assertEqual(ledger['httpRequests'], 2)
            self.assertEqual(ledger['generationCalls'], 1)
            self.assertEqual(ledger['reservedUSD'], '0.041408')
            with self.assertRaisesRegex(RuntimeError, 'Prior incomplete/failed'):
                adapter.run(self.prepared, 'model_only', directory, True, transport)


    def test_explicit_review_preserves_failure_and_blocks_new_failure(self):
        def transport(route, payload, key):
            if route == 'responses/input_tokens':
                return b'{"input_tokens":224}'
            raise adapter.DiagnosticError('http_rejection', 'http_response', httpStatus=400)
        with patch.dict(os.environ, {'OPENAI_API_KEY': 'TEST_ONLY_KEY'}, clear=True), tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(RuntimeError):
                adapter.run(self.prepared, 'model_only', directory, True, transport)
            original = ai.corpus.read(Path(directory)/'ledger.json')
            reviewed = [original['attempts'][0]['runId']]
            with self.assertRaises(RuntimeError):
                adapter.run(self.prepared, 'model_only', directory, True, transport, reviewed)
            after = ai.corpus.read(Path(directory)/'ledger.json')
            self.assertEqual(after['attempts'][0], original['attempts'][0])
            self.assertEqual(after['reservedUSD'], '0.082816')
            self.assertEqual((after['httpRequests'], after['generationCalls']), (4, 2))
            self.assertEqual(after['attempts'][1]['ownerReviewedFailureIds'], reviewed)
            with self.assertRaisesRegex(RuntimeError, 'Prior incomplete/failed'):
                adapter.run(self.prepared, 'model_only', directory, True, transport, reviewed)
