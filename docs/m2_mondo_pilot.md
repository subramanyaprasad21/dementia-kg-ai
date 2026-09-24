# M2.1 — bounded Mondo live-capture pilot

Owner-authorized implementation and acquisition, pending checkpoint review. Baseline: `48f149135177baa245c5b01afb43da0493ec39e8`. M1 remains closed. This pilot does not freeze M2 versions, implement M2.3 extraction/alignment, or build a KG. No M1 file, `m1-id-1` receipt or approved scientific specification is changed.

## Authority and finite scope

The owner authorized the eight concepts and five parent-response requirements below, using edition metadata before and after retrieval. No descendant closure, alternative source, historical-release substitution, or Open Targets evidence acquisition is authorized. The separate profiles below identify capture artifacts and minimum source descriptions; they are not ontology vocabulary additions or biomedical assertions added to the graph.

## Executable minimum contract

Implementation: `tools/m2_mondo_capture.py`; offline controls: `tests/test_m2_mondo_capture.py`. Standard-library Python only. Existing M1 dependencies and implementations remain unchanged.

### Response bytes, request identity and deterministic representation

Requests use GET, `Accept: application/json`, `Accept-Encoding: identity` and `User-Agent: DementiaGraph-Mondo-Pilot/1`. Raw files contain exactly the HTTP entity-body bytes received, after HTTP transfer framing, before UTF-8 decoding or JSON parsing. The server must honour identity content encoding; an unexpected compressed response stops before body reading. The successful batch used identity encoding throughout. These are body digests, not TLS-packet or HTTP-framing digests.

The request receipt has exactly `method`, `url`, `headers`, `bodySha256`. Its SHA-256 covers canonical bytes of this exact application request descriptor; the GET body digest is SHA-256 of empty bytes. Automatically supplied HTTP transport headers/framing are not claimed to be captured wire bytes. Response headers, including dates, caching headers and content lengths when supplied, are preserved in their observed ordered list in each capture receipt. Raw body SHA-256 is independent of the JSON projection.

Canonical receipt serialization uses the RFC 8785 string/null/container subset: UTF-16 object-key ordering, compact UTF-8 JSON, no Unicode normalization. Every upstream JSON value in a projected field is losslessly typed before canonicalization:

- String: `{type: string, value: <exact string>}`.
- Number: `{type: number, lexeme: <original JSON number token>}`. `1`, `1.0`, and `1e0` intentionally remain distinct. No float conversion.
- Boolean: `{type: boolean, lexeme: true|false}` with the lexeme stored as a string.
- Null: `{type: null}`.
- Array/object: `{type: array|object, value: <recursively typed content>}`.

A selected field is `{state: present, value: <typed value>}` or `{state: absent}`. Thus absent, JSON null, empty string, empty array and empty object remain distinct. Unselected fields are outside this projection, not missing or biologically negative. Required edition/IRI/identifier/extent information cannot be supplied by missingness; its absence stops acceptance. Duplicate JSON keys, non-finite numbers and invalid Unicode cannot produce an accepted description. All arrays preserve order and multiplicity; no array is implicitly a set.

### `m2-capture-1`

Exact receipt keys: `profile`, `execution`, `slot`, `request`, `requestSha256`, `started`, `ended`, `status`, `responseHeaders`, `rawSha256`, `receivedBytes`, `complete`, `error`, `license`, `sourceContext`.

Execution is the exclusive batch directory name plus `/` and a one-based attempt ordinal. Creating an existing directory fails; the CLI has no resume/reset or automatic retry. Required successful values must be present. Initially unavailable response/context/error values are explicit null, and failed attempts remain recorded. `sourceContext` has exactly `edition`, `versionIri`, `loaded`, `updated`; it records actual metadata, not a guessed edition from capture time. `license` has `identifier`, `url`, `source`, `attribution`, `changes`.

Identifier: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/m2-capture-1/` plus full SHA-256 of the canonical receipt. A new encounter has a new execution/time and capture identity even if content is unchanged. New capture is not new independent evidence. Started/ended are actual UTC times; source timestamps retain their exact provider lexical values.

### `m2-source-description-1`

Exact receipt keys: `profile`, `provider`, `dataset`, `edition`, `versionIri`, `locator`, `projectionVersion`, `payloadSha256`.

Fixed values: provider `EMBL-EBI-OLS`; dataset `Mondo`; projection `mondo-ols-minimum-1`. Identifier uses the same administrative base plus `m2-source-description-1/` and full canonical receipt SHA-256. Content digest supplies the local description revision; there is no invented upstream record revision. Capture timestamps, execution, HTTP headers and response links do not enter term/parent description identity. Service-load metadata remains linked in the capture context; it is also content in the metadata description.

Exact projections (field paths refer to OLS JSON):

| Kind | Locator and fixed projection |
| --- | --- |
| Edition metadata | Locator `ontology-metadata`; `/ontologyId`, `/version`, `/loaded`, `/updated`, `/status`, `/config`. `/config/versionIri` is mandatory for edition verification. Both before/after captures reuse this locator. |
| Individual term | Locator `term-<seven digits>`; `/iri`, `/obo_id`, `/label`, `/description`, `/synonyms`, `/annotation`, `/obo_synonym`, `/obo_xref`, `/is_obsolete`, `/ontology_name`. Each field has explicit presence/type wrappers. Unknown fields and `/_links` remain in raw bytes but are excluded from this projection. |
| Parents | Locator `parents-<child digits>`; rows at `/_embedded/terms/*` restricted to the eight allowed `obo_id` values, projected with the same term field list. Payload keys `child`, `parents`, `excludedRows`, `extent`. Entire raw response remains retained. No out-of-scope concept becomes a projected parent resource. |

An individual term must match both requested `obo_id` and full IRI, have ontology name `mondo`, a label, and explicit `is_obsolete: false`. Parent completeness requires `/page/number = 0`, `/page/totalPages` no greater than one, `/page/totalElements` matching the received row count, and no `/_links/next`. Otherwise this finite implementation stops for review rather than following additional pages automatically. The expected parent must actually occur with matching identifier/IRI, Mondo ownership and non-obsolete status. OLS `/parents` response context establishes the source-reported parent navigation assertion; this does not claim an independently inspected OWL axiom or biomedical truth.

Payload, edition, locator or projection changes produce new immutable description identities. Same description through a new capture reuses its identity. A conflicting receipt/payload under an existing description digest stops rather than overwrites. Replay rehashes original raw bytes and request receipts, reparses, reprojects and regenerates both identity families without network access or new execution allocation. The retained ledger is the replay input; no audit-transcription receipt supplies live data.

## Safeguards and storage

100 requests / 10,485,760 uncompressed body bytes per batch; every attempt is recorded before opening the connection. Error/redirect bodies count. Automatic redirects and retries are disabled: their responses are retained and cause a stop. No redirect follow-up is issued. A byte limit is enforced during reading; a boundary response is marked incomplete. A request limit prevents a further request. Non-200, bad JSON, missing fields, mismatching terms/parents, pagination, content-length mismatch, or changed edition/load metadata stops the batch. A stopped batch remains unusable as a complete pilot.

The operator verified Mondo's [CC BY 4.0 declaration](https://mondo.monarchinitiative.org/#license) before capture. The finite pilot uses that permission, preserves attribution and identifies the projection changes. This is not a general-purpose licence detector for other providers. New or conflicting retention conditions require review. No redistribution is performed.

Raw responses and the acquisition ledger are stored outside Git at:

`/Users/subramanyaprasad/dementia-kg-ai-source-captures/mondo-pilot-001/`

Retain this directory unchanged for replay; keep local backed-up copies under the same permission and attribution metadata. It is not a temporary-directory dependency. Raw source bodies and projected payloads in the ledger must not be added to this repository. This report contains technical receipts/results only. The implementation's output path guard rejects repository-local raw storage.

The capture ledger includes all request/response hashes, timestamps, identities, source context, projected payloads and raw filenames. No source artifact has been version-frozen for M2.2. A provider-declared edition checked before/after is evidence of service context, not byte-for-byte reproduction of the released ontology file or the earlier M1 OLS encounter.

## Open Targets 26.06 blocker

Local metadata-access readiness check: no `gcloud` or `bq` executable, no available `google` authentication package, no `GOOGLE_APPLICATION_CREDENTIALS` configuration, and no standard application-default credential file. Only presence indicators were inspected; no credential file content, account token or secret was read or exposed. No credential request, authentication initiation, BigQuery query or cloud resource creation occurred.

Therefore authenticated metadata-only access was unavailable in the inspected environment. A retained 26.06 BigQuery dataset remains **NOT YET VERIFIED**. Previous unauthenticated metadata access returned 401; current GraphQL remains unsuitable for historical 26.06 evidence. No archive partition was acquired.

Unsent provider inquiry for separate owner authorization:

> Does Open Targets retain an officially supported BigQuery dataset or record-level service for Platform release 26.06? We need a bounded export of eight already identified evidence IDs: two Europe PMC, four Genomics England and two clinical-precedence records. Please identify the immutable dataset/table or endpoint, release-verification metadata, required access and any query/export conditions. If only bulk Parquet is retained, can the provider supply an official eight-record export with release and source provenance? We will supply the eight exact IDs from our existing allowlist if this route is available. We cannot substitute current release records.

## Verification commands

Run from the repository root; capture command is historical documentation, **not permission to rerun**:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 tools/m2_mondo_capture.py capture /Users/subramanyaprasad/dementia-kg-ai-source-captures/mondo-pilot-001
PYTHONDONTWRITEBYTECODE=1 python3 tools/m2_mondo_capture.py replay /Users/subramanyaprasad/dementia-kg-ai-source-captures/mondo-pilot-001
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/private/tmp/dementiagraph-m1-task008-pyshacl python3 -m unittest discover -s tests -v
 git diff --check
 git diff --exit-code 48f149135177baa245c5b01afb43da0493ec39e8 -- .
```

The last command protects every previously tracked file; new authorized files are reviewed separately. No packages were installed.

## Actual capture results

Batch `mondo-pilot-001`: **15 requests, 130,541 body bytes**, all HTTP 200, no retry, redirect or truncation. Started `2026-09-24T12:39:57.540500+00:00`; ended `2026-09-24T12:40:08.772988+00:00`.

Edition `2026-09-01`; version IRI `http://purl.obolibrary.org/obo/mondo/releases/2026-09-01/mondo-international.owl`. Both loaded and updated: `2026-09-24T00:09:08.017393439` before and after.

Eight terms retrieved and matched:

| Identifier | Observed label |
| --- | --- |
| MONDO:0004975 | Alzheimer disease |
| MONDO:0017276 | frontotemporal dementia |
| MONDO:0008243 | Pick disease |
| MONDO:0010857 | semantic dementia |
| MONDO:0017160 | behavioral variant of frontotemporal dementia |
| MONDO:0007088 | Alzheimer disease type 1 |
| MONDO:0015140 | early-onset autosomal dominant Alzheimer disease |
| MONDO:0100087 | familial Alzheimer disease |

Five actual parent checks:

| Child | Expected parent present | Raw parent rows | In-scope rows |
| --- | --- | --- | --- |
| MONDO:0010857 | MONDO:0017160 — yes | 2 | 1 |
| MONDO:0017160 | MONDO:0017276 — yes | 2 | 1 |
| MONDO:0007088 | MONDO:0015140 — yes | 2 | 1 |
| MONDO:0015140 | MONDO:0100087 — yes | 2 | 1 |
| MONDO:0100087 | MONDO:0004975 — yes | 3 | 1 |

All five assertions agree with the paths in M1 source audit §T4-H. The eight labels agree with the audited concept labels. Six additional parent rows remain only in raw provenance, with no expanded research projection. The service-load time is new; raw response equivalence to historical M1 observations cannot be established because those response bodies were not archived. Two bounded xref checks also agree: Pick disease / OMIM:172700 retains description `MONDO:equivalentTo`; semantic dementia / OMIM:600274 retains `Orphanet:100069`. These do not resolve the OT mapping ambiguity. Synonym/xref/annotation inventories were not exhaustively adjudicated against historical observations. This is a new capture, not historical reproduction.

### Complete identity inventory

Full identity IRI prefix is the project `/id/` base followed by `m2-capture-1/` or `m2-source-description-1/`. The following are the complete SHA-256 suffixes; no identity is truncated. There are **15 capture identities and 14 distinct source-description identities**: identical before/after metadata reuses its description.

| Slot | Capture SHA-256 | Source-description SHA-256 |
| --- | --- | --- |
| metadata-before | `f9fda363b357424051dba5ec17b66f515ab232020a9d96c7b15dd107a9a9a310` | `e059c94f5a96c814d7bced2808acb1f0a13116dfa66e78da450d2a75940cb370` |
| term-0004975 | `671ae563e5d58290aedeea605e5a5ab8099748ac579a42c97506cbdf73a94cb0` | `ac7891d0eaa2c3ea0a0151e7bee4975547e2a86ab623122a668927d5592dcfda` |
| term-0017276 | `7b58d86145772df339142f1a3ea64f8897474c40e817cc1bdcc485936bf1be16` | `0d2b3e51071f3a4a55f28ad27a75beb32783df9912fc04987046922fb65823a0` |
| term-0008243 | `4bd7def3a15387f9e85554e77725076a1e5341c24ead3c32950e9ca6d4d35d71` | `73c977941a154047d77e18aeb3216d5bf8a400d7c267eab0e1a231c8d9a0f45c` |
| term-0010857 | `6c7903d7217f5759f797821d266bd22ace9052c412c726f360d69459a80cc12a` | `752891d19b4838df23ce669537aaaf23f891c270c7781ea0493adfcacd8ab118` |
| term-0017160 | `6a332830a2c8c872137fc31082db220f7c09e14c945a7068bdc4d03ce1028e65` | `998e808199226fcd021eecd0d64ad5e61319315679d385d268a65ac349add906` |
| term-0007088 | `ec4158167351df7c7bba57e464f174afbd22342f37ac0cd5d352542f0085257a` | `9bef377f5a513436743b9a7134830e6be7e0e42e20f2b0597d2d3f1fbdcfc32b` |
| term-0015140 | `2946b4530c95a26787037d76171b84f96369e4f6a6520384860243f377d49623` | `e191d85b0e4a86818c06a8c364f23063d39fdc196deefac0b6055bf1ad932ea3` |
| term-0100087 | `08bedac785d1e42a09a9cb5eb21b38b4f9736d2649c9976318ee79f92ba78fe7` | `e8697f8970426e5d53f3a90971ef8af7ef7b7a1d3fde049e3f8121fb960bd6ae` |
| parents-0010857 | `572cea7916000f7d094c5b6ca09ca3c0953bdf69b97de51f8bda054b15623e57` | `baf29ead4ab38b5353ac2b491fe761ce03d95aa83c660e707c7ba89c5f47929b` |
| parents-0017160 | `7601fe8f6d8c0c1c5944be92c632b3ce0317f3a1fc2a8db508da8cf5985816e3` | `70de222014b50a4b41d236761346f9964451a8bfbcac0cd82d15fc5029ad614c` |
| parents-0007088 | `0b65f4fcb8dd1713cd6e09c9ad2e7336723f8c05577a6324a0bb8c21f362cd84` | `dacb0cc6a3190d5cab05a84f933c1f8605c8f3b888e30a712ca04262d96be3de` |
| parents-0015140 | `768c899613aa14467091acc51c079cb233bfecc1c4cd8c1e4dd2e44437696d67` | `82a5c48f883323120b180ea460f26d92f365e0af886c7414a3f24829b8bb0a2c` |
| parents-0100087 | `7d464ed0daf1350e97e77a5d25bc13647561e16293270404db0637ef6a9230bf` | `591d8091c79dd1155c1dfe700eb34acc0309ed184ce897fb2077dcd25cc17145` |
| metadata-after | `af0a0439f15ab7a3b6bcc13ce036012b893a2bd6164099ed57d8568862e82588` | `e059c94f5a96c814d7bced2808acb1f0a13116dfa66e78da450d2a75940cb370` |

Ledger SHA-256: `6238dc242bf3207999b379da2d491d9c711e92aca36a473d8f37e76c7ac1792e`. This checksum identifies the local acquisition receipt file, not an M2 release freeze.

## Verification and accounting limitations

Offline replay was run repeatedly against the preserved artifacts and reproduced every request/raw digest, capture identity, source-description identity, projection and parent result. Temporary copies were used to append a byte to a raw response and to corrupt a description ID; both mutations were rejected. Temporary copies were removed. Original ledger SHA-256 remained unchanged.

The 14 new automated tests cover canonical ordering, numeric lexical precision, type separation, missing/empty/null distinctions, duplicate-key rejection, ordered-array preservation, replay/revision/capture identity distinctions, the finite plan, edition gating, parent scope and completeness, error-body accounting, byte/request limits, truncation/compression rejection, redirect stopping, exclusive batch creation and repository-local raw-storage rejection. Synthetic controls are not additional biomedical source evidence.

**Accounting boundary limitation:** before the instrumented batch, two preparatory web-tool opens consulted the licence page and OLS metadata. That tool did not expose exact raw response bytes or underlying request accounting. These lookups are not reconstructed as captured artifacts. Thus 15 requests / 130,541 bytes is the exact instrumented capture-batch total, not a proven total for every network action in this turn. There were also two additional web-tool lookup initiations; their exact transport totals are unavailable. The pilot itself is below both G05 limits, but whole-turn byte-budget verification cannot be claimed. Future acquisition-related metadata and permission fetches should use the same metered transport. No further requests or recapture are performed to conceal or repair this accounting gap. Owner review must distinguish successful artifact replay from this procedural limitation.

Remaining boundaries: no independent biomedical adjudication; no historical OLS-response reproduction; provider edition attribution rather than full ontology artifact equality; no exhaustive historic annotation comparison; Open Targets historical access unresolved; no M2.2 or later implementation.

### Final verification result

Complete suite: **105 tests passed in 407.650 seconds** (all 91 M1 regressions plus 14 new contract/transport controls). Exit status 0. Log: `/private/tmp/dementiagraph-mondo-pilot-tests.log` (diagnostic log, not a source artifact). Existing SHACL baseline/positive-control and reasoning/semantic acceptance regression expectations remain intact, including the historical completeness defect.

Repeated live-artifact offline replay passed; both additional mutation probes rejected corruption. Python AST parsing and explicit whitespace checks passed for the three new files. `git diff --check`, `git diff --cached --check`, and the complete tracked-file comparison against baseline passed. The index is unchanged and no tracked file differs from baseline; only the three authorized-purpose pilot files are untracked. Nothing is staged, committed or pushed. The original ontology, 20/28/39 manifest, fixtures, receipts, ledger, M1 closure record and approved design documents remain byte-for-byte unchanged.

Successful replay and bounded response verification are ready for owner review. Whole-turn network accounting remains the explicit procedural limitation above; no blanket compliance or wider M2 readiness is claimed.
