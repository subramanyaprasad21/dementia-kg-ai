# M2.3 — offline extraction of the frozen Mondo subset

Owner-authorized from `cc2da11315710b436472305a86fbb898408c5d81`. This is a source-faithful JSON intermediate, ready for implementation-result review after verification. It is not normalization, entity alignment, RDF generation, biomedical validation or full-corpus extraction. M0/M1 and the M2.1/M2.2 source records remain unchanged.

## Inputs and verification gate

Frozen input: `manifests/mondo-pilot-001.freeze.json`, SHA-256:

`b7763d83f41e61c9d8bc617189dc04826609926f83e480289e33f4ac9cc8bb0a`

Artifact directory: `/Users/subramanyaprasad/dementia-kg-ai-source-captures/mondo-pilot-001/` (15 original raw responses and the acquisition ledger). Declared Mondo edition is **2026-09-01**; version IRI is `http://purl.obolibrary.org/obo/mondo/releases/2026-09-01/mondo-international.owl`. OLS loaded/updated values remain `2026-09-24T00:09:08.017393439`. Source edition, load timestamps and capture timestamps remain separate.

Before creating any output record, the extractor checks the exact approved manifest digest, invokes the offline freeze verifier, verifies the pinned ledger and all response digests, and replays all 15 capture and 14 distinct source-description identities. It then reads and rehashes the exact bytes used for extraction. A missing/altered/unverifiable input stops processing; there is no manifest regeneration, silent repair, source substitution or network fallback. The output is computed completely before an output file is opened. Build uses exclusive creation and cannot overwrite an existing output artifact.

## Output and contract

Artifact: [`extractions/mondo-pilot-001.json`](../extractions/mondo-pilot-001.json).

- Extraction contract: `mondo-extraction-1`.
- Artifact size: **80,478 bytes**.
- SHA-256: `43d7537f1f8e14340160d9581e8891db7f2dbe60a903c3910648295aae091882`.
- Inventory: **8 concept records, 5 immediate-parent assertion records**.
- Separate exclusion inventory: **6 raw-row provenance references**, not accepted assertion records.
- Upstream projection: unchanged `mondo-ols-minimum-1`.

The artifact is deterministic compact UTF-8 JSON using the existing string/null/container JCS subset plus one trailing LF. It has no generation clock, random values or environment-dependent output paths. Arrays preserve the frozen allowlist and source ordering. Counts are strings. No new ontology vocabulary, RDF statements or biomedical identity IRIs are minted; `recordKey` and `kind` are intermediate-format fields only.

Top-level keys: `contract`, `freeze`, `sourceContext`, `projection`, `permissions`, `concepts`, `parentAssertions`, `excludedRawRows`, `inventory`, `interpretation`.

### Concepts and contextual annotations

Each concept carries `recordKey`, `kind`, `assertionOrigin`, `projectionRole`, `sourceValues`, and `lineage`. The exact fixed source paths are:

`/iri`, `/obo_id`, `/label`, `/description`, `/synonyms`, `/annotation`, `/obo_synonym`, `/obo_xref`, `/is_obsolete`, `/ontology_name`.

These are the fields already covered by the frozen projection, not a newly expanded annotation inventory. Values are read directly from each individual-term body, not supplied by audit prose or inferred from a normalized identifier. Relevant source-provided definitions, synonyms, scoped xrefs and annotations are preserved as nested source values. Referenced identifiers inside annotations remain attributed text; they do not create additional extracted concept records, resolved mappings or equivalence assertions. Other source fields remain accessible through the raw artifact, but are not silently added to this contract.

Presence/type wrappers follow the approved capture convention: absent field versus present null, empty string, empty list/object, strings, booleans, and exact numeric lexemes remain distinct. Source spelling, Unicode, punctuation, identifier separators, array order and duplicate values are preserved. No trimming, case folding, colon/underscore substitution, sorting/deduplication of arrays or biomedical interpretation occurs.

The exact concept inventory and original labels are:

| Source identifier | Original label |
| --- | --- |
| MONDO:0004975 | Alzheimer disease |
| MONDO:0017276 | frontotemporal dementia |
| MONDO:0008243 | Pick disease |
| MONDO:0010857 | semantic dementia |
| MONDO:0017160 | behavioral variant of frontotemporal dementia |
| MONDO:0007088 | Alzheimer disease type 1 |
| MONDO:0015140 | early-onset autosomal dominant Alzheimer disease |
| MONDO:0100087 | familial Alzheimer disease |

### Accepted parents versus excluded raw information

Each accepted assertion carries child `obo_id`, `iri`, `label` from the verified child term body and parent `obo_id`, `iri`, `label`, `is_obsolete`, `ontology_name` from the exact accepted parent-response row. Both sides have source lineage. The relationship is the source-reported immediate-parent navigation of the captured OLS endpoint, not inferred closure or a new independent OWL/biomedical assertion.

| Child | Accepted parent | Accepted source row | Excluded source rows |
| --- | --- | --- | --- |
| MONDO:0010857 | MONDO:0017160 | 1 | 0 |
| MONDO:0017160 | MONDO:0017276 | 1 | 0 |
| MONDO:0007088 | MONDO:0015140 | 0 | 1 |
| MONDO:0015140 | MONDO:0100087 | 1 | 0 |
| MONDO:0100087 | MONDO:0004975 | 0 | 1, 2 |

Indices are zero-based under `/_embedded/terms/` in the appropriate parent response. Exclusion entries contain only `disposition: raw-provenance-only` and lineage; they carry no promoted child/parent values, labels or relationships. Their response-level description identity identifies the approved projected response; the raw digest and pointer locate the excluded content outside that projection. They are not misrepresented as content of an accepted atomic parent description.

`assertionOrigin` records source attribution; `projectionRole`, selected row pointers and the finite output inventory express project-approved selection. These control fields are project metadata, not claims that the provider issued our research-scope decisions.

### Lineage and identity

Every concept, accepted parent and exclusion reference carries:

- Frozen manifest path, exact SHA-256 and freeze checkpoint commit.
- Extraction contract/version.
- Original response slot, raw-artifact basename and SHA-256.
- Existing full source-description identity and capture identity.
- Exact original request URL and JSON Pointer locator (empty pointer means the whole term object).
- Original capture start/end timestamps.

Each parent additionally has `childLineage`, because the child lexical values come from the individual-term response while the accepted parent row comes from the parent endpoint. No existing identities are replaced by extraction identities. The artifact checksum identifies the whole intermediate; a new file does not manufacture independent evidence.

Replaying extraction from the same verified artifacts reproduces the exact output bytes. `verify` compares the entire stored intermediate against recomputation, rejecting additional records, changed labels/IDs, altered lineage, inferred equivalence fields and silent omissions. It does not merely count records. Relocated byte-identical artifacts produce identical output. There is no network call or new source capture.

## Permissions and storage

The existing CC-BY-4.0 permission/attribution receipt is copied unchanged, including its source locator and description of projection changes. The extraction is a derived, attributed subset; the original raw material remains outside Git and unchanged. No new permission verification is claimed. This task creates the intermediate locally; it does not publish or push it. Reviewers need the separately retained source directory for full replay; hashes alone cannot recover missing bodies.

## Implementation and commands

New tool: `tools/m2_mondo_extract.py`; tests: `tests/test_m2_mondo_extract.py`. Standard library plus unchanged capture/freeze helpers; no packages installed.

```sh
PYTHONDONTWRITEBYTECODE=1 python3 tools/m2_mondo_extract.py verify
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p test_m2_mondo_extract.py -v
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/private/tmp/dementiagraph-m1-task008-pyshacl python3 -m unittest discover -s tests -v
```

For relocation, pass `--artifacts /path/to/preserved/copy`; tests accept `MONDO_PILOT_ARTIFACTS`. Missing external artifacts fail explicitly. The original artifact was created with the offline `build` command; repeating build against an existing output fails rather than overwriting it. No live OLS call is needed.

## Test coverage and interpretation limits

The 12 new tests check independent expected identifiers/labels and parent pairs; separation of the six raw exclusions; pinned output digest and repeated replay; all original context fields and source spelling; exact description/capture lineage; preserved mapping annotations without equivalence promotion; changed/missing raw input rejection; changed-manifest rejection; extra/inferred output rejection; lineage/permission tampering; relocation; and silent omission detection. Mutations use temporary copies. Original artifact fingerprints are checked after the tests. Network connections are blocked in the new in-process tests.

Pick disease's OMIM:172700 annotation remains literal source context `MONDO:equivalentTo`; semantic dementia's OMIM:600274 description remains `Orphanet:100069`. Neither is converted into a project equivalence edge or used to repair Open Targets mapping. No broader annotation correctness or biomedical truth is established by source fidelity.

Open Targets 26.06 remains blocked; full M2.1 acquisition and full-corpus M2.2 freezing remain incomplete. This is a new OLS capture of a declared edition, not historical-response reproduction or a complete Mondo release reproduction. The two uninstrumented preparatory lookups remain disclosed in the unchanged freeze package. M2.4 normalization, M2.5 alignment, M2.6 RDF generation and later stages have not begun.

## Final verification results

- Complete suite: **129 tests passed in 199.643 seconds**, exit status 0, including all 117 existing regressions and 12 new extraction tests. Diagnostic log: `/private/tmp/dementiagraph-mondo-extraction-tests.log`.
- Offline input verification, identity replay, extraction regeneration and byte-for-byte output verification passed. Manifest digest remains `b7763d83f41e61c9d8bc617189dc04826609926f83e480289e33f4ac9cc8bb0a`; output digest remains `43d7537f1f8e14340160d9581e8891db7f2dbe60a903c3910648295aae091882`.
- Negative controls rejected missing/changed frozen bodies, changed manifest bytes, extra concepts/parents, inferred-equivalence fields, changed endpoints, changed identifier spelling, incorrect source-description/capture links, altered permissions and omitted records/context/exclusion references. Relocated byte-identical inputs yielded identical output.
- Original raw-artifact and ledger fingerprints remained unchanged. The approved freeze and every previously tracked file remain byte-for-byte identical to baseline. No source request occurred.
- Python syntax, explicit new-file whitespace checks and both Git diff checks passed. Exactly four new files are untracked: `extractions/mondo-pilot-001.json`, `tools/m2_mondo_extract.py`, `tests/test_m2_mondo_extract.py`, and this document. Nothing staged, committed or pushed.

The bounded Mondo M2.3 extraction is ready for owner review within these limits. No later M2 stage is authorized or started by this record.
