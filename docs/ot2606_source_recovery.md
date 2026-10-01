# Historical Open Targets 26.06 recovery and bounded freeze

This recovery continues from `4f1f28f`. No historic M1/Mondo files or profiles are edited. This is an eight-row OT source slice, not full Q01–Q07 reconstruction.

## Actual inputs and acquisition boundary

Four unchanged browser-downloaded Parquet files are copied outside Git to `~/dementia-kg-ai-source-captures/ot2606-evidence-001/`. `OT2606_ARTIFACTS` may relocate this directory without changing identities. Original Downloads files remain intact. The freeze manifest records full filenames, bytes, SHA-256, actual schema, Parquet metadata, original browser download URLs, local observation receipts and permission review. Edition 26.06 is bound by the exact official archive route and saved browser origins; EP downloaded byte ranges additionally match the earlier instrumented archive scan. No publisher-signed full-file checksum is claimed. Exact manual browser HTTP timestamps, headers, attempts and transfer accounting are unavailable; local observation time is not acquisition time or source edition.

The earlier EP scan's original ledger and 250 range artifacts are retained with the files. Offline verification hashes every range and compares the matching files' source ranges byte-for-byte. The completed 125-file scan establishes one occurrence of each EP ID across the partition; local GE/clinical files are their complete respective partitions. No new biomedical request or repeat scan was made.

Official permission review on 2026-09-25: [Open Targets licence](https://platform-docs.opentargets.org/licence) marks Platform data CC0 and permits downstream use of its listed sources. Preserve Open Targets, datasource and publication attribution. This applies to this distribution, not independently acquired PanelApp/registry distributions or full articles. No raw-file redistribution is included in this release. Permission review relied on the published licence page; a raw-byte permission-page capture and exact transport accounting are not claimed. Future publication must retain applicable source attributions and distinguish extracted snippets from independently licensed full articles.

## Contracts and reproducibility

`m2-local-file-observation-1` records one **local inspection**, not a reconstructed network encounter. Exact keys: profile, execution, fileName, sourceUrl, edition, rawSha256, bytes (decimal string), observationTime, acquisitionTime (null), acquisitionTimeReason, downloadOrigins (ordered original metadata). Identity is the existing UTF-8/JCS-subset canonical receipt SHA-256 under `/id/<profile>/<digest>`. Replay retains the receipt. A new actual inspection has a new execution/time; it does not create independent evidence.

`m2-ot-parquet-description-1` describes an individual OT evidence row. Exact keys: profile, provider, edition, datasource, sourceRecordId, schema (ordered name/type pairs), projection, contentSha256. Projection includes every original column and nested value. Strings are unchanged; integer values use exact decimal strings; finite binary64 values use Python hexadecimal float lexical representation (including signed zero); null, boolean, array and object have explicit type tags. Arrays retain order, duplicates and null entries. Missing columns remain absent and are never synthesized as null. No transport headers, local paths, inspection time or unrelated row bytes enter description identity. Changed projected payload or schema produces a new description. The raw file digest remains separate lineage. These are narrow successor profiles; existing profiles remain untouched.

The machine manifest is deterministic sorted JSON with LF. Row receipts use the existing canonicalizer's string/null/container subset after explicit numeric typing. `ot2606_source.py` verifies pinned authorities, original files, scan artifacts, edition, URLs and schemas before extraction. Output retains all eight rows and original text-mining offsets/snippets with complete manifest/file/description/local-observation lineage. Scores are source values, not causal or clinical confidence. No source-value normalization, silent label correction, mapping repair or biological equivalence occurs.

## Reconciliation and availability

The separate assessment preserves the original 56-slot contract and historical audit. It updates availability with per-slot scope and supporting evidence IDs: **9 VERIFIED, 26 PARTIALLY VERIFIED, 21 UNAVAILABLE**. The nine are Mondo plus eight evidence-row slots. Locator-only target/drug/publication support is partial; panel editions, registry populations/status/results, mechanisms, indications, source aggregates and old query totals remain unsupported or partial. All seven broader question contracts remain partial.

The exact machine comparison to pinned fixture assertions has **53 VERIFIED / 6 DISCREPANT** checks. Four discrepancies are normalized MONDO colon-versus-underscore spelling; two are the clinical original label abbreviated as `FTD` in the fixture versus `frontotemporal dementia` in source. Both forms remain unchanged. No clinical equivalence or original audit error is inferred from these lexical differences. All eight IDs, target identifiers, datasource values and non-null publication-locator lists match.

Previously unavailable EP text-mining sentences/offsets are now present in the archive. Original disease fields are **absent columns**, not reproduced explicit nulls. This cannot retroactively change the earlier GraphQL inspection or its depth. APP and contextual MAPT/PSEN1 mappings remain original source assignments; their causal correctness or mapping algorithm remains unverified. Two clinical rows share `nct00594737`, drug and stage, but distinct targets/IDs; this is not independent trial confirmation or efficacy.

## Verification

Runtime: DuckDB 1.5.5 in an isolated temporary installation; existing Python/RDF environment unchanged. No project dependency installation or biomedical network acquisition is performed by these tools.

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=tools:/private/tmp/ot2606-duckdb-inspection:/private/tmp/dementiagraph-m1-task008-pyshacl python3 -m unittest discover -s tests -p 'test_ot2606_source.py' -v
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=tools:/private/tmp/ot2606-duckdb-inspection python3 tools/ot2606_source.py verify
```

Negative controls cover missing/changed raw files, wrong edition/route/rights, duplicate/missing requested IDs, numeric/absence distinctions and changed audit expectations. Historical artifacts remain pinned. This completes bounded source verification/freezing/extraction and no-transformation assessment; source-backed RDF and broader clinical acceptance are separate work.
