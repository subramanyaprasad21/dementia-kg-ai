"""Owner transcription and frozen-metric replay; no generation or new gold."""
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
import m7_owner_metrics as m

class OwnerMetrics(unittest.TestCase):
    def test_exact_owner_fact_matrix_and_unchanged_metric_result(self):
        s=m.read(m.BASE/'owner-review-scores.json')
        expected=[[1,1],[1,1],[1,1,0],[1,0],[1],[1],[0,1],[0,1],[1],[0],[0,1],[0,1]]
        for n,values in enumerate(expected,1):
            for c in ('grounded','verified'):
                self.assertEqual(s['annotations'][c][n-1]['supportedFactIds'],[f'M7-{n:02d}-F{i}' for i,v in enumerate(values,1) if v])
            self.assertEqual(s['annotations']['model_only'][n-1]['supportedFactIds'],[])
        result=m.calculate();self.assertEqual(result,m.read(m.BASE/'owner-review-metrics.json'))
        self.assertAlmostEqual(result['conditions']['grounded']['requiredFactRecall'],49/72)
        self.assertIsNone(result['conditions']['model_only']['retainedAssertionPrecision'])
        self.assertEqual(result['pairedPrecision']['difference'],0)

    def test_coverage_is_separate_from_output_omission(self):
        s=m.read(m.BASE/'owner-review-scores.json')
        r=s['coverage'][2];self.assertNotIn('M7-03-F3',s['annotations']['grounded'][2]['supportedFactIds'])
        supplied=set().union(*(set(v) for v in r['requiredSupport'].values()))
        self.assertEqual(m.frozen.retrieval_coverage(r['requiredSupport'],supplied),1)
        removed=set(r['requiredSupport']['M7-03-F3']);supplied-=removed
        self.assertLess(m.frozen.retrieval_coverage(r['requiredSupport'],supplied),1)

    def test_original_question_answer_rubric_sections_unchanged(self):
        file='experiments/m7-portfolio-challenge-001/consolidated-owner-review.md'
        original=subprocess.check_output(['git','show','14dcbcb2733bc7896ea649f95cbe4c4c12c785ca:'+file],cwd=m.ROOT).decode()
        current=(m.ROOT/file).read_text()
        for n in range(1,13):
            key=f'## M7-{n:02d}\n'
            a=original.split(key,1)[1].split('### Owner scoring',1)[0]
            b=current.split(key,1)[1].split('### Owner scoring',1)[0]
            self.assertEqual(a,b)
        manifest=m.read(m.BASE/'artifact-manifest.json')
        for name,digest in manifest['rawFiles'].items():self.assertEqual(m.digest(m.BASE/name),digest)

    def test_prose_surface_traceability_and_equal_conditions(self):
        s=m.read(m.BASE/'owner-review-scores.json');v=m.read(m.BASE/'verification.json')
        for i,d in enumerate(s['details']):
            for condition,offset in [('model_only',0),('grounded',1)]:
                c=v['outcomes'][2*i+offset]['candidate']
                surfaces={'answer_text':c['answer_text'],**{f'claim-{n}-explanation':x['explanation'] for n,x in enumerate(c['claims'],1)},**{f'unanswered-{n}':x for n,x in enumerate(c['unanswered'],1)}}
                for p in d['prose'][condition]['propositions']:
                    for surface in p['surfaces']:self.assertIn(p['text'],surfaces[surface])
                self.assertEqual(len({p['text'] for p in d['prose'][condition]['propositions']}),len(d['prose'][condition]['propositions']))
            self.assertEqual(s['annotations']['grounded'][i],s['annotations']['verified'][i])

    def test_frozen_metric_rejects_unscored_or_invalid_labels(self):
        s=m.read(m.BASE/'owner-review-scores.json')
        items=[dict(id=d['id'],category='answerable' if i<6 else 'insufficient',requiredFactIds=[f['id'] for f in d['requiredFacts']]) for i,d in enumerate(s['details'])]
        for field,value in [('qualificationPass',None),('proseLabels',['fabricated']),('supportedFactIds',['invented-fact'])]:
            a=copy.deepcopy(s['annotations']['grounded']);a[0][field]=value
            with self.assertRaises(ValueError):m.frozen.aggregate(items,a)

    def test_review_provenance_and_no_retrieval_failure(self):
        s=m.read(m.BASE/'owner-review-scores.json')
        self.assertIn('assistant-applied',s['provenance']);self.assertFalse(s['independentReview'])
        for c in s['annotations'].values():self.assertTrue(all(a['status']=='completed' for a in c))
        self.assertIn('NOT-APPLICABLE',m.calculate()['modelOnlyRetrievalCoverage'])
