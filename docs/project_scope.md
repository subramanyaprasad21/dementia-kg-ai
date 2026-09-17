# Project scope

## Current recommendation after Task 004 — not approved

2026-09-17. **Recommend option A from Task 004: freeze bounded AD+FTD for M1 in the separate Task 005 owner review.** This is a recommendation to that review, not a freeze or permission to start M1. AD MONDO:0004975 and FTD MONDO:0017276 remain the two proposed anchors; AD-only remains a credible fallback until the owner decides. The evidence now supports seven technically reviewable source-bound questions, not clinical adjudication. See [current core and M1 requirements](competency_questions.md#task-004-proposed-core--owner-review-pending) and [deeper source review](source_audit.md#task-004-technical-source-review).

### What FTD adds, and what AD alone already supplies

| Requirement / value | AD-only capability | Increment from the inspected FTD cases |
| --- | --- | --- |
| Evidence support versus citation presence | PSEN1 and mechanism references suffice. | Same-target, different-source comparison with FTD; useful contrast, not a new logical capability. |
| Source disease versus normalized anchor | AD9 susceptibility annotation already exposes broadening. | Pick→FTD direct mapping plus historical terminology offers a deeper traced example; no whole-family genetic claim needed. |
| Descendant interpretation | APP/AD1 already suffices. | Second explicit path allows comparison with direct normalization; duplication acknowledged, no unique FTD requirement. |
| Contextual mapping ambiguity | No analogous two-assignment case established in the audited AD-only bundle. | OMIM:600274 has two inspected normalized destinations; provenance must retain ambiguity without global repair. Unique to this **sample**, not to FTD biology or all possible AD data. |
| Evidence dependence | Generic risk exists with any reused source. | Concrete GRIN1/GRIN3B records share memantine/report provenance; tests an otherwise hidden dependency. An AD equivalent was not established here. |
| Mechanism versus clinical population | AD mechanisms/stages can test basic separation. | An FTD-labelled indication links to restrictive registry cohorts; paired with a MAPT drug lacking an exact FTD indication, it avoids relying entirely on easy missing-edge negatives. |

**FTD is justified as bounded design material, not because a second disease is logically necessary.** AD-only can adequately test the generic disease-scope verification hypothesis. FTD adds actual inspected mapping/dependency/population cases and a shared-target comparison without new source categories. That incremental value is proportionate if claims remain technical and acquisition stays bounded; review hours, expert availability and future sample-size feasibility have not been measured. Neither better experimental performance nor unique graph necessity follows. Recommend AD-only if the owner cannot support review of contextual mappings/populations; no replacement anchor is justified by this pass.

### Proposed boundary for Task 005

Direct normalized-anchor associations remain the core boundary. Preserve original narrower disease labels and separately labelled diagnostic paths; never pool every descendant's evidence into the anchor. Context is limited to records required by Q01–Q07: Pick MONDO:0008243; semantic dementia MONDO:0010857; bvFTD MONDO:0017160 as an intermediate classification node; AD1 MONDO:0007088, early-onset autosomal dominant AD MONDO:0015140 and familial AD MONDO:0100087 as the inspected AD path. These are supporting context, not additional disease cohorts. Other observed parents and late-onset AD remain audit history, not a requirement to collect more associations. Trial population text stays source-local until separately justified mapping exists.

Mondo is proposed as a disease reference/alignment resource with explicit path context; no wholesale import decision. OT is proposed for bounded association/evidence and optional mechanism/indication records, with upstream source references. HPO clinical comparison and processes/pathways remain deferred. Publication inspection and registry links support claim boundaries; they do not authorize full-text redistribution or an expanded literature KG. Source-route permissions and artifact choices still require owner review before acquisition.

### Losses, uncertainties and owner gate

This boundary loses LBD/PD-specific naming and SNCA cases, phenotype discrimination, broad dementia coverage and subtype-wide biological comparisons. Restricting to source-record claims also gives up positive causal, therapeutic and clinical-generalization conclusions. Keeping FTD costs more contextual review than AD-only. Historical LBD findings remain preserved.

Remaining uncertainty: exact OT input panel snapshots/mapping rules, inaccessible source bodies, biomedical validity of classifications, eligible post-filter corpus size, independent human review, and incremental graph benefit. These are not silently resolved. For the proposed technical scope they can be represented as explicit limits rather than requiring another open-ended M0 search; any positive biomedical answer requiring them stays out of scope.

Owner decisions: accept/revise this boundary or choose AD-only; review the seven core rubrics and the absence of expert adjudication; select source routes and review capacity; consider the recommended primary research emphasis and evaluation safeguards. Task 005 should turn approved choices into a coherent M0 freeze record and identify any genuinely blocking issue. It must not equate accepting this investigation with authorizing M1 implementation.

## Historical Task 002–003 scope investigation

Task 003 assessment, 2026-09-17 (Asia/Kolkata); Task 002/002A history retained below. Status: PROVISIONAL; no scope or source selection approved. Evidence is recorded in the [source audit](source_audit.md); duplication risks are in [related work](related_work.md).

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

## Checkpoint 1 recommendation — historical, superseded by Task 003 proposal

**Task 002A revises the earlier preference: the second anchor remains UNDECIDED between MONDO:0007488 and MONDO:0017276.** Retain AD as the provisional reference anchor and a two-anchor subset of Option B as a candidate, not an approved scope. Seven phenotype entries do not justify preferring LBD; 2,454 target associations do not justify preferring FTD. The first recommendation placed too much weight on endpoint phenotype presence without demonstrating usable comparative question coverage.

Conditional choice: favor the LBD source record only if name-boundary/overlap questions have reviewable, source-qualified evidence and its intended boundary is acceptable. Favor FTD if subtype/propagation questions are central and independently reviewable at a deliberately chosen family/subtype granularity. If both can support the chosen contrast, prefer the one with lower demonstrated curation burden under the same review criteria, not higher counts. If cross-disease comparison adds no necessary relational question, Option A remains viable.

The candidate core remains disease identity, bounded hierarchy, qualified disease–target associations, association evidence, and provenance. Phenotype and drug-mechanism extensions remain conditional; GO/process expansion remains deferred. Vascular dementia and Option C remain deferred. This does not promote FTD descendants or the clinical LBD umbrella into scope.

Before selecting an anchor, an owner-authorized next M0 step should inspect a comparably bounded sample for both candidates under the same proposed evidence/source rules, preserving original disease IDs and qualifiers. Assess whether each can support reviewable relation-composition questions, necessary shared/distinct evidence, and realistic manual adjudication. Do not use Task 002/002A examples as held-out evaluation material. This was the Checkpoint 1 proposal; the owner subsequently authorized the bounded Task 003 audit below. No question freeze was authorized.

## What this boundary excludes or loses

Either two-anchor scope cannot support claims about dementia generally or balanced four-disease symptom comparison. Choosing the LBD record loses FTD subtype comparisons; choosing FTD loses LBD/DLB name-boundary comparisons. Neither includes vascular mechanisms or an unrestricted FTD spectrum. It offers limited generalization across disease families. Deferring GO/pathway expansion loses process-mediated explanations; deferring unrestricted literature extraction loses open-ended coverage of recent findings. These losses are acceptable only if retained questions justify a primary experimental contrast.

Retaining a record does not authorize claims that an associated gene causes a disease, a linked drug treats it, or missing evidence establishes biological absence. No patient-level records, clinical recommendations, generic disease-relatedness edges, unrestricted descendant closure, or automatic xref equivalence are proposed.

## Consequences for competency-question design

Prioritize source-qualified association retrieval, evidence attribution, disease-name ambiguity, direct versus propagated support, and bounded comparisons. Optional multi-hop questions must ask what relationships are recorded, not infer treatment from disease–target–drug connectivity. Phenotype questions must name the source disease/subtype and preserve qualifiers.

These are question families, not validated questions or gold labels. Check that some comparisons require real relation composition rather than two disconnected lookups. Distinguish source insufficiency from retrieval failure and invalid biological conclusions. Source observations used here are design material, not unbiased evaluation examples; held-out questions remain separate.

## Task 003 matched-audit comparison

The [sampling protocol and record inventory](source_audit.md#task-003-matched-sampling-protocol--written-before-new-examples) were written before new examples. The [design question records](competency_questions.md) were drafted afterwards. This is a small, rank-biased inspection of three targets per disease and fixed evidence strata, not comprehensive or representative disease coverage. An extra predeclared bvFTD inspection was an asymmetric granularity diagnostic and is not credited as matched coverage.

| Criterion | AD + source-defined LBD | AD + source-defined FTD |
| --- | --- | --- |
| Provisionally usable questions | Six CANDIDATE records out of eight drafts, plus one deferred and one rejected; no independent human validation. | Same counts. Equal totals are not a tie-breaking score; several shared templates occur across scopes. |
| Diversity | Source-component comparisons, publication support, mechanism/indication distinctions, identity and annotation-quality controls. | Same core families plus observed source-ID mapping divergence and original clinical-population versus broad indication scope. |
| Multi-hop potential | Concrete SNCA drug paths terminate in indications for other disease/phenotype concepts; useful unsupported-transfer cases. | Concrete MAPT paths include both another-disease indication and a traceable FTD-labelled indication with narrower original trial conditions. |
| Provenance depth | PSEN1 EP publication abstract and prasinezumab trial traced; SNCA panel assertion remains inaccessible. | PSEN1 EP and first GE citation abstract plus gosuranemab trial traced; panel details inaccessible. Extra GE abstract is due to source presence, not a full matched literature review. |
| Semantic ambiguity | MONDO LBD label versus clinical umbrella; related AD synonym and a phenotype entry resolving to dementia. | Broad FTD versus Pick/semantic dementia/FTLD source labels; same OMIM ID appears with different normalized diseases in sampled records. |
| Hierarchy complexity | No children in the audited LBD node; AD already supplies a nontrivial propagation control. | FTD adds a second propagation example and family/subtype granularity. Greater complexity is a cost and must be bounded. |
| Phenotypes | Three returned entries reveal duplicate annotations, missing frequency and mixed entity resolution. | Broad and bvFTD OT counts zero; direct HPO subtype page has annotations with insufficient inspected qualifier/provenance detail. Both pairings defer clinical phenotype comparisons. |
| Drug-path feasibility | Two sampled SNCA drugs have no exact LBD indication in their returned lists; one mechanism lacks references. | Two sampled MAPT drugs: zagotenemab has AD/tauopathy indications; gosuranemab has FTD PHASE_1 and a terminated, narrower-population trial. No efficacy claim. |
| Evidence comparability | GW strata present in all three LBD seed associations; GE only for SNCA. Compared with AD, source mixtures differ. | GE strata present for all three FTD seeds; GW strata empty in those seeds. Not comparable as equal amounts/types of genetic evidence. |
| Imbalance | Within the nine-target universe, seven shared with AD; source-filtered usable population still unknown. | Nine shared with AD in that universe, with CP-only GRIN1/GRIN3B in FTD. Greater overlap does not imply stronger support. |
| Curation burden | Name boundary, missing source fields and reference gaps require careful review. | More source-granularity, mapping and trial-population review; likely higher burden, qualitative inference only. |
| Evaluation burden | Positive metadata questions and bounded insufficiency cases exist; drug questions could overrepresent easy negative answers. | Both present and absent exact indications allow more varied claim-support criteria; broad labels require specialist review. No measured balance or sample-size adequacy. |
| Triviality risk | L04–L06 are low-hop/metadata controls answerable from complete source chunks; a second disease is not essential to those tasks. | Several controls are also table-answerable. F02–F05/F07 offer explicit multi-record dependencies but have not been tested against text retrieval. |
| Unsupported biological interpretation | Risk of upgrading text-mining links to causality or importing PD indications into LBD. | Risk of upgrading broad association/indication mapping to all-FTD causality or efficacy and treating clinical-precedence joins as independent confirmation. |
| Distinction from T2DM project | Only if the work evaluates qualified evidence and claim-support behavior under controlled conditions; same OT extraction alone is insufficient. | Same requirement; observed contextual mapping/indication cases give concrete design material, not proof of a contribution. T2DM code was not audited. |
| Published-work distinction | Existing dementia KG/RAG and verification work remains directly relevant. | Same; no novelty claim from FTD inclusion, provenance or a verifier. A paper-level matched comparison still requires review. |

## Task 003 recommended boundary — PROVISIONAL

**Recommend AD + the source-defined FTD family anchor for the next M0 review, with bounded subtype/source context.** AD is MONDO:0004975; FTD is MONDO:0017276. This revises the Checkpoint 1 undecided recommendation without recording owner approval. The reason is the observed combination of shared-target evidence differences, context-dependent source mappings, and a traceable clinical indication whose original population is narrower than its normalized disease. It is not FTD's raw count or the number of questions.

The broad FTD anchor is sufficient for the current direct association comparison; substituting bvFTD alone would discard the associations actually audited without demonstrating replacement coverage. A whole FTD subtree is unnecessary. A bounded family-plus-context representation is useful to preserve why evidence must not be generalized, but must not pool all subtype annotations into FTD.

Candidate context is limited to records actually encountered: Pick disease MONDO:0008243 (direct evidence's original label/context), behavioral variant of FTD MONDO:0017160 / ORPHA:275864 (separate, currently deferred phenotype diagnostic), and semantic dementia MONDO:0010857 (returned only by the inclusive diagnostic; exact hierarchy path still NOT YET VERIFIED). OMIM:172700 and OMIM:600274 remain original-source identifiers, not new globally equivalent disease anchors. Trial source populations such as FTLD with tau inclusions and symptomatic MAPT carriers must remain original report context until mappings are justified; do not invent new ontology concepts for them here. These context records are not additional co-equal disease anchors or authorization to ingest their data.

AD remains direct-anchor-only for core sampling. Its observed AD1 MONDO:0007088 and late-onset EFO:1001870 records remain separately labelled propagation diagnostics. No automatic descendant closure is selected for either anchor. Process/pathway relations remain deferred; phenotype discrimination remains deferred; drug paths are optional statement/provenance tests, never treatment recommendations.

The recommendation is conditional on owner review capacity for these distinctions. **AD-only is a credible fallback**, with four source-bound candidate controls demonstrating propagation, provenance and drug-stage distinctions already. If the extra FTD questions collapse to redundant templates or cannot receive reliable review, the smaller scope is preferable. LBD remains a documented alternative, not a rejected disease; it offers useful PD/LBD boundary and missing-reference examples.

## Task 003 losses and implications

Following the recommendation loses the focused LBD/PD name-boundary and SNCA mechanism-without-LBD-indication cases. It does not support claims about dementia generally, disease-exclusive genes, phenotype discrimination, comparative efficacy, or broad FTD clinical generalization. Restricting subtype context loses wider hereditary/clinical subtype coverage and process-mediated explanation. These are deliberate scope costs, not missing implementation tasks.

The evidence most strongly suggests investigating **provenance-aware claim-scope verification with retrieval held fixed**: can a defined check prevent an answer from turning a mapped association, mechanism, subtype record or clinical report into a broader unsupported claim? Semantic grounding and subtype scope are components to define, not simultaneous independent primary claims. Graph retrieval remains an alternative contrast; this audit did not show it outperforms vector retrieval or that its information is unique to graphs.

## Owner decisions required after Task 003

1. Accept/revise the AD+FTD recommendation, retain the LBD alternative, or choose AD-only; approve exact anchor and context boundaries separately from accepting this audit.
2. Decide whether the extra cross-disease/mapping questions add enough value beyond the AD-only controls to justify FTD review burden.
3. Review candidate answer criteria, minimum provenance depth and acceptable treatment of inaccessible original assertions. No clinician/expert review is assumed.
4. Select evidence eligibility for a later collection; current three-source strata are an audit design, not approved ingestion rules. Resolve source-route/licensing matters before acquisition.
5. Authorize a bounded Task 004 reviewer-rubric and evidence-adjudication pass, including redundancy reduction and review of the most promising records. No ontology design or primary-experiment freeze is recommended yet.
6. Establish reviewer availability, time and budget; none is inferred from this small sample.
