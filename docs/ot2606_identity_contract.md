# OT historical evidence identity extension

With the actual schemas verified, the bounded successor activates `m2-evidence-record-1` for the frozen eight-row OT slice. The older inactive investigation draft remains historical and unchanged; it is not itself activated. No existing profile, ontology term or M1/Mondo identity changes.

## Exact boundary

The five-key envelope remains profile/kind/origin/inputs/contentRevision. Source kinds: SourceSnapshot, DiseaseConceptReference, EvidenceOccurrence, MappingRecord and StudyRecord, origin `live-source-derived` (historical source records acquired now, not current-release substitutions). Local operations: SelectionContext, SelectionMembership, project-grouping DiseaseTargetAssociation, DerivedStatement and MissingnessRecord, origin `project-operation`. Mechanisms, indication records, populations, source aggregate associations, historical selection replay and additional classes are **not activated**.

SourceSnapshot exact inputs: descriptionId, edition, datasource, locator. Values must equal the verified `m2-ot-parquet-description-1` receipt and row lineage. There are no fabricated OLS timestamps/version IRIs. Other activated kinds use the exact corresponding key catalogue from G02 §3.4a unchanged. A locator is the canonical JSON string `{url,recordId}` from the frozen extraction. Inputs ending Key/Keys resolve to previously registered records. Nullable values remain explicit null with reasons in owned limitation text; absent required lineage blocks acceptance. Destination/candidate/input arrays follow the existing sorted-set convention; source arrays remain ordered in the extraction. Description identities remain distinct from local-observation identities.

Disease roles remain original, normalized and project-anchor. Original IDs and labels use only fields actually present. No reference is minted where both original ID and label are absent. Normalized destinations preserve `MONDO_` spelling; source authority is MONDO. Original authority is supplied only for actual OMIM identifiers, not invented for label-only source wording. A normalized label is null because the evidence rows do not supply one. The two project-anchor references are local query roles using observed AD/FTD destination identifiers; no new anchor or descendant closure is introduced. No MONDO equivalence is asserted against the frozen OLS slice.

Mapping inputs retain studyId as panel context where present; method, methodVersion and execution are null because the upstream process is unknown. Empty candidate arrays mean no reported candidate entries, not proof that ambiguity is absent. Contextual OMIM:600274 destinations remain separate records. MappingRecord → EvidenceOccurrence is the only mappingContext direction.

EvidenceOccurrence retains exact source ID and scoped snapshot/locator. Source assertions are distinguished from local groupings. Source stage belongs in a StudyRecord describing the OT report context; registry source date/arm are null, because an OT publicationDate or studyStartDate is not a registry-version date. The original lowercase `nct00594737` locator remains lowercase; it is not silently merged with the audit's uppercase locator. No registry status, results or population are invented.

Authority-qualified Target/Publication/Study referents reuse the existing **referent** identity route, which is not an audit-transcription identity. Only authority and exact identifier are asserted; no old labels become new source observations. New EvidenceOccurrence IDs cannot use M1 audit receipts.

ContentRevision hashes the existing sorted/deduplicated owned-assertion payload. SelectionMembership keeps the established occurrence+context identity with null contentRevision; changing an explanation under an already registered ID is rejected, and later explanations must use review/derivation machinery. Source value/payload revisions create new descriptions/IRIs. Source descriptions exclude capture time. The registry rejects unregistered references, unsupported kinds/origins, mismatched source context, conflicting supplied identities and collisions. No recursive RDF hashing, new inference or global identity framework is introduced.

## Local operation scope

`ot2606-evidence-001/2` identifies this actual fixed-ID, direct-normalized AD/FTD selection, not a historical OT query. Six anchor-normalized occurrences are grouped; the two narrower diagnostic occurrences remain represented but are not pooled into anchor groups. Selection completeness is only for the explicitly enumerated IDs in this artifact. The release is not a complete disease association list. Groupings have no source aggregate scores or historical ranks.

`ot2606-evidence-001/3` is a two-record comparison of the clinical report locators. It can establish shared source only for these inputs, never evidence independence or clinical efficacy. All source-level score/date/array/missingness details remain in the source slice and extraction. Missingness records are sparse; do not duplicate an already scoped limitation.

## Implemented verification

Six focused identity tests pass: deterministic replay, payload revisions, wrong origin/inactive kind, rejected audit snapshot reuse, collision/conflicting IDs, corrupted descriptions, capture-independent record identities, membership explanation policy and contextual disease separation. Extraction-package hashes legitimately change when capture linkage changes; source record identities do not. Local operation timestamps are pinned in `manifests/ot2606-evidence-001.operations.json` and are not acquisition dates.

RDF and provenance use the existing Mondo serialization helpers and original SHACL. Initial development findings (wrong metadata property owners, observationContext participant and missing local observedAt) were corrected in the new builder; no old shape or ontology was weakened. Missingness observations now point to the verified source-description information resource. Grouping execution remains in its receipt and linked SelectionContext; no unsupported executionReference owner is introduced. The two original-input warnings are retained.
