import sys
import unittest
from pathlib import Path
from rdflib import Graph, URIRef
from rdflib.namespace import RDF
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'tools'))
import development_retrieval as r
import replay_development_retrieval as replay


class DevelopmentRetrieval(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph = r.corpus.load()

    def retrieve(self, mode='graph', **kwargs):
        return r.retrieve(self.graph, 'mechanism', ['CHEMBL3990042'], mode,
                          record_types=[str(r.D.MechanismRecord)], **kwargs)

    def test_packets_are_asserted_and_exclude_raw_blob_promotion(self):
        packets = r.packets(self.graph)
        self.assertEqual(len(packets), 48)
        for packet in packets:
            facts = Graph().parse(data=packet['text'], format='nt')
            self.assertTrue(set(facts) <= set(self.graph))
            self.assertEqual(r.corpus.digest(packet['text'].encode()), packet['sha256'])
            self.assertFalse(any((s, RDF.type, r.PROV.Entity) in self.graph and p == r.D.sourceText for s, p, o in facts))

    def test_positive_mechanism_and_same_packets_across_methods(self):
        graph_result = self.retrieve()['results']
        self.assertEqual(len(graph_result), 1)
        expected = graph_result[0]['packet']
        for mode in r.MODES:
            result = self.retrieve(mode)
            matches = [v for v in result['results'] if v['packet']['id'] == expected['id']]
            self.assertEqual(len(matches), 1)
            self.assertEqual(matches[0]['packet'], expected)
            self.assertTrue(matches[0]['anchorPaths'])

    def test_removed_drug_link_blocks_graph_answer(self):
        expected = self.retrieve()['results'][0]['packet']['id']
        changed = Graph()
        changed += self.graph
        changed.remove((URIRef(expected), r.D.hasDrug, None))
        result = r.retrieve(changed, 'mechanism', ['CHEMBL3990042'], 'graph',
                            record_types=[str(r.D.MechanismRecord)])
        self.assertFalse(result['results'])

    def test_unknown_anchor_and_missing_population_not_negative_biology(self):
        absent = r.retrieve(self.graph, '', ['NO-SUCH-SOURCE-ID'], 'graph')
        self.assertEqual(absent['status'], 'NO-RETRIEVABLE-SUPPORT')
        for mode in r.MODES:
            result = r.retrieve(self.graph, 'population', ['CHEMBL3990042'], mode,
                                record_types=[str(r.D.ClinicalIndicationRecord)],
                                required_predicates=[str(r.D.hasPopulationScope)])
            self.assertFalse(result['results'])
            self.assertIn('never biological negation', result['limitation'])

    def test_budget_never_truncates_or_leaks_packet(self):
        for mode in r.MODES:
            result = self.retrieve(mode, k=1, max_bytes=1)
            self.assertEqual(result['budget']['usedPacketBytes'], 0)
            self.assertFalse(result['results'])
            self.assertTrue(result['skippedForBudget'])
            result = self.retrieve(mode, k=1)
            self.assertLessEqual(len(result['results']), 1)
            self.assertLessEqual(result['budget']['usedPacketBytes'], 65536)

    def test_original_identifier_not_silently_normalized(self):
        old = r.retrieve(self.graph, '', ['OMIM:172700'], 'graph', record_types=[str(r.D.MappingRecord)])
        replaced = r.retrieve(self.graph, '', ['OMIM_172700'], 'graph', record_types=[str(r.D.MappingRecord)])
        self.assertTrue(old['results'])
        self.assertFalse(replaced['results'])

    def test_invalid_schema_filters_and_limits_rejected(self):
        with self.assertRaises(ValueError):
            self.retrieve(k=0)
        with self.assertRaises(ValueError):
            r.retrieve(self.graph, '', record_types=[str(r.D.UnapprovedClass)])
        with self.assertRaises(ValueError):
            r.retrieve(self.graph, '', required_predicates=[str(r.D.provesEfficacy)])

    def test_vector_positive_and_out_of_vocabulary(self):
        docs = [dict(id='a', text='controlled alpha'), dict(id='b', text='controlled beta')]
        scores = r.vector_scores(docs, 'alpha')
        self.assertGreater(scores['a'], 0)
        self.assertEqual(scores['b'], 0)
        self.assertEqual(r.vector_scores(docs, 'unseen'), {'a': 0, 'b': 0})

    def test_design_control_replay_is_not_full_question_acceptance(self):
        result = replay.build()
        self.assertEqual(r.corpus.encode(result), (r.corpus.ROOT/replay.OUTPUT).read_bytes())
        self.assertFalse(result['heldOut'])
        self.assertFalse(result['fullQuestionAcceptance'])
        self.assertEqual(len(result['results']), 24)
        self.assertTrue(all(not v['records'] for v in result['results'] if v['case']=='Q07-unavailable-population'))
        mapping = next(v for v in result['results'] if v['case']=='Q05-ambiguous-original' and v['mode']=='graph')
        self.assertEqual(len(mapping['records']), 2)
        selection = next(v for v in result['results'] if v['case']=='Q04-persisted-selection-context' and v['mode']=='graph')
        self.assertEqual(len(selection['records']), 2)
