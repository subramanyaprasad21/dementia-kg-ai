# M2.7 — attached Mondo capture and description provenance

The separate `kg/mondo-pilot-001/provenance.ttl` graph adds **29 existing information resources / 131 triples**: 14 distinct `m2-source-description-1` IDs and 15 `m2-capture-1` IDs, typed using existing prov:Entity. Combined with immutable M2.6 records this is 60 subjects / 317 triples. No new identity family, class or property is introduced.

SourceSnapshots already derive from their description IDs. Capture resources use contextRecord to identify the encountered description, never an independence or biomedical-support relation. Before/after metadata encounters remain two captures of one description. Their sourceText retains the canonical capture receipts (request/raw digests, source edition, OLS load timestamp, capture times, rights and acquisition context); sourceLocator retains frozen manifest and external artifact references. Description sourceText includes the original description receipt, source context, permission metadata and attributed source-value projections from the unchanged extraction. This text explicitly distinguishes extraction values from the entire capture projection and from raw bytes. Receipt payload hashes refer to the original verified projection, not this RDF wrapper.

All eight original labels, IRIs and annotations remain accessible with types/missingness intact in the attributed extraction values; identifiers and labels also appear structurally in the scoped references. Parent source values and row locators remain linked. Six additional rows are exclusion locators only, never projected parent assertions. Source xref strings (including equivalence-like wording) are not owl:sameAs or local mapping assertions. All provenance replay is offline and verifies the original response bodies outside Git before use.

Three focused tests passed: all capture/description identities and canonical receipt hashes; exact annotations/permissions and six exclusion locators; deterministic replay and rejection of a removed capture-context edge. No M2.6 payload/receipt changes were needed. No raw source response bodies are committed.

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/private/tmp/dementiagraph-m1-task008-pyshacl python3 tools/m2_mondo_provenance.py verify
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/private/tmp/dementiagraph-m1-task008-pyshacl python3 -m unittest discover -s tests -p test_m2_mondo_provenance.py -v
```

`build` refuses an existing output; `build()` provides an in-memory graph for reproducible release. `MONDO_PILOT_ARTIFACTS` relocates unchanged external raw files. M2.8 must validate the combined graph. Source edition remains 2026-09-01; no full Mondo-release or historical OLS-response reproduction is claimed. The two uninstrumented preparatory lookups and Open Targets 26.06/full-corpus gaps remain as documented in the freeze. No new acquisition, inference, biomedical review or full dementia KG is claimed.
