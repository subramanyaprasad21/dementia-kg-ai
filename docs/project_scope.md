# Project scope

Task 002 assessment, clarified by Task 002A, 2026-09-16–17 (Asia/Kolkata). Status: PROVISIONAL; no scope or source selection approved. Evidence is recorded in the [source audit](source_audit.md); duplication risks are in [related work](related_work.md).

The intended task remains research knowledge answering from a documented evidence collection. Individual diagnosis, treatment recommendations, and clinical decision support are excluded. Transformation Fidelity and the T2DM KG remain separate projects. This project's intended extension is controlled evaluation of retrieval, grounding, and defined verification properties, not another disease-specific integration exercise.

## Three options

Option A is Alzheimer disease only. Option B is the four candidate anchors Alzheimer disease, Lewy body dementia, vascular dementia, and frontotemporal dementia, with membership still negotiable. Option C expands to a wider dementia/neurodegenerative hierarchy. These options are knowledge boundaries, not OWL designs.

The four anchors exist as non-obsolete Mondo concepts and resolve in OT 26.06. Source concept existence does not establish equivalent clinical scope or usable coverage for every relation. The intended DLB boundary and granularity of FTD need owner review.

| Criterion | A — Alzheimer only | B — four candidate dementias | C — broad spectrum |
| --- | --- | --- | --- |
| Disease concepts | MONDO:0004975 verified; subtype inclusion undecided. | Four anchors verified; overlapping labels and subtype boundaries need review. | Dementia hierarchy exists; full dementia/neurodegenerative closure not verified or enumerated. |
| Phenotypes | OT returns 17 rows, with mixed source disease IDs; usable clean count unknown. | OT returns 17/7/0/0; HPO has narrower FTD annotations. Balanced broad-disease coverage not established. | Expanded coverage NOT YET VERIFIED; cannot extrapolate from rare-disease annotations. |
| Target/gene associations | 13,289 distinct target IDs in OT direct associations; substantial eligibility review needed. | All four have records; distinct target IDs in OT direct associations range from 808 to 13,289. | Dementia parent: 14,795 targets with descendant inclusion versus 3,089 direct; neither is a full-spectrum usable graph count. |
| Drug/target coverage | 440 OT indication records; mechanisms not comprehensively audited. | Indication records for all four; sampled rivastigmine links to ACHE/BCHE mechanisms. | Expanded coverage NOT YET VERIFIED; more stages, indications, and identifiers to review. |
| Evidence/provenance | Sample APP evidence has a publication ID but null original disease fields. | Evidence sampled for one target per anchor; missing references and source-label differences observed. | Schemas exist; full provenance coverage NOT YET VERIFIED; review surface grows. |
| Identifier consistency | Same Mondo anchor in OLS/OT helps; source annotation IDs still vary. | Four common IDs reduce matching work; source granularity/synonyms differ. | Mixed namespaces, obsolete mappings, and added disease families increase review. |
| Ontology alignment | One bounded context; latest Mondo still differs in date from OT. | Manageable with explicit anchors/subtypes and tracked propagation. | Multiple inheritance and unrestricted closure complicate inclusion and interpretation. |
| Cross-disease questions | No between-disease comparisons; within-AD source/subtype comparisons possible. | Supports investigating shared/distinct associations and coverage; actual overlap unmeasured. | More comparisons possible, but source heterogeneity may dominate interpretation. |
| Data imbalance | Source/subtype imbalance persists despite one disease. | Observed order-of-magnitude target disparity and phenotype gaps require disease-stratified reporting. | Likely more exposure to imbalance (inference); distribution NOT YET VERIFIED. |
| Integration difficulty | Lowest relative burden; evidence semantics still nontrivial. | Moderate with a small core; high if all four require equal phenotype/drug depth. | Highest relative burden with open-ended branches and requirements. |
| Evaluation difficulty | Simplest stratification/manual review; limited transfer claims. | Needs disease/source strata and explicit missingness; cannot assume symmetric coverage. | Hardest to interpret one contrast across changing task/source mixtures. |
| Published-work overlap | Direct overlap with AlzKB, DALK, KRAGEN, ESCARGOT, and Alzheimer GraphRAG evaluation. | Wider scope is not novelty; AlzKB already includes related neurodegenerative scope. | Broad biomedical KG/RAG work exists; expansion does not avoid duplication. |
| Timeline feasibility | Most feasible relative option with tight time/review capacity. | Conditionally feasible if staged; four equally rich slices not justified yet. | Defer; no defensible estimate without a fixed closure/source plan. |

Difficulty and timeline assessments are design inferences from coverage and dependencies, not measured build times. Owner availability, deadline, compute/API budget, and reviewer capacity remain unknown; no calendar estimate is claimed.

## Task 002A: AD + LBD candidate versus AD + FTD

Here “LBD candidate” means the **source-defined MONDO:0007488 record**, not the clinical umbrella including Parkinson's disease dementia. FTD means **MONDO:0017276**, not automatically its descendants or a phenotype-rich replacement subtype. AD means **MONDO:0004975**. Exact source identities, synonyms and hierarchy differences are recorded in the [boundary audit](source_audit.md#task-002a-exact-candidate-boundaries).

Clinical context, rather than proposed graph assertions: Mondo/OT describe the LBD record through Lewy-body pathology and overlap with Alzheimer/Parkinson presentations; they describe FTD through behavioral, executive and language changes with frontotemporal degeneration. Official NIA indexed extracts describe AD amyloid/tau pathology, tau/TDP-43 involvement in FTD, and AD/Lewy pathology co-occurrence. Sources: [AD fact sheet](https://www.nia.nih.gov/health/alzheimers-and-dementia/alzheimers-disease-fact-sheet), [FTD overview](https://www.nia.nih.gov/health/frontotemporal-disorders/what-are-frontotemporal-disorders-causes-symptoms-and-treatment), [mixed pathology context](https://www.nia.nih.gov/10-years-alzheimers-disease-and-related-dementias-research/advanced-understanding-dementia-risk). Direct NIH pages were access-blocked; these limited contextual claims use official indexed extracts. They do not establish a binary molecular partition or patient-level diagnostic task.

| Criterion | AD + source-defined LBD record | AD + FTD |
| --- | --- | --- |
| Biological/clinical distinction | Different pathological emphasis with overlapping dementia manifestations; mixed pathology complicates a simple AD-versus-LBD dichotomy. | Behavioral/language/executive emphasis and a heterogeneous disease family; shared tau involvement means it is not simply molecularly disjoint from AD. |
| Overlap with AD | Source definition explicitly notes overlap; clinical co-occurrence does not imply identical graph nodes. Actual shared target/phenotype sets unmeasured. | Clinical overlap and shared protein context do not define identical syndromes. Actual shared target/phenotype sets unmeasured. |
| Target-association coverage | 1,306 distinct target IDs in OT direct associations versus AD's 13,289. Sufficient presence to investigate; not evidence of a balanced usable slice. | 2,454 versus AD's 13,289. Larger inventory than LBD is not a selection argument without evidence/source eligibility. |
| Phenotype feasibility | Seven stored endpoint entries versus AD's 17; sampled duplicates, IEA/source-ID issues and null HPO resolution limit apparent advantage. | Zero at the broad OT anchor; direct HPO subtype annotations exist. Investigate subtype-qualified use; broad FTD cannot inherit them without an explicit justified interpretation. |
| Evidence/provenance | SNCA sample has source OMIM:127750 and no literature IDs; does not establish lower or higher overall provenance quality. | MAPT sample has literature IDs but source Pick disease/OMIM:172700, exposing granularity mismatch. One sample cannot rank provenance quality. |
| Cross-disease competency questions | Potentially useful for separating shared manifestations/associations from distinct source identities and evidential support. Clinical overlap is context, not a measured graph intersection. | Potentially useful for distinguishing broad-family from subtype support and comparing evidence across disease families. Needs intentional granularity. |
| Multi-hop graph questions | Disease–association–evidence routes are plausible; one rivastigmine mechanism sample supports investigating drug–target joins. No complete disease–target–drug path set verified. | Disease/subtype–association–evidence offers a concrete hierarchy composition candidate. Drug indications exist but comparable mechanism paths were not sampled. Lack of sampling is not evidence of absence. |
| Risk of trivial similarity/difference | Shared generic symptoms or a familiar gene name could make questions answerable without relational evidence; label ambiguity could dominate performance. | Obvious behavior-versus-memory wording, absent phenotype rows, or retrieval of only a subtype label could produce trivial contrasts. Broad-to-subtype questions must genuinely require composition. |
| Source imbalance | Strong raw target-count imbalance; phenotype presence could hide evidence duplication/source granularity. Post-filter balance unknown. | Smaller raw count gap does not establish better balance. Subtype annotations and broad associations can be asymmetrically mixed. Post-filter balance unknown. |
| Evaluation feasibility | No children returned for the second anchor reduces that local hierarchy surface, but clinical label ambiguity and provenance still need review. | More explicit subtype relationships support propagation tests but add adjudication work. Current Mondo and OT immediate parents differ. |
| Published-work overlap | Existing Alzheimer/related-neurodegenerative KGs and QA methods remain relevant; this exact pairing's novelty or prior evaluation is NOT YET VERIFIED. | Same general overlap; adding FTD does not establish novelty. No verified head-to-head result favors this pairing. See the existing focused scan. |
| What it could teach experimentally | Under fixed retrieval, test whether a defined check prevents unsupported equivalence, causal/treatment wording, and claim transfer across ambiguous source labels; conditional on reviewable examples. | Under fixed retrieval, test whether a defined check preserves source disease/subtype scope and avoids unjustified upward/downward generalization; conditional on reviewable examples. |

These are design inferences and possible experimental emphases, not approved contrasts or a promise of performance. Both pairings can support association-provenance questions. Neither has measured post-filter coverage, shared-target overlap, matched multi-hop support, or an independently reviewed question set. Selection based on the current unequal sampling would favor whichever candidate happened to receive more inspection.

## Revised recommended knowledge boundary

**Task 002A revises the earlier preference: the second anchor remains UNDECIDED between MONDO:0007488 and MONDO:0017276.** Retain AD as the provisional reference anchor and a two-anchor subset of Option B as a candidate, not an approved scope. Seven phenotype entries do not justify preferring LBD; 2,454 target associations do not justify preferring FTD. The first recommendation placed too much weight on endpoint phenotype presence without demonstrating usable comparative question coverage.

Conditional choice: favor the LBD source record only if name-boundary/overlap questions have reviewable, source-qualified evidence and its intended boundary is acceptable. Favor FTD if subtype/propagation questions are central and independently reviewable at a deliberately chosen family/subtype granularity. If both can support the chosen contrast, prefer the one with lower demonstrated curation burden under the same review criteria, not higher counts. If cross-disease comparison adds no necessary relational question, Option A remains viable.

The candidate core remains disease identity, bounded hierarchy, qualified disease–target associations, association evidence, and provenance. Phenotype and drug-mechanism extensions remain conditional; GO/process expansion remains deferred. Vascular dementia and Option C remain deferred. This does not promote FTD descendants or the clinical LBD umbrella into scope.

Before selecting an anchor, an owner-authorized next M0 step should inspect a comparably bounded sample for both candidates under the same proposed evidence/source rules, preserving original disease IDs and qualifiers. Assess whether each can support reviewable relation-composition questions, necessary shared/distinct evidence, and realistic manual adjudication. Do not use Task 002/002A examples as held-out evaluation material. No new sampling exercise, question freeze, or Task 003 is initiated here.

## What this boundary excludes or loses

Either two-anchor scope cannot support claims about dementia generally or balanced four-disease symptom comparison. Choosing the LBD record loses FTD subtype comparisons; choosing FTD loses LBD/DLB name-boundary comparisons. Neither includes vascular mechanisms or an unrestricted FTD spectrum. It offers limited generalization across disease families. Deferring GO/pathway expansion loses process-mediated explanations; deferring unrestricted literature extraction loses open-ended coverage of recent findings. These losses are acceptable only if retained questions justify a primary experimental contrast.

Retaining a record does not authorize claims that an associated gene causes a disease, a linked drug treats it, or missing evidence establishes biological absence. No patient-level records, clinical recommendations, generic disease-relatedness edges, unrestricted descendant closure, or automatic xref equivalence are proposed.

## Consequences for competency-question design

Prioritize source-qualified association retrieval, evidence attribution, disease-name ambiguity, direct versus propagated support, and bounded comparisons. Optional multi-hop questions must ask what relationships are recorded, not infer treatment from disease–target–drug connectivity. Phenotype questions must name the source disease/subtype and preserve qualifiers.

These are question families, not validated questions or gold labels. Check that some comparisons require real relation composition rather than two disconnected lookups. Distinguish source insufficiency from retrieval failure and invalid biological conclusions. Source observations used here are design material, not unbiased evaluation examples; held-out questions remain separate.

## Owner decisions required

1. Decide whether a two-anchor subset of B is needed versus A; second anchor remains undecided between the source-defined LBD record and FTD. Review the exact boundary and continued vascular deferral.
2. Decide whether cross-disease comparison is essential to the research task; it is not itself a contribution.
3. Approve source roles: Mondo disease reference, HPO conditional phenotype use, OT association evidence, EFO alignment dependency; GO deferred.
4. Resolve HPO distribution route and annotation eligibility before adoption, including upstream reuse restrictions.
5. Establish evidence inclusion rules, original-versus-propagated semantics, phenotype granularity, and handling of duplicate/unresolved records. No mapping strategy is frozen.
6. Establish review capacity, deadline, and compute/API budget before assigning a timeline.
7. Authorize the next bounded M0 investigation and competency-question drafting; primary contrast and evaluation protocol remain unfrozen.
