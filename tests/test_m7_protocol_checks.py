"""Synthetic controls only: no held-out questions, human reviews or API calls."""
import copy
import json
from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
import m7_protocol_checks as m

class ProtocolChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plan=json.loads((Path(__file__).resolve().parents[1]/'assessments/m7_protocol_proposal.json').read_text())

    def items(self):
        # Dummy declarations exercise validation; they are not real eligibility reviews.
        return [dict(id=f'CONTROL-{n}',question=f'Synthetic control {n}',category=c,stratum=s,
                     rootIds=['urn:synthetic:root'],dependencyGroups=['shared-control'],requiredFactIds=['fact'],
                     requiredQualifications=['source-relative'],requiredAbstention=('unsupported extension' if c=='insufficient' else None),
                     eligibilityReviews=[dict(reviewerId=f'SYNTHETIC-{r}',decision='eligible',rationale='Test only') for r in ['A','B']],
                     origin='human-authored',developmentExposed=False,nearParaphraseOfDevelopment=False,syntheticControl=False,
                     selfContained=True,goldReviewed=True)
                for n,(s,c) in enumerate((s,c) for s in self.plan['strata'] for c in ['answerable','insufficient'])]

    def validate(self,items):return m.validate_items(items,[],['urn:synthetic:root'],self.plan['strata'])

    def test_exact_budget_and_draft_blocks_execution(self):
        self.assertEqual(m.budget(self.plan)['newIncludingDevelopmentRetryUSD'],'5.843576')
        self.assertFalse(self.plan['executionAuthorized'])
        self.assertFalse(m.readiness(self.plan)['ready'])
        p=copy.deepcopy(self.plan);p['formalBudget']['generations']=25
        with self.assertRaises(AssertionError):m.budget(p)

    def test_positive_eligibility_shape_not_novelty_proof(self):self.assertTrue(self.validate(self.items()))

    def test_development_duplicates_paraphrase_declarations_and_synthetic_records_fail(self):
        for field,value in [('question','Synthetic control 1'),('developmentExposed',True),('nearParaphraseOfDevelopment',True),('syntheticControl',True),('selfContained',False),('goldReviewed',False)]:
            items=self.items();items[0][field]=value
            with self.subTest(field=field),self.assertRaises(ValueError):self.validate(items)
        with self.assertRaises(ValueError):m.validate_items(self.items(),['SYNTHETIC control 0!!!'],['urn:synthetic:root'],self.plan['strata'])

    def test_allocation_lineage_and_review_declarations_are_required(self):
        for field,value in [('rootIds',['urn:unknown']),('rootIds',[]),('dependencyGroups',[]),('requiredFactIds',[]),('eligibilityReviews',[]),('requiredQualifications',[])]:
            items=self.items();items[0][field]=value
            with self.subTest(field=field),self.assertRaises(ValueError):self.validate(items)
        items=self.items();items[1]['category']='answerable'
        with self.assertRaises(ValueError):self.validate(items)

    def test_all_refusal_is_not_perfect_precision_or_successful_abstention(self):
        items=self.items();annotations=[dict(id=i['id'],status='refusal') for i in items]
        result=m.aggregate(items,annotations)
        self.assertIsNone(result['retainedAssertionPrecision'])
        self.assertEqual(result['requiredFactRecall'],0)
        self.assertEqual(result['requiredAbstentionPassRate'],0)
        self.assertEqual(result['failures'],{'refusal':12})
        self.assertEqual(result['zeroRetainedRate'],1)

    def completed(self,item):
        return dict(id=item['id'],status='completed',retainedLabels=['supported','unsupported'],retainedRelevant=[True,False],
                    provenanceCorrect=[True,False],proseLabels=['supported','unsupported','unresolved'],supportedFactIds=['fact'],qualificationPass=True,
                    abstentionPass=(True if item['category']=='insufficient' else None),excessiveAbstention=(False if item['category']=='answerable' else None))

    def test_exact_macro_metrics_and_failure_denominators(self):
        items=self.items();annotations=[self.completed(i) for i in items];result=m.aggregate(items,annotations)
        self.assertEqual(result['retainedAssertionPrecision'],0.5)
        self.assertEqual(result['requiredFactRecall'],1)
        self.assertAlmostEqual(result['unsupportedProseRate'],1/3)
        self.assertAlmostEqual(result['unresolvedProseRate'],1/3)
        annotations[0]=dict(id=items[0]['id'],status='timeout')
        result=m.aggregate(items,annotations)
        self.assertEqual(result['requiredFactRecall'],11/12)
        self.assertEqual(result['qualificationPassRate'],11/12)
        self.assertEqual(result['precisionDefinedItems'],11)
        self.assertEqual(result['failures'],{'timeout':1})

    def test_empty_failure_duplicate_labels_and_invalid_fact_ids_rejected(self):
        items=self.items();annotations=[self.completed(i) for i in items]
        with self.assertRaises(ValueError):m.aggregate(items,annotations[:-1])
        annotations[0]['supportedFactIds']=['invented']
        with self.assertRaises(ValueError):m.aggregate(items,annotations)
        annotations[0]=dict(id=items[0]['id'],status='timeout',abstentionPass=True)
        with self.assertRaises(ValueError):m.aggregate(items,annotations)

    def test_retrieval_coverage_is_separate_from_answer_scoring(self):
        self.assertEqual(m.retrieval_coverage({'one':['a'],'two':['b','c']},['a','b']),0.5)
        with self.assertRaises(ValueError):m.retrieval_coverage({'one':[]},[])

    def test_paired_difference_keeps_empty_pairs_visible(self):
        items=self.items();left=[self.completed(i) for i in items];right=copy.deepcopy(left)
        for a in right:
            a['retainedLabels']=['supported'];a['retainedRelevant']=[True];a['provenanceCorrect']=[True]
        self.assertEqual(m.paired_precision_difference(items,left,right),{'difference':0.5,'definedPairs':12,'plannedItems':12})
        right[0]['retainedLabels']=[];right[0]['retainedRelevant']=[];right[0]['provenanceCorrect']=[]
        result=m.paired_precision_difference(items,left,right)
        self.assertEqual(result['definedPairs'],11)
        self.assertEqual(result['plannedItems'],12)
