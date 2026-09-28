# Portfolio and application descriptions

These descriptions cover the qualified development corpus and completed M7 portfolio challenge. They do not claim a comprehensive dementia KG, independent validation or a held-out benchmark.

## One-line CV version

Built a provenance-aware dementia RDF knowledge graph, bounded hybrid retrieval and grounded AI assertion verification, with reproducible development evaluation and structured error analysis.

## Technical CV version

Built a 191-resource, 1,112-triple biomedical RDF corpus from bounded Mondo and historical Open Targets evidence, preserving mapping, study and source provenance. Implemented structural validation, semantic-boundary tests, lexical/graph hybrid retrieval and grounded LLM answering with local RDF assertion verification. Evaluated 24 generated responses across 12 owner-authored development-overlapping questions, separating assertion support, fact completeness and outside-knowledge leakage.

## Research-application version

This project examines how provenance-aware knowledge representation constrains biomedical AI answers. Explicit evidence, mapping, mechanism, indication and study records preserve source boundaries rather than imply clinical conclusions. In a sole-owner-directed portfolio challenge, all 55 retained grounded assertions were supported, while question-level required-fact completion was 68.06%; local verification produced no precision change. The result motivates distinguishing assertion support from answer completeness, with independent review and broader validation still required.

## Supporting artifacts

- [Corpus manifest](../manifests/dementia-development-001.json) and [graph characterisation](m3_graph_characterisation.md).
- [Retrieval methods](m4_development_retrieval.md).
- [M7 owner-directed findings and annotation provenance](m7_owner_evaluation_findings.md).
- [Offline reproduction and limitations](reproducibility.md).

These are descriptions of implemented work, not novelty, clinical-validity or superiority claims.
