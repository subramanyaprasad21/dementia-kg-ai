# M2.2 — offline Mondo subset freeze

Owner authorized this offline package from baseline `699f5347d56fb050a1dd58a1fd72121f8e5b0a93`. Implementation is complete for review; this document does not declare the full M2.1 corpus acquired or authorize M2.3. No source was acquired, repaired, replaced or enriched in this task. M0/M1 closure and the committed Mondo pilot remain unchanged.

## Frozen reference

Manifest: [`manifests/mondo-pilot-001.freeze.json`](../manifests/mondo-pilot-001.freeze.json).

- Profile: `m2-mondo-slice-freeze-1`; slice/batch: `mondo-pilot-001`.
- Manifest SHA-256: `b7763d83f41e61c9d8bc617189dc04826609926f83e480289e33f4ac9cc8bb0a`.
- Manifest length: 44,287 bytes.
- Acquisition ledger SHA-256: `6238dc242bf3207999b379da2d491d9c711e92aca36a473d8f37e76c7ac1792e`.
- Ledger length: 286,212 bytes; raw response bodies: 130,541 bytes across 15 files.
- Required external artifact inventory: 16 files (15 responses plus `ledger.json`), totalling 416,753 bytes.

The manifest is a metadata reference package, not a copy of the source corpus. No response bodies or projected source payloads are added to Git. Capture receipts contain existing request/response metadata, source context and permissions; source-description receipts contain content digests. Source payloads remain in the external acquisition ledger and raw artifacts.

The trusted manifest digest above and its matching test anchor make replacement detectable. Once checkpointed, Git history supplies the review reference. This is content-addressed integrity and a no-overwrite policy, not a digital signature or physically write-protected storage. Any approved revision must be a new explicitly reviewed package; do not regenerate over this manifest to make changed artifacts pass.

## Exact source inventory and context

Provider: EMBL-EBI OLS; ontology: Mondo Disease Ontology. Declared edition: **2026-09-01**.

Version IRI: `http://purl.obolibrary.org/obo/mondo/releases/2026-09-01/mondo-international.owl`.

OLS `loaded` and `updated`: **2026-09-24T00:09:08.017393439**, identical before/after acquisition. Source timestamps retain the provider's original lexical form; no timezone is invented for those source strings.

Capture period: **2026-09-24T12:39:57.540500+00:00** to **2026-09-24T12:40:08.772988+00:00**. Each of the 15 receipts retains its own request start/end time. Capture time, service-load time and ontology edition remain separate.

The frozen eight-term allowlist is exactly:

- `MONDO:0004975` — Alzheimer disease.
- `MONDO:0017276` — frontotemporal dementia.
- `MONDO:0008243` — Pick disease.
- `MONDO:0010857` — semantic dementia.
- `MONDO:0017160` — behavioral variant of frontotemporal dementia.
- `MONDO:0007088` — Alzheimer disease type 1.
- `MONDO:0015140` — early-onset autosomal dominant Alzheimer disease.
- `MONDO:0100087` — familial Alzheimer disease.

The five source-reported parent assertions and raw JSON row positions are:

| Child | Accepted parent | Accepted row index | Excluded raw row indices |
| --- | --- | --- | --- |
| MONDO:0010857 | MONDO:0017160 | 1 | 0 |
| MONDO:0017160 | MONDO:0017276 | 1 | 0 |
| MONDO:0007088 | MONDO:0015140 | 0 | 1 |
| MONDO:0015140 | MONDO:0100087 | 1 | 0 |
| MONDO:0100087 | MONDO:0004975 | 0 | 1, 2 |

Indices are zero-based at `/_embedded/terms/<index>` in the corresponding `parents-<child digits>` response. The manifest records these full JSON pointers and links each response slot to its immutable body digest and capture/description receipts. The six excluded row occurrences are preserved only as raw provenance; they are not six new projected concepts or accepted relationships. No unrequested parent relationship, path closure or OWL entailment is inferred.

All eight terms and five assertions are rechecked against the actual retained OLS JSON bodies, not HEAD responses, audit prose or manually supplied manifest labels. This checks source-reported OLS navigation, not an independent inspection of an OWL release file.

## Manifest structure and deterministic serialization

The top-level keys are:

- `profile`, `sliceId`, `scope`, `baselineCommit`, `provider`, `ontology`.
- `sourceContext`, `capturePeriod`.
- `artifactRootHint`, `ledger`.
- `contracts`, `terms`, `parentAssertions`, `responses`, `inventory`.
- `permissions`, `retention`, `limitations`.

Each response entry has `slot`, relative `artifact` basename, byte length and SHA-256, full `captureId` and `captureReceipt`, full `descriptionId` and `descriptionReceipt`. There are **15 distinct capture identities and 14 distinct description identities**. Before/after metadata captures share the same source-description identity without collapsing their distinct encounters.

`contracts` pins `m2-capture-1`, `m2-source-description-1`, projection `mondo-ols-minimum-1`, and the hashes of the three baseline pilot files. `m1-id-1` is untouched. The new freeze profile identifies an offline packaging convention, not an ontology term, new capture or new biomedical source record.

Serialization reuses the existing string/null/container canonicalizer (RFC 8785 subset with UTF-16 key order), UTF-8, exactly one trailing LF. Counts and byte lengths are decimal strings. Arrays use the fixed acquisition/allowlist order; row pointers retain source response order. No current timestamp, machine-dependent destination path or random value enters generation. Duplicate keys and noncanonical serialization are rejected. Rebuilding from a relocated byte-identical artifact directory yields the same manifest bytes; the original root is retained only as a provenance/location hint.

`tools/m2_mondo_freeze.py` has only offline `build` and `verify` commands. Build checks the fixed historical ledger digest before any generation and refuses to overwrite an existing destination. Verify regenerates the expected manifest from the pinned artifacts and capture replay and requires byte equality. A changed ledger is not accepted merely because its internally supplied hashes have been updated. No repair, network fallback, auto-download or latest-release lookup exists.

## Permissions, retention and portability

The existing permission receipt is preserved: **CC-BY-4.0**, `https://creativecommons.org/licenses/by/4.0/`, with the recorded Mondo licence locator, attribution to Mondo contributors and EMBL-EBI OLS, and disclosure that raw bodies are unchanged while the projection excludes transport links/out-of-scope parents. Permission was checked during the approved pilot; this offline task neither rechecks a website nor claims a captured licence-page artifact exists.

Local artifacts remain unchanged at:

`/Users/subramanyaprasad/dementia-kg-ai-source-captures/mondo-pilot-001/`

Retain all 16 files, including the ledger, together. Supply a reviewer with a permitted local copy outside Git, preserving basenames and bytes and carrying the attribution/limitations. `--artifacts` can point to that copy without changing the frozen manifest. This task did not create a backup or assert remote availability. Hashes cannot recover a lost artifact. Without the external files, a reviewer can inspect metadata but cannot reproduce source-body verification; the verifier fails explicitly, with no network recovery.

The freeze tests likewise require the original directory or `MONDO_PILOT_ARTIFACTS` pointing to a preserved copy. Missing artifacts fail rather than silently skip the integration checks. Existing M1/M2.1 tests remain unchanged.

## Verification commands

From the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 tools/m2_mondo_freeze.py verify
PYTHONDONTWRITEBYTECODE=1 python3 tools/m2_mondo_freeze.py verify --artifacts /path/to/local/copy
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p test_m2_mondo_freeze.py -v
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/private/tmp/dementiagraph-m1-task008-pyshacl python3 -m unittest discover -s tests -v
```

For a relocated full-suite run, set `MONDO_PILOT_ARTIFACTS` to that copy. No new dependency is required. The original manifest was generated with `python3 tools/m2_mondo_freeze.py build`; rerunning this command against its existing path must fail, not rewrite the freeze.

The 12 new checks cover: repeated canonical generation and offline replay; exact independent allowlists and accepted/excluded row positions; raw hashes and 15/14 identity links; edition/time/permission preservation; missing bodies; changed body bytes; changed ledger/permissions; changed manifest identity/permissions; scope expansion or row reclassification; artifact relocation; noncanonical/duplicate-key manifests; and CLI no-overwrite behavior. Network connection attempts are blocked during in-process integration tests. Negative tests use disposable copies, never mutate the originals, and verify the original artifact fingerprints afterward.

## Explicit limits and remaining gates

- **Open Targets 26.06 remains blocked/unverified** for bounded historical record access. No current-release substitution, query, provider contact or archive acquisition occurred.
- **Full M2.1 acquisition remains incomplete.** This package freezes only the already approved Mondo OLS slice, not a complete multi-source corpus.
- This is a **new OLS capture of a declared edition**, not reproduction of historical M1 audit responses. Earlier audit observations remain unchanged.
- No complete Mondo ontology release file was acquired or reproduced. Before/after edition agreement does not establish byte equality to the full ontology release or transactional server snapshot isolation.
- The **two uninstrumented preparatory lookups remain disclosed** in the manifest and pilot report. The known 15 requests / 130,541 bytes cover only the instrumented batch; whole-turn historical traffic totals remain unknown. This offline freeze does not retroactively fix that limitation.
- No new source assertions, M2.3 extraction, normalization, alignment, RDF generation, downstream KG release or biomedical validation is claimed.
- No files have been staged, committed or pushed by this task. Owner checkpoint review remains pending.

## Final verification results

- Complete suite: **117 tests passed in 198.030 seconds**, exit status 0: all 105 M1/M2.1 regressions plus 12 new freeze tests. No skipped integration checks. Diagnostic log: `/private/tmp/dementiagraph-mondo-freeze-tests.log`.
- Offline verifier passed with manifest SHA-256 `b7763d83f41e61c9d8bc617189dc04826609926f83e480289e33f4ac9cc8bb0a`; all source body hashes and capture/description identities reproduce. Exact inventory is 8 terms, 5 accepted parent rows, 6 excluded raw row occurrences, 15 captures and 14 distinct descriptions.
- Negative controls rejected missing/changed bodies, changed ledger permissions, changed manifest identities/permissions, expanded terms/changed parent scope, erased exclusion pointers, noncanonical/duplicate-key manifests and overwriting the existing manifest. Relocated byte-identical artifacts remained valid.
- Original raw artifacts and ledger fingerprints were unchanged after verification and mutation controls. No discrepancy required repair. No network acquisition or provider inquiry occurred.
- Python syntax, explicit new-file whitespace checks, `git diff --check`, `git diff --cached --check`, and byte-for-byte tracked-file comparison against baseline passed. No existing tracked file changed; M1 ontology/manifest/receipts/fixtures and M2.1 implementation/report remain intact.
- Exactly four files are new and unstaged: this document, the JSON freeze manifest, the offline freeze tool and its tests. No raw source body is included. Nothing is committed or pushed.
