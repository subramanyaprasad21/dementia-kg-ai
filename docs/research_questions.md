# Research questions

Status: **M0–M7 development complete.** This file is the living research summary. The exact M0-era version named by the historical freeze is preserved at [`archive/frozen/ot2606-evidence-001/docs/research_questions.md`](../archive/frozen/ot2606-evidence-001/docs/research_questions.md); its manifest and SHA-256 authority remain unchanged.

## Current research framing

The project asks how far a bounded, provenance-aware dementia knowledge graph can support evidence-grounded answering while preserving source scope, and what a deterministic local verifier adds once retrieval and generated evidence are fixed.

The final implementation separates four questions that were intertwined in the early design work:

1. **Evidence support:** can generated structured assertions be tied back to exact RDF statements and cited source records?
2. **Scope preservation:** can the system avoid turning narrower source statements into broader disease, population, treatment or equivalence claims?
3. **Verification effect:** does the local assertion/citation/type verifier reject unsupported submitted assertions or otherwise change the retained grounded output?
4. **Answer completeness:** even when retained assertions are supportable, does the generated answer use the required evidence completely enough to answer the question?

These questions are deliberately narrower than claims about biomedical truth, clinical validity or graph superiority.

## Design boundaries retained from M0–M6

The early research design identified recurring failure boundaries that remain relevant to the completed system:

- citation presence is not the same as claim support;
- shared or dependent evidence records must not be counted as independent confirmation;
- a normalized disease identifier does not erase the narrower source label or population;
- direct and descendant-inclusive retrieval are different selections;
- a mapping does not establish unconditional semantic equivalence;
- mechanism evidence is not treatment indication or efficacy evidence;
- a graph path is not clinical adjudication;
- missing or uninspected evidence is not a negative biological fact.

These constraints informed Q01–Q07, the ontology/SHACL design and the later M7 challenge. They define properties the system can check locally; they do not establish biomedical correctness.

## What was actually evaluated

M7 used a **12-question development-overlapping portfolio challenge**, not an unseen holdout benchmark.

Two generation conditions were executed for each question:

- **model-only**: no graph evidence packet;
- **grounded**: the bounded evidence packet supplied to the model.

The **verified** condition is the same grounded generation after deterministic local assertion/citation/type checks. It is not a third model generation.

The recorded run produced:

- **24 generated responses**: 12 model-only and 12 grounded;
- **55 structured grounded assertions**;
- **55/55 assertions accepted** by the local deterministic verifier;
- **0.0 verification-minus-grounded assertion-precision difference** on this run;
- **68.0556% single-reviewer strict required-fact completion** for grounded and verified answers.

See [M7 findings](m7_owner_evaluation_findings.md) and [M7 execution results](m7_portfolio_results.md) for the exact scoring and provenance.

## Interpretation

The completed evaluation supports a limited conclusion: the submitted grounded assertion records were locally supportable under the implemented verifier, while complete use of all required evidence remained substantially harder.

The run does **not** show that verification improved the grounded outputs, because the verifier rejected none of the 55 submitted grounded assertions. It also does not establish that graph retrieval is superior to lexical/vector retrieval, that the answers are clinically valid, or that the observed performance generalises to unseen questions.

The result therefore shifts the strongest open question from simple assertion support toward **evidence use and completeness**: when the relevant evidence is available, what causes a grounded answer to omit, compress or fail to integrate required facts?

## Research questions that remain open

The current repository leaves several questions for a stronger follow-up study:

1. Does the verifier add measurable value on adversarial or naturally occurring outputs that contain unsupported structured assertions?
2. Does a graph retrieval condition outperform lexical/vector alternatives when the compared systems receive matched information and comparable budgets?
3. Does the 68.0556% required-fact completion result persist on genuinely unseen questions?
4. How much do independent reviewers agree on required-fact, relevance and scope-preservation judgements?
5. Which failures arise from retrieval coverage, evidence-packet construction, model evidence integration or answer-generation behaviour?

Those are future research questions. They are not claims established by the present portfolio experiment.

## Historical design record

The original M0 research framing intentionally left the exact experiment, metrics, sample size and graph-advantage claim unresolved. That historical state is retained byte-for-byte in the frozen archive rather than rewritten to match later outcomes:

- [Frozen M0-era research questions](../archive/frozen/ot2606-evidence-001/docs/research_questions.md)
- [Historical decision record](decisions/README.md)
- [Current evaluation protocol](evaluation_protocol.md)

This separation keeps the development history auditable while allowing the living project documentation to describe the completed M0–M7 system accurately.
