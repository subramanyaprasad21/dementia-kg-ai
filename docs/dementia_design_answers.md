# Executable design-question evidence interface

Implemented from `5b8b98314e9b592e1653638358a1210645c3f072` to prioritize usable research outputs. No new acquisition, identity profile, ontology term, or source interpretation is introduced.

## Run

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=tools:/private/tmp/ot2606-duckdb-inspection:/private/tmp/dementiagraph-m1-task008-pyshacl python3 tools/dementia_design_answers.py Q06
```

Use Q01–Q07 or `all`. Existing external dependencies are reused. Raw source directories must remain available: missing or altered files fail verification, rather than producing an apparently successful answer.

The command verifies the captured context and accepted evidence RDF, executes bounded question-specific lookups/joins, and returns structured supported facts, supporting source locators, unanswered requirements and limitations. `assessments/dementia-design-answers.json` is the reproducible current output. It is an exposed design/acceptance result, not a benchmark score or generated biomedical answer.

Evidence-occurrence answers are obtained from RDF assertions through the existing `validate_ot2606.answers` function. Context facts come from the verified source intermediate because mechanism/indication RDF identity coverage remains unactivated. Selection counts come from the existing verified local file computation. This hybrid evidence interface is explicitly **not** represented as an RDF-only retrieval baseline, completed M4, or complete KG integration.

## Actual outputs

| Question | Output | Remaining limitation |
|---|---|---|
| Q01 | Three source-specific PSEN1 evidence descriptions, original/normalized fields and citations | Primary PanelApp context and independent article interpretation absent |
| Q02 | Shared nct00594737 report and bounded GRIN1/GRIN3B mechanism participation | Source composition and primary registry population/status absent |
| Q03 | Original Pick/OMIM versus source-normalized FTD description | Panel version and biomedical mapping validity unresolved |
| Q04 | Four local selection results: APP direct/inclusive 0/1; MAPT 3/10, with membership and input hashes | Bounded file computation only, not historical API replay or end-to-end new-context RDF acceptance |
| Q05 | Two source-scoped, divergent OMIM mappings retained | Panel context and mapping adjudication unresolved |
| Q06 | Separate mechanisms and indications for zagotenemab/lecanemab; scoped list absence result | FTD/MAPT aggregate and independently reviewed publication interpretation absent |
| Q07 | Gosuranemab mechanism and exact FTD indication/report linkage | Primary registry population, eligibility, dated status and efficacy cannot be supplied |

Six answers are PARTIAL; Q04 is SUPPORTED-BOUNDED-COMPUTATION. Missing evidence produces UNANSWERED when no supported facts remain. Partial answers do not satisfy the complete original question rubric. The questions and their requirements are unchanged.

For the Q06 absence result, the implementation requires the whole captured zagotenemab list to equal the independently retained complete-list extraction. Removing a row prevents the absence claim. This integrity guard uses the extraction as a completeness certificate; the returned disease values still come from actual source rows. It does not infer absence beyond this release/list.

## Verification

Five focused tests establish useful positive outputs and actual evidence sensitivity: removal of the Q03 source occurrence yields UNANSWERED; changed shared-report evidence removes the shared locator; partial indication lists cannot support absence; wrong source edition is rejected; missing selections do not yield a supported Q04 result. No test relies only on a fixed rejection label.

No paid model calls, M3 characterisation, M4 comparison, or M5 implementation is claimed. The next substantive boundary is additional acquisition and the already specified context identity extension, not another planning milestone. Once the required acquisition and context identity extension are available, this interface provides a direct acceptance target for the corresponding source/RDF integration.

Verification completed: **221 tests passed in 281.853 seconds** (216 existing plus five interface tests). A second CLI execution reproduced the saved answer artifact byte-for-byte. Existing tracked source, ontology, fixture and identity files remained unchanged.

## Continued source integration

The initial result table above records the first interface milestone. The current saved answers additionally include the recovered historical scalar aggregate and four explicitly project-derived technical inspection summaries, with verified source hashes and passage locators. See `continued_m2_results.md` for acquisition accounting, changed support and remaining limitations. The CLI uses those verified captures; this is still a qualified design interface, not a retrieval experiment or completed M4.
