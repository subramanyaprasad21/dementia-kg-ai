import copy
import sys
import unittest
from pathlib import Path
from unittest.mock import patch
from rdflib import Graph, URIRef
from rdflib.namespace import RDF
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
import m2_mondo_rdf as rdf


class MondoRDF(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.graph, cls.receipts = rdf.build()

    def test_inventory_and_exact_pairs(self):
        expected={'SourceSnapshot':13,'DiseaseConceptReference':13,'HierarchyStep':5}
        for kind,count in expected.items():self.assertEqual(len(set(self.graph.subjects(RDF.type,rdf.DKG[kind]))),count)
        ids=set(str(o) for o in self.graph.objects(None,rdf.DKG.externalIdentifier))
        self.assertEqual(ids,set(rdf.extract.freeze.TERMS))
        pairs=[]
        for s in self.graph.subjects(RDF.type,rdf.DKG.HierarchyStep):
            c=self.graph.value(s,rdf.DKG.childReference);p=self.graph.value(s,rdf.DKG.parentReference)
            pairs.append((str(self.graph.value(c,rdf.DKG.externalIdentifier)),str(self.graph.value(p,rdf.DKG.externalIdentifier))))
            self.assertNotEqual(self.graph.value(c,rdf.DKG.inSnapshot),self.graph.value(p,rdf.DKG.inSnapshot))
        self.assertEqual(set(pairs),set(rdf.extract.freeze.PARENTS))

    def test_determinism_roundtrip_and_committed_output(self):
        values=rdf.outputs()
        self.assertEqual(values,rdf.outputs())
        parsed=Graph().parse(data=values['records.ttl'],format='turtle')
        self.assertEqual(set(parsed),set(self.graph))
        self.assertEqual(rdf.verify()['records'],31)

    def test_receipt_replay_and_change(self):
        for iri,e in self.receipts['records'].items():
            rec=e['receipt']
            self.assertEqual(rdf.identity.receipt(rec['kind'],rec['inputs'],e['payload']),rec)
            self.assertEqual(rdf.identity.identify(rec),iri)
        entry=next(e for e in self.receipts['records'].values() if e['receipt']['kind']=='HierarchyStep')
        changed=copy.deepcopy(entry['receipt']['inputs'])
        changed['childKey'],changed['parentKey']=changed['parentKey'],changed['childKey']
        self.assertNotEqual(rdf.identity.identify(rdf.identity.receipt('HierarchyStep',changed,entry['payload'])),entry['iri'])

    def test_altered_input_rejected_before_build(self):
        with patch.object(rdf.extract,'verify',side_effect=ValueError('altered frozen input')):
            with self.assertRaisesRegex(ValueError,'altered frozen'):rdf.build()
        import tempfile
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            for name,raw in rdf.outputs().items():(root/name).write_bytes(raw)
            (root/'records.ttl').write_bytes(b'')
            with self.assertRaises(ValueError):rdf.verify(root)
