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

## Pending gates at bootstrap — historical

Research question, final datasets, external ontologies, ontology scope, mapping strategy, provenance model, competency-question freeze, graph database, embedding model, LLM, agent architecture, evaluation ground truth, protocol changes, contribution interpretation, novelty claims, and removal of failed experiments from provenance require owner approval. No approval of these selections is recorded here. Optional architecture choices may remain DEFERRED until needed.

## Task 005 approved M0 freeze package

**Package status: APPROVED. M0 FROZEN / M1 ENTRY AUTHORIZED.** Proposal prepared 2026-09-17; approved 2026-09-17 (Asia/Kolkata). Approval evidence: the owner’s explicit **“APPROVAL — M0 FREEZE / CHECKPOINT 4”** instruction approving D002 through D014 as documented, with the qualifications recorded here. Checkpoint 3 (`8f1c4b6`) had accepted the investigation only; Checkpoint 4 supplies the freeze and entry authorization. No new scientific decisions are introduced.

Common record fields for D002–D014: proposal date 2026-09-17; **status APPROVED (previously PROPOSED)**; approval date 2026-09-17; approval evidence as above. D001 remains APPROVED and unchanged. Supersedes: no approved decision; the approved scope now replaces earlier provisional scope recommendations as current policy. Superseded by: none. Each record’s original proposal wording below is preserved as the approved decision text; conditional references to this package’s approval are now satisfied. Dependencies concerning later work remain gates, not completed deliverables.

**Approval limits:** exact source acquisition artifacts/versions, executable evaluation protocol, held-out benchmark, reviewer arrangements, final metrics/statistics, experimental results and novelty/contribution claims are outside this approval. All documented M1/later deferrals remain incomplete. AD+FTD is approved without automatic descendant closure; AD-only is the considered but unselected V1 alternative. Q01–Q07 are design questions only; R1–R14 are semantic requirements, not classes/properties. RDF/OWL is approved as provisional semantic authority. Graph advantage remains NOT YET DEMONSTRATED; no biomedical domain-expert adjudication is claimed. Phenotypes, pathways, Neo4j/property graph, embeddings, KG embeddings, graph ML and agents remain deferred until separately justified. M1 entry is authorized, but this checkpoint must stop before M1 work starts; no push is authorized.

### D002 — Disease scope

Status: **APPROVED**. Approval: M0 Freeze / Checkpoint 4, 2026-09-17.

- **Question / proposed decision:** Select AD MONDO:0004975 and broad FTD MONDO:0017276 for V1 direct normalized-anchor comparison. Preserve only audited narrower source/context records. No bvFTD substitution, third anchor, full-subtree ingestion or automatic descendant closure. Explicit diagnostic paths remain distinguishable from core direct associations.
- **Alternatives / evidence / rationale:** AD-only, AD+LBD, four-disease and broad-spectrum alternatives were investigated in Tasks 002–004. [Scope assessment](../project_scope.md) favors bounded FTD for observed mapping/dependency/population cases, not counts. AD-only remains an unrejected fallback until approval; approval would make it the considered but unselected V1 alternative, not scientifically invalid.
- **Consequences / dependencies:** Adds bounded contextual review burden. No general dementia, all-FTD clinical or phenotype-discrimination claim. Depends on D003/D004/D008 and later source eligibility decisions. On approval replaces the earlier provisional scope recommendations as current policy; their historical records remain.

### D003 — Core knowledge boundary

Status: **APPROVED**. Approval: M0 Freeze / Checkpoint 4, 2026-09-17.

- **Question / proposed decision:** Include disease identity; necessary hierarchy/context; disease–target associations; association evidence; provenance; original/normalized identity; mapping ambiguity; direct/descendant-derived distinctions; target–drug mechanisms; drug–disease indications; needed trial/study/population context; and separately labelled derived/audit statements.
- **Alternatives / evidence / rationale:** Earlier optional drug paths and phenotype/process-rich scopes are documented in Tasks 002–004. [Q01–Q07](../competency_questions.md) require mechanisms/indications in the representation; broad phenotypes/processes do not survive the core question review.
- **Consequences / dependencies:** Core means a semantic capability, not comprehensive acquisition of every instance. In the proposed V1, mechanisms/indications cease to be optional capabilities; earlier wording stays historical. Depends on D002/D004/D009; deferrals in D014.

### D004 — Design competency questions

Status: **APPROVED**. Approval: M0 Freeze / Checkpoint 4, 2026-09-17.

- **Question / proposed decision:** Freeze exactly Q01–Q07 with their existing required slots, A–E evidence boundaries and graph-value assessments as DESIGN questions. Preserve the deferred/challenge/parked/rejected history.
- **Alternatives / evidence / rationale:** Task 003's 21 records were reduced by Task 004; Checkpoint 3 accepted that work. [Current core](../competency_questions.md#task-004-core--approved-as-design-questions-at-checkpoint-4) covers distinct operations without treating cross-cutting checks as extra samples.
- **Consequences / dependencies:** No new questions, clinical gold labels or held-out status. Later substantive changes need versioned owner review; shared evidence/templates remain dependent. Depends on D002/D009/D011/D012.

### D005 — Research emphasis

Status: **APPROVED**. Approval: M0 Freeze / Checkpoint 4, 2026-09-17.

- **Question / proposed decision:** Primary emphasis: disease-scope verification with evidence access and retrieval held fixed. Secondary: provenance completeness/evidence dependency; hierarchy/normalization/propagation interpretation. No exact statistical hypothesis or final experimental design frozen.
- **Alternatives / evidence / rationale:** Earlier graph-retrieval and ontology-grounding primary contrasts remain historical alternatives. [Research questions](../research_questions.md) and Q01–Q07 motivate checking unsupported broadening, not multiple simultaneous primary claims.
- **Consequences / dependencies:** Exact intervention, controls, metrics and statistics need later approval. The obligation to evaluate graph benefit does not automatically create a second primary experiment. Depends on D004/D011/D013.

### D006 — KG identity and quality target

Status: **APPROVED**. Approval: M0 Freeze / Checkpoint 4, 2026-09-17.

- **Question / proposed decision:** The project will construct and evaluate an explicit semantic KG for entities, relations, hierarchy, evidence, provenance, scope, mappings and derived statements, subject to later implementation authorization. **Graph advantage is NOT YET DEMONSTRATED.**
- **Alternatives / evidence / rationale:** Task 004 acknowledges that structured text/relational representations can answer the core cases. The owner's Task 005 sections 7/16 specify a provenance-aware dementia KG and controlled KG–LLM research system, not a generic chatbot, tutorial/course adaptation, size-driven graph or agent demo.
- **Consequences / dependencies:** Later evaluation must test measurable benefit against justified alternative representations/retrieval approaches under matched access. Neither graph superiority nor graph necessity is an accepted result. Depends on D005/D007/D011; no engine selected.

### D007 — Provisional semantic authority

Status: **APPROVED**. Approval: M0 Freeze / Checkpoint 4, 2026-09-17.

- **Question / proposed decision:** Carry RDF/OWL as the provisional semantic source of truth into M1, reaffirming D001. Freeze the direction, not its implementation.
- **Alternatives / evidence / rationale:** D001/[charter](../project_charter.md) already establish provisional RDF/OWL authority; property-graph projection remains unapproved. Task 005 preserves this distinction.
- **Consequences / dependencies:** Namespace, classes/properties, OWL profile, import strategy, provenance vocabulary, serialization, reasoner and triple store remain M1 decisions/proposals subject to applicable owner gates. No OWL/RDF is created now. Depends on D009; does not supersede D001.

### D008 — Source roles

Status: **APPROVED**. Approval: M0 Freeze / Checkpoint 4, 2026-09-17.

- **Question / proposed decision:** Mondo is the authoritative disease concept reference/alignment source for the proposed anchors; no whole-ontology import. HPO remains a candidate for later phenotype extension outside core V1. OT is a candidate major association/evidence source, subject to M1/M2 acquisition and reproducibility decisions; it does not define biomedical truth.
- **Alternatives / evidence / rationale:** [Source audit](../source_audit.md) distinguishes reference, import, mapping and extension and records coverage/reuse limitations. Broader source integration is not required by the core. Existing upstream publications/panels/registries are provenance dependencies, not independent bulk-acquisition approvals.
- **Consequences / dependencies:** Other sources/ontologies require a demonstrated CQ/representation need and owner review. Exact versions/artifacts, licences, eligibility rules and snapshot/checksum procedures remain unfrozen. Depends on D002/D003/D009; unresolved acquisition issues must be resolved before affected reuse, not assumed away by M0 approval.

### D009 — Semantic requirements

Status: **APPROVED**. Approval: M0 Freeze / Checkpoint 4, 2026-09-17.

- **Question / proposed decision:** Freeze [R1–R14](../competency_questions.md#r1r14-approved-semantic-requirements) as requirements for the M1 model, with the Q01–Q07 crosswalk. No classes, properties or implementation names are selected.
- **Alternatives / evidence / rationale:** Task 004's seven grouped requirements are accepted investigation material. Task 005 separates them into fourteen stable, reviewable distinctions rather than choosing an ontology from source schemas.
- **Consequences / dependencies:** M1 must explain how its proposed model satisfies each requirement and exposes limitations. Changing a requirement needs owner review. Depends on D003/D004/D007/D008.

### D010 — Validation boundaries

Status: **APPROVED**. Approval: M0 Freeze / Checkpoint 4, 2026-09-17.

- **Question / proposed decision:** Distinguish reasoning/consistency, structural constraints, identity/mapping, query checks, provenance completeness, evidence existence, claim scope and answer support. These are potential layers, not a frozen architecture.
- **Alternatives / evidence / rationale:** D001/[charter](../project_charter.md) reject treating a validator as biomedical truth. The [evaluation protocol](../evaluation_protocol.md) carries that distinction into the proposed freeze.
- **Consequences / dependencies:** Each later check must name its property, assumptions and error limits. No requirement to implement every listed layer; OWL/SHACL cannot establish biomedical truth. Depends on D009/D011/D012.

### D011 — Evaluation commitments and timing

Status: **APPROVED**. Approval: M0 Freeze / Checkpoint 4, 2026-09-17.

- **Question / proposed decision:** Keep design, development and held-out questions separate. Evaluate supported completion, unsupported broadening, qualification, abstention, direct/propagated distinction, mechanism/indication distinction, disease scope and provenance completeness. No held-out set exists.
- **Alternatives / evidence / rationale:** The [protocol](../evaluation_protocol.md) retains matched access and leakage/dependency safeguards. Task 005 expressly leaves final metrics, benchmark size and statistics open; this is narrower than reading the bootstrap exit criterion as a completed executable protocol.
- **Consequences / dependencies:** Accept design-level evaluation commitments for M0; defer independent labels/reviewer arrangements, final protocol/statistics and held-out custody/access to explicit later gates before affected execution or exposure. No development tuning on final held-out questions. Final protocol/access rules must be frozen before tuning against the final evaluation set; M7 is execution. Depends on D004/D005/D010/D012. Approval must include this staged exit interpretation; otherwise M0 evaluation readiness remains unresolved.

### D012 — Review and claim boundary

Status: **APPROVED**. Approval: M0 Freeze / Checkpoint 4, 2026-09-17.

- **Question / proposed decision:** Current work is TECHNICAL SOURCE REVIEW. No clinician, neurologist or biomedical domain-expert adjudication, and no biomedical ground-truth labels, are claimed. Future expert involvement must be explicitly documented.
- **Alternatives / evidence / rationale:** Tasks 003/004 restrict answers to inspected evidence/depth, not an assumed expert gold standard. [Core A–E boundaries](../competency_questions.md) preserve qualification and abstention.
- **Consequences / dependencies:** No silent promotion of metadata correctness to causal or therapeutic truth. Unavailable text and ambiguous mappings remain visible. Future domain-level claims need an appropriate review plan; technical source claims can guide M1. Depends on D004/D010/D011.

### D013 — Duplication risk and novelty

Status: **APPROVED**. Approval: M0 Freeze / Checkpoint 4, 2026-09-17.

- **Question / proposed decision:** Retain duplication risk for dementia/AD KGs, GraphRAG, KG-grounded biomedical QA, ontology-grounded LLMs and claim verification. Novelty remains **NOT YET VERIFIED**.
- **Alternatives / evidence / rationale:** The existing [related-work scan](../related_work.md) documents overlapping formulations; changing disease, adding an LLM or adding verification is not evidence of novelty. No new literature search in Task 005.
- **Consequences / dependencies:** A later evidence-backed assessment must support any specific contribution claim. Lack of a proven novelty claim does not itself block semantic design. Depends on D005/D006; no superiority claim authorized.

### D014 — Deferred scope and unselected technology

Status: **APPROVED**. Approval: M0 Freeze / Checkpoint 4, 2026-09-17.

- **Question / proposed decision:** Defer broad phenotype/frequency comparisons, processes/pathways, unrestricted dementia/FTD descendants, KG embeddings, link prediction, graph ML, agents and Neo4j/property-graph projection from core V1. Deferred is not permanently rejected.
- **Alternatives / evidence / rationale:** Earlier breadth/architecture options remain in the historical documents. Tasks 004/005 favor the smallest boundary meeting the seven questions; no technology comparison is invented here.
- **Consequences / dependencies:** M0 selects none of Neo4j, property-graph projection, Fuseki deployment architecture, embedding model, vector database, LLM provider/model, prompt framework, LangChain, LangGraph, agent count/decomposition, API framework, UI, Docker/deployment architecture, observability stack, KG embedding model or GNN/graph ML architecture. Revisit only on a concrete requirement with owner approval. Depends on D003/D005/D007; no hidden technology mandate.

## Approval and later gates

The owner has approved D002–D014 and authorized M1 entry. The [M0 plan](../m0_plan.md) records the approved entry brief and still-incomplete later work. Do not begin M1 automatically after this checkpoint. Exact semantic model/import/provenance and source-acquisition choices remain reviewable M1/M2 decisions; later evaluation gates remain mandatory. This checkpoint authorizes the local documentation commit, not acquisition, deployment, experiments or a push. Future changes to frozen decisions require explicit owner approval and preserved decision history.
