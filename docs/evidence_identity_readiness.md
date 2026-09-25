# Evidence identity successor — inactive draft

`contracts/evidence-identity-draft.json` is **DRAFT-NOT-APPROVED**, activation false. Proposed name `m2-evidence-record-1` is reserved in planning only: no generator, parser, registry, identity receipt or RDF record uses it. No existing profile is changed.

## Exact elements that can be fixed now

The draft envelope retains profile/kind/origin/inputs/contentRevision. Candidate input key lists are copied from the existing approved finite M1 conceptual tuples, not inferred from milestone names. They cover EvidenceOccurrence; source-aggregate and project-grouping DiseaseTargetAssociation; MappingRecord; MechanismRecord; ClinicalIndicationRecord; StudyRecord; PopulationScope; SelectionContext/Membership; HierarchyPath; DerivedStatement; InspectionRecord; MissingnessRecord. These are **existing ontology classes**, not a requirement to instantiate every possible class/record.

For source descriptions, keep verified snapshot and exact record/row locator, record ID when supplied, scoped participants and owned payload revision. Original disease, reported destination and project/query anchor remain distinct. Mapping context points to the affected occurrence; process/version uncertainty remains explicit. Hierarchy and query inclusion cannot stand in for normalization. Mechanism, indication, report, population and clinical phase/status remain separate.

For operations, preserve actual execution, method/version, input versions, scope and qualified result. Replayed operations preserve their execution reference; later explanations do not create a new retrieval or membership. The existing StudyRecord/population deferred-link exception remains protected by the immutable bundle, not recursive identity hashing. Optional inputs use explicit null with attributed reason; mandatory unknown identity inputs prevent stable acceptance. []S alone denotes a sorted/deduplicated set; []O preserves order/repetition. Other unknown arrays remain disallowed until explicitly specified.

Canonicalization, full SHA-256, exact lexical spelling, owned-payload revisions and collision rejection carry forward unchanged. Source identity must not include unrelated capture timestamps or selection encounters. A second capture does not create independent evidence.

Authority referents Target/Drug/Publication/Study already have approved authority-qualified principles. Verify any existing referent's authority and scope before reuse; attach newly acquired descriptions separately. Do not create duplicate referents because a source edition changed, or silently certify an audit-derived label as freshly verified. SourceSlice remains a mechanical prov:Entity representation, not a class extension.

## What cannot yet be finalized

The current m2-source-description-1 is fixed to Mondo and its projection. The current m2-rdf-record-1 snapshot contract requires OLS loaded/updated/versionIri values and its reference contract does not cover all source/normalized roles or absent identifiers. Those fields cannot be fabricated for OT, panels, registry or articles. Separate approved successor source-description and RDF snapshot/reference contracts must define the provider-specific context actually available.

Exact raw field paths, atomic-record boundaries, provider record/version rules, export locators, unknown-field handling and source-specific permissions remain pending a real historical schema/route. The candidate M1 key lists are semantic requirements, **not an activated historical response projection**. Current APIs do not certify 26.06 fields. When verified source data changes an expected optional field into a mandatory identity blocker, document and review that decision rather than minting a guessed receipt.

The first candidate implementation batch should activate only the necessary source record kinds for the available response, then the corresponding scoped operations. No need for a universal ingestion/identity service. Test receipt replay, payload revisions, incompatible snapshots, shared-source handling and forbidden M1-audit/live substitution before generating source-backed RDF.

## Readiness result

Two draft checks confirm the inactive status, exact approved input-key lineage, existing ontology kinds and explicit unresolved source contracts. This authorizes no source capture or identity activation. Next actionable work after a provider reply is a concrete route/schema/permission review and a minimal successor contract for owner approval, preserving every earlier artifact.
