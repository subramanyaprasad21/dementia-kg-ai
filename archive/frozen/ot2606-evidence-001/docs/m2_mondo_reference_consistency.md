# M2.5 — bounded Mondo reference-consistency assessment

Baseline: `4d6b189f8a0814d396d4df8216b621f1036b305c`. Owner authorization covers reference consistency of the frozen Mondo subset only. This record is pending owner acceptance.

**Decision: no semantic alignment or source-value transformation is required for this subset.** All five accepted parent assertions resolve both endpoints uniquely against the eight extracted concepts in the same frozen edition. This is exact, source-context-qualified reference lookup, not biomedical equivalence, source-description identity, or an alignment pipeline. The extraction remains the sole intermediate dataset; no aligned records, new identifiers, RDF or mapping repairs are produced.

## Authority and verified inputs

The conceptual contract §§3–4/7 distinguishes referents, versioned descriptions and encounters, and prohibits automatic equality or contextual mapping repair. The approved implementation readiness and G02 mechanics preserve source-scoped references, version context and distinct description/capture identities. The 20/28/39 manifest, Q01–Q07 and R1–R14 remain unchanged.

| Input | Verified SHA-256 |
| --- | --- |
| `extractions/mondo-pilot-001.json` | `43d7537f1f8e14340160d9581e8891db7f2dbe60a903c3910648295aae091882` |
| `assessments/mondo-pilot-001.normalization.json` | `0df85aa9649a0318015732c8fa5bcecb4fd549dc0a67f6c76a8ee795992bafa7` |
| `manifests/mondo-pilot-001.freeze.json` | `b7763d83f41e61c9d8bc617189dc04826609926f83e480289e33f4ac9cc8bb0a` |

Before reference assessment, the existing offline verifier checks the manifest, all raw response digests and capture/description receipts, then compares the extraction with source-derived replay in memory. It does not rewrite any artifact. External raw responses and ledger remain in `/Users/subramanyaprasad/dementia-kg-ai-source-captures/mondo-pilot-001/`; `MONDO_PILOT_ARTIFACTS` supports their existing relocation convention. Missing or altered inputs fail without network fallback. Tests fingerprint the three inputs and all external batch files before and after execution.

Source context remains edition `2026-09-01`, version IRI `http://purl.obolibrary.org/obo/mondo/releases/2026-09-01/mondo-international.owl`, with OLS loaded/updated `2026-09-24T00:09:08.017393439`. Capture timestamps remain distinct. The source load timestamp receives no invented timezone.

## Endpoint results

Each row has one child candidate and one parent candidate. Matching uses both original `obo_id` and original `iri`, verified Mondo authority, frozen edition/service context and record lineage. Labels and xrefs are not lookup keys or fallback evidence.

| Child | Parent | Result |
| --- | --- | --- |
| `MONDO:0010857` | `MONDO:0017160` | Unique child and parent; original direction and lineage preserved |
| `MONDO:0017160` | `MONDO:0017276` | Unique child and parent; original direction and lineage preserved |
| `MONDO:0007088` | `MONDO:0015140` | Unique child and parent; original direction and lineage preserved |
| `MONDO:0015140` | `MONDO:0100087` | Unique child and parent; original direction and lineage preserved |
| `MONDO:0100087` | `MONDO:0004975` | Unique child and parent; original direction and lineage preserved |

The eight unchanged concepts also include `MONDO:0008243`, which is not an endpoint of an accepted pair. No relationship is manufactured to connect it. All six excluded parent-row references retain their raw-provenance-only disposition.

## Identity and provenance boundaries

The external concept ID/IRI is a reference value. An individual-term response describes that concept. A parent-response row supplies an attributed navigation assertion, within a different source description. A capture is the encounter with its response, not the concept or description itself.

For each accepted assertion, `childLineage` resolves to the child term's existing lineage. The assertion's `lineage` preserves its original parent endpoint request URL and row JSON Pointer. The matched parent concept retains its separate individual-term URL and locator. Parent-response and parent-term description IDs and capture IDs are explicitly checked to differ. Complete lineage equality against the independently replayed extraction protects the freeze link, source context, raw digest, source locator, contract and capture times as well as IDs. No identity is minted or merged.

## Bounded verification

Only two files are added: this record and `tests/test_m2_mondo_reference_consistency.py`. The small resolver lives in the test module; it is not a production alignment API. It returns references to existing in-memory objects and writes nothing.

Digest verification and content checks are separate. Negative controls call the resolver directly with mutated in-memory inputs, not mutated files. Expected error reasons ensure lookup failures occur at the applicable checks rather than merely at a checksum gate. Synthetic mutations are not source evidence.

| Test | Evidence |
| --- | --- |
| T01 | Exact approved hashes, offline source/identity replay, original no-transformation decision |
| T02 | All ten endpoint lookups succeed even with reversed concept-list order; original objects and complete lineage remain unchanged |
| T03 | Missing child or parent candidate rejected by lookup |
| T04 | Conflicting identifier/IRI and foreign ontology authority rejected |
| T05 | Identical duplicate and conflicting multiple candidates rejected as ambiguous, never silently deduplicated |
| T06 | Different edition or version IRI rejected before matching |
| T07 | Reversed relation, extra accepted assertion and substitution of an excluded row locator rejected |
| T08 | Altered description/capture IDs, locators or freeze references rejected; term/parent-response lineage collapse rejected |
| T09 | Original attributed xrefs accepted unchanged; same label/xrefs cannot rescue a changed ID/IRI; added xref-derived equivalence claims rejected |

Preserving source annotations does not assert their biomedical truth. The negative checks forbid new project correspondence claims; they do not censor original source annotation text. Existing M2.4 source-value fidelity tests continue to cover annotation mutations, missingness and lexical preservation without duplicating those tests here.

Commands:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p test_m2_mondo_reference_consistency.py -v
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/private/tmp/dementiagraph-m1-task008-pyshacl python3 -m unittest discover -s tests -v
```

## Deferred questions and limits

Open Targets 26.06 remains unavailable through a verified bounded acquisition route. The historical Pick/OMIM:172700 versus FTD assignment and the differing OMIM:600274 assignments still require the original evidence occurrences and source mapping context. Mondo xref text alone cannot adjudicate these assignments, establish biomedical equivalence or justify repairs. Source process/version uncertainty stays unresolved; even later record acquisition would not itself prove clinical correctness.

This assessment establishes within-slice reference consistency only. It does not establish cross-source alignment, independent biomedical validation, historical OLS-response reproduction, full Mondo-release reproduction or full-corpus M2.1/M2.2 completion. The two uninstrumented preparatory lookups remain disclosed in the unchanged freeze package. No acquisition, M2.6 RDF generation or later stage is authorized by this result.

## Final verification results

- **150 tests passed in 201.448 seconds**, exit status 0: all 141 existing regressions plus nine focused M2.5 tests. Full log: `/private/tmp/dementiagraph-mondo-reference-tests.log`.
- All five assertions resolved to unique child and parent concepts. Positive controls preserved source values and separate identities; all documented negative controls rejected their mutations at content-level checks.
- All three approved input digests matched. Offline response-digest and identity replay passed; input and external batch fingerprints remained unchanged.
- No semantic alignment, source-value transformation or duplicate intermediate dataset was necessary. Existing tracked files and the Git index remain unchanged. Only the two files listed above were created; syntax, whitespace and Git diff checks passed.
- No external request, staging, commit, push or M2.6 implementation occurred. The bounded assessment is ready for owner review.
