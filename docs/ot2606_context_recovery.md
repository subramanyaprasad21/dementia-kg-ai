# OT26.06 context batch: source recovery and remaining acceptance boundary

Owner authorization: attachment `8bfb4d8b-8356-4746-b3cd-37b4836135e1/Pasted text.txt`, following `753adead3ec76385b402f794b306f2aa49205a0a`. Four exact files, 20 MiB / 100 requests. This completes their acquisition and bounded offline inspection, not full M2 or a new KG release.

## Completed source work

`tools/ot2606_context.py` captures only the four committed routes. It refuses an existing batch directory, counts requests before sending, disables redirect following and automatic retries, accounts error/partial bodies, stops on size/budget/HTTP failure and preserves an interrupted ledger. It verifies raw bytes before schemas, extraction or selection. Budget measures response-body bytes (as earlier G05 accounting), not estimated TLS/network overhead; received headers are recorded separately. No new dependency or general acquisition framework.

Actual batch: **4 GET requests / 12,702,710 received body bytes**, all HTTP200, no retries, redirects or failures. No metadata request was needed during the batch; previously committed metadata supplied routes/sizes. Permission basis remains official Platform CC0-1.0 and provider attribution. Other documentation browsing is not biomedical record capture. Raw bytes and ledger are at `~/dementia-kg-ai-source-captures/ot2606-context-001/`, outside Git.

`manifests/ot2606-context-001.capture.json` is the exact ledger copy: request hashes, URLs, timestamps, response headers, sizes and raw SHA-256 values. This is transport provenance, not activation of a new semantic identity profile. `extractions/ot2606-context-001.json` preserves **16 complete selected rows** with typed source values, exact file/zero-based row locators, file hashes, ledger digest/capture index, schema and source-value hashes:

- **4 mechanism rows**, covering the five required drug/target slots. Memantine's original row includes another drug and seven target IDs; only memantine with GRIN1/GRIN3B belongs in the bounded proposed graph projection. Extra source array entries remain raw context, never independent acquired mechanisms for extra research entities.
- **4 indication rows**: complete zagotenemab list (AD and tauopathy), lecanemab AD, gosuranemab FTD. No FTD entry in the complete inspected zagotenemab list is a scoped source observation, not universal absence of an indication or treatment benefit.
- **8 disease-context rows** for the existing finite concept allowlist. Original arrays, names, synonyms, xrefs and ontology metadata are preserved; extra ancestors/descendants are source selection context, not new accepted graph relationships or equivalence.

Mechanism table has no source `id` or `datasourceId`; indication table supplies `id`, `maxClinicalStage`, `clinicalReportIds`, `drugId`, `diseaseId` only. It does **not** supply original indication condition wording or the primary report's population/status. Do not fill these from normalized disease names, audit prose, or maximum stage. The maximum stage `APPROVAL` on the lecanemab row is a source value, not a newly adjudicated regulatory assertion.

All fifteen required PMID locators are now source-observed: 12 in the eight-row evidence release and the remaining 30581980, 25031633, 33303932 in these mechanism rows. Citation recovery does not establish article inspection or validity of the claimed proposition.

## Local selection result

`assessments/ot2606-context-001.selections.json` records the actual new file-level algorithm: for APP/AD and MAPT/FTD, filter the complete local GE partition by targetId and either exact diseaseId or anchor union the **OT26.06 source descendants array**, then sort evidence IDs. Results:

| Pair | Direct distinct IDs | Inclusive distinct IDs |
|---|---:|---:|
| APP / MONDO_0004975 | 0 | 1 |
| MAPT / MONDO_0017276 | 3 | 10 |

The named APP `8bac3794…` and MAPT `019b39b2…` diagnostic IDs occur inclusively; the latter is absent directly. These reproduce the numerical audit observation under a specified new local predicate. No claim of replaying a historical API session, defaults, order or execution identity. Full GE file and hierarchy digests bind every result. No whole-EP or all-datasource selection completeness is inferred. Source closure is used for the computation only, not added to the accepted five-parent Mondo graph.

## Successor 56-slot assessment and Q acceptance

The original 9/26/21 release assessment is immutable. `assessments/ot2606-context-001.readiness.json` preserves its statuses and records a separate source-support dimension:

- 9 existing narrow source slots remain verified.
- 24 authority-reference slots now have observed locators; no independent metadata claim.
- Five mechanism and four indication slots have the required source rows; complete zagotenemab list context is recovered too.
- Local Q04 counts/membership are reproducible; clinical report links are recovered.
- Historical aggregate/source composition, three versioned PanelApp contexts, two primary registry records, and rights-cleared inspection remain incomplete.

Q01/02/03/05/06/07 remain **PARTIAL**. Q04's source calculation is verified, but new-context RDF/query acceptance remains pending. Details for each question, not a single inflated completion percentage, are in the successor assessment. No question is silently narrowed or declared passed merely because an ID exists.

## Narrow identity decision — pending, not activated

The approved `docs/ot2606_identity_contract.md` explicitly says mechanisms, indications and source aggregates are **not activated**. The existing `m2-ot-parquet-description-1` also requires an evidence ID and datasourceId. It cannot describe the mechanism schema without inventing fields. Preserve both contracts and all old receipts.

Proposed bounded successor, **PENDING OWNER APPROVAL**:

1. `m2-ot-context-description-1`: exact receipt keys `profile`, `provider`, `edition`, `table`, `schema`, `locator`, `contentSha256`. Provider `Open Targets Platform`, edition `26.06`; schema is the observed ordered column-name/type list. Locator is exact `{url,fileSha256,fileRowNumber}` with row number encoded as a decimal string. Hash the existing canonical typed all-column source projection; preserve array order, nulls, strings and source booleans/numeric types. Absent fields remain absent. No invented source ID; existing `id` remains in sourceValues when present. SHA-256 with existing canonicalization. Capture timestamp/request/header fields are excluded. Repackaging changes the file-scoped description; it does not assert a new independent biological observation. Repeated capture of the same file/row preserves the description.
2. `m2-context-record-1`: unchanged envelope `profile/kind/origin/inputs/contentRevision`, only SourceSnapshot, DiseaseConceptReference, MechanismRecord, ClinicalIndicationRecord for the initial context projection. SourceSnapshot inputs exactly `{descriptionId,edition,datasource,locator}`, with datasource the observed archive table name. Other inputs use existing G02 tuples unchanged: disease `(snapshotKey,locator,role,authority,identifier,label)`; mechanism `(snapshotKey,locator,drugKey,targetKey)`; indication `(snapshotKey,locator,drugKey,diseaseKey)`. All keys required; optional values explicitly null only where G02 allows them. No new ontology terms. Existing authority-qualified Target/Drug/Publication referents may be reused.
3. Disease roles are source-normalized or contextual references, with exact source IDs. Never supply an original disease role from the normalized table. One mechanism source description may support multiple bounded drug/target record projections; these remain dependent on the same source row. No clinical indication from mechanism composition. Reports remain source locators unless separately justified StudyRecords are implemented; do not copy an indication's maximum stage into every report.
4. Owned payload digest remains immutable contentRevision; all snapshot/participant links must resolve to verified descriptions/referents, reject unsupported origin, missing lineage, collisions and M1 identity reuse. A payload/source change creates a new description/record; capture-only changes do not. Execution identities for future selection/RDF conversion must be recorded as actual new project operations, not fabricated historical encounters.

This is the smallest contract change needed before the recovered context can safely become source-backed RDF. No speculative identity generator was activated, no fake M1 receipts reused, no OWL/SHACL modified. The proposed profile deliberately does not activate primary registry populations, article review, source aggregates or every draft class in advance.

## One consolidated remaining-acquisition request

The approved four-file batch is complete; its unused budget is not permission for other sources. Request **two named additional sub-batches, 74 MiB / 200 requests total**, with separate non-transferable limits:

**B — historical association selectivity: 64 MiB / 100 requests.** Exact 28 filenames/official26.06 routes are already in `assessments/remaining-m2-plan.json`, under `association_overall_direct` and `association_by_datasource_direct`. Targets only FTD/MAPT aggregate and FTD/GRIN1, FTD/GRIN3B source composition. Inspect Parquet footers/key-column ranges first, then matching bounded rows if the same budget permits. Exact necessary range bytes remain NOT YET VERIFIED. Do not download complete ~GiB partitions; stop with an additional-size calculation if selective access exceeds the limit. No need to redownload GE/clinical/europepmc or buy provider access.

**C — primary-source version/rights and bounded capture: 10 MiB / 100 requests.** Three PanelApp gene/panel contexts, two NCT studies, fifteen publication locators, four conditional full texts only. Preflight versions/rights first; capture only where compatibility and retention are established:

- PanelApp: 265/PSEN1, 474/MAPT, 540/MAPT. Official API/documentation and gene history pages; entity route and explicit version parameter must be verified before capture. The old panel/gene endpoint failed previously and is not to be retried blindly. Exact panel editions used by OT remain unknown; original GE rows do not encode them. A current response is not a historical substitute.
- ClinicalTrials.gov: NCT00594737 and NCT03658135. Official `/api/v2/studies/{NCT}` is current; the official Record History interface is the candidate historical route. An [NLM modernization report](https://www.nlm.nih.gov/od/bor/NLM_BOR_CTG_WG_Modernization_Update_Report_20241031_508.pdf) documents history comparison, not a guaranteed version-export endpoint. Retrieve version history metadata first within the authorized batch; do not infer a version ID from a last-update field. Exact historical route/permissions remain unresolved. If unavailable, report without switching editions.
- Publications: Europe PMC REST `search` with exact `EXT_ID` plus `SRC:MED`, `resultType=core`, bounded to the fifteen existing PMIDs. Four permitted article bodies only: PMC7852392, PMC6742707, PMC6298197, PMC4054967; official Europe PMC `/{PMCID}/fullTextXML` or supported PMC API after checking article-specific rights. No paywall workaround, supplementary corpus, regulatory label acquisition or extra disease. Record inspected spans and access depth; full-text permissions are not inherited from OT CC0.

Official PanelApp API docs and ClinicalTrials.gov terms pages did not yield readable version/permission guarantees in this turn's documentation check. These remain **NOT YET VERIFIED**, not presumed unrestricted. Sizes of B's selected ranges and C's permitted responses remain unknown; protective caps are not completeness estimates. Count metadata, redirects, retries and failed bodies; stop-and-report without automatic reset or source substitution. No primary biomedical records were acquired during this turn.

## M3/M4/M5 disposition

M2 minimum acceptance is **not yet satisfied**. Unavailable registry population and source composition are substantive Q requirements, not optional enrichment. Consequently M3 graph characterisation and M4 baselines have not been started as a bypass. Existing accepted graph remains **152 resources / 898 asserted triples**; no new graph results are claimed. M5 depends on accepted retrieval outputs plus a concrete model, inference ceiling and frozen evaluation design; no model chosen or paid call launched. Q01–Q07 stay exposed design material, not a held-out benchmark.

After identity approval, context RDF/semantic validation can proceed independently of B/C, using existing source bytes. After the minimum bundles pass, proceed directly through the approved M3→M4→M5 sequence. No architecture redesign or optional enrichment blocks that path.

## Verification and reproduction

Run with the existing external DuckDB/RDFLib/pySHACL/owlrl environment:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=tools:/private/tmp/ot2606-duckdb-inspection:/private/tmp/dementiagraph-m1-task008-pyshacl python3 tools/ot2606_context.py verify
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=tools:/private/tmp/ot2606-duckdb-inspection:/private/tmp/dementiagraph-m1-task008-pyshacl python3 -m unittest discover -s tests -v
```

Focused controls verify finite plan/budget, no reset, failed-body accounting, truncation, request/body tampering, exact sixteen-row replay, relocation/missing inputs, original mechanism group structure, indication identity, and source-derived direct/inclusive membership. They do not establish clinical correctness or biomedical evidence independence. Full regression results follow below after completion.

Final verification: **216 tests passed in 275.300 seconds**, including all 207 prior regressions and nine new tests. After tightening the full-zagotenemab predicate and locator-coverage assertions during the regression run, all nine context tests were rerun against the final code and passed in 1.474 seconds. No pre-existing tracked file differs from baseline. Whitespace/newline checks passed for all seven new files. No raw Parquet or local acquisition directory is included in Git.

Committed artifact digests: capture manifest `970a28d46d5e618de9ad424a678b8d5c19942da061167bfca70e72734bd7ceb0`; extracted intermediate `6c46d63043914193cbfcd1f10f94de581f81a1e27efe2c85e7703ea9afb90884`. These identify actual files; they are not newly approved semantic source-description identities.
