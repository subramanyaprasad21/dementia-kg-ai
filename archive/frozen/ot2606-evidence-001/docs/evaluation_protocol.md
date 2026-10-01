# Evaluation protocol

Status: **M0 FROZEN / M1 ENTRY AUTHORIZED**; executable evaluation protocol remains PROVISIONAL and unfrozen. The approved commitments are an interpretable primary contrast, question-set separation, and a held-out protocol/access freeze before tuning against the final evaluation set. No benchmark, labels, model, metric selection, or results exist.

## Task 005 approved validation and evaluation commitments

D010/D011 in the [freeze package](decisions/README.md#task-005-approved-m0-freeze-package) approve principles and required outcome dimensions, not a validation architecture or final experimental protocol. Bootstrap commitments remain in force; the freeze package was approved at Checkpoint 4, without completing deferred evaluation work.

Validation must distinguish OWL reasoning/consistency, SHACL structural constraints, identifier/mapping checks, query validation, provenance completeness, evidence existence, claim-scope checking and answer-to-evidence support. These are potential layers with different checked properties; no requirement to implement all layers or a particular sequence is created. OWL/SHACL success and evidence presence cannot establish biomedical truth.

Approved evaluation dimensions (not final metrics): supported answer completion; unsupported broadening; correct qualification; required abstention (including excessive abstention as a trade-off); direct versus propagated evidence; mechanism versus indication; disease-scope interpretation; provenance completeness. The existing capability table below explains these dimensions without finalizing metrics, denominators, thresholds, sample size or statistics.

DESIGN, DEVELOPMENT and HELD-OUT questions remain separate. No held-out set exists. Final held-out questions must not be used for development tuning; construction, custody, permitted evaluation access and contamination procedures require approval before any exposure/use. Freeze the final protocol/access rules before tuning against the final evaluation set; this timing commitment is not permission to tune on final questions. M7 executes evaluation, not its initial design.

Current answer criteria are technical source-review criteria, not biomedical ground truth. Reviewer arrangements, independent labels, statistical design and final benchmark remain **NOT READY for execution** and are explicitly deferred to a later approval gate. The owner accepted this staged boundary at Checkpoint 4; they do not block authorized M1 semantic-design entry, but remain incomplete. M1 must not begin automatically after this checkpoint. No experiment or deployment is authorized by approving M0.

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

## Task 004 capability-level evaluation implications

The seven [approved design questions](competency_questions.md#task-004-core--approved-as-design-questions-at-checkpoint-4) and their A–E boundaries are DESIGN material only. Technical source review provides draft criteria, **not independent labels or domain-expert adjudication**. No benchmark or held-out examples are created. C7–C9 are cross-cutting criteria rather than extra independent questions.

| Capability | Core cases | Later review/check needed |
| --- | --- | --- |
| C1 Association evidence tracing | Q01, Q02 | Exact target/disease/record joins plus a source-type distinction. Separate evidence-ID correctness from whether inspected text supports the claim. |
| C2 Original versus normalized scope | Q03, Q05 | Correct paired scope fields and mandatory source qualification; fail unsupported broadening even if the normalized identifier is correct. |
| C3 Direct versus descendant selection | Q04 | Classification against recorded query settings and normalized disease; separately identify upstream mapping. |
| C4 Mechanism versus indication | Q06 | Statement-type classification and correct indication scope; composed path must not receive a treatment/efficacy label. |
| C5 Clinical population | Q07 | Required population qualification, stage/status separation and bounded abstention about efficacy. Semantic wording requires human rubric review. |
| C6 Mapping ambiguity | Q05 | Preserve both assignments and context; no unapproved equivalence/repair. Disclosure is a valid answer, not generic refusal. |
| C7 Provenance completeness | All, especially Q01/Q02/Q06 | Required record/source/locator/depth slots; correct claim attribution; shared report dependency acknowledged. A present URL alone does not pass. |
| C8 Unsupported claims | All | Claim-level support decision relative to the bundle; wrong scope, causal upgrade and therapeutic upgrade recorded separately. No unsupported positive biomedical gold labels. |
| C9 Abstention and qualification | All | Correctly withhold unsupported parts while answering supported record facts; distinguish ambiguity/access limit from disproven claim. Measure excessive abstention too. |
| C10 Hierarchy interpretation | Q03–Q05 | Verify consecutive versioned source steps without equating classification, normalization and equivalence. A path check is not clinical adjudication. |

Proposed deterministic checks concern IDs, source fields, query flags, path steps and presence of required provenance slots. Proposed semi-deterministic review concerns whether prose preserves population scope and avoids implication beyond those records. Neither should be scored through keyword presence alone. Reviewers must inspect the claim–source match; expertise, number, independence and disagreement resolution remain owner decisions. Restrict technical labels to technical propositions unless appropriate domain review is later supplied.

For the recommended fixed-evidence contrast, define unsupported broadening as the primary candidate failure property. Before implementation/evaluation, approve its claim unit and denominator, answerable-case denominator, treatment of partially supported answers and abstention. Report support failures alongside supported-answer completion and excessive withholding so blanket refusal cannot look like success. Provenance-slot completeness and hierarchy classification can be secondary outcomes; no metrics or thresholds are frozen here.

Group by underlying report/publication, source assertion and question template before any later split. Q01/Q05 share PSEN1 evidence, Q03–Q05 share MAPT/mapping paths, Q06/Q07 share drug semantics; two clinical-precedence IDs can share one trial. All current records, answers and near-paraphrases are exposed design material, not seven independent test items. A future unexposed collection, its reviewers and access policy must be established separately; do not manufacture held-out variants now.

Source limitations should be review outcomes, not hidden exclusions. Distinguish uninspected full text, failed access, null fields, absent record in a bounded list, conflicting/contextual mappings and unsupported inference. Keep primary-source dates and downstream versions separate. Future paired systems need the same limitations and evidence—not richer graph provenance against incomplete vector text. Task 005 may approve these design constraints while explicitly scheduling the later held-out protocol/access freeze before tuning; it cannot claim that the final evaluation set already exists.
