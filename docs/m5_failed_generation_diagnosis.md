# M5 first generation: offline diagnosis

## Scope and conclusion

No network requests, credential access, SDK installation, live retries or budget resets were performed for this diagnosis. The first failed attempt remains untouched. This is engineering diagnosis, not a pilot result.

**No specific root cause can be recovered from the retained evidence.** The saved generation request passes local replay, approved-contract checks, JSON serialization and JSON Schema meta-validation. An API rejection specific to generation is plausible; a transport/read failure is also possible. There is no defensible basis to rank model access, billing, reasoning compatibility or schema rejection individually. The confirmed implementation defect is that the old adapter discarded the HTTP status and error classification.

A successful token-count request does not prove that the generation endpoint accepts the account/model/configuration. In particular, the counting payload omitted `reasoning`, `max_output_tokens` and `store` by design. Do not change those approved generation fields on speculation.

## Exact retained context

External run directory: `/Users/subramanyaprasad/dementia-kg-ai-model-runs/m5-pilot-001`.

| Artifact | SHA-256 |
|---|---|
| `001.request.json` (2,256 bytes) | `ff99b45a4c45bbbbe3b8d77e48114de78df9121cf8f5955baddbcc09bc97e6b9` |
| `001.prepared.json` | `304c65bb0289b49b7b49f93384bdc2cb1eadc8949a834313d30c356751ec5ef4` |
| `ledger.json` | `7bd6bca5239362ff2f8f9768c9c0f915e873c51c3354ddedd12c6a44b2db7c78` |

The ledger records Q01's model-only attempt, 224 counted input tokens, two HTTP invocations, one generation attempt and USD 0.041408 reserved. Status is `failed-review-required`. There is no retained response file, HTTP status, provider error code, request ID, usage or output. Actual charge is unknown. An invocation count is not proof of successful transmission.

The attempt ran from 2026-09-26T17:18:23.424845+00:00 to 17:18:27.592340+00:00, including counting. This does not resemble exhaustion of the configured 120-second timeout, but cannot exclude an earlier network failure.

## Local request inspection

| Item | Recorded value / result |
|---|---|
| Model | Exact `gpt-6-sol`; no substitution |
| API | Direct REST `POST https://api.openai.com/v1/responses` |
| Reasoning | `{"effort":"low"}` |
| Structured output | `text.format`: `type=json_schema`, `name=dementia_evidence_answer`, `strict=true` |
| Schema | Root object; every object has all properties required and `additionalProperties=false`; string/array/object fields and finite claim enum |
| Output limit | `max_output_tokens=4096` (not Chat Completions `max_tokens`) |
| Tools / storage | `tools=[]`, `store=false` |
| Input | String containing the approved model-only question JSON; no evidence packets |
| Serialization | UTF-8 deterministic JSON; exact saved bytes reproduced, round-trip equal |
| HTTP construction | Standard-library `urllib.request.Request`; fixed endpoint, POST, JSON content type |
| Timeout / retries | 120 seconds; zero automatic retries; redirects denied; environment proxies disabled |

The recorded request equals `request_for(saved_prepared, 'model_only')`, including the approved prompt and schema, after frozen-corpus verification. `jsonschema.Draft202012Validator.check_schema` passes. This proves JSON Schema well-formedness, not that a particular provider/model accepts every field.

No OpenAI SDK is installed in the inspected Python 3.12.7 environment. The failed path never used SDK request objects or serialization, so an SDK serialization error is excluded for this attempt. No SDK object-construction test is possible without installing one; none was installed. The existing `jsonschema` 4.25.1 dependency was used for offline schema checking. No fresh API documentation was fetched under the offline-only instruction. Account access and current server-side model compatibility remain unverified.

## Minimal diagnostic correction

`tools/m5_openai_adapter.py` now validates this finite approved request contract before HTTP construction and reports closed-vocabulary failures for endpoint, serialization, field set, model, reasoning, tools and structured-output deviations. It does not purport to be a universal API validator or to verify server-side model support.

Transport diagnostics distinguish local construction failure (not sent), HTTP rejection (response received), timeout/connection failure (transmission unknown), unsafe/oversized response and an unclassified client/read failure. HTTP error bodies are inspected only in bounded memory (at most 65,537 bytes); raw bodies are never saved. Only numeric HTTP status and allowlisted `code`, `type`, and `param` values survive. Unknown classifications are recorded as `unclassified`. Provider messages, all headers, request IDs, arbitrary parameter strings and exception text are excluded. Any body containing the supplied credential is not classified. This intentionally trades some detail for secret safety.

Future failed attempts retain the safe diagnostic in their ledger entry. Reservations, request accounting, failed-attempt blocking and no-retry behavior remain unchanged. Existing historical entries are not rewritten or backfilled with invented metadata. Prompt, model, endpoint and scientific conditions remain unchanged.

## Verification

- Saved request replay and exact byte serialization pass with network opening patched to fail.
- 27 focused M5 tests pass, including seven new diagnostic tests.
- Synthetic controls exercise invalid fields/schema/reasoning/model, serialization failure, wrong endpoint, pretransmission construction failure, HTTP rejection, secret suppression, timeout/connection classification, exact POST construction and unchanged reservation/resume blocking.
- Synthetic controls are not actual API responses or biomedical evidence.
- Full regression: **271 tests passed in 303.833 seconds**, including all 264 prior tests. `git diff --check` passes.

## Next decision

The minimal fix is diagnostic instrumentation, not a speculative model/configuration change. No API retry is authorized by this task. A future approved attempt must preserve the failed attempt and cumulative budget; the existing failed-ledger guard must not be bypassed by deleting/resetting the ledger or creating a fresh budget. Any deliberate resume mechanism requires separate handling and must retain the previous reservation. No comparative AI results exist yet.

## Owner-authorized diagnostic retry

The owner subsequently approved exactly one live diagnostic retry, followed by continuation only on success. The retry used byte-identical saved request and prepared evidence, the same model/configuration and the same cumulative ledger. A narrowly explicit `reviewed_failure_ids` argument permits an owner-reviewed historical failure without modifying its entry or releasing its reservation. New failures still block continuation. No automatic retry was added.

**Result: stopped immediately on HTTP 429, `api_type=insufficient_quota`, `category=http_rejection`, `transmission=response_received`.** Error code and parameter were unclassified. Request ID was not retained. This is an HTTP-side rejection, not a transport failure. No further calls were made and no model outputs exist. This classification applies to the retry; it cannot retroactively establish the cause of the original attempt.

Cumulative accounting is four HTTP requests, two generation attempts and USD 0.082816 reserved, including the unchanged original reservation. Actual billing remains unknown. The USD 5 ceiling and original call/token limits were not changed. The original ledger can be reconstructed byte-for-byte by selecting its original entry and counters; its recorded digest still verifies.

Verification: **28 focused M5 tests pass**, including explicit reviewed-failure preservation, cumulative reservation and rejection of a second unreviewed failure. The prior full suite passed 271 tests before this narrow retry-authorization addition. `git diff --check` passes. The sanitized result and ledger snapshot are in `assessments/m5-diagnostic-retry.json`. No secrets, provider message text, HTTP headers or raw error bodies are retained. No further live request is authorized by this result.
