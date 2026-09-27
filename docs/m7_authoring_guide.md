# M7 private human-authoring guide

**Blank framework only. No questions or gold answers have been authored, approved or frozen. No model calls are authorized by completing a template field alone.**

Subramanya Prasad is the approved human curator and sole human reviewer. Independent review is a future validation gap. This portfolio evaluation is not expert-reviewed, clinically validated or independently validated; no inter-rater agreement will be calculated. The governing protocol is [m7_protocol_proposal.md](m7_protocol_proposal.md), profile `m7-protocol-sole-reviewer-2`.

## Start privately

Copy [the blank template](../templates/m7_questions.blank.json) outside the repository and routine implementation context. Keep the committed blank unchanged. Do not paste completed gold answers into the implementation conversation. Record accesses in your private `accessLog`: role/reviewer ID, UTC time, purpose, relative artifact identifier and SHA-256 of the accessed version. Do not record credentials. Give the completed private file's path when ready; completing it does not automatically authorize a freeze or API request.

The template allocates twelve slots, one of each category in every stratum. Slot allocation is administrative, not question authorship:

| Slots | Stratum | Categories |
|---|---|---|
| M7-01 / M7-02 | Evidence and provenance | answerable / insufficient |
| M7-03 / M7-04 | Original versus normalized source scope | answerable / insufficient |
| M7-05 / M7-06 | Hierarchy versus selection | answerable / insufficient |
| M7-07 / M7-08 | Contextual mapping | answerable / insufficient |
| M7-09 / M7-10 | Mechanism versus indication | answerable / insufficient |
| M7-11 / M7-12 | Missing information and qualification | answerable / insufficient |

`insufficient` denotes a qualification/abstention case. It must still permit at least one useful source-supported fact. Six blanket refusals are not a valid set. An answerable item must be answerable from the actual frozen packet scope with its mandatory qualifications, not from assumed biomedical knowledge.

## Eligibility checklist

Write the questions yourself, using the unchanged AD/FTD development corpus. Every question must be self-contained, genuinely new, and supported by an explicit bounded scope. Use no new sources, AI-authored trial questions or LLM-generated gold labels. Keep the source edition and record distinctions intact.

Reject a candidate if it is:

- A Q01–Q07 paraphrase, a historical design alternative, or a development variant.
- A simple entity substitution preserving a rehearsed answer or question structure.
- Dependent on an undefined reference to another question.
- Answerable only by missing records, except where the question explicitly tests the bounded qualification/abstention requirement.
- Based on assumed clinical efficacy, source completeness, mapping equivalence or independent evidence unsupported by the supplied records.
- So broad that the approved eight-root / 192-KiB scope cannot contain the intended support.

A different wording does not establish novelty. If twelve eligible questions cannot be constructed across the required strata, stop and report the shortage. Do not change allocation or relabel old questions to fill it.

## Contamination review

Privately compare each candidate with:

1. All Q01–Q07 text, required slots and historical alternatives in [competency_questions.md](competency_questions.md).
2. The committed [corrected retrieval plan](../assessments/m5-corrected-retrieval-plan.json).
3. Original requests, prepared contexts and outputs in `experiments/m5-development-pilot-001/` and `experiments/m5-corrected-followup-001/`.
4. Any other project examples or prompts you consulted; record their paths and versions.

In `contaminationReview`, list all seven question IDs, the inspected artifact references, your novelty rationale, the entity-swap/rehearsed-answer assessment and any prior exposure. Record related source records, reports and templates in `dependencyGroups`. Shared groups are not independent samples; include transitive dependencies. This remains a question-only holdout on an exposed corpus, not an evidence-disjoint or pretraining-free study.

The existing offline validator can reject exact normalized-text duplicates and declared development exposure. It cannot establish semantic novelty or certify your review. Never set the review flags merely to make a validator pass.

## Complete each slot

- `question`: your exact final question text, at most 4,096 UTF-8 bytes.
- `origin`, `authoredBy`, `authoredAtUTC`: record actual human authorship (`human-authored`), your reviewer ID and authorship time only after writing the item.
- `rootIds`: exact existing RDF packet-root IRIs, at most eight, with no duplicates. The later dry run must recover all intended packets within 196,608 bytes; it must not silently truncate.
- `requiredFactIds`: unique local IDs for the facts needed for completion. Every item needs at least one.
- `referenceFacts`: one record per required fact ID containing `factId`, your `referenceText`, `supportAssertions` (verbatim N-Triples), `rootIds`, and `sourceReferences` (edition, source record and provenance locators). Inspect actual assertions; do not infer missing support. These are gold fields and must not enter generation requests.
- `requiredQualifications`: explicit source-scope, uncertainty and interpretation conditions needed for a valid answer.
- `requiredAbstention`: the precise unsupported extension that must be withheld for an insufficient item; null for an answerable item.
- `prohibitedClaims`: item-specific unsupported upgrades, written before generation.
- `provenanceRequirements`: which source/edition/record references must accompany the answer.
- `scoringRubric`: define concrete pass criteria for each required fact, qualification, relevance and provenance; use abstention criteria for insufficient items and excessive-abstention criteria for answerable items. Do not change the protocol's metric definitions or denominators.
- `eligibilityReviews`: after your actual review, supply exactly one record with `reviewerId` = `subramanya-prasad`, `decision` = `eligible`, and your substantive `rationale`. An ineligible candidate must not be declared eligible.
- `developmentExposed`, `nearParaphraseOfDevelopment`, `selfContained`, `goldReviewed`: record your actual determinations; null/false defaults deliberately prevent acceptance. `syntheticControl` remains false only for your real authored items.

The template's empty values are placeholders, not evidence that information is missing upstream. Its top-level content flags describe authoring status only. Do not confuse these with ontology missingness records or manufacture new graph records.

## Scoring and later reassessment

Freeze your reference facts and rubric before generation. Afterwards, personally label factual prose and structured assertions as supported, unsupported, contradicted or unresolved relative to the frozen source scope. Preserve original text offsets and reasons. Automated RDF verification does not assign human prose labels. The same grounded prose receives the same human score in grounded and verified conditions; verification filters a separate assertion surface.

Preserve every raw response, failure, request, token/cost record and deterministic verification artifact. Do not repair outputs, replace questions after seeing responses, or claim that sole-reviewer judgments are independent validation. Future independent scoring must remain a separately documented reassessment.

## Return and remaining freeze checks

Return the local path and confirmation that you personally completed authorship, contamination review, reference facts and rubric. Do not send the private contents into routine chat. The authoring gate remains open until then. Before generation, the implementation must still verify the completed package, record controlled access, freeze code/configuration and dataset hashes, dry-run every retrieval scope, verify pricing/configuration and commit the approved frozen evaluation package. A path submission alone does not satisfy these checks. No M7 freeze or model/API run is performed as part of this authoring framework.
