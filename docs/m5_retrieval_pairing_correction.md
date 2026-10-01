# M5 question-to-retrieval correction — offline revision 2

Baseline: `518f469f783e0c1c98deab2c80f0a49aeba00b93`. No API, token-count or acquisition requests were made. No model, prompt, answer criteria, question wording, graph fact or historical result was changed. This is a proposed follow-up retrieval baseline, not a new model experiment.

## Root cause and correction to the earlier diagnosis

The historical `m5_pilot_plan.build()` zipped core question text with the seven M4 **engineering controls**. Those controls exercised narrow record retrieval, not full competency-question inputs. In addition, hybrid reciprocal-rank fusion unions lexical hits with anchor hits; an anchor is not a hard eligibility filter. Type-only restrictions therefore admitted off-topic records.

The earlier results report's suggestion that Q03's OMIM:172700 anchor was mismatched was incorrect: the Q03 specification explicitly requires that identifier and Pick wording. Its defect was extra unrelated mappings, not the anchor. Q02's NCT00594737 study records were also relevant; they were inadequate alone, not an unrelated trial. The historical report remains unchanged; this dated correction supersedes those interpretations.

## Every original pairing and exact correction

IDs below abbreviate only for readability. Full source IDs are constants in `tools/m5_corrected_retrieval.py`; full RDF roots, packet hashes, exact questions and request hashes are in `assessments/m5-corrected-retrieval-plan.json`.

| Question | Original actual retrieval defect | Corrected finite scope | Packets / bytes |
|---|---|---|---:|
| Q01 PSEN1 AD/FTD | Correct PSEN1 anchor returned the three required evidence records **plus both unrelated GRIN clinical-precedence rows**. Evidence-only outward packets omitted incoming disease mapping and missingness records. | Mapping packets for `1261ad02…`, `986bb22b…`, `98c49197…`, plus the two Europe PMC source-omission MissingnessRecords. Mapping packets already contain the associated evidence, target and publication-reference assertions; no redundant EvidenceOccurrence roots are added. | 5 / 81,004 |
| Q02 GRIN1/GRIN3B independence | Only two StudyRecords for NCT00594737; lacked the question's target/evidence/mapping and mechanism comparison. | The two mapping packets for `ed0b04f2…` and `0d60abae…`, the two CHEMBL807 gene-indexed MechanismRecords, and the existing explicitly project-derived shared-report comparison. Its provenance supplies both occurrences and shared study identifier. | 5 / 101,299 |
| Q03 Pick → FTD/MAPT | OMIM:172700 anchor **was correct**, but the hybrid result also included both PSEN1 Europe PMC mappings. | Only the mapping packet contextualized by `04e8f548…`: original Pick/OMIM:172700, reported MONDO_0017276, MAPT evidence and source-local provenance. | 1 / 21,332 |
| Q04 normalization versus descendant inclusion | Two local fixed-ID SelectionContexts were presented for a question about historical direct/inclusive diagnostics; no complete hierarchy paths or narrower mapped records. | Mapping packets for APP `8bac3794…`, MAPT `019b39b2…`, and Pick contrast `04e8f548…`, plus all five accepted directed hierarchy steps. Local fixed-ID selections are not substituted for historical query operations. | 8 / 130,084 |
| Q05 divergent OMIM:600274 assignments | Both intended mappings were present, plus an unrelated PSEN1 Europe PMC mapping; no explicit hierarchy context. | Exactly the two contextual mappings `98c49197…` and `019b39b2…`, plus semantic-dementia → frontotemporal-lobar-degeneration → FTD source steps. No equivalence, merge or repair. | 4 / 65,842 |
| Q06 mechanism versus indication | Mechanism-only retrieval mixed zagotenemab with CHEMBL807 and gosuranemab; no indication comparison or explicit FTD/MAPT association context. AD-control mechanism alone was insufficient. | Existing bounded MAPT association **project grouping**; zagotenemab CHEMBL4298021 mechanism and its two retained indications; AD-control CHEMBL3833321 mechanism and indication. | 6 / 92,688 |
| Q07 gosuranemab population | Planned but unrun: correct gosuranemab indication mixed with three other-drug indications; lacked its mechanism. | CHEMBL3990042 mechanism and exact indication `c680c47a8cc2571635e1d5c629e51834273a3e67d25ebedfa9e58b729ad65189`. No invented registry population or mechanism-study findings. | 2 / 23,417 |

Q04's exact existing steps remain:

- MONDO:0007088 → MONDO:0015140 → MONDO:0100087 → MONDO:0004975.
- MONDO:0010857 → MONDO:0017160 → MONDO:0017276.

The source-scoped disease references remain distinct. Lexical lookup selects existing references; it creates no identity or equivalence assertion.

## Minimal implementation

- `tools/development_retrieval.py`: optional `allowed_roots` query filter, applied identically before vector/graph/hybrid ranking. Empty, duplicate or unknown explicit root scopes fail. Legacy calls omit it and return their original data structure and results unchanged.
- `tools/m5_evidence_answers.py`: exposes the retrieval scope and packet budget to preparation; deterministic validation replays the same scope. Model request schema, instructions, output cap and verification criteria are unchanged.
- `tools/m5_corrected_retrieval.py`: resolves question IDs explicitly, independently of M4 list order. It reads exact source identifiers and actual graph relationships; missing/ambiguous intended records fail. This is the new preparation entry point. The historical M5 plan remains a historical replay tool.
- The new plan stores each exact scope, packet hash, question, request hash, known gap and proposed follow-up budget. It does not duplicate the graph or store a new normalized dataset.

The shared corrected retrieval budget is **8 packets / 192 KiB**, replacing 5 / 64 KiB for this revision only. Q04 requires eight existing records; several complete finite scopes exceed 64 KiB. All intended packets must fit or preparation fails, rather than silently dropping a mandatory participant. This context-budget change is explicit and part of the proposed follow-up configuration. It does not change the model's 100,000 input-token cap, 4,096 output-token cap, or the historical pilot budget/results. Individual record packet construction is unchanged.

## Comparable inputs and remaining answerability limits

**Yes for bounded development comparisons:** questions are byte-identical; model-only requests are unchanged; grounded and verified conditions receive the exact same corrected request and reuse one generated output. All intended packets are recovered deterministically under the shared budget. No unrelated packet roots enter the allowed set. Text/vector/graph methods share candidate restrictions, though a vector search with no lexical match may return fewer results. M5 uses hybrid selection and explicitly requires the entire finite scope.

**No claim of complete Q01–Q07 answerability:** the RDF graph is unchanged and retains its known limitations. Q04's historical 0→1/3→10 computations reside in non-RDF context and are not supplied as graph assertions. Q07's dated primary-registry population/status and source-description-only report links remain unavailable to this interface. Panel editions, article inspection, original mapping validity and full datasource/indication-list completeness are not established. Q06's existing association remains a project grouping. Missingness and source qualifiers are preserved; answer criteria are not relaxed.

This is explicit finite question scoping, not automatic entity grounding or evidence of better unrestricted retrieval ranking. All questions remain exposed design/development material. Reusing baseline outputs is not an independent new sample and will be labelled as reuse.

## Proposed follow-up — offline plan only

- **8 new generations**: corrected grounded Q01–Q07 (7), plus missing model-only Q07 (1).
- Reuse the six historical model-only Q01–Q06 outputs: exact request hashes are unchanged. Do not rerun them merely to obtain different answers.
- All seven grounded inputs change, so none of the old grounded outputs is treated as a result for this corrected baseline. Original outputs remain intact for comparison of development revisions.
- Verified outputs are local postprocessing of the same seven grounded generations; no extra model calls.
- Up to **16 additional HTTP requests** including token counting; proposed cumulative ceilings **22 generation attempts / 44 HTTP requests**, retaining both historical failures. Existing adapter ceilings remain unchanged in this revision.
- Serialized new requests: **567,588 bytes**. Rough input estimate **141,897–283,794 tokens** using 2–4 bytes/token. This is a heuristic, not an installed tokenizer measurement or an upper bound. Exact counting is deferred to any future live run.
- Output allowance: **32,768 tokens** maximum (8 × 4,096). No reliable point estimate of output demand is claimed for enlarged context.
- Hard new-input ceiling: **800,000 tokens** (8 × 100,000).
- Using the previously recorded $2/M input and $10/M output rates: estimated token cost with maximum outputs is approximately **$0.6115–$0.8953**; conservative hard token-cost ceiling **$1.92768**. Rates were not re-fetched because this task is offline only; pricing must be confirmed before expenditure.
- Adding the full prior $0.807722 reservation gives **$2.735402**, still under $5. Conservative cumulative tokens, reserving 224 input / 4,096 output for each historical failed attempt: **917,141 input / 48,529 output**, within the original 1.4M / 57,344 ceilings. No refund or deletion of earlier failures is proposed.

The proposed change is limited to this corrected context configuration and eight-call extension; it does not change the model, evidence or research questions. This document does not execute a full or held-out experiment.

## Verification and historical preservation

Regression checks independently assert Q01's three source IDs and target; Q02's two genes, common trial and drug mechanism context; Q03's original/destination distinction; Q04's exact directed steps and three mappings; Q05's distinct destinations; Q06's mechanism/indication/AD-control types; Q07's exact drug and missing population. Negative controls reject missing/ambiguous records, forged roots and insufficient context budget; unrelated lexical hits cannot escape the explicit scope. Retrieved triples must be a subset of the unchanged accepted graph.

The historical pilot replays byte-for-byte through the unchanged v1 plan and saved result verifier. Tests also check that questions, ontology, graph and original experiment files have no Git diff against the baseline. Network opening is blocked in plan/history replay tests.

Full offline suite: **285 tests passed in 338.961 seconds**, including all 274 previous tests and 11 new pairing regressions. `git diff --check` passes. Verification was offline: no API calls were made and source material was not altered.
