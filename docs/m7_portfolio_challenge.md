# M7 — Development-overlapping portfolio challenge set

Owner-approved amendment, 2026-09-28, from `367b75513bf4dae7b5e4932b7aeca02faca7097d`.

## Designation and limits

The questions are human-authored by the project owner and distinct in wording from development Q01–Q07. Semantic overlap with previously rehearsed capabilities exists; **this evaluation does not estimate unseen-question generalization**. Results are intended to demonstrate reproducible system behavior across retrieval, provenance, reasoning, qualification and abstention tasks. No claim of clinical validation, independent validation, statistical generalization or benchmark superiority is permitted.

This replaces the earlier held-out designation for this set. The original protocol, blank authoring template, rejected holdout assessment and all development outputs remain historical artifacts; they are not retroactively relabelled as successful holdout validation. The six-stratum paired sampling requirement does not apply to these owner-selected overlapping questions. The submitted six primarily answerable / six qualification-style allocation is preserved, with mixed dispositions retained privately rather than forcing all questions into wholly answerable/unanswerable labels.

## Frozen package

`evaluations/m7-portfolio-challenge-001/` contains:

- `questions.json`: exact twelve owner questions, M7-01–M7-12, intended categories and exact retrieval root IDs. Only surrounding whitespace was removed from the original submission.
- `protocol.json`: amended designation, unchanged model/limits and fixed scoring policy.
- `retrieval-checks.json`: request and packet hashes from offline construction; no generated responses.
- `provenance.json`: original overlap findings and rejected owner candidates A/B with original wording, reason and before-freeze ordering. Exact earlier timestamps are not invented.
- `freeze.json`: public code/data/protocol pins and private artifact digests. Private rubric contents and absolute local paths are excluded from Git.

The private `m7-portfolio-challenge-001` directory contains immutable `rubric.json`, readable `rubric.md`, and unchanged copies of the earlier private draft and eligibility review. The rubric is **assistant-prepared**, explicitly frozen at owner request, and not independently authored gold. This does not attest that the owner has already individually reviewed every reference entry. The rubric preserves required facts, qualifications, unsupported claims, exact retrieved assertions, provenance and expected answer/qualify/abstain/mixed dispositions. No output labels or scores have been invented.

Subramanya Prasad is the sole curator/reviewer. Human prose scoring remains required after generation. Independent review is a future gap, not a prerequisite; no inter-rater agreement will be calculated or claimed. All raw responses, request configurations, failures, deterministic verification artifacts and scoring rationale must be retained for future reassessment.

## Conditions and fixed scoring

One model-only and one KG-grounded generation per question: **24 generations, 36 logical condition outcomes**. Grounded + local verification reuses the identical grounded text and retrieved evidence. It is a post-generation process, not a third model call. Model-only receives no packets or rubric. Requests are constructed solely from public questions and frozen RDF roots; private reference/rubric fields never enter request construction.

The primary metric, companion metrics and formulas remain those in `tools/m7_protocol_checks.py` and the original protocol's “Exact metrics and aggregation” section. Required-fact IDs and qualitative pass requirements are fixed in the private rubric. M7-01–06 use the fixed six-item answerable-intended denominator for excessive abstention; M7-07–12 use the six-item qualification/abstention denominator for required abstention. The legacy scorer's internal `insufficient` category denotes this denominator, **not** an assertion that these items contain no answerable facts. Mixed dispositions and useful positive facts remain required. Failures contribute zero completion and do not count as successful abstention.

Source-relative structured assertion support, human prose correctness, completion, unsupported/contradicted claims, unresolved judgments, qualifications, abstention, relevance, provenance, retrieval coverage, failures and costs remain separate. Grounded/verified prose is identical and receives identical prose scores. Only their retained structured-assertion surfaces differ. Descriptive statistics and paired differences only; no significance or superiority inference. M7-12 concerns unsupported graph composition, never patient-specific prescribing advice.

## Frozen failure and request rules

Preserve `gpt-6-sol`, low reasoning, strict JSON, no tools, max output 4096, 120-second timeout, existing prompts, standard/default service tier and zero challenge retries. Record refusals, timeouts, malformed responses and API errors as outcomes. No answer repair, question substitution or scoring changes after outputs. Isolated failures may continue only under the original policy and safe budgets; authentication/quota, changed model/pricing, integrity, budget or systematic failures stop the batch. Unknown failed-attempt charges retain their reservation.

Existing prompts still identify development context. They are pinned and intentionally not rewritten to imply an unseen benchmark. The original Q07 timeout remains unchanged; its optional one-call development retry is separate and is not executed by this freeze task.

## Budget and execution boundary

At the previously approved rate assumptions of USD 2/M input and USD 10/M output:

| Component | Generations | Input ceiling | Output ceiling | Maximum token reservation |
|---|---:|---:|---:|---:|
| Twelve-item challenge | 24 | 2,400,000 | 98,304 | $5.783040 |
| Optional unchanged development Q07 retry | 1 | 9,788 | 4,096 | $0.060536 |
| Combined | 25 | 2,409,788 | 102,400 | $5.843576 |

Challenge requests include up to 24 token-count calls in addition to 24 generations (48 HTTP requests). The optional development retry adds two requests. Existing reservation is $1.544974; challenge alone reaches at most $7.328014, or $7.388550 with the optional retry. Both remain inside the approved $6 additional / $7.50 cumulative ceilings. These are conservative reservations, not actual spending or empirically predicted token use. Current pricing is not verified by this offline task; verify before paid execution and stop for material changes. Never reset prior ledgers.

**No model/API calls are authorized by the current freeze instruction.** A subsequent execution instruction is needed. No live M7 runner is implemented in this task; any runner must preserve frozen requests, scoring, zero-retry and cumulative-ledger rules and must pass offline controls before spending. The freeze pins existing request/retrieval/verifier/scoring code; it does not falsely claim an unimplemented orchestration layer was tested.

## Offline verification

Run with the existing RDFLib 7.1.4 / owlrl 7.1.4 / pySHACL 0.30.1 environment:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=tools:/private/tmp/ot2606-duckdb-inspection:/private/tmp/dementiagraph-m1-task008-pyshacl python3 tools/m7_challenge_freeze.py
# Add --private-directory /your/private/m7-portfolio-challenge-001 to verify private pins too.
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=tools:/private/tmp/ot2606-duckdb-inspection:/private/tmp/dementiagraph-m1-task008-pyshacl python3 -m unittest discover -s tests -v
```

Verification results are recorded after the full run below. Existing research inputs, historical outputs and budget ledgers remain unchanged. No raw biomedical material or private reference answer is added to Git.

### Completed verification — 2026-09-28

**304 tests passed in 362.051 seconds**, including all 299 previous regressions and five new challenge-freeze tests. Public request/packet replay and private artifact hashes verify. All twelve question texts match the prior owner submission exactly; all intended roots fit the fixed retrieval budgets. Changed/missing artifacts, altered scope/allocation, holdout relabelling and private rubric fields in public questions are rejected by the new controls. `git diff --check` passes. No live requests or source acquisition occurred.

The temporary test environment had lost package source files. Exact existing versions were restored outside Git: RDFLib 7.1.4, owlrl 7.1.4, pySHACL 0.30.1, pyparsing 3.3.3 and wcwidth 0.8.4; other matching cached packages were restored locally. This was test-environment repair, not a project dependency or research-artifact change. Only software packages were downloaded; no model or biomedical requests were made.
