# M1 Task 007 — audit-derived fixtures and identity verification

**Implemented for owner review. No staging, commit, push or live acquisition.**

Implementation baseline: `09d8c7c403a8495fd3c1bc4e0ce8de76165e5eab`. Actual fixture source: Git blob `docs/source_audit.md` at `229540ce7383d9b47a7f7688099522fed7777d44`. These are different roles: implementation baseline versus pinned audit edition.

## Scope, authority and changes

The [conceptual contract](m1_conceptual_model_contract.md), [readiness manifest](m1_implementation_readiness.md), [approved G01–G06 mechanics](m1_implementation_mechanics.md) and [Q01–Q07](competency_questions.md) govern this bounded implementation. The 20/28/39 ontology remains byte-identical to the approved Task 006 baseline.

Only the two approved documentation changes were made: the exact narrow mappingContext paragraph correction in mechanics §3.4a, and an appended resolution reference in the Task 006 implementation record. MappingRecord → EvidenceOccurrence/contextual source resource remains the direction. Its owned mappingContext assertion is hashed normally; it is not a deferred inverse link. Only the separately approved population attachment exception remains. No semantic alternative or reverse property was introduced.

Created exactly:

- `fixtures/m1/audit_fixture_spec.json`: reviewed finite transcription selections, record assertions, question slots and unavailable information.
- `fixtures/m1/audit_derived.ttl`: generated instance fixture bundle under existing terms, not a production KG.
- `fixtures/m1/identity_receipts.json`: canonical receipts, hashed payloads, exact passage metadata, null explanations and whole-bundle integrity digest.
- `fixtures/m1/execution_ledger.json`: actual initial local execution reference `m1-audit-fixtures/1`, scope and timestamp. No historical retrieval is impersonated.
- `tools/m1_fixture_identity.py`: the finite approved receipt and JCS string/null/array/object subset, SHA-256 and conflict registry.
- `tools/build_m1_audit_fixtures.py`: offline pinned-audit replay, finite structural checks and controlled request outcomes.
- `tests/test_m1_fixture_identity.py`: automated positive/negative structural and identity checks.
- This document.

No dependency, environment, configuration, package, SHACL or additional infrastructure file was added. Python standard library and the RDFLib 7.1.4 installation already available from Task 006 were used; no new package installation occurred.

## Provenance and representation boundary

There are **170 records and 1,130 triples**, using **48 exact selected passages from 12 pinned audit sections**. Whole-section bytes determine snapshot digests; line-span locators identify exact selected passages, whose text is preserved verbatim. Section projections can include historical discussion outside V1, but only the named Q01–Q07 passage selections are transcribed into source slices. No LBD record is introduced as an anchor or additional evidence example.

Every SourceSnapshot identifies `project-audit`, the actual full Git commit, section locator and content hash. Neither OT 26.06 nor Mondo 2026-09-01 is asserted as a newly acquired snapshot. Those labels survive only as historical audit attribution where present. This is reproduction of project audit transcription, not reproduction of upstream biomedical responses.

SourceSlice is an existing `prov:Entity` use, not a new local class. Citation links connect source slices to Publication referents, allowing historical inspection context to be navigated from mechanisms/evidence through their publication references. SourceSnapshot/SourceSlice provenance is inspectable without relying on an LLM's memory.

Seven present InspectionRecords describe automated extraction/structural inspection of the local audit. Their interpretationOutcome is `not-assessed` for biomedical meaning. They do not claim that the program read a publication body or independently repeated an old review. Historical abstract/full-text/metadata depth remains quoted, attributed audit content.

SelectionContexts represent present local selections of named audit observations, with explicit scope and incomplete upstream extent. They do not claim replay of the original API requests or regeneration of old totals. Each membership points to its occurrence and actual local context. Ordered hierarchy steps reproduce the explicitly documented chains only; no ontology import, closure or inferred biomedical equivalence is performed.

## Record inventory

| Type | Count |
| --- | ---: |
| SourceSnapshot | 12 |
| SourceSlice (`prov:Entity`, no local class) | 48 |
| DiseaseConceptReference | 25 |
| Target | 5 |
| Drug | 4 |
| Publication | 15 |
| Study | 2 |
| DiseaseTargetAssociation | 1 |
| EvidenceOccurrence | 8 |
| MappingRecord | 8 |
| SelectionContext | 4 |
| SelectionMembership | 8 |
| HierarchyStep | 5 |
| HierarchyPath | 2 |
| MechanismRecord | 5 |
| ClinicalIndicationRecord | 4 |
| StudyRecord | 2 |
| PopulationScope | 2 |
| DerivedStatement | 1 |
| InspectionRecord | 7 |
| MissingnessRecord | 2 |

The source aggregate remains distinct from individual occurrences. Its missing historical method/score definition is not invented, and no score is interpreted. The derived dependency statement concerns only the two selected clinical-precedence occurrences. Referent counts, occurrence counts and independent study counts are not interchangeable.

## Mandatory question slots and limits

The JSON specification records required record aliases, exact passages and unavailable information per question. These assertions are controlled transcriptions; automatic presence checks do not replace review of their scientific fidelity.

| Question | Represented slots | Explicit unavailable/qualified slots |
| --- | --- | --- |
| Q01 | PSEN1 and both anchors; all three full source evidence IDs; datasource/type context; PMIDs 33008897, 31555645, 22503161, 23028126; panel 265; original-field gaps and recorded historical review depths | Exact extraction spans, raw historical upstream artifacts and variant-level causal adjudication. Two field:mappingInput missingness observations use existing MappingRecords, not duplicate generic requirement nodes. |
| Q02 | Both GRIN targets and full clinical-precedence IDs; memantine; both gene-indexed mechanisms; shared NCT00594737; dated report; quoted join/query/source composition, original label/null ID, unreviewed publication locators | No separately captured memantine indication-row ID/detail; retain the audit account of the join, not an invented indication record. No trial-result review or independent genetic confirmation. |
| Q03 | Full MAPT/Pick occurrence; original OMIM:172700 and reported FTD assignment; panel 474; direct local membership; separate Pick MONDO context; PMID/depth limits | Exact upstream input edition/mapping algorithm and individually adjudicated panel-citation phenotype support are not available. |
| Q04 | Full APP/AD1 and MAPT/semantic-dementia IDs; direct/inclusive query descriptions; all five consecutive edges and two ordered paths; Q03 contrast | Original full API result sets are not archived. Counts 0→1/3→10 are quoted dated observations, not newly calculated evidence totals or complete result coverage. |
| Q05 | Separate OMIM:600274 source-scoped references, two reported destinations, panel/gene contexts, unresolved status and annotated xref account | Exact raw original label for the selected MAPT inclusive row is not printed in T3-H. Panel wording remains separately attributed, not substituted. No canonical OMIM interpretation, equivalence, mapping cause or repair established. |
| Q06 | FTD/MAPT aggregate; zagotenemab mechanism and AD/tauopathy indication descriptions; PMID 33303932 metadata limitation; lecanemab/APP AD control and PMID 25031633 molecular qualification | Tauopathy canonical ID and detailed indication-row IDs absent. No archived full indication response or inspected product-specific label; no new exhaustive absence/current-approval claim. |
| Q07 | Gosuranemab/MAPT mechanism; full FTD indication ID; NCT03658135; dated population/design/status description; PMID 30581980 and its distinct healthy-participant context | No independently identified Study referent for the mechanism publication; do not fabricate one. Combined four-cohort wording retained without invented cohort mappings. No clinical benefit adjudication. |

Missingness does not multiply merely because an inaccessible publication affects several interpretations. Existing source slices and scoped limitation/inspection records carry those limits. Only two additional MissingnessRecords are needed for original disease inputs absent from the selected PSEN1 mappings.

## G01–G06 execution

- **G01:** exact approved namespace and record kind/digest paths; no schema additions.
- **G02:** exact key tables read from the approved mechanics; strings/null/ordered arrays/unordered sets are distinguished. The canonicalizer supports only the approved numeric-free receipt/payload subset, not arbitrary API JSON. UTF-16 object-key ordering and unchanged Unicode strings are tested. Full 64-character SHA-256 digests are used. Source records precede mappings; source/encounter identity is separate. StudyRecord population attachments remain outside its record content hash and inside the bundle digest. Membership identity hashes only occurrence/context; later explanations are separate derived/review records, not new retrievals. Null reasons are explicit; uncertain source method/version values are not invented.
- **G03:** all twelve enum catalogues are loaded; lexical values, applicable owners, single state and direct/descendant contradictions are checked for this bundle.
- **G04:** all 76 field/requirement tokens are admitted, with sparse creation, field-presence checks and duplicate/recursive missingness rejection. Not every possible source-specific applicability judgment is automated.
- **G05:** no network acquisition code; the builder uses Git's local pinned blob. Live-source budgets are not consumed, executed or tested as acquisition machinery.
- **G06:** identity and structural violations raise explicit failures. Honest source limits remain attributed and qualification-bearing. The controlled outcome function accepts a finite request vocabulary and is not a free-text answer system or biomedical judge.

`build_m1_audit_fixtures.py` is a replay tool for this archived execution, not a generic new-run allocator. It never appends a new execution automatically. New actual selection/review operations require a separately recorded execution and reviewed artifact version. Shared-source assertions do not become independent confirmation through repeated replay or distinct record IDs.

## Verification commands

Run from repository root, using the Task 006 verification dependency location if still available:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/private/tmp/dementiagraph-m1-task006-rdflib python3 tools/build_m1_audit_fixtures.py
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/private/tmp/dementiagraph-m1-task006-rdflib python3 -m unittest discover -s tests -p test_m1_fixture_identity.py -v
git diff --check
git diff --cached --check
git status --short --untracked-files=all
```

The first command writes only the two generated, approved fixture artifacts, using the existing spec/ledger. Tests build in memory and write no artifacts. `PYTHONDONTWRITEBYTECODE=1` avoids unapproved cache files. If RDFLib is unavailable in a later environment, report that requirement before installing it; no project dependency installation is implicit.

## Results and issues encountered

**24 automated tests pass.** They verify exact pinned passage bytes/locators, all full evidence IDs, referent identifiers, required slot presence/unavailability, canonical golden digest, Unicode and key/set ordering, malformed receipt rejection, changed source/payload versions, deterministic replay (including reversed input record order), collision/conflicting-payload rejection, correct mapping direction, separate encounters, stable membership under explanation revision, finite catalogues, sparse missingness, positive and deliberately broken paths, citation-depth navigation, shared trial dependency, prohibited claim policy and unchanged ontology. Turtle and N-Triples graph round-trips pass with literal lexical preservation enabled.

Two implementation issues were found and resolved by tests:

1. RDFLib's automatic namespace bindings could change serialization aliases after a serializer ran. The deterministic bundle writer now uses full IRIs, with the required explicit prefix declarations retained. This affects presentation only; IDs are receipt-derived.
2. RDFLib's default parsing normalizes dateTime `Z` to `+00:00`, changing the RDF literal spelling. Round-trip tests explicitly disable `rdflib.NORMALIZE_LITERALS` during parsing so archived lexical values and identity payloads are preserved. This parser setting is necessary for exact lexical graph preservation; semantic date equality alone is insufficient for receipt fidelity.

The mappingContext correction is implemented and tested. No new manifest contradiction required a schema change. Source incompleteness remains explicit, particularly the unavailable upstream artifacts and IDs listed above. The implementation is bounded: it does not certify every possible G06 rule against arbitrary external data or exercise a live acquisition workflow.

## R1–R14 obligations exercised

| Requirement | Evidence in this task | Still outside automated completion |
| --- | --- | --- |
| R1 | Separate aggregate and eight occurrences; correct participant signatures | Source scoring validity, causal strength, full aggregate reconstruction |
| R2 | Original and normalized reference separation, preserved raw identifiers and absent-input records | Canonical biomedical identity judgments |
| R3 | Mapping direction, distinct contextual OMIM assignments, ambiguity outcome | Mapping validity, source algorithm reconstruction |
| R4 | Membership/selection distinction, two complete ordered chains; missing-step/cycle/wrong-endpoint controls | Broader propagation or unobserved source completeness |
| R5 | Local selection versus attributed normalization; explanation revision preserves membership | Original upstream execution reproduction |
| R6 | Snapshot/section/passage hashes, receipts, replay, versions and conflict tests | Live artifact provenance/permissions, all possible source routes |
| R7 | Full record IDs; publication/study separation and navigable quoted review provenance | Primary body access and claim-support adjudication |
| R8 | Present automated inspection distinguished from quoted historical depth | Independent clinical or expert review |
| R9 | 76-token validation, two relevant missing mapping inputs, no repeated access-gap nodes | All possible source-specific missingness judgments |
| R10 | Separate mechanisms and indications; controlled treatment/approval upgrades rejected | Biomedical drug mechanism or efficacy assessment |
| R11 | Distinct reports/populations; dated status; completion/failure upgrades rejected | Trial results, detailed cohort mappings, benefit interpretation |
| R12 | Attributable derived shared-study result, input/method/execution metadata and replay | General comparison/query engine and all future grouping variants |
| R13 | Shared trial found by graph intersection; removed-link control unresolved; independent-confirmation upgrade rejected | General evidence independence adjudication |
| R14 | Positive source-scoped results plus qualified/unsupported outcomes | Held-out answer evaluation, natural-language claim verification |

The controlled forbidden-claim requests are policy tests against known disallowed interpretations, not learned scientific judgments. Positive identity/mapping/path/shared-source checks prevent a blanket abstention implementation from satisfying the suite. These exposed fixtures do not establish graph advantage, experimental efficacy or novelty.

## Remaining review boundary

No SHACL, live acquisition, production ingestion, retrieval, LLM integration, database, reasoner configuration or experiment was implemented. Historical source availability, rights, live projections and independent expert adjudication remain deferred. No original study or clinical truth is established merely by passing tests. Owner review is required before committing this Task 007 work.
