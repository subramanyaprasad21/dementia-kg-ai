# M5 development pilot: first funded results

Status: **partial development pilot, not held-out evaluation or M5 scientific closure**. The same approved `gpt-6-sol` request configuration was used: low reasoning, strict JSON, 4,096 maximum output tokens, no tools, standard service tier, no automatic retry. All returned model identifiers were `gpt-6-sol`.

## Execution and accounting

After the owner confirmed funding, the existing ledger resumed with the two historical failed attempts explicitly reviewed. Those attempts, their reservations and original payloads remain unchanged. Twelve new generations succeeded. Execution stopped at the original 14-generation-attempt / 28-HTTP-request ceiling, before sending anything for Q07. This is incomplete coverage, not a completed seven-question pilot. No budget or model change was made.

- Q01–Q06: six model-only and six retrieval-grounded generations.
- Local verification processes those same six grounded outputs, adding no generation.
- Successful usage: 116,693 input tokens; 7,569 output tokens; zero reported cached input tokens.
- At the approved $2/M input and $10/M output rates: **$0.309076 estimated successful-generation cost**. This is not an invoice.
- Cumulative reserved amount: **$0.807722**, within the $5 ceiling. Billing of the two earlier failed requests remains unknown; their $0.082816 reservation remains included.
- No new generation errors or refusals. Q07 has no output and is not assigned a score.

## Operational observations

| Question | Grounded candidate statements | Exact RDF statements accepted | Rejected | Model-only unanswered entries | Grounded unanswered entries |
|---|---:|---:|---:|---:|---:|
| Q01 | 6 | 6 | 0 | 2 | 4 |
| Q02 | 3 | 3 | 0 | 2 | 1 |
| Q03 | 2 | 2 | 0 | 1 | 1 |
| Q04 | 3 | 3 | 0 | 3 | 2 |
| Q05 | 8 | 8 | 0 | 2 | 2 |
| Q06 | 2 | 2 | 0 | 3 | 2 |
| Total | 24 | 24 | 0 | 13 | 12 |

All model-only outputs contain zero structured cited claims, consistent with their no-packets instruction. This does not mean the prose contains no factual claims. The retrieval-only condition leaves the same 24 statements unchecked; local verification confirms their literal membership in the supplied packets and attaches provenance. It rejected none in this sample. No improvement in accuracy, clinical reliability or unsupported-prose detection has been demonstrated. Unanswered-entry counts are descriptive and are not accuracy or correct-abstention scores.

The preparation document explicitly left final scientific metrics and reviewer arrangements undecided. These are the implemented operational measurements, not a retrospectively invented scientific scoring rubric.

## Exposed limitations requiring attention before evaluation

1. **Question-to-retrieval relevance:** the committed plan paired the seven core question texts positionally with existing retrieval cases. For example Q02 asks about FTD GRIN1/GRIN3B independence, but its approved retrieval configuration selects StudyRecord packets anchored on NCT00594737. Q03 asks about FTD/MAPT while its configured mapping anchor is OMIM:172700. Exact plan replay therefore preserves a potentially mismatched or incomplete context; it does not establish adequate question coverage. These configurations were not silently repaired mid-run. A deliberate question-to-evidence alignment review is required before further scientific comparison.
2. **Verification boundary:** all 24 cited triples are present, but free-text explanations, entity interpretation, relevance, and completeness remain unverified. The model-only Q01 answer also gives general PSEN1 background despite lacking the sampled records. No biomedical truth or falsehood judgment is assigned here.
3. **Evidence visibility:** generated answers explicitly identify absent disease linkage, datasource composition or source context in the supplied packets. Retrieved packet incompleteness must not be interpreted as absence from the full graph or source corpus.
4. **No observed verification rejection:** this pilot demonstrates successful structured generation and deterministic assertion checking, not a measured advantage of verification. Synthetic negative tests remain separate from these observed model outputs.
5. **No independent test population:** Q01–Q07 are exposed development/design material. No held-out questions, independent labels or reviewer adjudication were created.
6. **Incomplete execution:** Q07 awaits separate authorization if completing it requires raising the original attempt/request ceiling. Available dollars do not override those ceilings.

## Reproducibility

`experiments/m5-development-pilot-001/` retains the cumulative ledger; exact prepared inputs and request payloads for all attempts; provider response bytes and deterministic local results for the 12 completed calls; and a summary containing artifact SHA-256 digests. No credential, header or raw error body is included. Original external run artifacts remain in place. Historic preparation/diagnostic records are preserved as records of their respective times.

Replay without network access:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=tools:/private/tmp/ot2606-duckdb-inspection:/private/tmp/dementiagraph-m1-task008-pyshacl python3 tools/replay_m5_pilot.py
```

The replay matches each request to the pinned plan, reconstructs retrieval from the pinned corpus, validates response hashes/model/usage, reruns assertion verification and checks saved results. It establishes local reproducibility of retained bytes and computations, not cryptographic attestation of provider origin or identical future model generations. The model is an alias, not a dated snapshot.

Tests include exact saved-result replay with networking blocked and rejection of altered request bytes. Full regression: **274 tests passed in 313.903 seconds**, including the two new recorded-pilot replay tests. `git diff --check` passes. Historical research artifacts remain unchanged.

## Next boundary

No further API calls, M7 evaluation or provider changes are included. First review the question-to-retrieval mapping defect and agree how to complete the missing Q07 coverage without rewriting these results. Any rerun must be a separately identified development revision with explicit call/token/cost authorization. M6 remains optional.
