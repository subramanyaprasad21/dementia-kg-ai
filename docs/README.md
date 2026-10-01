# Documentation map

This directory contains both **current project summaries** and **historical development records**. The distinction matters: milestone files preserve the state and decisions that existed when they were written, so an older document may say that a later milestone had not yet begun even though the M0–M7 development programme is now complete.

For the current state of DementiaGraph-V, start with the documents below rather than inferring project status from an earlier milestone record.

## Current summaries

| Document | Purpose |
|---|---|
| [Portfolio summary](portfolio_summary.md) | Compact description of the implemented system, corpus and completed M7 evaluation. |
| [Research questions](research_questions.md) | Current research framing, completed evaluation result and open questions. |
| [Evaluation protocol](evaluation_protocol.md) | What was evaluated, how conditions were compared, and what the current evidence does and does not support. |
| [Reproducibility](reproducibility.md) | Offline replay paths, environment requirements, frozen-authority handling and test entry points. |
| [Related work](related_work.md) | Research context and the boundaries between this project and adjacent KG/LLM work. |
| [Source audit](source_audit.md) | Source identity, provenance and acquisition record across the bounded corpus. |

The repository-level [README](../README.md) remains the shortest entry point for the completed system and its main limitations.

## Technical implementation and results

These records describe implemented stages rather than the current project status as a whole.

- [M3 graph characterisation](m3_graph_characterisation.md) — structural properties of the qualified development graph.
- [M4 development retrieval](m4_development_retrieval.md) — lexical, graph and hybrid retrieval over the same finite corpus.
- [M5 verified-AI preparation](m5_verified_ai_preparation.md), [development pilot](m5_development_pilot_results.md), [retrieval correction](m5_retrieval_pairing_correction.md), [failed-generation diagnosis](m5_failed_generation_diagnosis.md), and [follow-up results](m5_corrected_followup_results.md) — controlled generation, retrieval pairing, execution failures and follow-up evidence.
- [M7 protocol proposal](m7_protocol_proposal.md), [portfolio challenge](m7_portfolio_challenge.md), [execution runner](m7_execution_runner.md), [results](m7_portfolio_results.md), and [evaluation findings](m7_owner_evaluation_findings.md) — frozen evaluation design, recorded execution and completed review metrics.
- [M7 authoring guide](m7_authoring_guide.md) — conventions used to construct the evaluation package.

Source-specific implementation and release records are grouped by name: `m2_mondo_*` for the bounded Mondo slice and `ot2606_*` for historical Open Targets 26.06 evidence/context.

## Historical development records

Files from M0, M1 and early M2 preserve the design state that existed at those checkpoints. They include modelling alternatives, entry criteria, implementation mechanics, semantic acceptance, acquisition decisions and closure records. They are retained because they document how later choices were reached.

Examples include:

- [Project scope](project_scope.md), [M0 plan](m0_plan.md), [competency questions](competency_questions.md), and [decision index](decisions/README.md).
- `m1_*` records covering conceptual modelling, ontology implementation, reasoning, SHACL, identity and implementation readiness/mechanics.
- [Remaining M2 plan](remaining_m2_plan.md), [continued M2 results](continued_m2_results.md), and [M2 closure decision](m2_closure_decision.md).
- Open Targets and Mondo acquisition/release records that preserve source-specific constraints and historical status.

A status statement in one of these files applies to **that recorded checkpoint**, not automatically to the current repository state.

## Historical integrity

Historical manifests remain unchanged. Exact authority bytes named by those manifests are mirrored under [`archive/frozen/`](../archive/frozen/README.md) and checked against their recorded SHA-256 values. This allows current summaries and portability documentation to evolve without rewriting the historical evidence they describe.

## Reading order for review

For a technical or PhD review, a compact path is:

1. [Repository README](../README.md)
2. [Portfolio summary](portfolio_summary.md)
3. [Research questions](research_questions.md)
4. [Evaluation protocol](evaluation_protocol.md)
5. [M3 graph characterisation](m3_graph_characterisation.md)
6. [M4 development retrieval](m4_development_retrieval.md)
7. [M7 evaluation findings](m7_owner_evaluation_findings.md)
8. [Reproducibility](reproducibility.md)

Historical milestone records can then be consulted when a design decision, source boundary or earlier implementation state needs to be traced.
