"""Controlled structural/identity tests; no new source access or clinical adjudication."""
import copy
import json
import re
import socket
import subprocess
import sys
import unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
from rdflib import Graph, URIRef, Literal, RDF
from rdflib.compare import isomorphic
from m1_fixture_identity import canonical, strict_load, digest, receipt, identify, Registry, XSD, ROOT
from build_m1_audit_fixtures import build, graph_text, passage, PIN, D, PROV, validate, decision, enum_catalogue, lit, link


class Fixtures(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spec=strict_load((ROOT/'fixtures/m1/audit_fixture_spec.json').read_text())
        with patch.object(socket.socket,'connect',side_effect=AssertionError('Network forbidden')):
            cls.g,cls.bundle=build()
        cls.records=cls.bundle['records']

    def node(self,a):return URIRef(self.records[a]['iri'])
    def clone(self):
        g=Graph()
        for t in self.g:g.add(t)
        return g

    def test_pinned_passages_and_hashes(self):
        raw=subprocess.check_output(['git','show',PIN+':docs/source_audit.md'],cwd=ROOT)
        self.assertEqual(digest(raw),self.bundle['source_blob_sha256'])
        for a,p in self.spec['passages'].items():
            block,_,loc,quote=passage(raw,p)
            self.assertEqual(self.bundle['passages'][a]['quote'],quote)
            self.assertEqual(self.bundle['passages'][a]['locator'],loc)
            self.assertEqual(self.bundle['passages'][a]['sectionDigest'],digest(block))
            self.assertEqual(str(self.g.value(self.node('slice:'+a),D.sourceText)),quote)
        for r in self.records.values():
            if r['receipt']['kind']=='SourceSnapshot':
                self.assertEqual(r['receipt']['inputs']['edition'],PIN)
                self.assertEqual(r['receipt']['inputs']['provider'],'project-audit')

    def test_question_slots(self):
        self.assertEqual(set(self.bundle['questions']),{'Q0'+str(i) for i in range(1,8)})
        # Independent minimum record expectations, not just iterating an empty spec.
        minimum={'Q01':{'e-psen-ad','e-psen-ftd','e-psen-ge'},'Q02':{'e-grin1','e-grin3b','study-mem','dependency'},'Q03':{'map-pick','member-pick','h-pick'},'Q04':{'ad-path','ftd-path','e-app-inclusive','e-mapt-inclusive'},'Q05':{'map-psen-ge','map-mapt-inclusive'},'Q06':{'mech-zago','ind-zago-ad','ind-zago-tau','mech-leca'},'Q07':{'ind-gos-ftd','report-gos','population-report-gos','pub-30581980'}}
        for q,slots in minimum.items():
            actual=self.bundle['questions'][q]
            self.assertTrue(slots<=set(actual['required_records']))
            self.assertTrue(actual['unavailable_in_audit'])
            for a in actual['required_records']:self.assertIn(a,self.records)
            for a in actual['required_passages']:self.assertIn('slice:'+a,self.records)
            self.assertTrue(actual['positive_control']);self.assertTrue(actual['prohibited'])

    def test_full_evidence_and_indication_ids(self):
        expected={'1261ad02e3d662cd23a476af47159a1501d01889','986bb22bf0f7858c36fc773e5b45c08cd9c514fd','98c49197e4989f7d3be8b2f8ee3c7699e2f3d6dc','04e8f548c45ece0c2d428eef5f5aa149f67f1fbd','8bac3794c7e23d4dc3e7b44e3b2e1af8dcccc4fe','019b39b2b176f9e7df8536022682738d12e32f39','ed0b04f2d73abb84a48ed87d556725b1743a425c','0d60abae93f3438f8750a76beb2b41de9b6b3efd'}
        actual={str(self.g.value(s,D.sourceRecordIdentifier)) for s in self.g.subjects(RDF.type,D.EvidenceOccurrence)}
        self.assertEqual(actual,expected)
        for r in self.records.values():
            if r['receipt']['kind']=='EvidenceOccurrence':
                self.assertTrue(any(r['receipt']['inputs']['sourceRecordId'] in self.bundle['passages'][a]['quote'] for a in r['passages']))
        self.assertEqual(str(self.g.value(self.node('ind-gos-ftd'),D.sourceRecordIdentifier)),'c680c47a8cc2571635e1d5c629e51834273a3e67d25ebedfa9e58b729ad65189')

    def test_referent_identifiers_are_in_selected_audit(self):
        for r in self.records.values():
            if r['receipt']['kind'] in {'Target','Drug','Publication','Study'}:
                id=r['receipt']['inputs']['identifier']
                self.assertTrue(any(id.lower() in self.bundle['passages'][a]['quote'].lower() for a in r['passages']),id)

    def test_no_historical_reviewer_upgrade(self):
        for s in self.g.subjects(RDF.type,D.InspectionRecord):
            self.assertEqual(str(self.g.value(s,D.reviewerType)),'automated-check')
            self.assertEqual(str(self.g.value(s,D.interpretationOutcome)),'not-assessed')
            self.assertIn('slice:', next(a for a,r in self.records.items() if r['iri']==str(self.g.value(s,D.inspectedRecord))))
        self.assertIn('METADATA ONLY',str(self.g.value(self.node('slice:paper-33303932'),D.sourceText)))
        self.assertIn('ABSTRACT ONLY',str(self.g.value(self.node('slice:paper-22503161'),D.sourceText)))

    def test_stable_replay_and_artifacts(self):
        g,b=build()
        self.assertEqual(self.bundle,b);self.assertEqual(graph_text(self.g),graph_text(g))
        stored=json.loads((ROOT/'fixtures/m1/identity_receipts.json').read_text())
        self.assertEqual(stored['records'],b['records'])
        self.assertEqual(stored['bundle_sha256'],digest(graph_text(g).encode()))
        self.assertEqual((ROOT/'fixtures/m1/audit_derived.ttl').read_text(),graph_text(g))
        for r in b['records'].values():
            self.assertEqual(identify(r['receipt']),r['iri'])
            self.assertEqual(canonical(r['receipt']).decode(),r['canonical'])
            self.assertEqual(set(r['nullReasons']),{k for k,v in r['receipt']['inputs'].items() if v is None})

    def test_roundtrip(self):
        for fmt in ['turtle','nt']:
            with patch('rdflib.NORMALIZE_LITERALS',False):
                g=Graph().parse(data=self.g.serialize(format=fmt),format=fmt)
            self.assertTrue(isomorphic(g,self.g));validate(g,self.records)

    def test_canonical_vectors_and_unicode(self):
        rec=dict(profile='m1-id-1',kind='Study',origin='referent',inputs=dict(authority='NCT',identifier='NCT00000001',disambiguator=None),contentRevision=None)
        self.assertEqual(digest(canonical(rec)),'8a354adc22138db8c5adcd7d309b6fc7c381143363d6008420bcd74b712ad206')
        self.assertEqual(canonical(dict(reversed(list(rec.items())))),canonical(rec))
        # UTF-16 key sorting differs from Unicode codepoint sorting here.
        self.assertEqual(canonical({'\ue000':'b','\U00010000':'a'}),' {"𐀀":"a","":"b"}'.strip().encode())
        self.assertNotEqual(canonical('é'),canonical('e\u0301'))
        self.assertEqual(canonical('\b\n\\"'),b'"\\b\\n\\\\\\\""')
        for bad in [1,True,1.5,float('nan'),'\ud800']:
            with self.assertRaises((ValueError,UnicodeError)):canonical(bad)
        with self.assertRaises(ValueError):strict_load('{"x":null,"x":""}')

    def test_ordered_and_set_arrays(self):
        r=self.records['dependency'];i=copy.deepcopy(r['receipt']['inputs'])
        i['inputKeys']=list(reversed(i['inputKeys']))+[i['inputKeys'][0]]
        self.assertEqual(receipt('DerivedStatement','project-operation',i,r['identityPayload']),r['receipt'])
        r=self.records['ad-path'];i=copy.deepcopy(r['receipt']['inputs']);i['stepKeys'].reverse()
        self.assertNotEqual(identify(receipt('HierarchyPath','audit-transcription',i,r['identityPayload'])),r['iri'])

    def test_null_empty_and_wrong_keys(self):
        self.assertNotEqual(canonical(None),canonical(''));self.assertNotEqual(canonical(None),canonical([]))
        r=self.records['e-pick'];i=copy.deepcopy(r['receipt']['inputs']);i['unknown']='x'
        with self.assertRaises(ValueError):receipt('EvidenceOccurrence','audit-transcription',i,r['identityPayload'])
        i=copy.deepcopy(r['receipt']['inputs']);i['locator']=''
        with self.assertRaises(ValueError):receipt('EvidenceOccurrence','audit-transcription',i,r['identityPayload'])

    def test_payload_revision_and_mapping_direction(self):
        r=self.records['map-pick']
        self.assertTrue(any(a['field']=='mappingContext' for a in r['identityPayload']))
        changed=copy.deepcopy(r['identityPayload']);changed.append(lit('limitationText','A new explicitly scoped review limit.'))
        newer=receipt('MappingRecord','audit-transcription',r['receipt']['inputs'],changed)
        self.assertNotEqual(identify(newer),r['iri'])
        for s,o in self.g.subject_objects(D.mappingContext):self.assertIn((s,RDF.type,D.MappingRecord),self.g)
        h=self.clone();h.add((self.node('e-pick'),D.mappingContext,self.node('map-pick')))
        with self.assertRaises(ValueError):validate(h,self.records)

    def test_encounter_not_source_identity(self):
        r=self.records['select-ftd'];i=copy.deepcopy(r['receipt']['inputs']);i['execution']='m1-audit-fixtures/2'
        payload=[dict(a,value='m1-audit-fixtures/2') if a['field']=='executionReference' else a for a in r['identityPayload']]
        self.assertNotEqual(identify(receipt('SelectionContext','project-operation',i,payload)),r['iri'])
        source=self.records['e-grin1'];self.assertEqual(identify(source['receipt']),source['iri'])
        self.assertNotIn('execution',source['receipt']['inputs'])
        ledger=json.loads((ROOT/'fixtures/m1/execution_ledger.json').read_text());ledger['executions'].append(copy.deepcopy(ledger['executions'][0]))
        with self.assertRaises(ValueError):build(ledger=ledger)

    def test_membership_explanation_revision(self):
        r=self.records['member-pick']
        self.assertEqual({a['field'] for a in r['identityPayload']},{'selectedOccurrence','inSelectionContext'})
        # New explanation is a DerivedStatement about the unchanged membership.
        d=copy.deepcopy(self.records['dependency']);inputs=d['receipt']['inputs'];inputs['subjectKey']=r['iri'];inputs['scope']='Later explanation only'
        new=receipt('DerivedStatement','project-operation',inputs,[link('subjectRecord',r['iri']),lit('scopeText','Later explanation only')])
        self.assertNotEqual(identify(new),d['iri'])
        self.assertEqual(identify(r['receipt']),r['iri'])
        self.assertEqual(len(list(self.g.subjects(RDF.type,D.SelectionContext))),4)

    def test_collisions_and_immutable_conflicts(self):
        r=self.records['e-pick'];registry=Registry();registry.add(r['receipt'],r['identityPayload'])
        registry.add(r['receipt'],r['identityPayload'])
        other=copy.deepcopy(r['receipt']);other['inputs']['sourceRecordId']='different'
        with self.assertRaises(ValueError):registry.add(other,r['identityPayload'],iri=r['iri'])
        with self.assertRaises(ValueError):registry.add(r['receipt'],r['identityPayload']+[lit('limitationText','changed')])

    def test_enums_missingness_and_owner_rejections(self):
        enums,tokens=enum_catalogue();self.assertEqual(len(enums),12);self.assertEqual(len(tokens),76)
        self.assertEqual(len(list(self.g.subjects(RDF.type,D.MissingnessRecord))),2)
        h=self.clone();h.set((self.node('map-pick'),D.mappingStatus,Literal('reviewed',datatype=URIRef(XSD+'string'))))
        with self.assertRaises(ValueError):validate(h,self.records)
        h=self.clone();h.set((self.node('missing-original-psen-ad'),D.expectedField,Literal('field:unknown',datatype=URIRef(XSD+'string'))))
        with self.assertRaises(ValueError):validate(h,self.records)
        h=self.clone();h.add((self.node('e-pick'),D.sourceText,Literal('wrong owner')))
        with self.assertRaises(ValueError):validate(h,self.records)
        h=self.clone();h.set((self.node('member-pick'),D.inclusionKind,Literal('descendant-selected',datatype=URIRef(XSD+'string'))))
        with self.assertRaises(ValueError):validate(h,self.records)

    def test_positive_and_negative_paths(self):
        for p in ['ad-path','ftd-path']:self.assertEqual(decision(self.g,self.records,p),'complete-for-declared-scope')
        h=self.clone();h.remove((self.node('ad-path-step-2'),D.parentReference,None))
        self.assertEqual(decision(h,self.records,'ad-path'),'not-established-by-bundle')
        h=self.clone();h.set((self.node('ad-path-step-2'),D.parentReference,self.node('h-ad1')))
        self.assertEqual(decision(h,self.records,'ad-path'),'not-established-by-bundle')

    def test_shared_source_not_independent(self):
        self.assertEqual(decision(self.g,self.records,'shared-trial'),'shared-source-established')
        self.assertEqual(len(list(self.g.subjects(D.refersToStudy,self.node('study-mem')))),3) # two evidence records + report
        h=self.clone();h.remove((self.node('e-grin3b'),D.refersToStudy,None))
        self.assertEqual(decision(h,self.records,'shared-trial'),'unresolved')
        h=self.clone();h.set((self.node('dependency'),D.dependencyStatus,Literal('independence-assessed-with-limits',datatype=URIRef(XSD+'string'))))
        with self.assertRaises(ValueError):validate(h,self.records)

    def test_mapping_and_clinical_boundaries(self):
        self.assertEqual(decision(self.g,self.records,'q03-original'),'OMIM:172700')
        self.assertEqual(decision(self.g,self.records,'mapping-ambiguity'),'mapping-ambiguous')
        self.assertNotEqual(self.node('original-psen-ge'),self.node('original-mapt-inclusive'))
        self.assertEqual(str(self.g.value(self.node('report-gos'),D.statusDate)),'2019-12-19')
        self.assertIn('four cohorts',str(self.g.value(self.node('population-report-gos'),D.sourceText)))
        self.assertNotIn((self.node('mech-zago'),D.hasDiseaseReference,None),self.g)
        for claim in ['genetic-confirmation','ftd-treatment','clinical-benefit','current-approval','phase-implies-completion','termination-implies-failure','global-mapping-equivalence','universal-absence']:
            self.assertEqual(decision(self.g,self.records,claim),'not-established-by-bundle')
        with self.assertRaises(ValueError):decision(self.g,self.records,'unapproved question')

    def test_citation_depth_navigable_without_receipt_lookup(self):
        publication=self.g.value(self.node('mech-gos'),D.citesPublication)
        self.assertIsNotNone(publication)
        paper=self.node('pub-30581980')
        sources=set(self.g.subjects(D.citesPublication,paper))
        self.assertIn(self.node('slice:paper-30581980'),sources)
        self.assertIn('healthy-participant',str(self.g.value(self.node('slice:paper-30581980'),D.sourceText)))

    def test_complete_path_wrong_endpoint_rejected(self):
        h=self.clone();h.set((self.node('ad-path-step-3'),D.parentReference,self.node('h-ftd')))
        self.assertEqual(decision(h,self.records,'ad-path'),'not-established-by-bundle')

    def test_source_version_and_changed_occurrence(self):
        r=self.records['e-pick']
        changed=r['identityPayload']+[lit('limitationText','A revised description, not independent evidence.')]
        self.assertNotEqual(identify(receipt('EvidenceOccurrence','audit-transcription',r['receipt']['inputs'],changed)),r['iri'])
        snapshot=next(v for v in self.records.values() if v['receipt']['kind']=='SourceSnapshot')
        inputs=copy.deepcopy(snapshot['receipt']['inputs']);inputs['edition']='synthetic-new-audit-version'
        self.assertNotEqual(identify(receipt('SourceSnapshot','audit-transcription',inputs,snapshot['identityPayload'])),snapshot['iri'])

    def test_missingness_prefers_existing_mapping_field(self):
        for a in ['psen-ad','psen-ftd']:
            missing=self.node('missing-original-'+a)
            self.assertEqual(self.g.value(missing,D.aboutRecord),self.node('map-'+a))
            self.assertEqual(str(self.g.value(missing,D.expectedField)),'field:mappingInput')
            self.assertIsNone(self.g.value(self.node('map-'+a),D.mappingInput))
        # Metadata-only/inaccessible paper limits already have scoped audit slices;
        # they must not each spawn additional downstream missingness records.
        self.assertEqual(len(list(self.g.subjects(RDF.type,D.MissingnessRecord))),2)

    def test_reverse_record_order_replays_same_ids(self):
        spec=copy.deepcopy(self.spec);spec['records'].reverse()
        g,b=build(spec=spec)
        self.assertEqual(self.bundle['records'],b['records'])
        self.assertEqual(graph_text(self.g),graph_text(g))

    def test_no_hidden_schema_or_changed_ontology(self):
        self.assertEqual((ROOT/'ontology/dementiagraph-v.ttl').read_bytes(),subprocess.check_output(['git','show','09d8c7c403a8495fd3c1bc4e0ce8de76165e5eab:ontology/dementiagraph-v.ttl'],cwd=ROOT))
        self.assertEqual({r['receipt']['kind'] for r in self.records.values()}, {'SourceSnapshot','DiseaseConceptReference','Target','Drug','DiseaseTargetAssociation','EvidenceOccurrence','MappingRecord','SelectionContext','SelectionMembership','HierarchyStep','HierarchyPath','Publication','Study','StudyRecord','MechanismRecord','ClinicalIndicationRecord','PopulationScope','DerivedStatement','InspectionRecord','MissingnessRecord','SourceSlice'})
        from rdflib.namespace import OWL,RDFS
        for p in [OWL.imports,OWL.sameAs,OWL.equivalentClass,RDFS.subClassOf,RDFS.domain,RDFS.range]:self.assertFalse(list(self.g.triples((None,p,None))))

if __name__=='__main__':unittest.main()
