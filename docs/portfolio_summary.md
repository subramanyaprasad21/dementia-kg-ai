# Portfolio and application descriptions

These descriptions refer to the qualified development corpus and completed M7 portfolio challenge. They do not claim a comprehensive dementia KG, independent validation or a held-out benchmark.

## One-line CV version

Built a provenance-aware dementia RDF knowledge graph with bounded hybrid retrieval, grounded LLM answering, deterministic assertion verification and reproducible error analysis.

## Technical CV version

Built a 191-resource, 1,112-triple biomedical RDF corpus from bounded Mondo and historical Open Targets evidence, preserving source identity, mappings, study context and provenance. Implemented SHACL/semantic checks, lexical and graph retrieval with reciprocal-rank fusion, grounded LLM answering, and local RDF assertion verification. Evaluated 24 generated responses across 12 development-overlapping questions, separating retained-assertion support from required-fact completeness and outside-knowledge leakage.

## Research-application version

Developed a provenance-aware dementia knowledge graph and controlled retrieval/answering pipeline to examine how explicit evidence boundaries carry through generation and verification. Evidence, mapping, mechanism, indication and study records remain distinct rather than being collapsed into stronger clinical claims. In the current single-reviewer portfolio evaluation, all 55 retained grounded assertions were supported by supplied RDF while question-level required-fact completion was 68.06%; local verification did not change precision. The result highlights a difference between supporting the assertions an answer makes and covering all evidence required for a complete answer.

## Supporting artifacts

- [Corpus manifest](../manifests/dementia-development-001.json) and [graph characterisation](m3_graph_characterisation.md)
- [Retrieval implementation and contract](m4_development_retrieval.md)
- [M7 evaluation findings](m7_owner_evaluation_findings.md)
- [Offline reproduction guide](reproducibility.md)

Broader validation, independent review and unseen-question evaluation are outside the current result set.
