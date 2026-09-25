import copy
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
import dementia_design_answers as d

class DesignAnswers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.e,cls.data,cls.sel=d.inputs()
    def result(self,q,e=None,data=None,sel=None):
        return d.answer(q,self.e if e is None else e,self.data if data is None else data,self.sel if sel is None else sel)
    def test_seven_qualified_positive_answers(self):
        for q in ['Q01','Q02','Q03','Q04','Q05','Q06','Q07']:
            a=self.result(q);self.assertTrue(a['facts']);self.assertEqual(len(a['facts']),len(a['support']))
            if q!='Q04':self.assertEqual(a['status'],'PARTIAL');self.assertTrue(a['unanswered'])
        self.assertEqual([x['count'] for x in self.result('Q04')['facts']],[0,1,3,10])
    def test_missing_evidence_blocks_answer(self):
        a=self.result('Q03',e={});self.assertEqual(a['status'],'UNANSWERED');self.assertFalse(a['facts'])
    def test_shared_report_mutation_changes_result(self):
        e=copy.deepcopy(self.e);e['ed0b04f2d73abb84a48ed87d556725b1743a425c']['studyLocators']=[]
        self.assertEqual(self.result('Q02',e=e)['facts'][0]['sharedReportLocators'],[])
        self.assertEqual(self.result('Q02')['facts'][0]['sharedReportLocators'],['nct00594737'])
    def test_partial_list_cannot_support_absence(self):
        data=copy.deepcopy(self.data)
        data['records']=[r for r in data['records'] if not(r['partition']=='clinical_indication' and d.source.untyped(r['sourceValues'])['drugId']=='CHEMBL4298021')]
        self.assertFalse(any('exactFTDIndicationInInspectedList' in x for x in self.result('Q06',data=data)['facts']))
        self.assertTrue(any(x.get('exactFTDIndicationInInspectedList') is False for x in self.result('Q06')['facts']))
    def test_wrong_release_and_missing_selection(self):
        data=copy.deepcopy(self.data);data['edition']='26.09'
        with self.assertRaises(ValueError):self.result('Q06',data=data)
        self.assertEqual(self.result('Q04',sel=[])['status'],'UNANSWERED')
