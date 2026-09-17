# Research questions

Status: **M0 FROZEN / M1 ENTRY AUTHORIZED**. Checkpoint 4 approved the research emphasis, not an exact statistical hypothesis or executable experiment. Research gap and novelty: NOT YET VERIFIED. M1 has not begun.

## Task 005 approved emphasis freeze

D005 approves the **emphasis**, not an exact statistical hypothesis or experimental design: disease-scope verification with evidence access and retrieval held fixed. Can a defined semantic/provenance-aware check reduce unsupported broadening of source claims? Retain exactly two secondary emphases: provenance completeness/evidence dependency; and hierarchy/normalization/propagation interpretation.

Broadening includes narrower disease→broad claim, mechanism→indication, trial population→whole disease, mapped identity→unconditional equivalence, descendant-derived→direct evidence, and citation presence→claim support. These are existing Q01–Q07 failure boundaries, not new competency questions. The Task 004 discussion below supplies rationale and competing explanations.

D006 approves an explicit KG research project while retaining **graph advantage NOT YET DEMONSTRATED**. Later evaluation must test benefit against alternative representations/retrieval approaches with matched information access; that obligation does not select a second primary experiment now. Exact check, comparator implementation, statistical hypothesis, metrics, sample size and model remain unfrozen. Novelty remains NOT YET VERIFIED. [Freeze decisions](decisions/README.md#task-005-approved-m0-freeze-package) were approved at Checkpoint 4; later experimental choices still require owner approval.

## Historical Task 004 recommended emphasis

**Primary: disease-scope verification under fixed evidence access.** Proposed question: does a defined check that compares an answer claim's disease/population scope with its supporting records reduce unsupported broadening without causing excessive abstention? Q03–Q07 provide concrete scope boundaries; Q01/Q02 prevent citation presence and dependent records from being mistaken for stronger support. This narrows the prior generic provenance-verification proposal. It tests a limited property, not biomedical truth.

Proposed contrast is the same answering process/evidence bundle with versus without that check. Hold evidence access, retrieval output and generation conditions fixed; account explicitly for any extra tokens/retries. Exact mechanism, models, primary outcome definition and acceptable trade-off need owner approval. A null improvement or worse withholding on answerable cases would count against the proposed benefit. Current questions offer no experimental result.

At most two secondary emphases:

1. **Provenance completeness and dependency handling:** correct claim-to-record attribution, inspection depth and shared-source disclosure.
2. **Hierarchy interpretation:** distinguish direct normalized evidence, descendant inclusion and upstream normalization; assess mapping ambiguity without forced repair.

Retrieval strategy and ontology grounding are not additional primary claims. Graph-versus-vector performance cannot be justified by this inspection alone: complete text bundles or relational tables can support all seven cases. A later retrieval comparison would require its own approved controlled contrast. No graph-essential case is established.

AD-only is sufficient for the generic hypothesis. Bounded FTD adds inspected ambiguity/population/dependency cases and cross-disease contrasts; it does not establish a new research hypothesis or novelty. Review the existing related work before contribution claims. No additional paper-level novelty scan or T2DM-code comparison was performed in Task 004.

## Historical candidate framing and Task 002–003 implications

## Candidate questions

The handoff asks when explicit ontology semantics, graph structure, and deterministic verification improve LLM-based retrieval and answering over heterogeneous dementia knowledge questions, and when they do not. This remains a useful organizing question, but contains too many variables for a single interpretable primary experiment.

Candidate narrower primary questions are whether a defined evidence-checking mechanism changes unsupported claims and abstention under fixed retrieval, whether graph retrieval changes evidence recovery relative to vector retrieval under matched knowledge access, or whether an explicitly specified ontology-grounding operation changes entity/relation errors with other components fixed. These are alternatives for review, not approved experiments or established hypotheses.

Candidate secondary questions concern question-family differences, coverage-related failures, validator false positives and false negatives, and the latency or token cost of retained components. Topology-related analysis is conditional on a justified graph property and interpretable comparison.

## Operational definitions and competing explanations

| Term | Working meaning / unresolved boundary |
| --- | --- |
| Improvement | Change in prespecified outcomes relative to a defined comparator; primary metric and acceptable trade-offs remain undecided. |
| Ontology grounding | A named operation using approved semantic resources, rather than a label for the whole KG pipeline; exact operation undecided. |
| Graph contribution | Explicit relationships or paths used in evidence retrieval; database choice alone is not a contribution. |
| Verification | Checking a specified property under stated assumptions, not establishing biomedical truth. |
| Evidence support | Support under an approved claim-to-evidence rubric; evidence presence alone does not establish support. |
| Answerability | Sufficiency of the frozen evidence collection under the approved scope and rubric, not universal biomedical knowability. |

Apparent gains could arise from unequal evidence access, more tokens or retries, entity-linking differences, source coverage, question leakage, or stricter abstention rather than the studied component. Evaluation must distinguish these explanations where feasible. A gain in supported answers may coexist with worse coverage, latency, or excessive abstention.

## Narrowing gate

Task 002 evidence now constrains the alternatives. The [source audit](source_audit.md) found unequal phenotype coverage, large differences in target-association counts, provenance gaps, and direct/descendant-inclusive distinctions. The [focused related-work scan](related_work.md) found existing Alzheimer GraphRAG and KG-based claim-verification studies. Neither cross-disease breadth nor adding a verifier establishes novelty.

A candidate primary contrast worth investigating is a defined evidence/provenance check versus its absence with retrieval held fixed. It could distinguish source-supported association statements from unsupported causal or therapeutic verbalizations. This is not selected: usable evidence, independently reviewed claim criteria, and differentiation from prior work still need examination. Phenotype-rich four-disease QA must not be assumed feasible. Graph-versus-vector retrieval remains an alternative primary contrast, not an additional simultaneous primary claim.

Task 002A reproduced the reported counts but clarified that target totals count distinct target IDs in aggregated OT associations, phenotype totals count stored entries with nested evidence, and indication totals count consolidated drug–disease records. These units cannot rank candidate disease anchors. The second anchor is now explicitly undecided between source-defined MONDO:0007488 and FTD MONDO:0017276. The former could emphasize label-boundary/claim-transfer checks; the latter could emphasize subtype/propagation checks. Neither is an approved experimental contrast, and neither broad clinical LBD nor automatic FTD descendant inclusion is adopted.

Select a primary contrast only after checking source coverage, independently reviewable answer criteria, related work, implementation feasibility, and available review/compute budget. Specify the changed component, fixed conditions, measurable failure property, and evidence that could contradict the expectation. Owner approval is required before freezing the question or interpreting results as a contribution.


## Task 003 implications — recommendation, not selection

The matched audit and evidence-linked design questions now provide concrete scope-control cases: one shared target has different evidence/source contexts; direct and descendant-inclusive selections differ; normalized FTD records can hide narrower source labels/populations; mechanisms and indication reports support different propositions. Both pairings have six provisional source-record candidates and AD-only has four; these totals include repeated templates and are not validated evaluation sample sizes.

The strongest candidate focus is provenance-aware claim-scope verification under fixed retrieval/evidence access. A possible intervention would check whether answer claims retain the source disease, evidence type and indication scope, while measuring both unsupported generalization and excessive abstention. No specific verifier, graph schema, model, metric or experiment is selected. Clinical-precedence evidence is partly derived from drug/indication joins, so using those same edges as independent confirmation would be circular.

Task 003 provisionally favors AD + source-defined FTD with bounded subtype context; AD-only remains viable if expert review or distinct question value is insufficient. This supersedes the Task 002A undecided recommendation only as a proposal. It does not show that graph retrieval is necessary: source-aware tables or sufficiently complete text bundles can answer these questions too. A later study must test incremental value against matched access, not compare a rich KG with an impoverished text baseline.
