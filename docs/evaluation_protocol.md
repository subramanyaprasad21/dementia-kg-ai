# Evaluation protocol

Status: PROVISIONAL and unfrozen. The approved commitments are an interpretable primary contrast, question-set separation, and a held-out protocol/access freeze before tuning against the final evaluation set. No benchmark, labels, model, metric selection, or results exist.

## Comparisons and controls

Candidate conditions from the handoff are LLM-only, vector retrieval, explicit KG retrieval, hybrid retrieval, hybrid with ontology grounding, and hybrid with ontology grounding plus defined verification. This is a menu, not a commitment to implement six systems. Choose one primary contrast after scope and feasibility review. LLM-only has different information access and must be interpreted accordingly.

For component comparisons, propose matching source snapshot, accessible facts, generation model/version, prompts except necessary intervention differences, question set, evidence/token budgets, and retry allowances. Record representations, chunking, retrieval size, decoding settings, seeds where relevant, and execution environment. Document unavoidable differences rather than claiming perfect control. Source-derived vector text must not silently provide facts unavailable to the KG comparator.

## Ground truth, splits, and answerability

Design, development, and held-out questions remain distinct. Ground-truth construction should use inspected evidence, explicit answer criteria, and documented human review. Reviewer count, expertise, independence, adjudication, sample size, and allocation are REQUIRES HUMAN DECISION. No expert review is assumed available. LLM-generated labels, if later proposed, would require a separately approved checking process.

Proposed answerability is relative to the frozen evidence collection and approved question scope. Distinguish sufficient support, insufficient support, ambiguity requiring clarification, conflicting evidence, and invalid/out-of-scope premises. These categories and their scoring remain provisional. Absence of a triple does not establish a negative biomedical fact.

The split procedure should address duplicate/paraphrased questions and shared templates or evidence patterns that could cause leakage. The appropriate grouping unit is undecided. Record any question exposure during design or tuning and its consequences for held-out eligibility.

Abstention evaluation must measure both appropriate withholding on unsupported questions and excessive withholding on answerable questions. Clarification and conflict disclosure should be distinguished from generic refusal if retained in the rubric.

## Outcomes, ablations, and uncertainty

Candidate retrieval measures are evidence/entity precision and recall, Recall@k, and MRR where ranked relevance is meaningful. Candidate answer measures are correctness, claim-level support, unsupported claim rate, provenance correctness, and abstention behavior. Query measures may include syntax, schema, execution, and semantic correctness if query generation is adopted. System measures may include latency, token use, retry rate, and failures. Define denominators, grading rules, and primary versus secondary outcomes before freezing; not all candidates need survive.

Candidate ablations remove one retained mechanism such as graph retrieval, vector retrieval, ontology grounding, evidence checks, SHACL, or repair. Planner/routing ablations apply only if those components are justified. Keep unrelated conditions fixed and identify interaction effects that prevent a simple causal interpretation.

For each verification mechanism, document the checked property, assumptions, false positives, false negatives, and what it cannot establish. Evaluate controlled failure fixtures separately from natural question performance. Conformance, consistency, evidence presence, and validator success do not establish biomedical truth or unrestricted answer entailment.

Uncertainty analysis should address finite question sampling, related questions, stochastic generation, and reviewer disagreement. Replication counts, confidence intervals or other statistical procedures, and sample-size rationale are undecided. Report effect sizes and trade-offs where appropriate; do not invent significance or assume questions are independent.

## Failure analysis and freeze

Candidate failure labels include entity linking, mapping, retrieval miss, graph path, vector retrieval, query generation/validation, insufficient knowledge, conflicting evidence, synthesis/verbalization, unsupported claim, provenance, validator false positive/negative, and unknown. Preserve uncertainty and multiple contributing causes rather than forcing every failure into one cause. Revise the taxonomy transparently as evidence accumulates.

Before system tuning against the final evaluation set, approve and freeze the protocol and held-out access rules. Proposed rules restrict final questions/labels from routine development, log access and exposure, and require a decision on contamination before continued held-out claims. Who curates, stores, and accesses the set remains undecided; no secure separation is claimed yet.

The eventual freeze record should identify question/evidence snapshot versions, rubric, systems/configurations, primary contrast, metrics, analysis, exclusions, and access permissions. Protocol changes require owner approval, versioning, rationale, and an assessment of whether evaluation remains valid. M7 runs the frozen evaluation and reproducibility checks. Failed runs and exclusions remain traceable; no experimental results may be removed from provenance without owner approval.


## Task 003 design-material constraints

The Task 003 evidence sample, question texts, answer sketches and near-paraphrases are DESIGN material and have been exposed during scope selection. They are not a held-out evaluation set. The rank-three target prefixes and selected source strata are deliberately bounded and biased; their overlap and missingness do not estimate disease-population coverage.

Candidate question counts must not be treated as independent observations: pairings and AD-only controls reuse targets, publications, path templates and source-rule patterns. Before any later split, review grouping by evidence record, source assertion, underlying publication/study and question template, rather than randomly splitting paraphrases. Source duplication and derived clinical-precedence evidence also require dependency handling.

Provisional answer criteria must distinguish exact source-record retrieval, inspection of an abstract, inspection of a primary report, clinical claim adjudication and unverified source mappings. A metadata-correct answer can still make an unsupported biological generalization. Counterbalance answerable positive cases with bounded insufficiency cases; otherwise a verifier that always abstains could look successful. Current questions have no independent human labels, execution results or demonstrated graph advantage. These constraints refine future planning without freezing a rubric, benchmark, primary contrast or access protocol.
