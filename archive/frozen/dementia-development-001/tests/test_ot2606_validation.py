import sys
import unittest
from pathlib import Path
from rdflib import Graph,URIRef,Literal
from rdflib.namespace import RDF,OWL,XSD
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'tools'))
import ot2606_source as source
import ot2606_rdf as rdf
import validate_ot2606 as v
import validate_m1_fixtures as structural
from test_m1_owl_reasoning import reason,unexplained_additions
D=rdf.DKG

class EvidenceValidation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=source.load(source.OUTPUT);g,_,cls.info=rdf.build(cls.data);cls.graph=g+rdf.provenance(cls.data)
    def test_independently_expected_positive_answers(self):
        answer=v.answers(self.graph)
        self.assertEqual(answer['04e8f548c45ece0c2d428eef5f5aa149f67f1fbd']['originalIdentifier'],'OMIM:172700')
        self.assertEqual(answer['04e8f548c45ece0c2d428eef5f5aa149f67f1fbd']['normalized'],'MONDO_0017276')
        self.assertEqual(answer['019b39b2b176f9e7df8536022682738d12e32f39']['normalized'],'MONDO_0010857')
        self.assertEqual(answer['8bac3794c7e23d4dc3e7b44e3b2e1af8dcccc4fe']['normalized'],'MONDO_0007088')
        self.assertEqual(answer['1261ad02e3d662cd23a476af47159a1501d01889']['publications'],['33008897'])
        self.assertEqual(answer['ed0b04f2d73abb84a48ed87d556725b1743a425c']['studyLocators'],['nct00594737'])
        self.assertEqual(len(v.semantic(self.graph,self.data)),8)
    def test_mapping_direction_snapshot_and_values_mutations(self):
        item=next(iter(self.info.values()));m=URIRef(item['mapping']);e=URIRef(item['occurrence']);dest=URIRef(item['normalized'])
        for mode in ('reverse','wrong-destination','wrong-snapshot','missing-evidence'):
            g=structural.clone(self.graph)
            if mode=='reverse':g.remove((m,D.mappingContext,e));g.add((e,D.mappingContext,m))
            if mode=='wrong-destination':g.set((dest,D.externalIdentifier,Literal('MONDO_9999999',datatype=XSD.string)))
            if mode=='wrong-snapshot':g.set((URIRef(item['snapshot']),D.snapshotVersion,Literal('26.09',datatype=XSD.string)))
            if mode=='missing-evidence':g.remove((e,RDF.type,D.EvidenceOccurrence))
            with self.assertRaises(ValueError):v.semantic(g,self.data)
    def test_grouping_scope_and_shared_study(self):
        groups=list(self.graph.subjects(RDF.type,D.DiseaseTargetAssociation));self.assertEqual(len(groups),5)
        selected=set(self.graph.objects(None,D.selectedOccurrence));self.assertEqual(len(selected),6)
        for row in self.info.values():self.assertEqual(URIRef(row['occurrence']) in selected,row['row']['diseaseId'] in {'MONDO_0004975','MONDO_0017276'})
        clinical=[r for r in self.info.values() if r['study']];self.assertEqual(clinical[0]['study'],clinical[1]['study']);self.assertNotEqual(clinical[0]['occurrence'],clinical[1]['occurrence'])
        derived=list(self.graph.subjects(RDF.type,D.DerivedStatement));self.assertEqual(len(derived),1)
        self.assertEqual(str(v.one(self.graph,derived[0],D.dependencyStatus)),'shared-source-established')
    def test_structural_warnings_and_real_defect(self):
        s,_,_=structural.validate_graph(self.graph);self.assertEqual(s['result_counts'],{'Warning':2});self.assertFalse(s['raw_shacl_conforms'])
        g=structural.clone(self.graph);mapping=next(g.subjects(RDF.type,D.MappingRecord));g.remove((mapping,D.mappingContext,None))
        s,_,_=structural.validate_graph(g);self.assertGreater(s['result_counts'].get('Violation',0),0)
    def test_no_clinical_upgrade_or_unknown_predicate(self):
        for predicate,obj in [(OWL.sameAs,URIRef('urn:control:equivalence')),(D.trialStatusText,Literal('COMPLETED',datatype=XSD.string)),(D.aggregateScore,Literal('1',datatype=XSD.decimal))]:
            g=structural.clone(self.graph);g.add((next(g.subjects(RDF.type,D.EvidenceOccurrence)),predicate,obj))
            with self.assertRaises(ValueError):v.semantic(g,self.data)
        self.assertFalse(list(self.graph.subjects(RDF.type,D.MechanismRecord)));self.assertFalse(list(self.graph.subjects(RDF.type,D.ClinicalIndicationRecord)))
    def test_roundtrip_and_owl_boundaries(self):
        b=rdf.common.serialize(self.graph);self.assertEqual(set(Graph().parse(data=b,format='turtle')),set(self.graph))
        ontology=structural.load_graph(ROOT/'ontology/dementiagraph-v.ttl');g=ontology+self.graph;closure,errors=reason(g)
        self.assertEqual(errors,[]);self.assertEqual(unexplained_additions(g,closure),set())
