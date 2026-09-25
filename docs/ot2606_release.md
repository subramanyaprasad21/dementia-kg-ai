# Bounded historical OT evidence release

## Outcome and boundary

Eight independently recovered Open Targets Platform 26.06 evidence rows now have reproducible freeze, source-preserving extraction, no-transformation assessment, contextual reference resolution, RDF identities, provenance and validation. The original Mondo release and all M1 artifacts are unchanged. This completes the **authorized eight-row source-backed slice through M2.9**, not the entire finite evidence corpus. Additional required sources remain unavailable or partial. No M3–M8 work, new biomedical acquisition or push occurred.

Release: `manifests/ot2606-evidence-001.kg-release.json`. It pins all source files, extraction/assessment/operation/identity artifacts, RDF components, implementation/test files and runtime versions. The combined graph is reconstructed from existing component files rather than committing a duplicate union dataset. Exact raw files and selective scan artifacts remain outside Git in `~/dementia-kg-ai-source-captures/ot2606-evidence-001/`.

## Source inventory

All eight IDs occur once within their relevant historical partitions: complete local GE and clinical partitions, plus the previously completed 125-file EP ID scan, whose exact matching ranges agree with the downloaded files. No repeat EP scan was performed.

| Partition / part | Bytes | SHA-256 |
| --- | ---: | --- |
| Genomics England / 00000 | 4,355,571 | `1ed453fd150769d7701760fbfb5935f9accfa0557a956b7cbe83bba403602a9b` |
| Clinical precedence / 00000 | 65,766,146 | `b3a66214b4941a5ec9c22bb43fb188f91c90d5a39e5d71d1e5e028b300202ad9` |
| Europe PMC / 00034 | 116,668,033 | `6d7ede3352b05338cc3bb6c2280d8f4fa031806a4c3185781c953961ca9d4a02` |
| Europe PMC / 00123 | 58,310,635 | `ab7b04a7323caa4c53128b4621399ab937500b780e2439c7d657ba6707562c5b` |

Full original names, official URLs, schemas, Parquet metadata and actual local observation receipts are in the freeze manifest. Owner-managed browser downloads do not have reconstructed HTTP headers or encounter timestamps. The earlier range scan remains 250 requests / 1,027,119,970 response-body bytes; this is not a fabricated accounting total for the manual full-file downloads.

## Graph and identity inventory

OT graph: **92 resources / 581 asserted triples**:

- 8 EvidenceOccurrence, 8 SourceSnapshot, 8 MappingRecord.
- 16 DiseaseConceptReference: 6 original, 8 normalized, 2 local project-anchor roles.
- 5 Target and 12 Publication referents; 1 source-spelled Study referent, 2 OT StudyRecord descriptions.
- 2 local SelectionContext, 6 SelectionMembership and 5 project-grouping DiseaseTargetAssociation.
- 1 bounded shared-source DerivedStatement, 2 MissingnessRecord.
- 16 provenance entities: 8 row descriptions, 4 raw files, 4 local observations.

Mondo union: **152 resources / 898 asserted triples**. Its five accepted parent assertions and six excluded raw rows are unchanged. There is no owl:sameAs, automatic descendant closure or cross-source identity merge. Source description and local observation identities remain distinct. All eight source occurrences have new source-backed identities, not audit-transcription identities. Authority-only referents retain the existing approved referent identity mechanics.

## Validation and acceptance

- Deterministic source extraction, receipt/RDF replay and raw/range hashes verify offline. Source relocation is tested; altered/missing files and wrong versions/lineage are rejected.
- Original strings, absent columns, explicit null values, empty arrays, ordered nested arrays and numeric values are preserved. Clinical literature null entries remain visible. No source normalization or mapping correction occurs.
- RDF-only queries recover exact source target/disease/publication/report/stage values. Actual graph mutations change or block affected answers; receipts do not supply missing query values.
- New graph and combined union: **zero SHACL violations / two warnings** for absent EP original input. **Raw conformance false; qualified structural acceptance.** The original M1 baseline remains its approved one-violation/eight-warning historical negative fixture.
- Combined declarations+data reasoning: **1,253 input triples → 2,651 closure triples**, no detected diagnostics and no unexpected substantive additions. This is a bounded OWL RL result, not proof of biomedical truth or universal consistency. Existing engine limitations remain documented.
- Full regression results are recorded below after completion; Q01–Q07 are design material and no held-out evaluation is claimed.

## Readiness and remaining source decisions

The separate 56-slot assessment gives **9 VERIFIED / 26 PARTIALLY VERIFIED / 21 UNAVAILABLE**. Nine covers eight exact rows plus frozen Mondo. Partial slots cover five target locators, twelve publication locators, memantine's drug locator, three panel/gene references, one study locator, two source-context slots and two source-snippet/full-text slots. These are not independently acquired full source records. All broader Q01–Q07 source-backed acceptance remains partial.

The source-row blocker for the eight exact OT 26.06 IDs is resolved. Remaining work must not be described as that same unresolved archive-access issue:

1. Historical source aggregate for FTD/MAPT and original selection/list composition: no ranks, totals or full disease-target coverage recovered from these rows.
2. Separate drug-target mechanism and drug-disease indication records for the approved finite slots: evidence clinicalStage/drugId fields cannot substitute for them.
3. PanelApp 265/PSEN1, 474/MAPT and 540/MAPT historical panel/gene editions: references recovered, original editions unverified.
4. ClinicalTrials.gov NCT00594737 and NCT03658135 historical records and population/status/outcome context: OT's lowercase locator and PHASE_3 do not establish those versions or results.
5. Independent inspection of approved publication metadata/passages and conditional full texts under their own permissions. OT snippets do not silently satisfy article-level obligations.
6. Mapping algorithms and ambiguous clinical equivalence remain unadjudicated; preserve assignments without repair.

A further exact-source acquisition requires owner authorization after its route/version/permissions and budget are established. The next work is to resolve those remaining finite M2 slots, not expand disease/pathway scope or download the whole Platform. M3 graph characterisation and M4 retrieval baselines must use an approved evaluation population; M5 verified AI integration additionally needs model/access/budget decisions. M6 agentic orchestration remains conditional. M7 needs the approved experimental protocol, held-out material and reviewer arrangements; M8 is research presentation/release. None is started as a workaround for incomplete M2.

## Reproduction

Use DuckDB 1.5.5, RDFLib 7.1.4, pySHACL 0.30.1 and owlrl 7.1.4. The current temporary dependency locations are implementation-environment details, not embedded source identities. Install those pinned versions in a separate environment if reconstructing elsewhere; no network is needed once dependencies and raw artifacts are present.

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=tools:/private/tmp/ot2606-duckdb-inspection:/private/tmp/dementiagraph-m1-task008-pyshacl python3 tools/ot2606_release.py verify
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=tools:/private/tmp/ot2606-duckdb-inspection:/private/tmp/dementiagraph-m1-task008-pyshacl python3 -m unittest discover -s tests -v
```

`OT2606_ARTIFACTS` and `MONDO_PILOT_ARTIFACTS` point to byte-identical external source directories. The tool performs no acquisition, does not regenerate historic artifacts, and reports mismatch rather than repairing it.

## Final integration result

**204 tests passed in 270.795 seconds**, exit status 0: all 182 existing regressions plus 8 source, 6 identity, 6 semantic/structural/reasoning and 2 release tests. Log: `/private/tmp/ot2606-full-regression.log`. The full run includes the original M1 one-violation/eight-warning baseline, all Mondo integrity/relocation safeguards, and the new source-fidelity negative controls. All 78 files tracked at the starting `4f1f28f` baseline remain byte-identical. No raw Parquet or auxiliary scan response bodies are included in Git.

Local implementation history preceding final release: `9402fe2bad91d5de6217576febd791a49d7f2bfe` (source recovery/freeze/extraction/assessment); `03b0c289628a2563a16de250ff267a9548f1f116` (identity/RDF/provenance). The final release commit records validation, packaging and this report. No push.
