# M3 — qualified development graph characterisation

Development proceeded with unresolved primary context recorded on 2026-09-26. Input: `manifests/dementia-development-001.json`. All computations are offline over its five asserted RDF files, without ontology closure or identifier merging.

## Results and definitions

- **191 subject resources / 1,112 triples**, including 56 PROV entities, 33 source-scoped disease references, 29 snapshots, 15 publication references and eight evidence occurrences. A subject-resource count is not a count of biomedical entities, source assertions or independent experiments.
- **299 distinct URI-to-URI endpoint pairs** between described subjects, excluding `rdf:type`. The undirected view has ten components with sizes **131, 9, 9, 9, 9, 9, 4, 4, 4, 3**. Provenance participates in this view; shared source infrastructure can create connectivity.
- A separately declared projection of participant, mapping, selection, study and hierarchy properties has **100 active nodes / 112 endpoint pairs**, six components of sizes **85, 3, 3, 3, 3, 3**, and excludes 91 inactive subjects. This is a record-link projection, not a biological interaction network. The exact predicates are stored in the machine report.
- The eight evidence occurrences comprise **four genomics_england, two europepmc and two clinical_precedence** records. This is deliberate sampling, not an estimate of disease/source prevalence. Multiple records can share one report; counts do not measure independent confirmation.
- All **32 inspected source records** (8 evidence, 8 mappings, 5 hierarchy steps, 5 mechanisms, 4 indications, 2 study records) have a source locator and linked snapshot with version and derivation. This structural coverage does not verify the primary source's completeness, permissions or biomedical truth. Referents and project operations are excluded from that denominator.
- Directed traversal over the declared projection, bounded at four edges, finds **19 evidence-to-publication pairs**, all direct. This is citation reachability; it is not support adjudication. Reverse edges, equal identifier strings, schema class membership and inferred disease equivalence do not create paths.

Full type, predicate, authority and coverage counts: `assessments/dementia-development-001.characterisation.json`.

## Roadmap coverage

M3.1 structural statistics, M3.2 connectivity, M3.3 bounded record-path analysis and M3.5 interpretation are implemented. For M3.4, the question-justified analyses are citation reachability, provenance coverage and source concentration. Centrality, community detection, embeddings and biological hub ranking add no defensible insight to this purposively selected record graph and are not implemented. Graph advantage remains NOT YET DEMONSTRATED.

Disconnected source-scoped references are preserved deliberately. Matching labels/identifiers must not be used to improve connectivity artificially. The five isolated three-node hierarchy motifs in the semantic projection are explicit step/child/parent structures, not automatically chained equivalent disease concepts.

## Reproduction and verification

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=tools:/private/tmp/dementiagraph-m1-task008-pyshacl python3 tools/characterise_development_graph.py
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=tools:/private/tmp/dementiagraph-m1-task008-pyshacl python3 -m unittest discover -s tests -p test_development_characterisation.py -v
```

Four tests pass: deterministic inventory/report replay, loss of provenance reduces coverage, equal literal/class values do not connect records, and deletion/reversal affects directed reachability. Projection predicates are checked against the unchanged ontology. During implementation an initial predicate list contained two unused names; these were replaced with the actual `reportedEvidence` and `selectedOccurrence` terms before recording results. No ontology term was added.

The full suite was run during M4 integration verification. These are descriptive engineering results on exposed development evidence, not held-out experimental results or independent biomedical validation.
