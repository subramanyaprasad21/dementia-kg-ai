# OT 26.06 bounded evidence RDF and validation

This local release projects the eight recovered historical rows. Mondo's existing 60-resource / 317-triple graph and every M1 artifact remain unchanged. The OT graph can be loaded alongside Mondo without merging source-scoped references or asserting equivalence. A union is a reproducible source-backed **slice**, not the complete dementia evidence corpus.

## Semantic content

EvidenceOccurrence, MappingRecord and original/normalized DiseaseConceptReference remain distinct. Six original references exist (four authority-qualified OMIM inputs and two label-only clinical inputs); Europe PMC has no original reference because its columns are absent. Eight normalized references preserve raw MONDO underscore spelling. Two additional local project-anchor references express query roles. No OLS disease label is grafted onto an OT source record.

Six exact AD/FTD-normalized rows participate in two local direct-only SelectionContexts and five project-grouping associations. APP/AD1 and MAPT/semantic-dementia diagnostic rows remain represented with their reported destinations but outside anchor selection/grouping. Source totals, historical rank/order and descendant selection are not recreated. The local result is complete only for its enumerated IDs; it is partial for wider disease coverage.

The two clinical report descriptions retain PHASE_3 and the literal lowercase nct00594737 locator. They are OT descriptions, not acquired ClinicalTrials.gov versions. Shared source is explicitly derived from these two report-locator fields only. No efficacy, population, approval, termination cause, drug mechanism or indication record is inferred. The raw drug/stage/date/score/null information remains queryable as attributed source context; structured clinical claims await the proper supporting source.

Original arrays, scores, nested offsets and snippets remain in the extraction and attributed provenance sourceText. No text-mining sentence is called an independently inspected full article. Original Parquet remains outside Git. Permissions, raw digests, local observation receipts and exact description IDs remain attached through existing vocabulary.

## Verification layers

- `validate_ot2606.answers` reads original/normalized values, targets, publications, shared study and phase context from RDF assertions, not receipts. Tests use independently specified expected IDs and mutate the actual graph to block/change answers.
- Source fidelity checks require exact graph replay against the verified extraction, including qualifiers and provenance. Unavailable mechanism/indication/population promotion, new schema predicates and invented aggregate scores are rejected.
- Unchanged Meta-SHACL/SHACL configuration produces **zero violations and two source-omission warnings**. Raw conformance is **false**; project structural acceptance is **qualified-structural-pass**. Warnings do not excuse structural defects. The historical M1 negative fixture remains separate and unchanged.
- Unchanged OWL RL controls find no unexpected substantive additions or reasoning diagnostics for the new asserted graph plus declarations-only ontology. Open-world interpretation and the documented engine limitations remain; this is not universal consistency certification or biomedical validation.
- Six validation tests cover positive RDF answers, reversed mappings, wrong snapshot/destination, missing evidence, bounded group constituents, shared study, real structural defects, clinical/equivalence upgrades, round-trip and reasoning controls.

## Acceptance scope

The 56-slot assessment remains authoritative for readiness: nine verified row/context slots, 26 partial and 21 unavailable. Q01–Q07 are exposed design questions, not a held-out benchmark. Their **broader source-backed acceptance remains partial** despite successful bounded source-fidelity checks. R1–R14 M1 acceptance is preserved, not newly claimed for unavailable sources. No biomedical expert review, independent clinical adjudication, complete historical audit reproduction, graph advantage or experimental result is claimed.

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=tools:/private/tmp/ot2606-duckdb-inspection:/private/tmp/dementiagraph-m1-task008-pyshacl python3 tools/ot2606_rdf.py verify
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=tools:/private/tmp/ot2606-duckdb-inspection:/private/tmp/dementiagraph-m1-task008-pyshacl python3 tools/validate_ot2606.py
```
