# Offline historical-response acceptance contract

This is an attributed **review-dossier evaluator**, not an Open Targets response parser, acquisition client, historical schema implementation or activated ingestion contract. No actual export is available. No biomedical source record or result is invented. All positive tests use CONTROL-E1/CONTROL-E2, synthetic field-state declarations and explicitly non-source artifact bytes.

## Inputs and trust boundary

`tools/evaluate_evidence_response.py` accepts an in-memory review dossier and a local name→bytes artifact map. It does no network or filesystem acquisition. Top-level keys are exactly profile (`historical-evidence-review-1`), materialKind (`provider-material` or `synthetic-control`), release, schema, permissions, export, accounting, records and contexts. Duplicate JSON keys are rejected by load_dossier. Missing/malformed required information returns BLOCKED.

Release/schema/permissions/export reviews require status reviewed, attributed reviewer, basis, artifact name and exact SHA-256. Real use requires a reviewer to establish the provider identity, immutable release binding, applicable rights and historical schema from retained supporting material. The evaluator checks the dossier's consistency and byte integrity; it cannot establish the truth/authenticity of reviewer assertions. A fabricated review declaration is not independent proof. Actual field extraction must wait for the approved route-specific projection.

Release edition must be exactly 26.06, binding export-bound; a current or label-only release claim blocks. Schema binding must be historical-export, not inferred from the current GraphQL service. Permissions require explicit permitted use and retention, known redistribution disposition and attribution requirements. Restricted redistribution can pass with a no-redistribution qualification; unknown terms block. No source licence is granted by this evaluator.

Each record supplies an exact requested id, source locator, datasource, originalNormalizedSeparate flag and logical field-state reviews. Logical names come from the required-slot contract, not guessed historical response paths. Each field review has state and basis. States are present, source-null, source-absent and unknown. Historical source null/absence in original identifiers or conditionally available source fields can pass with a qualification; unavailable required target/normalized identifiers or locators prevent complete acceptance. Source-specific references are checked by category. Eight real requested IDs and their audited datasources are fixed by the contract; synthetic tests use two unrelated control IDs and cannot pass as provider material.

Context reviews separately cover association, selection, mapping and mechanism-indication-clinical. Verified means the required context and its limits are documented; it does not mean mappings are clinically valid. Partial/unavailable/unresolved required context keeps the overall result PARTIAL. The 56-slot contract remains the wider Q01–Q07 inventory: a PASS on this OT review dossier does not satisfy separate PanelApp, publication or registry slots.

Accounting records batch, complete, automaticReset, stopReason and attempts. Each attempt has kind (metadata/request/retry/redirect/unsuccessful) and receivedBytes. All attempts and bytes count; booleans, negatives, missing attempts, incomplete accounting and automatic reset are rejected. Received bytes cannot be below the retained export size. The operational ceiling remains 100 attempts / 10,485,760 bytes. Actual request ledger provenance still requires review; counts supplied in a dossier are not independently measured by this offline evaluator.

## Outcomes and precedence

| Outcome | Meaning |
| --- | --- |
| PASS | Dossier has consistent attributed release/schema/permission evidence, exact requested IDs and all required reviewed context; legitimate source-null/absent optional information remains qualified. Not a biomedical claim or source-contract approval. |
| PARTIAL | No hard blocker, but requested records/field reviews/context are missing or unresolved; export is incomplete/truncated; or acquisition stopped compliantly at a protective limit. Do not accept unverified truncated rows. |
| BLOCKED | Wrong/ambiguous edition, absent mandatory provenance, changed artifact digest, unresolved rights, malformed dossier, unexpected/duplicate IDs, conflicting datasource, conflated original/normalized roles, invalid accounting or exceeded budget. |

BLOCKED takes precedence over PARTIAL. Compliant stopping is not a protocol violation: reaching a ceiling without exceeding it yields PARTIAL. No budget reset or automatic follow-up is authorized. Synthetic results always say synthetic-control-only; both material kinds always return activatesSourceContract=false, authorizesAcquisition=false and biomedicalSupport=NOT ASSESSED.

## Verification and next use

Six tests exercise positive synthetic completeness, qualified nulls, partial exports/records/context, malformed and ambiguous metadata, missing lineage, digest corruption, wrong release/current schema, scope expansion, duplicate IDs, rights uncertainty, retries/redirects/failed-body accounting, exceeded budgets and compliant stopping. No biomedical payload value is supplied as a positive control.

After a provider reply, review source availability and permissions first; resolve exact historical field paths and context retention; then populate the dossier only from actual authorized artifacts. This tool supplies a checklist/evaluation step, not permission to capture or activate projections. Existing records and all identity profiles remain unchanged.
