# Continued M2: implemented context, recovered aggregate and inspected publications

The context identity extension and both additional acquisition batches were executed within the bounded scope defined in the preceding records. The contract proposed in `ot2606_context_recovery.md` is applied here only to its stated four classes; that historical report and all previous source artifacts remain unchanged. No broad activation of every draft class occurred.

## Delivered

1. Executable Q01–Q07 evidence interface (commit `49634f5`) with qualified positive answers and evidence-sensitive abstention.
2. Context RDF and deterministic identity receipts: **43 resources / 226 triples**, including **five MechanismRecords and four ClinicalIndicationRecords**, eight snapshots and four normalized disease references. Memantine's two bounded target records share a single source description. Original arrays and report locators stay in source context; no extra source targets or disease hierarchy edges are promoted.
3. Union with existing Mondo/evidence release: **191 resources / 1,112 asserted triples**. Existing authority referents are reused; inventories are not added naively. No inferred graph is persisted.
4. Historical FTD/MAPT scalar aggregate recovered from already captured ranges: `associationScore=0.7898500725428946`, `evidenceCount=5056`, `aggregationType=overall`, source `aggregationValue` is the literal string `None`, not a missing-value repair. The integer is the source field, not 5,056 independent confirmations or unique targets. Projection recorded in `extractions/ot2606-association-001.partial.json` with footer/column digests and row locator.
5. Metadata for all **15 named publications** and permission-cleared local XML for all **four named PMC articles**. Technical selected-passage inspection is recorded with raw hashes, paragraph indexes and text hashes; no full article body is committed.

## Capture accounting and limits

| Attempt | Requests | Received body bytes | Result |
|---|---:|---:|---|
| Four OT context files (previous completed capture) | 4 | 12,702,710 | Complete, unchanged |
| Association probe, 64 MiB / 100 requests | 39 | 57,628,393 | Stopped before a requested range exceeded the remaining budget; no reset |
| Primary sources, 10 MiB / 100 requests | 11 | 801,988 | 15 metadata records + four article bodies; failed requests included |

The association probe reached 11 of 28 listed files and found the requested FTD/MAPT row in `association_overall_direct/part-00010-c3eaa79c-fb08-4d4a-9391-a4eceb74fa7a-c000.snappy.parquet`, physical row 265528. It initially requested unnecessary timeseries columns after locating the row. This was inefficient: those bytes are counted and retained, not concealed. No further range was fetched once the predicted request exceeded the ceiling. Offline recovery now uses **only the six required, already captured scalar columns**. Future continuation must project the required columns before fetching values; no repeat of the timeseries scan is justified.

There are **no recovered datasource-composition rows**. The unscanned remainder and partial sparse inspection file are not complete source files. `recover_projection` reconstructs a temporary inspection file from digest-verified ranges and refuses a missing required column. Its synthetic Parquet header and unfilled regions are never represented as a downloaded complete file. No full-table uniqueness, ranks, coverage or timeseries result is claimed.

The primary batch includes four initial NCBI OA metadata requests that returned 404 (6,336 bytes). The Europe PMC metadata route used for this batch supplied per-article licence declarations; it was used without resetting the ledger. Licences: PMC7852392 CC BY-NC; PMC6742707 CC BY; PMC6298197 CC BY-NC-ND; PMC4054967 CC BY. Bodies are retained locally for academic inspection, not redistributed through Git or treated as unrestricted training material. Capture timestamps identify new captures, not historical response reproduction.

Two official ClinicalTrials.gov candidate history-metadata requests returned **403** (268 bytes total). No current study record was substituted. Historical registry versions remain unresolved. Exact PanelApp input editions are also still absent from the local OT fields; previously failed API routes were not blindly repeated. These are source-access/version limitations, not permission to infer a panel revision from release dates.

## Source interpretation actually inspected

Inspection scope: first four matching body paragraphs per recorded pattern, or all matches if fewer. This is technical source inspection, not exhaustive article review or independent biomedical adjudication.

- PMC7852392 / PMID33008897: the selected passage compares human AD glycoproteomics with APP/PS1 mouse data. Do not upgrade that context to a new human PSEN1 causal association.
- PMC6742707 / PMID31555645: selected review paragraphs discuss presenilin/AD and tau/FTD separately. They do not establish PSEN1 causation of FTD; this does not prove that every passage in the article lacks relevant information or that the OT extraction is erroneous.
- PMC6298197 / PMID30581980: selected methods/objective passages describe a phase-one study in healthy participants, with safety/tolerability and pharmacology objectives. This is separate from NCT03658135; no patient benefit is inferred.
- PMC4054967 / PMID25031633: selected passages describe soluble amyloid-beta protofibril targeting. Preserve molecular-species qualification beyond a gene-indexed mechanism; historical article wording is not a current regulatory conclusion.
- Abstracts for PMID22503161, 23028126, 9641683 and 9789048 were inspected in the metadata response. They concern heterogeneous dementia-family genetics, an AD genetics review and historical FTDP-17/tau studies. No phenotype-wide equivalence or variant-specific modern clinical adjudication follows. PMID33303932 has no abstract in the returned metadata; its body remains unreviewed.

## Updated usable answers and what is still unanswered

The CLI now adds the verified scalar aggregate and four explicitly **project-derived technical inspection summaries** to the evidence-linked design outputs. Evidence and context source values remain distinct from those summaries. Q01 no longer reports those four article passages as unavailable. Q06 now includes the inspected aggregate, but does not assert complete table coverage or a treatment relationship. Q07 still explicitly withholds the unavailable registry population/status.

The original 56-slot assessment remains immutable. A new successor assessment records source recovery separately from RDF integration and question completeness. The state is:

- 24 reference-only slots have observed locators.
- All five mechanism/four indication slots are now represented in source-backed RDF; complete bounded zagotenemab list remains inspectable.
- The requested FTD/MAPT aggregate has a verified scalar projection; aggregate-table coverage is incomplete and no new source-aggregate RDF identity profile is activated.
- Four conditional article sources are captured and selected passages inspected, subject to recorded licences/depth.
- Local direct/inclusive GE computations remain reproduced; historical API execution is not.
- Primary PanelApp contexts, primary registry versions/populations/status and GRIN datasource composition remain incomplete.

Q01–Q07 are unchanged and remain design material. The presence of partial evidence is not full question acceptance. No M2 full-corpus closure, M3 completion, retrieval comparison result or model improvement is claimed. M3/M4 cannot be presented as a workaround for unresolved required population/source-context checks. No paid model or M6 orchestration was launched.

## Validation and next genuine decisions

Context RDF alone: SHACL **0 violations / 0 warnings**, raw conformance true. Combined graph: **0 violations / 2 existing warnings**, qualified structural acceptance; raw conformance remains false due to those warnings. OWL RL control confirms no new local substantive predicate assertion or equality between distinct resources. This does not prove biomedical truth or universal logical consistency.

Remaining decisions are concrete:

1. Historical ClinicalTrials.gov access needs an accessible historical export or a separately documented policy for a newly dated primary record. Current records will not silently replace the historical requirement.
2. Exact PanelApp input editions remain unresolved. Using an explicitly dated independently captured panel as contextual evidence would require a separately documented provenance decision; it would not reproduce the OT input snapshot.
3. Further association range retrieval requires a budget continuation plan using the **same accumulated ledger** and only necessary scalar/key columns. The current 64-MiB ceiling has not been reset or exceeded. No exact remaining total is claimed before required datasource column sizes are established.

Existing accepted context RDF, local selection results, recovered aggregate and inspected article sources can be reused directly; no architecture redesign or new general framework is needed.

The Git copy of the primary attempt ledger redacts provider `Set-Cookie` header values. Its `localLedgerSha256` binds the original ledger retained outside Git; all raw body digests, accounting and source metadata remain verifiable. This is explicitly a redacted transport-metadata copy, not a byte-identical raw ledger. Association transport metadata contains no such headers. No credentials or session cookie values are committed.

Final regression: **229 tests passed in 286.126 seconds**, including 221 prior/interface tests, five context-RDF tests and three remaining-capture tests. The strengthened five answer-interface tests were rerun separately against the final augmented outputs and passed in 6.510 seconds. Context RDF replay and combined SHACL were also checked directly. Original M1/Mondo/eight-evidence source artifacts remain unchanged; only the new answer interface and its generated output/test were updated to consume the additional verified sources. A trailing-output-newline defect in the initial CLI was corrected without changing source data.
