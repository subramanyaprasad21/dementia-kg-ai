"""Clearly synthetic review controls: no biological payloads or provider records."""
import copy
import hashlib
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
import evaluate_evidence_response as acceptance


def control():
    raw=b'SYNTHETIC review-control artifact; not historical source evidence.'
    review=dict(status='reviewed',reviewer='synthetic-test',basis='synthetic control only',artifact='control',sha256=hashlib.sha256(raw).hexdigest())
    fields={k:dict(state='present',basis='synthetic field-state control; no biomedical value') for k in acceptance.CORE|acceptance.ORIGINAL|acceptance.SPECIFIC['europepmc']}
    rows=[dict(id=i,locator='synthetic:'+i,datasource='europepmc',fields=copy.deepcopy(fields),originalNormalizedSeparate=True) for i in ['CONTROL-E1','CONTROL-E2']]
    d=dict(profile='historical-evidence-review-1',materialKind='synthetic-control',
           release=dict(review,edition='26.06',binding='export-bound'),schema=dict(review,binding='historical-export'),
           permissions=dict(review,use='permitted',retention='permitted',redistribution='restricted',attribution='synthetic condition'),
           export=dict(review,complete=True),accounting=dict(batch='synthetic-batch',complete=True,automaticReset=False,stopReason='complete',attempts=[dict(kind='request',receivedBytes=len(raw))]),
           records=rows,contexts={k:dict(state='verified',basis='synthetic context control') for k in acceptance.CONTEXT})
    return d,{'control':raw}


class ResponseAcceptance(unittest.TestCase):
    def result(self,mutation=lambda d:None):
        d,a=control();mutation(d);return acceptance.evaluate(d,a)

    def test_synthetic_pass_does_not_establish_readiness(self):
        r=self.result();self.assertEqual(r['outcome'],'PASS');self.assertEqual(r['scope'],'synthetic-control-only')
        self.assertFalse(r['activatesSourceContract']);self.assertFalse(r['authorizesAcquisition'])
        self.assertEqual(r['biomedicalSupport'],'NOT ASSESSED')

    def test_partial_records_fields_and_context(self):
        for mutation in [lambda d:d['records'].pop(),lambda d:d['records'][0]['fields'].pop('targetIdentifier'),
                         lambda d:d['contexts']['selection'].update(state='unavailable'),lambda d:d['export'].update(complete=False)]:
            self.assertEqual(self.result(mutation)['outcome'],'PARTIAL')
        def qualified(d):d['records'][0]['fields']['originalDiseaseIdentifier']['state']='source-null'
        r=self.result(qualified);self.assertEqual(r['outcome'],'PASS');self.assertTrue(r['qualifications'])

    def test_incorrect_release_schema_and_lineage_block(self):
        for mutation in [lambda d:d['release'].update(edition='26.09'),lambda d:d['release'].update(binding='label-only'),
                         lambda d:d['schema'].update(binding='current'),lambda d:d['export'].update(sha256='0'*64),
                         lambda d:d['records'][0].update(locator=''),lambda d:d['permissions'].update(retention='unknown'),
                         lambda d:d['records'][0].update(originalNormalizedSeparate=False)]:
            self.assertEqual(self.result(mutation)['outcome'],'BLOCKED')
        d,a=control();self.assertEqual(acceptance.evaluate(d,{})['outcome'],'BLOCKED')

    def test_missing_duplicate_and_unexpected_identifiers(self):
        self.assertEqual(self.result(lambda d:d['records'].append(copy.deepcopy(d['records'][0])))['outcome'],'BLOCKED')
        self.assertEqual(self.result(lambda d:d['records'][0].update(id='UNREQUESTED'))['outcome'],'BLOCKED')
        self.assertEqual(self.result(lambda d:d.update(materialKind='provider-material'))['outcome'],'BLOCKED')

    def test_budget_counts_failures_and_compliant_stop(self):
        def exact(d):
            d['accounting'].update(attempts=[dict(kind='unsuccessful',receivedBytes=10485760)],stopReason='byte-limit')
        self.assertEqual(self.result(exact)['outcome'],'PARTIAL')
        for mutation in [lambda d:d['accounting'].update(attempts=[dict(kind='redirect',receivedBytes=1)]*101),
                         lambda d:d['accounting'].update(attempts=[dict(kind='retry',receivedBytes=10485761)]),
                         lambda d:d['accounting'].update(automaticReset=True),lambda d:d['accounting'].update(complete=False),lambda d:d['accounting'].update(attempts=[])]:
            self.assertEqual(self.result(mutation)['outcome'],'BLOCKED')

    def test_malformed_and_ambiguous_inputs(self):
        for value in [{},None,{'profile':'wrong'}]:self.assertEqual(acceptance.evaluate(value,{})['outcome'],'BLOCKED')
        with self.assertRaises(ValueError):acceptance.load_dossier('{"profile":"a","profile":"b"}')
        self.assertEqual(self.result(lambda d:d['release'].update(edition=['26.06','26.09']))['outcome'],'BLOCKED')
