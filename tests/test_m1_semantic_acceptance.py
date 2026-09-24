"""Independent bounded semantic expectations; no new biomedical source evidence."""
import json
import subprocess
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
from rdflib import Graph, URIRef, Literal, RDF, XSD
from validate_m1_fixtures import ROOT, DATA, load_graph, clone, validate_graph
from m1_fixture_identity import identify, receipt, canonical
from m1_semantic_acceptance import (D,PROV,AcceptanceError,mappings,hierarchy,selection,
    intersection,bounded_extent,constituents,evidence,shared_studies,clinical,accept_claim,
    comparison_control,grouping_control,membership_explanation)

BASELINE='7ce1c4c7011ce8911e2b54243306a94ac298ee18'


class SemanticAcceptance(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.g=load_graph(DATA)
        cls.bundle=json.loads((ROOT/'fixtures/m1/identity_receipts.json').read_text())
        # Alias lookup supplies test inputs only; query code does not read receipts.
        cls.records=cls.bundle['records']

    def n(self,alias):return URIRef(self.records[alias]['iri'])
    def ids(self,refs):return [r['identifier'] for r in refs]

    def test_01_q03_reverse_mapping_preserves_scopes(self):
        r=mappings(self.g,self.n('e-pick'));self.assertEqual(len(r['mappings']),1)
        m=r['mappings'][0]
        self.assertEqual(self.ids(m['original']),['OMIM:172700'])
        self.assertEqual(self.ids(m['normalized']),['MONDO:0017276'])
        self.assertEqual(m['original'][0]['labels'],('Pick disease',))
        self.assertNotEqual(m['original'][0]['iri'],m['normalized'][0]['iri'])
        g=clone(self.g);g.remove((self.n('map-pick'),D.mappingContext,None))
        self.assertTrue(mappings(g,self.n('e-pick'))['unavailable'])
        self.assertFalse(mappings(g,self.n('e-pick'))['mappings'])

    def test_02_q05_ambiguity_is_not_collapsed(self):
        a=mappings(self.g,self.n('e-psen-ge'))['mappings'][0]
        b=mappings(self.g,self.n('e-mapt-inclusive'))['mappings'][0]
        self.assertEqual(self.ids(a['original']),['OMIM:600274'])
        self.assertEqual(self.ids(b['original']),['OMIM:600274'])
        self.assertNotEqual(a['original'][0]['iri'],b['original'][0]['iri'])
        self.assertEqual(self.ids(a['normalized']),['MONDO:0017276'])
        self.assertEqual(self.ids(b['normalized']),['MONDO_0010857'])
        self.assertEqual((a['status'],b['status']),('unresolved','unresolved'))
        g=clone(self.g);g.remove((self.n('map-mapt-inclusive'),D.reportedDestination,None))
        self.assertEqual(mappings(g,self.n('e-mapt-inclusive'))['mappings'][0]['normalized'],[])
        # Multiple contextual mappings must be returned, not Graph.value-coalesced.
        g=clone(self.g);g.set((self.n('map-psen-ge'),D.mappingContext,self.n('e-mapt-inclusive')))
        self.assertEqual(len(mappings(g,self.n('e-mapt-inclusive'))['mappings']),2)

    def test_03_q01_original_gaps_and_source_trace(self):
        for alias in ['e-psen-ad','e-psen-ftd']:
            r=evidence(self.g,self.n(alias));m=r['mappings'][0]
            self.assertEqual(m['original'],[])
            self.assertEqual(m['gaps'][0]['field'],'field:mappingInput')
            self.assertEqual(m['gaps'][0]['reason'],'source-omission')
            self.assertTrue(r['provenance']['locator']);self.assertTrue(r['publications'])
            self.assertTrue(r['source_text'])
            self.assertEqual(r['datasource'],'europepmc')
        r=evidence(self.g,self.n('e-psen-ad'))
        self.assertEqual(r['source_id'],'1261ad02e3d662cd23a476af47159a1501d01889')
        g=clone(self.g);g.remove((self.n('e-psen-ad'),D.citesPublication,None))
        self.assertFalse(evidence(g,self.n('e-psen-ad'))['publications'])
        g.remove((self.n('e-psen-ad'),D.sourceLocator,None))
        with self.assertRaises(AcceptanceError):evidence(g,self.n('e-psen-ad'))

    def test_04_q04_rdf_only_chain_order_and_endpoints(self):
        expected={'ad-path':('MONDO:0007088','MONDO:0004975',3),
                  'ftd-path':('MONDO:0010857','MONDO:0017276',2)}
        reverse=Graph()
        for t in sorted(self.g,key=lambda t:tuple(map(str,t)),reverse=True):reverse.add(t)
        for alias,(start,end,count) in expected.items():
            r=hierarchy(self.g,self.n(alias))
            self.assertEqual((r['start']['identifier'],r['end']['identifier'],len(r['steps'])),(start,end,count))
            self.assertEqual(r,hierarchy(reverse,self.n(alias)))
        direct=membership_explanation(self.g,self.n('member-pick'))
        self.assertEqual(direct['inclusion'],'exact-anchor');self.assertEqual(direct['paths'],[])
        self.assertEqual(len(membership_explanation(self.g,self.n('member-app-inclusive'))['paths']),1)

    def test_05_chain_mutations_block_explanation(self):
        cases=[('missing',(self.n('ad-path'),D.pathStep,self.n('ad-path-step-2'))),
               ('endpoint',(self.n('ad-path-step-3'),D.parentReference,self.n('h-ftd'))),
               ('cycle',(self.n('ad-path-step-2'),D.parentReference,self.n('h-ad1'))),
               ('branch',(self.n('ad-path-step-2'),D.childReference,self.n('h-ad1')))]
        for name,triple in cases:
            with self.subTest(case=name):
                g=clone(self.g)
                if name=='missing':g.remove(triple)
                else:g.set(triple)
                with self.assertRaises(AcceptanceError):membership_explanation(g,self.n('member-app-inclusive'))
        g=clone(self.g);g.remove((self.n('ad-path'),D.pathStep,self.n('ad-path-step-3')))
        # A shorter connected path is not a valid explanation to the AD anchor.
        with self.assertRaises(AcceptanceError):membership_explanation(g,self.n('member-app-inclusive'))

    def test_06_source_snapshot_compatibility(self):
        # Different anchor/path sections are a valid documented join, not sameAs.
        self.assertEqual(len(membership_explanation(self.g,self.n('member-app-inclusive'))['paths']),1)
        unrelated=self.g.value(self.n('select-ad'),D.inSnapshot)
        g=clone(self.g);g.set((self.n('ad-path-step-2'),D.inSnapshot,unrelated))
        with self.assertRaises(AcceptanceError):hierarchy(g,self.n('ad-path'))
        g=clone(self.g);snap=g.value(self.n('ad-path'),D.inSnapshot)
        g.set((snap,D.snapshotVersion,Literal('synthetic-other-edition',datatype=XSD.string)))
        with self.assertRaises(AcceptanceError):hierarchy(g,self.n('ad-path'))

    def test_07_selected_evidence_exact_sets(self):
        expected={'select-ad':{'e-psen-ad'},
                  'select-ftd':{'e-psen-ftd','e-psen-ge','e-pick','e-grin1','e-grin3b'},
                  'select-ad-inclusive':{'e-app-inclusive'},'select-ftd-inclusive':{'e-mapt-inclusive'}}
        for context,aliases in expected.items():
            r=selection(self.g,self.n(context))
            self.assertEqual(r['occurrences'],{self.n(a) for a in aliases})
            self.assertEqual(r['state'],'partial');self.assertTrue(r['qualifications'])
        self.assertEqual(len(selection(self.g,self.n('select-ftd'))['targets']),4)

    def test_08_scoped_target_intersection_and_sensitive_removal(self):
        r=intersection(self.g,self.n('select-ad'),self.n('select-ftd'))
        self.assertEqual(r['targets'],{self.n('target-psen')})
        self.assertEqual(r['support'][self.n('target-psen')],
                         ({self.n('e-psen-ad')},{self.n('e-psen-ftd'),self.n('e-psen-ge')}))
        self.assertTrue(accept_claim(r,'sampled-shared-target'))
        g=clone(self.g);g.remove((self.n('member-psen-ad'),D.inSelectionContext,None))
        changed=intersection(g,self.n('select-ad'),self.n('select-ftd'))
        self.assertFalse(changed['targets']);self.assertFalse(accept_claim(changed,'sampled-shared-target'))
        with self.assertRaises(AcceptanceError):intersection(self.g,self.n('select-ad'),self.n('select-ftd-inclusive'))

    def test_09_partial_vs_complete_finite_scope(self):
        inputs={self.n('e-psen-ad')}
        r=bounded_extent(self.g,self.n('select-ad'),inputs)
        self.assertTrue(r['local_complete']);self.assertFalse(r['upstream_complete'])
        g=clone(self.g);g.set((self.n('select-ad'),D.completenessStatus,Literal('complete-for-declared-scope',datatype=XSD.string)))
        self.assertFalse(bounded_extent(g,self.n('select-ad'),inputs)['upstream_complete'])
        g.remove((self.n('member-psen-ad'),D.inSelectionContext,None))
        with self.assertRaises(AcceptanceError):bounded_extent(g,self.n('select-ad'),inputs)

    def test_10_project_grouping_recovery_and_ancillary_exclusion(self):
        g,n,rec,payload=grouping_control(self.g,self.n('select-ftd'),self.n('target-psen'))
        wanted={self.n('e-psen-ftd'),self.n('e-psen-ge')}
        self.assertEqual(constituents(g,n),wanted);self.assertEqual(identify(rec),str(n))
        # Identity-invalid mutations are deliberately disposable negative controls.
        g.add((n,D.contextRecord,self.n('e-pick')))
        self.assertEqual(constituents(g,n),wanted)
        extra=clone(g);extra.add((n,PROV.wasDerivedFrom,self.n('e-pick')))
        with self.assertRaises(AcceptanceError):constituents(extra,n)
        g.remove((n,PROV.wasDerivedFrom,self.n('e-psen-ge')))
        with self.assertRaises(AcceptanceError):constituents(g,n)
        with self.assertRaises(AcceptanceError):constituents(self.g,self.n('assoc-ftd-mapt'))

    def test_11_q02_shared_study_is_graph_sensitive(self):
        r=shared_studies(self.g,self.n('e-grin1'),self.n('e-grin3b'))
        self.assertEqual(r['studies'],{self.n('study-mem')})
        self.assertTrue(accept_claim(r,'shared-study',study=self.n('study-mem')))
        self.assertFalse(accept_claim(r,'independent-genetic-confirmation'))
        g=clone(self.g);g.remove((self.n('e-grin3b'),D.refersToStudy,None))
        changed=shared_studies(g,self.n('e-grin1'),self.n('e-grin3b'))
        self.assertEqual(changed['status'],'unresolved')
        self.assertFalse(accept_claim(changed,'shared-study',study=self.n('study-mem')))

    def test_12_q06_mechanism_vs_indication_positive_and_negative(self):
        r=clinical(self.g,self.n('drug-zago'))
        self.assertEqual({m['target'] for m in r['mechanisms']},{self.n('target-mapt')})
        self.assertEqual({i['disease']['identifier'] for i in r['indications']},{'MONDO:0004975',None})
        self.assertEqual([i['disease']['labels'] for i in r['indications'] if i['disease']['identifier'] is None],[('tauopathy',)])
        self.assertTrue(accept_claim(r,'reported-indication',disease_id='MONDO:0004975'))
        self.assertFalse(accept_claim(r,'reported-indication',disease_id='MONDO:0017276'))
        self.assertFalse(accept_claim(r,'efficacy'));self.assertFalse(accept_claim(r,'global-absence'))
        g=clone(self.g);g.remove((self.n('ind-zago-ad'),D.hasDrug,self.n('drug-zago')))
        changed=clinical(g,self.n('drug-zago'))
        self.assertFalse(accept_claim(changed,'reported-indication',disease_id='MONDO:0004975'))
        self.assertTrue(changed['mechanisms'])
        control=clinical(self.g,self.n('drug-leca'))
        self.assertEqual({m['target'] for m in control['mechanisms']},{self.n('target-app')})
        self.assertTrue(accept_claim(control,'reported-indication',disease_id='MONDO:0004975'))

    def test_13_q07_population_status_not_efficacy(self):
        r=clinical(self.g,self.n('drug-gos'));report=r['indications'][0]['reports'][0]
        self.assertEqual(report['study'],self.n('study-gos'))
        self.assertEqual(report['status'],('TERMINATED',));self.assertEqual(report['date'],('2019-12-19',))
        self.assertIn('four cohorts',report['populations'][0]['text'])
        self.assertTrue(accept_claim(r,'dated-population-report',study=self.n('study-gos')))
        for claim in ['efficacy','phase-implies-success','termination-implies-failure']:
            self.assertFalse(accept_claim(r,claim))
        for field in [D.hasPopulationScope,D.statusDate]:
            g=clone(self.g);g.remove((self.n('report-gos'),field,None))
            changed=clinical(g,self.n('drug-gos'))
            self.assertFalse(accept_claim(changed,'dated-population-report',study=self.n('study-gos')))
            self.assertTrue(accept_claim(changed,'reported-indication',disease_id='MONDO:0017276'))

    def test_14_positive_computation_new_identity_replay(self):
        args=(self.g,self.n('e-grin1'),self.n('e-grin3b'),self.n('select-ftd'))
        g,n,rec,payload=comparison_control(*args);g2,n2,rec2,payload2=comparison_control(*args)
        self.assertEqual((n,rec,payload),(n2,rec2,payload2));self.assertEqual(set(g),set(g2))
        self.assertNotEqual(n,self.n('dependency'))
        self.assertEqual(identify(receipt('DerivedStatement','project-operation',rec['inputs'],payload)),str(n))
        self.assertNotEqual(rec['contentRevision'],self.records['dependency']['receipt']['contentRevision'])
        self.assertNotEqual(rec['inputs']['execution'],'m1-audit-fixtures/1')
        self.assertEqual(set(g.objects(n,PROV.wasDerivedFrom)),{self.n('e-grin1'),self.n('e-grin3b')})
        self.assertEqual(set(g.objects(n,D.sharedInput)),{self.n('study-mem')})
        self.assertEqual(str(g.value(n,D.completenessStatus)),'complete-for-declared-scope')
        self.assertFalse(list(g.objects(self.n('dependency'),D.completenessStatus)))
        self.assertTrue(set(self.g)<=set(g))

    def test_15_positive_control_structural_acceptance_and_historical_failure(self):
        g,n,rec,payload=comparison_control(self.g,self.n('e-grin1'),self.n('e-grin3b'),self.n('select-ftd'))
        result,_,_=validate_graph(g)
        self.assertEqual(result['result_counts'],{'Violation':1,'Warning':8})
        violations=[r for r in result['results'] if r['severity']=='Violation']
        self.assertEqual(violations[0]['focus'],str(self.n('dependency')))
        # Acceptance view excludes only the historical negative record, in memory.
        view=clone(g);view.remove((self.n('dependency'),None,None))
        result,_,_=validate_graph(view)
        self.assertEqual(result['result_counts'],{'Warning':8})
        self.assertFalse(result['raw_shacl_conforms'])
        self.assertEqual(result['project_structural_acceptance'],'qualified-structural-pass')
        self.assertFalse(list(self.g.objects(self.n('dependency'),D.completenessStatus)))

    def test_16_grouping_control_structural_acceptance(self):
        g,n,rec,payload=grouping_control(self.g,self.n('select-ftd'),self.n('target-psen'))
        result,_,_=validate_graph(g)
        self.assertEqual(result['result_counts'],{'Violation':1,'Warning':8})
        self.assertEqual([r['focus'] for r in result['results'] if r['severity']=='Violation'],[str(self.n('dependency'))])

    def test_18_clinical_publication_depth_stays_attributed(self):
        z=clinical(self.g,self.n('drug-zago'))
        text=' '.join(x['text'] for m in z['mechanisms'] for x in m['audit_publication_context'])
        self.assertIn('METADATA ONLY',text)
        gos=clinical(self.g,self.n('drug-gos'))
        text=' '.join(x['text'] for m in gos['mechanisms'] for x in m['audit_publication_context'])
        self.assertIn('healthy-participant',text)
        g=clone(self.g);g.remove((self.n('slice:paper-33303932'),D.citesPublication,None))
        changed=clinical(g,self.n('drug-zago'))
        self.assertFalse(changed['mechanisms'][0]['audit_publication_context'])
        self.assertTrue(changed['mechanisms'])  # Mechanism record survives; paper review does not.

    def test_17_committed_inputs_unchanged(self):
        paths=subprocess.check_output(['git','ls-tree','-r','--name-only',BASELINE],cwd=ROOT,text=True).splitlines()
        for path in paths:
            self.assertEqual((ROOT/path).read_bytes(),subprocess.check_output(['git','show',BASELINE+':'+path],cwd=ROOT),path)
        self.assertEqual(len(self.g),1130);self.assertEqual(len(self.records),170)
        self.assertEqual(len(self.bundle['passages']),48)


if __name__=='__main__':unittest.main()
