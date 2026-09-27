"""Independent semantic witnesses for explicit question scopes; no API calls."""
import copy
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch
from rdflib import Graph, URIRef
from rdflib.namespace import RDF
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
import m5_corrected_retrieval as m
D=m.D

class CorrectedRetrieval(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph=m.ai.corpus.load()
        cls.prepared={q:m.prepare(q) for q in m.questions()}

    def roots(self,q): return [URIRef(r['packet']['id']) for r in self.prepared[q]['retrieval']['results']]
    def oftype(self,q,t): return {s for s in self.roots(q) if (s,RDF.type,D[t]) in self.graph}
    def values(self,subjects,p): return {str(v) for s in subjects for v in self.graph.objects(s,p)}
    def participants(self,subjects,p): return {v for s in subjects for v in self.graph.objects(s,p)}

    def test_q01_exact_psen_records_and_both_normalized_diseases(self):
        evidence=self.participants(self.oftype('Q01','MappingRecord'),D.mappingContext)
        self.assertEqual(self.values(evidence,D.sourceRecordIdentifier),{'1261ad02e3d662cd23a476af47159a1501d01889','986bb22bf0f7858c36fc773e5b45c08cd9c514fd','98c49197e4989f7d3be8b2f8ee3c7699e2f3d6dc'})
        self.assertEqual(self.values(self.participants(evidence,D.hasTarget),D.externalIdentifier),{'ENSG00000080815'})
        mappings=self.oftype('Q01','MappingRecord')
        self.assertEqual(self.participants(mappings,D.mappingContext),evidence)
        self.assertEqual(self.values(self.participants(mappings,D.reportedDestination),D.externalIdentifier),{'MONDO_0004975','MONDO_0017276'})
        self.assertEqual(len(self.oftype('Q01','MissingnessRecord')),2)

    def test_q02_both_genes_share_report_and_two_mechanism_projections(self):
        evidence=self.participants(self.oftype('Q02','MappingRecord'),D.mappingContext)
        self.assertEqual(self.values(evidence,D.sourceRecordIdentifier),{'ed0b04f2d73abb84a48ed87d556725b1743a425c','0d60abae93f3438f8750a76beb2b41de9b6b3efd'})
        self.assertEqual(self.values(self.participants(evidence,D.hasTarget),D.externalIdentifier),{'ENSG00000176884','ENSG00000116032'})
        self.assertEqual(self.values(self.participants(evidence,D.refersToStudy),D.externalIdentifier),{'nct00594737'})
        mechanisms=self.oftype('Q02','MechanismRecord')
        self.assertEqual(len(mechanisms),2)
        self.assertEqual(self.values(self.participants(mechanisms,D.hasDrug),D.externalIdentifier),{'CHEMBL807'})
        self.assertEqual(self.values(self.oftype('Q02','DerivedStatement'),D.dependencyStatus),{'shared-source-established'})

    def test_q03_pick_anchor_was_correct_and_remains_record_local(self):
        mappings=self.oftype('Q03','MappingRecord')
        self.assertEqual(len(mappings),1)
        self.assertEqual(self.values(self.participants(mappings,D.mappingInput),D.externalIdentifier),{'OMIM:172700'})
        self.assertEqual(self.values(self.participants(mappings,D.mappingContext),D.sourceRecordIdentifier),{'04e8f548c45ece0c2d428eef5f5aa149f67f1fbd'})
        self.assertEqual(self.values(self.participants(mappings,D.reportedDestination),D.externalIdentifier),{'MONDO_0017276'})

    def test_q04_all_five_directed_steps_and_three_distinct_mapping_contexts(self):
        edges=set()
        for s in self.oftype('Q04','HierarchyStep'):
            child=self.graph.value(s,D.childReference);parent=self.graph.value(s,D.parentReference)
            edges.add((str(self.graph.value(child,D.externalIdentifier)),str(self.graph.value(parent,D.externalIdentifier))))
        self.assertEqual(edges,{('MONDO:0007088','MONDO:0015140'),('MONDO:0015140','MONDO:0100087'),('MONDO:0100087','MONDO:0004975'),('MONDO:0010857','MONDO:0017160'),('MONDO:0017160','MONDO:0017276')})
        self.assertEqual(self.values(self.participants(self.oftype('Q04','MappingRecord'),D.mappingContext),D.sourceRecordIdentifier),{'8bac3794c7e23d4dc3e7b44e3b2e1af8dcccc4fe','019b39b2b176f9e7df8536022682738d12e32f39','04e8f548c45ece0c2d428eef5f5aa149f67f1fbd'})
        self.assertFalse(self.oftype('Q04','SelectionContext')) # local fixed-ID selections are not historical inclusive queries

    def test_q05_both_assignments_no_third_mapping(self):
        mappings=self.oftype('Q05','MappingRecord')
        self.assertEqual(len(mappings),2)
        self.assertEqual(self.values(self.participants(mappings,D.mappingInput),D.externalIdentifier),{'OMIM:600274'})
        self.assertEqual(self.values(self.participants(mappings,D.reportedDestination),D.externalIdentifier),{'MONDO_0017276','MONDO_0010857'})

    def test_q06_mechanism_and_indication_and_ad_control(self):
        for typ in ('MechanismRecord','ClinicalIndicationRecord'):
            self.assertEqual(self.values(self.participants(self.oftype('Q06',typ),D.hasDrug),D.externalIdentifier),{'CHEMBL4298021','CHEMBL3833321'})
        self.assertEqual(len(self.oftype('Q06','ClinicalIndicationRecord')),3)
        association=self.oftype('Q06','DiseaseTargetAssociation')
        self.assertEqual(self.values(self.participants(association,D.hasTarget),D.externalIdentifier),{'ENSG00000186868'})
        self.assertEqual(self.values(association,D.originRole),{'project-grouping'})

    def test_q07_exact_gosuranemab_only_and_population_absence_is_explicit(self):
        self.assertEqual(len(self.roots('Q07')),2)
        self.assertEqual(self.values(self.participants(self.roots('Q07'),D.hasDrug),D.externalIdentifier),{'CHEMBL3990042'})
        self.assertEqual(self.values(self.oftype('Q07','ClinicalIndicationRecord'),D.sourceRecordIdentifier),{'c680c47a8cc2571635e1d5c629e51834273a3e67d25ebedfa9e58b729ad65189'})
        self.assertFalse(self.participants(self.roots('Q07'),D.hasPopulationScope))
        self.assertIn('primary registry population/status',m.GAPS['Q07'][0])

    def test_scope_excludes_unrelated_lexical_hits_and_candidates_match_across_modes(self):
        for q,p in self.prepared.items():
            expected=set(p['retrieval']['allowedRoots'])
            for mode in m.ai.retrieval.MODES:
                r=m.ai.retrieval.retrieve(self.graph,'unrelated CHEMBL807 PSEN1 trial',mode=mode,k=8,max_bytes=196608,record_types=p['retrieval']['recordTypes'],allowed_roots=sorted(expected))
                self.assertEqual(r['eligiblePackets'],len(expected))
                self.assertLessEqual({row['packet']['id'] for row in r['results']},expected)
                if mode!='vector': self.assertEqual({row['packet']['id'] for row in r['results']},expected)
                self.assertFalse(r['skippedForBudget'])
            self.assertEqual(m.ai.request_for(p,'retrieval'),m.ai.request_for(p,'verified'))
            self.assertNotIn('packets',__import__('json').loads(m.ai.request_for(p,'model_only')['input']))

    def test_missing_or_ambiguous_records_and_forged_scope_fail(self):
        g=Graph();g+=self.graph
        s=next(iter(self.participants(self.oftype('Q03','MappingRecord'),D.mappingContext)))
        g.remove((s,D.sourceRecordIdentifier,None))
        with self.assertRaises(ValueError):m.scopes(g)
        g=Graph();g+=self.graph
        fake=URIRef('urn:duplicate')
        for p,o in g.predicate_objects(s):g.add((fake,p,o))
        with self.assertRaises(ValueError):m.scopes(g)
        p=copy.deepcopy(self.prepared['Q03']);p['retrieval']['allowedRoots']=['urn:invented']
        with self.assertRaises(ValueError):m.ai.validate_prepared(p)

    def test_offline_plan_and_original_pilot_remain_reproducible(self):
        import m5_pilot_plan
        import replay_m5_pilot
        with patch('urllib.request.OpenerDirector.open',side_effect=AssertionError('Network forbidden')):
            self.assertEqual(m.build(),m.ai.corpus.read(m.ai.corpus.ROOT/m.OUTPUT))
            self.assertEqual(m5_pilot_plan.build(),m.ai.corpus.read(m.ai.corpus.ROOT/m5_pilot_plan.OUTPUT))
            self.assertEqual(replay_m5_pilot.replay(),m.ai.corpus.read(replay_m5_pilot.DIRECTORY/'summary.json'))
        for name in ['experiments/m5-development-pilot-001','assessments/m5-pilot-plan.json','docs/competency_questions.md','kg','ontology']:
            changed=subprocess.run(['git','diff','518f469f783e0c1c98deab2c80f0a49aeba00b93','--',name],cwd=m.ai.corpus.ROOT,capture_output=True,check=True)
            self.assertEqual(changed.stdout,b'')


    def test_insufficient_packet_budget_fails_instead_of_silent_partial_selection(self):
        with patch.dict(m.BUDGET, {'k':5,'max_bytes':65536}):
            with self.assertRaisesRegex(ValueError,'omitted'):
                m.prepare('Q04')
        for p in self.prepared.values():
            for record in p['retrieval']['results']:
                packet_graph=Graph().parse(data=record['packet']['text'],format='nt')
                self.assertFalse(set(packet_graph)-set(self.graph))
