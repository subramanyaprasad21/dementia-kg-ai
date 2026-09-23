# M1 Task 008 — Structural validation with SHACL

## Scope and authority

Implementation pending owner review; no checkpoint commit is created by this task.
Baseline: `855c16191bb49f7bb885716ee4c90b18d0db66f6`.

This implements bounded structural checks over the Task 006 declarations-only ontology vocabulary and Task 007 audit-derived fixtures. The conceptual contract, implementation readiness sections 3–6 and 12, approved G01–G06 mechanics, and V01–V27 catalogue govern the constraints. The approved 20/28/39 manifest, Q01–Q07 and R1–R14 remain unchanged.

Exactly four new files constitute this task:

- `validation/m1_shapes.ttl`: local SHACL Core constraints and warning diagnostics.
- `tools/validate_m1_fixtures.py`: local graph loading, strict validator configuration and separate raw/project reports.
- `tests/test_m1_shacl.py`: controlled structural mutations and preservation checks.
- `docs/m1_shacl_validation.md`: this implementation and verification record.

The actual fixture source remains the pinned project audit at `229540ce7383d9b47a7f7688099522fed7777d44`, not independently reproduced upstream evidence. No source acquisition occurred. Synthetic controls are in-memory mutations of those fixtures, never new biomedical observations or valid replacement identity receipts.

## Execution environment

Python 3.12.7. Dependency installation was reported before execution and isolated outside the repository at `/private/tmp/dementiagraph-m1-task008-pyshacl`. No project dependency file was added or changed.

| Package | Exact version |
| --- | --- |
| pyshacl | 0.30.1 |
| rdflib | 7.1.4 |
| owlrl | 7.1.4 |
| packaging | 26.3 |
| prettytable | 3.18.0 |
| pyparsing | 3.3.3 |
| html5rdf | 1.2.1 |
| wcwidth | 0.8.4 |

The installed `owlrl` is a pySHACL dependency, not an enabled inference engine. Recreating this environment requires these exact package versions; an ephemeral `/private/tmp` environment is not a permanent deployment or dependency lockfile.

Validator arguments are fixed:

```python
inference='none'
advanced=False
js=False
iterate_rules=False
meta_shacl=True
do_owl_imports=False
inplace=False
abort_on_first=False
allow_infos=False
allow_warnings=False
ont_graph=None
```

Both inputs are local RDFLib graphs. The runner clones data and shapes before passing them to pySHACL and checks that caller inputs remain unchanged. The ontology is not mixed into the data to supply inferred participant types. No endpoint, imports, SPARQL constraints, SHACL rules, JavaScript or second validation toolchain is used. Tests block socket connection attempts.

The shapes graph uses a separate `/validation/m1#` namespace. Shapes are validation resources, not additions to the ontology manifest. Explicit type assertions supply participant-role checks. These shapes are scoped application constraints, not global OWL domain/range or disjointness axioms.

## Implemented rule coverage and boundaries

| Catalogue rule | Task 008 coverage | Remaining responsibility |
| --- | --- | --- |
| V01–V02 | Turtle parsing; preservation of committed schema and inventory checked by regressions | Parser/schema inventory and prohibited-axiom checks remain outside SHACL; arbitrary future vocabulary drift is not inferred from passing shapes |
| V03 | Mandatory typed participants, owner signatures for 28 object fields and 39 literal fields, cardinality, literal types, mapping direction, source/grouping roles, mechanism/indication record separation | Supplied source fields and record truth require ingestion/provenance checks |
| V04 | Exact 12 enum catalogues; 76 missingness tokens; input-only mapping, direct-only selection, inspection access/depth and other explicit state checks | Truth of a valid state and arbitrary prose contradictions require review/application evaluation |
| V05–V06 | Existing Task 007 identity/pinned-provenance regression retained | Hashes, replay, immutable identity and fabricated source/reviewer information are not established by SHACL |
| V07 | Warning for explicit source-omission records | Whether omission is truthful or alternate tracing adequate requires provenance review |
| V08 | Structural input links, step locator or scoped locator-gap representation | These links do not establish actual source support or traceability of every claim |
| V09–V10 | Warning for partial/unknown path; complete path requires explicit typed steps and mandatory endpoints | Connectedness, cycles, declared endpoints and version compatibility remain application/identity checks; not a general path validator |
| V11–V12 | Partial/unknown selection warning; mandatory run metadata remains required | Pagination completeness, list-wide absence and exhaustive answer claims remain application judgments |
| V13 | Unresolved mapping warning; observed destination not replaced; review context required for reviewed-with-limits | Mapping validity/equivalence and interpretation of validity-unreviewed require review; no equivalence inferred |
| V14–V15 | Inaccessible/not-attempted warning; incompatible positive depth rejected; new inspection execution/reviewer metadata required | Historical attribution, actual inspection depth and claim support remain qualified review matters |
| V16–V18 | Dependency participants/shared-input metadata and clinical role separation checked structurally | No proof of independence, dependence, efficacy, approval or clinical correctness; Task 007 controlled claim tests remain separate |
| V19 | Token-owner applicability, contextual basis and rationale; missingness cannot waive mandatory participants/metadata | Actual gap relevance, reason truth and non-duplication across interpretations require scoped review |
| V20 | Empty candidate lists and unused optional score remain permitted; replay regression unchanged | No extra MissingnessRecord or SHACL Info result is generated for legitimate absence |
| V21–V22 | Trial phase/status/date owner and datatype checks; undated reported status warning | Actual source precision, current status and interpretation remain review obligations |
| V23 | At most one decimal score; source origin and definition or explicit limitation/gap; undefined-score warning | Causal/probabilistic interpretation cannot be licensed by structural conformance |
| V24 | Required computation method/version, execution, input lineage, scope, completeness and result; dependency basis | Reproducibility of the actual computation and truthful inputs remain separate |
| V25–V27 | No acquisition; committed audit/receipt/profile regression retained | Operational acquisition ceilings, permissions, historical availability and release-profile acceptance remain outside these shapes |

Information-resource alternatives follow the approved local record types and `prov:Entity` source slices; they do not create an InformationResource ontology class. The nine composite missingness tokens have explicit permitted-owner checks, as do all 67 ordinary field tokens. Broad source-description alternatives require actual scoped provenance review: an allowed RDF type is not proof of appropriate source context.

Precedence is preserved: V03 and V24 mandatory structure is never waived by a V07/V09/V11/V14/V22 warning, qualified historical language or a MissingnessRecord. Lexical token membership is V04; token-owner applicability is V19. The raw report may contain multiple constraint results for one malformed record; result counts are diagnostics, not counts of independent scientific defects. Findings retain their source shape and severity rather than being recast as biomedical evidence.

## Baseline and controls

The committed baseline contains exactly **170 records, 1,130 RDF triples, 48 pinned passages and 12 audit-section snapshots**. Its dependency DerivedStatement lacks `completenessStatus`. The fixture is preserved byte-for-byte.

| Input | Violations | Warnings | Raw `sh:conforms` | Project structural acceptance |
| --- | --- | --- | --- | --- |
| Committed Task 007 baseline | 1 | 8 | false | blocked |
| In-memory completeness control | 0 | 8 | false | qualified-structural-pass |
| Nonempty, warning-free synthetic target control | 0 | 0 | true | structural-pass |

The one baseline violation is `DerivedStatement_completenessStatus_required` at the existing `dependency` record, path `dkg:completenessStatus`. The eight warnings are four `PartialSelection`, two `UnresolvedMapping` and two `RecordedSourceOmission`. No other baseline finding is expected or suppressed.

The completeness control adds exactly one typed string, `complete-for-declared-scope`, to the existing dependency node in memory for shape testing. This creates 1,131 test triples. It does **not** repair the persisted fixture, create an identity-valid revised record, establish source completeness, or warrant reusing its original receipt for the changed payload. Passing this control establishes only that the required field resolves this structural violation.

Warnings remain visible in strict raw conformance. Project acceptance reports `blocked` whenever any Violation exists; warnings alone give `qualified-structural-pass`, requiring the corresponding qualifications. This is not unrestricted answer acceptance. No baseline exception silently converts its violation into a pass. The CLI exits 1 for the expected blocked baseline; the test suite succeeds by asserting that exact finding.

## Controlled tests

The new suite tests the baseline and synthetic controls, missing membership/selection/computation fields, reversed mappingContext, wrong participant and lost owner types, permitted contextual source resources, exact catalogues and lexical errors, missingness owner/rationale, direct/descendant conflicts, access/depth conflicts, partial versus complete empty paths, trial-status ownership and missing dates, missingness failing to waive an endpoint, input-only mapping, shared-input requirements, Meta-SHACL rejection of malformed shapes, fixed local configuration, RDF round-trip and input immutability, and byte-for-byte baseline preservation. Additional source-aggregate/grouping and mechanism/indication separation cases test approved role boundaries.

Mutations never assert new biological facts. Removing an optional field or using an unresolved state is not treated as false biomedical information. Missing mandatory local structure still fails even in a graph containing warnings and valid missingness records. Automatic structural outcomes are separate from Task 007 controlled claim decisions and unresolved manual biomedical/provenance judgments.

## Verification commands

Run from the repository root, using the isolated dependency directory:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/private/tmp/dementiagraph-m1-task008-pyshacl python3 -m unittest discover -s tests -p test_m1_fixture_identity.py -v
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/private/tmp/dementiagraph-m1-task008-pyshacl python3 -m unittest discover -s tests -p test_m1_shacl.py -v
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/private/tmp/dementiagraph-m1-task008-pyshacl python3 tools/validate_m1_fixtures.py
git diff --check
git diff --cached --check
git status --short
```

The first two commands must exit 0. The baseline CLI must exit 1 with exactly the findings above. Each validation enables Meta-SHACL. The test suite includes a malformed shape that must raise an error, rather than silently skipping Meta-SHACL. Untracked-file whitespace and syntax are inspected separately because `git diff --check` does not inspect untracked contents.

## Results and encountered issues

Verified on 2026-09-23:

- Complete combined suite: **55 tests passed** in 182.291 seconds (24 unchanged Task 007 tests plus 31 Task 008 tests).
- Turtle parsing and Meta-SHACL passed for the implemented shapes. The deliberately malformed shape was rejected as expected.
- Standalone baseline CLI exited 1 as expected: exactly one completeness violation and eight warnings; no additional unexpected baseline findings.
- Synthetic completeness control: zero violations and the same eight warnings. Warning-free nonempty control: raw conformance true.
- Controlled negative mutations were rejected; qualified partial/uncertain controls were preserved. Tests include score qualification, unresolved inclusion and inspection scope.
- RDF fixture round-trip and validator input immutability passed. Every committed baseline file was compared byte-for-byte, including the ontology, fixtures, receipts, identity implementation and approved documents.
- Inventory unchanged: 170 records / 1,130 triples / 48 passages / 12 audit sections. Ontology unchanged: 20 local classes / 27 local object properties plus external `prov:wasDerivedFrom` / 39 datatype properties.
- All 86 local vocabulary references in the shapes are declared in the existing ontology; no ontology classes/properties are declared by the shapes.
- `git diff --check` and `git diff --cached --check` passed. Explicit whitespace and Python syntax checks on the four untracked files passed. No tracked or staged changes; only the four authorized new files are present.

The combined verification command was:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/private/tmp/dementiagraph-m1-task008-pyshacl python3 -m unittest discover -s tests -v
```

Implementation issues were corrected without changing committed inputs: pySHACL adds working shapes metadata, so private graph copies protect caller inputs; SHACL list/state literals use explicit `xsd:string` to match the frozen fixtures under lexical-preserving RDFLib parsing. Repeated information-resource alternatives share named node shapes to keep the constraints maintainable. The undefined-score property constraint has explicit Warning severity, because a parent shape severity does not automatically set a nested property constraint severity. An early test expected the wrong trial-status diagnostic name; that assertion was corrected after confirming the invalid owner was rejected. These are validator/test implementation corrections, not ontology changes.

## Deferred acceptance obligations

Task 008 supplies structural evidence toward R1–R14; it does not complete all obligations. R1–R5 participant, mapping and selection roles; R6–R8 provenance/inspection slots; R9 missingness; R10–R11 clinical record boundaries; and R12–R14 computation/dependency/qualification metadata receive bounded checks. Exact receipts, source passage fidelity, replay, chain topology and controlled claim acceptance remain in the separate Task 007 suite where covered. General ingestion, full path/source compatibility, true evidence independence, actual source support, biomedical adjudication, answer-level evaluation and research experiments remain deferred.

No SHACL outcome proves biomedical truth, source completeness, evidence independence or clinical correctness. No graph-advantage or novelty result follows. An empty or incomplete graph may satisfy targeted shapes vacuously; separate fixture inventory/Q-slot and provenance regressions are therefore mandatory. The fixture's known completeness defect remains an open acceptance issue for any future persisted computation revision, requiring the approved immutable-identity mechanics rather than an in-place repair.

False positives remain possible when applying this bounded local profile to a different source representation without an approved adapter. False negatives include well-formed but false assertions, irrelevant or misleading provenance, unencoded prose contradictions, and absent records outside shape targets. Review and the separate inventory/identity/application checks remain necessary; these limitations are not waived by a structural pass.
