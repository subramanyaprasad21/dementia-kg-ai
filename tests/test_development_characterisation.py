import sys
import unittest
from pathlib import Path
from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDF, OWL
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'tools'))
import characterise_development_graph as m


class Characterisation(unittest.TestCase):
    def test_deterministic_statistics(self):
        result = m.build()
        self.assertEqual(m.corpus.encode(result), (m.corpus.ROOT/m.OUTPUT).read_bytes())
        s = result['statistics']
        self.assertEqual((s['subjectResources'], s['triples']), (191, 1112))
        self.assertEqual(sum(s['resourceConnectivity']['componentSizes']), 191)
        self.assertEqual(sum(s['evidenceSourceCounts'].values()), 8)
        self.assertTrue(all(not row['missing'] for row in s['sourceRecordProvenance'].values()))
        schema = Graph().parse(m.corpus.ROOT/'ontology/dementiagraph-v.ttl', format='turtle')
        self.assertTrue(m.SEMANTIC <= set(schema.subjects(RDF.type, OWL.ObjectProperty)))

    def test_missing_provenance_changes_coverage(self):
        graph = m.corpus.load()
        owner = next(graph.subjects(RDF.type, m.D.MechanismRecord))
        graph.remove((owner, m.D.inSnapshot, None))
        self.assertIn(str(owner), m.analyse(graph)['sourceRecordProvenance']['MechanismRecord']['missing'])

    def test_connectivity_excludes_schema_and_literal_coincidence(self):
        g = Graph()
        a, b = URIRef('urn:control:a'), URIRef('urn:control:b')
        for s in (a, b):
            g.add((s, RDF.type, m.D.Target))
            g.add((s, m.D.externalIdentifier, Literal('same-string')))
        self.assertEqual(m.analyse(g)['resourceConnectivity']['componentSizes'], [1, 1])
        g.add((a, m.D.hasTarget, b))
        self.assertEqual(m.analyse(g)['resourceConnectivity']['componentSizes'], [2])
        self.assertEqual(m.distances(g, a, {m.D.hasTarget})[b], 1)
        self.assertNotIn(a, m.distances(g, b, {m.D.hasTarget}))

    def test_path_removal_changes_reachability(self):
        graph = m.corpus.load()
        owner, publication = next(graph.subject_objects(m.D.citesPublication))
        graph.remove((owner, m.D.citesPublication, publication))
        self.assertNotIn(publication, m.distances(graph, owner, {m.D.citesPublication}))
