# Remaining finite M2 corpus: minimum acquisition and acceptance plan

Baseline: `64fafbe76270e0c603a5efe23363aef9039a6bcf`. This is a successor planning assessment, not a replacement release, permission to download, activated identity contract, or full-corpus acceptance. Mondo + eight OT evidence records remain 152 resources / 898 asserted triples. All earlier artifacts remain unchanged.

## Offline assessment and replay

The 56-slot contract and released assessment were inspected without rewriting either. `assessments/remaining-m2-plan.json` retains every slot, original locator, Q membership and previous status, assigns an acquisition operation, and specifies its missing information. Its four SQL queries replay against the hash-verified, already downloaded complete GE and clinical-precedence partitions. No new source records are integrated into the graph.

The historical **9 verified / 26 partial / 21 unavailable** labels remain intact. They are not 47 independent downloads:

| Previous group | Exact remaining requirement / smallest operation |
|---|---|
| 18 partial reference slots: five targets, twelve PMIDs, memantine | Already have source-observed authority locators. The contract explicitly requires reference-only representation, not independent metadata enrichment. No download just to populate these slots. Article interpretation is separate. |
| Three unavailable drug references: zagotenemab, gosuranemab, lecanemab | Now observed in the existing clinical-precedence partition by exact CHEMBL ID. Locator-only requirement satisfied; mechanisms and indications remain separate. |
| Three unavailable PMIDs: 30581980, 25031633, 33303932 | Required mechanism-study locators; recover their relationship from the mechanism table before independent article inspection. Do not replace relationship provenance with a PubMed search hit. |
| Three partial PanelApp contexts | 265/PSEN1, 474/MAPT, 540/MAPT: exact historical panel edition, entity identity, phenotype/OMIM values, confidence and citations. OT studyId does not identify a panel version. |
| One partial and one unavailable registry record | NCT00594737 and NCT03658135: versioned primary registry population/design/status/eligibility and dates. OT phase/report IDs are insufficient. |
| Ten unavailable association/mechanism/indication slots | FTD/MAPT aggregate; five mechanism slots for four drugs; four indication slots (zagotenemab AD/tauopathy, lecanemab AD, gosuranemab FTD). Slot aliases are not invented upstream IDs. |
| Two partial contexts | GRIN1/GRIN3B datasource composition still needs the association datasource table; clinical linkage has local OT support but still lacks indication and primary registry provenance. |
| Two unavailable contexts | Direct/inclusive selection semantics and complete bounded membership; complete scoped zagotenemab indication list. Eight named rows do not establish either completeness. |
| Two partial and two unavailable conditional full texts | PMC7852392, PMC6742707 have OT snippets; PMC6298197, PMC4054967 do not. Exact article edition, permitted passage, locator and inspection depth remain necessary for passage-level claims. |

Thus **21 reference-only slots** have observed locators without additional authority downloads. This does not reclassify 21 biomedical claims as verified. All seven full question bundles still have qualifications/gaps.

### New local observations and their limits

The stored SQL, parameters, input hashes and results are reproducible offline:

- Exact normalized FTD equality in GE: PSEN1 **5 rows / 5 distinct evidence IDs**; MAPT **3 / 3**.
- Exact normalized FTD equality in clinical precedence: GRIN1 **3 / 3**; GRIN3B **3 / 3**.
- All three remaining CHEMBL drug locators occur in the local clinical-precedence partition.
- Gosuranemab `CHEMBL3990042` → `nct03658135` → `MONDO_0017276` with source `PHASE_1` is locally recoverable.

These are new offline queries over archived 26.06 files, not replayed historical GraphQL encounters. They do not establish full source composition, API ordering, inclusive closure, a standalone indication identity, registry status or clinical efficacy. Do not promote other reports returned during exploratory inspection into the finite corpus.

Recovered clinical literature arrays include source null; the old audit described an empty string. Together with the previously documented lexical discrepancies, this remains a representation distinction to preserve, not silently repair. Absent original-ID columns also remain different from API null fields.

## Coordinated acquisition proposal

Use only official routes and release 26.06. Exact historical fields remain subject to schema inspection. Raw material stays outside Git, with request ledger, byte digests, file/schema metadata, version provenance, permissions, immutable descriptions and separate capture identities. Count every metadata request, redirect, retry and unsuccessful body; never reset a ceiling automatically.

### A. Small OT context batch (highest priority)

Official base: <https://ftp.ebi.ac.uk/pub/databases/opentargets/platform/26.06/output/>.

| Table | Finite selection / projection | Why required |
|---|---|---|
| `drug_mechanism_of_action/` (two files) | CHEMBL807, CHEMBL4298021, CHEMBL3990042, CHEMBL3833321; original mechanism/action, target object, gene links, references and source IDs | Q02/Q06/Q07; actual mechanism distinct from joined clinical-precedence evidence |
| `clinical_indication/clinical_indication.parquet` | Those four drugs; preserve original condition, normalized ID, stage, exact indication ID and report references. Inspect the complete zagotenemab list, but do not expand disease anchors. | Q06 absence limited to the inspected list; Q07 exact gosuranemab indication `c680c47a8cc2571635e1d5c629e51834273a3e67d25ebedfa9e58b729ad65189`; memantine only as far as required to verify the documented join |
| `disease/disease.parquet` | AD/FTD selection hierarchy and named APP/MAPT diagnostics; inspect release-matched hierarchy context needed for bounded selection, do not promote new concepts/parent edges into the research graph | Q04: archived OT taxonomy is not automatically identical to Mondo 2026-09-01 |

HEAD metadata gives exact payload sizes: mechanisms **281,271 + 299,939 bytes**, indications **4,970,713 bytes**, disease **7,150,787 bytes**; total **12,702,710 bytes (12.11 MiB)**. These are planned file-body bytes, excluding metadata/retries. Directory listings establish these files, not their schemas or requested rows. The machine plan records filenames and size metadata. Proposed ceiling **20 MiB / 100 requests** for this batch, including metadata and failures. This exceeds the old 10-MiB cap and is therefore a separate acquisition budget rather than an extension of the previous ceiling. Stop on schema/edition ambiguity or exhaustion. No fallback to 26.09. Full downloads of these small context tables are simpler than a new remote scanning framework; research projections remain finite.

### B. Historical aggregates — selective, not full-table download

`association_overall_direct/`: 14 files, roughly 1 GiB; `association_by_datasource_direct/`: 14 files, roughly 1.1 GiB (rounded directory sizes, not exact transfer estimates). Need FTD/MAPT aggregate and FTD/GRIN1, FTD/GRIN3B datasource composition. Preserve datasource identifiers, scores/count definitions, direct scope and release metadata. Do not infer these from GE/clinical rows alone.

Propose a separately accounted **64-MiB / 100-request metadata-and-selectivity pilot** over these 28 Parquet files. Read footers, then necessary key columns/ranges where feasible; reject a server's unexpected full-body response before unbounded transfer. Full association partitions are outside this plan. Exact matching files and total key-column bytes are **NOT YET VERIFIED**. If the pilot cannot locate the bounded rows within its ceiling, report exact additional bytes before continuing. It is not a promise that 64 MiB suffices.

Selection context can reuse the full local GE partition after A verifies release-specific hierarchy and applicable selection semantics. Recompute and label a new derived bounded selection, retaining original audit settings/counts separately. Do not claim historical API ordering/session reproduction. Whether all historical inclusive counts can be reproduced remains unresolved. No full Europe PMC partition is needed for the core GE diagnostic question; the two EP files do not support whole-partition counts.

### C. Primary sources and publications — version/rights gated

Propose a single **10-MiB / 100-request** primary-source batch with this finite allowlist and stop conditions, not unrestricted enrichment:

- **PanelApp:** three entity records only: 265/PSEN1, 474/MAPT, 540/MAPT. Official [API documentation](https://panelapp.genomicsengland.co.uk/api/docs/) is the route authority. Version-pinned entity URLs and compatible historical editions are **NOT YET VERIFIED**; do not assume a panel-wide response or current entity establishes the historical version. Establish applicable direct-source retention/reuse terms first. OT's downstream licence does not establish direct PanelApp permissions.
- **ClinicalTrials.gov:** NCT00594737 and NCT03658135 only. [Official API documentation](https://clinicaltrials.gov/data-api/about-api) describes current study access; it does not certify a historical snapshot. The audit's last-update dates (2012-06-04 and 2019-12-19) are field observations, not capture version IDs. Historical history/export route, version IDs and direct reuse conditions are **NOT YET VERIFIED**. Capture only once the requested edition is established. If historical access fails, any explicitly new dated context must be treated as a separate design decision rather than a substitute for the historical record.
- **Publications:** the fifteen PMIDs in the unchanged contract, preferably one bounded metadata request; retain exact citation links from OT before inspection. Full text only for PMC7852392, PMC6742707, PMC6298197, PMC4054967 if the exact article licence permits it. Use official supported retrieval APIs, not automated HTML scraping. [PMC rules](https://pmc.ncbi.nlm.nih.gov/tools/openftlist/) require article-specific rights checks; inclusion in PMC alone is insufficient. Metadata, abstract, snippet and full-text inspection are distinct depths. Unknown/denied rights means retain locator plus missingness, not copy the body.

Expected primary-source payload sizes and exact historical routes are **NOT YET VERIFIED**. The ceiling is protective, not an estimate of scientifically complete evidence. Do not silently truncate a required list to fit it. Version/rights preflight may finish with an unresolved outcome before any record capture.

[Open Targets licence](https://platform-docs.opentargets.org/licence), checked 2026-09-25: Platform data CC0 1.0; cite the provider. Its documentation says supplier data are available without restriction to OT users. This does not grant full-text rights from external publishers or resolve direct-source PanelApp terms. Preserve attribution and permission evidence at capture time.

No exact combined download promise is possible before B/C route/schema checks. The proposed ceilings total **94 MiB / 300 requests**, in three distinct named batches, never an automatic reset or transfer between budgets. Batch A can be executed independently first: it has the highest ratio of unresolved question coverage to acquisition size.

## Reuse and source-specific implementation gates

Reuse unchanged: digest verification, immutable freezes, typed lexical serialization, capture-versus-description separation, replay/collision checks, no-transformation assessment, scoped reference matching, original-value retention, RDF provenance pattern, SHACL/OWL separation, semantic negative controls and release packaging.

Source-specific work only: actual table projections and editions; bounded selection algorithm and extent; mechanism/indication/population/report identity receipts; primary-source permission and review-depth metadata. Existing `m2-evidence-record-1` does not activate every mechanism/indication/population class. Finalize the already proposed successor receipts against real schemas; any identity-contract change remains a separate design change. Preserve m1-id-1, m2-capture-1, m2-source-description-1 and existing RDF profiles unchanged. Do not use a live schema to guess historical fields or construct another ingestion framework.

## Minimum acceptance before broader research stages

| Question | Minimum additional support or explicit unresolved outcome |
|---|---|
| Q01 | Existing three PSEN1 evidence rows plus versioned PanelApp context and permitted inspection sufficient for the claimed article comparison. Missing original fields remain missing; no causal upgrade. |
| Q02 | Existing shared report linkage plus actual memantine mechanism and bounded datasource composition; registry information only at established version/depth. Shared evidence is not independent confirmation. |
| Q03 | Existing Pick evidence and Mondo path plus source-versioned PanelApp context; preserve upstream normalization separately from the direct query. Mapping cause/equivalence remains unadjudicated. |
| Q04 | Release-matched hierarchy/selection semantics and complete bounded GE membership, validated against full local GE data; original audit counts retained independently. No partial list promoted to complete. |
| Q05 | Existing divergent OMIM mappings plus 265/540 contextual records; preserve unresolved ambiguity, do not require a fabricated reconciliation. |
| Q06 | Actual FTD/MAPT aggregate, mechanisms and complete bounded zagotenemab indication list; separate lecanemab control and publication depth. No composed treatment/efficacy assertion. |
| Q07 | Exact gosuranemab indication, preserved report linkage, versioned registry population/design/status, separate mechanism-study context and inspection depth. No efficacy conclusion. |

Missingness can support a qualified answer/abstention, but cannot satisfy a mandatory absent relationship or turn the investigation into a successful positive biomedical answer. If a required historical input remains unavailable, an explicit research-design disposition is needed before declaring the finite corpus complete. Do not force 56/56 by relabelling missing slots.

Shortest defensible sequence:

1. Acquire A under its separate acquisition budget; process its finite projections through existing M2 stages. In parallel within the defined budgets, resolve B selectivity and C historical versions/rights. Reuse local counts/linkages immediately, without additional downloads.
2. Complete finite source bundles, settle identity gates, rerun Q01–Q07 semantic acceptance and release a versioned corpus with clear residual limitations. No ontology redesign.
3. **M3 graph characterisation:** characterize the actual accepted graph (types, relations, source imbalance, connectivity and provenance coverage) with its finite sampling limitations. Do not claim population representativeness or graph advantage.
4. **M4 retrieval baselines:** build fair text/graph comparisons over the same accepted evidence population, with comparable source context and retrieval budgets. Existing design fixtures can support engineering controls; Q01–Q07 and paraphrases are not held-out evaluation.
5. **M5 verified AI integration:** add traceability, semantic checks and abstention against accepted retrieval outputs. Model/access/cost choices and the evaluation protocol must be fixed before evaluation. SHACL conformance does not establish answer truth.

M6 remains conditional orchestration, M7 requires held-out material/reviewer arrangements/statistics, M8 presentation/release. Do not start M3–M5 as a bypass for unresolved M2 acceptance. Offline work immediately possible includes receipt specification after observed schemas, test design and corpus documentation; no additional architecture is needed now.

## Verification

Three focused tests verify all 56 slots and unchanged authorities, replay every recorded local SQL query against hashed input files, alter query identifiers to ensure the query really returns no matches, and prevent locator-only satisfaction from becoming question acceptance. The pre-existing full regression suite is run separately; results are recorded below when complete. No source bodies, historical artifacts, ontology terms, or prior identity profiles are changed.

Planning preflight used five directory-listing GETs (14,703 response-body bytes total) and four HEAD calls (no Parquet bodies), plus official documentation browsing. This was not the future instrumented capture batch; transport-level redirect/header accounting was not retained and is not claimed. The machine assessment retains the listing rows and HEAD sizes. No biomedical response body was downloaded.

Final verification: **204 pre-existing tests passed in 277.605 seconds**, plus **3 new planning tests passed in 1.086 seconds**: **207 passing tests in total**, run in separate regression/focused invocations. Existing tracked files compare byte-for-byte unchanged against baseline. Historical SHACL exceptions remain governed by their existing tests; this plan does not reclassify them.

Reproduction commands (existing external dependency locations, no installation):

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=tools:/private/tmp/ot2606-duckdb-inspection:/private/tmp/dementiagraph-m1-task008-pyshacl python3 -m unittest discover -s tests -v
```

The full command now discovers the additional three tests too. The recorded verification sequence ran full discovery before the new test file existed; its 204-test log is `/private/tmp/remaining-m2-regression.log`. The three new tests were run separately with `-p test_remaining_m2_plan.py`. The 207 total therefore comes from those two recorded invocations, not a single combined run.
