# M1 Task 002 — conceptual model contract

Status: **APPROVED CONCEPTUAL CONTRACT; IMPLEMENTATION CHOICES OPEN**. Baseline: `2eef391 Compare M1 ontology modelling alternatives`. The owner has approved this conceptual contract for Alternative B, including its Q01–Q07 and R1–R14 traceability. M0 remains frozen. This document defines meaning, not ontology names, namespaces, properties, identifiers, axioms, shapes or executable rules.

## 1. Architecture and authority

Follow [approved Alternative B](m1_modelling_options.md): identifiable disease–target associations, distinct evidence occurrences, contextual normalization and selection, and separate mechanism/indication/study records. Preserve [Q01–Q07 and R1–R14](competency_questions.md) and the [bounded V1 scope](project_scope.md). AD MONDO:0004975 and FTD MONDO:0017276 remain the only approved disease anchors. All biomedical examples below refer to the frozen investigation, not new source verification.

The organizing unit is a **scoped association record**, not an unconditional assertion of biological causality. Its constituents describe reported evidence and its interpretation. Source claims, platform transformations, project computations and technical judgments must remain distinguishable. An assertion's presence records its attribution, not the project's endorsement of its truth.

Separate three levels throughout: a referent (for example a study), a versioned description of that referent, and an encounter with that description (retrieval or inspection). Repeated encounters do not manufacture new underlying evidence. Unknown identity cannot be repaired by guessing. No arbitrary UUID or physical identifier strategy is selected.

## 2. Conceptual roles and necessity

These labels are explanatory handles, not proposed OWL classes. “Required” means representational capability when the relevant case exists, not a demand to populate every role for every record.

| Candidate concept | Decision | Meaning and reason |
| --- | --- | --- |
| DiseaseConcept | Required referent role | A disease meaning referenced in a declared authority; separate from a platform record, label, patient, anchor role or mapping observation. |
| Target | Required referent role | The source-indexed target, including identifier authority and organism context where supplied. Gene indexing does not identify every protein form or molecular species. |
| Drug | Required referent role | The source-identified intervention; do not silently equate product, formulation, active substance and platform drug identifier. |
| DiseaseTargetAssociation | Required distinct record | A source aggregate or an explicitly project-derived grouping for a particular scope/view; see section 5. |
| EvidenceRecord / EvidenceOccurrence | Required single occurrence role, not two obligatory nodes | A particular source record version reporting evidence. “Record” and “occurrence” denote this role here; storage copies and query hits are not additional evidence. |
| SourceAssertion | Required distinguishable content/attribution role; separate node optional | What a source says, at its original scope. A single-claim occurrence may carry this role; split it conceptually when multiple claims have different scope/support. No universal proposition registry needed. |
| Mapping / NormalizationRecord | Required first-class record | A contextual assignment or unresolved assignment assessment, not disease identity. Needed to compare competing assignments. |
| SelectionContext | Required first-class context plus membership relation | Records the retrieval/view and why a particular occurrence belongs to it. Run context alone cannot describe different paths for different hits. |
| ProvenanceRecord | Required information; universal wrapper node unnecessary | Attach source/version/locator/activity attribution to the appropriate record. Shared source descriptions and transformations may be identifiable; avoid one provenance node that hides which claim it qualifies. |
| Publication / Study / SourceLocator | Publication and study referents required where present; locator normally a value/relation | A publication reports research; a study is the investigation; a locator points to a resource or passage. These are not interchangeable. Qualify a locator separately if version, passage or access history requires it. |
| MechanismRecord | Required qualified record | A source report of drug–target mechanism, with any supported molecular detail and source context. |
| ClinicalIndicationRecord | Required qualified record | A source-defined drug–disease indication/development entry; not automatically an authorization or efficacy claim. |
| Trial / StudyContext | Required where questions demand it | Identifiable study plus dated contextual descriptions. One registry record is not the entire study or every report of it. |
| PopulationScope | Required contextual description | Original eligibility/cohort wording and supported restrictions, attached to the relevant study arm/report/claim. It need not become a reusable disease class or global population entity. |
| DerivedStatement / DerivedComparison | Required distinguishable result | A project computation's scoped output and derivation; not another source assertion. |
| Inspection / ReviewRecord | Required contextual record | An inspection event and bounded technical conclusion tied to a source version and claim. One inspection may inform several separately scoped conclusions. |
| Dependency / SharedEvidence | Required qualified relation; standalone record when necessary | Link records to the shared publication/trial/assertion/input. A separate dependency assessment is useful when basis, direction, uncertainty or review needs its own provenance. |

Additional required contextual information: source artifact/version description, bounded hierarchy steps, claim-local missingness and support/qualification outcomes. These need not each become a separate class. Association scores, phase, status, inspection depth and missingness categories are contextual values, not mandatory standalone entities. Regulatory context is needed only if a claim uses an approval-labelled field; comprehensive regulatory modelling is deferred.

## 3. Semantic identity and version contract

Identity decisions below concern co-reference, not database keys or OWL equality axioms. They do not authorize automatic `sameAs`, key-based merges or clinical equivalence. Preserve conflicting records rather than choosing one silently.

| Role | Same identity when | Different or unresolved when |
| --- | --- | --- |
| Disease/target/drug referent | Same authoritative referent with justified identifier resolution; labels alone do not establish it | Different authorities/IDs require verified alignment; obsolete, split or merged concepts require contextual reconciliation |
| Versioned entity description | Same referent, source artifact/version and description scope | Source release or described meaning changes; keep descriptions distinct even if referent persists |
| Association record | Same origin, disease scope, target, source snapshot, aggregation definition and selection/view specification | Any dimension changes; source aggregates and project groupings are always distinguishable; unknown dimensions prevent a justified merge |
| Evidence occurrence | Same originating provider/dataset, source record identity and record version/snapshot | Same text, PMID, target pair or payload resemblance alone is insufficient; changed source versions stay separate |
| Source assertion occurrence | Same attributed claim at the same source location/version and scope | Same proposition in another source remains another occurrence; multiple platform representations do not prove distinct original assertions |
| Mapping observation | Same source occurrence/context, input identity/label, reported destination(s), assigning authority/process and version | Different panel/gene/record context or destinations remain distinct; unknown process/version is recorded, not presumed equal |
| Selection specification and run | Same specification can be reused; each retrieval execution is a separate encounter | Different anchor, filters, inclusion mode, snapshot or traversal policy means a different specification; time alone creates a new run, not new evidence |
| Selection membership | Same occurrence in the same run/result view | Alternative paths are membership explanations, not additional evidence; different runs retain encounters without multiplying occurrence count |
| Publication / study | Same authoritative publication or study identifier | A shared author/title or a paper reporting a trial is not identity; multiple reports may describe one study |
| Mechanism / indication | Same source record/version and scoped content/participants | Drug–target or drug–disease pair alone is insufficient; different sources, populations or versions remain separate records |
| Population description | Same description in the same study/report/arm/version context | Similar wording in different studies does not establish the same population; no automatic cross-study merge |
| Derived result / review | Same documented operation/assessment occurrence with its input versions and settings | Repeated computations/reviews are separate activities even if their conclusions agree; content equality does not imply activity identity |

**Association dimensions:** source/origin, disease anchor or explicitly stated diagnostic scope, target, platform release/snapshot, aggregation method/version and direct versus inclusive selection all matter to the scoped association. A disease–target pair may group related records for navigation but is not a sufficient association identity. A changed local sampling filter changes a project grouping; it does not rewrite the identity of a source aggregate it samples. Repeated retrieval of an unchanged source aggregate adds encounter provenance, not a new aggregate.

A release identifier may be unavailable. Retain the known retrieval/artifact context and state version unknown; retrieval time is not an invented release number. Do not merge unversioned records across retrievals unless available identity evidence supports it. If a stable source record identity is absent, preserve separately traceable artifact locations and mark duplicate status unresolved; no invented canonical upstream identity.

One publication reused by five source records means one identified publication and five source occurrences, if their source record identities are distinct. Repeated retrieval of one identified occurrence means one occurrence plus multiple selection encounters. Neither arithmetic establishes independent evidence units.

## 4. Disease identity contract

| Role | Contract |
| --- | --- |
| Source disease identity | Original identifier and label as the particular evidence/source record supplies them; absence remains explicit. |
| Normalized/platform disease identity | Destination reported by the platform for that record; a versioned assignment, not a replacement for the original. |
| Approved project anchor | AD MONDO:0004975 or FTD MONDO:0017276, assigned the project comparison role. |
| Descendant disease | A concept related to an anchor by the explicitly retained source hierarchy/path; relation is versioned and bounded. It is not an extra anchor. |
| Query anchor | Disease requested for a particular retrieval/traversal; often a project anchor but a separate contextual role. |
| Mapped disease | Destination of a particular normalization assignment; it can differ from the query anchor. |
| External ontology reference | Reference to an authority's concept identifier, with its inspected version/context; it does not import its ontology. |

**Pick example (Q03):** the original Pick label/OMIM:172700 in the MAPT evidence maps to platform FTD MONDO:0017276. The row is direct for that normalized FTD query anchor. Separately sourced Pick MONDO:0008243 and its hierarchy context do not explain away the upstream normalization. Do not assert global OMIM:172700 = MONDO:0008243 = FTD equivalence from this record, or infer which unverified algorithm made the assignment. Historical label and publication-to-phenotype qualifications survive.

Normalization does **not** imply `owl:equivalentClass`; source and normalized disease do not collapse automatically. Descendant selection does not make evidence direct evidence for a parent. Referencing MONDO does not import all MONDO axioms. An application association/record is not an instance of the disease it references. Exact class-versus-concept-reference encoding and import mechanics remain unresolved implementation decisions.

## 5. Association contract

A disease–target association record describes a **scoped aggregation/grouping of reported evidence relating a disease reference and target**. It does not itself assert causality, therapeutic action or a clinically uniform syndrome.

Two origins must be distinguished:

1. **Source aggregate:** the platform's reported aggregate for its documented context. At the attribution level this is a source assertion about an aggregate, not an individual experimental observation.
2. **Project grouping:** a grouping created from specified selected occurrences under a declared operation. This is a derived project result. It cannot impersonate a platform aggregate or inherit its score.

Both use association-centric roles but have distinguishable origin and derivation. A source aggregate can have many constituent evidence occurrences. An occurrence may be relevant to multiple scoped associations, with each membership explained; this is not independent replication. Distinguish platform-reported contribution, project-selected membership and technically assessed support. A generic “supports” link must not erase those meanings.

A source aggregate may exist with **zero currently accessible linked occurrences** when the source reports it but constituent retrieval is absent, partial or inaccessible. Record that status. Zero accessible records is neither zero source evidence nor a supported answer bundle. A project computation over an empty selection is an empty derived result, not a fabricated positive association. Available samples must not be declared the aggregate's complete constituents without source evidence of completeness.

A score belongs to the source aggregate's scoring context, including source, method, release, view and any datasource component to which it applies. It is only the source-defined aggregate measure unless further interpretation is documented. It is not automatically probability, causality, confidence in a biomedical claim, evidence volume or an independence-weighted quantity. Filtering evidence does not authorize recalculating or transplanting the score. No project score is proposed.

Core comparison remains direct normalized-anchor records. Inclusive diagnostics are separately labelled views/results for Q04, never silently pooled into core anchor associations.

## 6. Evidence and source assertion contract

An evidence occurrence records what a provider exposes at a particular record version, including its datasource/type and available original/mapped context. A provider may itself derive the record (for example clinical precedence). Therefore “source assertion” does not mean primary experiment or raw observation. Preserve known upstream derivation and unknown steps.

Distinguish an occurrence from: the publication or study it references; the citation/locator relation; the attributed statement content; the association aggregate; and a project-derived comparison. A single occurrence may cite several publications or contain several claims. Keep claim-to-locator attribution at the finest level actually supported by the source. A panel-wide reference list must remain panel-wide; do not invent claim-specific publication links.

A separate universal SourceAssertion node is not required for each occurrence. Its semantic content, scope and attribution must nevertheless be independently addressable when one record contains different claims or one source assertion appears in several normalized records. This keeps Alternative B rather than adopting C's universal proposition machinery.

Citation presence does not establish evidential support. Technical review must say what was inspected and what the text permits, separately from the source's linkage. Missing original disease, locator, study linkage or extraction span remains missing. Publication count, occurrence count and independent study count must never be substituted for each other.

## 7. Mapping/normalization contract

**First-class conceptually:** a mapping observation records a contextual source-to-platform assignment or unresolved assessment. It preserves input identifier and label independently (either can be missing), occurrence/panel/gene context, destination where reported, assigning source/process, source/version information where known, ambiguity and the basis for any review.

Distinguish **observed destination** from **candidate destination**. An unresolved mapping can have no established destination, several candidates, or an observed platform destination whose correctness remains unresolved. A reported assignment is not transformed into a mere hypothetical candidate because the project cannot adjudicate it. Multiple observations sharing an input ID can coexist.

For Q05, the PSEN1/panel 265 and MAPT/panel 540 OMIM:600274 assignments retain their different destinations and contexts. No global mapping repair, identity merge or source-error conclusion follows. The observed output does not verify the upstream algorithm or exact snapshot. Unverified process/version stays explicitly unknown.

## 8. Selection and propagation contract

**First-class conceptually:** selection context identifies requested anchor, target/filter restrictions, datasource criteria, direct/inclusive mode, source snapshot or its missingness, retrieval time/run, result extent/completeness and declared operation. Membership binds a specific occurrence to this context with its mapped disease and inclusion explanation. Source hierarchy steps and their versions are retained where a path is required.

| Operation | Meaning and boundary |
| --- | --- |
| Upstream normalization | Source/platform assigns the original disease to a normalized disease before the observed retrieval. |
| Direct query selection | The source's direct-mode retrieval selects the record for the normalized query anchor under its documented semantics; not direct causal or primary-study evidence. |
| Descendant-inclusive selection | The retrieval includes a record normalized to a narrower disease within the specified hierarchy context. It remains narrower-mapped evidence. |
| Project-side traversal | A project computation follows explicit stored relationships under a declared bound; it is not proof that the source executed that traversal. |
| Inferred hierarchy relationship | A logical conclusion from identified axioms and a declared entailment regime; distinct from a retrieved parent step and from query membership. No such execution occurs here. |

In Q04, retain the source direct/inclusive observations and separately inspected paths. Do not claim those paths reveal the source's exact undocumented internal execution. Where a full justification path is unavailable, membership can be recorded as observed but its explanation remains incomplete. Directness is relative to anchor/view, not a permanent global flag on an evidence occurrence.

Same occurrence through two paths is one occurrence with two path explanations. Same occurrence through two runs is one occurrence with two encounters if identity is established. Missing pagination/results cannot justify “only inclusive” or absence conclusions; compare adequately inspected, explicitly bounded result sets. No automatic descendant closure or further subtree collection is authorized.

## 9. Drug, mechanism, indication and study contract

| Role | Meaning |
| --- | --- |
| Mechanism | Source-attributed relation between drug and molecular target/action; retain gene-indexing limits, molecular detail and source reference where available. |
| Indication | Source-defined drug–disease entry with its own provenance and development/regulatory qualifiers; a platform term whose meaning must not be upgraded. |
| Trial/study | Identifiable investigation; retain report/registry descriptions at their dates and distinguish it from associated papers. |
| Population | Source-local participants, cohorts, eligibility and arm context; narrower than an indication label where the source says so. No invented disease mappings. |
| Phase | A reported development/study-stage value in the context to which the source attaches it. An indication-level maximum phase is not every trial's phase. |
| Status | Dated registry/source state such as termination; not efficacy, phase or current universal status. |
| Regulatory approval | If used, a qualified source assertion requiring jurisdiction, authority, product, indication, population and effective/as-of context where available. Missing qualifications block an unrestricted current approval claim. |

Mechanism does not imply indication; indication does not imply efficacy; trial presence does not imply successful treatment; an approval-labelled source record does not imply unrestricted current approval; a disease–target–drug path does not justify treatment recommendation. Phase does not imply completion, termination does not by itself imply efficacy failure, and healthy-participant findings do not become patient benefit.

For Q06, preserve zagotenemab's mechanism and inspected indication list separately, and the lecanemab/APP control's molecular-detail qualification. For Q07, gosuranemab's FTD indication, registry population/status and separate healthy-participant mechanism study keep their own source and inspection chains. There is no new regulatory investigation or comprehensive drug model in this task.

## 10. Derived statement contract

A project-derived statement is an attributed output of a declared operation on identified inputs. Examples: an intersection of sampled targets, two records sharing a trial locator, or a membership difference between recorded direct and inclusive results. These are claims about the inspected bundle, not unrestricted biology.

Every result must carry: operation/meaning and version if defined; input record versions; source/selection boundaries; filters and comparison settings; output scope; derivation activity/date; responsible process/reviewer attribution where known; completeness and missingness limits. Unknown items remain explicit and may prevent a reproducibility claim. A derived result must not overwrite its inputs.

Separate: **source assertion** (attributed source content); **normalized representation** (recorded assignment retaining original content); **derived comparison** (project computation); **logical inference** (entailment from stated premises/rules); and **review conclusion** (bounded technical assessment). A project calculation is not automatically an OWL inference. A comparison that two records reference the same paper establishes shared publication provenance; it does not alone establish complete statistical dependence. No derived independence score is introduced.

## 11. Inspection/review contract

Inspection is a contextual event tied to specific source material/version, access route/date, inspector/process and question/claim. Review is its bounded interpretation, with outcome, rationale and scope. Several claims can have different review outcomes from one inspection; a later inspection does not erase earlier access limits.

**Depth is a controlled conceptual value on an inspection**, not an independent entity or a timeless attribute of a PMID. Metadata-only, abstract, full-text, selected-passage and source-page inspection must be distinguished. “Full text accessible” is not “full text read”; selected passages do not become full-document review. Registry/source-page inspection is a material type and need not fit a single linear depth ranking with journal text.

Access outcome and interpretation outcome are separate dimensions: source inaccessible is an access result; unresolved interpretation can follow successful access at any depth. An inspection attempt may therefore have no content depth. Preserve inspected sections where relevant. Technical conclusions include source-record support, not established by this bundle, mapping ambiguity and access limitation; precise coding vocabulary remains open.

None of these labels constitutes biomedical domain-expert adjudication. No independent human review or clinical truth label is claimed. Review provenance must identify actual reviewer type without inventing a human expert.

## 12. Missingness contract

Represent missingness at the relevant record, information slot and observation/inspection context, not as a universal unknown entity or one undifferentiated null.

| Conceptual category | Meaning / guard |
| --- | --- |
| Not provided by source | The inspected source representation omits the information; do not claim omission from every upstream source. |
| Not retrieved | The project has not acquired the needed information; not proof the source lacks it. |
| Source inaccessible | A recorded access attempt failed or was restricted; retain route/date and reason if known. |
| Not applicable | A justified scope judgment, not a default used to satisfy a required field. |
| Not yet inspected | Material may be available, but its relevant content has not been reviewed. |
| Unresolved | Available information does not determine identity, mapping or interpretation. |
| Reason unknown | Absence is observed but its cause is unknown; do not assign one of the above by guesswork. |

These are conceptual distinctions, not final enumeration codes. Several reasons can coexist for different sources/slots or times. Known values and unresolved judgments may coexist: a known platform destination can have unresolved mapping validity. Later resolution adds a new observation/review rather than retroactively fabricating earlier completeness. Validation may require either a value or a contextual reason; it cannot certify that the reason is factually correct without source checking.

## 13. Dependency contract

| Situation | Required treatment |
| --- | --- |
| One publication reused | Link each occurrence to the same identified publication; preserve distinct assertions/locators and attribution scope. |
| One trial across indications | Share study identity, retain separate indication memberships/populations/report versions; do not merge all indication records. |
| One assertion in multiple normalized records | Retain each platform occurrence/mapping and the common source assertion when established; if suspected, record uncertainty rather than asserting identity. |
| One occurrence through multiple paths | Share occurrence identity; retain query memberships and path explanations separately. |

A **duplicate record** repeats the same identified occurrence/version; a **shared source** means a common publication/study/input; **dependent evidence** has an established shared derivation or relevant reliance for the particular claim; **independent evidence** requires a justified assessment of underlying studies/data and claim context. Different IDs, different publications, or no known shared link do not establish independence. Shared publication is a dependence warning, not automatic proof that every study it reports is the same experiment.

For Q02, the recorded shared drug/report and documented mechanism–indication derivation justify the concrete clinical-precedence dependency conclusion. It is not inferred from PMID equality alone. Dependency assessments preserve the basis, inspected depth, relation kind and uncertainty; “depends on” is directional, while “shares this trial” is a common-input comparison. Avoid declaring every dependency symmetric or transitively independent/non-independent. No numerical independence score or universal evidence-unit count is proposed.

## 14. What the future ontology may safely infer

The owner approved only the narrow intended entailment boundaries below. No executable inference rule or OWL profile is selected by this conceptual approval:

- Classification among later approved **application record roles**, where subtype meaning is explicit; for example, a qualified mechanism record remains a record. Exact classes are not selected here.
- Inverse navigation for a relation only if its defined meaning warrants it; this adds an equivalent access direction, not biomedical content.
- Logical consequences of explicitly approved, versioned hierarchy axioms only within a separately specified entailment boundary. Current Q04 needs explicit path interpretation, not automatic closure; no disease-hierarchy entailment is presently required or authorized.

Shared-input detection, source-specific directness classification, target intersections, completeness checks and support judgments are query/transformation/application operations. They must not be disguised as OWL consequences. No core question currently requires advanced OWL reasoning. Intended record typing cannot substitute for data validation or claim verification.

## 15. What must never follow automatically

The future model/application must not upgrade:

- Normalized disease into equivalence with original disease.
- Descendant-selected evidence into direct parent evidence, or an extra project anchor.
- Mechanism into indication, or a disease–target–drug path into treatment recommendation.
- Indication into efficacy, trial presence into successful treatment, or phase into completion.
- Approval-labelled source metadata into unrestricted current regulatory approval.
- Citation into assessed support, or panel-wide citations into adjudicated claim-specific evidence.
- Repeated records into independent corroboration, or no known dependency into independence.
- Missing evidence into evidence of absence, or inaccessible text into a disproven claim.
- Source aggregate score into causality, probability, evidence volume or therapeutic ranking.
- Technical review into biomedical expert adjudication, or passed validation into biomedical truth.
- Identifier resemblance into equality, or incomplete provenance into invented source history.

These are prohibitions on automatic upgrades, not assertions that the biomedical propositions are necessarily false. A future independently justified claim would require its own evidence, scope and authorization; it cannot arise merely from these graph patterns.

## 16. Open-world and bounded validation consequences

An absent indication in a graph is unknown globally. Even a complete inspection of a named drug list permits only “no matching indication in this declared source snapshot/view,” not an unrestricted negative disease indication relation. No such negative property is proposed. A partial page or failed retrieval cannot establish even list-wide absence.

Later data validation can check required participants, role compatibility, version-or-missingness information, locator syntax, selection context and derivation inputs under a declared validation graph. Application logic must check result completeness, deduplicate established identities, assess support, detect unsupported broadening and qualify/abstain. Ingestion preserves original values and flags unresolvable identity rather than silently repairing them.

OWL's open-world semantics does not supply a closed-world completeness test. Later equality/key choices must not force uncertain records to merge; different record identifiers also do not by themselves establish biological independence. Validation and answer rules require explicit dataset/snapshot boundaries. No shapes or closed-world rule implementation is created here.

## 17. Responsibility matrix

S = ontology semantics; P = provenance model; V = SHACL/data validation; T = ingestion/transformation logic; A = application verification; E = experimental evaluation. Entries specify responsibility, not selected technology or implemented checks. Evaluation criteria below are future concerns, not frozen metrics or completed experiments.

| Concept/rule | S | P | V | T | A | E |
| --- | --- | --- | --- | --- | --- | --- |
| Disease/target/drug identity | Distinct referent and record roles | Authority/version | Identifier/context presence | Resolve only justified matches | Preserve disputed identity | Identity/scope fidelity |
| Association and score | Aggregate vs grouping vs observation | Origin/method/view | Participants and context | Preserve source aggregate; label project grouping | No score/causal upgrade | Correct interpretation |
| Evidence/assertion/publication/study/locator | Distinct meanings and attribution scope | Record/source chain | Roles and locator-or-reason | Preserve occurrence identity and panel attribution | Citation vs inspected support | Trace fidelity |
| Mapping | Assignment not equivalence | Source/process/context | Input/destination-or-status | Preserve observed/candidate distinctions | No invented repair | Ambiguity handling |
| Selection/hierarchy | Membership relative to context | Run, path, versions | Anchor/mode/path-or-limit | Preserve settings and hits | Distinguish source selection from traversal | Propagation accuracy |
| Mechanism/indication | Distinct relation meanings | Separate source records | Required roles | Preserve molecular scope | Reject invalid composition | Clinical overstatement |
| Study/population/phase/status/approval | Context-bound meanings | Report date/authority | Context-or-reason | Preserve source wording and attachment | No efficacy/current approval upgrade | Population/status fidelity |
| Derived results | Result not source assertion | Inputs/operation | Inputs/settings/scope | Compute reproducibly | Bound conclusion to inputs | Derivation fidelity |
| Inspection/review | Event, material, outcome distinct | Inspector/date/version | Depth/access/outcome fields | Preserve actual inspection record | Assess support/qualification | Review-depth fidelity |
| Missingness | Unknown not false | Observation and reason basis | Value-or-reason, applicability | Do not fabricate values | Qualify/abstain | Missingness handling |
| Dependency/deduplication | Occurrence vs shared input | Common trial/assertion lineage | Dependency basis where claimed | Deduplicate established repeats | No automatic independence | Reuse sensitivity |
| Inference and open-world boundary | Limited declared entailments | Premises/regime | Validation graph declared | Keep inferred/source origin | Bounded absence, no global negative | Unsupported-inference detection |

## 18. Q01–Q07 minimum conceptual walkthroughs

The frozen required slots and A–E rubric remain authoritative; these walkthroughs do not replace or relax them. Each path includes source/version or explicit missingness and claim-local review outcomes. Arrows are information dependencies, not proposed ontology properties.

| Question | Minimum conceptual path and why |
| --- | --- |
| Q01 | AD/FTD PSEN1 associations → selected evidence occurrences → datasource/source assertions → publications/panel → inspections → qualified comparison. Association separates aggregation from individual records; evidence preserves EP/GE differences and original-field nulls; locators bind each PMID; review depth bounds text/causal interpretation. Selection context fixes the sampled direct view and prevents empty sample cells becoming universal absence. |
| Q02 | FTD GRIN1/GRIN3B associations → two clinical-precedence occurrences → shared memantine mechanism and indication/report lineage → trial nct00594737 → technical dependency result. Distinct occurrences remain visible while the shared input defeats the proposed independent genetic-confirmation reading. Source composition, query boundary, missing originals and actual registry inspection remain attached; unread publication bodies stay unread. |
| Q03 | FTD/MAPT association → evidence occurrence → original Pick/OMIM:172700 → normalization observation → mapped FTD; separately selection context → direct FTD query anchor, and ontology context → Pick MONDO:0008243. This separates upstream normalization from hierarchy context. Panel 474 and abstract inspections preserve citation and historical-label limits. No global Pick=FTD assertion follows. |
| Q04 | Recorded direct/inclusive selection contexts → occurrence memberships → mapped AD1/semantic dementia → complete audited hierarchy steps → AD/FTD anchors; compare Q03 normalization. Retain APP/MAPT identities, source filter, query flags, dated counts and source versions. A derived comparison explains membership differences; no executed OWL inference or pooled core evidence is implied. |
| Q05 | Two occurrences → original OMIM:600274 → separate contextual mapping observations → FTD versus semantic dementia; attach PSEN1/panel 265 and MAPT/panel 540, xref annotation and review limits. Shared input identifier permits comparison, not merge. Missing algorithm/snapshot and inaccessible authoritative interpretation require unresolved outcome, not canonical repair. |
| Q06 | FTD/MAPT association → target ← zagotenemab mechanism ← drug → separate inspected indication records → disease references; mechanism locator → inspection. Retrieve bounded list context before reporting no exact FTD match. Keep lecanemab/APP AD control and molecular-species qualifications separate. Clinical reports attach only to their actual indication; path existence cannot create treatment support. |
| Q07 | Gosuranemab → FTD indication occurrence → trial nct03658135 → dated population/design/status description → inspection/review; separately drug → MAPT mechanism → study/publication → inspection. Population restrictions qualify broad indication wording; phase/status are separate, and healthy-participant mechanism observations cannot establish patient efficacy. Original cohort wording remains unmapped unless verified. |

Every path has a conceptual home. Actual future acquisition completeness remains unverified; a representable path does not imply all inputs are available or sufficient to answer.

## 19. R1–R14 traceability

Requirement text is copied verbatim from the frozen document. All fourteen requirements have approved conceptual representations. Exact encoding and operational validation remain open.

| ID | Frozen requirement | Conceptual representation |
| --- | --- | --- |
| R1 | Association separately from individual evidence. | Association aggregate/grouping distinct from evidence occurrence (sections 5–6). |
| R2 | Original/source disease identity separately from normalized disease identity. | Original identifier/label plus separate normalized assignment (4, 7). |
| R3 | Mapping context and unresolved ambiguity. | Contextual mapping observation with observed/candidate destinations and unresolved outcome (7). |
| R4 | Direct evidence separately from descendant-derived/propagated evidence. | Selection membership relative to query anchor, mapped disease, mode and path (8). |
| R5 | Query-time descendant inclusion separately from upstream source normalization. | Normalization observation separate from selection specification/run and traversal (7–8). |
| R6 | Evidence provenance at claim/association level. | Claim-local attribution and association origin/version; no universal provenance wrapper required (2, 5–6). |
| R7 | Publication/study/source locator where available. | Distinct publication/study referents and qualified locator information (2, 6). |
| R8 | Inspection/review depth where relevant. | Inspection event with material, depth, access and interpretation dimensions (11). |
| R9 | Missing provenance/information explicitly rather than silently repaired. | Slot-local contextual missingness and known reason or reason unknown (12). |
| R10 | Target–drug mechanism separately from disease indication. | Separate mechanism and indication records and prohibited composition (9, 15). |
| R11 | Clinical indication separately from trial population and trial status. | Indication, study/report, population and dated phase/status roles (9). |
| R12 | Derived comparisons/intersections separately from source assertions. | Derived result with inputs/operation, distinct from attributed source content (10). |
| R13 | Shared/dependent evidence so multiple records are not automatically independent support. | Shared study/publication/assertion inputs and qualified dependency assessment (13). |
| R14 | Scope qualification and abstention conditions required by the core questions. | Bounded review outcome, claim scope, reason and inspected bundle; application decides qualification/abstention (11, 16). |

## 20. Mandatory V1 core versus deferred extensions

**Mandatory representation capability:** bounded AD/FTD references and audited disease context; target/drug references required by the questions; scoped associations; distinct evidence occurrences and attributable content; contextual mappings and ambiguity; selection/run/membership and explicit diagnostic paths; source/version/locator provenance; separate mechanisms, indications and study/population/status contexts; derived results; inspection/review and missingness; shared-source/dependency information; qualified answer/abstention boundaries.

Mandatory capability does not imply every source supplies all values or every association has a drug/trial. Missing information must be representable, not fabricated. Only records required by the bounded core are candidates for later acquisition. No global proposition registry, universal provenance wrapper, independent-evidence score or duplicated disease taxonomy is required.

**Deferred:** phenotype/frequency modelling; biological processes/pathways; broader dementia/subtree expansion; unrestricted descendant closure; comprehensive regulatory/product modelling; embeddings and LLM selection; KG embeddings/link prediction/graph ML; agents; property-graph projection; broad literature ingestion. No frozen requirement unexpectedly requires these expansions.

**Unselected implementation choices:** exact ontology names and namespace, source artifact acquisition, identifier allocation, MONDO encoding/import mechanics, provenance vocabulary, named graphs/RDF-star, OWL profile, executable inference rules, SHACL shapes, reasoner and triple store. This conceptual approval does not select them.

## 21. Approved commitments and unresolved implementation decisions

The owner approved the conceptual contract, including:

1. Scoped association identity including origin/source, disease/target, snapshot, aggregation definition and selection view; keeping source aggregates and project groupings distinguishable.
2. Evidence occurrence identity independent of retrieval encounters, with conservative treatment of unknown versions/IDs and no automatic identity repair.
3. Required first-class mapping observations and selection contexts with per-occurrence memberships; retaining unresolved and observed assignments separately.
4. SourceAssertion as required content/attribution role without a mandatory universal node; splitting claims where scope/provenance differs.
5. Context-bound study/population, inspection and missingness representation, including separate access and interpretation outcomes.
6. Dependency assessments based on traceable shared inputs, without automatic independence or an independence score.
7. Minimal candidate entailments and separation of semantic, validation, transformation and application responsibilities.

These conceptual commitments are approved. The approval also preserves the disease/source/anchor/selection distinctions, normalization without equivalence, separate clinical roles, derived statements versus source assertions, explicit technical review and missingness, the forbidden entailments, default open-world interpretation, and Q01–Q07/R1–R14 traceability.

This approval does not freeze ontology class names, property names, namespace, exact RDF encoding, provenance vocabulary, exact MONDO import/reference mechanics, OWL profile, reasoner, SHACL shapes, missingness code vocabulary, dependency vocabulary, triple store or software stack. Upstream mapping algorithms/snapshots, some source bodies, complete acquisition artifacts and clinical truth remain unresolved where recorded in M0. No investigation here resolves them. Graph advantage remains **NOT YET DEMONSTRATED**; design questions remain exposed design material, not held-out evaluation items.

## 22. Proposed next M1 task and review limits

After separate task authorization, prepare a **schema design proposal and decision crosswalk** from this contract: candidate record/class/property roles, disease-reference encoding options, provenance vocabulary mapping, identity/version representation, and a prose inventory of intended axioms versus validation/application checks. Resolve remaining choices before executable ontology construction. Do not begin that task automatically.

Review basis: the approved modelling-options comparison and frozen scope, question, requirement and source-audit documents. This is conceptual design analysis; no new biomedical source claims, dataset acquisition, reasoner execution, OWL consistency check or SHACL validation is claimed. Technical semantics follow the distinctions already explained and sourced in the modelling-options document. Matrix coverage is a design review, not proof of implementation correctness or evidence sufficiency.

Only this new Markdown document is created. Frozen documents and Q01–Q07/R1–R14 remain unchanged. The conceptual-design task created no ontology namespace, class/property implementation, RDF/OWL/TTL/JSON-LD, shapes, data instances, source code, dependencies, database configuration or SPARQL tests. The owner authorizes a local commit of this document only; no push or next M1 task is authorized.
