# M1.6 — Bounded semantic acceptance and M1 closure preparation

Status: **M1.6 APPROVED / M1 CLOSED within the bounded audit-derived scope**, by explicit owner approval on 2026-09-24. This does not authorize M2 implementation.
Baseline: `7ce1c4c7011ce8911e2b54243306a94ac298ee18`.

## Scope and authority

Only three files are added:

- `tools/m1_semantic_acceptance.py`
- `tests/test_m1_semantic_acceptance.py`
- `docs/m1_semantic_acceptance.md`

The frozen Q01–Q07, R1–R14, conceptual contract, implementation-readiness sections 3/7/12/14/16, approved G01–G06 and Task 006–008/M1.4 records govern this work. The declarations-only ontology and 20/28/39 manifest are unchanged. No existing implementation, fixture, identity receipt, execution ledger, shape, reasoning test or approved design document is edited. No new source, ontology term, dataset, dependency, LLM, production retrieval framework or experiment is introduced.

The evidence remains the pinned project audit at `229540ce7383d9b47a7f7688099522fed7777d44`. Reproducibility means reproducible handling of that audit-derived bundle, not reproduction of historical upstream sources. All synthetic controls are disposable in-memory operations. Original inventory remains 170 records / 1,130 RDF triples / 48 passages / 12 audit-section snapshots.

## Query implementation

Functions navigate RDFLib graph assertions. They do not read identity receipts, fixture specifications, alias dictionaries or hidden answer tables. Tests use receipt aliases only to select input IRIs, and use explicit expected identifiers/sets as independent oracles. Receipt utilities are used only to generate/verify synthetic operation identities. No reasoning closure is substituted for source assertions.

| Function | Capability and boundary |
| --- | --- |
| `mappings`, `reference` | Incoming mappingContext lookup; original, reported and candidate references, raw identifiers/labels, mapping status, context IRIs and relevant missingness. No merge or canonical repair. |
| `source`, `snapshot` | Require pinned project-audit edition/provider/projection and a record locator belonging to its declared section. Different legitimate sections remain distinct and joinable. |
| `hierarchy` | Reconstruct a unique connected nonbranching directed chain from unordered RDF step links. Reject cycles, disconnected edges and missing source context; return actual endpoints. No receipt-stored ordering is used. |
| `membership_explanation` | Connect normalized disease to chain start and query anchor to chain end for descendant explanations. A shorter connected chain is not enough. Exact-anchor membership does not become propagation because other hierarchy records exist. |
| `selection`, `intersection` | Return context-scoped memberships, deduplicated occurrences/targets, contributing occurrence pairs, source context and qualifications. Reject direct/inclusive mixing. |
| `bounded_extent` | Compare enumerated membership with an explicitly supplied finite local input set. Does not infer upstream extent from a status literal. |
| `constituents` | On project-grouping associations only, recover directly linked EvidenceOccurrence derivation inputs; compare against the context's selected occurrences for the grouping target. Exclude ancillary contextRecord links. |
| `evidence`, `publication_contexts` | Trace source IDs, source types, mappings/gaps, citations, attributed audit excerpts and applicable technical review context. A citation is not adjudicated support. |
| `shared_studies` | Compute the actual intersection of study-reference links for two given occurrences; absence of shared links produces unresolved status, not independence. |
| `clinical` | Separately return mechanism/target, indications, linked study reports, original populations, dated status and attributed publication context. |
| `accept_claim` | Finite structured acceptance of supported shared-target, shared-study, reported-indication and dated-population statements. False means this claim is not licensed by the supplied bounded result, not that its biomedical proposition is false. |

The functions assume the approved fixture vocabulary and are exercised alongside parser, identity and SHACL regressions. They are not a replacement ingestion validator or a generic answer engine. They do not establish source truth by checking self-reported metadata.

### Source compatibility and raw identifiers

SourceSnapshot identifies an audit section, not an upstream ontology release. General source checks require the pinned audit edition and section-local locator. A hierarchy path, its steps and endpoint reference descriptions must agree on the declared audited chain section; membership joins can legitimately reference anchors and normalized records from other sections of the same audit. No rule declares all differing snapshot IRIs incompatible or all same-edition biomedical sources compatible.

Inclusive records contain raw `MONDO_0007088` and `MONDO_0010857`, whereas path references contain `MONDO:0007088` and `MONDO:0010857`. `comparison_key` compares only MONDO authority plus exactly seven digits for this bounded navigation join. It preserves raw fields and resource IRIs and creates no sameAs, normalized replacement record or generalized identity resolution. The explanation reports this join basis. There is no global OMIM normalization or arbitrary identifier resemblance rule.

The tauopathy indication is **label-only** in the frozen fixture. Its identifier remains absent and its label remains `tauopathy`. An initial test incorrectly expected an identifier and was corrected after inspecting the actual assertions. Likewise initial literal comparisons incorrectly expected colon spellings in inclusive records. These were implementation/test assumptions, not defects repaired in the source fixture.

## Q01–Q07 results and evidence-sensitive controls

All statements below are about the pinned local bundle. Test numbers refer to `SemanticAcceptance.test_01` through `test_18` in the new test file; full descriptive method names make each case identifiable.

| Question | Verified useful positive result | Mutation / qualification | New tests |
| --- | --- | --- | --- |
| Q01 | PSEN1 AD/FTD Europe PMC occurrences retain full record IDs, citations, available audit excerpts, normalized references and original-input gaps. AD ID is `1261ad02e3d662cd23a476af47159a1501d01889`. | Removing a citation removes it from the answer; removing source locator blocks the affected evidence trace. Original fields remain absent with scoped source-omission reasons. No causal ranking or extraction-error finding. | 03; existing passage/ID/review regressions |
| Q02 | GRIN1/GRIN3B share the existing `study-mem` reference (`NCT00594737` referent). A finite two-input comparison is reproducible. | Removing one study link changes result to unresolved and withdraws the shared-study claim. Shared source does not become independent genetic confirmation. | 11, 14–15 |
| Q03 | Reverse lookup from `e-pick` returns original `OMIM:172700`, label Pick disease, and reported destination `MONDO:0017276`. Membership remains exact-anchor with no propagation explanation. | Removing mappingContext removes that mapping answer; no reverse property or substitute normalized original is invented. | 01, 04 |
| Q04 | RDF-only chains recover AD `MONDO:0007088` → `MONDO:0004975` (3 steps) and FTD `MONDO:0010857` → `MONDO:0017276` (2 steps). Membership links and modes remain separate from normalization. | Missing step, branch, cycle, wrong end, shortened chain, unrelated snapshot or changed audit edition blocks a complete explanation. Reordered serialization preserves answers. | 04–07 |
| Q05 | Two record-local `OMIM:600274` references remain distinct. Destinations retain raw `MONDO:0017276` and `MONDO_0010857`; both mappings remain unresolved. | Removing a destination changes the result rather than filling it; multiple incoming mapping records are returned separately. No canonical repair or source-error claim. | 02 |
| Q06 | Zagotenemab has a MAPT mechanism and separate AD and label-only tauopathy indications. Lecanemab provides the separate APP/AD positive control. Publication 33303932's METADATA ONLY limitation remains attributed text. | Removing AD indication attachment removes that reported-indication answer while preserving mechanism. No exact FTD indication is returned from this finite set; no global absence, efficacy or approval claim follows. Removing paper-context linkage removes that review context. | 12, 18 |
| Q07 | Gosuranemab FTD indication links to `study-gos`, population wording containing four cohorts, TERMINATED status and source date 2019-12-19. Healthy-participant mechanism-study context remains separate. | Removing population or date withdraws the dated-population statement but preserves the separately supported platform indication. Phase/status do not establish efficacy or treatment outcome. | 13, 18 |

These tests do not recompute historical 0→1/3→10 upstream coverage counts, review original paper bodies or create biomedical ground truth. Historical observations remain attributed audit material.

### Selection and intersection expectations

| Context | Exact occurrence aliases recovered | State |
| --- | --- | --- |
| select-ad | e-psen-ad | partial |
| select-ftd | e-psen-ftd, e-psen-ge, e-pick, e-grin1, e-grin3b | partial |
| select-ad-inclusive | e-app-inclusive | partial |
| select-ftd-inclusive | e-mapt-inclusive | partial |

Direct AD targets: PSEN1 (`ENSG00000080815`). Direct FTD targets: PSEN1, MAPT (`ENSG00000186868`), GRIN1 (`ENSG00000176884`) and GRIN3B (`ENSG00000116032`). Their local selected-target intersection is PSEN1. Two FTD PSEN1 occurrences contribute to one target; they do not inflate target counts or prove independence. Removing AD PSEN1 membership changes the intersection to empty and withdraws the sampled-shared-target statement. This is not an exhaustive AD/FTD association comparison.

Test 09 demonstrates that a finite declared local set can be completely enumerated while its original SelectionContext remains partial for upstream scope. Changing completenessStatus alone never establishes upstream completeness; a missing declared member fails the finite-set check. Tests 10/16 use a labelled synthetic PSEN1 project grouping over the two FTD PSEN1 occurrences. The original source aggregate is rejected as a project grouping; missing/extra constituents fail, and an ancillary context link does not count as a constituent.

### Unsupported conclusions

Fixed prohibitions remain explicit policy boundaries for causality, independent genetic confirmation, efficacy, phase-success, termination-failure, global absence and mapping equivalence. They are not counted as evidence-sensitive achievements by themselves. Positive structured results and their withdrawal under actual graph mutations provide the nontrivial acceptance evidence. No model examines arbitrary prose or adjudicates biomedical truth. Unrecognized claim requests fail closed as outside this finite contract.

## Completeness defect disposition

The owner's approved disposition is implemented without editing the historical record:

`https://github.com/subramanyaprasad21/dementia-kg-ai/id/DerivedStatement/ccef4969cf1d11102c765c34e9bb65756f85d0122798cb31d796d77a1b77867a`

Its original receipt/payload remain immutable, and it remains the expected structural negative fixture. It is not accepted as a complete persisted computation. Its underlying evidence links remain inspectable.

`comparison_control` independently recomputes the shared-study intersection from the two selected occurrence nodes. It uses the existing m1-id-1 receipt/payload code, explicit method/version, both source inputs, selection context, scope, rationale, result and `complete-for-declared-scope`. Completeness means the complete calculation over those two named local inputs, not complete source evidence. It does not derive its answer from the historical resultSummary or receipt.

The deterministic new in-memory IRI is:

`https://github.com/subramanyaprasad21/dementia-kg-ai/id/DerivedStatement/fd956b20cf41227fd68b7b985b4a577ca3589f0eac320a820de9fcf8eac59b2b`

Content revision: `7fb54972e192ec83149842605f1e993c55a6894da13f1d6d8f02990c67173599`.

It has 14 owned payload assertions plus its class assertion. Adding it produces an in-memory 171-record / 1,145-triple graph. Replay preserves its receipt and IRI; these differ from the historical computation. Provenance points directly to the two existing occurrences; sharedInput identifies their actual common study. It is not falsely derived from the old conclusion.

`m1-semantic-controls/1` names the deterministic synthetic control scenario (comparison and grouping), not a new recorded historical execution. Repeated tests replay that scenario; no live retrieval or persistent execution ledger entry is claimed. It must not be reused to describe a future genuinely distinct persisted operation. Any future persisted correction requires separately authorized artifact scope and actual execution metadata under G02/G05.

| Validation input/view | Violations | Warnings | Raw SHACL conformance | Project structural acceptance |
| --- | ---: | ---: | --- | --- |
| Original historical bundle | 1 | 8 | false | blocked |
| Original plus new computation | 1, on original record only | 8 | false | blocked as a whole graph |
| Explicit acceptance view: new computation, historical negative subject excluded in memory | 0 | 8 | false | qualified-structural-pass |
| Original plus synthetic grouping | 1, on original record only | 8 | false | blocked as a whole graph |

The acceptance view is not a repaired persisted fixture or suppressed baseline finding. The original is always separately validated and its failure asserted. The eight warnings remain four partial selections, two unresolved mappings and two source omissions. Task 008's field-only synthetic control remains separately tested and unchanged. No new MissingnessRecord is used to excuse the historical defect.

## R1–R14 acceptance reconciliation

**Status vocabulary:** bounded PASS means the stated capability is demonstrated for this finite audit-derived M1 scope by concrete outputs and controlled cases. It does not complete later ingestion, source validation or experimental responsibilities. Automated evidence includes ordinary code/identity checks, SHACL and bounded OWL diagnostics. Synthetic controls demonstrate representability/behavior, not biomedical observations. The owner approved this bounded reconciliation and milestone closure on 2026-09-24; no independent biomedical adjudication is claimed.

| Requirement | Concrete evidence and test/result | Bounded M1 classification | Manual or deferred responsibility |
| --- | --- | --- | --- |
| R1 Association vs evidence | Existing distinct types/participants; tests 10/16 recover exactly two synthetic grouping inputs, exclude context-only evidence and reject source aggregate as grouping | PASS, grouping demonstrated by synthetic control | Real aggregate reconstruction/scoring and production ingestion |
| R2 Original vs normalized | Test 01 recovers Pick original/mapped values; 03 preserves missing originals; 02 retains distinct OMIM contexts and raw spelling | PASS | Authoritative disease identity/clinical equivalence judgments |
| R3 Context and ambiguity | Test 02 returns both unresolved assignments, preserves context IRIs and responds to destination removal/multiple mappings | PASS | Upstream mapping algorithm/version reconstruction; canonical repair remains unapproved |
| R4 Direct vs descendant | Tests 04–07 derive unordered RDF chains and distinguish exact/inclusive membership; invalid topology/endpoints/source context rejected | PASS for named paths | Broader hierarchy closure and source-version compatibility beyond this audit |
| R5 Selection vs normalization | Test 04 keeps direct Pick membership free of propagation explanation; inclusive explanations connect normalized references to separately scoped anchors | PASS | Historical upstream query execution reproduction |
| R6 Claim/association provenance | Existing 48-passage/hash/receipt regressions; tests 03/06/12/13/18 retain source context; 14–15 preserve direct computation lineage and new identity | PASS with historical negative result explicitly excluded from completed computation acceptance | Live source artifacts, permissions and truth of source attribution |
| R7 Publication/study/locator | Existing full IDs and passage checks; 03/11/18 expose citations, common study, locators and attributed paper context | PASS within available audit | Primary-body access and claim-support adjudication |
| R8 Inspection depth | Existing explicit automated-check/not-assessed and access-depth constraints; test 18 preserves METADATA ONLY and healthy-participant context, withdraws absent paper context | PASS as representation/qualification | Actual historical review fidelity and independent domain-expert review |
| R9 Missing information | Existing 76-token and nonduplication tests; 03 preserves source-omission gaps; 09 separates finite scope from upstream completeness | PASS | Future source-specific gap truth/relevance and inaccessible content |
| R10 Mechanism vs indication | Test 12 preserves MAPT mechanism when indication attachment is removed; distinct AD/APP positive control and structural/OWL separation retained | PASS | Molecular mechanism, drug efficacy, regulatory assessment |
| R11 Indication/trial/population/status | Test 13 yields dated four-cohort report; removing population/date withdraws only that stronger statement; test 18 keeps healthy-participant source context separate | PASS | Trial results, clinical efficacy and detailed cohort adjudication |
| R12 Derived vs source | Tests 08–10 compute bounded target/grouping results; 14 validates a new deterministic receipt; 15 gives qualified structural acceptance while historical defect remains visible | PASS for finite computation/control; historical record remains negative | Persisted correction if later needed; general comparison/production engine |
| R13 Shared/dependent evidence | Test 11 computes real shared-study intersection and changes to unresolved on link removal; existing false-independence controls and new result retain qualification | PASS for shared-source representation and bounded comparison | Statistical/biomedical independence or universal dependence judgments |
| R14 Scope/abstention | Tests 03/08/09/11–13/18 retain useful positives, withdraw affected claims under mutations and preserve limited scope; all prior forbidden-upgrade checks retained | PASS for structured Q01–Q07 contract | General free-text answering, held-out evaluation, supported-completion metrics |

No row is called biomedical-complete. PASS is justified by the observed capability and mutation result, not a similarly named test. The unavoidable manual/source judgments remain explicitly deferred rather than being silently inferred from technical checks.

## Verification commands and results

Run from repository root using existing Python 3.12.7, RDFLib 7.1.4, pySHACL 0.30.1 and owlrl 7.1.4 in the already installed isolated environment:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/private/tmp/dementiagraph-m1-task008-pyshacl python3 -m unittest discover -s tests -p test_m1_semantic_acceptance.py -v
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/private/tmp/dementiagraph-m1-task008-pyshacl python3 -m unittest discover -s tests -v
git diff --check
git diff --cached --check
git status --short --untracked-files=all
```

New suite: 18 tests passed in 15.367 seconds. On 2026-09-24, the complete suite passed **91 tests in 197.364 seconds**: all 73 existing regressions plus the 18 new M1.6 tests. RDF parsing, Meta-SHACL, reasoning controls, baseline 1-Violation/8-Warning and synthetic 0-Violation/8-Warning assertions passed. No findings were suppressed. Explicit new-file syntax/whitespace and Git diff checks passed; only the three authorized new files are present. Test 17 compares every tracked baseline file byte-for-byte; existing inventory, provenance, receipt, schema, SHACL and reasoning regressions remain required. No new package is installed. Git checks are supplemented by explicit whitespace and Python syntax checks for the three new untracked files.

## Approved bounded closure and remaining gates

The owner approved **bounded M1 closure** on 2026-09-24, accepting the results, the R1–R14 bounded/deferred distinction, the visible historical negative fixture and the scoped limitations documented here. The completeness defect disposition and its execution results are accepted within that boundary. This approval does not authorize M2 entry or implementation. The project milestone status is recorded in [README](../README.md).

No requirement to silently repair the historical fixture or invent absent evidence has been introduced. This package does not claim an entirely conformant historical graph. Any persisted replacement is outside the current three-file scope. The colon/underscore comparison is an explicit navigation convention preserving raw data, not approval of concept equivalence.

Remaining limitations are not concealed blockers: source compatibility is verified only within the pinned audit profile; shared-source joins do not settle true independence; no general natural-language evaluation or upstream source reproduction exists. The two documented owlrl limitations remain unchanged. Graph advantage remains NOT YET DEMONSTRATED. Q01–Q07 remain exposed design cases, not a held-out benchmark or independent experimental observations.

Final regressions passed. No unresolved implementation blocker has been identified for this bounded M1 acceptance package. The owner authorized the three M1.6 files and a minimal milestone-closure documentation update to be committed locally. Pushing, M2 work and research experiments remain unauthorized by this checkpoint.

### Closure checkpoint verification

On 2026-09-24 the complete suite was rerun: **91 tests passed in 199.592 seconds**. This run preceded the authorized README milestone-status update, because three existing historical-baseline guards compare all tracked files, including README. After that documentation update, all other tracked baseline files were checked byte-for-byte, and Git/whitespace checks covered the four checkpoint files. No implementation input was changed after the successful run. Direct full-suite reruns after closure will flag README in those historical guards until a separately scoped maintenance change permits the approved status update; this checkpoint does not claim a post-documentation unqualified full-suite pass.
