# Research questions

Status: PROVISIONAL. No primary contrast is selected. Research gap and novelty: NOT YET VERIFIED.

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

Select a primary contrast only after checking source coverage, independently reviewable answer criteria, related work, implementation feasibility, and available review/compute budget. Specify the changed component, fixed conditions, measurable failure property, and evidence that could contradict the expectation. Owner approval is required before freezing the question or interpreting results as a contribution.
