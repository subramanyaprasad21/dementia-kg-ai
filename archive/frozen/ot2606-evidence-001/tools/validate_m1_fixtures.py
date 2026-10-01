"""Local SHACL Core checks. Raw conformance is not biomedical acceptance."""
import json
from collections import Counter, deque
from contextlib import contextmanager
from importlib.metadata import version
from pathlib import Path

import rdflib
from rdflib import Graph, URIRef
from rdflib.namespace import RDF, OWL, SH
from pyshacl import validate

ROOT = Path(__file__).resolve().parents[1]
SHAPES = ROOT / 'validation/m1_shapes.ttl'
DATA = ROOT / 'fixtures/m1/audit_derived.ttl'
M1S = 'https://github.com/subramanyaprasad21/dementia-kg-ai/validation/m1#'
CONFIG = dict(inference='none', advanced=False, js=False, iterate_rules=False,
              meta_shacl=True, do_owl_imports=False, inplace=False,
              abort_on_first=False, allow_infos=False, allow_warnings=False)
PACKAGES = ['pyshacl', 'rdflib', 'owlrl', 'packaging', 'prettytable',
            'pyparsing', 'html5rdf', 'wcwidth']


@contextmanager
def lexical_preservation():
    """Single-threaded local parsing; preserve archived literal spellings."""
    previous = rdflib.NORMALIZE_LITERALS
    rdflib.NORMALIZE_LITERALS = False
    try:
        yield
    finally:
        rdflib.NORMALIZE_LITERALS = previous


def load_graph(path):
    if not isinstance(path, Path) or not path.is_file():
        raise ValueError('An existing local Path is required; no URL inputs')
    with lexical_preservation():
        return Graph().parse(data=path.read_bytes(), format='turtle')


def clone(graph):
    result = Graph()
    for triple in graph:
        result.add(triple)
    return result


def named_shape(shapes, node):
    """Diagnostic name only; leave the original engine report untouched."""
    queue, seen = deque([node]), set()
    while queue:
        item = queue.popleft()
        if item in seen:
            continue
        seen.add(item)
        if isinstance(item, URIRef) and str(item).startswith(M1S):
            return str(item)
        queue.extend(sorted(set(shapes.subjects(None, item)), key=str))
    return str(node)


def validate_graph(data=None, shapes=None):
    data = load_graph(DATA) if data is None else data
    shapes = load_graph(SHAPES) if shapes is None else shapes
    if not isinstance(data, Graph) or not isinstance(shapes, Graph):
        raise TypeError('Pass local RDFLib graphs, not endpoints')
    for predicate in [OWL.imports, SH.sparql, SH.rule, SH.js]:
        if any(shapes.triples((None, predicate, None))):
            raise ValueError('Only local SHACL Core shapes are authorized')
    before, shape_before = clone(data), clone(shapes)
    # No ontology graph is mixed into the data. Explicit type assertions supply
    # participant checks; no RDFS/OWL closure or rule engine is invoked.
    conforms, report, text = validate(data_graph=clone(data), shacl_graph=clone(shapes),
                                      ont_graph=None, **CONFIG)
    if not isinstance(report, Graph):
        raise RuntimeError('Validator did not produce a validation report: ' + str(report))
    if set(before) != set(data) or set(shape_before) != set(shapes):
        raise RuntimeError('Validation mutated an input graph')
    rows = []
    reports = list(report.subjects(RDF.type, SH.ValidationReport))
    if len(reports) != 1:
        raise RuntimeError('Expected one raw validation report')
    for result in report.objects(reports[0], SH.result):
        severity = str(report.value(result, SH.resultSeverity)).rsplit('#', 1)[-1]
        path = report.value(result, SH.resultPath)
        messages = sorted(str(x) for x in report.objects(result, SH.resultMessage))
        source = report.value(result, SH.sourceShape)
        rows.append(dict(focus=str(report.value(result, SH.focusNode)),
                         path=str(path) if isinstance(path, URIRef) else None,
                         severity=severity, source_shape=named_shape(shapes, source),
                         component=str(report.value(result, SH.sourceConstraintComponent)),
                         messages=messages))
    rows.sort(key=lambda r: (r['severity'], r['focus'], r['source_shape'], r['path'] or ''))
    counts = Counter(r['severity'] for r in rows)
    raw_conforms = report.value(reports[0], SH.conforms).toPython()
    if bool(conforms) != raw_conforms:
        raise RuntimeError('Engine return and raw sh:conforms disagree')
    acceptance = ('blocked' if counts['Violation'] else
                  'qualified-structural-pass' if counts['Warning'] or counts['Info'] else
                  'structural-pass')
    summary = dict(raw_shacl_conforms=raw_conforms,
                   project_structural_acceptance=acceptance,
                   result_counts=dict(counts), results=rows,
                   configuration=CONFIG.copy(),
                   scope='M1 local structural validation only; no biomedical/source-completeness/independence judgment')
    return summary, report, text


def synthetic_completeness_control(data=None):
    """In-memory structural mutation only; never save or mint new evidence."""
    data = load_graph(DATA) if data is None else data
    result = clone(data)
    receipts = json.loads((ROOT / 'fixtures/m1/identity_receipts.json').read_text())
    target = URIRef(receipts['records']['dependency']['iri'])
    predicate = URIRef('https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#completenessStatus')
    if (target, predicate, None) in result:
        raise ValueError('Expected the committed completeness gap to remain present')
    result.add((target, predicate, rdflib.Literal('complete-for-declared-scope', datatype=rdflib.XSD.string)))
    # This mutation intentionally is NOT an identity-valid replacement artifact.
    # It proves shape behavior only, leaving original receipts and data untouched.
    return result


def main():
    summary, _, _ = validate_graph()
    summary['dependency_versions'] = {name: version(name) for name in PACKAGES}
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 1 if summary['project_structural_acceptance'] == 'blocked' else 0


if __name__ == '__main__':
    raise SystemExit(main())
