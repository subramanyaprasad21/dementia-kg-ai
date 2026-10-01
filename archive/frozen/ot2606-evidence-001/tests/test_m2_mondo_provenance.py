import json
import sys
import tempfile
import unittest
from pathlib import Path
from rdflib import URIRef
from rdflib.namespace import RDF
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
import m2_mondo_provenance as provenance
rdf=provenance.rdf


class MondoProvenance(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph=provenance.build();cls.data,cls.freeze=rdf.load()

    def test_all_captures_descriptions_and_receipt_hashes(self):
        self.assertEqual(len(set(self.graph.subjects(RDF.type,rdf.PROV.Entity))),29)
        for e in self.freeze['responses']:
            capture=URIRef(e['captureId']);description=URIRef(e['descriptionId'])
            self.assertIn((capture,rdf.DKG.contextRecord,description),self.graph)
            rec=json.loads(str(self.graph.value(capture,rdf.DKG.sourceText)))
            self.assertEqual(rec,e['captureReceipt'])
            self.assertEqual(rdf.identity.BASE+'m2-capture-1/'+rdf.extract.capture.sha(rdf.extract.capture.canonical(rec)),str(capture))
            desc=json.loads(str(self.graph.value(description,rdf.DKG.sourceText)))['descriptionReceipt']
            self.assertEqual(rdf.identity.BASE+'m2-source-description-1/'+rdf.extract.capture.sha(rdf.extract.capture.canonical(desc)),str(description))

    def test_annotations_and_exclusions_preserved_as_text(self):
        for c in self.data['concepts']:
            text=json.loads(str(self.graph.value(URIRef(c['lineage']['sourceDescriptionId']),rdf.DKG.sourceText)))
            self.assertEqual(text['extractedSourceValues'][0]['values'],c['sourceValues'])
            self.assertEqual(text['permissions'],self.freeze['permissions'])
        excluded=sum(len(json.loads(str(t))['excludedRawRowLocators']) for s,t in self.graph.subject_objects(rdf.DKG.sourceText) if 'm2-source-description-1/' in str(s))
        self.assertEqual(excluded,6)
        self.assertFalse(list(self.graph.triples((None,rdf.DKG.parentReference,None))))

    def test_replay_and_tampered_capture_link(self):
        self.assertEqual(provenance.verify()['resources'],29)
        self.assertEqual(rdf.serialize(self.graph),rdf.serialize(provenance.build()))
        e=self.freeze['responses'][0]
        changed=rdf.Graph()
        for t in self.graph:changed.add(t)
        changed.remove((URIRef(e['captureId']),rdf.DKG.contextRecord,None))
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/'changed.ttl';path.write_bytes(rdf.serialize(changed))
            with self.assertRaises(ValueError):provenance.verify(path)
