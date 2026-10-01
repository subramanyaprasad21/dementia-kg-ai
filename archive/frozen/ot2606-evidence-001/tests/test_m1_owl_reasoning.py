"""M1.4 bounded rule checks, not OWL DL certification or biomedical validation."""
import json
import socket
import subprocess
import sys
import unittest
from importlib.metadata import version
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, RDFS, OWL, XSD
from owlrl import DeductiveClosure, OWLRL_Semantics
from owlrl.XsdDatatypes import OWL_RL_Datatypes
from validate_m1_fixtures import ROOT, DATA, load_graph, clone
from build_m1_audit_fixtures import decision, validate as validate_fixture

BASELINE = '1e3836fce61b79c6ec78a351c2217a6847e8a5c6'
D = Namespace('https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#')
ERR = Namespace('http://www.daml.org/2002/03/agents/agent-ont#')
CONFIG = dict(axiomatic_triples=False, datatype_axioms=False,
              rdfs_closure=False, improved_datatypes=True)
ANNOTATIONS = {RDFS.label, RDFS.comment, RDFS.seeAlso, RDFS.isDefinedBy,
               OWL.versionInfo, OWL.backwardCompatibleWith, OWL.priorVersion,
               OWL.incompatibleWith, OWL.deprecated}


def reason(source):
    """No imports or persistence. Error triples are retained and inspected."""
    before = set(source)
    result = clone(source)
    with patch.object(socket.socket, 'connect', side_effect=AssertionError('Network forbidden')):
        DeductiveClosure(OWLRL_Semantics, **CONFIG).expand(result)
    if set(source) != before:
        raise AssertionError('Reasoning mutated caller input')
    errors = sorted(str(v) for v in result.objects(None, ERR.error))
    # Recognize an error node even if its message is unexpectedly absent.
    nodes = set(result.subjects(RDF.type, ERR.ErrorMessage))
    if any(not list(result.objects(n, ERR.error)) for n in nodes):
        errors.append('ErrorMessage node without diagnostic text')
    return result, errors


def unexplained_additions(source, closure):
    """Finite permitted consequence patterns for this declarations-only input.

    Not a generic OWL validator. Anything outside these reviewed patterns is
    returned, including new local claims and non-reflexive equality.
    """
    classes = set(source.subjects(RDF.type, OWL.Class)) | {OWL.Thing, OWL.Nothing}
    properties = set(source.subjects(RDF.type, OWL.ObjectProperty)) | set(source.subjects(RDF.type, OWL.DatatypeProperty))
    typed = {s for s, p, o in source if p == RDF.type and o in classes}
    datatypes = set(OWL_RL_Datatypes) | {RDFS.Literal}
    unexpected = set()
    for s, p, o in set(closure) - set(source):
        allowed = (
            (p == OWL.sameAs and s == o) or
            (p == OWL.equivalentClass and s == o and s in classes) or
            (p in {OWL.equivalentProperty, RDFS.subPropertyOf} and s == o and s in properties) or
            (p == RDFS.subClassOf and s in classes and o in classes and
             (s == o or o == OWL.Thing or s == OWL.Nothing)) or
            (p == RDF.type and o == OWL.Class and s in {OWL.Thing, OWL.Nothing}) or
            (p == RDF.type and o == OWL.AnnotationProperty and s in ANNOTATIONS) or
            (p == RDF.type and o == RDFS.Datatype and s in datatypes) or
            (p == RDF.type and o == OWL.Thing and s in typed) or
            (p == RDF.type and isinstance(s, Literal) and o in datatypes and s.datatype == o) or
            (p == OWL.disjointWith and (s, o) == (XSD.dateTime, XSD.string))
        )
        if not allowed:
            unexpected.add((s, p, o))
    return unexpected


class OWLReasoning(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = load_graph(ROOT / 'ontology/dementiagraph-v.ttl')
        cls.data = load_graph(DATA)
        cls.input = cls.schema + cls.data
        cls.bundle = json.loads((ROOT / 'fixtures/m1/identity_receipts.json').read_text())
        cls.records = cls.bundle['records']
        cls.schema_closure, cls.schema_errors = reason(cls.schema)
        cls.closure, cls.errors = reason(cls.input)

    def node(self, alias):
        return URIRef(self.records[alias]['iri'])

    def test_01_inventory_and_no_prohibited_input_axioms(self):
        self.assertEqual(len(self.schema), 355)
        for kind, count in [(OWL.Class, 20), (OWL.ObjectProperty, 27), (OWL.DatatypeProperty, 39)]:
            self.assertEqual(sum(str(s).startswith(str(D)) for s in self.schema.subjects(RDF.type, kind)), count)
        prov = Namespace('http://www.w3.org/ns/prov#')
        self.assertEqual(set(self.schema.subjects(RDF.type, OWL.Class)) -
                         {s for s in self.schema.subjects(RDF.type, OWL.Class) if str(s).startswith(str(D))}, {prov.Entity})
        self.assertIn((prov.wasDerivedFrom, RDF.type, OWL.ObjectProperty), self.schema)
        self.assertEqual(set(self.schema.predicates()), {RDF.type, RDFS.label, RDFS.comment,
                                                        RDFS.isDefinedBy, OWL.versionIRI, OWL.versionInfo})
        self.assertEqual(set(self.schema.objects(None, RDF.type)),
                         {OWL.Class, OWL.ObjectProperty, OWL.DatatypeProperty, OWL.Ontology})
        # The instance input cannot smuggle in keys, restrictions or other OWL axioms.
        self.assertTrue(set(self.data.predicates()) <= set(self.schema.subjects(RDF.type, OWL.ObjectProperty)) |
                        set(self.schema.subjects(RDF.type, OWL.DatatypeProperty)) | {RDF.type})
        self.assertTrue(set(self.data.objects(None, RDF.type)) <= set(self.schema.subjects(RDF.type, OWL.Class)))

    def test_02_schema_diagnostics_and_consequences(self):
        self.assertEqual(self.schema_errors, [])
        self.assertFalse(unexplained_additions(self.schema, self.schema_closure))
        self.assertTrue(set(self.schema) <= set(self.schema_closure))

    def test_03_combined_diagnostics_and_consequences(self):
        self.assertEqual(self.errors, [])
        self.assertFalse(unexplained_additions(self.input, self.closure))
        self.assertTrue(set(self.input) <= set(self.closure))
        self.assertFalse(any(str(p).startswith(str(D)) for _, p, _ in set(self.closure) - set(self.input)))

    def test_04_positive_builtin_entailment(self):
        n = self.node('map-pick')
        self.assertNotIn((n, OWL.sameAs, n), self.input)
        self.assertIn((n, OWL.sameAs, n), self.closure)
        self.assertNotIn((D.MappingRecord, RDFS.subClassOf, OWL.Thing), self.schema)
        self.assertIn((D.MappingRecord, RDFS.subClassOf, OWL.Thing), self.schema_closure)

    def test_05_isolated_nothing_contradiction(self):
        graph = Graph()
        graph.add((URIRef('urn:m1-test:contradiction'), RDF.type, OWL.Nothing))
        result, errors = reason(graph)
        self.assertTrue(errors)
        self.assertTrue(any('Nothing' in e for e in errors), errors)
        self.assertTrue(list(result.subjects(RDF.type, ERR.ErrorMessage)))
        self.assertEqual(len(graph), 1)

    def test_06_mapping_does_not_create_equality(self):
        for alias in ['map-pick', 'map-psen-ge', 'map-mapt-inclusive']:
            m = self.node(alias)
            a, b = self.data.value(m, D.mappingInput), self.data.value(m, D.reportedDestination)
            self.assertIsNotNone(a); self.assertIsNotNone(b); self.assertNotEqual(a, b)
            for p in [OWL.sameAs, OWL.equivalentClass, OWL.differentFrom]:
                self.assertNotIn((a, p, b), self.closure)
                self.assertNotIn((b, p, a), self.closure)
        self.assertEqual(decision(self.data, self.records, 'mapping-ambiguity'), 'mapping-ambiguous')

    def test_07_hierarchy_navigation_is_not_equivalence(self):
        steps = list(self.data.subjects(RDF.type, D.HierarchyStep))
        self.assertEqual(len(steps), 5)
        for step in steps:
            a, b = self.data.value(step, D.childReference), self.data.value(step, D.parentReference)
            self.assertNotEqual(a, b)
            for p in [OWL.sameAs, OWL.equivalentClass, RDFS.subClassOf]:
                self.assertNotIn((a, p, b), self.closure)
                self.assertNotIn((b, p, a), self.closure)

    def test_08_association_no_causal_upgrade(self):
        # There is intentionally no causality predicate: test no new association
        # content, not a vacuous query over invented biomedical vocabulary.
        owners = set(self.data.subjects(RDF.type, D.DiseaseTargetAssociation))
        self.assertTrue(owners)
        added = set(self.closure) - set(self.input)
        self.assertFalse(any(s in owners and str(p).startswith(str(D)) for s, p, _ in added))
        self.assertFalse(unexplained_additions(self.input, self.closure))
        # Interpreting existing prose/scores as causality remains manual/application work.

    def test_09_shared_evidence_not_independent_confirmation(self):
        self.assertEqual(decision(self.closure, self.records, 'shared-trial'), 'shared-source-established')
        independent = (self.node('dependency'), D.dependencyStatus,
                       Literal('independence-assessed-with-limits', datatype=XSD.string))
        self.assertNotIn(independent, self.closure)
        bad = clone(self.data); bad.set(independent)
        with self.assertRaises(ValueError):
            validate_fixture(bad, self.records)
        self.assertEqual(decision(self.data, self.records, 'genetic-confirmation'), 'not-established-by-bundle')

    def test_10_mechanism_not_indication_or_efficacy(self):
        mechanisms = set(self.data.subjects(RDF.type, D.MechanismRecord))
        self.assertTrue(mechanisms)
        for n in mechanisms:
            self.assertNotIn((n, RDF.type, D.ClinicalIndicationRecord), self.closure)
            self.assertNotIn((n, D.hasDiseaseReference, None), self.closure)
        self.assertEqual(set(self.data.subjects(RDF.type, D.ClinicalIndicationRecord)),
                         set(self.closure.subjects(RDF.type, D.ClinicalIndicationRecord)))
        for request in ['ftd-treatment', 'clinical-benefit']:
            self.assertEqual(decision(self.data, self.records, request), 'not-established-by-bundle')

    def test_11_trial_status_not_success(self):
        n = self.node('report-gos')
        for p in [D.trialPhaseText, D.trialStatusText, D.statusDate]:
            self.assertTrue(list(self.data.objects(n, p)))
            self.assertEqual(set(self.data.objects(n, p)), set(self.closure.objects(n, p)))
        self.assertFalse(any(s == n and str(p).startswith(str(D))
                             for s, p, _ in set(self.closure) - set(self.input)))
        for request in ['phase-implies-completion', 'termination-implies-failure', 'clinical-benefit']:
            self.assertEqual(decision(self.data, self.records, request), 'not-established-by-bundle')

    def test_12_missing_evidence_not_negation(self):
        source = clone(self.input)
        n = self.node('e-grin3b')
        source.remove((n, D.refersToStudy, None))
        result, errors = reason(source)
        self.assertFalse(errors)
        self.assertFalse(unexplained_additions(source, result))
        self.assertNotIn((None, RDF.type, OWL.NegativePropertyAssertion), result)
        self.assertNotIn((None, OWL.differentFrom, None), result)
        self.assertEqual(decision(result, self.records, 'shared-trial'), 'unresolved')
        self.assertEqual(decision(result, self.records, 'universal-absence'), 'not-established-by-bundle')

    def test_13_incomplete_path_not_completed(self):
        self.assertEqual(decision(self.data, self.records, 'ad-path'), 'complete-for-declared-scope')
        source = clone(self.input)
        missing = (self.node('ad-path'), D.pathStep, self.node('ad-path-step-2'))
        self.assertIn(missing, source); source.remove(missing)
        result, errors = reason(source)
        self.assertFalse(errors)
        self.assertNotIn(missing, result)
        self.assertFalse(unexplained_additions(source, result))
        self.assertEqual(decision(result, self.records, 'ad-path'), 'not-established-by-bundle')
        # Any pre-existing completeness label is an assertion, not a new entailment.
        self.assertEqual(set(source.objects(self.node('ad-path'), D.completenessStatus)),
                         set(result.objects(self.node('ad-path'), D.completenessStatus)))

    def test_14_forbidden_result_detector(self):
        bad = clone(self.closure)
        a, b = self.node('original-psen-ge'), self.node('original-mapt-inclusive')
        injected = (a, OWL.sameAs, b)
        self.assertNotEqual(a, b); self.assertNotIn(injected, bad)
        bad.add(injected)
        self.assertEqual(unexplained_additions(self.input, bad), {injected})

    def test_15_datatypes_and_engine_limitations_visible(self):
        datatypes = {o.datatype for _, _, o in self.data if isinstance(o, Literal)}
        self.assertEqual(datatypes, {XSD.string, XSD.date, XSD.dateTime})
        self.assertTrue(datatypes <= set(OWL_RL_Datatypes))
        # owlrl retains generalized RDF with literal subjects internally. Do not
        # serialize this closure as an asserted Turtle source artifact.
        self.assertTrue(any(isinstance(s, Literal) for s, _, _ in self.closure))
        self.assertEqual(set(self.closure.triples((None, OWL.disjointWith, None))),
                         {(XSD.dateTime, OWL.disjointWith, XSD.string)})

    def test_16_known_structural_gap_not_repaired_by_reasoning(self):
        n = self.node('dependency')
        self.assertNotIn((n, D.completenessStatus, None), self.data)
        self.assertNotIn((n, D.completenessStatus, None), self.closure)
        self.assertFalse(self.errors)  # Does NOT mean structural acceptance.
        # Exact 1/8 baseline and 0/8 synthetic-control SHACL outcomes are checked
        # by the unchanged Task 008 suite over raw data, never the OWL closure.

    def test_17_configuration_and_versions(self):
        self.assertEqual(version('owlrl'), '7.1.4')
        self.assertEqual(version('rdflib'), '7.1.4')
        self.assertEqual(CONFIG, dict(axiomatic_triples=False, datatype_axioms=False,
                                      rdfs_closure=False, improved_datatypes=True))

    def test_18_all_committed_inputs_unchanged(self):
        paths = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', BASELINE], cwd=ROOT,
                                        text=True).splitlines()
        import ast
        # Only the named guard methods may change; all other test code stays pinned.
        guard_methods = {
            'tests/test_m1_shacl.py': 'test_26_committed_inputs_and_inventory_unchanged',
            'tests/test_m1_owl_reasoning.py': 'test_18_all_committed_inputs_unchanged',
            'tests/test_m1_semantic_acceptance.py': 'test_17_committed_inputs_unchanged',
        }

        def without_guard(data, method):
            matches = [n for n in ast.walk(ast.parse(data))
                       if isinstance(n, ast.FunctionDef) and n.name == method]
            self.assertEqual(len(matches), 1, method)
            node = matches[0]
            lines = data.splitlines(keepends=True)
            return b''.join(lines[:node.lineno - 1] + lines[node.end_lineno:])

        closure = '9fd456f7a8a6669b6c7f035cf3693ccbd64b5a91'
        for path in sorted(set(paths) | {'docs/m1_semantic_acceptance.md'}):
            # Pin the approved closure text, rather than exempting README/docs.
            revision = closure if path in {'README.md', 'docs/m1_semantic_acceptance.md'} else BASELINE
            expected = subprocess.check_output(['git', 'show', revision + ':' + path], cwd=ROOT)
            actual = (ROOT / path).read_bytes()
            if path in guard_methods:
                actual = without_guard(actual, guard_methods[path])
                expected = without_guard(expected, guard_methods[path])
            self.assertEqual(actual, expected, path)
        self.assertEqual(len(self.data), 1130)
        self.assertEqual(len(self.records), 170)
        self.assertEqual(len(self.bundle['passages']), 48)
        self.assertEqual(sum(r['receipt']['kind'] == 'SourceSnapshot' for r in self.records.values()), 12)


if __name__ == '__main__':
    unittest.main()
