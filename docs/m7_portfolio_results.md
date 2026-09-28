# M7 portfolio challenge execution and deterministic results

**Subsequent review update:** [Owner-directed scoring and findings](m7_owner_evaluation_findings.md) are now recorded. Pending-review statements below describe the preserved execution checkpoint, not the current annotation status. Raw execution and automated verification artifacts are unchanged.

Designation: **Development-overlapping portfolio challenge set**.
Frozen package: `259af039b034fbd9753e4f69c214459b3fcf5049`.
Execution implementation: `a2a0323d334924c219477288de96876bfc254114`.
Owner explicitly authorized the live run, post-generation deterministic
verification, frozen scoring and local results commit. No push authorized.

## Execution

Exactly **24/24 generations** completed and produced structurally valid answers:
12 model-only and 12 grounded. Verified uses those same 12 grounded responses,
not additional generations. **48 HTTP requests**, including 24 authoritative
input counts; **zero retries**, timeouts, HTTP failures, refusals or invalid
structured answers. No optional development Q07 retry occurred.

Frozen questions, retrieval scopes, prompts, strict JSON schema, model
`gpt-6-sol`, low reasoning, 4096 maximum output tokens, empty tools, timeout
120 seconds and failure rules were unchanged. Public and private integrity
checks passed before execution. Requests replay against the frozen hashes.
No experiment parameter was changed after outputs became available.

## Provider usage and accounting

| Generation condition | Input tokens | Output tokens |
|---|---:|---:|
| Model-only | 2,760 | 1,909 |
| Grounded | 332,321 | 15,001 |
| Total | **335,081** | **16,910** |

Verified adds zero generation tokens. Output usage includes provider-reported
reasoning tokens. All 24 responses include cached-input and cache-write counts.
Exact token-priced cost: **$1.0054045**; no unknown-cost generation.
This is calculated from returned usage and verified prices, not an invoice
reconciliation. The existing reservation **$1.544974** was preserved unchanged.
New reservation **$1.8207425**; cumulative reservation **$3.3657165**, below
$7.50. Reservations were not refunded after successful calls.

Current official pricing verified immediately before execution:
[GPT-6 Sol](https://developers.openai.com/api/docs/models/gpt-6-sol),
$2 input / $0.20 cached input / $2.50 cache write / $10 output per million.
Each call was admitted using its server count and maximum cache-write/output
cost. Existing historical M5 costs are not reinterpreted here.

## Deterministic verification, separate from human scoring

| Question | Model-only claims | Grounded claims | RDF accepted | RDF rejected |
|---|---:|---:|---:|---:|
| M7-01 | 0 | 8 | 8 | 0 |
| M7-02 | 0 | 10 | 10 | 0 |
| M7-03 | 0 | 7 | 7 | 0 |
| M7-04 | 0 | 5 | 5 | 0 |
| M7-05 | 0 | 2 | 2 | 0 |
| M7-06 | 0 | 3 | 3 | 0 |
| M7-07 | 0 | 4 | 4 | 0 |
| M7-08 | 0 | 4 | 4 | 0 |
| M7-09 | 0 | 4 | 4 | 0 |
| M7-10 | 0 | 3 | 3 | 0 |
| M7-11 | 0 | 1 | 1 | 0 |
| M7-12 | 0 | 4 | 4 | 0 |
| Total | **0** | **55** | **55** | **0** |

All 55 grounded claims pass the unchanged local exact-assertion/citation/type
checks. The verified condition retains all 55; generated prose is byte-for-byte
unchanged. These are mechanical counts, not the frozen human-labelled primary
precision metric. Model-only has no emitted structured assertions, so its
assertion precision cannot be called zero or 100%. Its prose remains available
for review. Empty assertions are not automatically correct abstention.

No model output was repaired. Lack of rejections here does not demonstrate that
the verifier detects every biomedical overclaim or improves prose. It only
shows these submitted assertion records pass its checks. Explanation accuracy,
relevance, required-fact coverage and clinical interpretation remain separate.

## Human scoring status — pending, not fabricated

Subramanya Prasad remains the sole human reviewer. The assistant-prepared frozen
private rubric remains unchanged and is not independent gold. No completed
owner output labels have been supplied during this execution task.

`experiments/m7-portfolio-challenge-001/owner-review.md` presents unchanged
questions, prose and structured claims. The adjacent `owner-review-template.json`
contains 36 condition rows with **null** human fields. Null means unscored;
it does not mean incorrect, unsupported, absent or abstaining.

The unchanged `m7_protocol_checks.aggregate` and
`paired_precision_difference` require actual owner labels. Therefore human
precision, relevance, provenance accuracy, required-fact completion, prose
correctness/unsupportedness, qualification/abstention, and their paired
comparisons are **not yet calculated**. Required-reference-fact retrieval
coverage also remains unreported; matching frozen retrieval roots alone is
not that metric. No inter-rater agreement is calculated.

Complete the review in a new file; retain the blank template and all raw outputs.
After receipt of the owner's labels, the existing frozen aggregators can produce
the remaining descriptive metrics without further model calls. Do not modify
the rubric in response to the outputs.

## Reproducibility and disposition

- `experiments/m7-portfolio-challenge-001/`: 97 exact raw execution files
  (24 count requests/responses, 24 generation requests/responses, one ledger).
- `artifact-manifest.json`: SHA-256 map for the raw execution archive.
- `verification.json`: reproducible deterministic outcomes and accounting.
- `tools/replay_m7_challenge.py`: offline request/response integrity, independent
  usage-cost recomputation and the unchanged local verifier; no model client.
- External originals and execution lock remain in the existing model-run area.
  They are not overwritten or reset.
- Model responses are stored as `.bin` to preserve exact bytes, including JSON
  formatting; their semantic content is not modified.

The evaluation is development-overlapping and cannot estimate unseen-question
generalization. It has no independent or clinical validation and supports no
statistical superiority claim. The graph remains a qualified bounded corpus,
not a complete dementia evidence base. The model is an alias, not a pinned
provider-weight snapshot. No M1–M6, source or frozen evaluation artifacts change.

**M7 execution and automated verification are complete; owner scoring and final
metric reporting remain open. M8 final-results release packaging is not yet
ready to be represented as complete.** No M8 work or push was performed.

## Regression and integrity verification

All **319 existing regression tests passed** in 384.185 seconds. All **three new
result-replay tests passed**, giving **322 passing tests** across the full
regression run and the new focused suite. The focused suite was repeated after
adding complete raw-manifest hash verification. Controls reject changed raw
responses and changed ledger accounting; successful replay reproduces the saved
verification artifact without inserting human scores.

Post-run public/private freeze verification passed for all 12 questions. The
original M5 cumulative ledger remains byte-identical to its committed copy.
Git whitespace checks passed; no credential-pattern findings in the new archive.
