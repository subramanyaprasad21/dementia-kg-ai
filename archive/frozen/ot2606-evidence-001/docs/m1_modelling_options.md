# M1 Task 001 — ontology/application modelling alternatives

Status: **M1 CHECKPOINT 1: ALTERNATIVE B APPROVED AS MODELLING DIRECTION; IMPLEMENTATION DETAILS OPEN**. Reviewed 2026-09-17. Baseline: main at b46de34, M0 frozen and pushed. This document begins authorized M1 design analysis; the frozen documents' statements that M1 had not begun describe their checkpoint date. No ontology, namespace, instance, shape, dependency or executable query is created here.

## 1. Frozen problem and interpretation

Represent the meaning and limits of the existing [Q01–Q07 and R1–R14](competency_questions.md), not merely a disease–gene link. Anchors remain AD MONDO:0004975 and FTD MONDO:0017276. Narrower disease context is bounded by the [approved scope](project_scope.md); no automatic descendant closure, phenotype modelling or process/pathway expansion. [Task 004 source review](source_audit.md#task-004-technical-source-review) supplies the examples; no new biomedical evidence investigation was performed.

The model must keep apart: an aggregate association; an individual source/evidence record; what that record asserts; its original and normalized disease; a query's selection of it; and a review judgment about what an answer may say. A locator is not its publication's conclusion. A stored support judgment is not automatically correct. Existing source ambiguity must survive ingestion rather than being resolved by ontology convenience.

Notation below is conceptual prose, not proposed class/property names. “Resource” means an identifiable thing the graph can describe. A resource representing a reported statement does not automatically assert that statement as an unqualified world fact.

## 2. Concepts before architecture choice

| Concept | Project-specific explanation |
| --- | --- |
| Reification | Give a statement a handle so its source and qualifications can be described. Rather than only connecting FTD and MAPT, describe the particular source record that connects them. RDF's standard statement description does not by itself assert the described triple; a domain-specific relation resource is another pattern, not identical syntax. |
| N-ary relationship | A fact needs more than two participants: drug, indication disease, source report, population and time. A relation resource connects those roles without treating population as a universal attribute of the drug. |
| Assertion/statement node | A record of someone saying something. Two records may express the same proposition but come from different sources—or share one underlying trial. Statement occurrence identity and proposition identity are different decisions. |
| Provenance | Which record, source version, activity and review produced this information? For Q02, two evidence IDs can lead back to one memantine trial. |
| Normalization | A source label/identifier is assigned a platform identifier. Pick wording mapping to FTD is an observed transformation, not proof that the concepts are equivalent. |
| Ontology alignment | Document how local/source concepts correspond to external meanings, including relation kind, context and uncertainty. An xref alone does not warrant equivalence. |
| Direct versus inferred relation | A source may explicitly state something; a system may derive another statement. OT “direct” instead describes normalized-anchor query membership. These senses must have separate fields/records. |
| Open-world assumption | Failure to find a gosuranemab efficacy assertion does not imply it is false. A bounded query can report no matching record in its declared snapshot; it cannot infer a universal clinical negative. |
| Domain/range | These supply typing implications, not database rejection rules. Using a property whose range is a disease type can infer that its object is a disease; it need not reject a wrongly supplied target. |
| SHACL versus OWL | OWL describes logical meaning; SHACL checks a selected data graph against declared constraints. “A locator field is required” is a data check, while “this record is a subtype of another record type” is semantic classification. Neither verifies that a paper supports a clinical claim. |

Technical grounding: [RDF 1.1 reification semantics](https://www.w3.org/TR/rdf11-mt/#reification), [W3C n-ary relation patterns](https://www.w3.org/TR/swbp-n-aryRelations/), [OWL primer](https://www.w3.org/TR/owl2-primer/) and [SHACL](https://www.w3.org/TR/shacl/). The examples and architecture judgments here are project design analysis, not claims those standards endorse this application.

## 3. Architecture A — direct relations with selective qualification (CONSIDERED ALTERNATIVE)

**Idea:** keep simple entity links; introduce a statement/relation resource whenever source, scope or evidence matters. Entities, sources and documents are resources. Identity labels and uncomplicated structural links stay direct; association, mapping, mechanism and indication links acquire qualified statement occurrences when needed.

For Q01, a disease–target summary edge is accompanied by a statement occurrence linked to evidence, whose mapping record preserves original/normalized disease. Multiple occurrences can describe the same endpoint pair. A summary edge must mean only “represented association exists in this declared view,” never causal support. It must be mechanically traceable to qualifying records and excluded from unsupported answer generation on its own.

Provenance attaches to occurrences rather than the bare edge or target. Mapping candidates/context require extra resources. Derived summaries identify inputs and rules; source assertions stay separate. Mechanisms and indications use different relation meanings and separate qualifications. Shared trial/publication resources expose dependencies. Query-selection resources distinguish direct versus inclusive results and paths.

**Reasoning possible:** limited type/hierarchy inference over deliberately asserted semantics. Reading a statement description does not automatically entail its described edge. No safe universal disease–target→drug-indication chain exists.

**What gets harder:** queries have two routes, qualified records and shortcuts. Nearly every frozen question needs qualification, so the apparent simplicity erodes. Synchronization and orphan shortcuts become recurring risks. A can satisfy the requirements if provenance-bearing occurrences are mandatory for core relations; it then approaches B in substance while retaining two representations.

## 4. Architecture B — explicit association resources with typed qualified relations (APPROVED DIRECTION)

**Idea:** make each aggregate disease–target association an explicit resource. Evidence records remain separate, reusable resources. Do not place one source disease on an aggregate with many differently scoped supports: each evidence occurrence retains its original identity and contextual normalization assignment. The association identifies its normalized anchor, target, source/snapshot and aggregation/view context.

Mappings, evidence-selection context, drug mechanisms, indications and needed trial/population context are identifiable relation records with their own roles. Ordinary resource-to-participant links remain direct edges. A bare disease–target shortcut is optional only as a later documented projection, not the canonical evidence carrier.

An evidence-selection record binds requested anchor, mapped disease, query setting, snapshot and applicable path. Thus the same evidence can be direct for its normalized disease and descendant-selected for another anchor without changing its intrinsic source record. Direct-anchor and inclusive aggregates must not overwrite one another. This addresses R4/R5 without importing a whole subtree.

Provenance attaches to the association and its constituent records; review-depth information belongs to the inspection of a particular source version, not a universal property of a PMID. Distinct evidence occurrences can reference the same trial or mechanism record. Derived comparisons point to inputs and declared selection operations. Mechanism and indication records never become interchangeable simply because they share a drug.

**Reasoning possible:** record-type classification, explicitly justified inverses/hierarchy relationships, and bounded path queries. Most core behavior is provenance-aware joining, not advanced OWL entailment. A separate application review result records qualification or abstention with its reason and inspected bundle.

**What gets harder:** more joins and identity rules than an edge-only graph; aggregation and query context must be versioned carefully. Generic claims beyond the seven questions need an extension rather than being expressible through one universal statement template. B must include qualified non-association relations; an association node alone does not solve Q06/Q07.

## 5. Architecture C — source claims as the organizing unit (CONSIDERED ALTERNATIVE)

**Idea:** every source assertion occurrence is a first-class resource. Its subject, relation meaning, object/participants, scope, evidence, mapping and provenance are separately accessible. Association aggregates become derived views over these occurrences. Mechanism and indication claims use distinct typed roles, not a single ambiguous relation string.

Direct edges connect claim resources to participants, source records and supporting locators; trusted entity metadata may stay direct. The asserted biomedical content is not automatically materialized as an unconditional edge. Claims with identical wording remain separate when source occurrence or review context differs. A semantic proposition can be shared only under an explicit identity policy; no automatic merging by text or endpoint pair.

Normalization produces linked contextual assignments, never overwrites original claims. Selection activities/results preserve query-time propagation separately. Derived comparisons link their input claims and method. Dependencies are discoverable through shared inputs, trials and publications. Missing provenance and review outcomes can be described consistently across statement types.

**Reasoning possible:** classification of claim/evidence kinds and lineage traversal. Generic subject/relation/object descriptions do not automatically inherit the semantics of the relation being described. Application logic or explicitly approved bridges would be needed to assert selected contents; indiscriminate bridges would erase qualification.

**What gets harder:** generic queries must repeatedly unpack claim roles; n-ary mechanism/trial content still needs typed patterns. Claim occurrence, proposition, aggregate and review identities create a larger modelling burden. It is a defensible option if diverse claim lifecycles dominate, but the frozen set does not yet establish that breadth.

## 6. R1–R14 coverage matrix

**D = directly supported** by the alternative's organizing pattern; **P = supported with additional pattern** explicitly identified below; **A = awkward**, representable but with duplicated routes or identity burden; **U = unsupported**. “Supported” means representable, not automatically validated or clinically adjudicated. No full alternative is marked U because each can be extended without contradicting its premise; the naked disease–gene model would be unsupported for most requirements.

| Requirement (exact frozen wording) | A | B | C |
| --- | --- | --- | --- |
| R1. Association separately from individual evidence. | P — statement occurrence plus aggregate identity | D — association and evidence are separate | P — distinguish aggregate view from claims |
| R2. Original/source disease identity separately from normalized disease identity. | P — mapping resource beside edge | D — per-evidence original and mapped identities | D — source content and normalized assignment |
| R3. Mapping context and unresolved ambiguity. | A — competing qualified edges need context | P — contextual mapping alternatives | D — competing assignments remain claims |
| R4. Direct evidence separately from descendant-derived/propagated evidence. | A — shortcut can conceal membership | P — evidence-selection record | P — selection result linked to claim |
| R5. Query-time descendant inclusion separately from upstream source normalization. | P — mapping and query records distinct | P — mapping versus selection activity | P — normalization versus selection activity |
| R6. Evidence provenance at claim/association level. | P — occurrence-level source links | D — association/evidence identity supports attachment | D — provenance on each claim occurrence |
| R7. Publication/study/source locator where available. | P — source/document resources | D — evidence locator links | D — claim/evidence locator links |
| R8. Inspection/review depth where relevant. | P — inspection record with version | P — inspection record with version | P — inspection record with version |
| R9. Missing provenance/information explicitly rather than silently repaired. | P — explicit missingness reason/status | P — explicit missingness reason/status | P — explicit missingness reason/status |
| R10. Target–drug mechanism separately from disease indication. | P — separate qualified relation patterns | D — separate mechanism/indication records | D — separate typed claim roles |
| R11. Clinical indication separately from trial population and trial status. | P — indication/report/population records | D — separate indication and report context | P — n-ary population/report pattern |
| R12. Derived comparisons/intersections separately from source assertions. | A — shortcut/source distinction must survive | P — derived result with inputs/rule | D — derived claims distinct from source claims |
| R13. Shared/dependent evidence so multiple records are not automatically independent support. | P — shared underlying dependency resources | D — reusable evidence/report resources | D — shared inputs between claim occurrences |
| R14. Scope qualification and abstention conditions required by the core questions. | P — review outcome and application check | P — review outcome and application check | P — review outcome and application check |

R9 needs a reason such as absent in source, not inspected or access failed; no invented PMID or fabricated “unknown source” entity. R13 records observed dependence; it does not infer independence from different identifiers or statistical dependence merely from a shared publication. R14 represents the review decision and conditions; an application still has to assess the claim against the inspected evidence.

## 7. Q01–Q07 support and conceptual query routes

All routes use the frozen records and their existing A–E criteria. These are information-access plans, not full production SPARQL, schema declarations or data instances. None establishes biomedical truth through connectivity.

| Question | A: qualified edges | B: association resources | C: claim occurrences |
| --- | --- | --- | --- |
| Q01 PSEN1 support | Join edge occurrence→evidence→source disease/publication→inspection; prohibit shortcut-only answer. | Join AD/FTD associations for PSEN1→evidence→mapping and publication/inspection; compare source type and depth. | Select AD/FTD association claims about PSEN1→support records→source/inspection; preserve occurrence identities. |
| Q02 independent genetic confirmation | Join two qualified occurrences to shared drug/report lineage; edge count is insufficient. | Find the two clinical-precedence evidence records and intersect report/mechanism identifiers, not aggregate scores. | Trace derivation inputs of both claim occurrences; find shared trial and mechanism lineage. |
| Q03 Pick source scope | Follow the direct FTD edge's qualified record to original Pick and normalization; direct shortcut alone loses the distinction. | Association→evidence→original Pick and mapped FTD; read query context independently. | Compare original assertion's scope with normalized assignment linked to the FTD claim. |
| Q04 propagation | Compare direct/inclusive selection records; do not union qualified and shortcut results without identity checks. | Association view→selection record→mapped disease/path; compare with direct Pick→FTD normalization case. | Compare selection derivations and original normalization events; return paths and input identities. |
| Q05 mapping ambiguity | Group contextual mapping records by OMIM:600274, retaining statement/gene/panel scope. | Group per-evidence assignments by original identifier; report both destinations and qualifiers. | Compare mapping claims sharing source identifier but differing in context/destination; no equality inference. |
| Q06 mechanism/indication | Traverse qualified disease–target and drug–target statements; separately retrieve indication records. | Association→target←mechanism←drug→indication→disease; compare disease identities without inventing indication. | Join association, mechanism and indication claim roles by participants; do not materialize a treatment claim. |
| Q07 trial population | Indication occurrence→report→population/status; mechanism inspection stays separate. | Drug→indication→clinical report→population/status and separate mechanism→inspection; retain source dates. | Indication claim→source report→population qualifiers; separate trial-status and mechanism claim contexts. |

Illustrative pseudo-query for the same Q03 information under each alternative (capitalized words are placeholders, not ontology terms):

```text
A: FIND qualified occurrence OF (FTD, association, MAPT)
   JOIN occurrence evidence, original disease, normalized disease, source
B: FIND association WITH anchor FTD AND target MAPT
   JOIN association evidence; JOIN evidence original/mapped disease and source
C: FIND source-claim occurrence WITH association meaning AND target MAPT
   JOIN normalized assignment TO FTD; RETURN original scope and source
```

Common query guards, realized through the routes above:

```text
Q04: FOR selected evidence in the specified direct/inclusive view
     RETURN requested anchor, mapped disease, selection mode, explicit path, mapping context
Q06: JOIN target to mechanism to drug
     LOOK UP that drug's indications separately; compare their disease with the requested anchor
Q07: JOIN indication to primary report to population and dated status
     RETURN qualification and actual inspection depth
Broadening check: COMPARE answer claim scope/relation with this evidence bundle
     IF required context is missing or mapping unresolved: qualify/abstain on that part
```

A future SPARQL `NOT EXISTS` can establish only a missing match within a declared dataset/view. It must not turn the Q06 bounded indication-list absence into “no indication exists anywhere.” A path query over hierarchy edges does not inherently return the intermediate path provenance or prove a biomedical generalization; that evidence needs explicit retrieval. [SPARQL 1.1](https://www.w3.org/TR/sparql11-query/) defines graph patterns/property paths; the scope guards above are application policy.

## 8. Provenance strategies — none frozen

These strategies can be combined and are not mutually exclusive architectures. Statement identity and provenance vocabulary answer different questions.

| Strategy | Semantic clarity / frozen-question fit | OWL compatibility and reasoning | SPARQL usability | Complexity / portability |
| --- | --- | --- | --- | --- |
| PROV-O-style subset | Common language for entities, activities, agents and derivation; useful for R6–R8/R12/R13. Still needs project semantics for scope, evidence support and missingness. | OWL vocabulary available; qualification patterns can carry activity context. `prov:Association` concerns an activity/agent association, not our disease–target association. Do not reuse it by name alone. | Extra joins expose source and transformation chains; does not assess paper entailment. | Medium; reusable lineage semantics. Referencing terms and importing all axioms are separate choices. |
| Lightweight project-specific provenance | Can express the minimal record/version/locator/depth fields clearly. Meaning must be documented and later mapped for exchange. | Ordinary OWL-compatible resource patterns possible; no automatic standard lineage interpretation. | Short, domain-specific paths. | Low initial cost, greater maintenance/interoperability burden if it grows into a private provenance framework. |
| Explicit statement/relation resources | Distinguish occurrences and attach claim-local context; supports all seven cases with typed patterns. Standard RDF reification is one encoding, not a clinical support model. | Ordinary resources are compatible with OWL if roles are disciplined. Described contents are not automatically asserted. OWL axiom annotations alone do not supply the required evidence/selection lifecycle. | More joins, portable ordinary triple patterns. | Medium; robust occurrence identity policy required. Appropriate with B or C and mandatory qualified parts of A. |
| Named graphs | Useful for source/version packaging or separating source and derived views. A graph name alone does not identify why each contained claim is supported. | Dataset grouping is not an OWL modal context or automatic trust boundary. Unioning graphs can lose distinctions; entailment dataset must be specified. | `GRAPH` can select views; per-claim qualifications still need records. | Medium when combined with records; graph-per-claim adds management overhead. Graph-name semantics and default-union behavior need a contract. |
| RDF-star / RDF 1.2 triple terms | Compact statement metadata may help, but repeated occurrences of the same triple still need identity/context. Older RDF-star implementations and RDF 1.2 must not be assumed interchangeable. | Do not assume seamless OWL 2 reasoning over triple terms. A projection/translation and semantics check would be needed. | Requires compatible parser, query language and export path; none selected or tested here. | Stack-dependent and currently unjustified for the core. Defer pending demonstrated need and end-to-end compatibility. |

Official basis: [PROV-O](https://www.w3.org/TR/prov-o/) provides qualified derivation patterns, not biomedical support semantics. [RDF 1.1 datasets](https://www.w3.org/TR/rdf11-concepts/#section-dataset) do not by themselves assign a provenance interpretation to graph names. The inspected [RDF 1.2 Concepts](https://www.w3.org/TR/rdf12-concepts/) page identifies a Candidate Recommendation Snapshot and triple-term model; this is an observed specification status, not an assertion of deployment compatibility. No project store exists against which compatibility could be established.

**Provisional preference:** ordinary identifiable relation/evidence resources, with a small PROV-O-style lineage subset and explicit project scope/review semantics. Named graphs may supplement snapshot organization. This is a recommendation for the next design comparison, not a frozen vocabulary/import decision. PROV derivation alone must never mean independent corroboration or scientific support.

## 9. Disease identity and ontology reuse

**Class-versus-record boundary:** a MONDO disease concept is commonly represented as an ontology class; an OT disease record is a record about that concept, not a patient instance of that disease. Do not type an association record as an instance of Alzheimer disease. For all three alternatives, prefer discussing a concept-reference layer explicitly before choosing how references become OWL assertions.

OWL 2 allows certain class/individual reuse of an IRI (“punning”), but the class and individual interpretations are separate. Referencing a class IRI as a participant does not automatically make its subclass hierarchy operate on that participant as an individual. A class-reference annotation or a concept-record link is another option; those links do not automatically yield OWL disease-hierarchy inferences either. This unresolved representation choice needs an owner-reviewed contract, not accidental OWL Full metamodeling. [OWL primer, metamodeling](https://www.w3.org/TR/owl2-primer/#OWL_2_DL_and_OWL_2_Full).

| Reuse option | Benefit | Cost / risk | Proposed disposition |
| --- | --- | --- | --- |
| Reference MONDO IRIs without full import | Preserves external identity with a small local semantic surface; fits the fixed anchors. | Referencing alone supplies no imported axioms, labels or hierarchy entailments. Need versioned source records for the bounded paths; do not fabricate a local replacement taxonomy. | Preferred starting proposal for A/B/C. Decide concept-reference pattern explicitly. |
| Partial/module import | Supplies selected axioms when a named inference genuinely needs them. | An extracted module can contain more than a handpicked subtree; extraction method, semantic preservation, version, licence and profile effects need review. | Investigate only against a concrete unmet inference requirement, not for convenience. |
| Full import | Broad external axiom context. | Large entailment/import closure, profile interactions and scope beyond audited paths; importing is not merely copying labels. Adds maintenance without demonstrated CQ need. | Not recommended for V1; M0 rejects it as an automatic default. |
| Local application classes aligned to external IRIs | Separates application records from medical concepts and can expose source context. | Record classes must not be declared equivalent to disease classes. Duplicated local medical classes increase mapping/drift burden; subclass/equivalence assertions need semantic justification. | Useful for application roles/records, not local copies of AD/FTD. No class names or axioms selected. |

Reference, mapping, import and application extension remain different operations. Neither a string match nor a source normalization assignment warrants `owl:sameAs` or `owl:equivalentClass`. The [approved source audit](source_audit.md#reuse-and-alignment-boundary) already records these reuse constraints; nothing is imported here.

## 10. Expressivity recommendation — PROPOSED

| Approach | Fit to frozen requirements | Recommendation / limit |
| --- | --- | --- |
| Simple RDFS/OWL semantics | Record-type classification, deliberately justified subtypes and ordinary relationships. The seven questions mostly join explicit records. | Start with a small axiom set; decide domain/range carefully. No property chain from association/mechanism to indication. |
| OWL 2 RL-style reasoning | Could support a controlled rule-oriented entailment regime for approved type/property semantics. | Candidate only if a documented inference need emerges; no CQ currently demands the full profile. Restrict input axioms and assess inferred-output scope. |
| More expressive OWL constructs | May describe complex class restrictions, but do not recover missing source fields or validate literature support. | No frozen requirement currently justifies additional expressivity. Existentials/cardinalities are not completeness checks. |
| Minimal axioms plus SHACL | Separates meaning from validation of record structure and permitted combinations. | Best current starting recommendation; constraint list and exact vocabulary/profile remain unselected. Application checks still handle claim scope and abstention. |

The [OWL 2 Profiles specification](https://www.w3.org/TR/owl2-profiles/) defines RL as a restricted profile oriented to rule-based implementation, not as a universal choice for KGs. Profile conformance concerns the actual axioms/import closure; selecting an engine name or saying “RL-style” is not conformance. No engine/profile is frozen.

**Inference genuinely needed?** None of Q01–Q07 presently requires an OWL reasoner to answer. Q04 requires inspectable hierarchy interpretation, achievable with the approved explicit path records and bounded query traversal. Classification of modelling record types could be useful, but is not a demonstrated requirement for more expressive logic. Query-derived selection and source normalization must remain recorded operations, not silently reclassified as OWL entailments. No automatic descendant closure is proposed.

## 11. Responsibility matrix

S = semantic modelling/inference concern; D = structural/data-quality check (potential SHACL); P = provenance; A = application verification; E = later evaluation. A dash means no primary responsibility, not a prohibition. D checks require declared validation targets/snapshot; absence alone is not a logical negation. Rows refer to the exact R wording in section 6.

| Requirement | S: meaning / optional inference | D: structural checks | P: lineage | A: verification | E: later outcome |
| --- | --- | --- | --- | --- | --- |
| R1 | Distinct aggregate/evidence roles | Required links, permitted roles | Aggregate inputs/version | Avoid score→support upgrade | Correct tracing |
| R2 | Distinct identity roles | Required role or explicit missingness | Source/mapping version | Compare scopes | Scope fidelity |
| R3 | Assignment ≠ equivalence | Context/status fields | Mapping authority/method | Preserve unresolved alternatives | Ambiguity handling |
| R4 | Membership relative to anchor/view | Anchor/mode/path fields | Selected record/snapshot | Classify direct/inclusive correctly | Directness accuracy |
| R5 | Mapping ≠ selection operation | Separate operation records | Inputs/outputs/settings | Avoid conflating the operations | Classification accuracy |
| R6 | Claim-local attribution meaning | Required provenance links | Source/activity chain | Match provenance to claim | Attribution completeness |
| R7 | Locator ≠ support | Format/role where supplied | Source locator/version | Retrieval/access check | Correct locator/limits |
| R8 | Inspection is contextual | Depth/date/target fields | Reviewer/activity and text version | Do not overstate review | Depth fidelity |
| R9 | Unknown ≠ false | Conditional field-or-reason rules | Origin of missingness | Qualification/abstention | Correct missingness treatment |
| R10 | Separate relation meanings | Mechanism/indication roles | Separate sources | Reject invalid relation composition | Distinction accuracy |
| R11 | Indication ≠ population/status | Report/context/date fields | Registry snapshot | Bound population and status claims | Qualification accuracy |
| R12 | Derived result ≠ source assertion | Input/method/result links | Derivation chain | Reproduce comparison under settings | Derivation fidelity |
| R13 | Shared input ≠ independent support | Dependency links where known | Reused trial/source IDs | Detect known reuse; no invented independence | Dependency handling |
| R14 | Represent judgment and scope | Required reason/context | Inspected evidence bundle | Decide support/qualification/abstention | Supported completion and excess abstention |

SHACL may check that the inspected-data record supplies a locator or an explicit reason for absence. It cannot determine whether a publication supports a claim merely from that locator. SHACL validation results depend on the selected graph and entailment configuration; these must be declared. OWL consistency is not data completeness, and passing either check is not biomedical truth. [SHACL specification](https://www.w3.org/TR/shacl/).

## 12. Invalid-inference risks by alternative

| Failure | A risk / guard | B risk / guard | C risk / guard |
| --- | --- | --- | --- |
| Normalized disease becomes equivalent to original | Shortcut hides mapping; require occurrence/context retrieval. | Aggregate may overwrite evidence scope; keep assignments per evidence. | Canonicalization may merge claims; keep source occurrences and contextual assignments. |
| Mechanism becomes indication | Naive two-edge path; prohibit derived indication shortcuts. | Shared drug connects distinct records; require an explicit indication record. | Generic claim chaining; require typed roles and separate support assessment. |
| Citation becomes support | Annotation mistaken for evidence; require inspection record. | Evidence linkage mistaken for entailment; distinguish locator from assessed support. | Claim-to-publication edge appears authoritative; require separate review judgment/depth. |
| Descendant evidence becomes direct | Flattened edges lose selection mode; keep view membership. | Merge of direct/inclusive aggregates; include snapshot/view in identity. | Derived claim overwrites original; retain selection inputs/path. |
| Repeated evidence becomes independent | Duplicate edges/occurrences inflate counts; trace shared inputs. | Distinct evidence IDs inflate support; group observed report dependencies. | Many claims from one source appear corroborative; preserve lineage and distinguish occurrence counts. |
| Missing match becomes false | Closed query interpreted globally; declare bundle boundary. | Empty evidence list mistaken for disproof; preserve reason/status. | Unsupported claim confused with negated claim; separate review outcome. |
| OWL identity collapses records | Over-broad equality/key on endpoints; do not equate occurrence IDs. | Pair-only key collapses source/version/view distinctions; define identity contract first. | Proposition-only key merges independent occurrences; separate proposition from occurrence. |

Further design risk across all options: under OWL's lack of a general unique-name assumption, different IRIs are not automatically proven different individuals. Conversely, careless keys/functionality can force unwanted equality. Do not use OWL cardinality to repair ambiguous provenance by merging records. Keep observed source-record identifiers as identifiers and validate uniqueness under an explicit record policy. These are design risks to test later, not observed failures of an implemented model. [OWL semantics overview](https://www.w3.org/TR/owl2-primer/).

## 13. Comparative effort and recommendation

Qualitative estimates only; no implementation timings, query benchmarks or reasoner tests were run.

| Criterion | A | B | C |
| --- | --- | --- | --- |
| Semantic clarity | Simple until most edges need qualification | Domain roles explicit; evidence remains separate | Uniform source-claim discipline, greater abstraction |
| OWL compatibility | Feasible with disciplined resource patterns; shortcuts need semantics | Feasible without metamodeling if concept references are separated | Feasible for claim resources; described predicates do not automatically operate as OWL relations |
| SPARQL usability | Simple shortcuts, complicated authoritative routes | Predictable typed joins | Most queries unpack claims/roles and aggregate views |
| Implementation complexity | Low skeleton, medium/high safe full-core version | Medium, focused on required relation records | High: occurrence/proposition/view/claim lifecycle |
| Reasoning burden | Synchronize asserted/derived shortcuts | Limited optional inference, explicit derivations | Requires careful content/assertion boundary |
| Portability | Good with ordinary triples; dual-view contract required | Good with ordinary triples and explicit records | Good serialization portability; application claim semantics need documentation |
| Frozen-question fit | Covers all with substantial qualification | Covers all with bounded supplementary patterns | Covers all, with more generic machinery than currently justified |

**B approved as the M1 modelling direction at Checkpoint 1:** explicit association resources, distinct evidence occurrences, contextual mappings and query selections, plus separately qualified mechanism/indication/trial records. The following implementation recommendations remain proposals: use ordinary resource patterns as the initial portability baseline. Investigate a small PROV-O-style subset; do not freeze it yet. Reference MONDO identities with explicit concept/record separation and bounded path context. Begin with minimal semantic axioms and separately specified structural/application checks; do not select an OWL profile or stack by preference.

Why A is weaker for this scope: qualifications are required across the core, so optional statement nodes become nearly universal while shortcut consistency remains extra work. Why C is not the first choice: its general claim lifecycle is valuable but demands more identity and query machinery than seven bounded cases justify. Neither is scientifically rejected or inherently wrong. B incorporates source-assertion discipline where needed without treating all information as a generic proposition. No graph advantage, novelty or biomedical expert validation follows from this recommendation.

## 14. Open owner decisions and next task

The owner approved explicit disease–target association resources with individual evidence occurrences kept distinct from aggregates; original/source disease distinct from normalized disease; representable mapping context and ambiguity; direct/descendant-derived selection distinct from upstream normalization; mechanism distinct from indication; indication distinct from trial population/status; derived statements distinct from source assertions; representable evidence dependency/shared-source information; and provenance attachable at the appropriate record/claim level.

This approval does not freeze exact ontology classes/property names, namespace, provenance vocabulary, record identity/version rules, MONDO reference/import mechanics, missingness representation, named graphs, RDF-star, OWL profile, inference rules, SHACL shapes, reasoner or triple store. These remain open decisions. Source artifact acquisition, evaluation labels/metrics and clinical review gates are unchanged.

**Proposed next M1 task:** after separate authorization, write a conceptual model contract for approved Alternative B: record roles and identity/version boundaries; association/evidence/mapping/selection responsibilities; qualified mechanism/indication/population patterns; and traceability to Q01–Q07/R1–R14. Resolve the class-versus-concept-reference question explicitly. Specify a small list of intended entailments and structural/application checks in prose. Do not generate OWL, shapes, data instances or production queries until separately authorized.

## 15. Review basis and limits

Primary technical sources consulted: W3C OWL primer/profiles, n-ary modelling note, RDF 1.1 Concepts/Semantics, SPARQL 1.1 Query, PROV-O, SHACL and the current RDF 1.2 Concepts status page, linked at the relevant discussions above. The n-ary document is a modelling note, not a mandated architecture. No stack compatibility is claimed from reading specifications. Biomedical examples and all requirements come from the frozen local documents. The alternatives, matrices, complexity estimates and recommendation are project analysis, not external source conclusions. The owner has approved B's modelling direction only; A and C remain documented as considered alternatives.

Only this document is added. Frozen M0 decisions, questions, requirements and evidence are unchanged. The design-comparison work created no ontology/data files, shapes, namespaces, dependencies, database configuration, test suites or experiments. Checkpoint 1 authorizes a local documentation commit only; no push or next M1 task is authorized.
