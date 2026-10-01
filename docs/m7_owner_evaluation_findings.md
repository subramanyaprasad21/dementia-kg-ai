# M7 evaluation findings

## Review provenance and limits

This records the completed single-reviewer scoring of
M7-01–M7-12. The exact instructions are preserved in
[`owner-review-instructions.txt`](../experiments/m7-portfolio-challenge-001/owner-review-instructions.txt).
Subramanya Prasad is the sole curator/reviewer. Strict fact-completion decisions
and question observations were supplied directly during manual review. Proposition
segmentation, line-level labels, assertion relevance/provenance judgments and
boolean rubric operationalization were entered during the same review process
under sections E/F of those instructions. They are **review-derived annotations**,
not a fresh independent attestation for every line or independently authored gold.

The completed [worksheet](../experiments/m7-portfolio-challenge-001/consolidated-owner-review.md),
[annotations](../experiments/m7-portfolio-challenge-001/owner-review-scores.json)
and [metrics](../experiments/m7-portfolio-challenge-001/owner-review-metrics.json)
retain this distinction. Frozen questions, answers, structured claims, automated
verification, rubric, required facts and M0–M6 design are unchanged. No model call,
source acquisition, outside biomedical fact, answer repair or rubric change was
used. The original blank worksheet remains available in commit `14dcbcb`.

This is a **development-overlapping portfolio challenge set**, not an unseen
holdout benchmark. There is no clinical-validity, independent-validation,
statistical-generalization or system-superiority claim. No inter-rater agreement
is calculated. The project and wider research are not declared finished.

## Intentional no-retrieval baseline

Model-only intentionally received no project KG or evidence corpus. Its inability
to supply corpus-specific facts is expected, **not a retrieval failure**. It
shows the base model's behavior without project evidence: uncertainty handling,
general reasoning, outside knowledge and whether that knowledge is represented
as corpus evidence. Its lack of structured assertions also leaves assertion
precision undefined, not zero and not perfect.

Grounded received the fixed retrieved project evidence. A grounded completeness
concern here means relevant material was available but the generated answer did
not convey the entire required fact. This differs from model-only's intentional
lack of access. These are not one generic “AI gap”.

## Reviewer observations by question

| Question | Grounded strict facts | Reviewer finding and distinguishing issue |
|---|---:|---|
| M7-01 | 2/2 | Required mechanism projections, identifiers, mechanism text and shared source context were used. Grounded worked as intended. Model-only fenced its memantine/ketamine/NMDA background off from graph claims. |
| M7-02 | 2/2 | Disease destinations, GE input and Europe PMC missingness were recovered. Grounded worked as intended. Model-only fenced general PSEN1/familial-AD knowledge off from mapping claims. |
| M7-03 | 2/3 | APP mapping and hierarchy were used; the separate APP-indexed lecanemab mechanism and AD indication were omitted. Candidate cross-record/cross-relation evidence-integration omission, not an established retrieval or ontology failure. |
| M7-04 | 1/2 | Shared nct00594737 and APP genomics_england distinction were conveyed; PMIDs 22503161, 23028126 and 2111584 were omitted. Citation/source-detail completeness gap; main shared-study answer correct. Model-only cleanly abstained. |
| M7-05 | 1/1 | MONDO_0017276 and source maximum PHASE_1 with limitations were conveyed. Grounded worked as intended. Model-only's fenced phase-2 background differs from the corpus-specific recorded stage; this is a scope contrast, not evidence that either is universally current. |
| M7-06 | 1/1 | Exact three-step MONDO path conveyed. Grounded worked as intended. Model-only's explicitly unverified simplified hierarchy does not establish the recorded path; it had no retrieval by design. |
| M7-07 | 1/2 | Non-causation boundary preserved; detailed Pick/OMIM:600274, FTD/semantic-dementia and bounded grouping context omitted. Source-context completeness gap, with good causal qualification. |
| M7-08 | 1/2 | Efficacy inference correctly withheld; complete CHEMBL3833321, APP-indexed mechanism, exact mechanism text and separate APPROVAL-stage AD indication details omitted. Distinct model-only trial-outcome/ARIA scope leakage and grounded mechanism/indication-detail omission. |
| M7-09 | 1/1 | Actual shared nct00594737 evidence supplied; grounded worked as intended. Model-only offered a sound general independence caution without pretending to know the records. |
| M7-10 | 0/1 | Phase-not-outcome boundary preserved, but the compound fact requires both StudyRecords, shared nct00594737 and clinical_precedence. Study/provenance-detail omission. Model-only separately introduced external memantine-benefit knowledge. |
| M7-11 | 1/2 | Complete historical total correctly withheld and fixed-scope limitation retained; enumerated recovered PSEN1 literature occurrence omitted. Local scope/count-context omission, mainly corpus accounting rather than biomedical inference. Model-only avoided inventing a total. |
| M7-12 | 1/2 | PSEN1-specific prescribing inference correctly rejected; full PSEN1→AD, lecanemab AD indication and APP-indexed mechanism chain omitted. Cross-record evidence-chain omission. Model-only separately introduced outside treatment eligibility/prescribing information. |

### Successful and incomplete grounded cases

Preserve **M7-01, 02, 05, 06 and 09** as successful required-evidence-use examples.
Preserve **M7-03, 04, 07, 08, 10, 11 and 12** as different completeness issues,
not seven interchangeable failures. Their main answers were often correct while
supporting source facts or provenance details were incomplete. Main-answer
correctness, strict required-fact completeness, provenance/detail completeness
and qualification are separate dimensions; there is no combined overall score.

The selected source evidence was present in the frozen material. Cause remains
unresolved: retrieval ranking, packet/evidence selection, question interpretation,
answer planning and generation/evidence integration have not been isolated by
this experiment. Do not infer that retrieval failed or the ontology is defective.
No new ablation, mechanism-of-failure experiment or causal attribution is added.

### Two levels of model-only outside knowledge

- **Fenced background:** M7-01, 02, 03, 05 and 06 explicitly separated background
  knowledge/guesses from what the graph records. Corpus-unsupported propositions
  remain labelled U (or R for the unverified simplified path), but these are not
  automatically major failures or claims of biomedical falsehood.
- **Stronger clinical/treatment scope leakage:** M7-08 (trial outcomes and ARIA),
  M7-10 (memantine clinical benefit) and M7-12 (treatment eligibility, diagnosis,
  amyloid confirmation, prescribing/safety criteria). These were not supplied by
  the evaluation corpus. They are recorded separately as scope-control concerns.
- **Clean abstention/general reasoning:** M7-04 cleanly abstained. M7-07, 09 and
  11 primarily used general logical/methodological principles without pretending
  to know project-specific facts.

## Existing metrics, unchanged definitions

`tools/m7_owner_metrics.py` is an offline input/provenance wrapper around the
unchanged `m7_protocol_checks.aggregate`, `retrieval_coverage` and
`paired_precision_difference`. It does not infer labels or redefine a metric.
All 12 outcomes per condition remain completed; there are no retrieval failures
assigned to model-only and no generation failures removed from a denominator.

| Descriptive metric | Model-only | Grounded | Verified |
|---|---:|---:|---:|
| Completed outputs | 12/12 | 12/12 | 12/12 (same grounded generations) |
| Retained assertions | 0 | 55 | 55 |
| Assertion support precision | Undefined (0 defined items) | 100% (12 defined items) | 100% (12 defined items) |
| Retained relevance / provenance accuracy | Undefined | 100% / 100% | 100% / 100% |
| Strict required-fact recall, macro over 12 questions | 0% | 68.0556% | 68.0556% |
| Zero-retained rate | 100% | 0% | 0% |
| Unsupported/contradicted prose rate, per-item macro | 17.9167% | 0% | 0% |
| Unresolved prose rate, per-item macro | 6.25% | 1.85185% | 1.85185% |
| Qualification pass | 9/12 | 12/12 | 12/12 |
| Strict source-scoped required-abstention pass | 0/6 | 6/6 | 6/6 |
| Excessive abstention on answerable questions | 0/6 | 0/6 | 0/6 |

Verification-minus-grounded paired assertion-precision difference is **0.0** on
12 defined pairs. This shows no filtering effect on the submitted assertions in
this run, not superiority. Grounded and verified prose, fact decisions and prose
labels are identical. Structured assertion support does not certify prose
completeness. The manual fact decisions yield 14/21 facts in total; the frozen
primary completion aggregation is the **per-question macro mean**, not 14/21.

### Scoring qualifications that matter

All factual surfaces (answer text, claim explanations, factual unanswered-field
statements) are considered. Exact copied propositions are counted once with
surface membership retained. Questions and nonfactual disclaimers are excluded.
Unsupported means unsupported **by the allowed corpus**, not medically false.
R is used for unresolved interpretations, not to invent a supported answer.

M7-04 has a narrow explanation-level ambiguity: two claim explanations attach
GRIN1/GRIN3B names to particular occurrence IDs; their source triples use Ensembl
identifiers. Those two explanation assignments are labelled **R**, not silently
validated by their accepted study-link triples. This does not change the recorded
shared-study main-answer or strict fact decisions. Further identity adjudication
is not performed and no source/model record is repaired.

The frozen private abstention rubric additionally calls for a source-scoped
explanation retaining useful required facts. Model-only's appropriate general
caution does not satisfy that full source-specific conjunction, hence 0/6; this
is **not** a claim that all its reasoning is poor or that its retrieval failed.
Grounded preserves useful source facts and boundaries even when a compound fact
is incomplete (notably M7-10). Strict fact completion and qualification are not
silently equated. Model-only Q08/Q10/Q12 qualification failures specifically
record the corpus-scope leakage concerns. No excessive abstention is
inferred merely from model-only's intended absence of evidence.

## Retrieval coverage versus completion

The G/V supplied packet unions contain the exact frozen reference witnesses for
all 21 fact slots: per-question coverage **1.0 for all 12** under the unchanged
coverage function. Model-only coverage is **not applicable**, not a retrieval
failure or unsuccessful retrieval.

`owner-review-scores.json` records the exact assertion witnesses and request
hashes separately from fact-completion labels. The fact IDs and underlying
reference assertions were frozen before generation; the fact-to-assertion
witness index is a **post-generation review annotation**, not
claimed to have been independently frozen as a new gold artifact. Thus coverage
is a transparent retrospective check of supplied material, not evidence of
upstream completeness or an independent retrieval benchmark.

For M7-03/04/07/08/10/11/12, supplied evidence can be sufficient while strict
answer completion is N. Exact source IDs are retained; labels such as semantic
dementia are the frozen rubric's interpretation of MONDO_0010857, not a new
label inserted into a packet that lacks it.

## Status and remaining work

Manual scoring and structured error analysis are recorded.
The source-instruction-to-annotation distinction, unresolved explanation labels,
proposition boundaries and retrospective witness indexing remain auditable
limitations; no independent review is claimed. The exact scoring input and
machine-readable metrics are available for later reassessment or independent review.

Broader research and M8 packaging remain outside this evaluation; no M8 release
work is included here. The historic execution report and blank review templates
remain identifiable as earlier states.

## Verification

**25 relevant tests passed, 0 failed**: six new review-transcription/metric checks
plus the existing M7 protocol, freeze and recorded-result replay tests. Tests
verify the exact review fact matrix, identical grounded/verified labels, unchanged
question/answer/rubric sections, raw-archive hashes, exact existing-metric replay,
prose surface traceability, rejection of unscored/invalid input, and the distinction
between available retrieval evidence and omitted output facts. Removing a required
witness reduces coverage; omitting a prose fact does not change supplied evidence.
Git whitespace checks pass. No live API calls were made during review and metric computation.
