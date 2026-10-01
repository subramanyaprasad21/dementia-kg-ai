# M2.8 — bounded Mondo KG validation

The union of immutable `records.ttl` and `provenance.ttl` contains **60 resources / 317 triples**. Six focused tests passed in 14.921 seconds. The unchanged approved M1 SHACL graph, with Meta-SHACL enabled and inference/advanced/JS/rule iteration/imports disabled, reports **raw conformance true, zero violations, zero warnings** for this source slice. This does not repair or hide the separate historical M1 baseline's one expected completenessStatus violation and eight warnings.

`tools/validate_m2_mondo.py` first replays original source integrity, record identities and provenance. Semantic acceptance independently reads the RDF participants, source snapshots, authorities, identifiers and row locators to recover the five exact approved directions, with compatible edition 2026-09-01. It then checks full graph equality to a fresh source-backed build, covering annotations, immutable identity payloads and capture links. The first check tests relational meaning; the second protects all source fidelity, not merely schema validity. Receipts are not used to supply missing query participants. Graph mutations are passed directly to these checks, independently of input checksums.

Positive/negative results:

- Exact eight external concepts / thirteen scoped references / five accepted parent assertions pass.
- Missing required endpoint and wrong endpoint type produce SHACL violations.
- Reversed direction, incompatible snapshot, extra hierarchy assertion, removed capture/source-text provenance and owl:sameAs additions fail semantic acceptance.
- An OWL RL/RDF control over ontology plus this graph adds no local-property assertions, prov:wasDerivedFrom assertions or non-reflexive owl:sameAs; no engine error diagnostic occurs. Existing owlrl limitations remain documented in `docs/m1_owl_reasoning.md`; this check is not universal consistency certification. Inferred triples are never persisted as source data.

The application result is `bounded-Mondo-source-fidelity-pass`, separate from raw SHACL conformance and biomedical interpretation. Eight source concepts and their scoped references do not establish disease equivalence, molecular causality or evidence independence. Only explicitly captured parent navigation is represented, not descendant closure. Neither full-source completeness nor clinical correctness is established. Full Q01–Q07 biomedical evidence needs the missing other sources; this slice supplies their Mondo context only. Original manual-review and broader R1–R14 obligations remain deferred.

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/private/tmp/dementiagraph-m1-task008-pyshacl python3 tools/validate_m2_mondo.py
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/private/tmp/dementiagraph-m1-task008-pyshacl python3 -m unittest discover -s tests -p test_m2_mondo_validation.py -v
```

No shapes, ontology terms, identity receipts, historical artifacts or source records were modified. Full regression verification and reproducible release packaging follow in M2.9. Open Targets 26.06 remains an unresolved full-corpus dependency; no 26.09 substitution or additional acquisition occurred.
