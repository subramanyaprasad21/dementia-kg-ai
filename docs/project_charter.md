# Project charter

Status: working charter. Principles below reflect the master handoff and the owner's Task 001 approval; implementation choices remain subject to separate decisions.

## Purpose and boundaries

DementiaGraph-V aims to become a reproducible biomedical knowledge research system whose retrieval and answering behavior can be examined experimentally. A chat interface alone is not the research outcome. Evidence tracing, controlled comparisons, and failure analysis are central to assessing the system.

The project is not clinical decision support. It will not diagnose individuals, recommend patient treatment, or replace clinicians. Research questions and examples must respect that boundary.

The project remains intellectually separate from Transformation Fidelity, which studies source-to-OMOP transformation, and the T2DM Disease Knowledge Graph, which already demonstrates semantic integration and KG engineering. Here, the intended extension concerns the interaction of structured knowledge, retrieval, LLMs, and verification. The related-work audit must establish whether any resulting contribution is novel.

## Scientific and engineering principles

System breadth may exceed the scope of the primary experiment. The experiment must isolate an interpretable primary contrast; secondary analyses cannot turn every component into an independent claimed contribution. Negative results and genuine failures belong in the research record.

Ontology design follows curated competency questions and available evidence. Reuse authoritative semantics where justified, align identifiers using documented evidence, and extend only for demonstrated application requirements. Do not measure modelling quality by class count.

RDF/OWL is the provisional semantic source of truth. A property graph projection requires a concrete need and an account of semantic preservation and loss. Neo4j has not been approved. Agentic orchestration, graph analytics, KG embeddings, and link prediction require specific research or engineering justification before adoption.

OWL semantics and inference, SHACL data constraints, query validity, and evidence checks serve different purposes. None establishes biomedical truth. Every verification mechanism must specify the property checked, assumptions, false-positive and false-negative possibilities, and limits. Generated statements, source assertions, inferred knowledge, and validation outcomes must remain distinguishable.

Provenance must support the eventual evidence requirements. Record source releases, transformations, mappings, exclusions, and derivations. Preserve distinctions among raw, normalized, derived, and inferred data. Source inconsistencies must not be silently repaired. Reproducibility includes model and prompt configurations, dependencies, evaluation procedures, and retained experimental artifacts; stochastic or externally hosted behavior may limit exact reruns.

Design competency questions, development questions, and held-out evaluation questions serve separate roles. Questions used to shape the system are not unbiased held-out evidence. Freeze the held-out protocol and access rules before tuning against the final evaluation set; M7 executes that protocol.

## Integrity and ownership

Claims require evidence. Citations, identifiers, mappings, labels, provenance, reviews, results, significance, and novelty must never be fabricated. Use NOT YET VERIFIED for unchecked claims, PROVISIONAL for proposals, REQUIRES HUMAN DECISION for approval gates, and DEFERRED for intentionally postponed choices.

Development is AI-assisted. Consequential scientific and architectural decisions belong to the owner. Substantial component proposals must explain purpose, inputs, outputs, connections, alternatives, trade-offs, failure modes, testing, and the concepts the owner needs to understand. Advanced concepts should be identified explicitly.

Course material is a learning reference, not an architectural specification. Any inspected or reused assets require appropriate licence review and attribution. Instructor work must not be represented as original work.

Git history must reflect actual work, including genuine failures. No backdating, invented checkpoints, artificial commit schedule, or erasure of failed experiments for appearances is acceptable. Before a proposed commit, present status, actual changes, checkpoint rationale, validation, unresolved issues, and a commit message; obtain checkpoint-specific approval. Pushes require separate approval and an account of what will be published. Task 001 authorizes neither a commit nor a push.
