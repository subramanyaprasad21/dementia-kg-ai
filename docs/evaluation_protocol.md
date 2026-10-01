# Evaluation protocol

Status: **M7 executed and scored.** This file is the living protocol summary for the completed portfolio evaluation. The exact earlier protocol named by the historical freeze is preserved at [`archive/frozen/ot2606-evidence-001/docs/evaluation_protocol.md`](../archive/frozen/ot2606-evidence-001/docs/evaluation_protocol.md); its manifest and SHA-256 authority remain unchanged.

## Evaluation purpose

The evaluation tests a bounded research system, not biomedical truth. Its purpose is to separate:

- what the model produces without graph evidence;
- what it produces when supplied with the bounded evidence packet;
- whether submitted grounded RDF assertions survive deterministic local checks;
- whether the resulting answer uses the required evidence completely enough for the question.

The protocol does not treat citation presence, RDF validity or a passing local verifier as proof of clinical correctness.

## Evaluation set

The final M7 package contains **12 development-overlapping questions**. It is a portfolio challenge set, not an unseen holdout benchmark.

The questions reuse concepts, evidence patterns and semantic boundaries encountered during M0–M6. This was disclosed before interpretation, so the results cannot estimate unseen-question generalisation.

The evaluation uses one curator/reviewer. There is no independent clinical adjudication and no inter-rater agreement result.

## Compared conditions

Each question has two model-generation conditions:

| Condition | Evidence supplied to model | Model generation |
| --- | --- | --- |
| Model-only | No graph evidence packet | Yes |
| Grounded | Frozen bounded evidence packet | Yes |
| Verified | Same grounded output after deterministic local checks | No additional generation |

The verified condition therefore isolates the implemented post-generation verifier. It does not receive a second chance to rewrite or repair the grounded answer.

The recorded run produced **24 generations**: 12 model-only and 12 grounded. Verified reuses the 12 grounded outputs.

## Fixed execution controls

The M7 execution record freezes the question package, retrieval scopes, prompts, structured response schema, model identifier, token ceilings, timeout rules, budget controls and failure handling for the recorded run.

Key controls include:

- no silent prompt trimming;
- no silent repair of model output;
- no replacement of failed outputs with hand-written answers;
- exact request/result persistence;
- deterministic replay of the committed public package;
- separate accounting for generation and verification;
- retained failed/unused states rather than provenance deletion.

The public replay path is offline and makes no model call.

## Deterministic verification

The local verifier checks the structured grounded assertions against the committed RDF/evidence representation. Its scope is deliberately limited to properties the repository can determine mechanically, including exact assertion/citation/type consistency.

It does **not** establish:

- biomedical truth;
- clinical efficacy;
- causal validity;
- completeness of the generated prose;
- correctness of unsupported model-only background knowledge.

In the recorded M7 run, **55 structured grounded assertions were submitted and all 55 passed**. The verified condition therefore retained the same 55 assertions and the same grounded prose.

## Human review and metrics

Single-reviewer scoring records required-fact completion and question-level observations separately from deterministic RDF verification.

The principal reported outcomes are:

- grounded structured assertions accepted by the local verifier: **55/55**;
- verification-minus-grounded paired assertion-precision difference: **0.0** on this run;
- strict required-fact completion, macro over 12 questions: **68.0556%** for grounded and verified answers.

Model-only emitted no comparable structured assertion records, so its structured assertion precision is **undefined**, not zero and not perfect.

The reviewer annotations are review-derived labels, not independent gold-standard clinical judgements.

## Interpretation rules

The evaluation supports only claims warranted by the recorded contrast.

A passing local assertion check means that the submitted structured assertion was supportable under the implemented repository rules. It does not mean the answer is complete or clinically correct.

The absence of verifier rejections means this run provides **no evidence of incremental verifier benefit** over the submitted grounded assertions. It does not show that the verifier is useless in general; the evaluated outputs simply did not exercise a rejection case.

The **68.0556% required-fact completion** result shows that local support and answer completeness are different properties. A grounded answer can avoid unsupported retained assertions and still omit relevant required evidence.

No result in this protocol establishes graph superiority, unseen-question generalisation, clinical validity or statistical superiority.

## Reproducibility

The committed public path can be replayed offline after installing the pinned project dependencies:

```sh
export PYTHONPATH=tools:tests
python tools/development_corpus.py verify
python tools/characterise_development_graph.py
python tools/replay_development_retrieval.py
python tools/m7_challenge_freeze.py
python tools/replay_m7_challenge.py
python tools/m7_owner_metrics.py
```

The key evaluation records are:

- [M7 protocol proposal and amendments](m7_protocol_proposal.md)
- [M7 execution results](m7_portfolio_results.md)
- [M7 single-reviewer findings](m7_owner_evaluation_findings.md)
- [`evaluations/m7-portfolio-challenge-001/`](../evaluations/m7-portfolio-challenge-001/)
- [`experiments/m7-portfolio-challenge-001/`](../experiments/m7-portfolio-challenge-001/)

Full upstream source-capture replay still requires the original external raw artifacts; the committed public corpus and evaluation replay do not silently fetch replacements.

## Limitations

The completed evaluation has four main limits:

1. the 12 questions are development-overlapping rather than unseen;
2. scoring uses one reviewer with no independent clinical adjudication;
3. the verifier saw no rejected grounded assertion in the recorded run, so incremental verifier benefit was not demonstrated;
4. the bounded corpus and model identifier do not establish performance outside this recorded configuration.

These limits are part of the result and should remain visible in any CV, application, report or future comparison.

## Historical protocol record

The earlier protocol documents the original staged plan, contamination concerns, matched-access requirement, scope-control criteria and unresolved held-out design. At that stage, the final metrics, benchmark size, statistical treatment and held-out mechanics were intentionally still open. That record remains available exactly as frozen:

- [Frozen historical evaluation protocol](../archive/frozen/ot2606-evidence-001/docs/evaluation_protocol.md)
- [Historical research questions](../archive/frozen/ot2606-evidence-001/docs/research_questions.md)
- [Historical decision record](decisions/README.md)

The living protocol above reports what was ultimately executed. The frozen files preserve what was known and undecided at the earlier milestone.
