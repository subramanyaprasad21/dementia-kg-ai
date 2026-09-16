# M0 plan

Status: documentation bootstrap. Scientific design is incomplete; M1 is not authorized.

## Sequence and dependencies

| Step | Work and output | Dependency / gate |
| --- | --- | --- |
| M0.1 | Compare bounded dementia scopes and intended research tasks. | Owner selects scope after feasibility evidence; no slice is selected yet. |
| M0.2 | Audit candidate data and ontology sources, including coverage, access, licence, and provenance. | Source facts require verification; final selections require approval. |
| M0.3 | Search and compare related work using a recorded method. | Gap and novelty remain NOT YET VERIFIED. |
| M0.4 | Curate evidence-grounded design competency questions. | Iterate with scope and source findings; owner approves the set. |
| M0.5 | Narrow the research question to an interpretable primary contrast. | Depends on feasibility, question needs, and related work; owner approval required. |
| M0.6 | Specify ground truth, controls, question splits, access rules, metrics, and analysis. | Owner approves the evaluation protocol and later changes. |

These steps permit iteration rather than imposing a strictly linear discovery process. Source and literature findings may require scope or question revisions. The initial bootstrap supplies structures and constraints, not completed audits.

## Risks and review gates

The main risks are an oversized domain, confounded comparisons, circular question design, inadequate source coverage, and treating validator success as truth. Engineering risks include representation drift, unsupported identifier alignment, insufficient provenance granularity, validator errors, and premature infrastructure. Address these through bounded scope, source evidence, explicit verification contracts, separated question sets, and component-specific approval.

Final datasets, external ontologies, ontology scope, mapping strategy, provenance model, competency questions, research question, and ground-truth protocol require owner decisions. Database, embedding model, LLM, and agent architecture selections also require approval when needed. Minor implementation choices may later be made within approved scope if documented.

The held-out evaluation protocol and access rules must be frozen before tuning against the final evaluation set. The exact benchmark construction and access workflow remains REQUIRES HUMAN DECISION. M7 executes the frozen evaluation; it is not the first point at which evaluation is designed. Changes require a versioned decision and assessment of evaluation contamination.

## Exit criteria and later milestones

M0 is complete only after owner review of the domain scope, source/ontology audit and selections, related-work assessment, curated competency questions, refined research question, and evaluation design. Unresolved dependencies must be identified explicitly; a blocking dependency cannot be hidden by labelling the milestone complete. Novelty need not be established to proceed, but must not be claimed without evidence.

M1 requires separate authorization for the semantic foundation, including formal modelling, provenance implementation, reasoning tests, and SHACL. Later milestones cover KG construction (M2), justified graph characterization (M3), retrieval baselines (M4), defined verification mechanisms (M5), optional orchestration (M6), evaluation (M7), and release documentation (M8). Create directories as real artifacts emerge, not as empty production scaffolding.
