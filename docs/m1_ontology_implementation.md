# M1 Task 006 — first declarations-only ontology implementation

Baseline: `09a89476603d1744d534e91504c13c2575badeb3`. Implemented under explicit owner authorization. **Implementation complete for schema declarations only; pending owner review, uncommitted.**

## Scope and governing specifications

Created only `ontology/dementiagraph-v.ttl` and this document. The schema follows [readiness sections 15–16](m1_implementation_readiness.md#15-exact-first-ontology-file-plan-not-executed), the [conceptual contract](m1_conceptual_model_contract.md), [approved mechanics](m1_implementation_mechanics.md), [charter](project_charter.md), and frozen Q01–Q07/R1–R14. The [schema investigation](m1_schema_design.md) remains historical rationale. No approved document was edited.

The ontology contains declarations, English labels/comments and standard descriptive metadata. Intended owners, direction, qualifications and forbidden interpretations are annotations, not logical constraints. There are no records, individual biomedical assertions, enum individuals, restrictions or imports. Referencing the external PROV terms does not load the PROV ontology or its axioms.

## Exact inventory

**Local classes (20):** SourceSnapshot, DiseaseConceptReference, Target, Drug, DiseaseTargetAssociation, EvidenceOccurrence, MappingRecord, SelectionContext, SelectionMembership, HierarchyStep, HierarchyPath, Publication, Study, StudyRecord, MechanismRecord, ClinicalIndicationRecord, PopulationScope, DerivedStatement, InspectionRecord, MissingnessRecord.

**Usable object properties (28: 27 local and one external):** inSnapshot, contextRecord, reportedEvidence, mappingContext, mappingInput, reportedDestination, candidateDestination, queryAnchor, selectedOccurrence, inSelectionContext, justificationPath, pathStep, childReference, parentReference, citesPublication, refersToStudy, indicationStudyRecord, hasPopulationScope, subjectRecord, comparatorRecord, sharedInput, inspectedRecord, aboutRecord, observationContext, prov:wasDerivedFrom, hasTarget, hasDrug, hasDiseaseReference.

**Local datatype properties (39):** externalIdentifier, identifierAuthority, sourceLabel, sourceRecordIdentifier, sourceLocator, sourceAuthority, snapshotVersion, artifactDescription, observedAt, recordVersion, scopeText, evidenceSourceType, aggregateScore, scoreDefinition, filterSpecification, operationMethod, methodVersion, limitationText, trialPhaseText, trialStatusText, statusDate, expectedField, rationale, resultSummary, originRole, selectionMode, inclusionKind, mappingStatus, inspectionDepth, materialKind, accessOutcome, interpretationOutcome, missingnessReason, dependencyStatus, completenessStatus, reviewerType, sourceText, reviewerIdentifier, executionReference.

External references: `prov:Entity` as `owl:Class`, and `prov:wasDerivedFrom` as `owl:ObjectProperty`, using their existing PROV IRIs. No local duplicate or Record superclass. Thus the graph has 21 class declarations including external Entity, 28 object-property declarations including external wasDerivedFrom, and 39 datatype-property declarations; the approved **local** class count remains 20.

## Namespace, version and annotations

- Ontology IRI: `https://github.com/subramanyaprasad21/dementia-kg-ai/ontology`.
- `dkg`: ontology IRI followed by `#`; `dgkr`: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/` (declared prefix only; no record IDs minted).
- Version IRI: ontology IRI followed by `/0.1.0`; `owl:versionInfo`: `0.1.0`.
- Explicit prefixes: dkg, dgkr, rdf, rdfs, owl, xsd, prov.
- Every local term: declaration, English rdfs:label/comment and rdfs:isDefinedBy pointing to the ontology. Both external PROV references have labels/comments but no local ownership assertion.
- UTF-8 without BOM, LF, final newline; triples ordered by full subject/predicate/object lexical/datatype/language values. Prefixes do not affect graph identity.

The version is schema metadata, not a source release or implementation of record identity. G01 does not guarantee HTTP dereferencing or institutional namespace ownership.

## Verification environment and commands

Neither system Python nor the bundled Python had RDFLib; no existing RDF CLI/bundled Node parser was found. This dependency requirement was reported before installation. RDFLib 7.1.4 was installed in the isolated directory `/private/tmp/dementiagraph-m1-task006-rdflib`, outside the repository, with isodate 0.7.2 and pyparsing 3.3.3. No project dependency file or other infrastructure was created. Package downloads were tooling acquisition, not biomedical source acquisition.

Installation command used:

```sh
python3 -m pip install --target /private/tmp/dementiagraph-m1-task006-rdflib 'rdflib==7.1.4'
```

Run the following verification from the repository root with `PYTHONPATH=/private/tmp/dementiagraph-m1-task006-rdflib python3` and supply this block on standard input. The check runs in memory and writes no fixtures or test files. It compares against the approved document inventory and immutable baseline, rather than trusting ontology counts alone.

```python
import re, subprocess
from pathlib import Path
import rdflib
from rdflib import Graph, Namespace, URIRef, Literal, RDF, RDFS, OWL, BNode
from rdflib.compare import isomorphic
base = "https://github.com/subramanyaprasad21/dementia-kg-ai/ontology"
D = Namespace(base + "#")
P = Namespace("http://www.w3.org/ns/prov#")
r = Path("docs/m1_implementation_readiness.md").read_text()
classes = re.search(r"\*\*Local class declarations \(20\):\*\* (.+?)\.", r).group(1).split(", ")
objects = re.search(r"\*\*Object-property manifest:\*\* (.+?)\.", r).group(1).split(", ")
datas = re.search(r"\*\*Datatype-property manifest:\*\* (.+?)\.", r).group(1).split(", ")
expected = {OWL.Class: {D[x] for x in classes}, OWL.ObjectProperty: {D[x] for x in objects if ":" not in x}, OWL.DatatypeProperty: {D[x] for x in datas}}
assert [len(expected[t]) for t in expected] == [20, 27, 39]
local = set.union(*expected.values())
ontology = URIRef(base)
subjects = local | {ontology, P.Entity, P.wasDerivedFrom}
predicates = {RDF.type, RDFS.label, RDFS.comment, RDFS.isDefinedBy, OWL.versionIRI, OWL.versionInfo}
g = Graph().parse("ontology/dementiagraph-v.ttl", format="turtle")
def check(h):
    assert set(h.subjects()) == subjects
    assert set(h.predicates()) == predicates
    assert not any(isinstance(n, BNode) for t in h for n in t)
    for typ, terms in expected.items():
        assert {s for s in h.subjects(RDF.type, typ) if str(s).startswith(str(D))} == terms
    for s in subjects:
        wanted = OWL.Ontology if s == ontology else OWL.Class if s == P.Entity else OWL.ObjectProperty if s == P.wasDerivedFrom else next(t for t, terms in expected.items() if s in terms)
        assert set(h.objects(s, RDF.type)) == {wanted}
        for annotation in [RDFS.label, RDFS.comment]:
            values = list(h.objects(s, annotation))
            assert len(values) == 1 and isinstance(values[0], Literal)
            assert values[0].language == "en" and str(values[0]).strip()
    assert set(h.subject_objects(RDFS.isDefinedBy)) == {(s, ontology) for s in local}
    assert set(h.subject_objects(OWL.versionIRI)) == {(ontology, URIRef(base + "/0.1.0"))}
    assert set(h.subject_objects(OWL.versionInfo)) == {(ontology, Literal("0.1.0"))}
    assert set(h.subjects(RDF.type, OWL.Class)) == expected[OWL.Class] | {P.Entity}
    assert set(h.subjects(RDF.type, OWL.ObjectProperty)) == expected[OWL.ObjectProperty] | {P.wasDerivedFrom}
    assert set(h.subjects(RDF.type, OWL.DatatypeProperty)) == expected[OWL.DatatypeProperty]
    for triple in h:
        for n in triple:
            if isinstance(n, URIRef) and str(n).startswith(str(D)):
                assert n in local
    assert len(h) == 355
check(g)
for fmt in ["turtle", "nt"]:
    reloaded = Graph().parse(data=g.serialize(format=fmt), format=fmt)
    assert isomorphic(g, reloaded)
    check(reloaded)
# Controlled checker tests, in memory only; these are not biomedical fixtures.
mutations = [
    ("extra local property", lambda h: h.add((D.unauthorized, RDF.type, OWL.ObjectProperty))),
    ("forbidden domain axiom", lambda h: h.add((D.hasTarget, RDFS.domain, D.EvidenceOccurrence))),
    ("missing declaration", lambda h: h.remove((D.Target, RDF.type, OWL.Class))),
    ("missing annotation", lambda h: h.remove((D.Target, RDFS.comment, None))),
]
for name, mutate in mutations:
    h = Graph()
    for triple in g: h.add(triple)
    mutate(h)
    try: check(h)
    except AssertionError: pass
    else: raise AssertionError("Checker failed to reject " + name)
raw = Path("ontology/dementiagraph-v.ttl").read_bytes()
assert not raw.startswith(b"\xef\xbb\xbf") and b"\r" not in raw and raw.endswith(b"\n")
assert set(re.findall(r"^@prefix ([a-z]+):", raw.decode(), re.M)) == {"dkg", "dgkr", "rdf", "rdfs", "owl", "xsd", "prov"}
for path in subprocess.check_output(["git", "ls-tree", "-r", "--name-only", "09a89476603d1744d534e91504c13c2575badeb3"]).decode().splitlines():
    assert Path(path).read_bytes() == subprocess.check_output(["git", "show", "09a89476603d1744d534e91504c13c2575badeb3:" + path])
print("PASS: RDFLib", rdflib.__version__, "; 355 triples; 20/27/39 local declarations + 2 external PROV references")
print("PASS: Turtle parse; Turtle and N-Triples graph round-trips; annotations; exact inventory; namespace/version; declaration-only whitelist")
print("PASS: four negative checker controls; approved tracked files unchanged; prefix/encoding checks")
```

Additional commands: `git diff --check`, `git diff --cached --check`, `git status --short`. Because both files are untracked before review, whitespace is also checked directly on their contents. No stage/commit/push command is part of this task.

## Verification results

Results are recorded after executing the block above: Turtle parse PASS; Turtle and N-Triples graph-isomorphic round-trips PASS; exact declarations and namespace PASS; PROV references PASS; annotations/version metadata PASS; closed declaration/annotation predicate and typing checks PASS; 355 triples. All four deliberate in-memory corruptions were rejected. Approved tracked documents remain byte-identical to the baseline. Direct whitespace and both Git diff checks PASS.

The allowed predicate/type policy rejects imports, subclass/subproperty hierarchies, domain/range, equivalence, disjointness, restrictions, property chains, extra property characteristics, unexpected subjects and blank nodes. This is a structural schema check, not a reasoner result or proof about future application transformations. No OWL reasoner was selected or run.

## Encountered issues and interpretation

1. Missing RDF parser was resolved using the isolated verification dependency reported above; no project runtime stack was chosen.
2. Mechanics section 3.4a mentions `EvidenceOccurrence.mappingContext` as a deferred linkage, whereas the frozen readiness signature defines **MappingRecord → EvidenceOccurrence or contextual source information resource**. This implementation preserves the frozen signature in the mappingContext annotation. No domain/range or linkage is implemented. The incompatible mechanics wording must be reconciled before implementing receipt/fixture links; it does not block this declarations-only schema. The design files were not modified and no reverse property was introduced.

No manifest or namespace deviation was needed. Tests do not establish that the future receipt generator or every fixture is implementable without further review.

## Deferred R1–R14 acceptance obligations

The declaration/annotation contribution is present; the following executable responsibilities are **not completed**:

| Requirement | Deferred acceptance evidence |
| --- | --- |
| R1 | Validate association/occurrence roles and source aggregate versus project grouping membership; prevent causal upgrades. |
| R2 | Preserve raw versus normalized disease values and provenance in fixtures; test no equivalence interpretation. |
| R3 | Validate mapping context/ambiguity, correct mappingContext direction and unresolved candidates. |
| R4 | Execute membership/directness and complete/incomplete bounded path checks. |
| R5 | Test separation of selection inclusion from upstream normalization and explanation revision. |
| R6 | Execute provenance, source-version, identity receipt and collision checks; preserve actual audit origin. |
| R7 | Test publication/study/source traceability without citation-to-support upgrades. |
| R8 | Validate actual inspection depth, access, reviewer and material context. |
| R9 | Validate finite missingness tokens/reasons, relevance and non-duplication; prevent silent repair. |
| R10 | Test mechanism/indication separation and rejection of treatment/efficacy inference. |
| R11 | Test report population, source date, phase/status and indication boundaries. |
| R12 | Execute reproducible derived comparisons, scoped inputs and source-versus-project distinctions. |
| R13 | Test duplicate/shared/dependent evidence handling; review any independence claim against actual evidence. |
| R14 | Test supported completion, qualification and abstention against controlled question expectations. |

Q01–Q07 remain design questions. Their fixtures, provenance round-trips, positive/negative application cases, SHACL and identity execution require later authorization. This task neither completes the readiness section 16 checklist nor changes its obligations.

## Explicit limitations and review boundary

Declarations-only OWL uses open-world interpretation and imposes no cardinality, owner/range, enum membership, disjointness or inference rules. Annotations document policy but cannot enforce it. No biomedical data was acquired, historical release reproduced, domain expert adjudication performed, completed KG built, or graph advantage demonstrated. Historical availability, permissions and live projections remain deferred. No source fixtures, identifier generator, SHACL, retrieval, LLM, experiment, store, reasoner configuration or additional project infrastructure was created. Stop for owner review before any commit.
