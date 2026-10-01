# Approved M2 RDF record identity extension

The owner authorized `m2-rdf-record-1` from baseline `1be4234cdb28c9a6b7eaf88b41b9c49ec8e7b4f2` for the frozen Mondo slice. This extends record identity only; it changes no ontology vocabulary or previous profile/artifact.

## Exact receipt contract

Every receipt has exactly `profile`, `kind`, `origin`, `inputs`, `contentRevision`. Profile is `m2-rdf-record-1`, origin is `live-source-derived`. All input values below are required nonempty original strings; no optional keys, inferred defaults, nulls or input arrays exist in this bounded profile. Missing required lineage blocks generation rather than becoming an invented value.

| Kind | Exact input keys |
| --- | --- |
| SourceSnapshot | descriptionId, edition, versionIri, loaded, updated, locator |
| DiseaseConceptReference | snapshotKey, locator, role, authority, identifier, label |
| HierarchyStep | snapshotKey, locator, childKey, parentKey |

`descriptionId` is an existing verified `m2-source-description-1` IRI. Snapshot edition, version IRI, OLS load/update strings and locator must match its verified freeze context; service timestamps receive no timezone inference. Snapshot locator is the original description-receipt locator. Other locators are canonical JSON strings of the extraction's complete `sourceRecordLocator` object (requestUrl and jsonPointer), preserving each original string. Roles are `reported-participant` for individual term descriptions and `hierarchy-endpoint` for parent-response row references. Authority is MONDO; identifiers and labels retain exact source spelling. All keys ending Key are full, previously registered M2 RDF record IRIs, never M1 receipts or external disease IRIs.

Content revision is SHA-256 of the existing normalized direct-owned-assertion payload: exact keys field/form/value/datatype/language, sorted and deduplicated by canonical bytes. Only approved properties are accepted. No recursive subgraph hashing. Every owned outgoing property, including provenance to source descriptions, is included before minting. rdf:type is fixed by kind; incoming links and separately identified provenance entities are not payload changes.

Reuse the existing string/null/container RFC8785-subset canonicalizer, UTF-8, full SHA-256 and G01 `/id/<Kind>/<digest>` IRIs. The distinct profile and origin prevent collision with M1 audit-transcription receipts without changing their namespace or implementation. There is no random execution or clock value in record generation. Replaying frozen inputs reuses identities; changed identity inputs or owned payload produce new identities. Conflicting supplied IDs or differing receipts/payloads under one digest fail. Capture identity is deliberately absent from source-record identity: capture encounters remain separately linked. A new capture of identical descriptions must not manufacture new biological evidence.

The registry checks description membership and source context against offline-verified inputs; the graph builder additionally checks exact locators, projected source values, accepted row selection and endpoint compatibility against the frozen extraction. Neither validation layer alone establishes biomedical truth. Snapshot, reference and hierarchy-assertion identities are always distinct from the underlying response-description ID.

## Verification

`tests/test_m2_rdf_identity.py` covers replay/key-order determinism, payload revisions, invalid profile/origin/keys, missing lineage, context conflicts, M1 identity reuse and explicit collision detection. No existing identity implementation or receipt is edited. The next stage may generate RDF only after these checks pass.
