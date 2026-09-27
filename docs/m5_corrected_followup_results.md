# Corrected M5 follow-up — preserved partial development results

Approved retrieval baseline: `18ddd6444a8391abebbe210f2c9ba9b5e97d2bb1`.

## Outcome

Eight generation attempts were made under the owner's explicit extension. **Seven completed; one timed out.** Corrected grounded Q01–Q06 completed, followed by the missing model-only Q07. Grounded Q07 reached the existing 120-second client timeout; the diagnostic is `timeout / transport / transmission=unknown`. No HTTP status, response ID, response body or usage was returned for this failure. It is unknown whether generation completed or was billed on the provider side. No retry, refund, manual output repair or substitute model was used.

All successful responses report `gpt-6-sol` and the standard/default service tier. Requests preserve low reasoning, strict JSON, no tools, `max_output_tokens=4096`, the approved question text, prompts and exact corrected retrieval hashes. Grounded and locally verified conditions use the same generated candidate and evidence; verification makes no model call. The six model-only Q01–Q06 outputs are reused with exact matching request hashes, not silently regenerated.

## Accounting

| Quantity | Observed / reserved |
|---|---:|
| New generation attempts | 8 |
| New successful / failed generations | 7 / 1 |
| New HTTP requests, including counting | 16 |
| Cumulative generation attempts / HTTP requests | 22 / 44 |
| Successful new input tokens | 194,998 |
| Successful new output tokens, including reasoning | 6,854 |
| Failed Q07 counted input tokens (not usage confirmation) | 9,788 |
| Failed Q07 output reservation | 4,096 |
| New conservative input / output accounting | 204,786 / 10,950 |
| Estimated successful new token cost | $0.458536 |
| Additional cumulative reservation | $0.737252 |
| Cumulative reservation, including all historical attempts | $1.544974 |
| Q07 timeout's retained reservation | $0.060536 |

Cost uses the unchanged approved assumptions of $2/M input and $10/M output; all completed calls report zero cached input tokens. Provider usage metadata, including reported cache-write and reasoning fields, is retained verbatim. Cost estimates are not billing invoices. Failed-call usage/billing is unknown and is not counted as zero. Across both runs, known successful token cost is $0.767612, excluding unknown failed-call charges. Full reservations remain held.

The additional reservation is below $1.92768, new token accounting is below 800,000/32,768, and cumulative reservation is below $5. The 22/44 attempt/request limits are exhausted. A further request requires separate authorization even though dollar/token headroom remains.

## Separate conditions and question-level observations

| Question | Model-only | Grounded cited claims | Locally verified exact RDF claims | Rejected | Grounded unanswered entries | Observation, not an adjudicated score |
|---|---|---:|---:|---:|---:|---|
| Q01 | Reused, unverified | 5 | 5 | 0 | 4 | Reports source-level assignments and original-field missingness; qualifies causal interpretation. |
| Q02 | Reused, unverified | 2 | 2 | 0 | 1 | Identifies shared NCT00594737 provenance and withholds independent genetic confirmation. |
| Q03 | Reused, unverified | 2 | 2 | 0 | 1 | Distinguishes original Pick label from normalized FTD scope. |
| Q04 | Reused, unverified | 2 | 2 | 0 | 3 | Reports hierarchy context but cannot establish historical direct/inclusive results; also notes missing Q03 definition in its standalone prompt. |
| Q05 | Reused, unverified | 8 | 8 | 0 | 3 | Keeps the two OMIM:600274 assignments record-local and unreviewed. |
| Q06 | Reused, unverified | 5 | 5 | 0 | 3 | Separates gene-indexed mechanism from indication and qualifies unsupported efficacy. |
| Q07 | New, unverified | — | — | — | — | Grounded request timed out; no grounded or verified output exists. |

All seven model-only outputs have zero structured cited claims by the no-evidence instruction, but their free text can contain general biomedical statements. That is not a zero-unsupported-claim measurement. Grounded-only keeps all 24 candidate statements unchecked. Local verification accepts 24 exact RDF statements and attaches provenance, while explicitly leaving explanation prose and answer text unverified. Grounded unanswered entries total 15; model-only entries total 15 across all seven questions. These descriptive counts have different coverage and are not accuracy or abstention-quality scores.

No observed claim was rejected in this follow-up, so it does not demonstrate a beneficial rejection intervention or superiority. Statements above summarize generated outputs without supplying independent biomedical adjudication. No statistical inference is made from six paired exposed development cases.

## Comparability and limitations

- Q01–Q06 have request-matched development outputs across model-only, grounded and verified conditions. Model-only has intentionally different information access; grounded/verified share the same candidate and packets.
- **Not all Q01–Q07 have comparable outputs:** Q07 lacks the grounded/verified pair. The failure is preserved, not removed from accounting or filled with a synthetic answer.
- Explicit question-scoped retrieval corrects engineering mismatches; it is not an evaluation of unrestricted natural-language retrieval or graph advantage.
- Q04's historical query counts remain outside the supplied RDF interface. Its reference to “Q03” is not expanded in the standalone prompt, which was deliberately left unchanged. Any future prompt correction must be separately identified rather than retroactively applied.
- Primary registry population/status, historical panel editions, full datasource composition and some publication-inspection details remain qualified source gaps. Mapping validity is not adjudicated.
- Exact triple membership does not validate interpretation, scope, clinical efficacy, evidence independence, completeness or question relevance.
- The model identifier is an alias and the six model-only outputs are explicitly reused; these are not independent replicated samples or held-out questions.

## Reproducibility and implementation

`tools/run_m5_corrected_followup.py` records a one-time explicit ledger amendment retaining original counters, entries, limits and ledger hash. It refuses automatic re-amendment or restart. The adapter's extension is opt-in; default historical limits remain unchanged. A fresh empty ledger cannot activate corrected follow-up mode. Both old failures remain reviewed, but any new failure stops execution.

`experiments/m5-corrected-followup-001/` stores only new attempt artifacts (015–022), a cumulative ledger snapshot, and a deterministic summary with hashes. The original pilot and corrected retrieval plan remain unchanged. Secrets, authorization headers and raw error bodies are not included.

Offline replay:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=tools:/private/tmp/ot2606-duckdb-inspection:/private/tmp/dementiagraph-m1-task008-pyshacl python3 tools/replay_m5_corrected_followup.py
```

Replay checks original attempt preservation, explicit limit amendment, exact corrected request hashes, response hashes/model/usage, local verification, reused model-only linkage, cost reservations and the visible timeout. Source/support claims are not added or repaired.

Full offline regression: **288 tests passed in 351.736 seconds**, including all previous regressions and three new amendment/accounting/replay tests. `git diff --check` passes. Original pilot, corrected plan, ontology and graph preservation checks pass. No credential-shaped values or authorization strings were found in the follow-up artifacts.

## Can M7 begin?

**Protocol preparation can proceed; formal M7 evaluation cannot begin yet.** The existing approved evaluation protocol requires an owner-approved freeze before evaluation execution. Remaining decisions/work:

1. Explicit disposition of incomplete Q07: authorize a bounded retry or retain it as a documented development failure. Do not claim seven complete pairs.
2. Freeze a primary contrast and what it measures. Current literal-RDF checking does not implement a prose-support verifier; either evaluate that limited capability explicitly or separately approve any enhancement. Model-only and curated-grounding comparisons have different information access.
3. Approve held-out construction, question/evidence dependency grouping, custody/access and contamination rules. These seven exposed questions and near-paraphrases are not eligible by relabelling.
4. Agree answerability categories, claim units, scoring denominators, completion/unsupported-broadening/qualification/abstention criteria, treatment of failures and exclusions, sample size and analysis before observing held-out results.
5. Establish reviewer arrangements and independent labels appropriate to the claimed technical or biomedical validity. No domain-expert adjudication is assumed available.
6. Freeze corpus/configuration, repeat/retry policy and explicit M7 API budget. Source gaps must remain part of the evaluation scope, not silently filled.

No M7 dataset construction, model calls, experiment execution or M6 agent implementation was started by this task. The immediate next step is a bounded evaluation-protocol decision, with Q07's timeout separately accounted for.
