# M7 execution-only runner

Implementation scope: offline runner implementation and mock tests only;
no live calls. Frozen basis:
`259af039b034fbd9753e4f69c214459b3fcf5049`.

## Boundaries

`tools/run_m7_challenge.py` uses the unchanged shared request constructor,
request validator, canonical serialization, redirect rejection and safe ledger
writer. It pins the freeze manifest digest and replays its public/private checks.
It does not use the M5 high-level execution function because that also scores.
Nothing here changes the frozen protocol, questions, prompts, private rubric or
research artifacts. The historical freeze correctly records that this runner
was not implemented at the freeze point.

Default execution is an offline dry run, without reading credentials or invoking
any transport. There is no optional Q07 development generation. Exactly 24
ordered requests are permitted: each M7-01–12 model-only then grounded.
Verified-condition processing is absent; later verification must reuse the same
recorded grounded answer and evidence. No claims or model output are scored.

Live execution requires an explicit run authorization, a private
integrity directory, current Standard pricing confirmation, and the fixed
existing external M5 ledger path. The credential is read only from
OPENAI_API_KEY. A persistent exclusive execution lock plus a fixed new output
directory prevents automatic restart, overwrite or duplicate batches. An
interruption requires review, not deletion of the lock or a budget reset.

## Configuration and accounting

Responses REST, gpt-6-sol, reasoning low, strict frozen JSON schema, no tools,
4096 output tokens, 120-second timeout, no retries and no redirects. No
extra service-tier, cache-policy or temperature fields are added to requests.
The account must use Standard processing; unexpected returned model/tier stops
execution and retains the reservation. A returned model alias is recorded,
not claimed to be an immutable model snapshot.

Official documentation checked 2026-09-28:
[model pricing](https://developers.openai.com/api/docs/models/gpt-6-sol) and
[cache accounting](https://developers.openai.com/api/docs/guides/prompt-caching).
Per million tokens: input $2, cached input $0.20, cache writes $2.50,
output $10. Cache writes replace, rather than add to, the input rate.
All input is reserved at $2.50; no presumed cache-hit discount.
The 100,000-input-per-request ceiling is below the long-context threshold.

Before each generation the input-token endpoint must return an integer within
the frozen limit. The runner reserves `(count * 2.50 + 4096 * 10) / 1,000,000`
before transmission and checks the $7.50 cumulative cap, $6 additional cap,
24 generations, 48 HTTP requests, 2,400,000 input and 98,304 output ceilings.
Failures retain reservations. Cost is reported separately from reservation;
missing cache-write usage leaves exact actual cost unknown. It is never inferred
as zero. No historical ledger is rewritten.

Exact requests, raw success/error response bytes, SHA-256 digests, timestamps,
run/order identifiers, safe request IDs, HTTP status, returned model and usage
are written outside Git. Malformed JSON is retained before parsing. Authorization
headers and exception strings are not persisted. Secret-containing or oversized
bodies stop processing and are not retained. Transport failures have no response
body to preserve. No output repair or retry is performed.

## Offline calculation — an estimate, not exact provider token counts

No local exact tokenizer or authenticated token-count call was used. Serialized
UTF-8 byte counts supply a conservative planning proxy, capped at the existing
100,000-token per-call ceiling. This is **not a certified bound on hidden provider
framing** and must not be reported as exact input-token usage. There is no
justification for claiming an exact offline count or a mathematically tight
provider-token bound. Mandatory live counts, not this proxy, govern expenditure.

| Question | Model-only bytes | Grounded bytes | Combined input proxy |
|---|---:|---:|---:|
| M7-01 | 2282 | 109031 | 102282 |
| M7-02 | 2293 | 87978 | 90271 |
| M7-03 | 2273 | 92132 | 94405 |
| M7-04 | 2341 | 109387 | 102341 |
| M7-05 | 2234 | 27887 | 30121 |
| M7-06 | 2260 | 47915 | 50175 |
| M7-07 | 2288 | 85367 | 87655 |
| M7-08 | 2271 | 26724 | 28995 |
| M7-09 | 2280 | 88365 | 90645 |
| M7-10 | 2298 | 94222 | 96520 |
| M7-11 | 2280 | 66959 | 69239 |
| M7-12 | 2353 | 78543 | 80896 |

Total input proxy **923,545**; maximum output **98,304**.
Planning cost: `923545 * 2.50 / 1e6 + 98304 * 10 / 1e6 = $3.2919025`.
Prior unchanged reservation **$1.544974**; cumulative estimate **$4.8368765**.
All 24 fit this conservative estimate, but exact all-call affordability remains
conditional on provider counts. The full frozen token ceilings at current rates
would cost $8.528014 cumulatively; the runner stops before a request that would
exceed $7.50 rather than changing the experiment.

Dry-run command (private artifacts never enter requests):

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=tools:/private/tmp/ot2606-duckdb-inspection:/private/tmp/dementiagraph-m1-task008-pyshacl python3 tools/run_m7_challenge.py --private-directory /Users/subramanyaprasad/dementia-kg-ai-private/m7-portfolio-challenge-001
```

## Verification

Focused mock controls cover exact request/config/order integrity, no dry-run
network activity, explicit live authorization, 24-generation ceiling, 48-request
execution, API/transport failure without retries, raw-byte preservation, immutable
run directories, changed historical ledger rejection, cache-write cost arithmetic,
and pre-generation/counted-request budget denial. Shared M5 and frozen M7
regressions are run alongside them. No live API calls or scoring were performed.

Verification outcome: **73 relevant tests passed** (15 new execution controls and
58 existing M7 freeze/protocol and M5 adapter/evidence/retrieval/follow-up tests).
The combined 72-test run passed, then the final 15-test execution suite passed
including the added mid-batch cap control. That control admits 20 maximum-count
requests, rejects the 21st generation, and retains $7.364174 cumulatively.
Python parsing and Git whitespace checks passed. Public and private freeze
verification passed during the offline dry run. No frozen file changed.
