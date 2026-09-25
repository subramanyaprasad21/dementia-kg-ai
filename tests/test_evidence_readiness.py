"""Static contract checks; no biomedical acquisition or invented source records."""
import hashlib
import json
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PATH=ROOT/'contracts/dementia-evidence-readiness.json'


class ReadinessContract(unittest.TestCase):
    def setUp(self): self.c=json.loads(PATH.read_bytes())

    def test_authorities_and_question_slots_preserved(self):
        for item in self.c['authorities']:
            self.assertEqual(hashlib.sha256((ROOT/item['path']).read_bytes()).hexdigest(),item['sha256'])
        spec=json.loads((ROOT/'fixtures/m1/audit_fixture_spec.json').read_bytes())
        self.assertEqual(set(self.c['questionRequirements']),set(spec['questions']))
        for q,req in self.c['questionRequirements'].items():
            self.assertEqual(req['requiredAuditRecords'],spec['questions'][q]['required_records'])
            self.assertEqual(req['unavailableInAudit'],spec['questions'][q]['unavailable_in_audit'])
            self.assertEqual(req['sourceBackedStatus'],'incomplete')

    def test_eight_evidence_ids_are_from_pinned_audit(self):
        spec=json.loads((ROOT/'fixtures/m1/audit_fixture_spec.json').read_bytes())
        expected={r['inputs']['sourceRecordId'] for r in spec['records'] if r['kind']=='EvidenceOccurrence'}
        actual={s['locator'] for s in self.c['sourceSlots'] if s['kind']=='evidence'}
        self.assertEqual(actual,expected);self.assertEqual(len(actual),8)

    def test_finite_scope_and_no_audit_promotion(self):
        slots=self.c['sourceSlots']
        self.assertEqual(len(slots),56);self.assertEqual(len({s['id'] for s in slots}),56)
        available=[s for s in slots if s['availability']=='frozen-source-backed']
        self.assertEqual([s['id'] for s in available],['mondo'])
        self.assertEqual(self.c['auditFixtures']['status'],'audit-transcription-not-source-reproduction')
        self.assertEqual(sum(s['kind']=='conditional-full-text' for s in slots),4)
        self.assertEqual(sum(s['kind']=='Publication' for s in slots),15)

    def test_limits_and_unknown_projections(self):
        self.assertEqual(self.c['limits']['requests'],100)
        self.assertEqual(self.c['limits']['bytes'],10485760)
        self.assertFalse(self.c['limits']['automaticReset'])
        self.assertTrue(self.c['projectionRequirements']['evidence']['rawPaths'].startswith('UNVERIFIED'))
        self.assertEqual(self.c['status'],'offline-planning-only')
