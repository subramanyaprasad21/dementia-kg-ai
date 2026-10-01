# M7 protocol: a small, question-held-out portfolio evaluation of evidence handling

> **Historical protocol:** the twelve-question evaluation was amended on 2026-09-28 to the [Development-overlapping portfolio challenge set](m7_portfolio_challenge.md). The held-out eligibility/designation and six-stratum allocation below remain historical; do not apply them to claim unseen generalization for the challenge set. The original scoring formulas and failure boundaries remain in force as specified by the amendment.

**Protocol and budget were approved; formal execution remained gated. No formal questions, gold answers or model calls were created during this protocol milestone.** Baseline: `6f4fcbdbdaea44453571fb8ea8fb72307fec5e27`. This proposal implements the evaluation principles in `docs/evaluation_protocol.md`; it does not retrospectively change them or relabel development outputs.

The machine-readable companion is `assessments/m7_protocol_proposal.json`. The engineering checks in `tools/m7_protocol_checks.py` validate arithmetic, eligibility declarations and metric aggregation using synthetic controls. They neither certify question novelty nor replace reviewers. There is no M7 live runner at this stage; any later runner must implement this frozen protocol rather than make new scoring decisions.

## The limited question this study can answer

On a fixed, already exposed dementia evidence corpus, what happens to **the source support of retained structured assertions**, supported-answer completion and abstention when the existing local verifier is applied to the same KG-grounded output?

The primary contrast is grounded versus grounded plus verification. Model-only is a secondary information-access baseline. The study cannot demonstrate superiority in dementia diagnosis, clinical validity, independent biomedical truth or retrieval generalization. It also cannot establish a graph-versus-vector advantage: this experiment supplies the same curated finite RDF context to both grounded conditions.

The existing verifier checks literal RDF statements and citation membership, not generated explanation prose. Both grounded conditions therefore retain the same prose, labelled unverified. Its source-relative correctness scores must be identical when that prose is identical; the protocol does not predict or claim a prose-correctness improvement. The evaluated intervention is the separate retained-assertion/provenance surface. This limitation must appear in any result summary, including a negative result.

## Construct twelve questions without disguising development reuse

**Recorded holdout definition:** previously unseen, human-authored question instances on the existing exposed corpus. This is not an evidence/source-disjoint holdout, a hidden corpus, or proof that the provider's pretraining excluded the material. This restricted interpretation defines the study scope. A stricter evidence-disjoint study cannot be promised from the current development slice without a separate corpus/design decision.

After protocol finalization and a code/configuration freeze, the designated curator and sole human reviewer, Subramanya Prasad (`subramanya-prasad`), writes exactly twelve self-contained questions, one source-answerable and one evidence-insufficient case in each of six strata:

1. Evidence and provenance tracing.
2. Original versus normalized disease scope.
3. Hierarchy navigation versus selection context.
4. Contextual mapping distinctions.
5. Mechanism versus indication.
6. Missing information and permissible qualification.

These strata are sampling categories, not six independent biological samples. The questions must remain inside the existing AD/FTD scope and frozen graph. No additional sources or biological facts are generated. Unsupported cases ask for an interpretation not warranted by the supplied evidence; they must still permit at least one useful source-relative fact plus a clearly bounded abstention. Thus blanket refusal cannot attain supported-answer completion.

For each candidate, the curator supplies privately: ID, question text, category, stratum, exact existing RDF packet roots (at most eight), required source-fact IDs with verbatim supporting assertion sets, required qualifications, required abstention if applicable, explicit prohibited broadening, source/provenance requirements, and dependency-group memberships. Gold answers must be grounded in inspected records and distinguish absence of support from a false biological proposition. No LLM-generated gold labels are permitted.

The sole human curator/reviewer checks each candidate **before seeing any model output** against all exposed development questions, historical alternatives and prior prompts/results. Exclude exact matches, paraphrases, simple entity swaps that preserve an already rehearsed answer, or disguised versions of Q01–Q07. A new wording alone does not establish eligibility. The curator records eligibility rationale and checks the gold support/qualification rubric before generation. This is not independent validation. The curator may not tune retrieval or prompts based on model answers.

**Feasibility stop:** if twelve genuinely eligible items with these strata cannot be constructed from the small corpus, stop before calls and seek a design amendment. Do not fill the set with near-paraphrases, change its size after observing outputs, acquire new data, or call a diagnostic challenge set held-out. The existence of twelve eligible items is not claimed by this proposal.

Shared underlying reports, source records, evidence derivations and question templates must be recorded. Questions sharing any of them belong to the same dependency component (including transitive links). All components may contain previously exposed evidence; disclose that rather than claiming group-disjoint development/test splitting. No random train/test split is manufactured from these twelve items.

## Access and freeze sequence

1. Finalize the protocol, limited holdout definition, sole-reviewer arrangement and exact budget.
2. Freeze code commit, ontology/corpus manifest, prompts/schema, selection algorithm, decoding settings, scoring rules and retry policy before any test-question exposure to the generation or implementation path.
3. The human curator constructs and reviews the private test/gold set. Keep it outside Git and routine development context. Use relative artifact identifiers, not personal machine paths. Record each access with role, UTC time, purpose and file hash; never credentials.
4. Run deterministic eligibility and retrieval dry runs only. Exact duplicate checking is automatic; semantic novelty and evidence relevance are human judgments. At most eight roots / 192 KiB per item; every intended packet must fit. Fixing an invalid item is permitted **before any model output**, followed by curator review and rehashing. No model-assisted trial questions.
5. Freeze question, gold, retrieval packet and access-log hashes. The generation process receives questions and packets, **not gold answers, rubric labels or expected conclusions**. Human rubric files remain segregated from requests.
6. Execute once without tuning. Accidental early exposure triggers a logged contamination decision: exclude/replace before execution with renewed review, or abandon the held-out label. Never silently erase exposure. After results exist, no replacement questions or cherry-picked exclusions.

A human attestation in JSON is only a record of a declaration, not proof that an independent review occurred. The confirmed sole reviewer and actual review records are execution gates; independent review is a future validation gap. After evaluation, any release of questions, gold, annotations and outputs should preserve the embargo/access logs as provenance.

## Exact conditions and configuration

| Condition | Inputs and output surface |
|---|---|
| Model-only | Exact test question; existing model-only instructions and strict schema; no KG packets or hidden gold. Free prose remains unverified. |
| KG-grounded | Same question, existing grounded instructions, fixed question-scoped RDF packets and their provenance/limitations. Original generated prose and all candidate claims are retained as unverified. |
| Grounded + local verification | **The identical grounded generation**, passed through the existing deterministic verifier. Same prose remains unverified; accepted/rejected assertions and provenance are shown separately. No second generation, repair prompt or richer context. |

Use `gpt-6-sol`, low reasoning, strict current JSON schema, `max_output_tokens=4096`, no tools, `store=false`, existing prompt version `m5-evidence-answer-1`, standard/default service tier, existing 120-second timeout, no automatic retries. No seed or temperature setting is invented. Record requested/returned model IDs and complete response usage. The configured alias is not a pinned immutable model snapshot; materially different returned configuration stops the run for review.

Retrieval uses the existing hybrid implementation, explicit curator-declared roots, unchanged packet construction and an 8-packet/192-KiB limit. Scope selection is a controlled input, not a test of automatic entity grounding. The two grounded conditions share exact request/evidence hashes. One model-only and one grounded generation per item gives **24 generations and 36 logical condition outcomes**. These are not 36 independent model samples. Execute sequentially in frozen ID order, model-only then grounded; use no adaptive ordering.

## Human scoring procedure

**Sole human curator and reviewer: Subramanya Prasad (`subramanya-prasad`).** The original two-reviewer protocol was explicitly amended before any formal generation. Independent second-reviewer validation is a future validation gap, not an execution prerequisite. Do not calculate or claim inter-rater agreement. Do not describe the evaluation as expert-reviewed, clinically validated or independently validated.

Review the 24 unique generated prose outputs, not duplicate prose as if independent. Assign condition-masked labels and a fixed shuffled presentation order. Blinding is partial: citations and content may reveal information access, and the reviewer is also the curator. The reviewer inspects frozen reference evidence; gold is never shown to the model. Record atomic factual prose propositions with original character offsets, source-relative labels and rationales. Preserve all raw model outputs, deterministic verification artifacts, segmentation and scoring records for later independent reassessment. Ambiguous judgments remain `unresolved`. Automated RDF support checks remain separate from human prose scoring; neither substitutes for the other.

Use four mutually exclusive **source-relative** proposition labels:

- `supported`: the frozen evidence supports this exact proposition and scope.
- `unsupported`: support is absent from the allowed evidence; this is not proof of biomedical falsehood.
- `contradicted`: an explicit frozen source assertion contradicts the proposition in the same scope.
- `unresolved`: ambiguity in the evidence or interpretation prevents a justified assignment.

Apply these independently to structured candidate assertions and all factual prose, including claim explanations, answer text and factual statements in unanswered fields. Nonfactual disclaimers are not factual propositions. Do not count the same copied proposition twice merely because it is displayed in two surfaces; retain surface membership for separate scoring. Corresponding statements retain the same recorded human label when the verifier filters them. Clinical truth is **not scored**.

Additional dimensions are separate:

| Dimension | Fixed rule |
|---|---|
| Source-relative factual support | Four labels above; no substitution of exact string match for human interpretation of prose. |
| Question relevance/usefulness | For each retained assertion, relevant/not relevant to the fixed question; report separately from factual support. Supported-answer completion counts required facts actually conveyed with correct scope. No global subjective usefulness score. |
| Qualification | Pass only if all item-specific mandatory scope/uncertainty qualifications are present without a conflicting unsupported upgrade. |
| Required abstention | For six insufficient items, pass only if the forbidden inference is withheld explicitly, the reason is correctly scoped, and no later prose makes that inference. A generic refusal is not automatically a pass. |
| Excessive abstention | For six answerable items, mark if the response unnecessarily withholds the requested source-supported answer. Failures are reported separately. |
| Provenance | Each retained assertion passes only when its cited supplied packet supports it and the required source/edition/record locators are correctly attached. Merely containing a URL fails. |
| Retrieval coverage | Fraction of predeclared required source-support slots whose entire assertion set is present in the frozen retrieved packet union. Does not measure completeness of upstream evidence or medicine. |

Gold required facts have stable IDs. The reviewer matches correctly expressed source facts to those IDs once each. Every item includes at least one source-supported fact, even when its requested stronger conclusion requires abstention. This avoids rewarding empty answers. Mandatory source gaps remain part of the gold qualification/abstention criteria, not opportunities to invent missing values.

## Exact metrics and aggregation

Let N=12, C_i be the retained structured assertions for item i, S_i the source-supported ones, F_i the predeclared required facts, and A_i the required facts correctly expressed in the complete output.

- **Primary descriptive contrast:** per-item retained-assertion precision |S_i|/|C_i|. Grounded uses every candidate assertion; verified uses the accepted subset. Report each condition's macro mean over items with nonempty C_i, the defined-item count, assertion counts, and verification-minus-grounded mean paired difference only on items where both precisions are defined. Undefined is `null`, not 0 or 1. No significance claim follows from this conditional contrast.
- **Mandatory completion companion:** mean |A_i|/|F_i| over **all 12 items**. Failures and blank outputs contribute zero. Prose and accepted statements are not double-counted. Shared grounded/verified prose is evaluated once and propagated consistently.
- **Zero-retained rate:** items with zero retained assertions or a failed output /12. An always-reject system has undefined precision, zero assertion retention and cannot demonstrate success by precision alone.
- **Unsupported prose:** per-item (unsupported + contradicted propositions)/all factual prose propositions, macro-averaged over items with any factual prose. Report the denominator and separate unresolved-proposition proportion. Do not silently count a no-prose failure as safe prose.
- **Qualification pass:** passing complete outputs /12; failure or unscored output contributes zero.
- **Required abstention pass:** passing insufficient items /6; API failures/refusals are not successful abstentions.
- **Excessive abstention:** answerable items unnecessarily withheld /6; separately show failures so a failed system cannot look useful.
- **Relevance and provenance:** each is a separate per-item fraction of retained assertions, macro-averaged over nonempty sets with their denominator reported. Do not convert either into source support or clinical validity.
- **Retrieval coverage:** per-item exact support-slot fraction above, plus macro mean /12; report intended versus retrieved roots/bytes and all shortages. This is identical for both grounded conditions.
- **Engineering outcomes:** completed, timeout, API error, refusal, invalid output, retrieval failure, verification failure counts; calls, input/output tokens, cost estimates and reserved unknown charges. Report logical-condition failures and distinct API failures separately: one failed grounded generation affects both grounded conditions, not two failed API calls.

Provide all question-level results and dependency-group membership. No p-values, confidence intervals, bootstrap significance, population effect estimate or “statistically superior” claim is justified by twelve purposively sampled dependent cases. Report descriptive paired differences, including zero/negative results, and counts by strata/dependency component without treating them as independent replicates. No post hoc choice of a more favorable primary metric.

## Failures, missing evidence, timeouts and development disposition

**Formal M7: zero retries.** Token-count failure, API error, refusal, timeout and invalid/incomplete schema output remain outcomes. Never manually repair JSON or use model-only text to fill a grounded failure. A grounded failure yields no verified answer. Local verification failure preserves the original grounded output and produces a failed verified surface. Do not treat technical failures as biological absence or correct abstention. Reserve cost before transmission; when usage is unknown, retain the full reservation. Continue to the next frozen item after an isolated item failure only while caps remain safe. Stop the whole batch for authentication/quota rejection, changed model/pricing, integrity mismatch, exhausted budget or a systematic implementation defect; preserve all completed and unrun items, with no new questions or tuning.

**Q07 development timeout:** propose at most one additional byte-identical grounded retry, with the unchanged 120-second timeout and max output 4096. The historical timeout, payload and reservation remain. Perform the retry before test-question access; do not reuse its result in M7. If it times out again, retain it and close this development diagnostic as incomplete; no retry loop or timeout increase. A test may proceed with this known limitation under the frozen formal failure policy. No retry is executed now.

**Q04 development limitation:** retain the unavailable historical counts and the original ambiguous reference to “Q03.” No counts, source edition or answers are repaired. No Q04 rerun is proposed. Held-out questions must be self-contained; if one requires absent historical count data, classify it as insufficient and specify the required qualified abstention. Do not substitute local subset counts, current-release counts or source prose outside the allowed interface. Fixing eligibility is not permission to change accepted source facts.

This records a disposition without pretending the two development issues have disappeared.

## Budget and execution gates

Use the recorded rate assumptions ($2/M input, $10/M output, no cache discount). Prices were not freshly verified during this protocol milestone. Verify them before execution; a changed rate or model requires review rather than silent substitution.

| Component | Generations | HTTP requests including counting | Input-token ceiling | Output-token ceiling | Maximum token cost |
|---|---:|---:|---:|---:|---:|
| M7 formal | 24 | 48 | 2,400,000 | 98,304 | $5.783040 |
| Optional Q07 development retry | 1 | 2 | 9,788 | 4,096 | $0.060536 |
| Combined ceiling | **25** | **50** | **2,409,788** | **102,400** | **$5.843576** |

Each formal call must pass live input counting at <=100,000 tokens before generation; no silent prompt trimming. The Q07 retry must fit its exact previously counted bound; otherwise stop before generation. No trustworthy empirical token estimate exists until humans select the test inputs. These are conservative ceilings, not predicted spending. Counting failures consume their HTTP attempt; no free reset.

The recorded budget allows **$6 maximum additional spend**, with an exact token reservation ceiling of $5.843576. Prior cumulative reservation is $1.544974, so conservative cumulative reservation is **$7.388550**, within the recorded cumulative cap of **$7.50**. Earlier development ledgers retain their historical limits; the new budget record must be linked without resetting them. If Q07 retry is unused, subtract its one generation/two requests and $0.060536; formal M7 remains separate from development accounting.

Link the formal ledger to the immutable development ledgers. Reserve all failures; do not reset prior budget records. Keep formal requests/results in a new versioned run, never overwrite development runs.

## Deliverables and execution sequence

This offline milestone contains the protocol, machine-readable limits, small eligibility/metric checks and synthetic regression tests. It contains no actual test set or results. Required human work and review access cannot be completed by asserting flags in code.

Execution sequence: implement only the frozen run/report harness, complete human construction/review and retrieval dry run, freeze hashes, execute under the stated limits, review outputs, compute these metrics, and persist actual results. If eligibility, sole-reviewer records or input readiness cannot be established, stop without spending.

Only after M7 reporting is finalized should M8 produce the concise README, 2–4-page-equivalent technical summary, reproducible commands, result/source links and demonstrated-only CV/GitHub wording. M8 must audit secrets, source redistribution rights, personal absolute paths and stale claims before external release. Historical provenance and Git history must remain intact; existing historical absolute-path references need a deliberate release treatment, not history rewriting or undisclosed deletion. README/CV result rewriting, an agent layer and external release are outside this protocol milestone.

## Historical offline verification at the original proposal commit

Synthetic tests check exact budget arithmetic, blocked readiness, duplicate/exposed question declarations, missing provenance/review fields, allocation, failure denominators, always-refuse behavior, undefined precision, paired comparisons and separate retrieval coverage. They are not human reviews, held-out examples or biomedical labels.

Full offline suite: **297 tests passed in 353.044 seconds**, including all 288 prior tests and nine new protocol controls. `git diff --check` passes. No existing research or development artifact changed. At this historical point, protocol sign-off, reviewer assignment and the actual eligible held-out set remained outstanding.


## Protocol sign-off and execution-gate status — 2026-09-27

The protocol was signed off at commit `7aae470051a631f713122391e14101e694ac7a74`, including the restricted question-only holdout definition and budget. Earlier proposal wording above records the original design; this sign-off supersedes its pending-status language. The subsequent sole-reviewer amendment below changes only the review arrangement.

Approved ceilings: 24 formal generations plus at most one unchanged Q07 development retry; 2,409,788 combined input tokens and 102,400 output tokens; USD 6.00 additional cost and USD 7.50 cumulative reservation. The existing conservative arithmetic remains USD 5.843576 additional token reservation and USD 7.388550 cumulative reservation. No earlier ledger, reservation or failed attempt is reset.

The following pre-generation gates apply, with the reviewer gate amended by the subsequent sole-reviewer decision. Once they pass, the recorded budget permits execution without another protocol change.

| Gate | Current verified state |
|---|---|
| Construct twelve eligible questions | Not complete: no actual human-authored holdout has been supplied. The synthetic unit-test controls are not candidates. |
| Exclude Q01–Q07 paraphrases and development variants | Not complete: requires actual candidates and recorded human novelty review. Automatic exact-duplicate checks alone are insufficient. |
| Freeze text, reference facts, retrieval scopes and scoring | Scoring protocol fixed; actual question/gold/packet artifacts do not yet exist and cannot be frozen. |
| Confirm reviewer arrangement | Complete under the explicit sole-reviewer amendment: Subramanya Prasad is curator and sole human reviewer. Independent review remains a disclosed future gap. |
| Offline contamination/access/protocol checks | Eleven synthetic protocol tests pass, including sole-reviewer and retained-gate controls. Actual access, eligibility, gold and retrieval checks remain pending the human-authored package. |
| Freeze evaluation package locally | Not complete: protocol sign-off does not constitute freezing a nonexistent dataset. |

Formal execution is blocked by these outstanding gates. No claim is made that twelve eligible questions are impossible; their eligibility has not yet been established. No AI-authored questions, fabricated reviewer attestations or development variants have been substituted.

The optional byte-identical Q07 retry remains permitted but unused. Its historical timeout and accounting remain unchanged. It is not a substitute for M7 eligibility or human review and supplies no held-out result.

Next required human input is Subramanya Prasad's reviewed private question/gold package following the construction and access sequence above. His reviewer role is recorded; actual question authorship, eligibility and gold review have not yet occurred in the repository record. Do not paste private gold into routine implementation context before the prescribed code/configuration freeze. No new API call, source acquisition or M8 work was performed while recording this protocol state. The amended full offline suite passed all 299 tests in 387.840 seconds, including all 297 previous tests and two new sole-reviewer/gate controls. The blank template was separately checked for exact 6/6 allocation, empty question/gold fields and expected eligibility rejection. Documentation links and `git diff --check` pass.


### Amendment provenance and retained limits

The original two-reviewer protocol remains inspectable in commit `7aae470051a631f713122391e14101e694ac7a74`. A subsequent explicit amendment replaces that arrangement with one named curator/reviewer for the present portfolio evaluation. Machine-readable profile: `m7-protocol-sole-reviewer-2`. The reviewer amendment changes no question-count, eligibility, gold-freeze, budget, prompt, model, failure, retrieval or metric definition. No inter-rater calculation is implemented. Future independent reassessment must be reported separately and must not retrospectively relabel the current results as independently validated.


### Human-authoring gate explicitly remains open

At this point the twelve questions had not yet been written, and automated generation or inference of gold answers was explicitly excluded. The next artifact was limited to [the blank authoring framework](m7_authoring_guide.md) and `templates/m7_questions.blank.json`. The curator would complete question text, reference facts and rubric privately. The template contains twelve balanced empty slots, null authorship/exposure declarations and no eligibility attestations; it fails eligibility validation as intended. It is not a frozen evaluation package. No M7 freeze or API call may occur until the completed human-authored set is returned and the remaining checks pass.
