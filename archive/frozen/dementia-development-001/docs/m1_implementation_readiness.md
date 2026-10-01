# M1 Task 004 — schema minimization and implementation readiness

**M1 CHECKPOINT 3 APPROVED — V1 IMPLEMENTATION BASIS; IMPLEMENTATION NOT AUTHORIZED**

Baseline: `00eb97b Define M1 conceptual model contract`. The owner approved the schema-design investigation and this minimized implementation-readiness specification at M1 Checkpoint 3. The broader [schema design](m1_schema_design.md) remains the candidate pool; its complete 21/56/44 catalogue is not the frozen V1 schema. The minimized 20-class / 28-object-property / 39-datatype-property manifest is the approved implementation basis, subject only to explicit evidence from fixture implementation showing that a term must be added, removed, merged or revised. Ontology implementation is not authorized. The [conceptual contract](m1_conceptual_model_contract.md) and [Q01–Q07/R1–R14](competency_questions.md) remain authoritative. No ontology, vocabulary, identifier or KG instance is created here.

## 1. Decision rules and proposed reduction

**MANDATORY V1 (M):** needed to implement a frozen requirement, sometimes conditionally on source availability. **DERIVABLE / QUERY-TIME (Q):** safely computed from retained facts and declared settings. **OPTIONAL IMPLEMENTATION CONVENIENCE (O):** not in the first file. **DEFERRED (D):** outside the first implementation. **REMOVE (X):** redundant or unjustified candidate term; its necessary meaning is preserved at the named replacement, if any. These statuses apply to schema capability, not a requirement to invent unavailable data.

Reduction prioritizes removing redundant routes and generic execution machinery, not merging source facts with interpretations. Controlled states become literal enumerations, eliminating concept nodes and their object-property declarations. Some properties change category rather than disappear. New consolidated names and the execution-reference field are explicitly inventoried below; they introduce no biomedical capability.

The first-file manifest is exactly the M terms in sections 2–5 plus the vocabulary/axiom policy in sections 6–7. Q/O/D/X terms must not silently reappear in generated ontology. The retained catalogue is the owner-approved implementation basis, not an implemented ontology or a claim of mathematically minimal size.

## 2. Every class candidate and referent boundary

| Original candidate | Status | First-file choice and concrete reason | Q/R and contract basis |
| --- | --- | --- | --- |
| Record | X | Remove local superclass. Explicit PROV Entity typing for information resources supplies the common artifact role where needed. No inference needs a private Record superclass. | R6; Q01–07; C§1–3 |
| DiseaseConceptReference | M | Source-scoped identifier/label description, not disease individual or duplicate medical taxonomy. | R2–5; Q03–05; C§4 |
| Target | M | Reusable target referent for joins; gene indexing limits stay contextual. | R1,10; Q01–06; C§2–3 |
| Drug | M | Reusable drug referent for mechanisms and indications, without product equivalence. | R10–11,13; Q02,06–07; C§9 |
| DiseaseTargetAssociation | M | Scoped source aggregate/project grouping; cannot merge with occurrence. | R1,12; Q01–06; C§5 |
| EvidenceOccurrence | M | Provider record/version identity independent of retrieval. | R1,6,13; Q01–05; C§3,6 |
| MappingRecord | M | Assignment/context/ambiguity would be lost in a disease link. | R2–3,5; Q03–05; C§7 |
| SelectionContext | M | One retrieval/execution view with anchor, filters and result extent. | R4–5; Q01–06; C§8 |
| SelectionMembership | M | Occurrence membership in a run, distinct from mapping and path multiplicity. | R4–5,13; Q02–04; C§8 |
| HierarchyStep | M | An audited source assertion with its own locator/version; unqualified parent links lose source history. | R4–6; Q04; C§8 |
| HierarchyPath | M | Groups exactly one inspected chain, not the union of alternative paths. Removing it would require an equivalent grouping structure. Endpoints need not be stored. | R4–5; Q04; C§8 |
| Publication | M | Publication referent/locator identity shared across citations; not an experiment. | R7,13; Q01–02,06–07; C§6 |
| Study | M | Underlying investigation identity across reports/versions; necessary for shared trial provenance. | R7,11,13; Q02,07; C§9,13 |
| Trial | X | No class. A trial is identified by Study reference and original source text/registry context; no CQ needs trial-subclass entailment. | R11; Q02,07; C§9 |
| StudyRecord | M | Dated registry/report description of Study, retaining phase/status/design and population attachment. | R8,11; Q02,07; C§1,9 |
| MechanismRecord | M | Drug–target statement with its own source and molecular qualification. | R10; Q02,06–07; C§9 |
| ClinicalIndicationRecord | M | Drug–disease source entry, not mechanism or study. | R10–11; Q02,06–07; C§9 |
| PopulationScope | M | Source/arm-local population wording. Merging multiple cohorts into StudyRecord text would hide which restrictions qualify which cohort. | R11,14; Q07; C§9 |
| DerivedStatement | M | Persist reviewed comparisons/dependency conclusions with inputs, method and limits; raw query results need not all persist. | R12–14; Q02,04–05; C§10,13 |
| InspectionRecord | M | Claim-specific inspection/access/interpretation history; keep distinct from generic computation so required review context is explicit. | R8–9,14; Q01–07; C§11 |
| MissingnessRecord | M | Sparse field-specific absence/uncertainty with its observation basis; a null or reason on a predicate alone loses ownership. | R9,14; Q01,05–07; C§12 |
| DependencyAssessment | X | Use DerivedStatement with dependencyStatus, participants, basis and rationale. | R12–13; Q02; C§13 |
| SourceSnapshot | M | Versioned source artifact context, shared by records; release text alone does not identify it. | R6–9; Q01–07; C§3 |
| DatasetRelease | X | Known release information is snapshotVersion on SourceSnapshot; not a parallel artifact class. | R6–9; Q01–07; C§3 |
| SourceAssertion | X | No mandatory class; a source information slice can be explicitly prov:Entity with source identity, text, context and snapshot. No universal proposition registry. | R6–7,12; Q01–07; C§6 |
| ProvenanceRecord | X | No universal wrapper; attach qualified source/derivation facts to their actual owner. | R6–9; Q01–07; C§2 |
| RegulatoryApproval | D | No class or positive approval capability. Existing source wording can be retained without a current approval claim. | R10–11,14; Q06; C§9 |

**Twenty local classes survive.** This is only a one-class reduction from the actual 21-class proposal, not a claim that the original table had 27 retained classes. Trial, DependencyAssessment and other rejected aliases above were already considered/merged candidates and are shown to make the review exhaustive. Each surviving class has an independently needed identity or qualification role; replacing it with an untyped wrapper or packed text would shift, not remove, the structure.

### Publication, Study and StudyRecord: why all three remain

Publication identifies a citable report (for example a PMID), not an experiment. Study identifies the investigation (for example an NCT identifier). StudyRecord identifies one dated source description of that investigation; different registries, report versions or scoped descriptions can describe the same Study. A paper can report multiple studies; a study can have multiple publications. No automatic one-to-one mapping is allowed.

Q01 needs publication-to-occurrence citation identity without claiming a known study link. Q02 needs the same memantine trial to be recognized across distinct GRIN1/GRIN3B source occurrences. Q07 needs the original registry population/status for nct03658135 at the inspected date, separately from the mechanism publication and healthy-participant investigation. A later registry status creates a new StudyRecord describing the same Study. Q07 does not authorize inventing an underlying study identity for a publication where the source does not provide it.

PopulationScope is not the underlying cohort itself: it is a source-local description with arm/cohort wording and provenance. It can be shared only when that description identity is justified, not because strings match. HierarchyStep is a source assertion; HierarchyPath is an audited grouping. Record removal does not remove these distinctions: source-context slices can use prov:Entity without creating a new local claim class.

## 3. Object-property audit: all 56 candidates

The table reviews every original object property exactly once. M terms are retained object properties unless the row explicitly changes them to datatype properties. X rows name replacements where semantics survive. All usage signatures are validation targets, never implicit OWL domain/range declarations. No inverse property is stored merely for navigation.

| Original object property | Status | Decision / retained meaning | Frozen trace |
| --- | --- | --- | --- |
| inSnapshot | M | Retain: Source artifact/context describing this record. | R6–9; Q01–07; C§3,6 |
| contextRecord | M | Retain: Source panel/passage/context; not automatically support or derivation. | R3,6–7; Q01,03,05; C§6–7 |
| associationDisease | X | Merge into hasDiseaseReference; owner class distinguishes association scope from indication disease. | R1–2,4; Q01–06; C§4–5 |
| associationTarget | X | Merge into hasTarget; owner class identifies the association role. | R1; Q01–06; C§5 |
| reportedEvidence | M | Retain: Source-reported constituent, not independent support. | R1,6,13; Q01–02; C§5–6 |
| selectedEvidence | Q | For project grouping, derive EvidenceOccurrence inputs through prov:wasDerivedFrom. Source constituents remain reportedEvidence. | R1,12; Q01–04; C§5,10 |
| originalDisease | Q | Reverse mappingContext to MappingRecord, then mappingInput. Preserve an input-only observation if destination is unavailable. | R2; Q01,03,05; C§4,6 |
| evidenceTarget | X | Merge into hasTarget on EvidenceOccurrence. | R1,6; Q01–05; C§6 |
| hasMappingRecord | Q | Reverse mappingContext, filtering the specific EvidenceOccurrence; panel context uses contextRecord. | R2–3,5; Q03–05; C§7 |
| mappingContext | M | Retain: Specific occurrence/panel context of assignment. | R3,6; Q03,05; C§7 |
| mappingInput | M | Retain: Original reference when identifiable. | R2–3; Q03,05; C§7 |
| reportedDestination | M | Retain: Observed platform destination. | R2–3,5; Q03–05; C§7 |
| candidateDestination | M | Retain: Possible mapping, not asserted assignment/equivalence. | R3; Q05; C§7 |
| queryAnchor | M | Retain: Requested disease in this context. | R4–5; Q01–05; C§8 |
| selectedOccurrence | M | Retain: Occurrence encountered in the result. | R4,13; Q02–04; C§8 |
| inSelectionContext | M | Retain: Run/view for membership or scoped comparison/grouping. | R4–5,12; Q01–06; C§8,10 |
| justificationPath | M | Retain: Inspected path explanation, not hidden source execution. | R4–5; Q04; C§8 |
| pathStep | M | Retain: Steps forming one validated directed chain. | R4–6; Q04; C§8 |
| pathStart | Q | Unique child endpoint without incoming chain step after path validation; absent/ambiguous on invalid path. | R4; Q04; C§8 |
| pathEnd | Q | Unique parent endpoint without outgoing chain step after path validation; no guess if incomplete. | R4; Q04; C§8 |
| childReference | M | Retain: Source child concept reference. | R4–5; Q03–05; C§8 |
| parentReference | M | Retain: Source parent concept reference. | R4–5; Q03–05; C§8 |
| citesPublication | M | Retain: Citation at the source's actual attribution scope. | R7,13; Q01–03,06–07; C§6 |
| refersToStudy | M | Retain: Explicit study reference, not identity with publication. | R7,11,13; Q02,07; C§6,9 |
| describesStudy | X | Merge into refersToStudy; StudyRecord owner means this is the described underlying study, with exactly one expected. | R11; Q02,07; C§9 |
| mechanismDrug | X | Merge into hasDrug on MechanismRecord. | R10,13; Q02,06–07; C§9 |
| mechanismTarget | X | Merge into hasTarget on MechanismRecord. | R10; Q02,06–07; C§9 |
| indicationDrug | X | Merge into hasDrug on ClinicalIndicationRecord. | R10–11; Q02,06–07; C§9 |
| indicationDisease | X | Merge into hasDiseaseReference on ClinicalIndicationRecord. | R10–11; Q06–07; C§9 |
| indicationStudyRecord | M | Retain: Source-linked clinical report; no arbitrary drug-wide join. | R7,11; Q02,07; C§9 |
| hasPopulationScope | M | Retain: Population restriction of this report/claim. | R11,14; Q07; C§9 |
| inputRecord | X | Use prov:wasDerivedFrom for actual input information resources. Referent comparison roles remain subjectRecord/comparatorRecord/sharedInput, not invented artifact derivation. | R12–13; Q01–07; C§10,13 |
| resultTarget | Q | Recompute bounded intersection from input association/evidence hasTarget values and stored method/settings; reviewed result is retained through summary/rationale and input lineage. | R12; Q01 comparison; C§10 |
| subjectRecord | M | Retain: Focus of dependency/membership/comparison assessment. | R12–14; Q02,04–05; C§10,13 |
| comparatorRecord | M | Retain: Other assessed record; role is not symmetric by default. | R12–13; Q02,04–05; C§10,13 |
| sharedInput | M | Retain: Established or assessed common publication/study/record, qualified by outcome. | R12–13; Q02; C§13 |
| inspectedRecord | M | Retain: Specific version/passage inspected or attempted. | R8–9; Q01–07; C§11 |
| aboutRecord | M | Retain: Record whose interpretation is assessed, or field-owning resource (including snapshot) whose information is missing. | R8–9,14; Q01–07; C§11–12 |
| observationContext | M | Retain: Inspection/retrieval context establishing the missingness observation. | R9,14; Q01,05–07; C§12 |
| originRole | M | Change to literal enumeration; no controlled-concept nodes. Retain name. | R1,12; Q01–06; C§5 |
| selectionMode | M | Change to literal enumeration; no controlled-concept nodes. Retain name. | R4–5; Q04; C§8 |
| inclusionKind | M | Change to literal enumeration; no controlled-concept nodes. Retain name. | R4–5; Q04; C§8 |
| mappingStatus | M | Change to literal enumeration; no controlled-concept nodes. Retain name. | R3; Q05; C§7 |
| inspectionDepth | M | Change to literal enumeration; no controlled-concept nodes. Retain name. | R8; Q01,06–07; C§11 |
| materialKind | M | Change to literal enumeration; no controlled-concept nodes. Retain name. | R8; Q01,06–07; C§11 |
| accessOutcome | M | Change to literal enumeration; no controlled-concept nodes. Retain name. | R8–9; Q01,05–07; C§11 |
| interpretationOutcome | M | Change to literal enumeration; no controlled-concept nodes. Retain name. | R14; Q01–07; C§11 |
| missingnessReason | M | Change to literal enumeration; no controlled-concept nodes. Retain name. | R9,14; Q01,05–07; C§12 |
| dependencyOutcome | M | Change to literal enumeration; no controlled-concept nodes. Rename dependencyStatus. | R13; Q02; C§13 |
| completenessStatus | M | Change to literal enumeration; no controlled-concept nodes. Retain name. | R9,12,14; Q01–07; C§8,10,16 |
| studyKind | D | No trial subclass or study-kind code needed for current questions; registry identity and original sourceText preserve trial context. | R11; Q02,07; C§9 |
| reviewerType | M | Change to literal enumeration; no controlled-concept nodes. Reviewer type belongs to InspectionRecord, not Agent. | R8,14; Q01–07; C§11 |
| prov:wasGeneratedBy | D | No separate activity nodes in first V1. executionReference, observedAt, operationMethod and methodVersion stay on result/context records. | R6,8,12; Q01–07; C§10–11 |
| prov:used | D | Actual informational inputs use prov:wasDerivedFrom; no separate activity graph needed. | R6,12; Q01–07; C§10 |
| prov:wasAssociatedWith | D | Actual inspector identity/type are literal metadata on InspectionRecord; no Agent node necessary. | R6,8; Q01–07; C§11 |
| prov:wasDerivedFrom | M | Retain: Documented information lineage, not clinical support. | R6,12–13; Q01–07; C§6,10 |

Consolidated mandatory replacements (not additional biomedical capabilities):

| New name | Owners → target | Meaning / boundary | Trace |
| --- | --- | --- | --- |
| hasTarget | DiseaseTargetAssociation, EvidenceOccurrence, MechanismRecord → Target | Source-indexed target of the typed owner; does not turn mechanism into association | R1,10; Q01–06; C§5–6,9 |
| hasDrug | MechanismRecord, ClinicalIndicationRecord → Drug | Drug participant; relation type remains on the owner | R10–11; Q02,06–07; C§9 |
| hasDiseaseReference | DiseaseTargetAssociation, ClinicalIndicationRecord → DiseaseConceptReference | Disease participant with owner-specific scope; never used for mapping identity | R1–2,10–11; Q01–07; C§4–5,9 |

## 4. Datatype-property audit: all 44 candidates

Presence notation in the retained-description column: R = required for that applicable owner, C = conditional on source availability/applicability. Provenance notation: S = source-preserved, G = generated, M = either with origin recorded (distinct from the disposition column M). Where needed for interpretation, supply explicit missingness instead of inventing a value. The original candidate datatype/meaning applies to M rows unless narrowed below.

| Original datatype property | Status | Decision / first-file meaning | Frozen trace |
| --- | --- | --- | --- |
| externalIdentifier | M | Retain: Authority-qualified external ID; string. C / S | R2,7,10–11; Q01–07; C§3–4,9 |
| identifierAuthority | M | Retain: Identifier authority/system; string. R when ID present / S | R2,7; Q01–07; C§3–4 |
| externalIRI | O | External identifier plus authority is enough. A resolver-generated URL is optional and only valid with an explicit resolver; do not assume resolution for arbitrary IDs. | R2–3; Q03–05; C§4 |
| sourceLabel | M | Retain: Original observed label; string or language-tagged text. C / S | R2–3,11; Q03,05,07; C§4,9 |
| sourceRecordIdentifier | M | Retain: Provider record ID, not semantic identity by itself. C / S | R1,6,13; Q01–07; C§3,6 |
| sourceLocator | M | Retain: URL/document/passage locator; string, URI form when applicable. C / S | R6–7; Q01–07; C§6 |
| sourceAuthority | M | Retain: Dataset/platform/provider name or identifier; string. R / S | R6; Q01–07; C§3 |
| snapshotVersion | M | Retain: Reported release/version; string. C / S | R6,9; Q01–07; C§3 |
| artifactDescription | M | Retain: Acquisition/artifact identity and extent; string. R / M | R6,9; Q01–07; C§3 |
| observedAt | M | Retain: Actual observation/retrieval date; dateTime or date at known precision. R for project encounters / G | R6,8; Q01–07; C§3,11 |
| recordVersion | M | Retain: Source record-specific version where supplied; string. C / S | R6,9; Q01–07; C§3 |
| scopeText | M | Retain: Scope, cohort, panel, gene context or qualified claim content; string. R when required to interpret claim / M | R3,11–14; Q01–07; C§6–13 |
| evidenceSourceType | M | Retain: Provider datasource/evidence category verbatim; string. C / S | R1,6,13; Q01–02; C§6 |
| inputIdentifier | X | mappingInput reference externalIdentifier preserves the raw source identifier. | R2–3; Q03,05; C§7 |
| inputLabel | X | mappingInput reference sourceLabel preserves the raw input label. | R2–3; Q03,05; C§7 |
| reportedMappedIdentifier | X | reportedDestination reference externalIdentifier preserves the reported destination string; do not replace it with an invented normalized code. | R2–3,5; Q03–05; C§7 |
| mappingAuthority | X | Use sourceAuthority on MappingRecord for known assigning authority; sourceAuthority on SourceSnapshot remains artifact provider. | R3,6; Q03,05; C§7 |
| mappingProcess | X | Use operationMethod/methodVersion on MappingRecord, with source attribution and explicit missingness for unknown process. | R3,5; Q03,05; C§7 |
| aggregationMethod | X | Use operationMethod/methodVersion on DiseaseTargetAssociation; owner and originRole fix its meaning. | R1,6,12; Q01–02; C§3,5 |
| aggregateScore | M | Retain: Source-defined numeric aggregate; decimal. C / S | R1,14; Q01–02; C§5 |
| scoreDefinition | M | Retain: Source scoring semantics/method reference; string. C; needed to interpret score / S | R1,6,14; Q01–02; C§5 |
| scoreComponent | O | First V1 supports one interpreted source score per association. scoreDefinition must state its component/total scope. Multiple separately structured component scores are not required. | R1,6; Q01–02; C§5 |
| filterSpecification | M | Retain: Exact known source filters/settings; string. R for selection; relevant for scoped aggregate / M | R4–5,12; Q01–06; C§3,8 |
| operationMethod | M | Retain: Documented operation and method meaning; string. R for project outputs / G | R5,12–13; Q02,04–05; C§8,10 |
| methodVersion | M | Retain: Method revision when known/defined; string. C / M | R6,12; Q02,04–05; C§10 |
| limitationText | M | Retain: Explicit interpretation/completeness limitation; string. R where limitation applies / M | R9,14; Q01–07; C§10–12 |
| mechanismText | X | Use sourceText on MechanismRecord; preserve original action/molecular qualification. | R10; Q06–07; C§9 |
| populationText | X | Use sourceText on PopulationScope; preserves original cohort restrictions. | R11,14; Q07; C§9 |
| armLabel | X | Use sourceLabel on PopulationScope; no second synonym label property. | R11; Q07; C§9 |
| studyDesignText | X | Use sourceText on StudyRecord; preserve original design wording. | R11,14; Q07; C§9 |
| trialPhaseText | M | Retain: Original phase or indication-level phase summary, retaining owner meaning; string. C / S | R11; Q02,07; C§9 |
| trialStatusText | M | Retain: Dated reported status; string. C / S | R11; Q02,07; C§9 |
| statusDate | M | Retain: Source's status date if known; date. C / S | R11; Q02,07; C§9 |
| approvalLabel | X | Retain any relevant original approval assertion verbatim in sourceText on a contextual source information slice; no structured positive-approval capability. | R10–11,14; Q06; C§9 |
| jurisdictionText | X | Preserve within the same sourceText approval assertion/context, not as a new regulatory query field. | R11,14; Q06; C§9 |
| regulatoryAuthorityText | X | Preserve within the same sourceText approval assertion/context; no new regulatory ontology. | R11,14; Q06; C§9 |
| productScopeText | X | Preserve within the same sourceText approval assertion/context; never equate platform drug with an unrestricted product approval. | R10–11,14; Q06; C§9 |
| effectiveDateText | X | Preserve original precision in that sourceText; no current-approval inference. | R11,14; Q06; C§9 |
| expectedField | M | Retain: Governed field/meaning token whose information is missing/unresolved; string. R / G | R9,14; Q01,05–07; C§12 |
| rationale | M | Retain: Technical basis, including dependency basis; string. R for assessment / G | R8–9,13–14; Q01–07; C§11–13 |
| resultSummary | M | Retain: Bounded human-readable finding; string; not sole structured result. R / G | R12–14; Q01–07; C§10 |
| agentIdentifier | X | Use reviewerIdentifier literal on InspectionRecord, preserving actual technical reviewer/process identity. | R6,8; Q01–07; C§11 |
| prov:startedAtTime | O | No Activity nodes. observedAt plus executionReference suffice for design questions; runtime intervals can remain application logs. | R6,8,12; Q01–07; C§10–11 |
| prov:endedAtTime | O | Same: no required timing-duration query; retain inspection/retrieval observation date. | R6,8,12; Q01–07; C§10–11 |

Mandatory replacement/additional literal fields:

| Name | Type / owner | Why retained | Trace |
| --- | --- | --- | --- |
| sourceText | string / MechanismRecord, PopulationScope, StudyRecord or contextual prov:Entity source slice | Exact relevant source wording; typed owner/record scope separates mechanism, population, design and any approval limitation. Not a dump of unrelated source content. | R10–11,14; Q06–07; C§9 |
| reviewerIdentifier | string / InspectionRecord | Actual inspector/process identity without a separate Agent node; unavailable identity is explicit, not an invented expert. | R6,8; Q01–07; C§11 |
| executionReference | string / SelectionContext, InspectionRecord, DerivedStatement (and computational HierarchyPath if independently produced) | Audit execution reference supplied by the acquisition/review process, distinguishing same-time reruns. Preserves an identity input that timestamps alone cannot supply. No UUID format or value is created. | R6,8,12; Q01–07; C§3,10–11 |

Twelve M object-property candidates become literal fields: originRole, selectionMode, inclusionKind, mappingStatus, inspectionDepth, materialKind, accessOutcome, interpretationOutcome, missingnessReason, dependencyStatus, completenessStatus, reviewerType. Their exact owner/enum policy is specified in section 5; no term is simultaneously an object and datatype property.

### Count reconciliation and exact retained names

- Local classes: **20**, versus 21 (Record removed; no new class).
- Object properties: **28** total, versus 56; includes one external PROV relation.
- Datatype properties: **39** total, versus 44; includes the 12 converted controlled-state fields and 3 replacements/identity fields. No external datatype properties are required.

**Object-property manifest:** inSnapshot, contextRecord, reportedEvidence, mappingContext, mappingInput, reportedDestination, candidateDestination, queryAnchor, selectedOccurrence, inSelectionContext, justificationPath, pathStep, childReference, parentReference, citesPublication, refersToStudy, indicationStudyRecord, hasPopulationScope, subjectRecord, comparatorRecord, sharedInput, inspectedRecord, aboutRecord, observationContext, prov:wasDerivedFrom, hasTarget, hasDrug, hasDiseaseReference.

**Datatype-property manifest:** externalIdentifier, identifierAuthority, sourceLabel, sourceRecordIdentifier, sourceLocator, sourceAuthority, snapshotVersion, artifactDescription, observedAt, recordVersion, scopeText, evidenceSourceType, aggregateScore, scoreDefinition, filterSpecification, operationMethod, methodVersion, limitationText, trialPhaseText, trialStatusText, statusDate, expectedField, rationale, resultSummary, originRole, selectionMode, inclusionKind, mappingStatus, inspectionDepth, materialKind, accessOutcome, interpretationOutcome, missingnessReason, dependencyStatus, completenessStatus, reviewerType, sourceText, reviewerIdentifier, executionReference.

### Retained object signatures and field placement

These signatures are for future validation. They create no global OWL domain/range. “Information resource” means an explicitly described source/result artifact, including a source slice typed prov:Entity; it is not a new class. References to Study/Publication denote their referents, not fabricated study artifacts. All inverse navigation is query-time.

| Object property | Allowed owner → value; restriction |
| --- | --- |
| inSnapshot | Information resource → SourceSnapshot; preserve source/version context |
| contextRecord | Information resource → information resource; panel/passage context, not automatically evidential support |
| reportedEvidence | Source-origin DiseaseTargetAssociation → EvidenceOccurrence; source-reported contribution |
| mappingContext | MappingRecord → EvidenceOccurrence or contextual source information resource; panel uses contextRecord where separate |
| mappingInput | MappingRecord → DiseaseConceptReference; original reference if supplied |
| reportedDestination | MappingRecord → DiseaseConceptReference; observed assignment |
| candidateDestination | MappingRecord → DiseaseConceptReference; possible assignment only |
| queryAnchor | SelectionContext → DiseaseConceptReference |
| selectedOccurrence | SelectionMembership → EvidenceOccurrence |
| inSelectionContext | SelectionMembership, DerivedStatement or project-grouping DiseaseTargetAssociation → SelectionContext |
| justificationPath | SelectionMembership → HierarchyPath; inspected explanation, not undocumented source execution |
| pathStep | HierarchyPath → HierarchyStep; exactly the explicit chain's steps |
| childReference | HierarchyStep → DiseaseConceptReference |
| parentReference | HierarchyStep → DiseaseConceptReference |
| citesPublication | Information resource → Publication; citation at actual source scope |
| refersToStudy | Information resource → Study; StudyRecord has exactly one described Study, other sources may reference several |
| indicationStudyRecord | ClinicalIndicationRecord → StudyRecord; actual source-linked report |
| hasPopulationScope | StudyRecord or scoped source information resource → PopulationScope |
| subjectRecord | DerivedStatement → information resource; focus of assessment |
| comparatorRecord | DerivedStatement → information resource; comparison partner, not implicitly symmetric |
| sharedInput | DerivedStatement → Publication, Study or information resource; qualified common basis |
| inspectedRecord | InspectionRecord → source information resource; specific inspected version/slice or attempted source description |
| aboutRecord | InspectionRecord or MissingnessRecord → affected identified resource; review owner or missing-field owner |
| observationContext | MissingnessRecord → InspectionRecord or SelectionContext or other documented observation result |
| prov:wasDerivedFrom | DerivedStatement, project-grouping association or locally derived information resource → input information resource; never clinical support |
| hasTarget | DiseaseTargetAssociation, EvidenceOccurrence or MechanismRecord → Target |
| hasDrug | MechanismRecord or ClinicalIndicationRecord → Drug |
| hasDiseaseReference | DiseaseTargetAssociation or ClinicalIndicationRecord → DiseaseConceptReference |

A source aggregate's retrieval encounter does not become its origin. For a project grouping, every directly linked EvidenceOccurrence input under prov:wasDerivedFrom is a selected constituent, and every selected constituent must be directly linked. Ancillary occurrence context that is not a constituent uses contextRecord instead; other artifact input types do not count as selected occurrences. This operation-specific contract makes selected membership recoverable without an ambiguous generic provenance join. Source aggregate reportedEvidence remains separate. MappingRecord is an observation of source normalization and may use mappingContext without claiming that the project performed the upstream normalization. Duplicate observations are not multiple independent supports.

Literal owner rules complete the datatype manifest:

- externalIdentifier/identifierAuthority: DiseaseConceptReference, Target, Drug, Publication, Study. sourceLabel: observed label on these or source information descriptions, including arm/cohort label on PopulationScope.
- sourceRecordIdentifier/recordVersion/sourceLocator/inSnapshot: versioned source descriptions, including evidence, mappings when supplied, mechanisms, indications and StudyRecord. SourceSnapshot also has sourceLocator. Identifiers absent from source remain absent with relevant reason.
- sourceAuthority: SourceSnapshot's provider, or MappingRecord's reported assigning authority; these owners distinguish the roles. snapshotVersion/artifactDescription: SourceSnapshot only.
- observedAt: actual observation date on snapshots, SelectionContext, InspectionRecord and derived results. executionReference: SelectionContext, InspectionRecord, DerivedStatement and independently computed HierarchyPath. Neither is a source release identifier.
- scopeText/limitationText: information resources whose claims/results need scope/limitations. They do not replace structured disease, target, study, mapping or input links.
- evidenceSourceType: EvidenceOccurrence. aggregateScore/scoreDefinition: source-origin DiseaseTargetAssociation, conditional; not project grouping. filterSpecification: SelectionContext and association view where relevant.
- operationMethod/methodVersion: MappingRecord's known source process; association's aggregate/grouping definition; SelectionContext's retrieval/traversal; DerivedStatement's computation; InspectionRecord's review method; HierarchyPath's construction if independently computed. Source-provided versus project-defined origin follows the typed record and provenance; unknown process/version stays unknown.
- trialPhaseText: StudyRecord or ClinicalIndicationRecord, preserving trial versus indication-summary meaning. trialStatusText/statusDate: StudyRecord only.
- expectedField: MissingnessRecord. rationale: InspectionRecord, MissingnessRecord, DerivedStatement. resultSummary: DerivedStatement, explanatory, never the sole structured basis.
- sourceText: typed clinical descriptions or source slices as above. reviewerIdentifier/reviewerType: InspectionRecord; a technical process/human identity with explicit actual review type, not an expert credential claim.
- Remaining literal states use exactly the owners in section 5. Literal enums and identifier/method fields are strings; source wording may preserve an actual language tag. aggregateScore is decimal. observedAt accepts date or dateTime at actual known precision; statusDate accepts date when source supplies a date (otherwise retain original wording in sourceText and a reason). No synthetic timestamps are created to pass checks.

## 5. Controlled-value decisions: no concept individuals in first V1

Each M row becomes a literal enumeration checked by a later validation layer. These are proposed exact token spellings for owner review; no individuals or OWL oneOf restrictions are created. Stored meanings, not application constants alone, must survive export. Application constants may mirror the approved literal list later.

| Field / owner | Status / representation | Proposed distinctions/tokens; boundary | Trace |
| --- | --- | --- | --- |
| originRole / DiseaseTargetAssociation | M / literal | source-aggregate, project-grouping | R1,12; Q01–06 |
| selectionMode / SelectionContext and scoped association | M / literal | direct-only, descendant-inclusive; unknown represented by missingness, not a false direct value | R4–5; Q04 |
| inclusionKind / SelectionMembership | M / literal | exact-anchor, descendant-selected, unresolved; persist observed/classified basis in scopeText and context | R4–5; Q04 |
| mappingStatus / MappingRecord | M / literal | input-only, validity-unreviewed, unresolved, reviewed-with-limits; input-only means known original context with no asserted destination, not a made-up normalization | R2–3,5; Q03,05 |
| inspectionDepth / InspectionRecord | M / literal | metadata-only, selected-passages, full-relevant-material; interpreted with materialKind and scopeText | R8; Q01,06–07 |
| materialKind / InspectionRecord | M / literal | metadata, abstract, full-text-source, registry-page, source-page; original material qualifier in scopeText where needed | R8; Q01–07 |
| accessOutcome / InspectionRecord | M / literal | accessible, partially-accessible, inaccessible, not-attempted | R8–9; Q01,05–07 |
| interpretationOutcome / InspectionRecord | M / literal | source-record-supported, not-established-by-bundle, mapping-ambiguous, access-limited, not-assessed | R14; Q01–07 |
| missingnessReason / MissingnessRecord | M / literal | source-omission, not-retrieved, inaccessible, not-applicable, not-inspected, unresolved, reason-unknown | R9,14; Q01,05–07 |
| dependencyStatus / DerivedStatement | M / literal | shared-source-established, dependence-established, possible-dependence, independence-assessed-with-limits, unresolved | R13; Q02 |
| completenessStatus / bounded information/result resource | M / literal | complete-for-declared-scope, partial, unknown; scopeText must identify the scope | R9,12,14; Q01–07 |
| reviewerType / InspectionRecord | M / literal | human-technical-review, software-assisted-technical-review, automated-check; actual identity and method required or explicitly unavailable | R8,14; Q01–07 |
| studyKind / Study | D | No persisted enum. Source identity and sourceText distinguish known trial context; no clinical inference depends on a trial subclass. | R11; Q02,07 |

These enums describe separate dimensions. Accessible does not mean inspected; full relevant abstract is not full-paper review. A single reviewed claim has its own interpretation record; one paper can lead to several scoped outcomes. A dependency assessment with shared-source-established does not assert complete dependence or independence. No positive domain-expert value is introduced for this project.

Record-level missingness applies to an expected field/meaning, e.g. mapping validity versus destination value. A provided destination and unresolved validity can coexist. Do not recursively generate missingness for every unused field on a MissingnessRecord. expectedField tokens must be drawn from the retained field names or an explicitly documented interpretation requirement; its first validation catalogue must cover all Q-required gaps before implementation acceptance.

## 6. Exact minimal PROV subset

| External term | Status | Use / why not more |
| --- | --- | --- |
| prov:Entity | M | Explicit type on information artifacts: source descriptions, snapshots, inspection/derived results and contextual slices. It avoids a local Record superclass, without claiming biomedical truth. |
| prov:wasDerivedFrom | M | Actual input information lineage for project comparisons/groupings and other known informational derivations. Not a support/independence relation and not automatically transitive. |
| prov:Activity | D | Separate execution nodes are not needed to answer current questions; run/result records preserve execution reference, date and method. |
| prov:Agent | D | Inspector identity/type can be preserved as literals. No agent-network question exists. |
| prov:wasGeneratedBy | D | No Activity graph in first file; do not duplicate event metadata. |
| prov:used | D | Input artifacts already linked by wasDerivedFrom; no extra execution join required. |
| prov:wasAttributedTo | D | No agent node; sourceAuthority and reviewerIdentifier retain the required attribution with scoped owners. This was considered explicitly, not omitted accidentally. |
| prov:wasAssociatedWith | D | Likewise no Agent/Activity graph. Never a disease association. |
| prov:startedAtTime / prov:endedAtTime | O | Timings may remain logs; actual observation date and collision-disambiguating executionReference persist. |

Use external term IRIs by reference, without importing PROV-O or copying its whole axiom set. Explicit Entity typing on information artifacts is a future data-generation obligation; no local subclass axiom is required for it. Target/Drug/Study referents are not automatically called information artifacts. If provenance needs a study as an input, use the actual StudyRecord/source artifact; sharedInput can independently identify the underlying Study as the subject of the comparison. This keeps informational lineage distinct from referent co-reference.

This reduction preserves provenance, not necessarily a full PROV event model. Project-specific mappingContext, inSnapshot, selection membership and review relations remain preferable because wasDerivedFrom cannot mean normalization validity, query membership or inspected support. No activity is inferred merely because a source transformation is suspected.

## 7. Axiom and domain/range audit

| Candidate from broader schema | Status | Purpose/entailment and risk | Q/R justification / first-file decision |
| --- | --- | --- | --- |
| Local subclasses under Record | X | Would classify description records, but no core query needs this inference; removing Record avoids the decorative hierarchy | R6 preserved by explicit artifact typing |
| Record/SourceSnapshot subclass prov:Entity | Q | Useful type is asserted explicitly on information artifacts; no inferential bridge necessary | R6/12; Q01–07 |
| Project grouping also typed DerivedStatement | O | Could reuse shapes; originRole plus operation-specific checks already suffice. No dual-type rule required | R1/12; Q01–06 |
| Association disjoint EvidenceOccurrence | O | Could detect a wrong type, but shape/ingestion role checks can do so without global inconsistency. Not needed for an answer | R1; Q01–02 |
| MechanismRecord disjoint ClinicalIndicationRecord | O | Same record-boundary check can be structural; no desired entailment requires disjointness | R10; Q06–07 |
| Inverse properties | Q | Reverse traversal yields navigation without extra vocabulary or duplicated assertions | All core traversals |
| Global domain/range | X for first file | No required new typing inference; can hide bad data by inferring unexpected types | Role constraints remain structural |
| Exact/minimum cardinalities, functionality or identity keys | X for first file | Can introduce anonymous existence or forced equality rather than report missing/conflicting source data | R1–5,9,13 |
| Automatic hierarchy transitivity/property chains | X | Would exceed bounded paths or imply misleading parent support | R4–5; Q04 |

**Smallest axiom set: declarations only.** Twenty class declarations, the retained local object/datatype declarations, and reference to the selected external terms. No local subclass, subproperty, inverse, domain/range, disjointness, cardinality, key, property-chain, equality or transitivity axioms are needed in the first file. No nontrivial biomedical entailment is requested. This is an intentional semantic vocabulary with explicit typed records and later constraints, not a claim that a reasoner adds value.

All 56 original property domain/range options receive the same first-file decision: no local global domain/range axiom. For retained participant, mapping, hierarchy, clinical, inspection, missingness and provenance fields, use the section 3 signatures as validation targets. Converted literal states have datatype/value checks, not inferred owners. Removed/derived properties have no declarations or axioms. Existing external PROV meanings must be respected without redefining their domains/ranges or importing them. **No exception is presently justified.**

Forbidden axioms remain: normalization-based sameAs/equivalentClass or SKOS exactMatch; mapping functionality; mechanism→indication chains; indication→efficacy; trial→success; phase→completion; descendant selection→direct parent evidence; citation→support; repeated citation→independence; missing fact→global negation; score→causality/probability; identifier resemblance→identity; technical review/validation→biomedical truth. These prohibitions also apply to application transformations, not just OWL syntax.

## 8. Disease-reference desk checks: conceptual triples only

The following are prose subject–relation–object sketches, not Turtle, allocated local identifiers or created KG instances. Labels such as “AD reference” are placeholders. The references preserve exact source strings and are scoped to the actual observed source context; identifierAuthority names the identifier system, not proof the authority's website was inspected.

| Case | Conceptual triples using retained properties | Result and boundary |
| --- | --- | --- |
| AD anchor | AD reference — externalIdentifier → MONDO:0004975; — identifierAuthority → MONDO; — sourceLabel → Alzheimer disease; — inSnapshot → inspected platform context. AD association — hasDiseaseReference → AD reference. AD selection — queryAnchor → AD reference. | Same justified reference may play anchor and query roles, but the role links stay different. No AD class instance or axiom import. |
| FTD anchor | FTD reference — externalIdentifier → MONDO:0017276; — identifierAuthority → MONDO; — sourceLabel → frontotemporal dementia; — inSnapshot → inspected platform context. FTD association — hasDiseaseReference → FTD reference. | Broad approved anchor, not automatic bvFTD substitution or descendant ingestion. |
| Pick original / mapped FTD | Pick-original reference — externalIdentifier → OMIM:172700; — sourceLabel → original Pick wording as recorded; — identifierAuthority → OMIM. Pick mapping — mappingContext → sampled MAPT occurrence; — mappingInput → Pick-original reference; — reportedDestination → FTD reference. Membership — selectedOccurrence → that MAPT occurrence; — inSelectionContext → direct FTD context. | Preserves narrower original meaning and observed destination. Separately sourced Pick MONDO:0008243 is another context reference/HierarchyStep participant, not an asserted equivalence or explanation of this row's direct selection. |
| OMIM:600274 ambiguity | PSEN1 mapping — mappingContext → PSEN1/panel-265 occurrence; — mappingInput → its original OMIM:600274 reference; — reportedDestination → FTD reference. MAPT mapping — mappingContext → MAPT/panel-540 occurrence; — mappingInput → its original OMIM:600274 reference; — reportedDestination → semantic-dementia reference with externalIdentifier MONDO:0010857. Both mappings — mappingStatus → unresolved; each occurrence — contextRecord → its panel source description. | Compare authority-qualified original IDs while retaining different source labels/context/version. Do not merge references or repair destinations. No assertion of canonical OMIM interpretation. |

Each reference has snapshot/context or explicit relevant missingness. Original labels are placeholders for the already recorded exact strings where not printed above; no new synonym or identifier resolution is asserted. When original identity exists but no assignment is supplied, a MappingRecord with input-only status retains mappingInput without inventing a destination. When only a destination exists, retain it and its input/process missingness separately.

Direct MONDO class-IRI use could still represent these cases with extra contextual records, but the single external class IRI alone cannot carry two source-local observations without qualification. Local references make those observations explicit and avoid class/individual punning. This is an application-specific clarity advantage, not a claim that the alternative is impossible or logically invalid.

## 9. Persisted versus derived facts

“Persisted” below is a future representation obligation, not data created in this task. A reviewed derived statement may be stored even when its raw computation is query-time.

| Important fact | Category | Retained representation / boundary |
| --- | --- | --- |
| Source aggregate participants, origin and score | Persisted source fact | association hasTarget/hasDiseaseReference, originRole, aggregateScore and scoreDefinition; score optional/source-defined |
| Source-reported evidence membership | Persisted source fact | reportedEvidence; never inferred from query result alone |
| Original disease wording / normalized destination | Persisted source fact | MappingRecord with mappingInput/reportedDestination reference fields; process unknown remains unknown |
| Candidate mapping / ambiguity assessment | Persisted project metadata or persisted derived result, according to origin | candidateDestination and mappingStatus with source or review context; no replacement of observed destination |
| Snapshot/version/source locator | Persisted source fact plus observed acquisition metadata | SourceSnapshot, source identity/version, observedAt; distinguish source version from retrieval date |
| Retrieval settings and execution | Persisted project metadata | SelectionContext: anchor, mode, filters, snapshot, executionReference, observedAt, completenessStatus |
| Observed query membership | Persisted project metadata | SelectionMembership: selectedOccurrence, context; preserves actual observed result, not reconstructed source execution |
| Inclusion classification and explanation | Persisted derived metadata | inclusionKind, justificationPath, scoped basis; source result presence alone does not prove the explanation |
| Hierarchy steps | Persisted source fact | HierarchyStep childReference/parentReference, snapshot/locator |
| Path grouping | Persisted project metadata or derived result | HierarchyPath pathStep, construction method and provenance; path endpoints queried from validated chain |
| Shared publication/trial references | Persisted source facts | citesPublication/refersToStudy. Equality of justified reference identity enables comparison |
| “These two records share a publication” raw join | Query-time derivation | Compare cited publication identities; not automatically statistical dependence |
| Reviewed dependency conclusion | Persisted derived result | DerivedStatement subjectRecord/comparatorRecord/sharedInput, dependencyStatus, input lineage, rationale/scope |
| “AD and FTD share sampled target X” | Query-time derivation; persisted derived result only if reviewed/exported as an auditable conclusion | Recompute intersection from scoped inputs via hasTarget; stored resultSummary is checked against those inputs, not its sole structured truth |
| Project grouping selectedEvidence shortcut | Query-time derivation | Filter grouping's prov:wasDerivedFrom inputs to EvidenceOccurrence; do not persist a second membership list |
| Mapping reverse navigation and path endpoints | Query-time derivation | Reverse mappingContext; validated chain topology, respectively |
| Phase/status/population | Persisted source fact | StudyRecord phase/status/date and hasPopulationScope; original sourceText |
| Actual inspection depth/access/reviewer | Persisted project metadata | InspectionRecord with source version/scope, reviewer identity/type, observedAt/executionReference |
| Scoped support/abstention judgment | Persisted derived review result | InspectionRecord interpretationOutcome/rationale/limitationText, attached to aboutRecord and inspectedRecord |
| Missingness reason | Persisted project metadata or recorded source observation | MissingnessRecord owner/expectedField/reason/context; source-omission restricted to inspected representation |
| Unsupported-broadening warning during answer generation | Application-only state | Runtime comparison of answer claim against scope; if retained as a reviewed decision, persist it via InspectionRecord and retain the assessed answer/source slice as an information resource with sourceText/scopeText, never an unexplained flag |
| HTTP retries, UI/cache state, execution duration | Application-only state | Logs; not authoritative evidence or new schema fields |

## 10. Identity inputs and collision risks

No local IDs or UUID mechanics are generated. Implementation must preserve the inputs below before deciding deterministic identifier construction. Equality policy is application-side and conservative, not an OWL key. sourceRecordIdentifier is a source identifier only; executionReference is a separate audit encounter reference, not a fabricated source ID.

| Class | Identity inputs that must survive | Collision / version risk |
| --- | --- | --- |
| DiseaseConceptReference | identifierAuthority, exact externalIdentifier if present, observed label, snapshot/context and source role where needed | Label-only identity, changed descriptions, multiple spellings and incompatible releases; do not merge on label or ID string alone |
| DiseaseTargetAssociation | originRole, disease/target identity, inSnapshot, operationMethod/methodVersion where known, selectionMode/filterSpecification/scope | Pair-only keys collapse source/view versions; unknown method prevents an unjustified cross-record merge |
| EvidenceOccurrence | source provider/dataset via snapshot, sourceRecordIdentifier where supplied, recordVersion or artifact version/location | Same PMID or payload text is not occurrence identity; missing source IDs require traceable artifact location, not invented upstream IDs |
| MappingRecord | mappingContext, mappingInput/reference observation, observed/candidate destination(s), sourceAuthority/process, snapshot/version, assessment scope | Same OMIM ID in different panels differs; changed destination is a new mapping observation, not silent mutation |
| SelectionContext | executionReference, queryAnchor, snapshot, selectionMode, filterSpecification, operationMethod, observedAt | Timestamp alone can collide; reruns preserve separate encounter references even if settings/results match |
| SelectionMembership | SelectionContext identity plus established EvidenceOccurrence identity | Multiple explanation paths must not generate extra occurrences or independent memberships for same context/occurrence |
| MechanismRecord | provider/source record/version or artifact location, drug/target identity, sourceText and source context | Identical drug/target pairs can describe different molecular species/actions/sources |
| ClinicalIndicationRecord | provider/source record/version/location, drug/disease identity, source context and linked report scope | Same drug/disease across versions or reports is not automatically same indication record |
| StudyRecord | Study identity through refersToStudy, source snapshot/record identifier/version, report scope and observation date | Same trial ID cannot overwrite different registry sources/dates or arm descriptions |
| DerivedStatement | executionReference, operationMethod/methodVersion, exact versioned inputs via wasDerivedFrom, relevant contexts, scope and output role | Same output text can arise from different inputs/methods; repeated runs differ even when equivalent results |
| InspectionRecord | executionReference, reviewerIdentifier/type, inspectedRecord version/slice, aboutRecord, scope/depth/material and observedAt | Same PMID/date does not identify the inspected text or judgment; separate claims may share an execution but need distinct records |

Other retained identities: SourceSnapshot preserves provider, known release/version, artifact locator/description and acquisition boundary; Publication/Study use justified authority-qualified referent IDs; HierarchyStep uses source assertion/version plus endpoints; HierarchyPath uses its exact step set and audited context; PopulationScope uses source report/arm/context and original wording; MissingnessRecord uses affected owner/field, observation context and reason assessment. No equality conclusion follows merely from similar content.

Unknown versions must be explicitly unknown. If two unversioned observations cannot be shown identical, retain their artifact/encounter boundaries and mark potential duplication unresolved. To accept the first implementation, a canonicalization/identifier specification must state how these inputs are serialized and how collisions are handled; that mechanical specification is still an owner decision, not silently chosen here. An acquisition process must provide stable execution references or an approved collision discriminator. No made-up random ID is offered as a substitute for missing identity evidence.

## 11. Version transition rules

| Change | Required result | What remains the same |
| --- | --- | --- |
| Open Targets release changes | New SourceSnapshot; new versioned occurrence, mapping/association descriptions for that snapshot; derived results tied to new inputs if recomputed | Justified Target/Drug/Publication/Study referents may remain; external concept identity may persist, local descriptions retain release context |
| Source record content changes | New versioned source description, even if provider reuses ID/version label; preserve artifact/observation boundary and disclose source-version ambiguity | Underlying referent may remain; old description is not overwritten |
| Mapping destination changes | New MappingRecord observation and any affected normalized association/view or derived result; retain old assignment/context | Original source assertion/reference may remain where justified |
| Retrieval rerun, source unchanged | New SelectionContext/executionReference and Membership encounters | Existing EvidenceOccurrence and source aggregate identity remain; do not mint duplicate evidence or regenerate source history |
| Inspection depth increases | New InspectionRecord with actual source version/material/depth and scoped outcome; preserve earlier limits | Publication/source referent persists; unchanged source description can be reused |
| Trial status changes | New dated StudyRecord and downstream review/derived results if revised | Same Study identity where registry identity is justified; old population/status report remains inspectable |

If a derived conclusion changes, produce a new DerivedStatement/InspectionRecord; do not mutate old evidence to fit the new outcome. Historical interpretations remain attached to their actual inspected snapshots. None of these rules authorizes new source acquisition during this task.

## 12. Future structural validation constraints (no shapes created)

Universally required means required for a complete instance of the specified record type, not globally required on every node. Incomplete source material may be retained with explicit limits but must not be passed off as a complete answer fixture. Conditional gaps must not be repaired with anonymous evidence or fabricated values.

| Constraint | Category | Later SHACL/data check | Ingestion/application boundary |
| --- | --- | --- | --- |
| Association has one hasTarget, hasDiseaseReference and originRole | Universally required for association record | Cardinality, role and enum checks | Missing participants block usable association, not proof of absence |
| Membership has one selectedOccurrence and inSelectionContext | Universally required for membership | Singular typed roles | Multiple paths do not duplicate occurrence |
| Mapping has contextual owner and a declared interpretation state | Universally required for mapping | mappingContext and mappingStatus | Input-only observation is not invented completed normalization |
| Reference identifier accompanied by identifierAuthority | Conditionally required when ID present | Owner/field pairing and string format | Label-only reference allowed with unresolved identity |
| Original/mapped IDs and labels present | Source-specific | Preserve supplied fields; no universal destination requirement | Zero/multiple candidates permitted; known destination with missing input is valid with explicit limits |
| Mapping context versus panel context remains explicit | Universally required when both supplied | mappingContext selects occurrence; contextRecord holds panel/source slice | Avoid unqualified global assignment by original ID |
| SourceRecordIdentifier/recordVersion | Source-specific | Required when supplied; otherwise location/version boundary and relevant missingness | Do not invent source ID or release |
| Snapshot sourceAuthority and artifactDescription | Universally required for snapshot | Nonempty source and artifact identity context | snapshotVersion may be unknown; retrieval date is not release |
| Selection run has anchor, mode, filterSpecification, executionReference, observedAt and completenessStatus | Universally required for observed retrieval | Correct types and enum; explicitly empty filter specification is allowed | Snapshot and target/datasource restrictions recoverable; incomplete pagination forbids list-wide absence |
| Path steps have child/parent reference and source context | Universally required for usable step | Singular endpoints and snapshot/locator-or-reason | Audited step semantics, not synthetic closure |
| Path is one connected acyclic chain | Conditionally required for a complete explanation | Possible custom constraint later; check typed steps | Application validates continuity/endpoints and reference compatibility; otherwise qualify, do not infer endpoints |
| Mechanism and indication participants | Universally required for usable respective record | Mechanism: hasDrug+hasTarget; indication: hasDrug+hasDiseaseReference | Validate role separation even without OWL disjointness |
| StudyRecord has one refersToStudy | Universally required for identified study description | Singular Study role | Unknown study identity requires an unresolved source slice, not an invented trial |
| PopulationScope has original sourceText and owner linkage | Conditionally required by population claim | Nonempty source text and incoming hasPopulationScope | Exact cohort mapping not invented |
| Phase/status/date | Source-specific | Attach to proper owner; validate dates at source precision | Phase not status; indication phase not every study's phase; incomplete date qualified |
| Score has source-defined context | Conditionally required when aggregateScore retained | At most one score under first-V1 policy; scoreDefinition or explicit reason | Do not interpret beyond definition; separate structured components not in first file |
| Inspection has inspectedRecord, aboutRecord, access/interpretation, actual date/execution and reviewer context | Universally required for a review result | Required roles/values or justified unavailable identity | Actual inspected source must match version; depth conditional on successful inspection |
| Inaccessible or not-attempted source has no invented positive depth | Conditionally required | Access/depth combinations | Not inspected differs from unsupported |
| Missingness has owner, expectedField, reason and contextual basis | Universally required for a meaningful MissingnessRecord | Fields plus observationContext or explained unavailable basis | Relevant gaps only; not-applicable needs rationale |
| Derived result has method, scoped inputs, executionReference, scope/completeness and explanatory result | Universally required for persisted computation | prov:wasDerivedFrom, operationMethod and remaining fields | Reproducibility needs methodVersion where defined; no source assertion substitution |
| Dependency judgment has participants and basis | Conditionally required for dependencyStatus | subjectRecord/comparatorRecord, sharedInput when claimed and rationale | Known sharing is not universal dependence; missing links never establish independence |
| Same identifier under conflicting content/version | Warning-only pending investigation | Flag potential collision | Do not auto-merge, overwrite or declare distinct underlying biology |
| Unsupported broadening / clinical truth | Not decidable by structural shapes alone | Structural evidence bundle can be checked | Application assesses claim against scope; later evaluation measures failures |

Shape exact targets, severities and source-specific field availability need an executable-policy review before their later implementation. The conceptual universal/conditional distinction is specified here; no SHACL vocabulary or graph is created.

## 13. Q01–Q07 re-walk using retained terms only

The existing required slots/A–E rubrics remain authoritative. Every route below also preserves version/source provenance and relevant MissingnessRecord/InspectionRecord context. Terms removed from the manifest are intentionally not used as persisted links.

| Question | Retained schema traversal / data | Implementability and reduction check |
| --- | --- | --- |
| Q01 | DiseaseTargetAssociation hasDiseaseReference + hasTarget PSEN1 → reportedEvidence → EvidenceOccurrence evidenceSourceType/inSnapshot/citesPublication/contextRecord. InspectionRecord aboutRecord + inspectedRecord + materialKind/inspectionDepth/interpretationOutcome. | Source typing and actual PMID/panel review boundaries remain. Source original fields are reached through reverse mappingContext → mappingInput; input unknown stays a MissingnessRecord, not a fabricated disease. No aggregate score upgrade. |
| Q02 | FTD associations → reportedEvidence → two distinct EvidenceOccurrences. Context source descriptions preserve mechanism/indication join lineage; MechanismRecord hasDrug/hasTarget and ClinicalIndicationRecord indicationStudyRecord → StudyRecord refersToStudy. DerivedStatement subjectRecord/comparatorRecord/sharedInput + dependencyStatus and prov:wasDerivedFrom → inspected source descriptions. | Shared memantine/trial basis survives. Removing Agent/Activity nodes does not remove source record, method, inspection or execution context. Do not infer the upstream join from matching drug text; retain its documented source description via contextRecord/sourceText. |
| Q03 | MAPT occurrence ← mappingContext ← MappingRecord → mappingInput Pick original and reportedDestination FTD. Membership selectedOccurrence → same occurrence; inSelectionContext → queryAnchor FTD + selectionMode direct-only. Separate HierarchyStep preserves Pick context. | OriginalDisease and hasMappingRecord shortcuts unnecessary: reverse mappingContext is sufficient. No source/normalized equivalence and no claim that hierarchy caused this direct membership. |
| Q04 | Membership inSelectionContext → mode/anchor/filter/snapshot; selectedOccurrence → reverse mappingContext → reportedDestination. justificationPath → pathStep → childReference/parentReference with source versions. | Retain observed direct/inclusive diagnostics. Derive endpoints only from a complete validated chain; compare queryAnchor to the derived endpoint. Removing stored pathStart/pathEnd does not lose source evidence. Intermediate nodes stay explicit. |
| Q05 | Two MappingRecords → mappingContext + mappingInput externalIdentifier/identifierAuthority/sourceLabel → different reportedDestination references; contextRecord retains PSEN1/panel 265 versus MAPT/panel 540; mappingStatus unresolved. | Raw inputIdentifier/inputLabel/reportedMappedIdentifier are preserved on source-scoped reference records, not dropped. Same original code enables a comparison without merging contextual references or choosing a repair. |
| Q06 | FTD association hasTarget MAPT ← hasTarget MechanismRecord → hasDrug zagotenemab ← hasDrug ClinicalIndicationRecord → hasDiseaseReference. Context source-list description has inSnapshot/completenessStatus/scopeText; inspections preserve cited publication depth. | Generic participant names are safe because typed owners preserve relation meaning. The lecanemab/APP control retains sourceText molecular limits. No exact FTD indication in inspected complete list is a bounded query result, not negative biology. Regulatory product-label review remains absent; removed approval fields do not create positive approval capability. |
| Q07 | Gosuranemab indication → indicationStudyRecord → StudyRecord refersToStudy nct03658135, trialPhaseText/trialStatusText/statusDate, hasPopulationScope → sourceText/sourceLabel. Separate MechanismRecord citesPublication/contextRecord; InspectionRecord qualifies source review. | Population, status and healthy-participant mechanism provenance remain separate. Keeping Publication, Study, StudyRecord and PopulationScope avoids collapsing source roles. No cohort ontology mapping or efficacy conclusion. |

No question requires a removed persisted shortcut. Fields retained after challenge: PopulationScope (multiple original cohort restrictions), StudyRecord (dated descriptions), InspectionRecord (actual review depth), sharedInput plus dependencyStatus (qualified dependency), and explicit HierarchyPath grouping. These were not merged because qualification/identity would be lost or equivalent hidden structure would be necessary. Every explanation uses declared fields; raw sourceText preserves original wording but does not substitute for required typed clinical/mapping links.

The diagnostic date/count observations for Q04 remain source descriptions with sourceText/scopeText and sourceLocator; membership comparisons are recomputed only for the retained explicit diagnostic inputs. This does not authorize reproducing historical complete result counts from a partial fixture or inventing a count property. For Q01/Q02, source-component/sample completeness likewise comes from scoped source descriptions, not the absence of a link.

## 14. R1–R14 implementation crosswalk

No requirement is dropped. Frozen wording is preserved verbatim below. O = OWL declaration/explicit type role; V = later validation; T = ingestion/transformation; A = application verification; E = experimental evaluation. The absence of substantive OWL axioms makes V/T/A boundaries especially important, not optional.

| ID | Frozen requirement | Retained schema | Responsibility / acceptance boundary |
| --- | --- | --- | --- |
| R1 | Association separately from individual evidence. | DiseaseTargetAssociation / EvidenceOccurrence; reportedEvidence versus occurrence inputs of project grouping | O distinct types; V origin/participant roles; T preserves source membership; A avoids causal upgrade; E trace fidelity. |
| R2 | Original/source disease identity separately from normalized disease identity. | DiseaseConceptReference; MappingRecord mappingInput/reportedDestination | T raw identifiers/labels/version; V correct role references; A no equivalence; E scope fidelity. |
| R3 | Mapping context and unresolved ambiguity. | MappingRecord mappingContext, contextRecord, candidateDestination, mappingStatus | V contextual fields; T preserves differing assignments; A unresolved interpretation; E ambiguity handling. |
| R4 | Direct evidence separately from descendant-derived/propagated evidence. | SelectionMembership, SelectionContext, HierarchyPath/Step; inclusionKind and justificationPath | V membership/path structure; A audited directness/path comparison; E propagation accuracy. |
| R5 | Query-time descendant inclusion separately from upstream source normalization. | MappingRecord separate from selection context and membership; operationMethod | T source assignment not project normalization; A separates query inclusion from upstream process; E operation classification. |
| R6 | Evidence provenance at claim/association level. | SourceSnapshot, inSnapshot/contextRecord, prov:wasDerivedFrom; record identity metadata | V source/version-or-reason; T no fabricated activities; A inspect claim lineage; E attribution completeness. |
| R7 | Publication/study/source locator where available. | Publication/Study/StudyRecord; citesPublication/refersToStudy/sourceLocator | T attribution scope; V locator roles; A locator does not prove support; E source tracing. |
| R8 | Inspection/review depth where relevant. | InspectionRecord: inspectedRecord/aboutRecord, depth/material/access/reviewer/date | V consistent fields; A actual review extent; E depth fidelity. |
| R9 | Missing provenance/information explicitly rather than silently repaired. | MissingnessRecord: aboutRecord/expectedField/missingnessReason/observationContext | V relevant field/reason; T no silent repair; A qualification; E missingness treatment. |
| R10 | Target–drug mechanism separately from disease indication. | MechanismRecord versus ClinicalIndicationRecord; hasDrug/hasTarget versus hasDrug/hasDiseaseReference | O distinct types; V role-specific fields; A reject composition; E unsupported clinical claims. |
| R11 | Clinical indication separately from trial population and trial status. | ClinicalIndicationRecord, Study/StudyRecord, PopulationScope; report links, phase/status/date/sourceText | V conditional role/date checks; T original context preserved; A limits benefit/approval/phase interpretation; E qualification accuracy. |
| R12 | Derived comparisons/intersections separately from source assertions. | DerivedStatement or project grouping, originRole, prov:wasDerivedFrom, method/settings/scope | V inputs/context; T reproducible comparisons; A source versus project distinction; E derivation fidelity. |
| R13 | Shared/dependent evidence so multiple records are not automatically independent support. | Shared Publication/Study references; DerivedStatement participants/sharedInput/dependencyStatus | T deduplicate justified occurrence identity; V assessment basis; A no automatic independence; E dependency sensitivity. |
| R14 | Scope qualification and abstention conditions required by the core questions. | InspectionRecord outcomes/rationale/limitations, contextual missingness and scoped derived results | V required qualification context; A actual support/abstention decision; E supported completion and excess abstention. |

## 15. Exact first-ontology-file plan (not executed)

The semantic inventory is approved as the current V1 implementation basis; namespace/serialization mechanics and implementation authorization remain outstanding.

**Local class declarations (20):** SourceSnapshot, DiseaseConceptReference, Target, Drug, DiseaseTargetAssociation, EvidenceOccurrence, MappingRecord, SelectionContext, SelectionMembership, HierarchyStep, HierarchyPath, Publication, Study, StudyRecord, MechanismRecord, ClinicalIndicationRecord, PopulationScope, DerivedStatement, InspectionRecord, MissingnessRecord.

**Object properties:** exactly the section 4 object manifest: 27 local names plus referenced prov:wasDerivedFrom (28 usable relations). No selectedEvidence, originalDisease, hasMappingRecord, pathStart, pathEnd, resultTarget or new inverse property declaration. Derivation/query rules are documented application obligations, not ontology axioms.

**Datatype properties:** exactly the section 4 datatype manifest (39 local names). Twelve are enum-like string fields. sourceText consolidates actual source wording on the appropriately scoped typed description; it must not conceal required structured participants. executionReference is an audit identity input, not a selected UUID scheme.

**Controlled vocabularies:** no individuals/concepts and no enum classes in the first file. Section 5 literal value lists are the proposed validation contract, documented in term comments or accompanying documentation. Later SHACL enforces values; OWL does not enumerate them.

**External vocabulary:** reference prov:Entity and prov:wasDerivedFrom only from PROV. Use standard RDF/OWL declaration and annotation machinery and XSD/string/date/decimal literal datatypes as needed for serialization. No MONDO, PROV-O or SKOS imports. MONDO identifiers occur in future reference records, not disease class axioms in the ontology file.

**Axioms:** class/property declarations only; no nontrivial logical axioms. Descriptive labels/comments may record approved meanings, conditional constraints and forbidden interpretations, but are not substitute logical constraints. The first file contains schema declarations and documentation, not KG fixtures, review instances or provenance data. External-term reference does not silently enable external inference closure.

**Intentionally absent:** wider biomedical vocabulary, regulatory ontology, phenotype/pathway extension, source assertions as biomedical truth, equality/mapping equivalence, automatic closure, relation-composition treatment rules, shape graph, query suite, records/instances, executable identifier generator, reasoner/store configuration and software dependencies. No new source acquisition or clinical claims.

## 16. Acceptance specification for the later implementation

These tests are planned, not written or run. Acceptance requires all applicable gates; mere syntactic success is insufficient.

| Gate | Future acceptance evidence |
| --- | --- |
| Authorized manifest | Owner-approved inventory and namespace/encoding policy; actual declared terms match it, with no undeclared shortcut fields in fixtures |
| RDF parses | Parser accepts schema and separately authorized fixtures; serializer round-trip preserves intended terms, datatypes and literals |
| OWL consistency, where applicable | Chosen reasoner reports no inconsistency for the declared entailment regime and fixtures; report engine/profile/import policy. With declarations-only semantics, this is a weak check, not biomedical validation |
| No forbidden entailments | Inspect axioms/import closure and test representative prohibited inferences against positive control inputs; also test application transformations for normalization equivalence, mechanism→indication, citation→support and independence upgrades |
| Seven fixtures representable | Q01–Q07 required slots and A–E boundaries represented by the retained manifest; no hidden field, external-memory step or fabricated missing source data |
| R1–R14 coverage | Every row of section 14 has an explicit schema/validation/application obligation and corresponding later check or documented deferred execution responsibility |
| Identifier/version reproducibility | Approved canonical input serialization and collision policy; reruns preserve source occurrence identity, concurrent encounters differ, changed releases/content create versioned descriptions. Unknown identity remains uncertain |
| Provenance round-trip | Export/reload preserves source snapshots, raw labels/IDs, source-versus-project role, mappings, query membership, inspection limits, shared input references and missingness reasons |
| Query-time replacement fidelity | Reverse mapping lookup recovers original/mapped fields; path endpoints derived only from valid chain; selected evidence recovered from direct occurrence input links; target intersections reproduce from pinned inputs |
| Structural expressibility | Section 12 constraints can be expressed by the chosen later SHACL plus ingestion/application checks without changing entity meaning or adding undeclared semantic fields; actual shapes remain a separate implementation task |
| Required positive cases | Correct retrieval of distinct normalized/source scopes, a complete audited path and shared study provenance; an always-abstain system cannot pass solely by avoiding errors |
| Relevant negative cases | Missing path step, mismatched snapshot, unresolved mapping, inaccessible text, partial list, reused trial and source-record-ID collision remain visible and appropriately qualified |
| Preservation of missingness and review | Known value plus unresolved validity is representable; full abstract not full paper; rerun/greater-depth review does not overwrite earlier limits |
| Original data scope | No downstream claim exceeds inspected bundle; Q01–Q07 remain design fixtures, not held-out experimental evidence; no domain-expert adjudication claimed |

The identifier mechanics, schema namespace and validation policy approval are remaining **pre-implementation blockers**, not failed science or permission to choose them silently. No test is accepted merely because this document describes it. There is no implemented ontology whose consistency, parsing, performance or graph advantage can be claimed.

## 17. Checkpoint 3 approval and remaining implementation gates

The following requests are retained as the investigation record. Checkpoint 3 approves the minimized implementation basis and direction in items 1–6; the remaining mechanics in item 7 and explicit implementation authorization remain outstanding. Manifest revisions require explicit fixture-implementation evidence.

Original decision requests:

1. Approve/revise the 20/28/39 manifest and the item-by-item dispositions, including only one local class removal.
2. Approve one DiseaseTargetAssociation with literal originRole, and source-reported membership distinct from query-derived project selected membership. No extra subclasses or dual typing required.
3. Approve source-scoped disease references as the canonical storage of original/mapped IDs and labels, with reverse mapping navigation and input-only observations when appropriate.
4. Approve literal controlled values and the very small PROV subset; accept explicit execution/reviewer metadata on results instead of separate Activity/Agent nodes.
5. Approve the sourceText consolidations, with structured clinical/mapping links retained and no positive regulatory capability; approve one source-defined score per association in first V1.
6. Approve declarations-only OWL semantics and structural/application enforcement; no domain/range/disjointness exceptions proposed.
7. Before executable implementation, settle namespace, deterministic ID serialization/collision policy, exact expectedField catalogue, enum values, source acquisition boundaries and validation severities. No identifier allocation or software selection is made here.

**Proposed next task:** after separate authorization, resolve the remaining implementation mechanics against the approved first-file manifest and acceptance specification. Ontology implementation should begin only when the owner explicitly authorizes it and those gates are resolved; do not repeat broad schema expansion. If owner approval supplies the remaining choices directly, a separately authorized first schema implementation can follow without another open-ended design investigation.

## 18. Review basis and task limits

The approved contract and frozen question/rubric/source documents supply the biomedical examples and requirements. Primary technical checks: [PROV-O](https://www.w3.org/TR/prov-o/#wasDerivedFrom) for informational derivation and [OWL 2 Primer](https://www.w3.org/TR/owl2-primer/) for typing/open-world distinctions. The smaller provenance subset and declarations-only design are project recommendations, not external source prescriptions.

This task performs documentation-level minimization and traceability review only. It does not execute the planned acceptance tests, import any vocabulary, mint identifiers, create RDF/OWL/SHACL/instances, install ontology software, configure a database or write production queries. The broader `docs/m1_schema_design.md` stays intact, and all previous approved history remains unchanged. Checkpoint 3 authorizes a local commit of this document and the schema-design investigation only. No push or ontology implementation is authorized. Graph advantage remains **NOT YET DEMONSTRATED**.

## 19. Approved implementation mechanics — initial audit-derived fixture scope

Following Checkpoint 3 at `229540c`, the owner explicitly approved the corrected [M1 Task 005 implementation mechanics](m1_implementation_mechanics.md#9-owner-approval-record-and-next-step) on 2026-09-22 (Asia/Kolkata). **G01–G06 are APPROVED** for the initial M1 audit-derived fixture scope: namespace/prefixes; deterministic identity/serialization/revisions/collisions; exact enumerations; finite non-duplicating missingness; audit-derived fixtures first; and validation severity, precedence and automatic/controlled-fixture/manual responsibilities.

This status update supersedes the outstanding-mechanics and proposed-next-task wording in sections 15–17, which remains intact as the Checkpoint 3 investigation history. The 20/28/39 manifest, Q01–Q07, R1–R14 and conceptual model are unchanged. Historical upstream availability, artifact permissions and live-acquisition projections remain deferred and are not resolved by this approval.

The present instruction authorizes only approval reconciliation and a local documentation checkpoint commit. Ontology implementation and fixture creation still require an explicit next-task authorization; live acquisition requires separate authorization. Do not push. The next bounded proposal follows the declarations-only first-file plan in section 15, with applicable schema checks from section 16; broader fixture, identity execution and application checks remain later work.
