"""Task 008 synthetic structural controls; never replacement source evidence."""
import json
import socket
import subprocess
import sys
import unittest
from collections import Counter
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import frozen_snapshots as frozen
from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, XSD, SH, OWL
from rdflib.compare import isomorphic
from pyshacl.errors import ReportableRuntimeError
from validate_m1_fixtures import (ROOT, DATA, SHAPES, M1S, CONFIG, load_graph,
                                 clone, validate_graph, synthetic_completeness_control,
                                 lexical_preservation)
from build_m1_audit_fixtures import enum_catalogue

D = Namespace('https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#')
S = Namespace(M1S)
BASELINE = '855c16191bb49f7bb885716ee4c90b18d0db66f6'


def string(value):
    return Literal(value, datatype=XSD.string)


class StructuralValidation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data, cls.shapes = load_graph(DATA), load_graph(SHAPES)
        cls.receipts = json.loads((ROOT / 'fixtures/m1/identity_receipts.json').read_text())
        cls.control = synthetic_completeness_control(cls.data)

    def node(self, alias):
        return URIRef(self.receipts['records'][alias]['iri'])

    def run_graph(self, graph):
        with patch.object(socket.socket, 'connect', side_effect=AssertionError('No network')):
            return validate_graph(graph, self.shapes)[0]

    def change(self, graph, alias, field, value):
        graph.set((self.node(alias), D[field], string(value)))

    def passed(self, graph):
        result = self.run_graph(graph)
        self.assertEqual(result['result_counts'].get('Violation', 0), 0, result['results'])
        return result

    def failed(self, graph, name):
        result = self.run_graph(graph)
        self.assertEqual(result['project_structural_acceptance'], 'blocked')
        self.assertTrue(any(r['severity'] == 'Violation' and
                            r['source_shape'] == M1S + name for r in result['results']), result)
        return result

    def test_01_expected_baseline(self):
        result = self.run_graph(self.data)
        self.assertEqual(result['result_counts'], {'Violation': 1, 'Warning': 8})
        self.assertFalse(result['raw_shacl_conforms'])
        self.assertEqual(result['project_structural_acceptance'], 'blocked')
        violation = [r for r in result['results'] if r['severity'] == 'Violation'][0]
        self.assertEqual(violation['focus'], str(self.node('dependency')))
        self.assertEqual(violation['path'], str(D.completenessStatus))
        self.assertEqual(Counter(r['source_shape'].split('#')[-1] for r in result['results']
                                 if r['severity'] == 'Warning'),
                         {'PartialSelection': 4, 'UnresolvedMapping': 2, 'RecordedSourceOmission': 2})

    def test_02_synthetic_control_separates_acceptance(self):
        result = self.passed(self.control)
        self.assertFalse(result['raw_shacl_conforms'])
        self.assertEqual(result['result_counts'], {'Warning': 8})
        self.assertEqual(result['project_structural_acceptance'], 'qualified-structural-pass')
        self.assertEqual(len(self.control), 1131)
        self.assertEqual(len(self.data), 1130)
        self.assertNotIn((self.node('dependency'), D.completenessStatus, None), self.data)

    def test_03_warning_free_nonempty_control(self):
        graph = Graph()
        node = URIRef('urn:task008:synthetic-target')
        graph.add((node, RDF.type, D.Target))
        graph.add((node, D.externalIdentifier, string('synthetic-control')))
        graph.add((node, D.identifierAuthority, string('test-only')))
        result = self.passed(graph)
        self.assertTrue(result['raw_shacl_conforms'])
        self.assertEqual(result['project_structural_acceptance'], 'structural-pass')

    def test_04_missing_membership_participant(self):
        graph = clone(self.control)
        graph.remove((self.node('member-pick'), D.selectedOccurrence, None))
        self.failed(graph, 'SelectionMembership_selectedOccurrence_required')

    def test_05_reverse_mapping_context(self):
        graph = clone(self.control)
        owner = self.node('map-pick')
        value = graph.value(owner, D.mappingContext)
        graph.remove((owner, D.mappingContext, value))
        graph.add((value, D.mappingContext, owner))
        result = self.failed(graph, 'MappingRecord_mappingContext_required')
        self.assertTrue(any(r['source_shape'] == M1S + 'Owner_mappingContext'
                            for r in result['results']))

    def test_06_wrong_participant_type_and_lost_owner_type(self):
        graph = clone(self.control)
        graph.set((self.node('mech-zago'), D.hasTarget, self.node('drug-zago')))
        self.failed(graph, 'Owner_hasTarget')
        graph = clone(self.control)
        graph.remove((self.node('map-pick'), RDF.type, D.MappingRecord))
        self.failed(graph, 'Owner_mappingContext')

    def test_07_contextual_information_resource_allowed(self):
        graph = clone(self.control)
        source = self.node('slice:paper-30581980')
        graph.set((self.node('map-pick'), D.mappingContext, source))
        self.passed(graph)

    def test_08_exact_catalogues(self):
        enums, tokens = enum_catalogue()
        self.assertEqual(len(enums), 12)
        self.assertEqual(len(tokens), 76)
        for field, values in enums.items():
            shape = S['Enum_' + field]
            prop = self.shapes.value(shape, SH.property)
            head = self.shapes.value(prop, SH['in'])
            self.assertEqual(set(self.shapes.items(head)), {string(v) for v in values})
        prop = self.shapes.value(S.MissingnessToken, SH.property)
        self.assertEqual(set(self.shapes.items(self.shapes.value(prop, SH['in']))),
                         {string(v) for v in tokens})
        # Each token has a conditional owner check, including the nine gaps.
        applied = {str(v) for v in self.shapes.objects(None, SH.hasValue)
                   if str(v).startswith(('field:', 'requirement:'))}
        self.assertEqual(applied, tokens)

    def test_09_enum_case_and_padding_are_invalid(self):
        for value in ['DIRECT-ONLY', 'direct-only ']:
            with self.subTest(value=value):
                graph = clone(self.control)
                self.change(graph, 'select-ad', 'selectionMode', value)
                self.failed(graph, 'Enum_selectionMode')

    def test_10_invalid_missingness_token(self):
        graph = clone(self.control)
        self.change(graph, 'missing-original-psen-ad', 'expectedField', 'field:invented')
        self.failed(graph, 'MissingnessToken')

    def test_11_missingness_wrong_owner(self):
        graph = clone(self.control)
        graph.set((self.node('missing-original-psen-ad'), D.aboutRecord, self.node('drug-zago')))
        result = self.run_graph(graph)
        self.assertEqual(result['project_structural_acceptance'], 'blocked')
        self.assertTrue(any(r['severity'] == 'Violation' and 'MissingOwner_' in r['source_shape']
                            for r in result['results']), result)

    def test_12_not_applicable_still_requires_rationale(self):
        graph = clone(self.control)
        self.change(graph, 'missing-original-psen-ad', 'missingnessReason', 'not-applicable')
        graph.remove((self.node('missing-original-psen-ad'), D.rationale, None))
        self.failed(graph, 'MissingnessRecord_rationale_required')

    def test_13_direct_descendant_conflict(self):
        graph = clone(self.control)
        self.change(graph, 'member-pick', 'inclusionKind', 'descendant-selected')
        self.failed(graph, 'DirectMembership')

    def test_14_access_depth_conflict_and_qualified_partial(self):
        graph = clone(self.control)
        self.change(graph, 'inspection-Q01', 'accessOutcome', 'inaccessible')
        self.change(graph, 'inspection-Q01', 'interpretationOutcome', 'access-limited')
        self.failed(graph, 'AccessDepth')
        graph.remove((self.node('inspection-Q01'), D.inspectionDepth, None))
        result = self.passed(graph)
        self.assertEqual(result['result_counts']['Warning'], 9)

    def test_15_partial_path_allowed_complete_empty_path_rejected(self):
        graph = clone(self.control)
        graph.remove((self.node('ad-path'), D.pathStep, None))
        self.failed(graph, 'CompletePathSteps')
        self.change(graph, 'ad-path', 'completenessStatus', 'partial')
        result = self.passed(graph)
        self.assertEqual(result['result_counts']['Warning'], 9)

    def test_16_missing_selection_metadata_not_excused_by_partial(self):
        graph = clone(self.control)
        graph.remove((self.node('select-ad'), D.executionReference, None))
        self.failed(graph, 'SelectionContext_executionReference_required')

    def test_17_computation_metadata_mandatory(self):
        graph = clone(self.control)
        fields = ['operationMethod', 'methodVersion', 'executionReference', 'scopeText']
        for field in fields:
            graph.remove((self.node('dependency'), D[field], None))
        result = self.run_graph(graph)
        found = {r['source_shape'] for r in result['results'] if r['severity'] == 'Violation'}
        for field in fields:
            self.assertIn(M1S + 'DerivedStatement_' + field + '_required', found)
        self.assertEqual(result['project_structural_acceptance'], 'blocked')

    def test_18_trial_status_wrong_owner(self):
        graph = clone(self.control)
        self.change(graph, 'mech-zago', 'trialStatusText', 'synthetic-status')
        self.failed(graph, 'Owner_trialStatusText')

    def test_19_undated_status_warning_preserves_uncertainty(self):
        graph = clone(self.control)
        graph.remove((self.node('report-gos'), D.statusDate, None))
        result = self.passed(graph)
        self.assertEqual(result['result_counts']['Warning'], 9)

    def test_20_missingness_does_not_waive_endpoint(self):
        graph = clone(self.control)
        step = self.node('ad-path-step-1')
        graph.remove((step, D.childReference, None))
        missing = URIRef('urn:task008:synthetic-missingness')
        for predicate, value in [(RDF.type, D.MissingnessRecord),
                                 (D.aboutRecord, step),
                                 (D.expectedField, string('field:childReference')),
                                 (D.missingnessReason, string('unresolved')),
                                 (D.observationContext, self.node('inspection-Q04')),
                                 (D.rationale, string('Synthetic control: absent mandatory endpoint.'))]:
            graph.add((missing, predicate, value))
        self.failed(graph, 'HierarchyStep_childReference_required')

    def test_21_input_only_mapping_conflict(self):
        graph = clone(self.control)
        self.change(graph, 'map-pick', 'mappingStatus', 'input-only')
        self.failed(graph, 'InputOnlyMapping')
        graph.remove((self.node('map-pick'), D.reportedDestination, None))
        self.passed(graph)

    def test_22_shared_basis_required_not_proof_of_independence(self):
        graph = clone(self.control)
        graph.remove((self.node('dependency'), D.sharedInput, None))
        self.failed(graph, 'SharedBasis')

    def test_27_source_aggregate_cannot_use_grouping_context(self):
        graph = clone(self.control)
        association = next(graph.subjects(RDF.type, D.DiseaseTargetAssociation))
        graph.set((association, D.originRole, string('source-aggregate')))
        graph.add((association, D.inSelectionContext, self.node('select-ad')))
        self.failed(graph, 'GroupingSelection')

    def test_28_mechanism_indication_record_separation(self):
        graph = clone(self.control)
        graph.add((self.node('mech-zago'), RDF.type, D.ClinicalIndicationRecord))
        self.failed(graph, 'ClinicalRecordSeparation')

    def test_29_score_requires_qualified_source_context(self):
        graph = clone(self.control)
        association = next(graph.subjects(RDF.type, D.DiseaseTargetAssociation))
        graph.remove((association, D.inSelectionContext, None))
        graph.set((association, D.originRole, string('source-aggregate')))
        graph.set((association, D.aggregateScore, Literal('0.2', datatype=XSD.decimal)))
        graph.remove((association, D.scoreDefinition, None))
        graph.remove((association, D.limitationText, None))
        self.failed(graph, 'ScoreContext')
        graph.set((association, D.limitationText, string('Synthetic uninterpreted score control.')))
        result = self.passed(graph)
        self.assertEqual(result['result_counts']['Warning'], 9)

    def test_30_unresolved_inclusion_requires_qualification(self):
        graph = clone(self.control)
        self.change(graph, 'member-pick', 'inclusionKind', 'unresolved')
        graph.remove((self.node('member-pick'), D.limitationText, None))
        self.failed(graph, 'UnresolvedInclusionBasis')
        self.change(graph, 'member-pick', 'limitationText', 'Synthetic unresolved explanation.')
        self.passed(graph)

    def test_31_inspected_passages_require_scope(self):
        graph = clone(self.control)
        graph.remove((self.node('inspection-Q01'), D.scopeText, None))
        self.failed(graph, 'InspectionScope')

    def test_23_meta_shacl_rejects_malformed_shapes(self):
        shapes = clone(self.shapes)
        shapes.set((S.DerivedStatement_completenessStatus_required, SH.minCount, string('wrong')))
        with self.assertRaises(ReportableRuntimeError):
            validate_graph(self.control, shapes)

    def test_24_local_core_configuration(self):
        self.assertEqual(CONFIG['inference'], 'none')
        self.assertTrue(CONFIG['meta_shacl'])
        for key in ['advanced', 'js', 'iterate_rules', 'do_owl_imports', 'inplace',
                    'allow_infos', 'allow_warnings']:
            self.assertFalse(CONFIG[key])
        for predicate in [OWL.imports, SH.sparql, SH.rule, SH.js]:
            self.assertFalse(any(self.shapes.triples((None, predicate, None))))
        forbidden = clone(self.shapes)
        forbidden.add((S.InformationResource, OWL.imports, URIRef('urn:forbidden')))
        with self.assertRaises(ValueError):
            validate_graph(self.control, forbidden)

    def test_25_roundtrip_and_no_input_mutation(self):
        before_data, before_shapes = set(self.control), set(self.shapes)
        self.passed(self.control)
        self.assertEqual(set(self.control), before_data)
        self.assertEqual(set(self.shapes), before_shapes)
        for graph in [self.data]:
            with lexical_preservation():
                parsed = Graph().parse(data=graph.serialize(format='turtle'), format='turtle')
            # RDFLib blank-node labels survive this serialization; graph equivalence
            # otherwise uses its canonical isomorphism check.
            self.assertTrue(set(graph) == set(parsed) or isomorphic(graph, parsed))

    def test_26_committed_inputs_and_inventory_unchanged(self):
        verified = frozen.verify_manifest_section(
            ROOT / 'manifests/ot2606-evidence-001.freeze.json',
            'authorities', 'ot2606-evidence-001')
        self.assertIn('README.md', verified)
        self.assertIn('tests/test_m1_shacl.py', verified)
        self.assertEqual(len(self.data), 1130)
        self.assertEqual(len(self.receipts['records']), 170)
        self.assertEqual(len(self.receipts['passages']), 48)
        self.assertEqual(sum(r['receipt']['kind'] == 'SourceSnapshot'
                             for r in self.receipts['records'].values()), 12)


if __name__ == '__main__':
    unittest.main()
