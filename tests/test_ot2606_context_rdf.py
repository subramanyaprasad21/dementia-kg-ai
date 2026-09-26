import copy,sys,unittest
from pathlib import Path
from rdflib import Graph,URIRef
from rdflib.namespace import RDF,OWL
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
import ot2606_context_rdf as r
import validate_m1_fixtures as shacl
from owlrl import DeductiveClosure,OWLRL_Semantics

class ContextRDF(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.graph,cls.receipts=r.build()
 def test_inventory_roundtrip_and_replay(self):
  self.assertEqual(len(self.graph),226)
  for kind,count in [('MechanismRecord',5),('ClinicalIndicationRecord',4),('DiseaseConceptReference',4),('SourceSnapshot',8)]:self.assertEqual(len(set(self.graph.subjects(RDF.type,r.D[kind]))),count)
  self.assertEqual(set(Graph().parse(data=self.graph.serialize(format='turtle'),format='turtle')),set(self.graph))
  for name,b in r.outputs().items():self.assertEqual((r.OUT/name).read_bytes(),b)
 def test_identity_capture_separation_revision_and_missing_lineage(self):
  data=r.context.extract();record=next(x for x in data['records'] if x['partition']=='drug_mechanism_of_action');schema=next(x['schema'] for x in data['schemas'] if x['file']==record['lineage']['file'])
  before=r.describe(record,schema);changed=copy.deepcopy(record);changed['lineage']['ledgerSha256']='new-capture'
  self.assertEqual(r.describe(changed,schema),before)
  changed['sourceValues']['value']['actionType']=r.source.typed('controlled-mutation');changed['sourceValueSha256']=r.source.sha(r.core.canonical(changed['sourceValues']))
  self.assertNotEqual(r.describe(changed,schema)[0],before[0])
  with self.assertRaisesRegex(ValueError,'Unverified'):r.Registry().add('SourceSnapshot',dict(descriptionId=before[0],edition='26.06',datasource=record['partition'],locator=r.text(before[1]['locator'])),[])
  with self.assertRaisesRegex(ValueError,'Unsupported'):r.Registry().add('PopulationScope',{},[])
 def test_structural_positive_and_missing_participant(self):
  result,_,_=shacl.validate_graph(self.graph);self.assertTrue(result['raw_shacl_conforms'])
  altered=Graph();altered+=self.graph
  mech=next(altered.subjects(RDF.type,r.D.MechanismRecord));altered.remove((mech,r.D.hasDrug,None))
  result,_,_=shacl.validate_graph(altered);self.assertFalse(result['raw_shacl_conforms'])
 def test_no_substantive_inference_or_equivalence(self):
  g=Graph();g+=self.graph;g.parse(r.source.ROOT/'ontology/dementiagraph-v.ttl',format='turtle');original=set(g)
  closure=DeductiveClosure(OWLRL_Semantics,axiomatic_triples=False,datatype_axioms=False,rdfs_closure=False,improved_datatypes=True);closure.expand(g)
  self.assertFalse(any(s!=o for s,o in g.subject_objects(OWL.sameAs)))
  self.assertFalse(any(str(p).startswith(str(r.D)) for s,p,o in set(g)-original))
 def test_shared_mechanism_and_source_values_remain_scoped(self):
  mem=[e for e in self.receipts['records'].values() if e['receipt']['kind']=='MechanismRecord' and any(a['field']=='sourceText' and 'NMDA' in a['value'] for a in e['payload'])]
  self.assertEqual(len(mem),2);self.assertEqual(mem[0]['receipt']['inputs']['snapshotKey'],mem[1]['receipt']['inputs']['snapshotKey'])
  self.assertFalse(list(self.graph.subjects(RDF.type,r.D.PopulationScope)))
  self.assertFalse(list(self.graph.triples((None,r.D.trialStatusText,None))))
