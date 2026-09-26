# M4 — bounded offline retrieval engineering

Status: **runnable local retrieval prototype**, not completion of every candidate M4 baseline or experimental evaluation. Uses the owner-approved qualified development corpus. M3 results are in `m3_graph_characterisation.md`.

## Runnable interface

```sh
export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH=tools:/private/tmp/dementiagraph-m1-task008-pyshacl
python3 tools/development_retrieval.py 'mechanism' --anchor CHEMBL3990042 --type MechanismRecord --mode graph
python3 tools/development_retrieval.py 'original normalized mapping' --anchor OMIM:172700 --type MappingRecord --mode vector
python3 tools/development_retrieval.py 'clinical indication' --anchor CHEMBL3990042 --type ClinicalIndicationRecord --mode hybrid
python3 tools/development_retrieval.py 'population' --anchor CHEMBL3990042 --type ClinicalIndicationRecord --require hasPopulationScope --mode hybrid
python3 tools/replay_development_retrieval.py
```

The last retrieval returns no support because the required population relationship is absent. It does not infer absence of a patient population or lack of efficacy in the real world. The separate `dementia_design_answers.py` interface still provides qualified design answers including source-intermediate computations; these are not secretly supplied to this RDF-only comparator.

## Accessible evidence and method contract

All methods access the same **48 record packets**, generated in memory from the five hash-pinned asserted RDF files. Roots are evidence, mappings, hierarchy steps, mechanisms, indications, study records, associations, selections, memberships, derived statements and missingness records. Every packet contains outgoing assertions on the root and nodes reached through at most two outgoing resource links, without traversing `rdf:type`. All statements retain exact RDF identifiers, datatypes, languages, direction and source qualifications. No new RDF is persisted.

Source/provenance entities' `sourceText` JSON blobs are excluded equally: their unprojected raw fields must not silently become accepted research assertions. Their locators and other represented provenance remain available. Non-RDF aggregates, local Q04 selection computations, publication inspection summaries and raw full text are excluded from both comparators. This restriction limits research claims; it does not erase the richer source bundle.

The packet ID is its existing root IRI. A content SHA-256 identifies a retrieval representation, not a new biomedical record identity. Text is a single lossless N-Triples representation of packet assertions. It is not a natural-language clinical narrative. All algorithms return that same packet; none receives a privileged answer template, identity-receipt oracle or manual biomedical conclusion.

| Mode | Implemented algorithm | Limits |
|---|---|---|
| `vector` | Local sparse TF-IDF: log term frequency, smoothed `log((1+N)/(1+df))+1` IDF, L2 cosine | Lexical vector baseline, **not neural semantic embeddings**. Lowercasing is only search-index processing; original source values remain intact. RDF URI/predicate tokens affect rankings. |
| `graph` | All explicit anchors must match a resource IRI or exact identifier/label field in the directed packet. Rank by sum of `1/(1+path length)`. Explicit type/predicate-only queries use a tied score. | Requires supplied structured anchors/filters; no free-text interpretation or automatic entity grounding. Matching strings selects references, never merges them or asserts equivalence. Paths and exact matched fields are returned. |
| `hybrid` | Reciprocal-rank fusion of full positive vector/graph rankings, constant 60, deterministic IRI tie break | Engineering default, not a tuned or empirically selected optimal configuration. Scores are not confidence. |

Approved class filters and required root-property filters apply equally across methods. Unknown classes/properties fail. This provides a minimal schema-constrained retrieval mode using declarations; it is not OWL entailment, automated clinical reasoning or proof that every returned assertion supports the question. Mechanism/indication type filters remain explicit. Reverse mapping lookup retrieves the MappingRecord with its original directed assertions; no reverse ontology property is introduced.

The default output ceiling is **five records / 65,536 encoded packet bytes**. Whole packets are retained or skipped, never truncated. Skipped IDs and used bytes are reported; ranking/path diagnostics are outside the evidence-packet byte count. These are byte/record engineering limits, not LLM token budgets. No claim of source-list completeness or negative biomedical fact follows from the retrieved subset. The same output limits, packet population, anchors and schema filters apply across methods; ranking differences can produce different subsets.

## Exposed development controls

`assessments/dementia-development-001.retrieval.json` records 24 executions (eight controls × three methods), including hashes of actual returned packets. These controls are related to Q01–Q07 but **do not constitute full question acceptance, relevance labels or held-out observations**.

| Control | Graph records returned | Meaning |
|---|---:|---|
| Q01 PSEN1 occurrences | 3 | Exact target-linked records; no causal interpretation |
| Q02 shared study reference | 2 | Two StudyRecords remain distinct, not two independent trials |
| Q03 original Pick identifier | 1 | Mapping context retained; no equivalence assertion |
| Q04 persisted selection contexts | 2 | Existing direct contexts only; not the external 0/1 and 3/10 calculation |
| Q05 shared original OMIM identifier | 2 | Both source-scoped mappings survive; ambiguity is not repaired |
| Q06 zagotenemab mechanism | 1 | No composed treatment/efficacy claim |
| Q07 gosuranemab indication | 1 | No registry population/status manufactured |
| Q07 required population | 0 | No retrievable support; qualified insufficiency |

Vector/hybrid rankings sometimes return more records with weaker lexical correspondence; these are retrieval candidates, not supported answer claims. Their relevance has not been independently adjudicated. No precision, recall, significance or graph-advantage result is claimed.

Nine tests cover asserted-only packets, identical evidence across methods, positive retrieval, link-removal sensitivity, unknown anchors, missing population, exact identifier spelling, whole-packet budgets, declared filters, lexical-vector controls and deterministic control replay. Positive cases prevent an always-reject implementation passing. Negative mutations exercise actual graph links rather than only a digest check. During implementation, duplicate text/triple-list serialization was removed; the revised packet budget now retains both ambiguous mapping records in the graph control.

## Approved roadmap and remaining gates

- **M4.1 LLM baseline:** pending model/version/access and cost authorization. No model call or result exists.
- **M4.2 vector RAG:** lexical-vector retrieval implemented; learned embeddings and generation are not implemented or represented as complete RAG.
- **M4.3 KG retrieval:** bounded asserted-graph retrieval implemented.
- **M4.4 hybrid retrieval:** deterministic local fusion implemented; no generated answers yet.
- **M4.5 ontology-grounded retrieval:** approved term/type/property constraints implemented; no additional axioms, inference or semantics invented.

Next concrete decision: select the generation model/access and a capped engineering-run budget, and approve the primary verification contrast before treating comparisons as experiments. A suitable proposal is fixed retrieval and model with verification disabled/enabled, reporting supported completion alongside unsupported broadening and excessive abstention. This is a proposal under the existing evaluation protocol, not a frozen metric/benchmark decision. M5 can then connect retrieval, claim attribution and qualified response synthesis. M6 remains optional; M7 still needs independently managed held-out material, reviewers, grading rules and statistical design. Design-question paraphrases are not held-out material.

No acquisition, model calls, ontology change, identity activation, M6 orchestration or M7 experiment occurred. Raw source bodies remain outside Git. No dependencies were installed. The full regression result is recorded after the integration run below.

## Final integration verification

**244 tests passed in 310.967 seconds**: all 229 previous regressions, two corpus integrity/relocation tests, four graph-characterisation tests and nine retrieval tests. Runtime: Python 3.12.7 and RDFLib 7.1.4, using the existing external dependency environment. Log: `/private/tmp/dementia-m3-m4-regression.log` (local execution record, not a portable release dependency).

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=tools:/private/tmp/ot2606-duckdb-inspection:/private/tmp/dementiagraph-m1-task008-pyshacl python3 -m unittest discover -s tests -v
```

Existing historical guards and source-replay tests passed. The approved ontology, M1 fixtures, identity receipts and prior M2 artifacts remain unchanged. No historical baseline finding was repaired or suppressed. The owner-approval appendix is the only modification to a pre-existing document in this milestone sequence; all other deliverables are new files. Git diff checks pass. No push was performed.
