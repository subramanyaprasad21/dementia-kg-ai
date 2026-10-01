# M5 OpenAI integration — offline implementation and proposed pilot

Status: **offline integration implemented; no live request was executed during this implementation stage**. The recorded configuration covers offline preparation, tests and local integration only. This is not M5 scientific closure, a held-out experiment or biomedical validation. Baseline: `5bbedb102eeadae5dfac67fc702724a9cf259316`.

## Architecture and behaviour

1. `m5_evidence_answers.prepare` reuses M4 hybrid/graph/vector retrieval against the pinned qualified corpus. It supplies the research question, exact packet assertions, source locators and identifiers, retrieval status, known unresolved inputs and an abstention signal. It hashes the complete request and records the corpus manifest hash and prompt version. Empty grounded retrieval needs no model call.
2. `m5_openai_adapter` is a single-provider adapter for the supported OpenAI Responses REST API using Python's existing HTTPS library. The OpenAI SDK is not installed; no package installation or multi-provider layer is necessary. A live run first counts input tokens, reserves maximum generation cost, then makes one generation request. No retries, redirects, tool use or fallback model.
3. Structured responses separate `answer_text`, claims (packet ID, exact asserted statement, claim type, candidate explanation), and unanswered parts. Model generation does not write assertions back into the KG.
4. Local verification replays retrieval and rejects changed requests/evidence, citations outside the returned packets, invented statement text and duplicate claims. Valid statements retain packet hashes, source locators and source versions. A returned exact statement is labelled **RDF-ASSERTION-SUPPORTED**, never clinically correct.
5. Biological causality, efficacy, independence, source completeness and biological absence are not established by this bounded checker. Candidate explanations and the overall generated prose remain **UNVERIFIED-MANUAL-REVIEW-REQUIRED**, even when a citation is valid. Only exact asserted facts enter `acceptedAssertions`. Zero accepted facts yields qualified insufficiency, not biological negation. Refused, incomplete, malformed or unaccounted API responses stop the run.

This is a deliberate limit: a model could label an inaccurate paraphrase as a source assertion. The system does not certify that paraphrase; it preserves it for review and presents exact source assertions separately. It does not yet automatically adjudicate prose relevance or semantic entailment. A meaningful later evaluation must measure useful completion and excessive withholding as well as unsupported claims. Do not describe citation matching as general claim verification.

All source/ontology identities, M1–M4 artifacts and exposed Q01–Q07 remain unchanged. Manual anchors and type filters still route the finite questions; unrestricted natural-language entity grounding and arbitrary query generation are not claimed. The earlier whole-question interface with extra source intermediates remains separate from this RDF-only model input.

## Three experimental conditions, no superiority claim

| Condition | Model input | Output handling |
|---|---|---|
| Model only | Question and shared JSON schema; no KG packets, answers or known corpus gaps | Unverified model-knowledge control; no accepted assertions |
| Retrieval | Question, bounded RDF evidence and qualifications | Preserve raw generated text/claims as unverified |
| Verified | **Same request and same generated response as retrieval** | Deterministic assertion checks, provenance attachment and qualified withholding |

Reuse of the grounded generation isolates this postprocessing intervention and saves calls. It does not test a different generation prompt or an independent second model. Model-only necessarily has different information access, so it is not the fixed-evidence primary contrast. Final metrics, interpretation, reviewers and held-out protocol remain undecided. No new held-out material or paraphrases are created.

## Model and request configuration

Proposed engineering default: **`gpt-6-sol`**, Responses API, `reasoning.effort=low`, `max_output_tokens=4096`, `store=false`, no tools, strict JSON Schema. Prompt version: **`m5-evidence-answer-1`**. The official model page documents Responses and structured-output support and currently instructs using the alias; no separately documented immutable snapshot is invented. The requested and returned model identifiers are recorded. Fixed configuration and request hashes support replay, but alias changes and stochastic generation prevent a claim of byte-identical future generations. No unsupported seed or temperature setting is assumed. [Official model documentation](https://developers.openai.com/api/docs/models/gpt-6-sol).

JSON shape is enforced again locally; API formatting success does not establish answer truth. Refusals and incomplete output are handled explicitly. [Structured outputs](https://developers.openai.com/api/docs/guides/structured-outputs).

The adapter uses `POST /v1/responses/input_tokens` before generation, with the same model/input/instructions/tools/text schema. This avoids pretending serialized bytes are an exact tokenizer count. Reported output-token limits include non-visible tokens. [Token-counting documentation](https://developers.openai.com/api/docs/guides/token-counting).

## Proposed pilot — execution controls

Machine plan: `assessments/m5-pilot-plan.json`. It extracts the exact seven core Q01–Q07 texts, not the historical alternative questions. Each uses the existing M4 manually specified anchors and record types, with at most five packets / 65,536 encoded packet bytes. Those routes supply partial RDF context; they do not make all seven questions answerable. In particular, Q04's external counts and registry population evidence are unavailable to the model.

- Seven model-only generations + seven grounded generations = **14 maximum generations**.
- Verify each grounded response offline to obtain the third condition, with no extra model calls.
- At most **14 token-count requests**, hence **28 HTTP requests**. No automatic smoke test, retry or repair loop outside this batch.
- Hard per-generation ceilings: **100,000 counted input tokens / 4,096 output tokens**.
- Aggregate ceilings: **1,400,000 input / 57,344 output tokens**.
- Serialized requests total approximately 387 KB. A rough 2–4 bytes/token planning heuristic suggests roughly **97,000–194,000 input tokens** in total; it is not a tokenizer result. Exact values remain unknown until live token counting. Actual output lengths are unknown; budget the full 57,344-token maximum.
- Verified Standard short-context prices on 2026-09-26: **$2 per million input tokens and $10 per million output tokens**. Ignoring cache discounts, the conservative generation-token bound is **$3.37344**; the rough input range plus maximum outputs suggests approximately **$0.77–$0.97**. Recorded pilot spending cap: **$5**. No Fast mode, region premium, tools or long-context threshold is requested. Recheck rates before a paid run; the dollar calculation is not a provider billing guarantee. [Official pricing](https://developers.openai.com/api/docs/pricing).

The local ledger reserves the worst-case generation amount before the call and never refunds failures automatically. Every actual request is counted; a crash/incomplete attempt, unexpected usage, changed limits or exhausted budget stops continuation. The same batch directory must be reused; creating a fresh directory does not reset the recorded budget. A serial lock prevents concurrent spending through one ledger. The adapter assumes its local ledger is retained intact; it is not an account-wide billing control.

## Credentials, records and permissions

Read the key only from `OPENAI_API_KEY` in the adapter process. No `.env` loader, credential-file reader or key argument exists. If absent, fail clearly. Configure it locally through the execution environment or secret manager; a variable set in an unrelated terminal is not automatically inherited by another process. Do not send a key in chat or place it in shell commands, repository files or examples.

`.gitignore` excludes `.env` variants, credential/secret directories, common key-file names and local runs. Git ignore is not a content scanner and cannot protect a key deliberately written into tracked source; all new files must still be reviewed before staging. No real credential was read or used during tests. Tests generate nonfunctional random markers solely to check non-persistence.

Run artifacts must be outside the repository. They contain the request/configuration, prepared evidence, response bytes, request/response hashes, returned model, response ID, token usage, run UUID and results. Authorization headers and exception bodies are never logged. Credential echoes in input or responses are rejected before retention. `store=false` is not claimed to eliminate all provider retention; no new article bodies or confidential records are included in requests.

## Offline use and live execution

```sh
export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH=tools:/private/tmp/dementiagraph-m1-task008-pyshacl
python3 tools/m5_evidence_answers.py prepare 'What mechanism does the source report for gosuranemab?' --anchor CHEMBL3990042 --type MechanismRecord --mode graph --out /private/tmp/m5-prepared.json
python3 tools/m5_pilot_plan.py
python3 -m unittest discover -s tests -p 'test_m5_*.py' -v
```

`m5_openai_adapter.py` requires `--approved-pilot` and `OPENAI_API_KEY` before any network access. The flag is an explicit execution guard for a live run; this document does not enable it. Use it only after the model, budget and execution scope have been reviewed. Passing `--condition retrieval` generates once and records both retrieval and verified outputs. `model_only` uses no retrieved input. Normal regression tests inject a stub transport and incur no API charges.

## Verification and limitations

Twenty focused tests passed: positive cited assertions, invented/mismatched citations, unsupported interpretation, prompt/evidence mutation, duplicate support, no-evidence abstention, refusal/incomplete output, baseline separation, budget ceilings, failure retention, no redirects/retries, secret non-persistence and deterministic pilot preparation. An initial pilot parser also matched historical alternatives; it was restricted to the seven core headings before the plan was recorded. No source observation was altered.

Full regression results are appended after the integration run. Live model/API compatibility, account model access, generated-answer quality and cost remain **NOT YET TESTED**. All synthetic controls are explicitly labelled and are not reported as model results. This implementation prepares M5; it does not close M5 or establish clinical correctness, source completeness or graph advantage.

### Completed integration verification

**264 tests passed in 306.636 seconds**, including all 244 previous regressions and 20 new M5 tests. Focused M5 verification also passed independently (20 tests, 11.505 seconds). The full run used the existing Python 3.12.7 / RDFLib 7.1.4 / pySHACL 0.30.1 / owlrl 7.1.4 / DuckDB 1.5.5 environment. No dependencies were installed.

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=tools:/private/tmp/ot2606-duckdb-inspection:/private/tmp/dementiagraph-m1-task008-pyshacl python3 -m unittest discover -s tests -v
```

Local log: `/private/tmp/dementia-m5-regression.log`. Final request construction was exercised through the CLI and validated offline, with no provider call. Syntax and Git diff checks passed. No pre-existing tracked file changed. The new files are `.gitignore`, `assessments/m5-pilot-plan.json`, this report, `tools/m5_evidence_answers.py`, `tools/m5_openai_adapter.py`, `tools/m5_pilot_plan.py`, `tests/test_m5_evidence_answers.py`, and `tests/test_m5_openai_adapter.py`. No key, raw source body or live model output is included.
