# M1 Task 003 — schema design proposal and decision crosswalk

**CHECKPOINT 3 APPROVED INVESTIGATION — BROADER CANDIDATE CATALOGUE; NOT IMPLEMENTED**

Baseline: `00eb97b Define M1 conceptual model contract`. Approved direction: Alternative B. M0 remains frozen. This proposal translates the [approved conceptual contract](m1_conceptual_model_contract.md) (abbreviated **C§** below) into candidate schema terms. Names are local names for review, not an ontology namespace, declarations or instances. The owner approved the investigation and architectural direction at M1 Checkpoint 3. The broader 21/56/44 catalogue and its original recommendations below remain investigation history; the approved implementation basis is the minimized 20/28/39 manifest in [implementation readiness](m1_implementation_readiness.md). Where they differ, that minimized specification governs. Ontology implementation is not authorized.

Authority: [Q01–Q07 / R1–R14](competency_questions.md), [scope](project_scope.md), and [modelling comparison](m1_modelling_options.md). All clinical examples reuse the frozen design material; no biomedical source acquisition or new verification is claimed. Only AD MONDO:0004975 and FTD MONDO:0017276 are anchors, with the already audited narrower context. No automatic descendant closure.

## 1. Design summary and notation

Recommend a small typed-record schema, local disease references, one association class with an explicit origin role, identifiable evidence/mapping/selection records, qualified clinical descriptions, and sparse contextual missingness. Distinguish an underlying study/publication from its versioned source description. Use a limited provenance vocabulary alongside local domain-specific relations. Do not add a universal subject–predicate–object claim ontology.

Every term below has a purpose, R/Q justification and C§ reference. Shared terms are reused rather than multiplied into disease-, target- and drug-specific versions. **Record** means a versioned information description, not the biological thing it describes. **ControlledValue** below is table notation for a future governed value concept, not an additional class recommendation; vocabulary member IRIs and code lists remain unselected. Likewise **Resource** is table shorthand for an identified resource, not a local class. Source/target columns are usage signatures, not OWL domain/range axioms.

All candidate domain relations are explicitly recorded or produced by a documented transformation. None is a biomedical inference. Reverse navigation in the tables means a query can traverse an edge backwards; it does not require another property or an OWL inverse axiom.

## 2. Disease-reference alternatives

| Option | OWL meaning and risks | Querying, provenance and source fidelity | Pick / OMIM ambiguity fit | Recommendation |
| --- | --- | --- | --- | --- |
| A. Use MONDO IRIs directly as application resources/individuals | Class IRIs used as individuals introduce metamodeling/punning choices. In OWL 2 DL, class and individual interpretations are separate; class hierarchy does not automatically operate on individual links. | Concise identifiers/joins, but labels and source-release context still need qualified records. Unresolved source labels require a separate representation. | Possible with mapping records, but encourages accidental source/normalized collapse if a single IRI slot is used. | Viable, but not preferred for this learning-focused, provenance-sensitive V1. |
| B. Local DiseaseConceptReference records | Local individuals describe an external/source concept reference; they are not instances of AD/FTD and are not equivalent to MONDO classes. External identifiers/IRIs are identifier values, not OWL identity axioms. | One extra join; explicit authority, source wording and snapshot. No imported disease inference. Unresolved label-only references remain possible with identity limitations. | Original Pick reference and mapped FTD reference remain distinct; OMIM:600274 record-local observations coexist. | **Recommended candidate.** |
| C. Local application disease representation with alignment to external concepts | If local classes duplicate MONDO, equivalence/subclass commitments require justification. If local concept individuals merely point outward, this approaches B. | Additional local taxonomy/alignment maintenance; richer alignment possible but no frozen CQ requires a replacement taxonomy. | Can preserve ambiguity via qualified alignment records; unqualified alignment predicates risk overstatement. | Defer local medical taxonomy; application records still useful as B. |

Under B, `externalIdentifier` retains an authority-qualified identifier; optional `externalIRI` preserves an absolute reference as a URI value. This is a reference, not a clinical equivalence assertion. `sourceLabel` retains observed wording. A `DiseaseConceptReference` identifies a source-scoped reference description: authority + identifier (if present) + snapshot/context. Reuse within the same justified context is allowed; equal strings across snapshots are comparison inputs, not automatic sameAs. Label-only references have unresolved identity. Concept-level grouping across descriptions is an explicit later resolution operation, not an extra V1 concept taxonomy.

The approved anchors are validated by their authoritative identifiers in the relevant reference records. They do not require an Anchor subclass. Source label variants belong to their own observations where contexts differ. Association/query roles point to reference records; mapping records preserve original assignments independently. Pick MONDO:0008243 context does not overwrite original OMIM:172700 or mapped FTD MONDO:0017276. OMIM:600274 assignments retain panel/gene context and their distinct observed destinations.

[OWL 2 Primer](https://www.w3.org/TR/owl2-primer/) supplies the class/individual distinction; choosing B is project design analysis. No MONDO import or equality bridge is proposed.

## 3. Candidate classes and deliberate omissions

“Keep” means candidate V1 capability, not mandatory data for every occurrence. A source role can be unpopulated if unavailable and documented. Required Q/R references identify why the class exists; they do not authorize broader acquisition.

| Candidate | Decision and meaning; why a node | Trace | Over-modelling guard |
| --- | --- | --- | --- |
| Record | Keep as minimal superclass for versioned descriptions and results; common provenance/locator fields | R6–R9; Q01–07; C§1–3,6 | No universal proposition model or arbitrary predicate slot |
| DiseaseConceptReference | Keep; source-scoped description of a disease reference, not disease/patient instance | R2–R5; Q03–05; C§4 | No local disease taxonomy |
| Target | Keep; identified source-indexed target referent; source qualifiers retained in records | R1,R10; Q01–06; C§2–3 | Gene ID does not identify every molecular form |
| Drug | Keep; source-identified drug referent needed for shared mechanisms/indications | R10–R11,R13; Q02,06–07; C§2,9 | No automatic product/formulation identity |
| DiseaseTargetAssociation | Keep, under Record; scoped aggregate or project grouping, not causal edge | R1,R6,R12; Q01–06; C§3,5 | One class with controlled origin role, not two disconnected schemas |
| EvidenceOccurrence | Keep, under Record; source record version and attributed content | R1–R9,R13; Q01–05; C§3,6 | Query encounters do not duplicate it |
| MappingRecord | Keep, under Record; one contextual assignment/assessment record | R2–R3,R5; Q03–05; C§7 | Observed assignments versus candidates stay distinct; no global mapping table |
| SelectionContext | Keep, under Record; run-specific settings/result-description, not evidence | R4–R5,R12; Q01–06; C§8 | One per execution/view; repeated specification may be compared without a separate template class |
| SelectionMembership | Keep, under Record; occurrence in a context with inclusion explanations | R4–R5,R13; Q02–04; C§8 | Multiple paths do not multiply occurrences |
| HierarchyStep | Keep, under Record; one source-attributed child/parent assertion | R4–R6; Q03–05; C§2,8 | Only audited steps; no complete hierarchy import |
| HierarchyPath | Keep, under Record; explicit bounded chain used as explanation, with source steps | R4–R5,R12; Q04; C§8,10 | A simple directed chain, not arbitrary graph/path machinery |
| Publication | Keep; identified publication referent shared by records | R7,R13; Q01–03,06–07; C§6 | Not interchangeable with study or citation |
| Study | Keep; underlying investigation/trial referent | R7,R11,R13; Q02,07; C§9,13 | Trial is a candidate study-kind value, not another class yet |
| Trial | Merge into Study with `studyKind` | R11; Q02,07; C§9 | No entailment needs Trial subclass |
| StudyRecord | Keep, under Record; dated source description of a Study | R7–R8,R11; Q02,07; C§1,9 | Necessary to avoid putting mutable status/population on timeless study identity |
| MechanismRecord | Keep, under Record; attributed drug–target mechanism statement | R10,R13; Q02,06–07; C§9 | Preserve molecular detail as source text until separate modelling justified |
| ClinicalIndicationRecord | Keep, under Record; source drug–disease development/indication entry | R10–R11; Q02,06–07; C§9 | Does not assert efficacy or unrestricted approval |
| PopulationScope | Keep, under Record; study/report/arm-local population description | R11,R14; Q07; C§9 | Original text and cohort context, no invented disease mapping |
| DerivedStatement | Keep, under Record; project output with inputs/method/scope | R12–R14; Q01–07; C§10 | Typed operation values rather than universal propositions |
| InspectionRecord | Keep, under Record; claim-scoped result of inspecting a particular source description | R8–R9,R14; Q01–07; C§11 | Activity separate; separate outcomes may share one activity |
| MissingnessRecord | Keep sparsely, under Record; relevant absent/unresolved slot with reason/context | R9,R14; Q01,05–07; C§12 | Not a node for every unused optional field |
| DependencyAssessment | Merge into DerivedStatement with dependency operation/outcome | R12–R13; Q02; C§13 | No independent evidence scoring subsystem |
| SourceSnapshot / DatasetRelease | Keep SourceSnapshot; merge DatasetRelease as known release metadata | R6–R9; Q01–07; C§3 | Snapshot identity is not just a version string or timestamp |
| SourceAssertion / ProvenanceRecord | No mandatory separate classes; attributed Record slice when needed, shared provenance relations | R6–R7,R12–R13; Q01–07; C§2,6 | A record slice may preserve panel-wide attribution without a claim universe |
| RegulatoryApproval | No standalone V1 class; qualified source Record only if required to retain approval-labelled metadata | R10–R11,R14; Q06–07; C§9 | No regulatory knowledge expansion or unrestricted approval conclusion |

Selected external provenance types: `prov:Entity` for descriptions/artifacts, `prov:Activity` for executed operations, `prov:Agent` for attributed actors/process agents. These are vocabulary reuse candidates, not imports. DiseaseConceptReference and the named description/result classes are candidate Record subclasses; Target, Drug, Publication and Study are referents, not Record subclasses. SourceSnapshot is an artifact description. No broad disjointness between all referents and records is needed for V1.

## 4. Association and evidence schema

### Association

Prefer **one DiseaseTargetAssociation class with required originRole**, distinguishing source aggregate from project grouping. Both share participant/view structure; separate unrelated classes duplicate queries. Subclasses could help classification, but add little before source roles/validation are settled. A project grouping may also be typed DerivedStatement to require derivation fields; a source aggregate must not be so typed merely because its provider performed an upstream calculation.

Candidate fields: `associationDisease`, `associationTarget`, `inSnapshot`, `originRole`, `aggregationMethod`, `selectionMode`, `filterSpecification`, `scopeText`, optional `aggregateScore`/`scoreDefinition`/`scoreComponent`. A project grouping additionally has `inputRecord`, `operationMethod`, `inSelectionContext` and recorded generation activity. A source aggregate preserves its source snapshot and aggregate definition; a local sampling query does not change it.

`reportedEvidence` means the platform reports a constituent connection. `selectedEvidence` means a project grouping includes an occurrence. Neither means independently adjudicated support. Partial samples cannot be declared full aggregate membership. `completenessStatus` and limitations qualify what is accessible. A source aggregate with inaccessible constituents is permitted; an empty project result belongs in DerivedStatement rather than fabricated positive association membership. Score metadata is source-specific and optional; multiple independently scored components require separately qualified Record descriptions, not an ambiguous list of numbers.

### Evidence

EvidenceOccurrence carries `sourceRecordIdentifier` if supplied, `inSnapshot`, original fields as reported, `evidenceSourceType`, target, mapping records, source locators and known references. Normalized identity is canonical through the MappingRecord's reported destination, not a second independently maintained disease field. A platform normalized disease can be recorded even when the original is absent; the MappingRecord then states that the assignment process/input is not fully known.

SelectionMembership points to EvidenceOccurrence; reverse traversal retrieves all encounters without duplicating evidence. Known shared publications/studies are ordinary reference links; dependency conclusions live in DerivedStatement. InspectionRecord points to the relevant evidence/source record or finer source slice. A panel record can be a generic Record with its own locator and references, linked by `contextRecord`; panel-wide citations are not copied as individually proven occurrence citations.

## 5. Mapping schema and SKOS boundary

MappingRecord links via `mappingContext` to the source occurrence/record; `mappingInput` to an original DiseaseConceptReference where possible; `reportedDestination` to a reported normalized reference; `candidateDestination` to possible alternatives. It also retains `inputIdentifier`, `inputLabel`, `reportedMappedIdentifier`, `mappingAuthority`, `mappingProcess`, `mappingStatus`, snapshot and scope/context. Missing source identity does not prevent preserving a known destination. Multiple candidates are allowed; alternative observed assignments in different panel/gene contexts are separate records.

Observed versus candidate is expressed by different relations, not inferred from a single ambiguous status. Unresolved validity may coexist with a reported destination. Candidate lists are not OWL alternatives that force a choice. Unknown source algorithms or snapshots are not reconstructed.

SKOS mapping properties describe semantic relationships between concepts, not the provenance and uncertainty of an observed platform assignment. `skos:exactMatch` carries stronger semantics (including symmetry/transitivity) than this task warrants; `closeMatch` also asserts a semantic mapping and is not a synonym for unresolved normalization. `broadMatch`/`narrowMatch` must not be inferred just because a platform normalized a narrow label to a broad anchor. These properties could later express separately justified concept alignments, but **none is proposed for ordinary MappingRecord outputs**. [SKOS Reference, mapping properties](https://www.w3.org/TR/skos-reference/#mapping).

## 6. Selection and explicit paths

Keep both SelectionContext and SelectionMembership. Context records query anchor, mode, filters, source snapshot, retrieval activity/date, result extent/completeness and operation method. Membership records selected occurrence, context and inclusion kind: exact normalized-anchor membership or descendant-selected membership. An inclusive result may contain direct matches; query mode alone does not classify each member.

HierarchyPath has `pathStart`, `pathEnd`, `pathStep`; HierarchyStep has `childReference`, `parentReference`, source/snapshot and locator. V1 paths must form one finite connected, directed, nonbranching chain between the declared endpoints. Ordering is reconstructed from step endpoints, not an unordered bag interpreted as a path. Alternative paths use separate HierarchyPath records. Source step identity remains shared. A future structural/application check must verify continuity, absence of cycles, endpoints, version compatibility and completeness; do not create a property-chain entailment or transitive closure.

Membership `justificationPath` is an inspected explanation, not a claim about undocumented source execution. A context with project-traversal operation remains distinct from source retrieval. An unavailable justification can be marked incomplete without discarding the observed membership. Per-run identity belongs to context; semantic occurrence identity remains source record/version. No record count can treat duplicate query paths as independent evidence.

## 7. Provenance options and recommendation

| Option | Fit | Cost/risk |
| --- | --- | --- |
| Lightweight local only | Short domain-specific source/snapshot/activity relations | Private lineage semantics may expand unnecessarily |
| Selected PROV-O only | Standard generation, use, attribution and derivation | Does not express mapping validity, query selection, evidence support or missingness by itself |
| Hybrid | Local record/clinical/selection semantics plus a small PROV subset | Requires disciplined separation between information entities and activities; preferred candidate |

Recommend hybrid: `prov:Entity`, `prov:Activity`, `prov:Agent`; `prov:wasGeneratedBy`, `prov:used`, `prov:wasAssociatedWith`, `prov:wasDerivedFrom`; optional activity timestamps from PROV. `SourceSnapshot` identifies source artifact/version; its source authority/locator can be values rather than a new platform class. Record identity is retained on each source record. Activity method/version distinguishes retrieval, project computation and inspection. Mapping process metadata does not manufacture an upstream Activity when execution details are unknown.

InspectionRecord is the result entity; inspection execution is an Activity. SelectionContext describes a retrieval result/run; retrieval execution is an Activity. An imported source record's retrieval is not its original source generation: generation provenance must identify the local representation when used, without claiming the source authored it during retrieval. `inSnapshot` preserves original source context. Re-retrieving an established EvidenceOccurrence creates another SelectionContext/membership, not another generation of that occurrence. If a local representation is revised, preserve its version boundary rather than assigning incompatible generation events to one immutable record. `wasDerivedFrom` is informational lineage, not evidential support or independence. Do not use `prov:Association` for disease–target associations. No full PROV-O import; external terms alone do not automatically load their axioms. [PROV-O](https://www.w3.org/TR/prov-o/).

## 8. Clinical and inspection records

MechanismRecord links Drug and Target with source mechanism text, molecular context and references. ClinicalIndicationRecord links Drug and DiseaseConceptReference, with specific supporting StudyRecords where reported. Study is a reusable referent; StudyRecord is the dated source description with phase text, trial status, status date, population and design wording. Phase on an indication retains its source's indication-level meaning; it must not be copied to every trial. PopulationScope retains original cohort/arm text without invented mappings.

Approval-labelled metadata remains scoped to its indication/source description. If retained, jurisdiction, authority, product scope, indication/population scope and effective/as-of context are fields or related source records; missing qualifiers block an unrestricted current approval answer. No standalone regulatory ontology or new review of labels is authorized.

InspectionRecord links `inspectedRecord` and `aboutRecord`, preserving material type, depth, access outcome, interpretation outcome, reviewed scope and rationale. A single inspection Activity can generate several claim-specific InspectionRecords; interpretation must not become a publication-global truth label. Minimal attribution uses the activity's agent and reviewer-type value. Metadata, abstract, selected passages, full text and source-page inspection remain distinguishable. Access failure need not have an inspection depth.

Keep stable evidence-bearing inspection facts, source versions, limitations and outcomes in the eventual RDF. Keep transient HTTP retries, credentials, UI state and verbose debug logs in application logs; a log pointer alone cannot replace required review provenance. Log technology is unselected. No technical review is labelled biomedical expert adjudication.

## 9. Missingness and dependency design

| Missingness option | R9/R14 suitability | Decision |
| --- | --- | --- |
| A. Explicit MissingnessRecord | Preserves affected record, field, reason, observation context and changing assessments | Recommended **sparsely**, only for required/interpretation-relevant gaps |
| B. Controlled reason attached to expected field | Compact if each field has a companion reason property, but proliferates properties; direct annotation of a predicate loses record/observation context | Use reason concepts inside A; avoid per-field companion properties and predicate-global reasons |
| C. Application-only | Easy initially, but graph exports lose reasons needed for qualification/abstention | Logs may supplement; insufficient as sole representation |

MissingnessRecord links `aboutRecord` to the affected information owner (Record, SourceSnapshot or other identified resource), optional `observationContext`, and `missingnessReason`; `expectedField` is a governed field token value, not a property IRI used as an individual. Candidate reasons: source omission, not retrieved, inaccessible, not applicable, not inspected, unresolved, reason unknown. Actual code spellings remain open. No missingness record for every irrelevant optional field. An unknown mapping validity can coexist with a known reported destination; expectedField must identify validity, not falsely say destination absent.

Duplicate occurrences are detected conservatively by established source record/version identity during ingestion. Preserve retrieval contexts. Same-publication and shared-study relationships arise from explicit references, not a duplicate/independence classification. Known or possible dependency uses DerivedStatement with operation, subject/comparator records, common input, dependency outcome, basis and review provenance. Different sources may be recorded without declaring independence. An independence conclusion is permitted only as a qualified reviewed result with stated basis, never inferred from missing links or distinct IDs. No binary independent flag or numerical independence score.

## 10. Derived outputs and identity boundaries

DerivedStatement covers sampled intersections, mapping comparisons, dependency findings and inclusion/exclusion findings. It links inputs, selection contexts and optionally subject/comparator/common-input records. It retains operation method/version, scope, output summary, completeness and limitations plus generation activity. Structured participants preserve queryability; summary text is explanation, not the sole evidence for a comparison.

A sampled intersection links `resultTarget` for each returned target. No resultTarget plus a complete bounded computation can represent an empty intersection; no invented positive association. Mapping comparison links its MappingRecord inputs; inclusion/exclusion comparison links the inspected contexts and subject occurrence. Exclusion is a result of a complete declared comparison, not a universal negative assertion. A dependency finding links both occurrences and its shared source basis. All remain project-derived.

Identity follows C§3: associations depend on origin, participant references, source/snapshot, aggregation and view; occurrences on provider/dataset record and version; contexts on execution; memberships on occurrence plus context; mapping on source occurrence/context and assignment observation; inspections/derivations on their operation and inputs. SourceSnapshot identity includes source and artifact identity, not release string alone. Retrieval dates do not invent releases. No OWL keys or UUID policy. Cross-snapshot comparisons resolve authority-qualified references explicitly; separate local descriptions are not automatically equal.

## 11. Candidate object-property catalogue

Each row proposes one property. **Nav:** Y = reverse query useful; N = no special reverse need. **Mode:** A = explicitly recorded from source/context; D = explicitly computed with provenance; P = reused PROV relation. No row requests automatic biomedical inference. Shared Record includes candidate description subclasses. Trace combines R, Q and conceptual-contract section.

| Name | Source → target | Meaning | Nav / mode | Trace |
| --- | --- | --- | --- | --- |
| inSnapshot | Record → SourceSnapshot | Source artifact/context describing this record | Y / A | R6–9; Q01–07; C§3,6 |
| contextRecord | Record → Record | Source panel/passage/context; not automatically support or derivation | Y / A | R3,6–7; Q01,03,05; C§6–7 |
| associationDisease | DiseaseTargetAssociation → DiseaseConceptReference | Normalized anchor or explicit diagnostic scope | Y / A,D | R1–2,4; Q01–06; C§4–5 |
| associationTarget | DiseaseTargetAssociation → Target | Target of this scoped association | Y / A,D | R1; Q01–06; C§5 |
| reportedEvidence | DiseaseTargetAssociation → EvidenceOccurrence | Source-reported constituent, not independent support | Y / A | R1,6,13; Q01–02; C§5–6 |
| selectedEvidence | DiseaseTargetAssociation → EvidenceOccurrence | Constituent of a project grouping | Y / D | R1,12; Q01–04; C§5,10 |
| originalDisease | EvidenceOccurrence → DiseaseConceptReference | Original source reference where supplied | Y / A | R2; Q01,03,05; C§4,6 |
| evidenceTarget | EvidenceOccurrence → Target | Source-indexed target of the occurrence | Y / A | R1,6; Q01–05; C§6 |
| hasMappingRecord | EvidenceOccurrence → MappingRecord | Contextual assignment description | Y / A | R2–3,5; Q03–05; C§7 |
| mappingContext | MappingRecord → Record | Specific occurrence/panel context of assignment | Y / A | R3,6; Q03,05; C§7 |
| mappingInput | MappingRecord → DiseaseConceptReference | Original reference when identifiable | Y / A | R2–3; Q03,05; C§7 |
| reportedDestination | MappingRecord → DiseaseConceptReference | Observed platform destination | Y / A | R2–3,5; Q03–05; C§7 |
| candidateDestination | MappingRecord → DiseaseConceptReference | Possible mapping, not asserted assignment/equivalence | Y / A,D | R3; Q05; C§7 |
| queryAnchor | SelectionContext → DiseaseConceptReference | Requested disease in this context | Y / A | R4–5; Q01–05; C§8 |
| selectedOccurrence | SelectionMembership → EvidenceOccurrence | Occurrence encountered in the result | Y / A | R4,13; Q02–04; C§8 |
| inSelectionContext | SelectionMembership or DerivedStatement or DiseaseTargetAssociation → SelectionContext | Run/view for membership or scoped comparison/grouping | Y / A,D | R4–5,12; Q01–06; C§8,10 |
| justificationPath | SelectionMembership → HierarchyPath | Inspected path explanation, not hidden source execution | Y / A,D | R4–5; Q04; C§8 |
| pathStep | HierarchyPath → HierarchyStep | Steps forming one validated directed chain | Y / A,D | R4–6; Q04; C§8 |
| pathStart | HierarchyPath → DiseaseConceptReference | Narrower normalized endpoint | N / A,D | R4; Q04; C§8 |
| pathEnd | HierarchyPath → DiseaseConceptReference | Anchor endpoint | N / A,D | R4; Q04; C§8 |
| childReference | HierarchyStep → DiseaseConceptReference | Source child concept reference | Y / A | R4–5; Q03–05; C§8 |
| parentReference | HierarchyStep → DiseaseConceptReference | Source parent concept reference | Y / A | R4–5; Q03–05; C§8 |
| citesPublication | Record → Publication | Citation at the source's actual attribution scope | Y / A | R7,13; Q01–03,06–07; C§6 |
| refersToStudy | Record → Study | Explicit study reference, not identity with publication | Y / A | R7,11,13; Q02,07; C§6,9 |
| describesStudy | StudyRecord → Study | Underlying study described by this versioned record | Y / A | R11; Q02,07; C§9 |
| mechanismDrug | MechanismRecord → Drug | Drug in attributed mechanism | Y / A | R10,13; Q02,06–07; C§9 |
| mechanismTarget | MechanismRecord → Target | Source-indexed target, with separate molecular wording | Y / A | R10; Q02,06–07; C§9 |
| indicationDrug | ClinicalIndicationRecord → Drug | Drug in source indication | Y / A | R10–11; Q02,06–07; C§9 |
| indicationDisease | ClinicalIndicationRecord → DiseaseConceptReference | Disease reference of indication entry | Y / A | R10–11; Q06–07; C§9 |
| indicationStudyRecord | ClinicalIndicationRecord → StudyRecord | Source-linked clinical report; no arbitrary drug-wide join | Y / A | R7,11; Q02,07; C§9 |
| hasPopulationScope | StudyRecord or Record → PopulationScope | Population restriction of this report/claim | Y / A | R11,14; Q07; C§9 |
| inputRecord | DerivedStatement → Resource | Identified input record/referent to computation; explicit role retained where needed | Y / D | R12–13; Q01–07; C§10,13 |
| resultTarget | DerivedStatement → Target | Target in a bounded computed result | Y / D | R12; Q01 comparison; C§10 |
| subjectRecord | DerivedStatement → Record | Focus of dependency/membership/comparison assessment | Y / D | R12–14; Q02,04–05; C§10,13 |
| comparatorRecord | DerivedStatement → Record | Other assessed record; role is not symmetric by default | Y / D | R12–13; Q02,04–05; C§10,13 |
| sharedInput | DerivedStatement → Resource | Established or assessed common publication/study/record, qualified by outcome | Y / D | R12–13; Q02; C§13 |
| inspectedRecord | InspectionRecord → Record | Specific version/passage inspected or attempted | Y / A | R8–9; Q01–07; C§11 |
| aboutRecord | InspectionRecord or MissingnessRecord → Resource | Record whose interpretation is assessed, or field-owning resource (including snapshot) whose information is missing | Y / A,D | R8–9,14; Q01–07; C§11–12 |
| observationContext | MissingnessRecord → Record | Inspection/retrieval context establishing the missingness observation | Y / A,D | R9,14; Q01,05–07; C§12 |
| originRole | DiseaseTargetAssociation → ControlledValue | Source aggregate versus project grouping | N / A,D | R1,12; Q01–06; C§5 |
| selectionMode | SelectionContext or DiseaseTargetAssociation → ControlledValue | Declared direct/inclusive view, not causal directness | N / A | R4–5; Q04; C§8 |
| inclusionKind | SelectionMembership → ControlledValue | Exact-anchor versus descendant-selected membership or unresolved explanation | N / A,D | R4–5; Q04; C§8 |
| mappingStatus | MappingRecord → ControlledValue | Interpretation/ambiguity state; does not replace observed/candidate distinction | N / A,D | R3; Q05; C§7 |
| inspectionDepth | InspectionRecord → ControlledValue | Actually inspected extent, not source accessibility | N / A | R8; Q01,06–07; C§11 |
| materialKind | InspectionRecord → ControlledValue | Abstract, registry page, full-text source etc.; independent of depth | N / A | R8; Q01,06–07; C§11 |
| accessOutcome | InspectionRecord → ControlledValue | Access success/failure/limit | N / A | R8–9; Q01,05–07; C§11 |
| interpretationOutcome | InspectionRecord → ControlledValue | Qualified technical conclusion, not biomedical truth label | N / A,D | R14; Q01–07; C§11 |
| missingnessReason | MissingnessRecord → ControlledValue | Reason for relevant missing/unresolved information | N / A,D | R9,14; Q01,05–07; C§12 |
| dependencyOutcome | DerivedStatement → ControlledValue | Qualified dependence/identity/source-sharing assessment | N / D | R13; Q02; C§13 |
| completenessStatus | Record → ControlledValue | Declared result/inspection extent, no completeness inferred from presence | N / A,D | R9,12,14; Q01–07; C§8,10,16 |
| studyKind | Study → ControlledValue | Trial/other investigation where source establishes it | N / A | R11; Q02,07; C§9 |
| reviewerType | prov:Agent → ControlledValue | Actual reviewer role/type; no invented expert attribution | N / A | R8,14; Q01–07; C§11 |
| prov:wasGeneratedBy | Record → prov:Activity | Local result/description generation, not fabricated upstream history | Y / P | R6,8,12; Q01–07; C§10–11 |
| prov:used | prov:Activity → prov:Entity | Information artifact used by known operation | Y / P | R6,12; Q01–07; C§10 |
| prov:wasAssociatedWith | prov:Activity → prov:Agent | Responsible actor/process agent, not a disease association | Y / P | R6,8; Q01–07; C§11 |
| prov:wasDerivedFrom | Record → prov:Entity | Documented information lineage, not clinical support | Y / P | R6,12–13; Q01–07; C§6,10 |

Controlled-value relations remain candidate object properties pending owner approval of concept versus literal codes. No new inverse names are proposed. `hasPopulationScope`'s broad Record usage is intentional for source-scoped claim context; StudyRecord is the normal Q07 owner. `inputRecord`/`sharedInput` may point to Publication or Study; their broad signatures must not force them into Record.

## 12. Candidate datatype-property catalogue

R = required for a complete applicable record; C = conditional on source availability, with explicit missingness where needed for the question; O = optional contextual detail. These are later validation expectations, not OWL cardinalities. Datatypes are proposals. S = source-preserved, G = project-generated, M = source-preserved or generated with origin recorded. Strings retain original spelling; a parsed date must not replace an imprecise original date with invented precision.

| Name / owner | Meaning / expected datatype | Presence / origin | Trace |
| --- | --- | --- | --- |
| externalIdentifier / DiseaseConceptReference, Target, Drug, Publication, Study | Authority-qualified external ID; string | C / S | R2,7,10–11; Q01–07; C§3–4,9 |
| identifierAuthority / same owners | Identifier authority/system; string | R when ID present / S | R2,7; Q01–07; C§3–4 |
| externalIRI / DiseaseConceptReference | Absolute external concept reference; anyURI; not OWL equality | O / S or documented resolution | R2–3; Q03–05; C§4 |
| sourceLabel / Record or referent | Original observed label; string or language-tagged text | C / S | R2–3,11; Q03,05,07; C§4,9 |
| sourceRecordIdentifier / Record | Provider record ID, not semantic identity by itself | C / S | R1,6,13; Q01–07; C§3,6 |
| sourceLocator / Record or SourceSnapshot | URL/document/passage locator; string, URI form when applicable | C / S | R6–7; Q01–07; C§6 |
| sourceAuthority / SourceSnapshot | Dataset/platform/provider name or identifier; string | R / S | R6; Q01–07; C§3 |
| snapshotVersion / SourceSnapshot | Reported release/version; string | C / S | R6,9; Q01–07; C§3 |
| artifactDescription / SourceSnapshot | Acquisition/artifact identity and extent; string | R / M | R6,9; Q01–07; C§3 |
| observedAt / Record or SourceSnapshot | Actual observation/retrieval date; dateTime or date at known precision | R for project encounters / G | R6,8; Q01–07; C§3,11 |
| recordVersion / Record | Source record-specific version where supplied; string | C / S | R6,9; Q01–07; C§3 |
| scopeText / Record | Scope, cohort, panel, gene context or qualified claim content; string | R when required to interpret claim / M | R3,11–14; Q01–07; C§6–13 |
| evidenceSourceType / EvidenceOccurrence | Provider datasource/evidence category verbatim; string | C / S | R1,6,13; Q01–02; C§6 |
| inputIdentifier / MappingRecord | Original assignment identifier exactly as observed; string | C / S | R2–3; Q03,05; C§7 |
| inputLabel / MappingRecord | Original assignment label; string | C / S | R2–3; Q03,05; C§7 |
| reportedMappedIdentifier / MappingRecord | Destination ID reported by platform; string | C / S | R2–3,5; Q03–05; C§7 |
| mappingAuthority / MappingRecord | Reported assigning source; string | C / S | R3,6; Q03,05; C§7 |
| mappingProcess / MappingRecord | Known upstream method, not inferred algorithm; string | C / S | R3,5; Q03,05; C§7 |
| aggregationMethod / DiseaseTargetAssociation | Source or project aggregate definition/version; string | R or explicit unavailable reason / M | R1,6,12; Q01–02; C§3,5 |
| aggregateScore / DiseaseTargetAssociation or qualified Record | Source-defined numeric aggregate; decimal | C / S | R1,14; Q01–02; C§5 |
| scoreDefinition / same owner | Source scoring semantics/method reference; string | C; needed to interpret score / S | R1,6,14; Q01–02; C§5 |
| scoreComponent / same owner | Datasource/component or total to which score applies; string | C / S | R1,6; Q01–02; C§5 |
| filterSpecification / SelectionContext or DiseaseTargetAssociation | Exact known source filters/settings; string | R for selection; relevant for scoped aggregate / M | R4–5,12; Q01–06; C§3,8 |
| operationMethod / DerivedStatement, HierarchyPath, SelectionContext or prov:Activity | Documented operation and method meaning; string | R for project outputs / G | R5,12–13; Q02,04–05; C§8,10 |
| methodVersion / same owners | Method revision when known/defined; string | C / M | R6,12; Q02,04–05; C§10 |
| limitationText / Record | Explicit interpretation/completeness limitation; string | R where limitation applies / M | R9,14; Q01–07; C§10–12 |
| mechanismText / MechanismRecord | Reported action and molecular-target detail; string | C / S | R10; Q06–07; C§9 |
| populationText / PopulationScope | Original eligibility/cohort wording; string | R / S | R11,14; Q07; C§9 |
| armLabel / PopulationScope | Source study arm/cohort identifier; string | C / S | R11; Q07; C§9 |
| studyDesignText / StudyRecord | Source-described design; string | C / S | R11,14; Q07; C§9 |
| trialPhaseText / StudyRecord or ClinicalIndicationRecord | Original phase or indication-level phase summary, retaining owner meaning; string | C / S | R11; Q02,07; C§9 |
| trialStatusText / StudyRecord | Dated reported status; string | C / S | R11; Q02,07; C§9 |
| statusDate / StudyRecord | Source's status date if known; date | C / S | R11; Q02,07; C§9 |
| approvalLabel / ClinicalIndicationRecord or qualified Record | Source approval wording only; string | C if field used / S | R10–11,14; Q06; C§9 |
| jurisdictionText / same owner | Jurisdiction qualifier as reported; string | C if approval used / S | R11,14; Q06; C§9 |
| regulatoryAuthorityText / same owner | Source-reported authority; string | C if approval used / S | R11,14; Q06; C§9 |
| productScopeText / same owner | Product/formulation restrictions as reported; string | C if approval used / S | R10–11,14; Q06; C§9 |
| effectiveDateText / same owner | Source effective/as-of wording at original precision; string | C if approval used / S | R11,14; Q06; C§9 |
| expectedField / MissingnessRecord | Governed field/meaning token whose information is missing/unresolved; string | R / G | R9,14; Q01,05–07; C§12 |
| rationale / InspectionRecord, MissingnessRecord or DerivedStatement | Technical basis, including dependency basis; string | R for assessment / G | R8–9,13–14; Q01–07; C§11–13 |
| resultSummary / DerivedStatement | Bounded human-readable finding; string; not sole structured result | R / G | R12–14; Q01–07; C§10 |
| agentIdentifier / prov:Agent | Actual reviewer/process identifier; string | C / M | R6,8; Q01–07; C§11 |
| prov:startedAtTime / prov:Activity | Known execution start; dateTime | C / G | R6,8,12; Q01–07; C§10–11 |
| prov:endedAtTime / prov:Activity | Known execution end; dateTime | C / G | R6,8,12; Q01–07; C§10–11 |

Redundant lexical IDs and reference links are deliberate only for lossless source preservation. Ingestion/validation must reconcile them or expose discrepancy; they must not become two independently editable truths. Target/Drug labels are display metadata from a declared source; conflicting/versioned labels belong in contextual Records, not a merged unqualified label set. No identifier-valued property is an OWL key.

## 13. Controlled-value proposals

Prefer governed enum-like concepts for repeatable operational categories, not a class per state. No final codes, member IRIs or SKOS scheme is created. Datatype source values are preserved alongside normalized categories only if mapping is documented.

| Area | Candidate distinctions | Why / trace |
| --- | --- | --- |
| Association origin | Source aggregate / project grouping | Enforces source versus project meaning; R1,12; Q01–06; C§5 |
| Selection mode | Direct only / descendant inclusive | Query specification, not member classification; R4–5; Q04; C§8 |
| Inclusion kind | Exact normalized anchor / descendant selected / explanation unresolved | Per-result semantics; R4–5; Q04; C§8 |
| Mapping status | Unreviewed validity / ambiguity unresolved / reviewed with stated limits | Orthogonal to reported vs candidate destination; R3; Q05; C§7 |
| Inspection depth | Metadata only / selected text / full relevant text with scope | Keep material kind separate; R8; Q01,06–07; C§11 |
| Material kind | Abstract / full-text source / registry or source page / metadata | Avoid falsely ranking heterogeneous materials; R8; Q01,06–07; C§11 |
| Access outcome | Accessible / partially accessible / inaccessible / not attempted | Access is not inspection; R8–9; Q01,05–07; C§11 |
| Interpretation outcome | Source-record support / not established by bundle / mapping ambiguity / access limited | Qualified technical conclusions; R14; Q01–07; C§11 |
| Missingness reason | Source omission / not retrieved / inaccessible / not applicable / not inspected / unresolved / reason unknown | Relevant gaps only; R9,14; Q01,05–07; C§12 |
| Dependency outcome | Shared source established / dependence established / possible dependence / independence assessed with limits / unresolved | Does not equate different sourcing with independence; R13; Q02; C§13 |
| Completeness | Declared complete for bounded operation / partial / unknown | Required before bounded absence claims; R9,12,14; Q01–07; C§16 |
| Study/reviewer kind | Trial versus other study; actual technical reviewer/process kind | Source/reviewer description, no expert label by default; R8,11; Q02,07; C§9,11 |

The inspection values are a proposal, not a revision of the approved distinctions: metadata-only, abstract, full-text, selected-passage and source-page inspection can be expressed using materialKind + inspectionDepth + scopeText. A later vocabulary must preserve all of them. Unknown not-applicable status is never substituted for a missing required value.

## 14. Domain/range and cardinality strategy

[OWL 2 Primer](https://www.w3.org/TR/owl2-primer/) explains that domain/range infer types and open-world restrictions are not database field checks. The following choices are project recommendations, not axioms created here.

| Property family (catalogue coverage) | Domain/range recommendation | Later validation focus |
| --- | --- | --- |
| associationDisease/Target; reportedEvidence; selectedEvidence | Narrow signatures semantically reasonable, but prefer explicit types and SHACL first; a wrong object must be reported, not silently retyped | Correct participants, origin-specific evidence relation, applicable scope |
| originalDisease/evidenceTarget/hasMappingRecord; mappingContext/Input/reportedDestination/candidateDestination | Narrow endpoint ranges may be useful after review; no equality or implied typing of external MONDO class IRIs | Expected record/reference roles; consistent lexical fields; observed/candidate distinction |
| queryAnchor/selectedOccurrence/inSelectionContext/justificationPath | Mixed owners on inSelectionContext make a narrow global domain risky; no multiple domain declarations | Exactly one context per membership; role-appropriate use and inclusion explanation |
| pathStep/pathStart/pathEnd/childReference/parentReference | Simple endpoint types potentially safe; no transitivity or path-to-membership chain | Continuous bounded chain, endpoint/version consistency, no invented steps |
| citesPublication/refersToStudy/describesStudy | Endpoint typing useful, but citation must not become support | Referent type and attribution scope |
| mechanismDrug/Target; indicationDrug/Disease/StudyRecord; hasPopulationScope | Specific roles could support narrow typing; broad hasPopulationScope domain deliberately avoids clinical conflation | Role correctness and claim-local study/population attachments |
| inputRecord/resultTarget/subjectRecord/comparatorRecord/sharedInput | resultTarget can have Target range; inputRecord/sharedInput broad, no forced Record range | Typed operation-specific inputs/results and derivation completeness |
| inspectedRecord/aboutRecord/observationContext | aboutRecord has several valid owners and missingness may concern a snapshot/referent; do not declare narrow global domain/range | Scoped review/missingness ownership and inspected version |
| All controlled-value properties | Prefer shape-specific value membership; no domain for each possible owner; no enum classes | Allowed category set for the relevant field, not a universal mixed code list |
| inSnapshot/contextRecord and all shared datatype fields | Shared domains must remain broad or omitted; lexical datatypes useful only where truly uniform | Conditional presence, datatype/format and correct source scope |
| PROV relations | Respect external entity/activity/agent roles; no narrower global redefinition | Local result vs source generation, actual actor/time and typed activities |

Multiple OWL domain axioms mean an intersection of inferred types, not an allowed-owner menu. Table owners therefore must not be mechanically converted to repeated domain declarations. For V1, **omit local global domains/ranges initially** unless owner review establishes a concrete typing benefit; use explicit typing plus later SHACL role checks. Each datatype row's expected datatype is a validation proposal, not a blanket restriction forcing conflicting source values into new meanings.

| Expectation | OWL | SHACL/data validation | Ingestion / application |
| --- | --- | --- | --- |
| Association has one disease scope, one target and one origin role in this representation | No exact-cardinality axiom | Required single values for a complete association | Flag incomplete source record, never invent participants |
| Evidence has source identity where supplied | No key/functionality | Identifier or traceable location plus missingness reason when needed | Deduplicate only on justified source/version identity |
| Mapping has zero/one/several candidates | No forced destination existence or max-one candidate | Zero candidates permitted; observed destination constraints source-dependent, not frozen globally | Preserve separate contexts and conflicting assignments |
| Membership has one occurrence and one context | No functional merging | Required singular roles | Multiple paths retained without duplicating occurrence |
| Indication has multiple studies | No maximum cardinality | Zero-to-many; missing required Q07 report handled explicitly | Do not attach all drug studies to every indication |
| Path forms a chain | No complex restriction/property chain | Endpoint and step-role checks | Validate continuity/version compatibility; qualify incompleteness |
| Review/missingness scoped to information | No universal existential | Required owner, outcome/reason and relevant context | Verify factual basis and actual review extent |
| Derived result has inputs/method | No unrestricted existential | Operation-specific required fields | Reproduce computation; distinguish empty result from absent retrieval |

No minimum source publication/study count or mandatory score is justified. Validation failures are data-quality outcomes, not grounds to create anonymous evidence or force identity merges. Cardinality and count policy beyond the bounded roles stays unselected.

## 15. Minimal candidate axioms and forbidden axioms

Candidate axioms for review only:

| Candidate | Useful consequence | Risk / disposition |
| --- | --- | --- |
| Named description classes subclass Record; Record and SourceSnapshot subclass prov:Entity | Record metadata/lineage queries can classify descriptions uniformly | Avoid treating underlying Target/Drug/Study as descriptions; recommend minimal hierarchy |
| Project grouping typed both DiseaseTargetAssociation and DerivedStatement when applicable | Reuses derived-output checks without duplicating association class | Requires origin consistency validation; no inference from source-provided scores |
| DiseaseTargetAssociation disjoint with EvidenceOccurrence | Detects accidental aggregate/occurrence conflation | Only if every future representation respects this record boundary; candidate narrow disjointness |
| MechanismRecord disjoint with ClinicalIndicationRecord | Exposes collapsed statement roles | One source document may contain both; use distinct record slices, not disjoint publications/drugs |
| Optional inverse navigation | No additional axiom currently needed; reverse query is sufficient | Avoid extra vocabulary and materialized-edge synchronization |
| Limited domain/range | Could infer application endpoint types later | Default omission until demonstrated benefit, as section 14 |

No OWL profile or reasoner is selected. A source aggregate is not disjoint from everything called a derived artifact: local representation generation and provider derivation still exist. Distinctions are made through roles/origin and record boundaries rather than over-broad disjointness.

**Must not introduce:** source disease equivalentClass normalized disease; sameAs from ordinary normalization; SKOS exactMatch as normalization default; mechanism chains yielding indication; indication yielding efficacy; trial presence yielding success; descendant membership yielding direct parent evidence; citation yielding support; repeated citation yielding independent support; absent evidence yielding negation; source score yielding causal/probabilistic ranking; globally functional disease mappings; pair-only association keys; global uniqueness inferred from identifier strings; automatic descendant closure or ontology-wide MONDO import; technical validation yielding biomedical truth. No class/property name can evade these semantic prohibitions.

## 16. Decision crosswalk: implementation responsibilities

OWL concerns meaning and the limited candidate classification/disjointness above. No column is an implementation completed by this task.

| Schema area | OWL | SHACL | Ingestion/transformation | Verification application | Experimental evaluation |
| --- | --- | --- | --- | --- | --- |
| Disease references | Application reference role, no disease equality | Authority/ID or reason, correct role | Preserve original labels; explicit version resolution | Compare scope without forced merge | Identity/scope fidelity |
| Association/evidence | Separate types | Participants, origin and conditional provenance | Preserve source aggregate, selected membership and score context | Avoid aggregate-to-causality upgrade | Evidence trace accuracy |
| Mapping | Assignment relation meaning, no equivalence | Context, destination/status coherence | Preserve reported/candidate distinctions | Surface ambiguity; no invented repair | Ambiguity handling |
| Selection/hierarchy | Distinct roles; no closure | Membership roles and step types | Store runs, paths, filters and result limits | Verify path/selection explanation and completeness | Propagation classification |
| Provenance/identity | Entity/activity separation | Source/version-or-reason, typed links | Preserve snapshots and justified deduplication | Audit claim-local lineage | Attribution fidelity |
| Clinical records | Mechanism/indication distinction | Role-specific participant/context checks | Preserve phase/status/approval wording | Block efficacy/population/approval broadening | Unsupported clinical claims |
| Inspection | Result not truth | Depth/material/access/outcome context | Record actual source versions/events | Assess support and abstention | Depth/qualification fidelity |
| Missingness | Unknown not false | Relevant slot/reason/owner | Avoid silent fill or irrelevant-null expansion | Use reason to qualify/abstain | Missingness treatment |
| Dependency | No automatic independence | Assessment basis/participants | Preserve shared inputs and record identity | Assess actual dependence with limits | Dependency handling |
| Derived outputs | Result distinct from source assertion | Inputs/method/scope/completeness | Reproducible bounded operations | Verify conclusions against inputs | Derivation fidelity |

## 17. Q01–Q07 candidate traversals

Arrows and names are explanatory routes, not RDF instances or production queries. Every route also follows `inSnapshot`, locators, missingness and relevant InspectionRecords; all frozen required slots and A–E boundaries remain mandatory.

| Q | Candidate route | Why separate / boundary |
| --- | --- | --- |
| Q01 | DiseaseTargetAssociation → reportedEvidence → EvidenceOccurrence → citesPublication/contextRecord; InspectionRecord → aboutRecord / inspectedRecord | Compare PSEN1 source types and actual inspected content, not aggregate scores. Null originals and sample limits survive. |
| Q02 | Two EvidenceOccurrences → contextRecord / refersToStudy; MechanismRecord → mechanismDrug/Target; ClinicalIndicationRecord → indicationStudyRecord → describesStudy; DerivedStatement → subjectRecord/comparatorRecord/sharedInput | Shared memantine trial/derivation is structured; distinct occurrence IDs cannot become independent genetic studies. |
| Q03 | EvidenceOccurrence → originalDisease; → hasMappingRecord → reportedDestination; SelectionMembership → selectedOccurrence and inSelectionContext → queryAnchor | Original Pick, mapped FTD and direct FTD query have different roles. Pick hierarchy context is not the cause of direct membership. |
| Q04 | SelectionMembership → inSelectionContext → selectionMode/queryAnchor; → selectedOccurrence → hasMappingRecord → reportedDestination; → justificationPath → pathStep → childReference/parentReference | Preserve APP/AD1 and MAPT/semantic-dementia diagnostics and intermediate steps. Query selection differs from normalization and from executed reasoning. |
| Q05 | Two MappingRecords → mappingContext/mappingInput/reportedDestination; inputIdentifier/inputLabel and mappingStatus; DerivedStatement → inputRecord | OMIM:600274 can have two contextual assignments without merge, repair or equivalence. Panel/gene context and access limits remain visible. |
| Q06 | Association → associationTarget ← mechanismTarget ← MechanismRecord → mechanismDrug; Drug ← indicationDrug ← ClinicalIndicationRecord → indicationDisease | Compare indication list separately from mechanism path; preserve inspected list completeness, publication depth and gene-indexing qualification. No treatment edge. |
| Q07 | ClinicalIndicationRecord → indicationStudyRecord → describesStudy/hasPopulationScope; StudyRecord phase/status fields; MechanismRecord → citesPublication/contextRecord; InspectionRecord → inspectedRecord | Broad FTD indication remains distinct from original trial population/status and healthy-participant mechanism study. No efficacy inference. |

Q02 source derivation connections not explicitly provided remain missing or documented through inspected context records; do not invent a mechanism-to-evidence provenance edge from matching drug names alone. Q06 absent exact FTD indication is at most a bounded inspected-list finding. Q07 trial cohorts remain original text without fabricated ontology mapping.

## 18. R1–R14 schema crosswalk

Frozen wording is reproduced verbatim. Every requirement has a candidate representation; the remaining risks are encoding choice, source completeness and validation policy, not an identified uncovered requirement.

| ID | Frozen requirement | Candidate classes/properties | Later validation/application duty |
| --- | --- | --- | --- |
| R1 | Association separately from individual evidence. | DiseaseTargetAssociation, EvidenceOccurrence; reportedEvidence / selectedEvidence | Check distinct record roles and constituent meaning; no independent-support interpretation. |
| R2 | Original/source disease identity separately from normalized disease identity. | DiseaseConceptReference, EvidenceOccurrence, MappingRecord; originalDisease, mappingInput, reportedDestination | Preserve original fields; lexical/link consistency and separate source/mapped scope. |
| R3 | Mapping context and unresolved ambiguity. | MappingRecord; mappingContext, candidateDestination, reportedDestination, mappingStatus | Allow competing contextual assignments; no automatic repair/equality. |
| R4 | Direct evidence separately from descendant-derived/propagated evidence. | SelectionContext, SelectionMembership, HierarchyPath/Step; inclusionKind, justificationPath | Validate bounded explanation and mode; do not reclassify descendants as direct parent evidence. |
| R5 | Query-time descendant inclusion separately from upstream source normalization. | MappingRecord versus SelectionContext/Membership; hasMappingRecord, inSelectionContext, queryAnchor | Separate upstream assignment from selection or project traversal. |
| R6 | Evidence provenance at claim/association level. | Record, SourceSnapshot, PROV activity; inSnapshot, contextRecord, prov:wasGeneratedBy/wasDerivedFrom | Check claim-local origin and distinguish local representation generation from source history. |
| R7 | Publication/study/source locator where available. | Publication, Study, StudyRecord; citesPublication, refersToStudy, sourceLocator | Preserve actual attribution scope; access and citation are not demonstrated support. |
| R8 | Inspection/review depth where relevant. | InspectionRecord; inspectedRecord, inspectionDepth, materialKind, accessOutcome | Validate actual depth/version and avoid publication-global judgments. |
| R9 | Missing provenance/information explicitly rather than silently repaired. | MissingnessRecord; aboutRecord, observationContext, expectedField, missingnessReason | Require contextual reasons only for relevant gaps; avoid invented values and blanket null expansion. |
| R10 | Target–drug mechanism separately from disease indication. | MechanismRecord, ClinicalIndicationRecord; mechanismDrug/Target, indicationDrug/Disease | Reject relation composition into indication or treatment. |
| R11 | Clinical indication separately from trial population and trial status. | ClinicalIndicationRecord, Study/StudyRecord, PopulationScope; indicationStudyRecord, describesStudy, hasPopulationScope; phase/status fields | Keep owner and dates explicit; no efficacy, completion or unrestricted approval upgrade. |
| R12 | Derived comparisons/intersections separately from source assertions. | DerivedStatement; inputRecord, resultTarget, operationMethod, inSelectionContext, completenessStatus | Reproduce bounded computations; keep source assertions distinct. |
| R13 | Shared/dependent evidence so multiple records are not automatically independent support. | EvidenceOccurrence, Publication/Study, DerivedStatement; sharedInput, subjectRecord, comparatorRecord, dependencyOutcome | Resolve duplicates conservatively; shared-source basis and independence limits remain explicit. |
| R14 | Scope qualification and abstention conditions required by the core questions. | InspectionRecord, DerivedStatement, MissingnessRecord; interpretationOutcome, rationale, scopeText, limitationText | Application verifies support and qualifies/abstains; passing shapes does not establish truth. |

## 19. Smallest defensible V1 and remaining decisions

The candidate core has **21 local classes**, counting Record and SourceSnapshot but not external PROV types: Record; DiseaseConceptReference; Target; Drug; DiseaseTargetAssociation; EvidenceOccurrence; MappingRecord; SelectionContext; SelectionMembership; HierarchyStep; HierarchyPath; Publication; Study; StudyRecord; MechanismRecord; ClinicalIndicationRecord; PopulationScope; DerivedStatement; InspectionRecord; MissingnessRecord; SourceSnapshot.

This is a representation capability inventory, not a demand to create instances for every class in every question. The additional StudyRecord is justified by dated population/status (Q07); the two path roles by versioned consecutive steps and alternative explanations (Q04). Missingness is sparse. DependencyAssessment, Trial, DatasetRelease and generic SourceAssertion/Provenance wrappers do not add separate classes. No broader disease taxonomy, phase/status class hierarchy or biomedical process classes are proposed. Optional regulatory metadata is retained only where already needed to prevent an approval overclaim.

Owner decisions before implementation:

1. Accept/revise local disease-reference records and identifier-value links to external concepts; approve no automatic equivalence/punning/import.
2. Accept one association class with originRole and separate reported versus selected evidence relations; review project-grouping dual typing as DerivedStatement.
3. Accept the candidate class/property catalogue, especially the versioned StudyRecord and bounded HierarchyPath/Step pattern.
4. Accept the hybrid provenance subset and strict activity/result/source-generation distinctions; retain no full import.
5. Accept sparse MissingnessRecord and dependency findings as qualified DerivedStatements rather than new assessment classes.
6. Review controlled-concept versus literal code encoding and exact future category definitions. Source phase/status text remains preserved regardless.
7. Approve/revise minimal subclass/disjointness candidates, default omission of global domain/range, and structural cardinalities outside OWL.
8. Specify validation targets, required-field-or-reason policies, source artifact/version acquisition and identity resolution before executable checks. No namespace, physical ID scheme, OWL profile, reasoner or store is selected here.

Known limitations: the catalogue is larger than a disease–gene schema because all seven questions demand source/selection/review distinctions. It is not proven minimal by implementation, and no query performance is measured. Hierarchy paths require later structural checks; string-based source method/filter descriptions require a later reproducibility format; sparse missingness requires an explicit relevant-field policy. PROV external-term use and any future loaded axioms require an import/entailment contract. These are visible owner/design choices, not silently completed work.

## 20. Proposed next task and review basis

After owner review and separate authorization, perform a **schema decision reconciliation and implementation-readiness specification**: settle names, reference encoding, controlled-value representation, provenance subset, intended axioms and shape/application obligations; define source/identity validation fixtures in prose and the proposed namespace policy for review. Do not create executable ontology, data, shapes or tests until explicitly authorized. Do not begin the next task automatically.

Primary technical references consulted for this proposal: [OWL 2 Primer](https://www.w3.org/TR/owl2-primer/), [SKOS Reference](https://www.w3.org/TR/skos-reference/#mapping) and [PROV-O](https://www.w3.org/TR/prov-o/). These establish vocabulary semantics, not endorsement of this schema. Domain decisions derive from the approved contract and frozen Q/R cases. No new clinical/biomedical assertions are verified by this design task. Graph advantage remains **NOT YET DEMONSTRATED** and no biomedical expert adjudication is claimed.

Only `docs/m1_schema_design.md` is created. No approved document is rewritten. No namespace, RDF/OWL/TTL/JSON-LD, SHACL, imports, generated RDF code, instances, production queries, software installation, database configuration, commits or pushes are created. This is a schema proposal, not implemented or reasoner-tested ontology.
