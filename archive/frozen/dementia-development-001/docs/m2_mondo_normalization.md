# M2.4 — bounded Mondo normalization assessment

Baseline: `72f7b0b5a869450f1c42c0eaf20c931fd6c62519`. The owner authorized assessment and validation of the frozen Mondo subset, not entity alignment or new acquisition.

**Decision: no source-value transformations are required.** The eight concepts and five accepted parent assertions already meet the approved source-preserving representation requirements. The committed extraction remains the sole intermediate dataset; no duplicate normalized dataset is created. This is a technical representation finding, not independent biomedical validation.

## Inputs, authority and deliverables

- Extraction: `extractions/mondo-pilot-001.json`; unchanged SHA-256 `43d7537f1f8e14340160d9581e8891db7f2dbe60a903c3910648295aae091882`.
- Freeze: `manifests/mondo-pilot-001.freeze.json`; unchanged SHA-256 `b7763d83f41e61c9d8bc617189dc04826609926f83e480289e33f4ac9cc8bb0a`.
- Original external artifacts: `/Users/subramanyaprasad/dementia-kg-ai-source-captures/mondo-pilot-001/`.
- Governing rules: conceptual contract §§4/7 (source identity and contextual mapping); approved implementation readiness (source-scoped references); G02 §§3.2–3.3 (exact source spelling, lossless values and versioned provenance). No class/property or ontology change is needed.

Only three files are created:

1. `assessments/mondo-pilot-001.normalization.json`: deterministic decision metadata, no copied concept dataset.
2. `tests/test_m2_mondo_normalization.py`: focused, read-only representation validators and tests.
3. This report.

The decision record uses profile `mondo-normalization-assessment-1`, compact canonical UTF-8 JSON plus LF, and SHA-256 `0df85aa9649a0318015732c8fa5bcecb4fd549dc0a67f6c76a8ee795992bafa7`. It records input hashes, bounded inventory, an empty transformation list, and seven category decisions. Each decision records source path patterns, original/target representation, necessity, justification, loss risk and named test evidence. Path patterns are descriptive, not executable JSON Pointers. No operation timestamp or new source identity is invented.

## Field-by-field assessment

| Category | Original representation inspected | Approved target | Necessary transformation | Justification and information-loss risk | Validation evidence |
| --- | --- | --- | --- | --- | --- |
| Identifiers / IRIs | Eight `MONDO:NNNNNNN` source strings; matching original `http://purl.obolibrary.org/obo/MONDO_NNNNNNN` IRIs; `ontology_name` is `mondo`. | Exact source spelling, consistent authority-qualified reference, source context retained. | None. | Already consistent. Separator/case/scheme changes or leading-zero removal alter provenance-bearing strings; they are not biomedical identity resolution. | T03–04; exact source-field comparison and syntax/IRI checks. |
| Labels | Eight present strings containing original wording. | Original source labels, without synonym substitution or lexical cleanup. | None. | No demonstrated defect. Case folding, trimming or Unicode normalization can erase distinctions. Source fidelity, not typographic preference, governs. | T03, T05; changed case/spacing rejected. |
| Contextual annotations | `annotation` is an object for every concept; descriptions, synonyms, scoped synonyms and xrefs are arrays. | Preserve nesting, qualifications, original values, order and multiplicity as attributed context. | None. | Flattening/deduplication/reordering can discard meaning. Literal mapping annotations do not authorize a global mapping repair or equivalence edge. | T05–06; annotation deletion/replacement, array reversal and invented equivalence rejected. |
| Typed values / missingness | All ten selected fields are present in each concept; typed strings, arrays, objects and booleans. Across concept source values: 70 typed null occurrences and four empty-array occurrences. | Keep present/absent, null, false and empty-value distinctions, with numeric lexemes preserved where applicable. | None. | Extraction already supplies the lossless form. These data need no float/date coercion or fabricated missing values. No top-level absence or numeric value was observed in the concept fields; controls for those cases are explicitly synthetic. | T07–08; positive controls for six distinct missing/empty states; pairwise substitutions and numeric type/precision collapse rejected. |
| Edition / timestamps | Edition `2026-09-01`, recorded version IRI, unqualified OLS loaded/updated `2026-09-24T00:09:08.017393439`; capture times have explicit `+00:00`. | Preserve edition, source load time and capture time separately at original precision. | None. | No timezone evidence permits adding UTC to OLS load strings. Conversion could invent a zone or truncate subsecond precision. | T09; appended `Z`, replaced edition and capture/source-time substitution rejected. |
| Directed parents / exclusions | Five source-qualified child→parent assertions; six separate raw-row references. | Same five directions and row pointers; six extra rows remain raw provenance only. | None. | Reversal, transitive closure, endpoint substitution or excluded-row promotion changes scope. No new parent relation is justified. | T10; reversed endpoints, extra accepted record, changed row pointer and exclusion disposition rejected. |
| Locators / lineage / representation | Manifest/commit/digest links, response digests, description/capture IDs, source URLs and row pointers; deterministic typed intermediate. | Preserve source-scoped lineage and original contracts, including separate child lineage on parent records. | None. | Replacing source identities or dropping context loses reproducibility. Equal strings alone do not justify merging references. | T01–03, T11–12; replay, original byte checks, altered lineage/permissions, omissions and extra records. |

Txx refers to `test_xx_...` in the new test module. The machine-readable record names each relevant test explicitly.

The eight unchanged IDs are `MONDO:0004975`, `MONDO:0017276`, `MONDO:0008243`, `MONDO:0010857`, `MONDO:0017160`, `MONDO:0007088`, `MONDO:0015140`, `MONDO:0100087`.

The five unchanged pairs are `0010857→0017160`, `0017160→0017276`, `0007088→0015140`, `0015140→0100087`, `0100087→0004975` (all MONDO). No excluded raw parent is included in this list.

## Verification method

Before assessing values, the tests pin the committed extraction digest and run the existing offline extractor verifier, which verifies the freeze, original response digests and capture/description identities. The original response files provide the comparison values for every selected field. No historical artifact is regenerated or modified.

Content validation is deliberately separate from the digest gate. In-memory negative mutations pass to the representation validator directly, so rejection is caused by source-value, type, scope, direction or lineage checks—not merely by a changed file checksum. The unchanged extraction is a positive control, and validator execution is checked not to mutate it. Controlled absent/null/empty/numeric examples are test inputs only, not biomedical records.

Validation checks every concept source field and parent endpoint against its actual source object/row. It verifies the five allowed ordered pairs against the frozen manifest, preserves the original exclusion inventory and checks all contextual metadata against the verified extraction. It performs no assignment, repair, canonical disease selection, reference merge or mapping adjudication.

The input artifact and external raw/ledger fingerprints are checked unchanged after the tests. No new standalone normalizer or general processing framework is introduced; the focused validators live in the test module. No dependency was installed and no source was contacted.

Commands:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 tools/m2_mondo_extract.py verify
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p test_m2_mondo_normalization.py -v
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/private/tmp/dementiagraph-m1-task008-pyshacl python3 -m unittest discover -s tests -v
```

As with earlier source-integrity tests, set `MONDO_PILOT_ARTIFACTS` for a relocated byte-identical artifact directory. Missing local artifacts fail explicitly; no network fallback exists.

## Consequences and M2.5 questions

The retained extraction can be consumed unchanged after owner acceptance of this assessment. A future justified derived value must coexist with its original, transformation rule/version and immutable input lineage; this task supplies no such value because none is needed. Keeping existing values is lossless. Potentially information-losing text cleanup, collection deduplication, numeric coercion and timezone inference remain unapproved.

M2.5 must separately determine whether any cross-source correspondence is actually needed and supported; distinguish a matching identifier string from merging source-scoped descriptions; and preserve ambiguous source mapping assignments. In particular, the Pick/OMIM and OMIM:600274 contexts must not be resolved merely from retained xref text. No entity alignment decision is made here. With Open Targets 26.06 still unavailable through a verified bounded route, alignment to those historical evidence records remains blocked. Do not substitute 26.09 or infer the missing mapping process.

Full-corpus M2.1/M2.2 remains incomplete. Historical OLS-response and complete Mondo-release reproduction are not claimed. The two uninstrumented preparatory lookups remain disclosed in the unchanged freeze package. RDF generation and later M2 stages remain deferred. No files are staged, committed or pushed by this task.

## Final verification results

- Complete suite: **141 tests passed in 227.216 seconds**, exit status 0, including all 129 existing regressions and 12 new M2.4 tests. The run finished during the usage interruption and was inspected afterward; it was not represented as an unfinished or newly rerun suite. Log: `/private/tmp/dementiagraph-mondo-normalization-tests.log`.
- The actual eight concepts and five directed parent assertions passed the source-preserving representation checks. Six extra parent rows remain outside the accepted projection. **Zero transformations** were required or performed; no duplicate dataset was created.
- Concrete negative controls rejected identifier/IRI rewrites, label changes, annotation removal/reordering, inferred equivalence, missingness/type/precision collapse, timezone invention, parent reversal, excluded-row promotion, changed lineage/permissions and record omissions/additions. Valid source-preserving controls passed without mutation.
- Original extraction SHA-256 remains `43d7537f1f8e14340160d9581e8891db7f2dbe60a903c3910648295aae091882`; the frozen manifest and original raw/ledger fingerprints remain unchanged. Offline source and identity replay passed.
- All previously tracked files match baseline. Python syntax, new-file whitespace and Git diff checks passed. Only the three listed assessment/test/documentation files are new and unstaged. No entity alignment, RDF generation, acquisition, staging, commit or push occurred.

The bounded M2.4 no-change assessment is ready for owner review. Later M2.5 decisions remain deferred as described above.
