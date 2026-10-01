import sys
import unittest
from pathlib import Path
from rdflib import Literal, URIRef
from rdflib.namespace import RDF, OWL, XSD
from owlrl import DeductiveClosure, OWLRL_Semantics
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
import validate_m2_mondo as validation
r=validation.rdf


class MondoValidation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.graph=validation.load_graph()

    def copy(self):return validation.structural.clone(self.graph)

    def test_positive_shacl_and_semantic_acceptance(self):
        result=validation.validate(self.graph)
        self.assertTrue(result['raw_shacl_conforms']);self.assertEqual(result['result_counts'],{})
        self.assertEqual((result['resources'],result['triples']),(60,317))

    def test_missing_endpoint_is_structural_failure(self):
        g=self.copy();step=next(g.subjects(RDF.type,r.DKG.HierarchyStep))
        g.remove((step,r.DKG.childReference,None))
        summary,_,_=validation.structural.validate_graph(g)
        self.assertGreater(summary['result_counts'].get('Violation',0),0)
        with self.assertRaises(ValueError):validation.semantic(g)

    def test_direction_and_snapshot_mutations(self):
        g=self.copy();step=next(g.subjects(RDF.type,r.DKG.HierarchyStep))
        child=g.value(step,r.DKG.childReference);parent=g.value(step,r.DKG.parentReference)
        g.set((step,r.DKG.childReference,parent));g.set((step,r.DKG.parentReference,child))
        with self.assertRaises(ValueError):validation.semantic(g)
        g=self.copy();snapshot=next(g.subjects(RDF.type,r.DKG.SourceSnapshot))
        g.set((snapshot,r.DKG.snapshotVersion,Literal('other',datatype=XSD.string)))
        with self.assertRaises(ValueError):validation.semantic(g)

    def test_equivalence_exclusion_and_provenance_mutations(self):
        for mutate in [
            lambda g:g.add((URIRef('urn:control:a'),OWL.sameAs,URIRef('urn:control:b'))),
            lambda g:g.add((URIRef('urn:control:extra'),RDF.type,r.DKG.HierarchyStep)),
            lambda g:g.remove(next(g.triples((None,r.DKG.contextRecord,None)))),
            lambda g:g.remove(next(g.triples((None,r.DKG.sourceText,None))))]:
            g=self.copy();mutate(g)
            with self.assertRaises(ValueError):validation.semantic(g)

    def test_wrong_participant_type_is_structural_failure(self):
        g=self.copy();step=next(g.subjects(RDF.type,r.DKG.HierarchyStep))
        parent=g.value(step,r.DKG.parentReference);g.remove((parent,RDF.type,r.DKG.DiseaseConceptReference))
        g.add((parent,RDF.type,r.PROV.Entity))
        summary,_,_=validation.structural.validate_graph(g)
        self.assertGreater(summary['result_counts'].get('Violation',0),0)

    def test_reasoning_no_substantive_additions(self):
        g=self.copy();g+=validation.structural.load_graph(r.ROOT/'ontology/dementiagraph-v.ttl')
        before=set(g)
        DeductiveClosure(OWLRL_Semantics,axiomatic_triples=False,datatype_axioms=False,
                         rdfs_closure=False,improved_datatypes=True).expand(g)
        additions=set(g)-before
        self.assertFalse([t for t in additions if str(t[1]).startswith(str(r.DKG)) or t[1]==r.PROV.wasDerivedFrom])
        self.assertFalse([t for t in additions if t[1]==OWL.sameAs and t[0]!=t[2]])
        self.assertFalse([t for t in g if 'error' in str(t[1]).lower()])
