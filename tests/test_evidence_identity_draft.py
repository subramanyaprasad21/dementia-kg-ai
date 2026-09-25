import json
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
import m1_fixture_identity as identity


class IdentityDraft(unittest.TestCase):
    def test_inactive_and_approved_keys_only(self):
        d=json.loads((ROOT/'contracts/evidence-identity-draft.json').read_bytes())
        self.assertFalse(d['activation']);self.assertEqual(d['status'],'DRAFT-NOT-APPROVED')
        catalogue=identity.catalogue()
        for kind,keys in d['candidateInputs'].items():self.assertEqual(keys,catalogue[kind])
        self.assertEqual(d['unchangedProfiles'],['m1-id-1','m2-capture-1','m2-source-description-1','m2-rdf-record-1'])

    def test_schema_coverage_and_open_gates(self):
        d=json.loads((ROOT/'contracts/evidence-identity-draft.json').read_bytes())
        ontology=(ROOT/'ontology/dementiagraph-v.ttl').read_text()
        for kind in list(d['candidateInputs'])+d['referents']:
            self.assertIn('dkg:'+kind.split(':')[0]+' rdf:type owl:Class',ontology)
        self.assertTrue(d['sourceSnapshot']['pending']);self.assertTrue(d['diseaseReference']['pending'])
        self.assertTrue(d['unresolved']);self.assertIn('until',d['implementationGate'])
