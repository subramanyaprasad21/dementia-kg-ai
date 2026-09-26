"""Synthetic candidate controls only; no real model execution/results."""
import copy
import json
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'tools'))
import m5_evidence_answers as m


class EvidenceAnswers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prepared = m.prepare('gosuranemab mechanism', ['CHEMBL3990042'], 'graph',
                                 [str(m.retrieval.D.MechanismRecord)])
        packet = cls.prepared['retrieval']['results'][0]['packet']
        statement = next(line for line in packet['text'].splitlines()
                         if line.startswith('<'+packet['id']+'>') and 'ontology#sourceText>' in line)
        cls.candidate = dict(answer_text='Synthetic candidate, not a model result.', claims=[dict(packet_id=packet['id'], statement=statement,
                                        claim_type='source_assertion', explanation='Synthetic unverified prose.')], unanswered=[])

    def test_positive_assertion_with_unverified_prose(self):
        result = m.verify(self.prepared, self.candidate)
        self.assertEqual(len(result['acceptedAssertions']), 1)
        self.assertEqual(result['decisions'][0]['status'], 'RDF-ASSERTION-SUPPORTED')
        self.assertEqual(result['decisions'][0]['explanationStatus'], 'UNVERIFIED-MANUAL-REVIEW-REQUIRED')

    def test_invented_statement_and_forged_citation_blocked(self):
        for field, value in [('statement', '<urn:invented> <urn:cures> <urn:dementia> .'),
                             ('packet_id', 'urn:not-retrieved')]:
            candidate = copy.deepcopy(self.candidate)
            candidate['claims'][0][field] = value
            result = m.verify(self.prepared, candidate)
            self.assertFalse(result['acceptedAssertions'])
            self.assertEqual(result['decisions'][0]['status'], 'REJECTED')

    def test_no_biomedical_upgrade_even_with_real_citation(self):
        for kind in m.CLAIM_TYPES[1:]:
            candidate = copy.deepcopy(self.candidate)
            candidate['claims'][0]['claim_type'] = kind
            self.assertFalse(m.verify(self.prepared, candidate)['acceptedAssertions'])
        candidate = copy.deepcopy(self.candidate)
        candidate['claims'][0]['explanation'] = 'This cures FTD.'
        result = m.verify(self.prepared, candidate)
        self.assertNotIn('This cures FTD.', json.dumps(result['acceptedAssertions']))
        self.assertEqual(result['decisions'][0]['explanationStatus'], 'UNVERIFIED-MANUAL-REVIEW-REQUIRED')

    def test_changed_evidence_or_prompt_rejected(self):
        changed = copy.deepcopy(self.prepared)
        changed['request']['input'] = '{}'
        with self.assertRaisesRegex(ValueError, 'Changed model request'):
            m.verify(changed, self.candidate)
        changed['requestSha256'] = m.corpus.digest(m.corpus.encode(changed['request']))
        with self.assertRaisesRegex(ValueError, 'Prompt evidence differs'):
            m.verify(changed, self.candidate)
        changed = copy.deepcopy(self.prepared)
        changed['retrieval']['results'] = []
        with self.assertRaisesRegex(ValueError, 'Retrieval differs'):
            m.verify(changed, self.candidate)

    def test_same_candidate_control_never_claims_verified_support(self):
        checked = m.verify(self.prepared, self.candidate)
        control = m.verify(self.prepared, self.candidate, False)
        self.assertEqual(checked['requestSha256'], control['requestSha256'])
        self.assertEqual(checked['decisions'][0]['candidate'], control['decisions'][0]['candidate'])
        self.assertEqual(control['status'], 'UNVERIFIED-CONTROL')
        self.assertFalse(control['acceptedAssertions'])

    def test_no_population_support_avoids_model_call(self):
        p = m.prepare('population', ['CHEMBL3990042'], 'graph',
                      [str(m.retrieval.D.ClinicalIndicationRecord)], [str(m.retrieval.D.hasPopulationScope)])
        self.assertFalse(p['canCallModel'])
        self.assertFalse(m.verify(p, self.candidate)['acceptedAssertions'])

    def test_synthetic_response_refusal_and_incomplete(self):
        response = dict(id='synthetic-control', model=m.MODEL, status='completed', output=[dict(type='message', content=[
            dict(type='output_text', text=json.dumps(self.candidate))])])
        self.assertEqual(m.parse_response(self.prepared, response), self.candidate)
        response['status'] = 'incomplete'
        with self.assertRaises(ValueError):
            m.parse_response(self.prepared, response)
        response['status'] = 'completed'
        response['output'][0]['content'] = [dict(type='refusal', refusal='synthetic')]
        with self.assertRaises(ValueError):
            m.parse_response(self.prepared, response)

    def test_duplicate_claims_do_not_inflate_support(self):
        candidate = copy.deepcopy(self.candidate)
        candidate['claims'] *= 2
        result = m.verify(self.prepared, candidate)
        self.assertEqual(len(result['acceptedAssertions']), 1)
        self.assertIn('DUPLICATE_CLAIM', result['decisions'][1]['reasons'])

    def test_invalid_shape_and_empty_question(self):
        with self.assertRaises(ValueError):
            m.prepare('')
        with self.assertRaises(ValueError):
            m.verify(self.prepared, dict(claims=[], unanswered=[], invented='value'))

    def test_pilot_plan_replay_and_finite_budget(self):
        import m5_pilot_plan as plan
        result = plan.build()
        self.assertEqual(m.corpus.encode(result), (m.corpus.ROOT/plan.OUTPUT).read_bytes())
        self.assertEqual([q['questionId'] for q in result['questions']], ['Q01','Q02','Q03','Q04','Q05','Q06','Q07'])
        self.assertEqual(result['generationCalls'], 14)
        self.assertEqual(result['totalOutputTokenCeiling'], 57344)
        self.assertFalse(result['liveAuthorized'])
        self.assertEqual(result['actualModelCalls'], 0)
