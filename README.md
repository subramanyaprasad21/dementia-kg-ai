# DementiaGraph-V

DementiaGraph-V is an AI-assisted research project studying how structured dementia knowledge, retrieval, and explicitly defined verification checks affect LLM-based knowledge answering.

Historical M1 closure status: **M0 FROZEN / M1 CLOSED within the bounded audit-derived research and implementation scope**, by explicit owner approval on 2026-09-24 (Asia/Kolkata). The original approved scope, conceptual design, 20/28/39 manifest, G01–G06 mechanics, Q01–Q07 and R1–R14 remain unchanged. No research novelty or performance result is established.

## Current portfolio evaluation status

The 12-question **development-overlapping portfolio challenge** has completed model-only and KG-grounded generation with local verification of the same grounded outputs. [Owner-directed review and structured error analysis](docs/m7_owner_evaluation_findings.md) are recorded, with explicit provenance for assistant-applied annotation under the owner’s supplied decisions. Findings separate the intentional no-retrieval baseline from successful grounded evidence use, partial completeness omissions and model-only outside-knowledge scope leakage. These are development findings, not an unseen benchmark, independent validation, clinical evaluation or proof of superiority. Broader research and M8 packaging remain pending; the project is not declared finished. The M1 closure material below is historical.

The owner approved D002–D014 in the [M0 freeze package](docs/decisions/README.md#task-005-approved-m0-freeze-package) and authorized the [M1 entry package](docs/m0_plan.md#m1-entry-package--approved). Subsequent M1 approvals and implementation records establish the bounded closure below. Deferred work remains deferred, not completed.

The approved direction is a provenance-aware AD+FTD knowledge graph and controlled KG–LLM research system, emphasizing disease-scope verification under fixed evidence access and retrieval. An explicit semantic representation is the project direction; graph advantage is NOT YET DEMONSTRATED. RDF/OWL remains the provisional semantic authority; the approved explicit-resource model has a declarations-only ontology implementation. No deployment stack is established by this closure. The quality target is a reviewable research system, not graph size, a generic chatbot, a course reproduction, cosmetic domain adaptation or an agent demonstration.

The intended use is biomedical research knowledge retrieval. The project does not diagnose dementia, recommend patient treatment, replace clinicians, or provide individual clinical decision support. Verification of a defined system property does not establish biomedical truth.

## M1 bounded closure — owner approved 2026-09-24

The [M1.6 acceptance record](docs/m1_semantic_acceptance.md) records the query results, controls, R1–R14 reconciliation and limitations supporting closure:

- Ontology: 20 local classes, 27 local object properties plus external `prov:wasDerivedFrom` (28 total), and 39 datatype properties; 355 triples, with declarations and annotations only.
- Audit-derived fixtures: 170 records, 1,130 RDF triples and 48 passages traceable to 12 pinned audit sections. Identity receipts, source/version distinctions, replay, immutable revisions and provenance are verified; the original fixtures, receipts and execution ledger are unchanged.
- All **91 tests passed** in the final implementation rerun (199.592 seconds), including identity/provenance, Turtle/Meta-SHACL, OWL reasoning controls and bounded semantic acceptance. OWL closure counts remain 953 triples for the ontology and 2,945 with fixtures, with no unexpected substantive inferred assertions or baseline contradiction diagnostics. The documented owlrl limitations remain applicable.
- Q01–Q07 and R1–R14 have bounded acceptance supported by useful RDF-derived results and controlled negative mutations. Design questions are not held-out evaluation cases, and technical checks do not replace manual judgments.
- The historical dependency DerivedStatement still lacks `completenessStatus`: the original baseline remains **one violation / eight warnings, raw SHACL conformance false**. Its unchanged identity and payload remain a historical negative fixture, not a complete persisted computation. A separately identified deterministic in-memory comparison yields zero violations / eight warnings in its explicit acceptance view; it does not repair history or establish upstream completeness.

The final 91-test run precedes this authorized README-only milestone reconciliation. All other tracked baseline files were subsequently checked byte-for-byte. Three historical whole-repository immutability guards include README and will flag this approved documentation change on a direct rerun; their implementation was not changed in this checkpoint. This test-maintenance limitation is separate from the verified semantic/structural results and requires a scoped guard update before expecting an unqualified post-closure full-suite pass.

Independent biomedical validation, historical upstream reproduction, clinical correctness, source completeness, primary-source/manual adjudication, held-out evaluation and research experiments remain deferred. Closure does not complete the wider project or demonstrate graph advantage.

The existing next milestone is **M2 — Data / KG construction**, beginning with **M2.1 — Source acquisition**, followed by version freezing, extraction, normalisation, entity alignment, RDF generation, provenance attachment, KG validation and a reproducible KG release V1. M2 work has not begun. A concrete acquisition scope, source versions/artifacts, permissions, retention and capture-budget plan require separate owner authorization under G05 before live acquisition; historical observations must not be silently replaced with current upstream data.

## Design documents

- [Project charter](docs/project_charter.md): durable principles and governance.
- [M0 plan](docs/m0_plan.md): sequence, dependencies, risks, and exit criteria.
- [Project scope](docs/project_scope.md): candidate domain boundaries and exclusions.
- [Research questions](docs/research_questions.md): candidate questions and narrowing criteria.
- [Source audit](docs/source_audit.md): evidence required before source selection.
- [Related work](docs/related_work.md): literature-search and comparison method.
- [Competency questions](docs/competency_questions.md): question-set separation and curation.
- [Evaluation protocol](docs/evaluation_protocol.md): provisional controlled evaluation design.
- [Decision register](docs/decisions/README.md): approval records and decision format.
