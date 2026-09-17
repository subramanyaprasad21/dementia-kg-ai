# Competency questions

Task 003, 2026-09-17. Status: DESIGN candidates only; not owner-approved, not human-adjudicated, not frozen, and never held-out evaluation material. Drafted after the bounded evidence inspection in [source_audit.md](source_audit.md#task-003-evidence-observations). No KG or question execution system exists.

## Set separation and interpretation

Design questions guide scope; development questions later support tuning; held-out questions require a separately approved freeze and access policy. These examples and close paraphrases have been exposed during design and cannot serve as unbiased held-out evidence. Question totals are not sample-size justifications or a reason to add weak questions.

`Verified` below means that the named metadata or text was inspected, not that a biomedical claim was validated or a graph query executed. CANDIDATE means a bounded answer rubric is plausible for owner review; REVISE/DEFER/REJECT do not count as usable candidates. No human expert review is claimed. Hop descriptions describe information dependencies, not proposed ontology properties/classes or measured query plans.

## Source and evidence key

All T3 references point to the labelled sections in the source audit: T3-T ranked targets; T3-X fixed-universe comparisons; T3-E evidence IDs/counts; T3-H direct/inclusive diagnostics; T3-P phenotype metadata; T3-D mechanisms/indications/reports; T3-R publication tracing. OT means Open Targets 26.06; original-source releases are not necessarily known. Full evidence IDs and exact API recipes are preserved in that audit; shortened IDs below uniquely identify its entries.

Graph-value labels: G1 explicit relation lookup; G2 multi-hop traversal; G3 cross-disease comparison; G4 provenance/evidence tracing; G5 ontology/hierarchy reasoning; G6 ambiguity/identifier resolution; G7 unsupported-claim detection; G8 abstention/missing-evidence reasoning. Labels describe potential value, not measured benefit.

Common caveat for every record: none depends on facts uniquely available in a KG. Relational joins or suitably structured documents could represent the same information. Ordinary text retrieval may answer correctly when it retrieves a complete bundle. Any eventual graph comparison must use matched knowledge access and test the benefit rather than assuming it.

## AD+LBD design question records

### L01 — CANDIDATE

**Question:** Within the fixed nine-target universe U, which targets have an OT direct association for both AD and the LBD record, and which shared targets have a GWAS component in LBD but not AD?

- **Scope / type:** AD+LBD; Comparison.
- **Entities:** AD, LBD, all nine T3-T targets.
- **Relation families / expected path:** disease–target association; association–source components. Two disease→association→target branches joined by target ID; then source components (2–3 links per branch).
- **Sources and required evidence/provenance:** T3-X; OT 26.06 direct Bs query.
- **Provisional answer criteria:** Seven shared IDs; SNCA and GBA1 have GW in LBD but not AD in these returned source components. List IDs and source settings; do not say biologically LBD-specific.
- **Answerability:** Verified for this finite metadata universe; underlying GWAS claims not adjudicated.
- **Graph value:** G1 G3 G4 G8. Structured intersection and source-conditioned comparison; not the largest overlap.
- **Non-triviality / LLM and vector alternative:** Memorized genes cannot supply the exact release-specific inventory. Vector retrieval over a prepared comparison table could answer readily; benefit needs a matched-source comparison.
- **Likely ambiguity:** No GW component here is source-scoped missingness, not negative genetic evidence.
- **Review burden:** Medium; qualitative estimate, no review time or expert availability measured. **Status:** CANDIDATE.

### L02 — CANDIDATE

**Question:** For PSEN1 in AD and LBD, trace the sampled Europe PMC evidence IDs to their publications. Does the inspected material support calling PSEN1 a cause of LBD?

- **Scope / type:** AD+LBD; Evidence/claim support.
- **Entities:** PSEN1, AD, LBD, PMIDs 33008897 and 38512130.
- **Relation families / expected path:** association–evidence; evidence–publication; provenance. Disease→association→evidence→publication, two branches.
- **Sources and required evidence/provenance:** T3-E, T3-R; OT plus four-publication lookup subset.
- **Provisional answer criteria:** Distinguish evidence IDs 1261ad02… and fa93de0b… and the two papers. The LBD paper's inspected abstract compares multiple conditions; causal assertion is not established by this inspection. Do not claim the full paper disproves causality.
- **Answerability:** Trace and abstract inspection verified; definitive biomedical answer NOT YET VERIFIED.
- **Graph value:** G2 G3 G4 G7 G8. Bind each citation to the correct disease-specific evidence and state inspection limits.
- **Non-triviality / LLM and vector alternative:** Abstract retrieval could support the caution; a bare LLM may know PSEN1. Exact evidence linkage adds structured value but is not unique to a graph.
- **Likely ambiguity:** Abstract insufficiency versus full-text absence; text-mining association versus assertion.
- **Review burden:** High; qualitative estimate, no review time or expert availability measured. **Status:** CANDIDATE.

### L03 — CANDIDATE

**Question:** Compare AD→APP→lecanemab and LBD→SNCA→prasinezumab: which edges are associations, mechanisms and explicit indications, and does either composed path alone establish treatment efficacy?

- **Scope / type:** AD+LBD; Multi-hop/unsupported claim.
- **Entities:** APP, SNCA, lecanemab CHEMBL3833321, prasinezumab CHEMBL4298077, AD, LBD.
- **Relation families / expected path:** disease–target; target–drug mechanism; drug–indication/report; provenance. Disease→association→target←mechanism←drug; separate drug→indication→report→disease.
- **Sources and required evidence/provenance:** T3-T, T3-E, T3-D; OT and NCT07055087 registry.
- **Provisional answer criteria:** AD/lecanemab has an OT indication with APPROVAL-labelled reports; prasinezumab's returned indications resolve PD/Mental deterioration, not LBD. Neither path alone proves efficacy. Cite the actual source disease and report.
- **Answerability:** Verified source-record paths and selected report; current regulatory/efficacy conclusion not verified.
- **Graph value:** G2 G3 G4 G6 G7. Keep mechanism and indication branches separate instead of transferring labels along connectivity.
- **Non-triviality / LLM and vector alternative:** A complete drug summary may answer; exact join and provenance discrimination require multiple records in this audit, not necessarily a graph engine.
- **Likely ambiguity:** Clinical LBD umbrella, PD, cognitive decline; maximum-stage versus current approval.
- **Review burden:** High; qualitative estimate, no review time or expert availability measured. **Status:** CANDIDATE.

### L04 — CANDIDATE

**Question:** Can the sampled APP–lecanemab and SNCA–cinpanemab mechanism edges both be traced to a publication from their OT mechanism fields, and what should be withheld where that trace is missing?

- **Scope / type:** AD+LBD; Provenance completeness.
- **Entities:** APP, SNCA, lecanemab, cinpanemab CHEMBL3833330.
- **Relation families / expected path:** target–drug mechanism; mechanism–reference. Target←mechanism←drug and mechanism→reference.
- **Sources and required evidence/provenance:** T3-D mechanism query; PMID 25031633 locator.
- **Provisional answer criteria:** Lecanemab supplies PMID 25031633; cinpanemab returns an empty mechanism references array. This prevents that field-level trace, not proof that no supporting publication exists anywhere.
- **Answerability:** Verified metadata; mechanism publication contents unreviewed.
- **Graph value:** G2 G4 G8. Distinguish a missing reference on an existing edge from a missing edge.
- **Non-triviality / LLM and vector alternative:** A two-row table or vector chunk is enough; useful provenance control, weak evidence for graph superiority or for choosing a second disease.
- **Likely ambiguity:** Missing in the endpoint versus unavailable globally.
- **Review burden:** Low; qualitative estimate, no review time or expert availability measured. **Status:** CANDIDATE.

### L05 — CANDIDATE

**Question:** When comparing the sampled AD and LBD phenotype records, which apparent missing phenotype resolves in the alternate identifier field, and which annotations originate from narrower source disease records?

- **Scope / type:** AD+LBD; Identity/provenance.
- **Entities:** AD; LBD; HP_0002354; MONDO_0001627; OMIM:608907; OMIM:127750.
- **Relation families / expected path:** disease–phenotype entry; entry–source annotation; identifier resolution. Disease→entry→HPO/EFO identity and entry→original disease/reference.
- **Sources and required evidence/provenance:** T3-P.
- **Provisional answer criteria:** The LBD null-HPO entry resolves as dementia MONDO_0001627 through phenotypeEFO; AD memory/disinhibition comes from AD9 susceptibility OMIM:608907. Preserve duplicate LBD evidence and missing frequencies; no clinical symptom comparison.
- **Answerability:** Verified stored metadata; source clinical validity/reuse unresolved.
- **Graph value:** G4 G6 G7. Preserve alternate entity resolution and source scope, avoiding an erroneous missing-node conclusion.
- **Non-triviality / LLM and vector alternative:** Structured table/vector retrieval could answer; mainly a data-quality control, not intrinsically a cross-disease scientific question.
- **Likely ambiguity:** HPO term versus disease concept; susceptibility annotation; duplicates.
- **Review burden:** Medium; qualitative estimate, no review time or expert availability measured. **Status:** CANDIDATE.

### L06 — CANDIDATE

**Question:** Does the source label 'Lewy body variant of Alzheimer disease' license merging the AD and LBD anchors or adding Parkinson's disease dementia to this slice?

- **Scope / type:** AD+LBD; Boundary/identifier.
- **Entities:** MONDO:0004975; MONDO:0007488; related synonym; PD dementia boundary.
- **Relation families / expected path:** source concept–synonym qualification; disease hierarchy; provenance. Concept→qualified synonym plus concept→parent; compare identities.
- **Sources and required evidence/provenance:** Task 002A exact-boundary table, reaffirmed T3-H anchor parents; MONDO/OT.
- **Provisional answer criteria:** No automatic merge: OT uses a related synonym, distinct disease IDs remain, and no PD-dementia inclusion was selected. State source-defined boundary rather than asserting a universal clinical equivalence policy.
- **Answerability:** Verified source lexical/hierarchy facts; clinical equivalence adjudication not performed.
- **Graph value:** G5 G6 G7. Carry relationship type of a synonym rather than matching its words.
- **Non-triviality / LLM and vector alternative:** One well-formed ontology-record chunk could answer. This is a semantic control, not evidence that multi-hop graph retrieval is required.
- **Likely ambiguity:** Ontology synonym scope versus clinical umbrella; release differences.
- **Review burden:** Medium; qualitative estimate, no review time or expert availability measured. **Status:** CANDIDATE.

### L07 — DEFER

**Question:** Which sampled symptoms distinguish AD from LBD, and how frequent is each in patients?

- **Scope / type:** AD+LBD; Phenotype discrimination.
- **Entities:** AD/LBD and sampled phenotype IDs.
- **Relation families / expected path:** disease–phenotype; frequency; source scope. Two disease→annotation→phenotype/frequency branches.
- **Sources and required evidence/provenance:** T3-P; additional eligible annotations would be required.
- **Provisional answer criteria:** No fair clinical contrast is supported: small ordered prefixes, null OT frequencies, heterogeneous source disease scopes and reuse uncertainties. Do not infer absence from unreturned entries.
- **Answerability:** INSUFFICIENT EVIDENCE.
- **Graph value:** G3 G8. Would need qualified comparison if data became adequate.
- **Non-triviality / LLM and vector alternative:** Generic symptom summaries are easy for LLM/vector systems; current data cannot support a novel structured claim.
- **Likely ambiguity:** Clinical prevalence versus source annotation frequency.
- **Review burden:** High; qualitative estimate, no review time or expert availability measured. **Status:** DEFER.

### L08 — REJECT

**Question:** Does the higher OT association score identify the disease's most causal or most therapeutically promising gene?

- **Scope / type:** AD+LBD; Invalid premise.
- **Entities:** Ranked AD/LBD targets.
- **Relation families / expected path:** association score only. One lookup.
- **Sources and required evidence/provenance:** T3-T and OT score semantics.
- **Provisional answer criteria:** Reject causal probability/therapeutic ranking interpretation; no such answer criterion can be derived from these scores.
- **Answerability:** Invalid premise established by documented score semantics.
- **Graph value:** G7. No meaningful graph requirement.
- **Non-triviality / LLM and vector alternative:** Generic explanation answers this without graph traversal; retain only as a rejected formulation.
- **Likely ambiguity:** Ranking heuristics versus causality.
- **Review burden:** Low; qualitative estimate, no review time or expert availability measured. **Status:** REJECT.

## AD+FTD design question records

### F01 — CANDIDATE

**Question:** Within U, which shared AD/FTD targets have only clinical-precedence components for FTD, and why should those associations not be treated as independent genetic confirmation of a drug path?

- **Scope / type:** AD+FTD; Comparison/source dependence.
- **Entities:** AD; FTD; GRIN1; GRIN3B; U.
- **Relation families / expected path:** disease–target association; source components; source derivation provenance. Two disease→association→target branches plus association→source.
- **Sources and required evidence/provenance:** T3-X; OT evidence documentation clinical-precedence definition.
- **Provisional answer criteria:** All nine targets are shared in U; GRIN1/GRIN3B are CP-only for FTD. CP is constructed from drug/indication and mechanism information, so it is not independent genetic confirmation. Individual CP records were not sampled; do not name an uninspected drug as their cause.
- **Answerability:** Aggregate-source comparison and documented derivation verified; row-level CP lineage NOT YET VERIFIED.
- **Graph value:** G3 G4 G7. Track source dependence in a joined path rather than count each edge as independent corroboration.
- **Non-triviality / LLM and vector alternative:** Could be answered from prepared source tables and documentation; graph lineage may help but is not uniquely necessary.
- **Likely ambiguity:** Datasource derivation versus full reconstruction of individual evidence.
- **Review burden:** Medium; qualitative estimate, no review time or expert availability measured. **Status:** CANDIDATE.

### F02 — CANDIDATE

**Question:** For shared PSEN1, how do the sampled AD and FTD evidence records differ in source, original disease identity and publication context, and what level of claim is supportable?

- **Scope / type:** AD+FTD; Evidence comparison.
- **Entities:** AD/FTD; PSEN1; OMIM:600274; PMIDs 33008897,31555645,22503161.
- **Relation families / expected path:** association–evidence; evidence–original disease; evidence–publication. Disease→association→evidence→publication/original disease, paired branches.
- **Sources and required evidence/provenance:** T3-E, T3-R.
- **Provisional answer criteria:** AD direct GE/GW sampled strata are empty; FTD GE record names OMIM:600274 and cites 22503161/23028126; EP publications differ. Reviewed 22503161 abstract gives phenotype context, not all-FTD causation. Other AD sources exist and were not excluded from reality.
- **Answerability:** Metadata and selected abstracts verified; gene/variant causal adjudication not verified.
- **Graph value:** G2 G3 G4 G7. Separate a shared target ID from different support and disease granularity.
- **Non-triviality / LLM and vector alternative:** A curated multi-document bundle could answer; exact linkage is a useful structured task, not proof of graph superiority.
- **Likely ambiguity:** Disease family, source phenotype, variant-level evidence versus gene-level aggregate.
- **Review burden:** High; qualitative estimate, no review time or expert availability measured. **Status:** CANDIDATE.

### F03 — CANDIDATE

**Question:** How does descendant inclusion change the sampled APP/AD and MAPT/FTD evidence, and how does that differ from a narrow original disease label already mapped to a broad anchor?

- **Scope / type:** AD+FTD; Propagation versus mapping.
- **Entities:** APP; MAPT; AD; FTD; MONDO_0007088; EFO_1001870; MONDO_0010857; OMIM:172700.
- **Relation families / expected path:** association–evidence; evidence–mapped/original disease; hierarchy context. Anchor→selected evidence→mapped disease/source disease; compare direct/inclusive views.
- **Sources and required evidence/provenance:** T3-E, T3-H.
- **Provisional answer criteria:** AD GE 0→1 and GW 8→10 expose AD1/late-onset records; FTD GE 3→10 exposes semantic-dementia record. Direct FTD/MAPT already says Pick disease while mapped to broad FTD. Report settings and IDs; do not infer the exact uninspected ontology path.
- **Answerability:** Query-selection effects and record mappings verified; full subtype path NOT YET VERIFIED.
- **Graph value:** G2 G3 G4 G5 G6. Distinguish two origins of apparent broad-disease support, which simple label matching collapses.
- **Non-triviality / LLM and vector alternative:** Vector retrieval can answer with explicit query metadata; separate source records otherwise require controlled joins.
- **Likely ambiguity:** Upstream normalization versus ontology propagation; unstable top-evidence tie order.
- **Review burden:** High; qualitative estimate, no review time or expert availability measured. **Status:** CANDIDATE.

### F04 — CANDIDATE

**Question:** For AD→APP→lecanemab and FTD→MAPT→gosuranemab, distinguish mechanism, indication stage, trial status and original clinical population. What would make 'approved effective treatment for the whole disease' unsupported?

- **Scope / type:** AD+FTD; Multi-hop/claim scope.
- **Entities:** AD/FTD; APP/MAPT; lecanemab; gosuranemab CHEMBL3990042; NCT03658135.
- **Relation families / expected path:** disease–target; mechanism; indication–report; report–source population. Association/mechanism branch plus drug→indication→report→source condition.
- **Sources and required evidence/provenance:** T3-D; OT and primary NCT03658135.
- **Provisional answer criteria:** AD/lecanemab has OT APPROVAL-labelled reports, without current product-label review. FTD/gosuranemab is PHASE_1 with terminated trial; registry names narrower tauopathy syndromes. Neither aggregate label proves unrestricted efficacy. Preserve terminated status and source population.
- **Answerability:** Path metadata and FTD registry checked; efficacy/current AD approval adjudication not performed.
- **Graph value:** G2 G3 G4 G6 G7. Maintain edge semantics and disease granularity across a composed answer.
- **Non-triviality / LLM and vector alternative:** A full evidence bundle supports vector QA too; benefit would be consistency of relation-bound assertions, not unique facts.
- **Likely ambiguity:** FTLD-tau/MAPT cohorts versus broad FTD; regulatory index versus product label.
- **Review burden:** High; qualitative estimate, no review time or expert availability measured. **Status:** CANDIDATE.

### F05 — CANDIDATE

**Question:** Does the FTD→MAPT→zagotenemab path have an explicit FTD indication in the inspected drug record, or does its clinical evidence point elsewhere?

- **Scope / type:** AD+FTD; Cross-disease path audit.
- **Entities:** FTD; AD; MAPT; zagotenemab CHEMBL4298021.
- **Relation families / expected path:** disease–target; drug–mechanism; drug–indication/report. FTD→association→MAPT←mechanism←drug→indication→disease.
- **Sources and required evidence/provenance:** T3-X, T3-D; NCT03518073 metadata.
- **Provisional answer criteria:** Mechanism targets MAPT; returned indications are AD and tauopathy, with no exact broad FTD ID. AD report stages differ (AACT PHASE_2, TTD PHASE_1); no efficacy conclusion. Absence is bounded to this drug/release.
- **Answerability:** Verified metadata; full clinical report contents not independently reviewed.
- **Graph value:** G2 G3 G4 G7 G8. Explicitly compare disease at path start with disease at indication end.
- **Non-triviality / LLM and vector alternative:** Could be answered by retrieving complete drug and association summaries; path identity checking is the candidate graph value.
- **Likely ambiguity:** Tauopathy parent does not imply all child indications.
- **Review burden:** Medium; qualitative estimate, no review time or expert availability measured. **Status:** CANDIDATE.

### F06 — DEFER

**Question:** Can the sampled AD and behavioral-variant FTD annotations support a fair symptom-frequency comparison for broad AD and broad FTD?

- **Scope / type:** AD+FTD; Phenotype granularity.
- **Entities:** AD; OMIM:608907; FTD; bvFTD MONDO:0017160; ORPHA:275864; HP:0000734.
- **Relation families / expected path:** disease hierarchy; disease–phenotype; annotation provenance/frequency. Broad disease→subtype context→annotation→phenotype, versus mapped AD entry.
- **Sources and required evidence/provenance:** T3-P, Task 002A hierarchy.
- **Provisional answer criteria:** No: OT broad/subtype FTD entries are empty, separate HPO browser annotations lack inspected qualifier/evidence metadata, and AD source granularity/frequency differs. Do not promote bvFTD to broad FTD or treat displayed frequency labels as matched prevalence data.
- **Answerability:** INSUFFICIENT EVIDENCE for the clinical comparison; mismatch itself verified.
- **Graph value:** G3 G4 G5 G8. Qualified comparisons would need explicit scope and annotation provenance.
- **Non-triviality / LLM and vector alternative:** A generic clinical comparison is trivial for text systems; current source asymmetry prevents reliable gold criteria.
- **Likely ambiguity:** Subtype substitution, licensing, unexpected HPO entry, source route.
- **Review burden:** High; qualitative estimate, no review time or expert availability measured. **Status:** DEFER.

### F07 — CANDIDATE

**Question:** Can OMIM:600274 be assigned one unconditional normalized disease solely from these samples, given the direct PSEN1/FTD and inclusive MAPT/FTD records?

- **Scope / type:** AD+FTD; Mapping ambiguity.
- **Entities:** PSEN1; MAPT; OMIM:600274; MONDO_0017276; MONDO_0010857.
- **Relation families / expected path:** association–evidence; evidence–source identifier; evidence–mapped disease. Two evidence records joined by original disease ID, then compare normalized IDs.
- **Sources and required evidence/provenance:** T3-E PSEN1/FTD GE 98c49197…; T3-H MAPT GE 019b39b2….
- **Provisional answer criteria:** Same source ID appears with broad FTD in one record and semantic dementia in another. Preserve per-record mapping/context; no automatic equivalence or repair. Exact original-source mapping rationale is NOT YET VERIFIED.
- **Answerability:** Observed metadata divergence verified; reconciliation unresolved.
- **Graph value:** G2 G4 G6 G7. Retain assertion-level mappings rather than a global string-to-node substitution.
- **Non-triviality / LLM and vector alternative:** A prepared two-row table suffices; graph value is contextual identity handling, not uniquely graph-computable knowledge.
- **Likely ambiguity:** Different panel contexts/snapshots and source mappings; apparent mismatch is not automatically source error.
- **Review burden:** High; qualitative estimate, no review time or expert availability measured. **Status:** CANDIDATE.

### F08 — REJECT

**Question:** Which has memory symptoms and which has behavioral symptoms: AD or FTD?

- **Scope / type:** AD+FTD; Generic clinical contrast.
- **Entities:** AD; FTD.
- **Relation families / expected path:** Unqualified disease–symptom association. No meaningful required path.
- **Sources and required evidence/provenance:** No adequate evidence-bound formulation.
- **Provisional answer criteria:** Reject binary generalization and weak graph rationale. The audit already has disinhibition under an AD susceptibility source record.
- **Answerability:** Not suitable as drafted.
- **Graph value:** G7. No useful graph requirement.
- **Non-triviality / LLM and vector alternative:** Memorized textbook summaries or a single vector result could answer the simplistic version.
- **Likely ambiguity:** Overlapping manifestations and subtype variation.
- **Review burden:** Low; qualitative estimate, no review time or expert availability measured. **Status:** REJECT.

## AD-only design question records

### A01 — CANDIDATE

**Question:** Why does APP have no direct Genomics England record in the sampled AD query but one when descendants are included, and which disease does that evidence actually describe?

- **Scope / type:** AD-only; Propagation/provenance.
- **Entities:** AD; APP; MONDO_0007088; OMIM:104300.
- **Relation families / expected path:** association–evidence; disease hierarchy context; source identity. AD→selected evidence→mapped AD1→original source ID.
- **Sources and required evidence/provenance:** T3-H; evidence 8bac3794…; direct GE count zero.
- **Provisional answer criteria:** State 0→1, mapped AD type 1 and familial AD1 source ID. No claim that all AD has this inherited mechanism.
- **Answerability:** Verified query metadata; exact multi-edge ontology route not reviewed.
- **Graph value:** G2 G4 G5 G7. Separate selection-level inclusion from broad-disease clinical generalization.
- **Non-triviality / LLM and vector alternative:** A complete record plus settings could be retrieved as text; useful semantic control.
- **Likely ambiguity:** Source AD1 versus broad AD; absence restricted to GE/direct query.
- **Review burden:** Medium; qualitative estimate, no review time or expert availability measured. **Status:** CANDIDATE.

### A02 — CANDIDATE

**Question:** Can the sampled PSEN1–AD literature link supply an original disease identifier and a causal claim from the inspected abstract?

- **Scope / type:** AD-only; Evidence sufficiency.
- **Entities:** AD; PSEN1; PMID33008897.
- **Relation families / expected path:** association–evidence; evidence–publication; provenance. AD→association→EP record→publication.
- **Sources and required evidence/provenance:** T3-E additional PSEN1; T3-R.
- **Provisional answer criteria:** Original disease ID is null, normalized AD exists; abstract alone does not establish the specific causal proposition. Distinguish missing metadata from no relationship.
- **Answerability:** Metadata and abstract checked; causality NOT YET VERIFIED.
- **Graph value:** G2 G4 G7 G8. Bind claim limits to the actual record and inspected text.
- **Non-triviality / LLM and vector alternative:** Abstract/text retrieval could answer; evidence linkage mainly supports auditability.
- **Likely ambiguity:** Null source ID is not an invalid normalized ID.
- **Review burden:** Medium; qualitative estimate, no review time or expert availability measured. **Status:** CANDIDATE.

### A03 — CANDIDATE

**Question:** For the two APP drugs selected by the protocol, what mechanism actions and indication stages are recorded, and which source records support those distinct statements?

- **Scope / type:** AD-only; Multi-hop/provenance.
- **Entities:** APP; lecanemab; tramiprosate; AD.
- **Relation families / expected path:** association; mechanism; indication; report/reference. AD→association→APP←mechanism←drug→indication→report.
- **Sources and required evidence/provenance:** T3-D; mechanism PMIDs and PMDA/TTD/AACT report IDs.
- **Provisional answer criteria:** INHIBITOR versus STABILISER; APPROVAL versus PHASE_3 labels in OT; identify mechanism references separately from clinical reports. No current efficacy ranking.
- **Answerability:** Metadata verified; mechanism publications and regulatory product label not inspected.
- **Graph value:** G2 G4 G7. Compare statement types and their different provenance routes.
- **Non-triviality / LLM and vector alternative:** A combined drug table makes retrieval simple; not proof a graph improves answers.
- **Likely ambiguity:** Current approval versus historical maximum; gene-product granularity.
- **Review burden:** Medium; qualitative estimate, no review time or expert availability measured. **Status:** CANDIDATE.

### A04 — CANDIDATE

**Question:** Should the sampled memory-impairment and disinhibition annotations be presented as unqualified all-AD facts, and what provenance would be lost?

- **Scope / type:** AD-only; Subtype/annotation scope.
- **Entities:** AD; OMIM:608907; HP_0002354; HP_0000734.
- **Relation families / expected path:** disease–phenotype entry; original disease; reference/qualifier. AD→annotation→phenotype and annotation→AD9 susceptibility source.
- **Sources and required evidence/provenance:** T3-P.
- **Provisional answer criteria:** Retain AD9 susceptibility source, TAS, reference, null frequency and curation date. Do not claim universality or infer prevalence.
- **Answerability:** Stored annotation metadata verified; upstream clinical assertion/reuse unresolved.
- **Graph value:** G4 G6 G7. Keep original scope alongside the broad normalized record.
- **Non-triviality / LLM and vector alternative:** One complete annotation chunk is sufficient; lower-hop semantic control.
- **Likely ambiguity:** Susceptibility record versus disease-family claim.
- **Review burden:** Medium; qualitative estimate, no review time or expert availability measured. **Status:** CANDIDATE.

### A05 — REJECT

**Question:** Which of the three highest-ranked AD targets is the best therapeutic target?

- **Scope / type:** AD-only; Unsupported therapeutic ranking.
- **Entities:** APP; GRIN1; GRIN3B.
- **Relation families / expected path:** Association scores alone. One rank lookup.
- **Sources and required evidence/provenance:** T3-T only; insufficient therapeutic evidence.
- **Provisional answer criteria:** Reject: aggregate ranking is not a validated therapeutic comparison.
- **Answerability:** INSUFFICIENT EVIDENCE; invalid inference from available inputs.
- **Graph value:** G7. No demonstrated graph need.
- **Non-triviality / LLM and vector alternative:** An LLM can recite a familiar target but cannot justify this ranking from the sample.
- **Likely ambiguity:** Association score versus intervention benefit.
- **Review burden:** High; qualitative estimate, no review time or expert availability measured. **Status:** REJECT.

## Quality review and count discipline

| Scope | Drafted | CANDIDATE | DEFER | REJECT | Independent validated questions |
| --- | ---: | ---: | ---: | ---: | --- |
| AD+LBD | 8 | 6 | 1 | 1 | None claimed |
| AD+FTD | 8 | 6 | 1 | 1 | None claimed |
| AD-only | 5 | 4 | 0 | 1 | None claimed |

The six candidates per pairing are provisionally usable source-record questions, not six independently validated scientific questions. There is template redundancy: L01/F01 are source-aware comparisons; L02/F02/A02 share evidence-support logic; L03/F04/F05/A03 are drug-path checks; L05/A04 are annotation-scope controls; F03/A01 share propagation logic. L04–L06 are useful semantic/provenance controls but comparatively weak evidence for choosing a second anchor or a graph engine. Do not add these as independent samples in a later statistical analysis without addressing shared evidence/templates.

The strongest potential relation-composition cases are L03 and F02–F05/F07, but strength here means explicit, auditable dependence on several records, not demonstrated model difficulty. None has been tested against an LLM or vector system. F03's diagnostic metadata supports a comparison, not verified OWL entailment along a complete hierarchy path. No efficacy/causality question is retained with unsupported positive gold labels. Negative answers are bounded to what the inspected records establish, not universal biomedical negatives.

## Requirements revealed, without ontology design

Retain the disease at each assertion and indication; distinguish original from normalized identifiers; preserve query settings and source version; distinguish a source assertion, an aggregate, a publication, a trial and an audit-derived comparison; retain missing reference fields and duplicated annotations visibly; distinguish insufficient evidence from a disproved claim. A complete vector-accessible evidence bundle must preserve the same information in a future matched comparison.

Owner review is needed for clinical claim boundaries, rubric clarity, duplicate/template grouping, acceptable provenance depth and manual adjudication. Questions about phenotype discrimination remain deferred. Neither the scope nor the primary experiment is frozen.
