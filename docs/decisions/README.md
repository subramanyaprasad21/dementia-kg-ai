# Decision register

This register separates owner-approved commitments from proposals. Approval of documentation does not approve a dataset, ontology, model, or experiment described as a candidate within it.

Statuses are PROPOSED, APPROVED, REJECTED, DEFERRED, and SUPERSEDED. Use stable decision IDs. Preserve earlier records when a later decision changes them; link both directions.

## Record format

Each future record contains: decision ID; date; status; question; alternatives considered; evidence; decision; rationale; consequences; dependencies; and supersedes/superseded-by links where relevant. Dates must reflect actual decisions. If a date is unavailable, say so rather than inventing one. Evidence should identify the owner instruction or reviewed artifact supporting the record. Do not imply that alternatives received review unless they did.

## Approved bootstrap record

Decision ID: D001. Date: 2026-09-16 (Task 001 session date, Asia/Kolkata). Status: APPROVED.

Question: What may the M0 documentation bootstrap create, and which methodological corrections govern it?

Alternatives considered: the preceding proposal included a verbatim handoff copy; Task 001 explicitly replaces that with a project-facing charter. Other possible alternatives are not recorded as reviewed.

Evidence: the owner's “TASK 001 — M0 DOCUMENTATION BOOTSTRAP” instruction, sections 1–2, 6–10. This is a record of the instruction, not a claim of external scientific evidence.

Decision: create README.md and the nine approved documents under docs, including this register. Keep the work at M0. Adopt these seven methodological commitments: narrow the eventual primary experiment to an interpretable contrast; separate design, development, and held-out questions; freeze held-out protocol/access rules before tuning against the final set; define verification by checked properties rather than biomedical truth; retain RDF/OWL as provisional semantic authority with Neo4j unapproved; keep agentic orchestration conditional on concrete need; and require explicit justification for graph analysis, embeddings, and link prediction.

Rationale: the owner approved the bootstrap with these corrections to preserve scientific interpretability and avoid premature architecture decisions.

Consequences: working documents may record candidates and unresolved gates, but may not imply completed audits, validated questions, or final selections. No implementation, acquisition, dependency installation, experiments, commit, or push is authorized by Task 001. Commit and push proposals require the review procedures in the charter.

Dependencies: later scientific and engineering decisions require evidence and owner approval. Supersedes: the earlier proposed verbatim handoff-copy operation and benchmark timing that first defined evaluation at M7. Superseded by: none.

## Pending gates

Research question, final datasets, external ontologies, ontology scope, mapping strategy, provenance model, competency-question freeze, graph database, embedding model, LLM, agent architecture, evaluation ground truth, protocol changes, contribution interpretation, novelty claims, and removal of failed experiments from provenance require owner approval. No approval of these selections is recorded here. Optional architecture choices may remain DEFERRED until needed.
