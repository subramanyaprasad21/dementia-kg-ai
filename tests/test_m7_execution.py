"""Synthetic transport responses only; no model calls or answer scoring."""
import copy
import json
from decimal import Decimal
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
import run_m7_challenge as m

class Execution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows=m.requests()

    def response(self,route,payload,key):
        obj={'input_tokens':100} if route.endswith('input_tokens') else dict(model='gpt-6-sol',status='completed',output=[],usage=dict(input_tokens=100,output_tokens=10,input_tokens_details=dict(cached_tokens=20,cache_write_tokens=50)))
        return dict(raw=json.dumps(obj).encode(),status=200,requestId='synthetic-request')

    def execute(self,call,prior=Decimal('1.544974'),rows=None):
        with tempfile.TemporaryDirectory() as d:
            result=m.execute(rows or self.rows,Path(d)/'run',prior,call,'mock-secret-not-real')
            files={p.name:p.read_bytes() for p in (Path(d)/'run').iterdir()}
            return result,files

    def test_frozen_order_integrity_and_config(self):
        self.assertEqual(len(self.rows),24)
        for row in self.rows:
            p=row['request']
            self.assertEqual(p['model'],'gpt-6-sol')
            self.assertEqual(p['reasoning'],{'effort':'low'})
            self.assertEqual(p['max_output_tokens'],4096)
            self.assertEqual(p['tools'],[])
            self.assertTrue(p['text']['format']['strict'])
        for field,value in [('model','other'),('reasoning',{'effort':'high'}),('max_output_tokens',8192),('tools',[{}]),('input','changed')]:
            rows=copy.deepcopy(self.rows);rows[0]['request'][field]=value
            call=Mock()
            with self.assertRaises((ValueError,m.shared.DiagnosticError)):self.execute(call,rows=rows)
            call.assert_not_called()

    def test_dry_run_never_calls_transport_or_reads_key(self):
        call=Mock(side_effect=AssertionError('network'))
        with patch.object(m,'requests',return_value=self.rows),patch.dict(m.os.environ,{},clear=True):
            result=m.run(call=call)
        call.assert_not_called()
        self.assertEqual(result['apiCalls'],0)
        self.assertTrue(result['estimatedFits'])
        self.assertIn('ESTIMATE',result['inputTokenStatus'])

    def test_live_requires_explicit_authorization(self):
        with patch.object(m,'requests',return_value=self.rows):
            with self.assertRaises(PermissionError):m.run(live=True)

    def test_24_calls_raw_preservation_no_scoring(self):
        call=Mock(side_effect=self.response)
        with patch.object(m.freeze.ai,'verify',side_effect=AssertionError('No scoring')):
            result,files=self.execute(call)
        self.assertEqual(call.call_count,48)
        self.assertEqual(result['generations'],24)
        self.assertEqual(result['status'],'execution-completed-unscored')
        self.assertEqual(len([x for x in files if x.endswith('.response.bin')]),48)
        self.assertEqual(result['attempts'][0]['actualCostUSD'],'0.000289')
        self.assertNotIn('result.json',files)

    def test_generation_limit_rejects_extra_or_missing(self):
        for rows in (self.rows+self.rows[:1],self.rows[:-1],list(reversed(self.rows))):
            call=Mock()
            with self.assertRaises(ValueError):self.execute(call,rows=rows)
            call.assert_not_called()

    def test_api_failure_retained_and_no_retry(self):
        def response(route,payload,key):
            if route=='responses':return dict(raw=b'{"error":"synthetic"}',status=400,requestId=None)
            return self.response(route,payload,key)
        call=Mock(side_effect=response)
        result,files=self.execute(call)
        self.assertEqual(call.call_count,2)
        self.assertEqual(result['generations'],1)
        self.assertEqual(result['status'],'stopped-review-required')
        self.assertEqual(files['01.generation.response.bin'],b'{"error":"synthetic"}')
        self.assertIsNone(result['attempts'][0]['actualCostUSD'])
        self.assertGreater(Decimal(result['reservedUSD']),Decimal('1.544974'))

    def test_transport_exception_no_retry(self):
        call=Mock(side_effect=TimeoutError('do not persist sensitive exceptions'))
        result,files=self.execute(call)
        self.assertEqual(call.call_count,1)
        self.assertEqual(result['status'],'stopped-review-required')
        self.assertNotIn(b'sensitive exceptions',files['ledger.json'])

    def test_cap_blocks_generation_after_count(self):
        call=Mock(side_effect=self.response)
        result,_=self.execute(call,prior=Decimal('7.49'))
        self.assertEqual(call.call_count,1)
        self.assertEqual(result['generations'],0)
        self.assertEqual(result['reservedUSD'],'7.49')

    def test_cap_blocks_even_count_at_exhaustion(self):
        call=Mock(side_effect=self.response)
        result,_=self.execute(call,prior=Decimal('7.50'))
        call.assert_not_called()
        self.assertEqual(result['httpRequests'],0)

    def test_cache_write_reservation_and_invalid_counts(self):
        self.assertEqual(m.cost(100000),Decimal('.290960'))
        for n in (-1,True,100001,'100'):
            with self.assertRaises(ValueError):m.cost(n)

    def test_unsafe_response_and_usage_drift_stop(self):
        for raw in (b'mock-secret-not-real',b'not json',json.dumps(dict(model='other',usage=dict(input_tokens=100,output_tokens=10))).encode()):
            def response(route,payload,key):
                return self.response(route,payload,key) if route.endswith('input_tokens') else dict(raw=raw,status=200,requestId=None)
            call=Mock(side_effect=response)
            result,files=self.execute(call)
            self.assertEqual(call.call_count,2)
            self.assertEqual(result['status'],'stopped-review-required')
            self.assertTrue(all(b'mock-secret-not-real' not in b for b in files.values()))

    def test_transport_timeout_endpoint_and_no_retry(self):
        response=Mock();response.__enter__=Mock(return_value=response);response.__exit__=Mock(return_value=False)
        response.read.return_value=b'{}';response.code=200;response.headers={'x-request-id':'test-id'}
        opener=Mock();opener.open.return_value=response
        with patch.object(m.urllib.request,'build_opener',return_value=opener):
            result=m.transport('responses',self.rows[0]['request'],'mock-secret-not-real')
        self.assertEqual(opener.open.call_count,1)
        self.assertEqual(opener.open.call_args.kwargs,{'timeout':120})
        self.assertEqual(opener.open.call_args.args[0].full_url,'https://api.openai.com/v1/responses')
        self.assertEqual(result['raw'],b'{}')

    def test_existing_run_cannot_be_overwritten(self):
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/'run';path.mkdir()
            call=Mock()
            with self.assertRaises(FileExistsError):m.execute(self.rows,path,Decimal('1.544974'),call,'mock-secret-not-real')
            call.assert_not_called()

    def test_prior_ledger_cannot_reset(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'ledger.json';p.write_text('{"reservedUSD":"0"}')
            with self.assertRaises(ValueError):m.prior_reservation(p)

    def test_budget_rechecked_mid_batch_without_refunds(self):
        def response(route,payload,key):
            if route.endswith('input_tokens'):
                return dict(raw=b'{"input_tokens":100000}',status=200,requestId=None)
            return self.response(route,payload,key)
        call=Mock(side_effect=response)
        result,_=self.execute(call)
        self.assertEqual(result['generations'],20)
        self.assertEqual(call.call_count,41)
        self.assertEqual(result['reservedUSD'],'7.364174')
        self.assertEqual(result['status'],'stopped-review-required')
