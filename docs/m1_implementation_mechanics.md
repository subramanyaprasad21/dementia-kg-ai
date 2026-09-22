# M1 Task 005 — remaining implementation mechanics

**APPROVED — G01–G06 FOR INITIAL M1 AUDIT-DERIVED FIXTURE SCOPE. NO IMPLEMENTATION OR LIVE ACQUISITION AUTHORIZED BY THIS CHECKPOINT.**

Review baseline: `229540c Design and minimize M1 ontology schema`. The working tree was clean at the original proposal task entry; this correction pass starts with the mechanics proposal and its readiness cross-reference already pending. The owner explicitly approved the corrected G01–G06 package on 2026-09-22 (Asia/Kolkata). Section 9 records the approval and its limits. Recommendation/proposal wording in the investigation below is retained as history; within the initial audit-derived fixture scope, the corrected choices are now approved. Prior approved scientific and conceptual decisions remain unchanged. Authority: [project charter](project_charter.md), [conceptual contract](m1_conceptual_model_contract.md), [approved implementation readiness](m1_implementation_readiness.md), [schema investigation history](m1_schema_design.md), [frozen competency questions](competency_questions.md) and [source audit](source_audit.md).

The approved 20 local classes / 28 object properties (27 local plus prov:wasDerivedFrom) / 39 datatype properties remain unchanged. No new ontology term, biomedical capability, research objective or substantive OWL axiom is proposed. Mechanical profile names, validation rule IDs, literal codes, receipt keys and missingness tokens below are documentation/application contracts, not new RDF properties or vocabulary individuals. No namespace is provisioned and no project record identifiers, source fixtures, code, RDF, OWL or shapes are created. Synthetic receipt examples below are documentation calculations only.

## 1. Gate register and resolution order

| Gate | Already established | Previously undecided | Proposed decision / owner assumption |
| --- | --- | --- | --- |
| G01 Namespace | Local disease-reference records; exact manifest; no MONDO/PROV imports | Base IRI, prefixes, version convention, publication expectations | Repository-scoped HTTPS identifiers, separate schema/data paths; no institutional namespace or hosting claim. Owner accepts persistence responsibility and non-dereferenceable local-development IRIs. |
| G02 Identity/serialization | Source occurrence ≠ encounter; versioned descriptions; conservative identity; raw context preserved | Canonical encoding, digest, run IDs, collision handling, metadata placement | Versioned JCS/SHA-256 identity receipts; fixed record projections; append-only execution receipts; explicit collision quarantine. Owner approves the profile and mechanical metadata within existing fields. |
| G03 Enums | Twelve literal state fields; their conceptual distinctions; no concept individuals | Exact admissible strings, ownership, combinations and change rules | Close the twelve lists in section 4; retain existing proposed strings, clarify cross-field conditions. Unknown values are not silently coerced. |
| G04 Missingness | Sparse field-specific reasons; contextual owner; missing ≠ false | Finite expectedField catalogue, interpretation tokens, eligibility and severity | Closed retained-field list plus nine necessary interpretation tokens; distinguish reason recording from permission to omit structural identity. |
| G05 Acquisition | Two anchors and audited context; Q01–Q07 design cases; source-specific limits | Exact route, historical/live separation, retention/reuse and stop boundaries | Fixture-first use of committed audit observations; separately authorized bounded official recapture only. Historical raw artifact availability remains NOT YET VERIFIED. |
| G06 Validation | Declarations-only OWL; later structural/application checks; no global domain/range | Severity, dataset/profile boundaries, blocking versus qualification | Three severity levels and separate structural/answer gates; explicit rules in section 7. Honest source gaps can be structurally valid while limiting an answer. |

**Recommended approval order:** G05 acquisition boundary → G01 namespace → G03 enumerations → G04 missingness catalogue → G02 identity/serialization → G06 validation severity. Source scope determines identity inputs; enum/field spellings must be stable before hashing interpretations; severity then applies to the agreed representation. These decisions can be reviewed as one package. Approval of this package alone need not authorize implementation or external acquisition; those actions require explicit scope in the owner's next instruction.

## 2. G01 — namespace and prefix conventions

### Recommendation

Use the existing repository identity as the administrative base for private/local V1 development:

| Purpose | Proposed exact convention |
| --- | --- |
| Ontology identifier | `https://github.com/subramanyaprasad21/dementia-kg-ai/ontology` |
| Local schema prefix `dkg` | `https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#` |
| Local record prefix `dgkr` | `https://github.com/subramanyaprasad21/dementia-kg-ai/id/` |
| First ontology version identifier | `https://github.com/subramanyaprasad21/dementia-kg-ai/ontology/0.1.0` |
| Term local names | Exact approved case-sensitive manifest names; no renamed terms or aliases |
| Record suffix | Exact approved class local name, `/`, then full lowercase SHA-256 digest; generic source information slices use the reserved mechanical kind `SourceSlice` without declaring a class |

These are **proposed IRI strings only**, not created resources or a statement that GitHub serves ontology content at these paths. HTTP resolution of these proposed paths is not available/claimed. They intentionally avoid a fictitious Exeter-owned domain, new public hosting, unverified w3id registration and branch/commit-dependent term IRIs. The existing repository is owner-controlled according to the approved project history; its continued administration is an approval assumption. Private repository access can limit documentation visibility.

Use explicit prefixes rather than a default prefix: `dkg`, `dgkr`, `rdf`, `rdfs`, `owl`, `xsd`, `prov`. Standard bases: RDF syntax `http://www.w3.org/1999/02/22-rdf-syntax-ns#`; RDFS `http://www.w3.org/2000/01/rdf-schema#`; OWL `http://www.w3.org/2002/07/owl#`; XSD `http://www.w3.org/2001/XMLSchema#`; PROV `http://www.w3.org/ns/prov#`. Only prov:Entity and prov:wasDerivedFrom are reused semantically. No `mondo` prefix is needed in the initial schema: identifiers remain literal values in local references. No SKOS vocabulary or imports are introduced.

Use `owl:versionIRI` and descriptive version metadata only if later schema implementation is authorized; these are standard metadata, not additions to the local manifest. Version-specific ontology identifiers must not change term identifiers. A future term-meaning change requires review rather than silently repurposing a term. Do not encode snapshot releases or Git hashes into the namespace base. Data versions belong in record identity and provenance.

### Consequences / approval

Implementation receives deterministic IRI construction and prefix spelling. Provenance links can remain stable across file moves and Git branches. IRIs identify application records, not equivalence to external disease classes. The trade-off is no guaranteed web resolution and dependence on repository administration. A persistent public namespace such as w3id may be preferable before public release, but establishing one is a separate publication decision; no availability or registration is inferred. **Owner approval requested:** accept this development namespace and its persistence trade-off, or supply an owned persistent base before any records are minted.

## 3. G02 — identifier generation, serialization and collisions

### 3.1 Three different things to identify

1. **Referent:** Target, Drug, Publication or Study under a justified authority-qualified identifier. A changing label is a new description, not a new referent.
2. **Source/versioned description:** occurrence, association, mapping, disease reference, clinical record, snapshot or source slice. Source edition, actual content and context remain part of its identity.
3. **Encounter/result:** selection run, membership, inspection or derived result. A new live run is a new encounter; replaying an archived run reuses the recorded execution reference.

Hash equality is a mechanical lookup result, not owl:sameAs, clinical equality or independent evidence. The protocol must not hash a whole linked RDF subgraph, because cyclical links, ordering and unrelated enrichment would make IDs unstable.

### 3.2 Canonical identity receipt

Recommend profile **`m1-id-1`**. Each identified resource has a retained identity receipt with: profile identifier; kind (approved class name, or SourceSlice); origin route; named identity inputs; and relevant content-revision key. Receipts are technical acquisition/build metadata, not new ontology entities. They must later be exportable alongside the graph or recoverable through the existing artifactDescription/sourceLocator metadata. They are not created in this task.

Proposed mechanics:

- Canonicalize the receipt with **RFC 8785 JSON Canonicalization Scheme (JCS)**, then hash its UTF-8 bytes with SHA-256; use all 64 lowercase hexadecimal characters. No digest truncation, random salt, name-based guesses or counter suffix to hide collisions.
- Receipt inputs are strings, arrays, objects and explicit null only. Numbers/dates used as identity inputs are strings at declared lexical precision; avoid binary floating-point coercion of IDs/scores. Duplicate object keys, invalid Unicode and non-finite numbers are rejected.
- Preserve original source strings exactly: no Unicode normalization, trimming, case folding, underscore-to-colon rewriting or label correction. A separately justified authority-specific referent key may normalize only under the rules below; original values remain stored. JCS defines deterministic object serialization but does not normalize Unicode strings. [RFC 8785](https://www.rfc-editor.org/rfc/rfc8785)
- Sort set-valued receipt arrays by their canonical element bytes and eliminate identical elements only where the field is explicitly a set. Preserve order for ordered inputs. No sorting of clinical prose, ordered study arms or an ordered sequence merely for convenience.
- A schema-known but unavailable identity component is explicit null, accompanied by a missingness/uncertainty reason in the capture context. Empty string, empty set, null, not applicable and unknown are not silently interchangeable. A required identity input that cannot be established prevents a stable-ID claim, even if the incomplete record is retained for audit.
- Generated IRIs use G01's record base and kind/digest suffix. Do not create blank nodes for identity-bearing records. Prefix choice or RDF serialization order must not affect identity.

**Referent authority keys:** use governed authority tokens `MONDO`, `OMIM`, `ENSEMBL`, `CHEMBL`, `PMID`, `DOI`, `NCT` where actually justified. For ENSEMBL/CHEMBL/PMID/MONDO/OMIM identifiers, preserve the observed authority-qualified spelling and verify it against the source; do not infer protein/variant versions from a gene ID. For NCT, case-insensitive registry spelling may be compared via uppercase `NCT` followed by its observed digits, while preserving original spelling. For DOI, retain the exact known DOI identifier; URL-to-DOI extraction or case normalization is not automatic in first V1. No other authority is admitted without a source-route review; other original labels may remain unresolved source references. DiseaseConceptReference remains source-scoped even when authority and identifier match another description.

### 3.3 Raw artifacts, content revisions and source editions

Maintain two digests for different purposes in later acquisition receipts: raw artifact SHA-256 for exact byte integrity, and an atomic-record content revision for repeatable description identity. These are receipt fields in existing artifactDescription/sourceLocator metadata, not additions to the 39-property manifest.

For JSON source rows, use a **fixed, versioned record projection** for that source/type across every query route. Remove only the transport/query envelope, never evidence fields or qualifications. For initial Phase F, the exact projection is the committed audit-section byte projection in section 3.4b; it is not upstream JSON. For later Phase R, an exact field-path projection must be supplied with its separately authorized acquisition specification; an audit recipe alone is insufficient. Extensions require a new projection version. Do not compare different projection versions as identical records by assumption. Canonicalize the projected JSON by JCS only if its values are safely represented without numeric value loss. Retain raw bytes separately. Reject unsafe canonicalization rather than silently round a number. Source IDs are strings. For non-JSON source pages/reports, raw bytes of the preserved relevant artifact determine the captured description revision; formatting changes can create a new captured version without implying new biology.

A stable source edition is a known platform release or immutable source-record version. A content revision is not a claimed upstream release. For an unversioned mutable source without an established immutable version, scope the capture by its execution reference and mark edition unknown; do not assert cross-run occurrence identity from matching label/ID alone. Within a known edition and fixed projection, identical occurrence content through different queries reuses the same occurrence identity. Changes to a projection or genuinely changed content produce a new local description version and retained lineage, never a silent replacement.

**SourceSnapshot key:** provider/dataset, origin route, known edition or explicitly unknown capture boundary, artifact kind/projection, and content digest of the exact logical artifact described. Atomic source-record snapshots may be reused across queries; response-envelope snapshots are distinct acquisition artifacts. An EvidenceOccurrence's source identity uses its atomic snapshot/edition, not the query-response envelope or SelectionContext. SourceSnapshot may represent a small source slice; it does not imply possession of a full release. Membership preserves the encounter separately.

SourceScope and fixed projection must be preserved before hashing; never deduce them from the resulting digest. Audit-transcription artifacts use their committed project document/section as the actual provenance, not a fabricated live API payload. Their keys cannot collide with live-source keys because origin route is included.

### 3.4 Explicit identity inputs for all retained kinds

Common receipt metadata: profile, kind, origin route. “Source key” below means provider/dataset + known edition or capture boundary + fixed projection + atomic content revision/location; it does not include an unrelated retrieval mode.

| Kind | Identity input tuple beyond common metadata | Stability / collision guard |
| --- | --- | --- |
| SourceSnapshot | Source key for the exact artifact/slice described | Release label alone is insufficient; wrapper artifact distinct from atomic record artifact |
| Target / Drug / Publication / Study | Verified authority + referent ID + organism/context if needed to disambiguate the actual identifier | Only justified co-reference; changing descriptive metadata stays contextual; no publication-study merge |
| DiseaseConceptReference | Source key, source record/slice locator, role within that observation, exact original ID/label or explicit absence | Same MONDO ID across descriptions does not erase original-source context; source role is receipt metadata, not a new property |
| EvidenceOccurrence | Source key + sourceRecordIdentifier if supplied, otherwise stable artifact element locator | Exclude mapping IDs, selection anchors and retrieval run; original/mapped lexical fields already belong to source content revision |
| DiseaseTargetAssociation, source aggregate | Source key, source record locator, disease/target keys, source aggregate method/version, direct/inclusive view and relevant source filters | Local sample filters do not rewrite source aggregate identity; unknown method marked unknown |
| DiseaseTargetAssociation, project grouping | Execution reference, participant keys, method/version, sorted direct occurrence inputs, selection-context keys and scope | Includes originRole; all direct occurrence inputs are members; ancillary inputs stay contextRecord |
| MappingRecord | Source occurrence key, source/panel context, original input reference, observed destination(s), source method/authority when known, mapping observation version | Evidence occurrence does not hash this back-link, avoiding an identity cycle; a later review/candidate change is a new mapping observation description |
| SelectionContext | Execution reference, requested anchor, source edition/artifact boundary, selectionMode, fixed filterSpecification and method/version | Rerun ≠ replay. Different query settings within a run have separate contexts |
| SelectionMembership | Occurrence key + SelectionContext key | Path additions do not manufacture a second member; membership is immutable once its explanation bundle is frozen for release |
| HierarchyStep | Source key, source assertion locator, child/parent reference keys | Do not confuse normalized mapping with parent assertion |
| HierarchyPath | Exact ordered chain of step keys, audited source/version boundary and construction scope; execution reference if project-computed | Endpoints are derived; alternative chains remain separate paths |
| MechanismRecord | Source key, source record/element locator, drug/target keys, scoped source mechanism wording | Pair-only key would erase molecular/source distinctions |
| ClinicalIndicationRecord | Source key, source record/element locator, drug/disease keys and indication scope | No merge by drug/disease alone or transfer of studies between indications |
| StudyRecord | Underlying Study key + source key + dated report/arm scope and source record locator | Status/source changes create new descriptions, not a new Study |
| PopulationScope | StudyRecord/source report key, arm/cohort locator and exact description | Similar population wording across studies is not identity |
| DerivedStatement | Execution reference, operation/method version, sorted input artifact keys with directional roles preserved, selection context, output scope | Inputs immutable; same output text can arise from different inputs. Subject/comparator order retained when meaningful |
| InspectionRecord | Execution reference, actual reviewer identity/type, inspected source version/slice, aboutRecord, material/depth/scope and scoped result identity | Several claim-specific outcomes may share one inspection execution; no PMID-global judgment |
| MissingnessRecord | Affected owner key, expectedField token, observation context, reason and assessment scope | A later reason/resolution creates another observation; owner must not include MissingnessRecord links in its identity |
| SourceSlice (prov:Entity, no local class) | Parent artifact/source key, element/passage locator, actual scoped source wording | Can preserve panel-wide citations or source qualifications without a universal proposition class |

Inputs must form a dependency order: snapshot/artifact and referents → source descriptions and occurrences → mappings/clinical contexts → query contexts/memberships → path/review/derived/missingness records. Where a table role would create a back-reference, use the independently captured source locator/role in the receipt rather than hashing the downstream linked record; for example, StudyRecord's identity uses its source arm locator, not the PopulationScope key, and SourceSlice uses a parent artifact rather than the referencing occurrence. Do not recursively hash graph cycles.

**Reference comparison rule:** scoped DiseaseConceptReference IRIs can differ while referring to the same authority-qualified concept. Path continuity and query-anchor comparison must compare the verified identifierAuthority/externalIdentifier pair under the explicitly audited source/version compatibility, not require identical local hashes or match labels. Retain the original reference records and the basis for the comparison. A cross-source/version join is a documented navigation decision, never owl:sameAs or disease equivalence; absent compatibility evidence produces an unresolved explanation. This is essential for Q03–Q05 and prevents source-scoped identity from breaking a legitimate bounded path.

**Filter receipt rule:** filterSpecification stores a canonical JSON string for the exact executed request specification, using existing fields rather than new schema properties. Preserve the recorded query/recipe version, variables, target/disease identifiers, source filters, inclusion mode, sort/limit and pagination settings, including explicitly omitted/defaulted settings distinguished from supplied values. Source defaults must be identified from the pinned recipe or marked unknown; do not replace unknown defaults with invented values. The raw request text/route remains locatable in capture metadata. JCS canonicalizes this technical specification; it does not determine biomedical eligibility. Phase F audit transcriptions preserve only settings actually documented and cannot claim complete request reproducibility when the audit lacks them.

### 3.4a Exact initial receipt contract — proposed `m1-id-1`

This finite contract covers the retained kinds in Phase F, not arbitrary upstream JSON or a general identity service. It makes the conceptual tuples above executable without selecting software. All keys below are case-sensitive. Reject extra keys; do not silently infer defaults.

Every receipt has exactly five required keys: `profile` (literal `m1-id-1`), `kind` (table kind), `origin` (`referent`, `audit-transcription`, or `project-operation`), `inputs` (object with exactly the keys in the table below), and `contentRevision` (full lowercase SHA-256 string, or null only for referents and SelectionMembership). No top-level key is optional. Source descriptions use audit-transcription; computations/reviews/selections/missingness use project-operation; referents use referent. MappingRecord and HierarchyPath may use either audit-transcription or project-operation according to actual origin. Different origins are not interchangeable.

**Input types:** plain entries below are nonempty strings; `?` permits null; `[]S` is an unordered set of strings, sorted by UTF-8 bytes with exact duplicates removed; `[]O` is an ordered string array with repetitions preserved. Suffixes are table notation, not key spelling. Every listed key must occur, including nullable keys. All unspecified arrays are prohibited. Empty arrays mean a known empty collection; unknown collections are null only where `?` is shown. Unavailable, not-applicable and unresolved nullable inputs require an attributed reason in accompanying metadata; never encode a reason as a fabricated identifier. Required unavailable inputs prevent acceptance under this profile. An unverified source description may still be represented from the audit artifact; a missing upstream ID does not mean its audit locator is missing.

Keys ending `Key` and elements of key arrays contain full resource IRIs generated from already determined receipts, never prefix aliases. `snapshotKey` identifies the actual pinned audit section snapshot. `locator` is its exact entry locator specified below. `method` is the actual operation label, `methodVersion` its documented version (nullable only where marked); `scope` is nonempty explicit scope text. Scope wording is identity-bearing for descriptions, not a biomedical equivalence test. Execution references have exact spelling `batchLabel/ordinal`: batchLabel matches `[a-z][a-z0-9-]*`, ordinal is positive decimal without leading zero; labels are owner-allocated and never reused for a different batch. Replay preserves both. No distributed allocator is required for initial single-writer work.

| Kind / variant | Exact keys in inputs |
| --- | --- |
| SourceSnapshot | provider, dataset, edition, projection, locator, artifactDigest |
| Target / Drug / Publication / Study | authority, identifier, disambiguator? |
| DiseaseConceptReference | snapshotKey, locator, role, authority?, identifier?, label? |
| EvidenceOccurrence | snapshotKey, locator, sourceRecordId? |
| DiseaseTargetAssociation / source-aggregate | originRole, snapshotKey, locator, diseaseKey, targetKey, method?, methodVersion?, selectionMode?, filters? |
| DiseaseTargetAssociation / project-grouping | originRole, execution, diseaseKey, targetKey, method, methodVersion, occurrenceKeys[]S, selectionKeys[]S, scope |
| MappingRecord | snapshotKey, locator, occurrenceKey, panel?, inputKey?, destinationKeys[]S, candidateKeys[]S, method?, methodVersion?, execution? |
| SelectionContext | execution, anchorKey, snapshotKeys[]S, selectionMode, filters, method, methodVersion, scope |
| SelectionMembership | occurrenceKey, contextKey |
| HierarchyStep | snapshotKey, locator, childKey, parentKey |
| HierarchyPath | snapshotKeys[]S, stepKeys[]O, method, methodVersion?, scope, execution? |
| MechanismRecord | snapshotKey, locator, drugKey, targetKey |
| ClinicalIndicationRecord | snapshotKey, locator, drugKey, diseaseKey |
| StudyRecord | studyKey, snapshotKey, locator, arm?, sourceDate? |
| PopulationScope | studyRecordKey, locator, arm? |
| DerivedStatement | execution, method, methodVersion, inputKeys[]S, subjectKey, comparatorKey?, selectionKeys[]S, scope |
| InspectionRecord | execution, reviewer, reviewerType, inspectedKey, aboutKey, materialKind, inspectionDepth?, method, methodVersion, scope |
| MissingnessRecord | ownerKey, expectedField, observationKey, reason, scope |
| SourceSlice | snapshotKey, locator, scope |

For referents, disambiguator is null for the currently admitted authority identifiers; no ad-hoc label/organism disambiguation is allowed. If an identifier is not unique under its verified authority, stop that referent's acceptance rather than guess a key. Disease reference role is one of `original`, `normalized`, `project-anchor`, `hierarchy-endpoint`, `reported-participant`, `mapping-candidate`; these receipt roles distinguish observations and do not add ontology terms or prevent references in other graph roles. At least one of authority-qualified identifier or attributed label must be present. If neither is available, express the information gap rather than fabricate a disease reference.

For source aggregates originRole is `source-aggregate`; for project groupings it is `project-grouping`. Unknown source selection settings remain null with a reason. `filters` is the JCS string of a fixed request description with keys `recipe`, `variables`, `pagination`, `sort`, `limit`, `defaults`; each value is the exact documented string or null. A string may contain verbatim request/variable text, preserving booleans and numeric spellings without converting them into receipt booleans/numbers. Null is unknown, not an omitted executed default; an explicitly omitted setting is recorded as the string `omitted` with its documented default in `defaults`. Phase F records only what the audit establishes. This encoding identifies the documented request description, not undocumented historical request bytes.

For MappingRecord, source process uncertainty is nullable; a project revision requires execution and actual method/version. HierarchyPath requires execution and methodVersion for project construction; an audit transcription uses method `audit-transcription`, methodVersion `audit-section-v1`, execution null. InspectionRecord always identifies the present technical inspector and actual operation. An anonymously attributed historical judgment stays quoted audit content and is not promoted to a newly completed InspectionRecord with invented reviewer identity. Known empty mappings/candidate arrays are distinct from absence of knowledge; where the audit does not establish the destination inventory, the payload must retain that limitation and the arrays contain only explicitly documented destinations, never a completeness claim.

**Content revision and immutable payload:** for a SourceSnapshot, contentRevision equals artifactDigest. For referents and SelectionMembership it is null. For every other kind it is SHA-256 of the JCS canonical payload described next. Thus changed outcomes, mapping candidates, qualifications, source wording or claim-bearing values create a new description even when the conceptual tuple is otherwise unchanged. This replaces the underspecified phrases “scoped result identity” and “mapping observation version” with a reproducible payload revision.

The payload is an array of direct, owned assertions represented by objects with exactly `field`, `form`, `value`, `datatype`, `language`. All values are strings except null datatype/language: form is `iri` or `literal`; IRI values are full IRIs with datatype/language null; literals have their exact lexical string and either a full datatype IRI or a language tag (the other is null). `field` is an exact manifest property name, including `prov:wasDerivedFrom`. Sort assertions by their complete JCS UTF-8 bytes and remove identical assertions. Do not hash inverse links, unrelated incoming links, labels on referenced resources, or a recursively traversed graph. Include every owned source/claim assertion intended for the immutable description; metadata not asserted on that description is kept in its external receipt/ledger. Hashing these flat assertions is not RDF graph canonicalization. Payload creation follows the approved property owners; it does not authorize additional properties.

To avoid circularity, SourceSnapshot payload/receipt metadata is represented by its artifact receipt, not hashed graph links. MissingnessRecord observations are separate, not inverse links added to the affected payload. StudyRecord uses source arm wording, never the downstream PopulationScope key, in its receipt; its owned hasPopulationScope assertion is attached only in a released bundle after both identities are determined and excluded from StudyRecord's contentRevision. Likewise exclude EvidenceOccurrence.mappingContext from its contentRevision because MappingRecord already identifies its occurrence. These two deferred linkage families are preserved in the immutable released bundle and checked against the source locator and independently determined linked record receipts; they are not dropped from the graph. Revising a mapping/population explanation uses a new reviewed result/bundle, not an overwrite of the occurrence or source report. The release inventory records the SHA-256 of each complete serialized bundle separately from record IDs, so changes to deferred attachments are detectable. All other payload IRI dependencies must already be determined; a dependency cycle is rejected rather than resolved by iterative hashing.

SelectionMembership's identity-bearing payload is only selectedOccurrence and inSelectionContext. Freeze its initial inclusion classification/explanation in the released bundle, without using those attachments to generate another membership ID. Later explanation changes follow section 3.5. Referent label enrichment belongs to contextual source descriptions, not a new authority identifier. A changed source section, entry locator, projection, payload, or receipt input changes source-description identity; a new execution changes operation identity; reordering equivalent sets or Turtle output does neither. Separate capture descriptions never count as independent evidence solely because their digests differ.

### 3.4b Concrete Phase F projections

The initial source is the Git blob `docs/source_audit.md` at the full commit resolving `229540c`, not a reconstructed upstream JSON response. Resolve and retain the full commit before fixture creation. Projection **`audit-section-v1`** is the exact UTF-8 bytes from the beginning of the named heading line through the byte before the next heading of equal or higher level, or end-of-file. Preserve line endings and all wording. The SHA-256 of those bytes is artifactDigest. Snapshot provider is `project-audit`, dataset is `docs/source_audit.md`, edition is the full commit. Snapshot locator is `docs/source_audit.md#` followed by the exact heading text without Markdown heading markers. Entry locator is that locator plus `;lines=start-end`, with inclusive one-based line numbers relative to the section; repeated IDs are disambiguated by their actual line span, never encounter order. Multiple records from the same passage can share a locator; kind, role and payload distinguish them.

| Initially transcribed record material | Exact section heading(s) used as section projections |
| --- | --- |
| Association descriptions / fixed sample context | T3-T: ranked association sample; T3-X: fixed-universe cross-probe |
| Evidence occurrences and source-reported mappings | T3-E: direct evidence inventory; T4-S: original panel and mapping context; T4-C: clinical-precedence dependency |
| Hierarchy assertions and paths | T3-H: propagation diagnostic (separate from direct sample); T4-H: paths versus normalization |
| Mechanisms, indications, study descriptions and populations | T3-D: drug/mechanism and indication paths; T4-D: indication population and mechanism; T4-C: clinical-precedence dependency |
| Publication/source qualifications and inspection history | T3-R: publication/source tracing and provenance limits; T4-P: publication support and stopping points; T4-method: reproduction and depth |
| Disease reference labels/identifiers | Task 002A: exact candidate boundaries, or the same section as the record reporting the reference |

A row reports only its own pinned passage; qualifications elsewhere use additional SourceSlice/derivation context, not fabricated concatenated upstream records. Technical transcription, local selection, review and derivation are project operations whose method/scope and owned assertion payload are captured under section 3.4a. Phase F needs no live endpoint projection. Phase R is deliberately outside this initial profile: before separately authorized live acquisition, specify its exact response field paths, transport exclusions, edition/capture boundary and numeric handling as a versioned extension. Merely citing an old query recipe is insufficient for live deterministic identity. This is a future acquisition gate, not an unresolved Phase F implementation mechanic.

### 3.4c Small synthetic canonicalization examples

These are documentation-only synthetic receipts, not acquired records or minted project IRIs. Canonical bytes below have no trailing newline. The examples use only ASCII keys/strings, so their sorted compact JSON is also their JCS representation.

**A — referent**

```json
{"contentRevision":null,"inputs":{"authority":"NCT","disambiguator":null,"identifier":"NCT00000001"},"kind":"Study","origin":"referent","profile":"m1-id-1"}
```

SHA-256: `8a354adc22138db8c5adcd7d309b6fc7c381143363d6008420bcd74b712ad206`.

**B — same membership on replay**

```json
{"contentRevision":null,"inputs":{"contextKey":"urn:example:selection-1","occurrenceKey":"urn:example:occurrence-a"},"kind":"SelectionMembership","origin":"project-operation","profile":"m1-id-1"}
```

SHA-256: `2db83b31ae917bfb7ec3d6df3eafab4ee87dbc4c817ef478f4dd070bb5355608`.

**C — genuinely different selection**

```json
{"contentRevision":null,"inputs":{"contextKey":"urn:example:selection-2","occurrenceKey":"urn:example:occurrence-a"},"kind":"SelectionMembership","origin":"project-operation","profile":"m1-id-1"}
```

SHA-256: `159d35da5f34dc550b0911141710d68fffe2e117216063908d5d5bedf3825057`.

Reversing the input object key order in A yields exactly the same canonical bytes/digest. Replaying B or reviewing its explanation leaves B unchanged; only an actual new selection with the different context in C changes membership identity. Set input `["urn:example:b","urn:example:a","urn:example:a"]` canonicalizes to `["urn:example:a","urn:example:b"]` before receipt serialization; that transformation is forbidden for ordered stepKeys. Changing a description payload produces a new contentRevision; do not truncate a digest or equate different hashes with independent studies. These small examples verify encoding behavior, not biomedical facts or a complete future implementation.

### 3.5 Execution references, changes and collision policy

Recommend an append-only capture ledger maintained when acquisition/inspection is later authorized. A human-approved batch label plus an allocated monotonically increasing execution ordinal forms executionReference. Allocation is serialized under a lock; parallel work uses distinct preallocated batch labels/ordinals. No random UUID strategy. An archived replay reuses the archived reference; a new live retrieval or inspection allocates a new one. Commit/retain the original ledger under the acquisition policy before calling the output reproducible. This ledger is future technical metadata, not another ontology class or an artifact created now.

A builder must compare canonical receipt bytes when an IRI already exists:

- Same receipt and same immutable record payload: idempotent reuse.
- Different receipt under the same hash: **blocking collision**, quarantine both; never auto-merge or append a random suffix.
- Same identity receipt but conflicting immutable payload: **blocking identity-profile defect or source-version conflict**, not permission to overwrite. Revise source/version boundaries under review.
- Missing proof of identity: retain a capture-local description with uncertainty; do not claim canonical co-reference or independent evidence.

Releases/content/mapping changes generate new versioned descriptions; reruns generate new encounters; deeper inspection generates a new InspectionRecord; changed trial status generates a new StudyRecord. Enrichment that only adds a retrieval encounter can link to an immutable source occurrence without changing it. Revising an explanation does not imply another retrieval or selection operation. Preserve the original EvidenceOccurrence, SelectionContext and SelectionMembership identities and their released payloads. Record the later explanation as a new DerivedStatement with subjectRecord identifying that membership and prov:wasDerivedFrom identifying the inspected path/source inputs; use an InspectionRecord for its review where applicable. Do not append a revised justificationPath to an immutable released membership. The original explanation remains inspectable, and the later result explicitly states what it revises. Create a new SelectionContext only when a new selection operation actually occurred (including an actual new local selection over archived inputs, clearly distinguished from live retrieval). No class/property change is needed.

### 3.6 RDF serialization proposal and consequences

For a later authorized first implementation, recommend Turtle, UTF-8 without BOM, LF line endings and final newline; explicit prefixes G01; deterministic ordering by full subject IRI, predicate IRI and object lexical/type/language tuple. No anonymous identity-bearing records, relative IRIs, implicit local timezone conversion or ontology imports. Literal enum codes use xsd:string, scores xsd:decimal, dates their actual supported precision (xsd:date or dateTime); known timestamps with offsets are stored in UTC while original source precision/wording remains in the source artifact. Do not invent midnight for date-only values. Labels/source text may preserve actual language tags; IDs/codes do not.

This is an output convention, not RDF graph canonicalization; record IDs come from identity receipts, not serialized triple order. Reasoning/validation results are not assumed from byte equality. The exact recipe/capture receipt and output serialization profile are retained in artifactDescription or linked sourceLocator information, using the existing manifest.

**Consequences:** reproducible IDs across replay and query ordering; more explicit handling of source editions/projections; source text retained without guessing equivalence. Immutable version discipline costs extra descriptions when provenance is uncertain. **Owner assumptions:** approve `m1-id-1`, SHA-256/JCS, fixed projection and artifact integrity receipts, ledger allocation and conservative unknown-version behavior. No implementation library is selected or installed. The source projection's actual endpoint compatibility and historical artifact availability remain to be checked during separately authorized acquisition.

## 4. G03 — exact enumeration catalogue

Already approved: twelve literal-state dimensions, no concept individuals, and the candidate spellings in readiness section 5. Recommendation **`m1-enum-1`** freezes those spellings without adding or removing a value. Lists are closed and case-sensitive; xsd:string, lowercase hyphenated tokens, no whitespace padding, aliases or implicit translation. Each applicable record uses one value per state dimension; distinct scoped conclusions use separate records. A missing state is not silently converted to a positive or unknown state.

| Field / owner | Exact allowed tokens | Frozen basis |
| --- | --- | --- |
| originRole / DiseaseTargetAssociation | source-aggregate, project-grouping | R1,12; Q01–06 |
| selectionMode / SelectionContext and scoped association | direct-only, descendant-inclusive | R4–5; Q04 |
| inclusionKind / SelectionMembership | exact-anchor, descendant-selected, unresolved | R4–5; Q04 |
| mappingStatus / MappingRecord | input-only, validity-unreviewed, unresolved, reviewed-with-limits | R2–3,5; Q03,05 |
| inspectionDepth / InspectionRecord | metadata-only, selected-passages, full-relevant-material | R8; Q01,06–07 |
| materialKind / InspectionRecord | metadata, abstract, full-text-source, registry-page, source-page | R8; Q01–07 |
| accessOutcome / InspectionRecord | accessible, partially-accessible, inaccessible, not-attempted | R8–9; Q01,05–07 |
| interpretationOutcome / InspectionRecord | source-record-supported, not-established-by-bundle, mapping-ambiguous, access-limited, not-assessed | R14; Q01–07 |
| missingnessReason / MissingnessRecord | source-omission, not-retrieved, inaccessible, not-applicable, not-inspected, unresolved, reason-unknown | R9,14; Q01,05–07 |
| dependencyStatus / DerivedStatement | shared-source-established, dependence-established, possible-dependence, independence-assessed-with-limits, unresolved | R13; Q02 |
| completenessStatus / bounded information/result resource | complete-for-declared-scope, partial, unknown | R9,12,14; Q01–07 |
| reviewerType / InspectionRecord | human-technical-review, software-assisted-technical-review, automated-check | R8,14; Q01–07 |

### Operational definitions and compatibility rules

- originRole describes the association's reported source aggregate versus project grouping. A local transcription of a source aggregate is still an attributed report of an aggregate; its capture route and actual project-audit provenance are explicit, never a claim that a live source was acquired.
- selectionMode is query/view specification. inclusionKind is per-member classification. An inclusive query may return exact-anchor members. direct-only plus descendant-selected is a violation. unresolved classification requires rationale/limitation, never a guessed path.
- mappingStatus input-only requires an observed original input and no asserted reported destination; candidate destinations may remain proposals if explicitly documented. validity-unreviewed means assignment validity has not been reviewed. unresolved means available evidence cannot settle it. reviewed-with-limits requires a scoped InspectionRecord; it does not mean equivalent concepts. A mapping lacking both input and observed/candidate destination is not made meaningful by a status alone.
- inspectionDepth metadata-only concerns metadata actually inspected. selected-passages means only selected content, with scopeText locating it. full-relevant-material means all of the explicitly identified material was inspected, not all potentially relevant literature. For materialKind abstract, this is a full abstract, not a full paper. Full-text-source requires scopeText clarifying whether the complete document or only a selected passage was inspected.
- For accessOutcome inaccessible or not-attempted, omit inspectionDepth for that content and use interpretationOutcome access-limited or not-assessed as applicable. If metadata is available separately, give it a separate metadata inspection rather than assigning positive content depth to an inaccessible body. partially-accessible permits metadata-only/selected-passages; claiming full-relevant-material requires separately scoped accessible material and its own record.
- source-record-supported means the inspected source supports the stated bounded record claim at actual depth. It is not clinical truth. not-established-by-bundle is not false; mapping-ambiguous does not mean source error; access-limited does not mean unsupported biology. not-assessed permits successful access without completed interpretation.
- missingnessReason source-omission applies only to the inspected representation; not-retrieved means acquisition was not done; inaccessible requires an actual recorded access limitation; not-applicable requires a scope rationale; not-inspected means no relevant content review; unresolved means evidence exists but does not settle the value/meaning; reason-unknown avoids invented explanations.
- shared-source-established means an identified common source; dependence-established additionally needs the documented dependence basis relevant to the claim; possible-dependence is a hypothesis with stated basis; independence-assessed-with-limits requires actual inspected evidence about study/input independence and cannot be generated from different IDs or absent shared links; unresolved remains unresolved. No M1 fixture acquires independent adjudication merely by using a code.
- complete-for-declared-scope requires a declared bounded operation, verified pagination/result extent where relevant and no missing required inputs for that operation. It does not mean complete disease knowledge. partial and unknown preserve incomplete/undetermined extent.
- human-technical-review means an actual identified human inspected the material without the software-assisted category being needed; software-assisted-technical-review means an identified human actually reviewed assisted work; automated-check covers actual machine-only checks, including AI-assisted technical processing without independent human content review. Owner approval of a design document alone is not human adjudication of its biomedical sources. No expert-review code is introduced.

Each record's origin, scope and rationale govern the interpretation; the tokens themselves never prove it. No fallback “other” is added to a closed state list. An unexpected source status is preserved in sourceText/trialStatusText; it is not forced into an internal enum. Unknown internal codes fail validation and require a versioned catalogue proposal. An added enum value would require explicit owner review, not silently change the 20/28/39 manifest.

**Consequences:** later constraints can enforce exact lexical values and combinations; exports retain qualification without extra nodes. Interpretation remains source-bound. **Owner approval requested:** freeze these lists and operational definitions as `m1-enum-1`; particularly confirm the reviewer-type and access/depth distinctions. No substantive inference or credential claim follows.

## 5. G04 — exact missingness-field catalogue

Already established: MissingnessRecord with aboutRecord, expectedField, missingnessReason, observationContext/rationale; use only interpretation-relevant gaps. Recommendation **`m1-missing-1`** uses a closed list. The value is an xsd:string token, not an ontology property reference or new property. Two namespaces of literal tokens are admitted: `field:` for an existing manifest field and `requirement:` for an interpretation requirement that is not a single persisted field.

### 5.1 Ordinary field tokens — exhaustive

The following are the only `field:` tokens. Ownership follows the approved signature for that field. Presence of a missingness reason does not waive a structurally mandatory field. Fields irrelevant to the owner/question must not generate missingness nodes.

| Field family | Exact allowed expectedField tokens |
| --- | --- |
| Object fields | `field:inSnapshot`, `field:contextRecord`, `field:reportedEvidence`, `field:mappingContext`, `field:mappingInput`, `field:reportedDestination`, `field:candidateDestination`, `field:queryAnchor` |
| Object fields | `field:selectedOccurrence`, `field:inSelectionContext`, `field:justificationPath`, `field:pathStep`, `field:childReference`, `field:parentReference`, `field:citesPublication`, `field:refersToStudy` |
| Object fields | `field:indicationStudyRecord`, `field:hasPopulationScope`, `field:subjectRecord`, `field:comparatorRecord`, `field:sharedInput`, `field:inspectedRecord`, `field:aboutRecord`, `field:observationContext` |
| Object fields | `field:prov:wasDerivedFrom`, `field:hasTarget`, `field:hasDrug`, `field:hasDiseaseReference` |
| Datatype fields | `field:externalIdentifier`, `field:identifierAuthority`, `field:sourceLabel`, `field:sourceRecordIdentifier`, `field:sourceLocator`, `field:sourceAuthority`, `field:snapshotVersion`, `field:artifactDescription` |
| Datatype fields | `field:observedAt`, `field:recordVersion`, `field:scopeText`, `field:evidenceSourceType`, `field:aggregateScore`, `field:scoreDefinition`, `field:filterSpecification`, `field:operationMethod` |
| Datatype fields | `field:methodVersion`, `field:limitationText`, `field:trialPhaseText`, `field:trialStatusText`, `field:statusDate`, `field:expectedField`, `field:rationale`, `field:resultSummary` |
| Datatype fields | `field:originRole`, `field:selectionMode`, `field:inclusionKind`, `field:mappingStatus`, `field:inspectionDepth`, `field:materialKind`, `field:accessOutcome`, `field:interpretationOutcome` |
| Datatype fields | `field:missingnessReason`, `field:dependencyStatus`, `field:completenessStatus`, `field:reviewerType`, `field:sourceText`, `field:reviewerIdentifier`, `field:executionReference` |

There are exactly **67 ordinary field tokens**: 28 object fields, including `field:prov:wasDerivedFrom`, and 39 datatype fields. Prefix text in that token is literal catalogue spelling; it does not depend on a serializer's prefix alias. `field:expectedField` and other MissingnessRecord structural fields may appear in validator reports but must not trigger recursive MissingnessRecord creation for malformed MissingnessRecords. Report those errors directly. Mandatory workflow metadata such as an absent executionReference is a validation defect, not an acceptable source-omission exception.

### 5.2 Composite interpretation tokens — exhaustive

| Exact token | Permitted aboutRecord owner | Meaning and reason for not using only an ordinary field | Q/R basis |
| --- | --- | --- | --- |
| requirement:original-disease-identity | EvidenceOccurrence | No available source identity through any mapping-input record. Prefer field:mappingInput on an existing MappingRecord; do not duplicate both reports for the same gap. | Q01,03,05; R2,9 |
| requirement:mapping-validity | MappingRecord | Destination exists, but validity/equivalence cannot be established. Do not falsely mark the destination absent. | Q05; R3,9 |
| requirement:source-content-access | InspectionRecord or scoped source information resource | Required source body cannot be accessed; locator/metadata may still exist. | Q01,05–07; R7–9 |
| requirement:extraction-span | EvidenceOccurrence | Specific text-mining passage is unavailable/unverified even when a paper is cited. | Q01; R7–9 |
| requirement:claim-specific-support | EvidenceOccurrence, MechanismRecord, ClinicalIndicationRecord or scoped source claim description | Citation/list exists but inspected support for the particular claim is missing or unresolved. | Q01,03,06–07; R7–9,14 |
| requirement:hierarchy-path-completeness | HierarchyPath or SelectionMembership | Some steps exist but the required complete chain is unavailable. Not the same as missing all pathStep values. | Q04; R4–5,9 |
| requirement:retrieval-completeness | SelectionContext or source-list description | Some returned records exist but the bounded result extent is incomplete/unknown. | Q02,04,06; R9,14 |
| requirement:molecular-target-detail | MechanismRecord | Gene-indexed relation exists but required molecular-form/action qualification is unavailable. | Q06; R10,14 |
| requirement:regulatory-label-review | ClinicalIndicationRecord or scoped approval-source description | Indication/approval wording exists but product-label review is absent. No positive regulatory capability is added. | Q06; R11,14 |

Total permitted expectedField vocabulary: **76 strings** (67 + 9). No wildcard token, free-text field name, removed schema name or undefined `requirement:` value is accepted. Explain details in rationale and limitationText, not by minting a new missingness token. This catalogue is application metadata, not 76 ontology terms.

### 5.3 Creation and resolution rules

Do not duplicate an existing scoped record that already adequately captures the same information gap, observation basis and consequence for the question. Reuse/reference that record in the explanation instead. One inaccessible source must not automatically generate access, extraction-span and claim-support MissingnessRecords merely because several downstream interpretations depend on it. Separate records require distinct gaps or observation bases that the existing record does not adequately express; token availability alone is not justification. Preserve all 76 permitted tokens.

Create a MissingnessRecord only if (a) a frozen question or its required provenance depends on the information, (b) the supplied source/inspection cannot provide it at that stage, and (c) the owner and observation basis are identified. Structural defects can be diagnosed without converting them into normal source gaps. Use one owner + token + observation + reason assessment per record; separate times/reasons remain separate observations.

All seven reasons from G03 are available, but require a truthful basis: source-omission requires inspection of that exact source representation; inaccessible requires an access attempt or documented access restriction; not-applicable requires a concrete scope rationale; unresolved needs the ambiguous evidence; reason-unknown is used only when the reason is itself unknown. A missingness record never supplies an absent field and never asserts biological negation.

Do not create MissingnessRecords for missing optional scores when the question does not use scoring, unused regulatory fields, absent study links not required by a claim, or ordinary empty candidate lists. Source identity on an evidence record is conditionally absent; inability to locate the source artifact at all can block fixture provenance. Similarly an incomplete hierarchy is a permissible source limit but blocks claiming that the full path was demonstrated.

**Consequences:** later validators and answer logic can distinguish inaccessible text from absent citations and ambiguous validity from absent destinations. This avoids recursive null-node proliferation and supports reproducible abstention reasons. **Owner approval requested:** adopt the finite 76-token catalogue, applicability rules and no-waiver principle; approve the nine interpretation tokens as values of existing expectedField, not new schema elements.

## 6. G05 — source-acquisition boundaries

### Established versus still unverified

The charter and source audit authorize the bounded scientific scope, not a frozen raw corpus. OT 26.06 and Mondo 2026-09-01 are **audited historical observations**, not proof that their original responses were archived. Exact original upstream panel snapshots, mapping algorithms, publication bodies and some access rights remain unverified where the audit says so. This task checks official technical documentation only; it does not acquire biomedical records or resolve historical source ambiguity.

### Recommended phases and exact finite boundary

**Phase F — first design fixtures, after separate implementation authorization:** transcribe only the mandatory Q01–Q07 slots and A–E limits from documents pinned at commit 229540c. Preserve the full evidence identifiers and source recipes from source_audit.md, not shortened display prefixes. The actual acquired artifact is the committed project audit text. sourceAuthority identifies the project audit, sourceLocator identifies commit/file/section, and sourceText/scopeText distinguish a recorded OT/registry observation from a newly fetched source response. Such fixtures test representability and verification behavior; they do not demonstrate fresh source reproduction or biomedical truth. Do not backdate their new creation/inspection dates to the audit dates. Represent those earlier dates only as attributed audit content.

**Phase R — optional bounded recapture, only with explicit acquisition authorization:** use official single-entity/record routes for exactly the same frozen slots. Capture request/variables, returned release metadata, projected source row, actual retrieval date, completeness, raw-body digest, projection version and permitted retention/reuse. An endpoint's current data must not be labelled OT 26.06 or Mondo 2026-09-01 unless that exact edition is established. If the historical edition cannot be retrieved, keep Phase F fixtures and label historical live reproduction unavailable; do not silently substitute current responses. New versions may be separate diagnostic material only after owner approval, never overwrite historical expectations.

| Source route | Permitted content in a later authorized capture | Explicit boundary / unresolved part |
| --- | --- | --- |
| Committed project audit | Q01–Q07 required slots, original dates, full IDs, reported query settings/paths and inspection limits | Not raw upstream evidence or proof of historical response completeness; no synthesis of omitted values |
| Open Targets official GraphQL/single-entity exports | Named AD/FTD associations and evidence rows; their exact target/drug metadata; mechanisms/indications/report links required by the seven questions | No full target ranking refresh, bulk Parquet, extra diseases or all evidence for all targets. Freeze a consistent record projection per source/type. Historical 26.06 capture availability NOT YET VERIFIED |
| MONDO/OLS term records | Two anchors and exactly Pick, semantic dementia, bvFTD, AD1, early-onset autosomal dominant AD, familial AD in their audited roles; explicitly audited consecutive parent steps only | No ontology download/import or closure. Provider/version of each step stays explicit. Historical individual-term availability NOT YET VERIFIED |
| Genomics England PanelApp | Named panel/gene records and their actual citation/xref context for panels 265, 474 and 540 where required | No panel-wide corpus, no invented per-citation phenotype adjudication; exact historical snapshots/redistribution route require verification |
| ClinicalTrials.gov official study records | nct00594737 and nct03658135 study/report metadata, original population/design/status and available version history | No participant-level data, trial database dump, efficacy upgrade or extrapolation from phase/status |
| Publication metadata and already cited sources | Only the frozen Q01–Q07 PMIDs/locators and specifically required passages if accessible and permitted | Metadata/citation availability does not license full text. No paywall/access bypass, bulk full-text collection or upgrading old inspection depth |
| OMIM / other identifiers | Retain existing source-reported IDs/labels and the recorded access limits | No independent OMIM acquisition or canonical mapping repair approved by this proposal |

The finite item allowlist is defined by the current core question sections, not every historical sample in source_audit.md. A new item must be required to complete an already named slot and explicitly reviewed before adding it; related-work examples and parked LBD cases are excluded. No HPO, pathway, process, phenotype, embedding, model or agent acquisition.

Proposed operational stop budget for Phase R: at most **100 read-only requests and 10 MiB of uncompressed response bodies per owner-approved capture batch**, and no bulk files. These are protective batch ceilings, not a definition of scientific completeness or a claim they suffice for every endpoint. A required response or pagination sequence exceeding the ceiling stops with incomplete extent and an owner-visible explanation; do not trim silently and report a complete list. No paid service, large cloud query or automatic retry loop is authorized. Captures should use named IDs and stop when the required slot is satisfied; list-wide absence for Q06 requires complete inspected extent within the approved boundary.

**Budget accounting:** count every outbound attempt, including retries, redirect follow-ups and unsuccessful requests, against the same batch's 100-request allowance. Count all uncompressed response-body bytes actually received/decoded, including error and redirect bodies, against 10 MiB (10,485,760 bytes); a failed request with no body contributes zero bytes but still consumes a request. Metadata requests and pagination also count. Do not issue the next request when the request allowance is exhausted. Enforce the byte allowance while reading; stop a response at the boundary and identify it as truncated/unusable as a complete artifact. Record any unavoidable transport-buffer overrun explicitly; do not conceal it or continue capture. Reaching a limit causes a compliant stop, a recorded request/byte total, affected slots and incomplete extent, and an owner-visible report. No automatic reset, relabelled batch, resume, retry or subdivision may circumvent the ceiling. Continuation requires explicit owner authorization of an additional budget. Scientific completeness is checked separately even when the batch stays below both limits.

### Permissions and provenance receipts

For every captured artifact, retain route/URL, provider, request/projection version, response date, edition if available, record locator, exact content/byte digests, relevant licence evidence and permitted retention/publication category. Recommend three explicit receipt dispositions: local-retention-permitted, metadata-or-locator-only, pending-rights-review. These are capture-policy metadata, not ontology enum fields. No source material is automatically staged in Git; redistribution is a distinct decision even for a private repository.

Official OT documentation recommends its API/web interface for single entities or associations and separate download routes for systematic work. Its licence page marks Platform data CC0 and lists separate source licences; that does not independently license a publisher's full text or a separately acquired upstream distribution. [OT data access](https://platform-docs.opentargets.org/data-access), [OT licence](https://platform-docs.opentargets.org/licence). Preserve attribution and distribution route regardless. Mondo's audited CC BY requirements remain recorded in source_audit.md; direct artifact reuse must retain applicable attribution/licence/change information. A current artifact-specific permission finding is not inferred from an old audit entry.

If a raw artifact cannot be retained lawfully, do not claim byte-for-byte public reproducibility of it. Retain allowed locators/metadata and inspectability limits; future sharing uses only allowed material. Exact retention rights and availability for still-unacquired artifacts remain **NOT YET VERIFIED** and are per-artifact stop gates, not a reason to pretend the schema is missing a class.

**Consequences:** first fixtures are reproducible as project-audit transcriptions; they are not independently sourced validation data. Live recapture creates a separately attributable version without contaminating the historical fixture. Provenance captures how much can actually be reproduced. **Owner approval requested:** Phase F first, Phase R separately authorized; the allowlist, batch ceilings, retention policy and no-silent-version-substitution rule. No acquisition takes place under this documentation task.

## 7. G06 — validation severity and acceptance policy

### Established / recommendation

Declarations-only OWL and no global local domain/range remain approved. OWL consistency does not check required fields. Recommend **`m1-validation-1`**, separating schema-build acceptance, source-record usability, and claim-level answer acceptance. Severity is not a biomedical confidence score.

Use the three standard SHACL severity concepts later: Violation, Warning and Info. SHACL results and application policy must remain distinct; do not assume a Warning automatically makes a validation report conformant. The standard conformance result depends on validation results; the project may additionally report an explicitly named acceptance status with its own policy, without changing the raw report. [SHACL specification](https://www.w3.org/TR/shacl/)

- **Violation:** blocks affected schema/record/fixture acceptance or the proposed answer claim. Preserve quarantined source data for audit where permitted; do not repair by fabrication. A source defect need not invalidate unrelated records.
- **Warning:** honest limitation or uncertain linkage; structurally valid qualified records may be accepted. The limitation can still block a particular requested assertion. An unqualified answer ignoring it becomes a separate violation.
- **Info:** documented expected condition with no acceptance block; never proof of biological truth.

A declaration file is accepted only if its syntax, exact manifest and prohibited-axiom checks pass. A fixture bundle can be structurally accepted with expected warnings, while its answer rubric requires qualification/abstention. The first positive and negative fixtures must declare expected warning/outcome pairs so that an always-abstain system cannot pass as successful.

### Precedence and verification responsibilities

- **V15 / V24 / V05:** an incompletely attributed historical judgment may remain quoted, qualified audit material. A new completed project judgment requires actual reviewer identity, method and required execution receipt. Cautious wording does not waive those requirements: V24 blocks acceptance as a completed reproducible review; V05 additionally applies to missing/conflicting identity receipts. Do not invent attribution to avoid a failure (V06). A source-unsupported claim also invokes V08.
- **V03 / V07 / V22:** mandatory local structure takes precedence. Upstream missing values receive warnings only where the approved record signature permits absence and alternative traceability/qualification is present. Missingness never satisfies a required participant or execution identity.
- **V09 / V11 / V10 / V12:** honest path/retrieval incompleteness is a warning on retained material. Misrepresenting that material as a correct complete path or exhaustive result violates claim acceptance. A malformed path cannot be used as a valid complete path merely by adding a general limitation.
- **V04 / V19:** lexical membership and allowed state combinations are V04; whether an otherwise valid missingness reason actually applies to this owner/gap is V19. Report one primary diagnostic with secondary rule references for a shared failure; do not inflate failure counts.
- **V25:** compliant stopping at the acquisition ceiling is not a violation. Record operational stop information and V11 where results are incomplete. Unauthorized continuation, concealed truncation/release mixing or permissions bypass violates V25; claiming complete results additionally invokes V12. Report transport overrun and stop immediately rather than silently expand the allowance.

| Verification responsibility | M1 scope and relevant rules |
| --- | --- |
| Automatically testable structural/lexical checks | V01–V05, structural parts of V08–V10, V19–V22, V24, V27: parser, manifest, finite signatures/codes, receipt bytes/digests, required metadata and explicit graph/path checks. A required provenance link being present does not prove it truthful. V25 counters/allowlist checks are future acquisition controls, not ontology shapes. |
| Controlled-fixture/application evaluation | V06–V18, V23–V26 where represented: compare fixture expectations for attribution, qualifications, completeness, shared inputs and forbidden upgrades; verify positive and negative outcomes. V20 replay and optional-value cases are positive controls. Explicit machine-readable violations can be detected, but arbitrary prose or unstated source facts cannot be comprehensively validated. |
| Manual provenance or biomedical judgment | Truth of source attribution/depth (V06/V08/V14/V15), mapping validity and cross-version compatibility (V09/V13), actual independence (V16/V17), claim-specific clinical/score interpretation (V18/V23), and artifact permissions/history (V25/V26). Technical source tracing is not biomedical expert adjudication; an unavailable or unqualified review leaves the judgment unresolved. |

These responsibilities overlap intentionally: a shape can check a reviewer's field, a fixture can check attribution behavior, and a reviewer must assess its truth. SHACL cannot establish biomedical truth, evidence independence, or completeness of unobserved upstream material. M1 controlled design cases are neither held-out evaluation nor independent confirmation of their underlying audit. No automatic general-purpose biomedical judge or additional research objective is implied.

### Exact initial rule catalogue

Rule IDs below are validator/application labels, not ontology terms. A validation report must identify rule, subject, field/requirement, severity, profile version and affected claim/bundle. Reports do not add classes/properties to the graph.

| Rule | Condition | Severity / effect | Layer / Q–R basis |
| --- | --- | --- | --- |
| V01 | Malformed RDF, illegal IRI/literal or undeclared local term | Violation; block schema/bundle | Parser/schema; all |
| V02 | Manifest drift, import, forbidden axiom or unauthorized substantive entailment | Violation; block schema | Schema audit; R1–14 |
| V03 | Wrong record role, wrong participant kind or absent mandatory structural participant/context | Violation; block affected record as usable | Later SHACL/ingestion; R1,4–5,10–11 |
| V04 | Invalid enum/missingness token, lexical padding/case error or contradictory state combination | Violation; no silent coercion | Later SHACL/application; R3–5,8–9,13–14 |
| V05 | Hash collision, conflicting immutable payload under same key, missing required identity receipt, execution reference reused for distinct live runs | Violation; quarantine identity conflict | Ingestion/identity; R6,12–13 |
| V06 | Fabricated source ID/version/locator, reviewer identity/depth or unsupported mapping repair | Violation; reject asserted provenance/claim | Ingestion/review; R2–3,6–9 |
| V07 | Source omits original disease, source record ID, locator or version; relevant reason and alternate traceability are truthful | Warning; retain qualified record, no invented value | Source-specific; Q01,05–06; R2,7,9 |
| V08 | Source artifact cannot be traced at all for a purported source-supported claim | Violation for that claim; artifact can remain explicitly unverified | Provenance/application; R6–7,14 |
| V09 | Path incomplete or version compatibility unresolved and honestly marked partial/unknown | Warning; block complete-path claim until resolved | Q04; R4–5,9 |
| V10 | Cyclic/disconnected/wrong-endpoint path represented as complete or claimed as correct | Violation; block path claim | Structural/application; Q04 |
| V11 | Retrieval partial/unknown, declared as such | Warning; no list-wide absence or exhaustive comparison | Q02,04,06; R9,14 |
| V12 | Claim of complete result or absence without proven declared result extent | Violation for claim | Application; Q02,04,06 |
| V13 | Mapping ambiguous or source process unknown, with reported destination preserved | Warning; requires qualification, no canonical repair | Q03,05; R3,5,9 |
| V14 | Source inaccessible/not inspected or extraction span unavailable, truthfully recorded | Warning; allow access-limited/not-assessed outcome | Q01,05–07; R8–9 |
| V15 | Missing reviewer identity/method for a completed technical judgment | Warning for explicitly qualified historical audit attribution only; new project judgment fails required review/reproducibility acceptance under V24 (V05 for identity defects); V06/V08 apply to fabricated or unsupported attribution | Q01–07; R8,14 |
| V16 | Known shared trial/publication or documented dependence represented accurately | Info; the dependency fact is expected, not a defective record | Q02; R13 |
| V17 | Reused/shared evidence asserted as independent, or absent links used to prove independence | Violation for claim | Q02; R13–14 |
| V18 | Mechanism→indication, indication→efficacy, phase→completion, termination→efficacy failure, unrestricted approval, or parent-directness upgrade | Violation for claim | Q03–04,06–07; R4–5,10–11,14 |
| V19 | Missingness reason is not applicable to the owner/gap, not-applicable lacks rationale, or missingness is used to waive mandatory structure | Violation; block affected record's structural acceptance | R9,14 |
| V20 | Valid empty candidate list, absent unused optional score or matching immutable record reused during replay | Info, generally no MissingnessRecord needed | R3,9,13 |
| V21 | Trial phase/status/date owner mismatch, or invented time precision | Violation; block faulty description | Q02,07; R11 |
| V22 | Known phase/status lacks required source date/context and is honestly qualified | Warning; prohibit current-status/general efficacy claim | Q02,07; R11,14 |
| V23 | Source score lacks an inspectable definition/component context | Warning if retained uninterpreted; violation if interpreted as causality/probability/confidence | Q01–02; R1,14 |
| V24 | A persisted project result lacks reproducible input/method/scope or required execution identity | Violation for acceptance as reproducible result; retain as unverified audit material if labelled | R12–14 |
| V25 | Capture exceeds approved scope/budget, mixes releases silently, or bypasses retention/permissions gate | Violation; stop capture/publication step | G05; R6,14 |
| V26 | Historical audit transcription clearly labelled, with pinned provenance and old review limits | Info; legitimate design fixture, not fresh-source replication | Q01–07; R6–9 |
| V27 | Finite namespace/receipt/enum/missingness profile version absent from a declared reproducible release | Violation for reproducibility acceptance | R6,12; all fixtures |

Source-record-ID conflict is not automatically a hash collision: flag uncertain co-reference with Warning while preserving separate captured versions; claiming they are the same immutable occurrence without evidence invokes V05. A historical unavailable source does not make the documentation false; it limits which future assertions can pass. Validation profiles must not generate MissingnessRecords recursively for validation failures.

**Consequences:** the same source gap can be a warning on data and a blocker for a stronger claim. Raw SHACL results remain auditable; application acceptance is separately labelled. Known dependency does not incorrectly appear as data corruption. **Owner approval requested:** these severities, scope of blocking and separation of source/structure/answer acceptance. No shapes, validator or implementation tests are created now; documentation examples are checked separately.

## 8. Consequence crosswalk and acceptance desk cases

| Gate | Ontology implementation consequence | Provenance / interpretation consequence | Reproducibility consequence |
| --- | --- | --- | --- |
| G01 | Stable exact term names under one proposed base; no new axioms | Local record IRI is not MONDO concept equivalence or institutional endorsement | Repository administration is a persistence dependency; namespace approval precedes minting |
| G02 | IDs generated from receipts; no new hash/run properties needed | Source, description and encounter identities remain distinct; opaque digests never imply truth | Replays stable; changed versions and encounters distinguished; receipts preserved and collisions blocked |
| G03 | Twelve string fields; no concept instances or new schema terms | Depth/access/outcome and dependency meanings remain separate | Versioned finite code lists prevent drift and silent remapping |
| G04 | Existing MissingnessRecord/expectedField used with 76 finite tokens | Known destination with unresolved validity remains expressible; reasons never waive structure | Repeated checks refer to the same field/requirement meaning |
| G05 | First schema can stay declarations-only; fixtures/capture remain separately authorized | Audit transcription does not impersonate raw source; actual source/rights limits survive | Reproducible project fixtures distinguished from historical live-source reproduction |
| G06 | Structural signatures and policy implemented later, not OWL domain/range | Structural validity ≠ supported answer ≠ biomedical truth | Raw validator results and application acceptance are separately versioned and reported |

No contradiction requiring a new class/property was identified in this documentation review. Two risks need explicit acceptance rather than silent repair: unversioned live sources cannot promise global record identity; and the proposed GitHub-scoped development IRIs do not supply a public resolution service. The finite profiles solve implementation decisions conditionally on owner acceptance; they do not establish unavailable source artifacts or rights.

Required later fixture checks, not executed now:

| Case | Expected behavior under this proposal |
| --- | --- |
| Replay a captured Q01 record with a different Turtle ordering | Same identity receipt/IRI and same qualifications |
| Retrieve the same known-edition/projection occurrence through direct and inclusive queries | One occurrence; separate SelectionContexts and Memberships |
| Two runs have the same wall-clock timestamp | Distinct allocated execution references prevent encounter collision |
| Provider reuses an ID while mapping/source content changes | New captured description version; old mapping/context retained; no overwriting |
| A mapping destination is known but OMIM interpretation is unresolved | reportedDestination remains; mappingStatus unresolved; requirement:mapping-validity explains limit |
| Original source identity unavailable in Q01 | Relevant expectedField/requirement with honest reason; no invented MONDO/OMIM input |
| Q04 chain loses a middle step | Path incomplete; endpoint inference/complete-chain answer blocked, source record retained with warning |
| Q02 two records share the trial | Shared study is expected information; independent genetic-confirmation claim rejected |
| Q06 indication list capture stops at a budget/pagination limit | Partial result; no exact-match absence claim for the whole list |
| Q07 trial status updates | Same Study referent; new StudyRecord; earlier registry population/status preserved |
| A paper body is inaccessible but metadata is available | Separate metadata inspection; no full-text depth or biomedical support fabricated |
| A canonical receipt digest collides or the payload changes under a supposedly immutable identity | Quarantine/block; never merge or generate a random suffix to hide it |

## 9. Owner approval record and next step

All six decisions changed from **PROPOSED / PENDING OWNER APPROVAL** to **APPROVED** by the owner’s explicit instruction on 2026-09-22 (Asia/Kolkata). Approval applies to the corrected package for the initial M1 audit-derived fixture scope. Historical live-source availability, permissions and Phase R endpoint projections remain explicitly deferred acquisition gates, not completed work. The approved commitments are:

1. The repository-scoped namespace and lack of a public resolution service in local V1.
2. `m1-id-1`: JCS/SHA-256 receipts, fixed source projection, immutable capture versions, ledger execution references, no random IDs, collision quarantine and conservative unknown-version identity.
3. `m1-enum-1`: the twelve exact unchanged token lists and operational combination rules.
4. `m1-missing-1`: 67 retained-field tokens plus nine interpretation tokens, finite owner/applicability rules and sparse creation.
5. `m1-capture-1` (the G05 policy): committed-audit fixtures first; live recapture separately authorized, finite source allowlist, batch ceiling, rights/retention receipts and no silent release substitution.
6. `m1-validation-1`: rule V01–V27, warning versus claim-blocking behavior and separate raw SHACL/application acceptance reports.

This approval resolves G01–G06 for the initial scope and authorizes recording the approval and committing only this documentation checkpoint locally. It does not authorize ontology implementation, fixture creation, external acquisition or pushing. The next step is a proposal for the bounded first schema implementation under readiness sections 15–16, followed by explicit owner authorization before execution. Do not reopen broad schema design or acquire a larger corpus as a substitute for these approvals. Schema generation alone does not require downloading source datasets; source-artifact availability is a gate for the affected fixture/reproduction claim.

## 10. Verification and changes in this task

Only documentation is changed: this mechanics investigation/approval record and its approval cross-reference in implementation readiness. The broader schema catalogue, charter, approved conceptual contract, source audit, Q01–Q07 and R1–R14 are unchanged. The approved term manifest is unchanged. Only the synthetic canonicalization/digest examples have been calculated for documentation verification; no production profile has been executed and no local record identifiers minted and no capture ledger, dataset, RDF/OWL/SHACL, Python implementation, package, database or production query created. The owner authorized a local documentation-only checkpoint commit; no push is authorized.

Primary technical sources checked for this proposal: [RFC 8785](https://www.rfc-editor.org/rfc/rfc8785), [SHACL](https://www.w3.org/TR/shacl/), [Open Targets data access](https://platform-docs.opentargets.org/data-access), [Open Targets licence](https://platform-docs.opentargets.org/licence). These support canonicalization, validation terminology and documented source routes; project policy choices are owner-approved within the initial scope recorded in section 9. No new biomedical findings, clinical adjudication, experimental result or novelty claim follows. Graph advantage remains **NOT YET DEMONSTRATED**.
