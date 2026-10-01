# M2.6 — frozen Mondo RDF records

Owner-authorized offline continuation from `1be4234cdb28c9a6b7eaf88b41b9c49ec8e7b4f2`, using the approved `m2-rdf-record-1` extension. No earlier artifact or schema is edited.

## Implemented representation

`tools/m2_mondo_rdf.py` verifies the extraction/normalization hashes and complete offline freeze/raw/identity replay before generation. `kg/mondo-pilot-001/records.ttl` contains **31 resources / 186 triples**: 13 SourceSnapshots (eight individual term and five parent descriptions), 13 DiseaseConceptReferences (eight term-scoped and five parent-row-scoped), and five HierarchySteps. These represent exactly eight external Mondo concepts, not thirteen different diseases. Child references reuse their original individual-term source context; parent references remain scoped to the parent-response row. Lookup compatibility never merges them.

Five directions remain 0010857→0017160, 0017160→0017276, 0007088→0015140, 0015140→0100087 and 0100087→0004975 (all MONDO). Six excluded rows remain outside the RDF assertion projection. No path closure, equivalence, mapping repair or biomedical relationship is inferred.

The unchanged three-class subset of the approved ontology is used, plus approved existing properties. External MONDO identifiers are literal reference values, not locally instantiated disease classes. Original labels are xsd:string without lexical normalization. Snapshot artifactDescription retains canonical receipt, source context and permission metadata. Source locators retain URL and row pointer. Original source IRIs and annotations remain in the unchanged extraction; M2.7 attaches its attributed source-value projections on the separate existing description resources, rather than inventing annotation properties on disease references.

`record-identities.json` retains exact receipts and owned payloads. `sourceSlots` is provenance lookup metadata outside identity, preserving child and parent capture paths; it is checked by full replay. SourceSnapshot payloads already include prov:wasDerivedFrom to immutable M2 description IDs. M2.7 defines those resources and capture context separately, so no record payload or identity needs to change when provenance is attached. This intermediate graph is not yet a complete release or fully linked provenance package.

## Reproduction and results

Use the existing RDFLib environment, without new dependencies:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/private/tmp/dementiagraph-m1-task008-pyshacl python3 tools/m2_mondo_rdf.py verify
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/private/tmp/dementiagraph-m1-task008-pyshacl python3 -m unittest discover -s tests -p test_m2_mondo_rdf.py -v
```

`build` creates only absent outputs, never overwrites. `outputs()` returns deterministic bytes in memory for release/replay. Sorted full-IRI triples are valid Turtle; no blank nodes or serializer-dependent prefix layout enters identity. Original literals are preserved. Set equality after RDF round-trip is tested separately from byte equality. `MONDO_PILOT_ARTIFACTS` supports relocated frozen raw artifacts.

Four focused tests passed: exact independent inventory/pairs; deterministic generation, serialization/replay and graph round-trip; every receipt/content revision and changed-direction identity; altered input and output rejection. The four identity-extension tests also passed before RDF generation. Full regressions run at final integration. No live acquisition, M1 audit identity reuse or raw-response Git storage occurred. Full-corpus acquisition remains incomplete and Open Targets 26.06 remains blocked. This is a new captured OLS slice of edition 2026-09-01, not historical OLS-response or full-release reproduction.
