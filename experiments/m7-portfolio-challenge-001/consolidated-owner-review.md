# Consolidated M7 owner-review package

**All 12 questions · owner-directed review recorded · no additional model calls**

Designation: **Development-overlapping portfolio challenge set**. Reviewer: Subramanya Prasad. The rubric is assistant-prepared and owner-authorized for freezing; it is not independently authored gold. No clinical or independent validation is claimed.

## Scoring key and review instructions

1. All M7-01–M7-12 entries below are now recorded from the supplied owner review and its authorized operationalization. The remaining instructions explain the scoring key; they do not request a second review or authorize changes to frozen material.
2. M = model-only; G = KG-grounded; V = grounded plus local verification. G and V have exactly the same prose. Give them identical prose/fact/qualification judgments; their retained assertion surfaces are assessed separately.
3. Use S = supported, U = unsupported, C = contradicted, R = unresolved, relative to the frozen evidence. Use Y/N for boolean judgments. Blank means not yet scored, never zero. Use NONE explicitly when no required facts were correctly conveyed. Do not introduce a numerical 1–5 score.
4. In the prose table, quote each substantive proposition and label it S/U/C/R. Add rows as needed. Include biomedical claims, factual explanations and abstention/qualification statements; do not silently omit an unsupported proposition. G/V are scored together because their text is identical.
5. In each required-fact table enter Y only when that fact is correctly conveyed with its required source scope, otherwise N. Each fact counts once. For each retained assertion label support S/U/C/R, question relevance Y/N and provenance accuracy Y/N. These are owner judgments; an automated RDF pass does not prefill them.
6. Complete qualification pass Y/N for each condition. For M7-01–06 assess excessive abstention Y/N; for M7-07–12 assess required abstention/qualification behavior Y/N according to the frozen criteria, including any mixed answer-and-qualify disposition. Other cells are marked not applicable.
7. For retrieval coverage, record which required fact IDs have sufficient supplied evidence, which lack it and the evidence/statement basis. This is separate from whether the model mentioned them. If a fact-to-assertion match is unresolved, state that rather than inventing coverage.
8. Do not change the frozen questions, rubric, generated prose, structured claims or automated results. Note any rubric concern in comments. Your review will feed the existing frozen metric functions; this worksheet does not change their definitions.

Automated RDF verification checks exact supplied assertions and citations. It does not establish human prose correctness, relevance, source completeness, efficacy or clinical truth. Owner required-fact decisions and observations are now recorded below. Line-level labeling/segmentation and rubric operationalization were performed under the owner’s explicit instructions; no independent human review or new individual human attestation is claimed.

Owner: Subramanya Prasad. Review instruction provenance: `owner-review-instructions.txt`. Entry: assistant transcription and authorized operationalization; see `owner-review-scores.json`.

## Contents

- [M7-01](#m7-01)
- [M7-02](#m7-02)
- [M7-03](#m7-03)
- [M7-04](#m7-04)
- [M7-05](#m7-05)
- [M7-06](#m7-06)
- [M7-07](#m7-07)
- [M7-08](#m7-08)
- [M7-09](#m7-09)
- [M7-10](#m7-10)
- [M7-11](#m7-11)
- [M7-12](#m7-12)

## M7-01

<!-- BEGIN M7-01 QUESTION -->
Which drug or drugs in the graph have a mechanism connected to GRIN1 and GRIN3B, and what sources support those connections?
<!-- END M7-01 QUESTION -->

### Model-only answer — unchanged

<!-- BEGIN M7-01 MODEL-ONLY ANSWER -->
````text
I cannot determine which drugs in the graph have mechanisms connected to both GRIN1 and GRIN3B because the graph and its supporting sources were not supplied. From general knowledge, memantine and ketamine act on NMDA receptors, of which GRIN1 is an essential subunit. That does not establish a GRIN3B-specific connection for either drug or show that either appears in the graph. This is an unverified development-control answer, not clinical advice.
````
<!-- END M7-01 MODEL-ONLY ANSWER -->

<details><summary>Complete structured claims and unanswered fields — unchanged values</summary>

```json
{
  "claims": [],
  "unanswered": [
    "Which drugs are present in the graph?",
    "Which graph connections link drug mechanisms to GRIN1 and GRIN3B?",
    "What sources support each connection?"
  ]
}
```

</details>

### KG-grounded answer — unchanged

<!-- BEGIN M7-01 KG-GROUNDED ANSWER -->
````text
The retrieved mechanism records identify one drug, CHEMBL807, with connections to two target identifiers: ENSG00000176884 (GRIN1) and ENSG00000116032 (GRIN3B). Both records describe its mechanism as “Glutamate [NMDA] receptor negative allosteric modulator” and trace to the same row of Open Targets Platform’s drug_mechanism_of_action table, edition 26.06. These are source-reported connections, not two independent confirmations or evidence of gene-wide action or clinical efficacy.
````
<!-- END M7-01 KG-GROUNDED ANSWER -->

<details><summary>Complete structured claims and unanswered fields — unchanged values</summary>

```json
{
  "claims": [
    {
      "claim_type": "source_assertion",
      "explanation": "The drug identifier in the GRIN1-connected mechanism packet is CHEMBL807.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/57e1f91585eea6d91f5772d3babe29fa1241ea3eaf722bbd535ce53135a114c1",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/Drug/d6636d191f768d9a02bdd2d95057639e5c570fa3e78594dce327a0d27b3876b0> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#externalIdentifier> \"CHEMBL807\"^^<http://www.w3.org/2001/XMLSchema#string> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "This mechanism record links that drug to the target identified in the packet as ENSG00000176884.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/57e1f91585eea6d91f5772d3babe29fa1241ea3eaf722bbd535ce53135a114c1",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/57e1f91585eea6d91f5772d3babe29fa1241ea3eaf722bbd535ce53135a114c1> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#hasTarget> <https://github.com/subramanyaprasad21/dementia-kg-ai/id/Target/95bd026992ad84a3133d0be3a8c3a64073536a4f13a344fdbe744b076668f051> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "The first target's recorded identifier is ENSG00000176884.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/57e1f91585eea6d91f5772d3babe29fa1241ea3eaf722bbd535ce53135a114c1",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/Target/95bd026992ad84a3133d0be3a8c3a64073536a4f13a344fdbe744b076668f051> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#externalIdentifier> \"ENSG00000176884\"^^<http://www.w3.org/2001/XMLSchema#string> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "The second mechanism record links CHEMBL807 to the target identified in its packet as ENSG00000116032.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/bbe177073d1a5b77b7cd9a6d71dc779d221fd18954938288f7a44b611dd9a45a",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/bbe177073d1a5b77b7cd9a6d71dc779d221fd18954938288f7a44b611dd9a45a> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#hasTarget> <https://github.com/subramanyaprasad21/dementia-kg-ai/id/Target/f941f90f41909fda2dfefa50fe5c0d5a521a3b3c234dfd3f17cb845644b8da40> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "The second target's recorded identifier is ENSG00000116032.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/bbe177073d1a5b77b7cd9a6d71dc779d221fd18954938288f7a44b611dd9a45a",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/Target/f941f90f41909fda2dfefa50fe5c0d5a521a3b3c234dfd3f17cb845644b8da40> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#externalIdentifier> \"ENSG00000116032\"^^<http://www.w3.org/2001/XMLSchema#string> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "The mechanism description is source text, not an independently established biological conclusion.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/57e1f91585eea6d91f5772d3babe29fa1241ea3eaf722bbd535ce53135a114c1",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/57e1f91585eea6d91f5772d3babe29fa1241ea3eaf722bbd535ce53135a114c1> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#sourceText> \"Glutamate [NMDA] receptor negative allosteric modulator\"^^<http://www.w3.org/2001/XMLSchema#string> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "The recorded source authority is Open Targets Platform's drug_mechanism_of_action table.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/57e1f91585eea6d91f5772d3babe29fa1241ea3eaf722bbd535ce53135a114c1",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/SourceSnapshot/84363bedf050f9d01fb380554ae9aa39903fad4ea9897e3f67229f3410bdcf11> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#sourceAuthority> \"Open Targets Platform / drug_mechanism_of_action\"^^<http://www.w3.org/2001/XMLSchema#string> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "The first connection traces to source file row 3184; the second mechanism packet records the same row and file, so the records should not be counted as independent sources.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/57e1f91585eea6d91f5772d3babe29fa1241ea3eaf722bbd535ce53135a114c1",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/57e1f91585eea6d91f5772d3babe29fa1241ea3eaf722bbd535ce53135a114c1> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#sourceLocator> \"{\\\"fileRowNumber\\\":\\\"3184\\\",\\\"fileSha256\\\":\\\"4a02cef4c182bb0ed20d341c6c4553f6c839b02f3217777fb65993a38e456a29\\\",\\\"url\\\":\\\"https://ftp.ebi.ac.uk/pub/databases/opentargets/platform/26.06/output/drug_mechanism_of_action/part-00001-10b94b1b-f29a-440c-98e0-c91862b6d2a8-c000.snappy.parquet\\\"}\"^^<http://www.w3.org/2001/XMLSchema#string> ."
    }
  ],
  "unanswered": [
    "The supplied mechanism packets do not state a drug name for CHEMBL807 or explicitly give the GRIN1 and GRIN3B symbols alongside their Ensembl identifiers.",
    "Independent verification of the mechanism connections and their biological or clinical implications is not supplied."
  ]
}
```

</details>

### Local verification — automated, not owner scoring

Grounded and verified prose are identical. Submitted assertions: 8; accepted: 8; rejected: 0.

| Claim | Automated outcome | Reasons |
|---|---|---|
| G1 / V1 | RDF-ASSERTION-SUPPORTED | None |
| G2 / V2 | RDF-ASSERTION-SUPPORTED | None |
| G3 / V3 | RDF-ASSERTION-SUPPORTED | None |
| G4 / V4 | RDF-ASSERTION-SUPPORTED | None |
| G5 / V5 | RDF-ASSERTION-SUPPORTED | None |
| G6 / V6 | RDF-ASSERTION-SUPPORTED | None |
| G7 / V7 | RDF-ASSERTION-SUPPORTED | None |
| G8 / V8 | RDF-ASSERTION-SUPPORTED | None |

Model-only is unverified; it has no structured claims in this recorded run. Its prose still requires review.

### Frozen required facts

| Fact ID | Exact frozen requirement |
|---|---|
| M7-01-F1 | The two represented mechanism projections connect CHEMBL807 to ENSG00000176884 and ENSG00000116032. |
| M7-01-F2 | Both retain the exact source text Glutamate [NMDA] receptor negative allosteric modulator and the same original source-description context. |

### Frozen expected behavior and qualifications

**Expected disposition:** answer

Supported record facts may be reported with the listed boundaries; absent or out-of-scope evidence cannot license the prohibited conclusions.

- Memantine is the project/source name for CHEMBL807; the Drug RDF node itself need not contain that label.
- Report row/file/source context. FDA/Wikipedia reference details are in the captured source row, not necessarily supplied packet assertions. Do not fabricate those details.

### Frozen unsupported claims to penalize

- Two independent mechanism experiments
- Gene-wide clinical action or proven FTD benefit

### Frozen scoring criteria — verbatim

```json
{
  "scoringDimensions": [
    "source-relative assertion support",
    "human prose support/unsupported/contradicted/unresolved labels",
    "required-fact completion",
    "relevance",
    "provenance accuracy",
    "qualification and bounded abstention",
    "retrieval coverage",
    "failure/usage/cost"
  ],
  "scoringRequirements": {
    "excessiveAbstention": "Flag withholding supported required facts unnecessarily.",
    "proseLabels": "Sole human reviewer assigns supported/unsupported/contradicted/unresolved against frozen evidence; no clinical truth claim.",
    "qualificationPass": "All listed acceptable qualifications relevant to the response must be respected; no listed forbidden claim may be asserted.",
    "requiredAbstention": null,
    "requiredFactCompletion": "Each listed fact ID counted once only when correctly conveyed with source scope; all items have a nonzero required-fact denominator. Failures score zero completion.",
    "sharedGeneration": "Identical grounded/verified prose receives identical human prose scoring; retained assertion surfaces scored separately."
  }
}
```

<details><summary>Frozen retrieval scope and source references</summary>

```json
{
  "retrievalScope": {
    "maxPacketBytes": 196608,
    "mode": "hybrid",
    "records": 8,
    "rootIds": [
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/DerivedStatement/fd3db67ec6a05fdaa22d8c1407740e44cdbfc775cc25b2239bdfbd15268bd611",
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/9bb44911596e3db2ef337067480b7d127897e4c5c7918e8f2ac31bb4d803c66b",
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/bad88e8b10862169dcb3022359308caa2c0da43953e03fdcadaef53999bfcc7b",
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/57e1f91585eea6d91f5772d3babe29fa1241ea3eaf722bbd535ce53135a114c1",
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/bbe177073d1a5b77b7cd9a6d71dc779d221fd18954938288f7a44b611dd9a45a"
    ],
    "status": "FROZEN"
  },
  "sourceReferences": [
    "manifests/dementia-development-001.json",
    "kg/mondo-pilot-001/records.ttl",
    "kg/mondo-pilot-001/provenance.ttl",
    "kg/ot2606-evidence-001/records.ttl",
    "kg/ot2606-evidence-001/provenance.ttl",
    "kg/ot2606-context-001/records.ttl"
  ]
}
```

</details>

### Owner scoring — recorded under the supplied review instructions

**A. Source-relative prose labels** (S supported / U unsupported / C contradicted / R unresolved). All factual surfaces are considered. Exact copied propositions are counted once; surface membership is retained. Nonfactual disclaimers and questions are excluded.

| Condition / surfaces | Exact proposition | Label | Basis |
|---|---|---|---|
| M / answer_text | I cannot determine which drugs in the graph have mechanisms connected to both GRIN1 and GRIN3B because the graph and its supporting sources were not supplied. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| M / answer_text | From general knowledge, memantine and ketamine act on NMDA receptors, of which GRIN1 is an essential subunit. | U | Outside biomedical assertion not established by frozen project evidence. U is source-relative, not a real-world falsity judgment. Owner explicitly notes it is fenced off from corpus claims; not automatically a major failure. |
| M / answer_text | That does not establish a GRIN3B-specific connection for either drug or show that either appears in the graph. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | The retrieved mechanism records identify one drug, CHEMBL807, with connections to two target identifiers: ENSG00000176884 (GRIN1) and ENSG00000116032 (GRIN3B). | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | Both records describe its mechanism as “Glutamate [NMDA] receptor negative allosteric modulator” and trace to the same row of Open Targets Platform’s drug_mechanism_of_action table, edition 26.06. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | These are source-reported connections, not two independent confirmations or evidence of gene-wide action or clinical efficacy. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-1-explanation | The drug identifier in the GRIN1-connected mechanism packet is CHEMBL807. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-2-explanation | This mechanism record links that drug to the target identified in the packet as ENSG00000176884. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-3-explanation | The first target's recorded identifier is ENSG00000176884. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-4-explanation | The second mechanism record links CHEMBL807 to the target identified in its packet as ENSG00000116032. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-5-explanation | The second target's recorded identifier is ENSG00000116032. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-6-explanation | The mechanism description is source text, not an independently established biological conclusion. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-7-explanation | The recorded source authority is Open Targets Platform's drug_mechanism_of_action table. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-8-explanation | The first connection traces to source file row 3184; | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-8-explanation | the second mechanism packet records the same row and file, so the records should not be counted as independent sources. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / unanswered-1 | The supplied mechanism packets do not state a drug name for CHEMBL807 or explicitly give the GRIN1 and GRIN3B symbols alongside their Ensembl identifiers. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / unanswered-2 | Independent verification of the mechanism connections and their biological or clinical implications is not supplied. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |

Excluded nonfactual material is retained with reasons in the machine-readable review; original answers above remain untouched.

**B. Strict required-fact completion — owner decisions**

| Fact ID | M | G | V |
|---|---|---|---|
| M7-01-F1 | N | Y | Y |
| M7-01-F2 | N | Y | Y |

**C. Retained assertion judgments** — statement support, question relevance and citation/source provenance; not a completeness score. Model-only has no retained assertions; precision is undefined.

| Assertion | Support | Relevant? | Provenance correct? | Reason |
|---|---|---|---|---|
| G1 / V1 | S | Y | Y | Drug identity answers which drug; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G2 / V2 | S | Y | Y | First mechanism participant identifies target; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G3 / V3 | S | Y | Y | First target identifier resolves participant; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G4 / V4 | S | Y | Y | Second mechanism participant identifies target; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G5 / V5 | S | Y | Y | Second target identifier resolves participant; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G6 / V6 | S | Y | Y | Exact source mechanism text answers mechanism; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G7 / V7 | S | Y | Y | Source authority answers provenance; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G8 / V8 | S | Y | Y | Source row/file locator supports shared context; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |

**D. Qualification and abstention** — applied from frozen rules and owner observations.

| Condition | Qualification | Required abstention | Excessive abstention |
|---|---|---|---|
| M | Y | Not applicable | N |
| G | Y | Not applicable | N |
| V | Y | Not applicable | N |

Grounded respects the frozen source boundaries despite any detail omissions. Model-only Q08/Q10/Q12 fails corpus-only qualification because the owner identifies clinical/treatment scope leakage; other model-only scope qualifications are respected.

Q01–06: no unnecessary withholding is inferred. Model-only lacks corpus access intentionally; grounded detail omissions are not automatically excessive abstention.

**E. Retrieval coverage — separate from output completion**

Frozen supplied G/V packets contain the reference witnesses for: M7-01-F1, M7-01-F2. Missing fact witness sets: none. Exact statement witnesses and request hash are recorded in `owner-review-scores.json`. A prose omission does not remove evidence from these packets. Model-only retrieval coverage: not applicable, intentionally no retrieval.

**F. Owner comments — supplied observations**

- Model-only had no corpus access by design.
- It introduced general knowledge about memantine/ketamine and NMDA receptors, but clearly did not present that as evidence of what was in the graph.
- Grounded retrieved and used the required mechanism projections, identifiers, mechanism text and shared-source context.
- No important grounded completeness problem observed.
- Classification: grounded worked as intended.

**Residual annotation note:** No outside biomedical knowledge was used to resolve labels.

## M7-02

<!-- BEGIN M7-02 QUESTION -->
What disease concepts are the PSEN1 evidence records mapped to in the graph, and if mapping information is missing for any record, why?
<!-- END M7-02 QUESTION -->

### Model-only answer — unchanged

<!-- BEGIN M7-02 MODEL-ONLY ANSWER -->
````text
I cannot determine which disease concepts the PSEN1 evidence records are mapped to because no graph records or mapping information were supplied. I also cannot determine whether any mappings are missing or why. Although PSEN1 is commonly associated with familial early-onset Alzheimer disease, that general knowledge does not establish how these particular records are mapped. This is an unverified development-control response, not clinical advice.
````
<!-- END M7-02 MODEL-ONLY ANSWER -->

<details><summary>Complete structured claims and unanswered fields — unchanged values</summary>

```json
{
  "claims": [],
  "unanswered": [
    "Which disease concepts are assigned to each PSEN1 evidence record in the graph?",
    "Are any records missing a disease-concept mapping, and if so, what is the documented reason?"
  ]
}
```

</details>

### KG-grounded answer — unchanged

<!-- BEGIN M7-02 KG-GROUNDED ANSWER -->
````text
The supplied PSEN1 evidence records report two disease-concept destinations: MONDO_0017276 for a Genomics England record and one Europe PMC record, and MONDO_0004975 for another Europe PMC record. The Genomics England record has a stated mapping input, OMIM:600274, labelled “Dementia, frontotemporal.” Both Europe PMC records have a reported destination but lack the original disease mapping input: their missingness records attribute this to original disease input columns being absent from the historical Europe PMC Parquet schema. These are source-reported mappings marked validity-unreviewed, not reviewed biomedical equivalences.
````
<!-- END M7-02 KG-GROUNDED ANSWER -->

<details><summary>Complete structured claims and unanswered fields — unchanged values</summary>

```json
{
  "claims": [
    {
      "claim_type": "source_assertion",
      "explanation": "Candidate interpretation: this is the reported destination for the Genomics England evidence record.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/3b48e810b77da8e3a8cf3c3c2613c10b0321818543f06a2762da1be90ca8d950",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/3b48e810b77da8e3a8cf3c3c2613c10b0321818543f06a2762da1be90ca8d950> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#reportedDestination> <https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/115e9f610af71460664bb63b5e5cf112710effd9027cd0ed71d4cfe3528eb29e> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "Candidate interpretation: the destination's recorded identifier is MONDO_0017276.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/3b48e810b77da8e3a8cf3c3c2613c10b0321818543f06a2762da1be90ca8d950",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/115e9f610af71460664bb63b5e5cf112710effd9027cd0ed71d4cfe3528eb29e> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#externalIdentifier> \"MONDO_0017276\"^^<http://www.w3.org/2001/XMLSchema#string> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "Candidate interpretation: this record supplies an original mapping input, unlike the two Europe PMC records.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/3b48e810b77da8e3a8cf3c3c2613c10b0321818543f06a2762da1be90ca8d950",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/08501ee3ac587ca779987f31b5db4192c5299e442d309286f36abcb8975e1a26> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#sourceLabel> \"Dementia, frontotemporal\"^^<http://www.w3.org/2001/XMLSchema#string> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "Candidate interpretation: this is the recorded identifier of that input.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/3b48e810b77da8e3a8cf3c3c2613c10b0321818543f06a2762da1be90ca8d950",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/08501ee3ac587ca779987f31b5db4192c5299e442d309286f36abcb8975e1a26> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#externalIdentifier> \"OMIM:600274\"^^<http://www.w3.org/2001/XMLSchema#string> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "Candidate interpretation: one Europe PMC record reports this destination.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/f365eb4f448c10ca07d06c86a6ce5dcad272803814f5addd0252b32ad02d1f04",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/f365eb4f448c10ca07d06c86a6ce5dcad272803814f5addd0252b32ad02d1f04> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#reportedDestination> <https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/5c9ccec62fe78b3e3bb8f60611bec066644f4beb6ef4a343232ebf91a22e723d> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "Candidate interpretation: that Europe PMC destination has the recorded identifier MONDO_0017276.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/f365eb4f448c10ca07d06c86a6ce5dcad272803814f5addd0252b32ad02d1f04",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/5c9ccec62fe78b3e3bb8f60611bec066644f4beb6ef4a343232ebf91a22e723d> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#externalIdentifier> \"MONDO_0017276\"^^<http://www.w3.org/2001/XMLSchema#string> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "Candidate interpretation: the other Europe PMC record reports this destination.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/ceefabe649d86c21686cb3476cd3cb58a2907701447958f54a81fa441e40677f",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/ceefabe649d86c21686cb3476cd3cb58a2907701447958f54a81fa441e40677f> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#reportedDestination> <https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/c049c408b5f38644d770b361909e043473b21df50c171a69f0e3039bd51abacc> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "Candidate interpretation: that destination has the recorded identifier MONDO_0004975; no source label for it is supplied here.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/ceefabe649d86c21686cb3476cd3cb58a2907701447958f54a81fa441e40677f",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/c049c408b5f38644d770b361909e043473b21df50c171a69f0e3039bd51abacc> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#externalIdentifier> \"MONDO_0004975\"^^<http://www.w3.org/2001/XMLSchema#string> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "Candidate interpretation requiring review: this records why the original mapping input is missing for the Europe PMC record reporting MONDO_0017276, not why its destination is missing.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MissingnessRecord/6e936f84b8434a6a8c7479f36d0792a0b60dc3745021234dcc88164983e3a394",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/MissingnessRecord/6e936f84b8434a6a8c7479f36d0792a0b60dc3745021234dcc88164983e3a394> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#rationale> \"Original disease input columns absent in the historical Europe PMC Parquet schema; not evidence of biological absence or a reproduced GraphQL null.\"^^<http://www.w3.org/2001/XMLSchema#string> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "Candidate interpretation requiring review: the same stated schema limitation applies to the Europe PMC record reporting MONDO_0004975.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MissingnessRecord/af7a7011477848f8309397edf525843d62d42708f7064b29444593d8fdb9ec21",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/MissingnessRecord/af7a7011477848f8309397edf525843d62d42708f7064b29444593d8fdb9ec21> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#rationale> \"Original disease input columns absent in the historical Europe PMC Parquet schema; not evidence of biological absence or a reproduced GraphQL null.\"^^<http://www.w3.org/2001/XMLSchema#string> ."
    }
  ],
  "unanswered": [
    "The original disease mapping inputs for the two Europe PMC records cannot be recovered from the supplied packets.",
    "The upstream mapping methods and biomedical validity of the reported assignments are not established by these packets."
  ]
}
```

</details>

### Local verification — automated, not owner scoring

Grounded and verified prose are identical. Submitted assertions: 10; accepted: 10; rejected: 0.

| Claim | Automated outcome | Reasons |
|---|---|---|
| G1 / V1 | RDF-ASSERTION-SUPPORTED | None |
| G2 / V2 | RDF-ASSERTION-SUPPORTED | None |
| G3 / V3 | RDF-ASSERTION-SUPPORTED | None |
| G4 / V4 | RDF-ASSERTION-SUPPORTED | None |
| G5 / V5 | RDF-ASSERTION-SUPPORTED | None |
| G6 / V6 | RDF-ASSERTION-SUPPORTED | None |
| G7 / V7 | RDF-ASSERTION-SUPPORTED | None |
| G8 / V8 | RDF-ASSERTION-SUPPORTED | None |
| G9 / V9 | RDF-ASSERTION-SUPPORTED | None |
| G10 / V10 | RDF-ASSERTION-SUPPORTED | None |

Model-only is unverified; it has no structured claims in this recorded run. Its prose still requires review.

### Frozen required facts

| Fact ID | Exact frozen requirement |
|---|---|
| M7-02-F1 | The three PSEN1 occurrences have destinations MONDO_0004975, MONDO_0017276 and MONDO_0017276 respectively for IDs 1261ad02…, 986bb22b…, 98c49197…. |
| M7-02-F2 | The GE record retains OMIM:600274 and Dementia, frontotemporal; the two literature mappings lack original disease input and retain missingness qualification. |

### Frozen expected behavior and qualifications

**Expected disposition:** mixed

Supported record facts may be reported with the listed boundaries; absent or out-of-scope evidence cannot license the prohibited conclusions.

- Normalized destinations are present; missing original fields do not mean every mapping field is missing.
- The graph records absent source information, not why the upstream source omitted it; no mapping equivalence is validated.

### Frozen unsupported claims to penalize

- An invented upstream omission explanation
- Global equivalence or causal AD/FTD claims

### Frozen scoring criteria — verbatim

```json
{
  "scoringDimensions": [
    "source-relative assertion support",
    "human prose support/unsupported/contradicted/unresolved labels",
    "required-fact completion",
    "relevance",
    "provenance accuracy",
    "qualification and bounded abstention",
    "retrieval coverage",
    "failure/usage/cost"
  ],
  "scoringRequirements": {
    "excessiveAbstention": "Flag withholding supported required facts unnecessarily.",
    "proseLabels": "Sole human reviewer assigns supported/unsupported/contradicted/unresolved against frozen evidence; no clinical truth claim.",
    "qualificationPass": "All listed acceptable qualifications relevant to the response must be respected; no listed forbidden claim may be asserted.",
    "requiredAbstention": null,
    "requiredFactCompletion": "Each listed fact ID counted once only when correctly conveyed with source scope; all items have a nonzero required-fact denominator. Failures score zero completion.",
    "sharedGeneration": "Identical grounded/verified prose receives identical human prose scoring; retained assertion surfaces scored separately."
  }
}
```

<details><summary>Frozen retrieval scope and source references</summary>

```json
{
  "retrievalScope": {
    "maxPacketBytes": 196608,
    "mode": "hybrid",
    "records": 8,
    "rootIds": [
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/3b48e810b77da8e3a8cf3c3c2613c10b0321818543f06a2762da1be90ca8d950",
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/ceefabe649d86c21686cb3476cd3cb58a2907701447958f54a81fa441e40677f",
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/f365eb4f448c10ca07d06c86a6ce5dcad272803814f5addd0252b32ad02d1f04",
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MissingnessRecord/6e936f84b8434a6a8c7479f36d0792a0b60dc3745021234dcc88164983e3a394",
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MissingnessRecord/af7a7011477848f8309397edf525843d62d42708f7064b29444593d8fdb9ec21"
    ],
    "status": "FROZEN"
  },
  "sourceReferences": [
    "manifests/dementia-development-001.json",
    "kg/mondo-pilot-001/records.ttl",
    "kg/mondo-pilot-001/provenance.ttl",
    "kg/ot2606-evidence-001/records.ttl",
    "kg/ot2606-evidence-001/provenance.ttl",
    "kg/ot2606-context-001/records.ttl"
  ]
}
```

</details>

### Owner scoring — recorded under the supplied review instructions

**A. Source-relative prose labels** (S supported / U unsupported / C contradicted / R unresolved). All factual surfaces are considered. Exact copied propositions are counted once; surface membership is retained. Nonfactual disclaimers and questions are excluded.

| Condition / surfaces | Exact proposition | Label | Basis |
|---|---|---|---|
| M / answer_text | I cannot determine which disease concepts the PSEN1 evidence records are mapped to because no graph records or mapping information were supplied. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| M / answer_text | I also cannot determine whether any mappings are missing or why. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| M / answer_text | Although PSEN1 is commonly associated with familial early-onset Alzheimer disease, | U | Outside biomedical assertion not established by frozen project evidence. U is source-relative, not a real-world falsity judgment. Owner explicitly notes it is fenced off from corpus claims; not automatically a major failure. |
| M / answer_text | that general knowledge does not establish how these particular records are mapped. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | The supplied PSEN1 evidence records report two disease-concept destinations: MONDO_0017276 for a Genomics England record and one Europe PMC record, and MONDO_0004975 for another Europe PMC record. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | The Genomics England record has a stated mapping input, OMIM:600274, labelled “Dementia, frontotemporal.” | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | Both Europe PMC records have a reported destination but lack the original disease mapping input: their missingness records attribute this to original disease input columns being absent from the historical Europe PMC Parquet schema. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | These are source-reported mappings marked validity-unreviewed, not reviewed biomedical equivalences. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-1-explanation | Candidate interpretation: this is the reported destination for the Genomics England evidence record. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-2-explanation | Candidate interpretation: the destination's recorded identifier is MONDO_0017276. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-3-explanation | Candidate interpretation: this record supplies an original mapping input, unlike the two Europe PMC records. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-4-explanation | Candidate interpretation: this is the recorded identifier of that input. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-5-explanation | Candidate interpretation: one Europe PMC record reports this destination. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-6-explanation | Candidate interpretation: that Europe PMC destination has the recorded identifier MONDO_0017276. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-7-explanation | Candidate interpretation: the other Europe PMC record reports this destination. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-8-explanation | Candidate interpretation: that destination has the recorded identifier MONDO_0004975; | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-8-explanation | no source label for it is supplied here. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-9-explanation | Candidate interpretation requiring review: this records why the original mapping input is missing for the Europe PMC record reporting MONDO_0017276, not why its destination is missing. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-10-explanation | Candidate interpretation requiring review: the same stated schema limitation applies to the Europe PMC record reporting MONDO_0004975. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / unanswered-1 | The original disease mapping inputs for the two Europe PMC records cannot be recovered from the supplied packets. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / unanswered-2 | The upstream mapping methods and biomedical validity of the reported assignments are not established by these packets. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |

Excluded nonfactual material is retained with reasons in the machine-readable review; original answers above remain untouched.

**B. Strict required-fact completion — owner decisions**

| Fact ID | M | G | V |
|---|---|---|---|
| M7-02-F1 | N | Y | Y |
| M7-02-F2 | N | Y | Y |

**C. Retained assertion judgments** — statement support, question relevance and citation/source provenance; not a completeness score. Model-only has no retained assertions; precision is undefined.

| Assertion | Support | Relevant? | Provenance correct? | Reason |
|---|---|---|---|---|
| G1 / V1 | S | Y | Y | GE destination linkage; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G2 / V2 | S | Y | Y | GE destination identifier; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G3 / V3 | S | Y | Y | Original GE disease input label; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G4 / V4 | S | Y | Y | Original GE input identifier; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G5 / V5 | S | Y | Y | First literature destination link; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G6 / V6 | S | Y | Y | First literature destination identifier; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G7 / V7 | S | Y | Y | Second literature destination link; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G8 / V8 | S | Y | Y | Second literature destination identifier; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G9 / V9 | S | Y | Y | First original-input missingness rationale; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G10 / V10 | S | Y | Y | Second original-input missingness rationale; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |

**D. Qualification and abstention** — applied from frozen rules and owner observations.

| Condition | Qualification | Required abstention | Excessive abstention |
|---|---|---|---|
| M | Y | Not applicable | N |
| G | Y | Not applicable | N |
| V | Y | Not applicable | N |

Grounded respects the frozen source boundaries despite any detail omissions. Model-only Q08/Q10/Q12 fails corpus-only qualification because the owner identifies clinical/treatment scope leakage; other model-only scope qualifications are respected.

Q01–06: no unnecessary withholding is inferred. Model-only lacks corpus access intentionally; grounded detail omissions are not automatically excessive abstention.

**E. Retrieval coverage — separate from output completion**

Frozen supplied G/V packets contain the reference witnesses for: M7-02-F1, M7-02-F2. Missing fact witness sets: none. Exact statement witnesses and request hash are recorded in `owner-review-scores.json`. A prose omission does not remove evidence from these packets. Model-only retrieval coverage: not applicable, intentionally no retrieval.

**F. Owner comments — supplied observations**

- Model-only had no corpus access by design.
- It mentioned general PSEN1/familial-AD knowledge but explicitly said this did not establish how these particular records were mapped.
- Grounded correctly recovered the MONDO destinations, Genomics England mapping input and Europe PMC missingness explanation.
- No important grounded completeness problem observed.
- Classification: grounded worked as intended.

**Residual annotation note:** No outside biomedical knowledge was used to resolve labels.

## M7-03

<!-- BEGIN M7-03 QUESTION -->
Which disease concepts connected to APP are represented in the current evidence corpus, and what are their sources?
<!-- END M7-03 QUESTION -->

### Model-only answer — unchanged

<!-- BEGIN M7-03 MODEL-ONLY ANSWER -->
````text
No evidence corpus was supplied, so I cannot determine which disease concepts connected to APP are represented in it or identify their sources. From model knowledge, APP is associated with Alzheimer’s disease and cerebral amyloid angiopathy, but that does not establish that either appears in the current corpus. This is an unverified development-control answer, not clinical advice.
````
<!-- END M7-03 MODEL-ONLY ANSWER -->

<details><summary>Complete structured claims and unanswered fields — unchanged values</summary>

```json
{
  "claims": [],
  "unanswered": [
    "Which APP-connected disease concepts are represented in the current evidence corpus?",
    "What are the sources for those concepts?"
  ]
}
```

</details>

### KG-grounded answer — unchanged

<!-- BEGIN M7-03 KG-GROUNDED ANSWER -->
````text
The supplied records connect the APP target (ENSG00000142192) to a Genomics England evidence occurrence whose source disease is “Alzheimer disease 1, familial” (OMIM:104300) and whose reported destination is MONDO_0007088. Mondo labels that destination “Alzheimer disease type 1” (MONDO:0007088) and reports an immediate-parent path through “early-onset autosomal dominant Alzheimer disease” (MONDO:0015140), “familial Alzheimer disease” (MONDO:0100087), and “Alzheimer disease” (MONDO:0004975). The Genomics England record is supplied through Open Targets Platform 26.06; the hierarchy comes from Mondo via EMBL-EBI OLS, edition 2026-09-01. This is a candidate reading of the retrieved records, not a validated disease association or a claim that the mapping establishes biomedical equivalence.
````
<!-- END M7-03 KG-GROUNDED ANSWER -->

<details><summary>Complete structured claims and unanswered fields — unchanged values</summary>

```json
{
  "claims": [
    {
      "claim_type": "source_assertion",
      "explanation": "The Genomics England evidence occurrence has the target whose recorded Ensembl identifier is ENSG00000142192; the packet does not supply a target-symbol triple.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/e10a18e680a100ce9ab8dea84d460991ae41e86378a939068732300c8a7a8ec7",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/EvidenceOccurrence/796696cbe1d8a518d5e57a122ddff4d49ed47f7ef40eeef4ab45186e7956ffe6> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#hasTarget> <https://github.com/subramanyaprasad21/dementia-kg-ai/id/Target/ab286f8dc660098033c6eae4a04a8c626c2d0429bb6df202af6d91888683c3ea> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "The source disease label attached to the occurrence’s mapping input is “Alzheimer disease 1, familial”; its identifier is OMIM:104300.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/e10a18e680a100ce9ab8dea84d460991ae41e86378a939068732300c8a7a8ec7",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/ed6dfb77e60621587045037175e0c6bfe61e86e6f650a09b9eb0a1ae384379ac> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#sourceLabel> \"Alzheimer disease 1, familial\"^^<http://www.w3.org/2001/XMLSchema#string> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "The Genomics England mapping reports a MONDO_0007088 destination; its recorded status is validity-unreviewed, not an equivalence determination.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/e10a18e680a100ce9ab8dea84d460991ae41e86378a939068732300c8a7a8ec7",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/afa9d8c09be76fef8779912526900975a7533e58b4740b43fd4af38bd44ef0fd> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#externalIdentifier> \"MONDO_0007088\"^^<http://www.w3.org/2001/XMLSchema#string> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "Mondo’s label for MONDO:0007088 is “Alzheimer disease type 1.”",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/HierarchyStep/9dbc4821c39c5ceb692fc73095131c200359c653dfc6ce0a0b355fadb756b8f8",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/94956f7d1148eef0e6a25454e94d4aa318f7f757457667eee343de4280c299da> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#sourceLabel> \"Alzheimer disease type 1\"^^<http://www.w3.org/2001/XMLSchema#string> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "The next Mondo concept on the reported immediate-parent path is “early-onset autosomal dominant Alzheimer disease” (MONDO:0015140).",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/HierarchyStep/9dbc4821c39c5ceb692fc73095131c200359c653dfc6ce0a0b355fadb756b8f8",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/bcd3ca8a4dfbf567bb35be1b516ad2278c40cc18254bcb2e6cd4cf75870edd80> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#sourceLabel> \"early-onset autosomal dominant Alzheimer disease\"^^<http://www.w3.org/2001/XMLSchema#string> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "Mondo records “familial Alzheimer disease” (MONDO:0100087) as the next concept on that parent path.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/HierarchyStep/677460eea8f681aaa0de334dc1973cfea6d9552515da4d0d8aab9a6c94ec73a3",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/8f1c74a3739d161dc1d7e3ec70e5de9d2ca810daf052041b5e2d6695d0c5168e> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#sourceLabel> \"familial Alzheimer disease\"^^<http://www.w3.org/2001/XMLSchema#string> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "Mondo records “Alzheimer disease” (MONDO:0004975) above familial Alzheimer disease on the reported immediate-parent path.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/HierarchyStep/e63bdc528cafa7ca08d8e902f71f4de3f96f826e5d4053778898020df9cc3850",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/56e84bf4b4a25940c7a39128c743710b469a768016bee72e1e1f922fc4cff8db> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#sourceLabel> \"Alzheimer disease\"^^<http://www.w3.org/2001/XMLSchema#string> ."
    }
  ],
  "unanswered": [
    "Whether these retrieved packets exhaust all APP-connected disease concepts in the current corpus.",
    "Whether the reported Genomics England disease mapping establishes biomedical equivalence or a validated APP–disease association."
  ]
}
```

</details>

### Local verification — automated, not owner scoring

Grounded and verified prose are identical. Submitted assertions: 7; accepted: 7; rejected: 0.

| Claim | Automated outcome | Reasons |
|---|---|---|
| G1 / V1 | RDF-ASSERTION-SUPPORTED | None |
| G2 / V2 | RDF-ASSERTION-SUPPORTED | None |
| G3 / V3 | RDF-ASSERTION-SUPPORTED | None |
| G4 / V4 | RDF-ASSERTION-SUPPORTED | None |
| G5 / V5 | RDF-ASSERTION-SUPPORTED | None |
| G6 / V6 | RDF-ASSERTION-SUPPORTED | None |
| G7 / V7 | RDF-ASSERTION-SUPPORTED | None |

Model-only is unverified; it has no structured claims in this recorded run. Its prose still requires review.

### Frozen required facts

| Fact ID | Exact frozen requirement |
|---|---|
| M7-03-F1 | APP evidence retains original OMIM:104300 / Alzheimer disease 1, familial and destination MONDO_0007088. |
| M7-03-F2 | The three accepted steps connect that destination through MONDO:0015140 and MONDO:0100087 to MONDO:0004975. |
| M7-03-F3 | A separate APP-indexed lecanemab mechanism and AD indication are represented; indication is not an APP causal assertion. |

### Frozen expected behavior and qualifications

**Expected disposition:** mixed

Supported record facts may be reported with the listed boundaries; absent or out-of-scope evidence cannot license the prohibited conclusions.

- Distinguish evidence mapping, hierarchy path and drug indication rather than merging all as direct APP disease assertions.
- Corpus is finite; source citation presence is not publication adjudication.

### Frozen unsupported claims to penalize

- A direct APP causal edge to every ancestor
- Complete disease coverage

### Frozen scoring criteria — verbatim

```json
{
  "scoringDimensions": [
    "source-relative assertion support",
    "human prose support/unsupported/contradicted/unresolved labels",
    "required-fact completion",
    "relevance",
    "provenance accuracy",
    "qualification and bounded abstention",
    "retrieval coverage",
    "failure/usage/cost"
  ],
  "scoringRequirements": {
    "excessiveAbstention": "Flag withholding supported required facts unnecessarily.",
    "proseLabels": "Sole human reviewer assigns supported/unsupported/contradicted/unresolved against frozen evidence; no clinical truth claim.",
    "qualificationPass": "All listed acceptable qualifications relevant to the response must be respected; no listed forbidden claim may be asserted.",
    "requiredAbstention": null,
    "requiredFactCompletion": "Each listed fact ID counted once only when correctly conveyed with source scope; all items have a nonzero required-fact denominator. Failures score zero completion.",
    "sharedGeneration": "Identical grounded/verified prose receives identical human prose scoring; retained assertion surfaces scored separately."
  }
}
```

<details><summary>Frozen retrieval scope and source references</summary>

```json
{
  "retrievalScope": {
    "maxPacketBytes": 196608,
    "mode": "hybrid",
    "records": 8,
    "rootIds": [
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/ClinicalIndicationRecord/8d409cf761cbae391ba0ac03b3aee9046100d030f6779e9ecaad80c4cd11815b",
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/HierarchyStep/677460eea8f681aaa0de334dc1973cfea6d9552515da4d0d8aab9a6c94ec73a3",
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/HierarchyStep/9dbc4821c39c5ceb692fc73095131c200359c653dfc6ce0a0b355fadb756b8f8",
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/HierarchyStep/e63bdc528cafa7ca08d8e902f71f4de3f96f826e5d4053778898020df9cc3850",
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/e10a18e680a100ce9ab8dea84d460991ae41e86378a939068732300c8a7a8ec7",
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/a413f6671dc36fa70a1079361b6b4236fb96a9e594c1785b40f8ee445869f6fb"
    ],
    "status": "FROZEN"
  },
  "sourceReferences": [
    "manifests/dementia-development-001.json",
    "kg/mondo-pilot-001/records.ttl",
    "kg/mondo-pilot-001/provenance.ttl",
    "kg/ot2606-evidence-001/records.ttl",
    "kg/ot2606-evidence-001/provenance.ttl",
    "kg/ot2606-context-001/records.ttl"
  ]
}
```

</details>

### Owner scoring — recorded under the supplied review instructions

**A. Source-relative prose labels** (S supported / U unsupported / C contradicted / R unresolved). All factual surfaces are considered. Exact copied propositions are counted once; surface membership is retained. Nonfactual disclaimers and questions are excluded.

| Condition / surfaces | Exact proposition | Label | Basis |
|---|---|---|---|
| M / answer_text | No evidence corpus was supplied, so I cannot determine which disease concepts connected to APP are represented in it or identify their sources. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| M / answer_text | From model knowledge, APP is associated with Alzheimer’s disease and cerebral amyloid angiopathy, | U | Outside biomedical assertion not established by frozen project evidence. U is source-relative, not a real-world falsity judgment. Owner explicitly notes it is fenced off from corpus claims; not automatically a major failure. |
| M / answer_text | but that does not establish that either appears in the current corpus. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | The supplied records connect the APP target (ENSG00000142192) to a Genomics England evidence occurrence whose source disease is “Alzheimer disease 1, familial” (OMIM:104300) and whose reported destination is MONDO_0007088. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | Mondo labels that destination “Alzheimer disease type 1” (MONDO:0007088) and reports an immediate-parent path through “early-onset autosomal dominant Alzheimer disease” (MONDO:0015140), “familial Alzheimer disease” (MONDO:0100087), and “Alzheimer disease” (MONDO:0004975). | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | The Genomics England record is supplied through Open Targets Platform 26.06; | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | the hierarchy comes from Mondo via EMBL-EBI OLS, edition 2026-09-01. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | This is a candidate reading of the retrieved records, not a validated disease association or a claim that the mapping establishes biomedical equivalence. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-1-explanation | The Genomics England evidence occurrence has the target whose recorded Ensembl identifier is ENSG00000142192; | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-1-explanation | the packet does not supply a target-symbol triple. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-2-explanation | The source disease label attached to the occurrence’s mapping input is “Alzheimer disease 1, familial”; | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-2-explanation | its identifier is OMIM:104300. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-3-explanation | The Genomics England mapping reports a MONDO_0007088 destination; | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-3-explanation | its recorded status is validity-unreviewed, not an equivalence determination. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-4-explanation | Mondo’s label for MONDO:0007088 is “Alzheimer disease type 1.” | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-5-explanation | The next Mondo concept on the reported immediate-parent path is “early-onset autosomal dominant Alzheimer disease” (MONDO:0015140). | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-6-explanation | Mondo records “familial Alzheimer disease” (MONDO:0100087) as the next concept on that parent path. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-7-explanation | Mondo records “Alzheimer disease” (MONDO:0004975) above familial Alzheimer disease on the reported immediate-parent path. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |

Excluded nonfactual material is retained with reasons in the machine-readable review; original answers above remain untouched.

**B. Strict required-fact completion — owner decisions**

| Fact ID | M | G | V |
|---|---|---|---|
| M7-03-F1 | N | Y | Y |
| M7-03-F2 | N | Y | Y |
| M7-03-F3 | N | N | N |

**C. Retained assertion judgments** — statement support, question relevance and citation/source provenance; not a completeness score. Model-only has no retained assertions; precision is undefined.

| Assertion | Support | Relevant? | Provenance correct? | Reason |
|---|---|---|---|---|
| G1 / V1 | S | Y | Y | APP occurrence participant; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G2 / V2 | S | Y | Y | Original familial AD disease label; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G3 / V3 | S | Y | Y | Normalized destination identifier; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G4 / V4 | S | Y | Y | First hierarchy node label; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G5 / V5 | S | Y | Y | Intermediate hierarchy node label; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G6 / V6 | S | Y | Y | Intermediate hierarchy node label; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G7 / V7 | S | Y | Y | Terminal hierarchy node label; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |

**D. Qualification and abstention** — applied from frozen rules and owner observations.

| Condition | Qualification | Required abstention | Excessive abstention |
|---|---|---|---|
| M | Y | Not applicable | N |
| G | Y | Not applicable | N |
| V | Y | Not applicable | N |

Grounded respects the frozen source boundaries despite any detail omissions. Model-only Q08/Q10/Q12 fails corpus-only qualification because the owner identifies clinical/treatment scope leakage; other model-only scope qualifications are respected.

Q01–06: no unnecessary withholding is inferred. Model-only lacks corpus access intentionally; grounded detail omissions are not automatically excessive abstention.

**E. Retrieval coverage — separate from output completion**

Frozen supplied G/V packets contain the reference witnesses for: M7-03-F1, M7-03-F2, M7-03-F3. Missing fact witness sets: none. Exact statement witnesses and request hash are recorded in `owner-review-scores.json`. A prose omission does not remove evidence from these packets. Model-only retrieval coverage: not applicable, intentionally no retrieval.

**F. Owner comments — supplied observations**

- Model-only had no corpus access and mentioned general APP knowledge, while correctly separating that from corpus evidence.
- Grounded correctly used APP disease mapping and hierarchy evidence.
- However, it omitted the separate APP-indexed lecanemab mechanism and AD indication even though those records were available.
- Classification: candidate grounded evidence-integration/completeness gap.
- Do NOT call this a retrieval failure or ontology defect; the cause is not established.

**Residual annotation note:** No outside biomedical knowledge was used to resolve labels.

## M7-04

<!-- BEGIN M7-04 QUESTION -->
Do GRIN1, GRIN3B and APP point to the same study or report, or different ones? If two of the three share one, tell me which two, and explain where the third one's evidence comes from.
<!-- END M7-04 QUESTION -->

### Model-only answer — unchanged

<!-- BEGIN M7-04 MODEL-ONLY ANSWER -->
````text
I can’t determine whether GRIN1, GRIN3B and APP point to the same study or report from the information provided. No study identifiers, reports or source records were supplied, so I can’t verify whether two share a source or where the third gene’s evidence comes from. This is an unverified development control, not clinical advice.
````
<!-- END M7-04 MODEL-ONLY ANSWER -->

<details><summary>Complete structured claims and unanswered fields — unchanged values</summary>

```json
{
  "claims": [],
  "unanswered": [
    "Which studies or reports are linked to GRIN1, GRIN3B and APP?",
    "Do any two genes share the same source, and what is the source for the third?"
  ]
}
```

</details>

### KG-grounded answer — unchanged

<!-- BEGIN M7-04 KG-GROUNDED ANSWER -->
````text
GRIN1 and GRIN3B point to the same reported study, nct00594737, in two Open Targets clinical_precedence records. APP’s supplied evidence comes instead from an Open Targets genomics_england record concerning “Alzheimer disease 1, familial”; it is not presented here as a clinical report for that study. This is a comparison of the supplied records, not an assessment of biological relationships or study outcomes.
````
<!-- END M7-04 KG-GROUNDED ANSWER -->

<details><summary>Complete structured claims and unanswered fields — unchanged values</summary>

```json
{
  "claims": [
    {
      "claim_type": "source_assertion",
      "explanation": "The GRIN1-linked occurrence refers to the shared study. Candidate interpretation requiring review.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/DerivedStatement/fd3db67ec6a05fdaa22d8c1407740e44cdbfc775cc25b2239bdfbd15268bd611",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/EvidenceOccurrence/7761d516706013aba8ffe20a7b45209f04fdbb1dbaf649cd6d51917a87dc6a80> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#refersToStudy> <https://github.com/subramanyaprasad21/dementia-kg-ai/id/Study/613b6fe05a946c8ee1c2d055f0a28809bdeb1c1be593d0115d1b6d543b9cc4b7> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "The GRIN3B-linked occurrence refers to that same study. Candidate interpretation requiring review.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/DerivedStatement/fd3db67ec6a05fdaa22d8c1407740e44cdbfc775cc25b2239bdfbd15268bd611",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/EvidenceOccurrence/b845e08aa2a1a47ad4e331d75ff3b2cc86250fd2c13b82fee2d5044f02c769c6> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#refersToStudy> <https://github.com/subramanyaprasad21/dementia-kg-ai/id/Study/613b6fe05a946c8ee1c2d055f0a28809bdeb1c1be593d0115d1b6d543b9cc4b7> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "The shared study has this recorded identifier. Candidate interpretation requiring review.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/DerivedStatement/fd3db67ec6a05fdaa22d8c1407740e44cdbfc775cc25b2239bdfbd15268bd611",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/Study/613b6fe05a946c8ee1c2d055f0a28809bdeb1c1be593d0115d1b6d543b9cc4b7> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#externalIdentifier> \"nct00594737\"^^<http://www.w3.org/2001/XMLSchema#string> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "APP’s supplied occurrence is classified as genomics_england evidence. Candidate interpretation requiring review.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/e10a18e680a100ce9ab8dea84d460991ae41e86378a939068732300c8a7a8ec7",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/EvidenceOccurrence/796696cbe1d8a518d5e57a122ddff4d49ed47f7ef40eeef4ab45186e7956ffe6> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#evidenceSourceType> \"genomics_england\"^^<http://www.w3.org/2001/XMLSchema#string> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "The source disease label associated with the APP evidence is recorded literally here. Candidate interpretation requiring review.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/e10a18e680a100ce9ab8dea84d460991ae41e86378a939068732300c8a7a8ec7",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/ed6dfb77e60621587045037175e0c6bfe61e86e6f650a09b9eb0a1ae384379ac> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#sourceLabel> \"Alzheimer disease 1, familial\"^^<http://www.w3.org/2001/XMLSchema#string> ."
    }
  ],
  "unanswered": [
    "Whether APP has any connection to nct00594737 outside the supplied records."
  ]
}
```

</details>

### Local verification — automated, not owner scoring

Grounded and verified prose are identical. Submitted assertions: 5; accepted: 5; rejected: 0.

| Claim | Automated outcome | Reasons |
|---|---|---|
| G1 / V1 | RDF-ASSERTION-SUPPORTED | None |
| G2 / V2 | RDF-ASSERTION-SUPPORTED | None |
| G3 / V3 | RDF-ASSERTION-SUPPORTED | None |
| G4 / V4 | RDF-ASSERTION-SUPPORTED | None |
| G5 / V5 | RDF-ASSERTION-SUPPORTED | None |

Model-only is unverified; it has no structured claims in this recorded run. Its prose still requires review.

### Frozen required facts

| Fact ID | Exact frozen requirement |
|---|---|
| M7-04-F1 | The GRIN1 and GRIN3B clinical occurrences share nct00594737. |
| M7-04-F2 | The selected APP occurrence is genomics_england and cites PMIDs 22503161, 23028126 and 2111584, rather than representing a third clinical report. |

### Frozen expected behavior and qualifications

**Expected disposition:** mixed

Supported record facts may be reported with the listed boundaries; absent or out-of-scope evidence cannot license the prohibited conclusions.

- Absence of an APP Study link in the bounded RDF is not proof APP never appears in that study or any trial.
- Panel 474 is captured source-only context if discussed; it is not a ClinicalTrials Study node and is outside an RDF-only packet answer.

### Frozen unsupported claims to penalize

- Three independent studies inferred from three genes
- Complete negative APP study-membership assertion

### Frozen scoring criteria — verbatim

```json
{
  "scoringDimensions": [
    "source-relative assertion support",
    "human prose support/unsupported/contradicted/unresolved labels",
    "required-fact completion",
    "relevance",
    "provenance accuracy",
    "qualification and bounded abstention",
    "retrieval coverage",
    "failure/usage/cost"
  ],
  "scoringRequirements": {
    "excessiveAbstention": "Flag withholding supported required facts unnecessarily.",
    "proseLabels": "Sole human reviewer assigns supported/unsupported/contradicted/unresolved against frozen evidence; no clinical truth claim.",
    "qualificationPass": "All listed acceptable qualifications relevant to the response must be respected; no listed forbidden claim may be asserted.",
    "requiredAbstention": null,
    "requiredFactCompletion": "Each listed fact ID counted once only when correctly conveyed with source scope; all items have a nonzero required-fact denominator. Failures score zero completion.",
    "sharedGeneration": "Identical grounded/verified prose receives identical human prose scoring; retained assertion surfaces scored separately."
  }
}
```

<details><summary>Frozen retrieval scope and source references</summary>

```json
{
  "retrievalScope": {
    "maxPacketBytes": 196608,
    "mode": "hybrid",
    "records": 8,
    "rootIds": [
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/DerivedStatement/fd3db67ec6a05fdaa22d8c1407740e44cdbfc775cc25b2239bdfbd15268bd611",
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/9bb44911596e3db2ef337067480b7d127897e4c5c7918e8f2ac31bb4d803c66b",
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/bad88e8b10862169dcb3022359308caa2c0da43953e03fdcadaef53999bfcc7b",
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/e10a18e680a100ce9ab8dea84d460991ae41e86378a939068732300c8a7a8ec7"
    ],
    "status": "FROZEN"
  },
  "sourceReferences": [
    "manifests/dementia-development-001.json",
    "kg/mondo-pilot-001/records.ttl",
    "kg/mondo-pilot-001/provenance.ttl",
    "kg/ot2606-evidence-001/records.ttl",
    "kg/ot2606-evidence-001/provenance.ttl",
    "kg/ot2606-context-001/records.ttl"
  ]
}
```

</details>

### Owner scoring — recorded under the supplied review instructions

**A. Source-relative prose labels** (S supported / U unsupported / C contradicted / R unresolved). All factual surfaces are considered. Exact copied propositions are counted once; surface membership is retained. Nonfactual disclaimers and questions are excluded.

| Condition / surfaces | Exact proposition | Label | Basis |
|---|---|---|---|
| M / answer_text | I can’t determine whether GRIN1, GRIN3B and APP point to the same study or report from the information provided. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| M / answer_text | No study identifiers, reports or source records were supplied, so I can’t verify whether two share a source or where the third gene’s evidence comes from. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | GRIN1 and GRIN3B point to the same reported study, nct00594737, in two Open Targets clinical_precedence records. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | APP’s supplied evidence comes instead from an Open Targets genomics_england record concerning “Alzheimer disease 1, familial”; | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | it is not presented here as a clinical report for that study. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | This is a comparison of the supplied records, not an assessment of biological relationships or study outcomes. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-1-explanation | The GRIN1-linked occurrence refers to the shared study. | U | Occurrence-specific GRIN1/GRIN3B name assignment in explanation requires identity reconciliation: supplied occurrence target links use Ensembl identifiers and do not themselves label gene symbols. Do not infer correctness from accepted refersToStudy triple. Owner shared-study conclusion and fact decisions remain unchanged. |
| G/V / claim-2-explanation | The GRIN3B-linked occurrence refers to that same study. | U | Occurrence-specific GRIN1/GRIN3B name assignment in explanation requires identity reconciliation: supplied occurrence target links use Ensembl identifiers and do not themselves label gene symbols. Do not infer correctness from accepted refersToStudy triple. Owner shared-study conclusion and fact decisions remain unchanged. |
| G/V / claim-3-explanation | The shared study has this recorded identifier. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-4-explanation | APP’s supplied occurrence is classified as genomics_england evidence. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-5-explanation | The source disease label associated with the APP evidence is recorded literally here. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |

Excluded nonfactual material is retained with reasons in the machine-readable review; original answers above remain untouched.

**B. Strict required-fact completion — owner decisions**

| Fact ID | M | G | V |
|---|---|---|---|
| M7-04-F1 | N | Y | Y |
| M7-04-F2 | N | N | N |

**C. Retained assertion judgments** — statement support, question relevance and citation/source provenance; not a completeness score. Model-only has no retained assertions; precision is undefined.

| Assertion | Support | Relevant? | Provenance correct? | Reason |
|---|---|---|---|---|
| G1 / V1 | S | Y | Y | First clinical occurrence study link; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G2 / V2 | S | Y | Y | Second clinical occurrence study link; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G3 / V3 | S | Y | Y | Shared study identifier; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G4 / V4 | S | Y | Y | APP source type distinct from clinical occurrences; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G5 / V5 | S | Y | Y | APP source disease context; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |

**D. Qualification and abstention** — applied from frozen rules and owner observations.

| Condition | Qualification | Required abstention | Excessive abstention |
|---|---|---|---|
| M | Y | Not applicable | N |
| G | Y | Not applicable | N |
| V | Y | Not applicable | N |

Grounded respects the frozen source boundaries despite any detail omissions. Model-only Q08/Q10/Q12 fails corpus-only qualification because the owner identifies clinical/treatment scope leakage; other model-only scope qualifications are respected.

Q01–06: no unnecessary withholding is inferred. Model-only lacks corpus access intentionally; grounded detail omissions are not automatically excessive abstention.

**E. Retrieval coverage — separate from output completion**

Frozen supplied G/V packets contain the reference witnesses for: M7-04-F1, M7-04-F2. Missing fact witness sets: none. Exact statement witnesses and request hash are recorded in `owner-review-scores.json`. A prose omission does not remove evidence from these packets. Model-only retrieval coverage: not applicable, intentionally no retrieval.

**F. Owner comments — supplied observations**

- Model-only cleanly abstained because study/source records were not supplied.
- Grounded correctly identified GRIN1 and GRIN3B as sharing nct00594737 and APP as genomics_england evidence.
- It omitted the three required APP PMIDs.
- Classification: grounded source/citation-detail completeness gap.
- Main answer was correct.

**Residual annotation note:** The occurrence-specific target names in two M7-04 claim explanations are marked R, separate from the correct shared-study conclusion; no answer was repaired.

## M7-05

<!-- BEGIN M7-05 QUESTION -->
What indication and development stage does the graph record for gosuranemab?
<!-- END M7-05 QUESTION -->

### Model-only answer — unchanged

<!-- BEGIN M7-05 MODEL-ONLY ANSWER -->
````text
I can’t determine what indication and development stage the graph records for gosuranemab because no graph data was supplied. From general knowledge, gosuranemab was studied in phase 2 trials for progressive supranuclear palsy and Alzheimer’s disease, but that does not establish the graph’s entry. This is an unverified development control, not clinical advice.
````
<!-- END M7-05 MODEL-ONLY ANSWER -->

<details><summary>Complete structured claims and unanswered fields — unchanged values</summary>

```json
{
  "claims": [],
  "unanswered": [
    "Which indication and development stage are recorded in the graph for gosuranemab?"
  ]
}
```

</details>

### KG-grounded answer — unchanged

<!-- BEGIN M7-05 KG-GROUNDED ANSWER -->
````text
The graph records gosuranemab’s indication as MONDO_0017276 and its maximum indication stage as PHASE_1. The original condition label is not supplied, so the indication cannot be named from these packets. This is a candidate interpretation of source records, not a clinical efficacy conclusion.
````
<!-- END M7-05 KG-GROUNDED ANSWER -->

<details><summary>Complete structured claims and unanswered fields — unchanged values</summary>

```json
{
  "claims": [
    {
      "claim_type": "source_assertion",
      "explanation": "The clinical indication record links to this disease reference; the reference gives the indication identifier. Its limitation text says the original condition label is absent.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/ClinicalIndicationRecord/ea2d65dcef2e7e8b4e9ee8aafd5a521c804b67b40862850878061133a1a1d3c6",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/0c038db53a8a2bf551c9132876e6809475e576353f8220ef6aaf38eee63e76ab> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#externalIdentifier> \"MONDO_0017276\"^^<http://www.w3.org/2001/XMLSchema#string> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "The record reports PHASE_1 as its source maximum indication stage, not as evidence of efficacy or current trial status.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/ClinicalIndicationRecord/ea2d65dcef2e7e8b4e9ee8aafd5a521c804b67b40862850878061133a1a1d3c6",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/ClinicalIndicationRecord/ea2d65dcef2e7e8b4e9ee8aafd5a521c804b67b40862850878061133a1a1d3c6> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#trialPhaseText> \"PHASE_1\"^^<http://www.w3.org/2001/XMLSchema#string> ."
    }
  ],
  "unanswered": [
    "The original condition label for MONDO_0017276 is not supplied."
  ]
}
```

</details>

### Local verification — automated, not owner scoring

Grounded and verified prose are identical. Submitted assertions: 2; accepted: 2; rejected: 0.

| Claim | Automated outcome | Reasons |
|---|---|---|
| G1 / V1 | RDF-ASSERTION-SUPPORTED | None |
| G2 / V2 | RDF-ASSERTION-SUPPORTED | None |

Model-only is unverified; it has no structured claims in this recorded run. Its prose still requires review.

### Frozen required facts

| Fact ID | Exact frozen requirement |
|---|---|
| M7-05-F1 | CHEMBL3990042 indication c680c47a8cc2571635e1d5c629e51834273a3e67d25ebedfa9e58b729ad65189 connects to MONDO_0017276 with trialPhaseText PHASE_1. |

### Frozen expected behavior and qualifications

**Expected disposition:** answer

Supported record facts may be reported with the listed boundaries; absent or out-of-scope evidence cannot license the prohibited conclusions.

- This is the source maximum indication stage, not primary registry status, population or efficacy.

### Frozen unsupported claims to penalize

- All-FTD benefit
- Trial completed/successful or safe because PHASE_1

### Frozen scoring criteria — verbatim

```json
{
  "scoringDimensions": [
    "source-relative assertion support",
    "human prose support/unsupported/contradicted/unresolved labels",
    "required-fact completion",
    "relevance",
    "provenance accuracy",
    "qualification and bounded abstention",
    "retrieval coverage",
    "failure/usage/cost"
  ],
  "scoringRequirements": {
    "excessiveAbstention": "Flag withholding supported required facts unnecessarily.",
    "proseLabels": "Sole human reviewer assigns supported/unsupported/contradicted/unresolved against frozen evidence; no clinical truth claim.",
    "qualificationPass": "All listed acceptable qualifications relevant to the response must be respected; no listed forbidden claim may be asserted.",
    "requiredAbstention": null,
    "requiredFactCompletion": "Each listed fact ID counted once only when correctly conveyed with source scope; all items have a nonzero required-fact denominator. Failures score zero completion.",
    "sharedGeneration": "Identical grounded/verified prose receives identical human prose scoring; retained assertion surfaces scored separately."
  }
}
```

<details><summary>Frozen retrieval scope and source references</summary>

```json
{
  "retrievalScope": {
    "maxPacketBytes": 196608,
    "mode": "hybrid",
    "records": 8,
    "rootIds": [
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/ClinicalIndicationRecord/ea2d65dcef2e7e8b4e9ee8aafd5a521c804b67b40862850878061133a1a1d3c6",
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/ee143c3db4c0dc5573dcafd8e6861a114e3f87a9b5718de04dec6a60023874d9"
    ],
    "status": "FROZEN"
  },
  "sourceReferences": [
    "manifests/dementia-development-001.json",
    "kg/mondo-pilot-001/records.ttl",
    "kg/mondo-pilot-001/provenance.ttl",
    "kg/ot2606-evidence-001/records.ttl",
    "kg/ot2606-evidence-001/provenance.ttl",
    "kg/ot2606-context-001/records.ttl"
  ]
}
```

</details>

### Owner scoring — recorded under the supplied review instructions

**A. Source-relative prose labels** (S supported / U unsupported / C contradicted / R unresolved). All factual surfaces are considered. Exact copied propositions are counted once; surface membership is retained. Nonfactual disclaimers and questions are excluded.

| Condition / surfaces | Exact proposition | Label | Basis |
|---|---|---|---|
| M / answer_text | I can’t determine what indication and development stage the graph records for gosuranemab because no graph data was supplied. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| M / answer_text | From general knowledge, gosuranemab was studied in phase 2 trials for progressive supranuclear palsy and Alzheimer’s disease, | U | Outside biomedical assertion not established by frozen project evidence. U is source-relative, not a real-world falsity judgment. Owner explicitly notes it is fenced off from corpus claims; not automatically a major failure. |
| M / answer_text | but that does not establish the graph’s entry. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | The graph records gosuranemab’s indication as MONDO_0017276 and its maximum indication stage as PHASE_1. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | The original condition label is not supplied, so the indication cannot be named from these packets. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-1-explanation | The clinical indication record links to this disease reference; | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-1-explanation | the reference gives the indication identifier. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-1-explanation | Its limitation text says the original condition label is absent. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-2-explanation | The record reports PHASE_1 as its source maximum indication stage, not as evidence of efficacy or current trial status. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / unanswered-1 | The original condition label for MONDO_0017276 is not supplied. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |

Excluded nonfactual material is retained with reasons in the machine-readable review; original answers above remain untouched.

**B. Strict required-fact completion — owner decisions**

| Fact ID | M | G | V |
|---|---|---|---|
| M7-05-F1 | N | Y | Y |

**C. Retained assertion judgments** — statement support, question relevance and citation/source provenance; not a completeness score. Model-only has no retained assertions; precision is undefined.

| Assertion | Support | Relevant? | Provenance correct? | Reason |
|---|---|---|---|---|
| G1 / V1 | S | Y | Y | Indication disease identifier; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G2 / V2 | S | Y | Y | Source maximum indication stage; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |

**D. Qualification and abstention** — applied from frozen rules and owner observations.

| Condition | Qualification | Required abstention | Excessive abstention |
|---|---|---|---|
| M | Y | Not applicable | N |
| G | Y | Not applicable | N |
| V | Y | Not applicable | N |

Grounded respects the frozen source boundaries despite any detail omissions. Model-only Q08/Q10/Q12 fails corpus-only qualification because the owner identifies clinical/treatment scope leakage; other model-only scope qualifications are respected.

Q01–06: no unnecessary withholding is inferred. Model-only lacks corpus access intentionally; grounded detail omissions are not automatically excessive abstention.

**E. Retrieval coverage — separate from output completion**

Frozen supplied G/V packets contain the reference witnesses for: M7-05-F1. Missing fact witness sets: none. Exact statement witnesses and request hash are recorded in `owner-review-scores.json`. A prose omission does not remove evidence from these packets. Model-only retrieval coverage: not applicable, intentionally no retrieval.

**F. Owner comments — supplied observations**

- Model-only had no corpus access and introduced general knowledge about gosuranemab Phase 2 studies, explicitly noting that this did not establish the graph entry.
- Grounded correctly returned MONDO_0017276 and source maximum PHASE_1 with proper limitations.
- No important grounded completeness issue.
- Classification: grounded worked as intended.
- Interesting baseline contrast: outside model knowledge and corpus-specific recorded stage differ, showing why grounding is necessary.

**Residual annotation note:** No outside biomedical knowledge was used to resolve labels.

## M7-06

<!-- BEGIN M7-06 QUESTION -->
How does Alzheimer disease type 1 connect to Alzheimer disease through the recorded disease hierarchy?
<!-- END M7-06 QUESTION -->

### Model-only answer — unchanged

<!-- BEGIN M7-06 MODEL-ONLY ANSWER -->
````text
Alzheimer disease type 1 is generally treated as a specific form of Alzheimer disease, so the likely hierarchy is “Alzheimer disease type 1 → Alzheimer disease.” No recorded disease hierarchy was supplied, so the exact recorded relationship cannot be verified. This is an unverified development control, not clinical advice.
````
<!-- END M7-06 MODEL-ONLY ANSWER -->

<details><summary>Complete structured claims and unanswered fields — unchanged values</summary>

```json
{
  "claims": [],
  "unanswered": [
    "What exact parent–child relationship does the recorded disease hierarchy specify?"
  ]
}
```

</details>

### KG-grounded answer — unchanged

<!-- BEGIN M7-06 KG-GROUNDED ANSWER -->
````text
The recorded parent-navigation path is Alzheimer disease type 1 (MONDO:0007088) → early-onset autosomal dominant Alzheimer disease (MONDO:0015140) → familial Alzheimer disease (MONDO:0100087) → Alzheimer disease (MONDO:0004975). Each arrow represents a source-reported immediate parent step, not a separately verified biological relationship.
````
<!-- END M7-06 KG-GROUNDED ANSWER -->

<details><summary>Complete structured claims and unanswered fields — unchanged values</summary>

```json
{
  "claims": [
    {
      "claim_type": "source_assertion",
      "explanation": "Candidate interpretation requiring review: this records the immediate parent of Alzheimer disease type 1 as early-onset autosomal dominant Alzheimer disease.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/HierarchyStep/9dbc4821c39c5ceb692fc73095131c200359c653dfc6ce0a0b355fadb756b8f8",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/HierarchyStep/9dbc4821c39c5ceb692fc73095131c200359c653dfc6ce0a0b355fadb756b8f8> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#parentReference> <https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/bcd3ca8a4dfbf567bb35be1b516ad2278c40cc18254bcb2e6cd4cf75870edd80> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "Candidate interpretation requiring review: this records familial Alzheimer disease as the next immediate parent.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/HierarchyStep/677460eea8f681aaa0de334dc1973cfea6d9552515da4d0d8aab9a6c94ec73a3",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/HierarchyStep/677460eea8f681aaa0de334dc1973cfea6d9552515da4d0d8aab9a6c94ec73a3> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#parentReference> <https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/8f1c74a3739d161dc1d7e3ec70e5de9d2ca810daf052041b5e2d6695d0c5168e> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "Candidate interpretation requiring review: this records Alzheimer disease as the immediate parent of familial Alzheimer disease.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/HierarchyStep/e63bdc528cafa7ca08d8e902f71f4de3f96f826e5d4053778898020df9cc3850",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/HierarchyStep/e63bdc528cafa7ca08d8e902f71f4de3f96f826e5d4053778898020df9cc3850> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#parentReference> <https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/56e84bf4b4a25940c7a39128c743710b469a768016bee72e1e1f922fc4cff8db> ."
    }
  ],
  "unanswered": []
}
```

</details>

### Local verification — automated, not owner scoring

Grounded and verified prose are identical. Submitted assertions: 3; accepted: 3; rejected: 0.

| Claim | Automated outcome | Reasons |
|---|---|---|
| G1 / V1 | RDF-ASSERTION-SUPPORTED | None |
| G2 / V2 | RDF-ASSERTION-SUPPORTED | None |
| G3 / V3 | RDF-ASSERTION-SUPPORTED | None |

Model-only is unverified; it has no structured claims in this recorded run. Its prose still requires review.

### Frozen required facts

| Fact ID | Exact frozen requirement |
|---|---|
| M7-06-F1 | MONDO:0007088 → MONDO:0015140 → MONDO:0100087 → MONDO:0004975 using three explicit HierarchySteps. |

### Frozen expected behavior and qualifications

**Expected disposition:** answer

Supported record facts may be reported with the listed boundaries; absent or out-of-scope evidence cannot license the prohibited conclusions.

- Source-scoped endpoint references remain separate; this is a reconstructed recorded path, not equivalence, causal inference or full hierarchy closure.

### Frozen unsupported claims to penalize

- A generic dementia parent above AD
- Direct equality among the four concepts

### Frozen scoring criteria — verbatim

```json
{
  "scoringDimensions": [
    "source-relative assertion support",
    "human prose support/unsupported/contradicted/unresolved labels",
    "required-fact completion",
    "relevance",
    "provenance accuracy",
    "qualification and bounded abstention",
    "retrieval coverage",
    "failure/usage/cost"
  ],
  "scoringRequirements": {
    "excessiveAbstention": "Flag withholding supported required facts unnecessarily.",
    "proseLabels": "Sole human reviewer assigns supported/unsupported/contradicted/unresolved against frozen evidence; no clinical truth claim.",
    "qualificationPass": "All listed acceptable qualifications relevant to the response must be respected; no listed forbidden claim may be asserted.",
    "requiredAbstention": null,
    "requiredFactCompletion": "Each listed fact ID counted once only when correctly conveyed with source scope; all items have a nonzero required-fact denominator. Failures score zero completion.",
    "sharedGeneration": "Identical grounded/verified prose receives identical human prose scoring; retained assertion surfaces scored separately."
  }
}
```

<details><summary>Frozen retrieval scope and source references</summary>

```json
{
  "retrievalScope": {
    "maxPacketBytes": 196608,
    "mode": "hybrid",
    "records": 8,
    "rootIds": [
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/HierarchyStep/677460eea8f681aaa0de334dc1973cfea6d9552515da4d0d8aab9a6c94ec73a3",
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/HierarchyStep/9dbc4821c39c5ceb692fc73095131c200359c653dfc6ce0a0b355fadb756b8f8",
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/HierarchyStep/e63bdc528cafa7ca08d8e902f71f4de3f96f826e5d4053778898020df9cc3850"
    ],
    "status": "FROZEN"
  },
  "sourceReferences": [
    "manifests/dementia-development-001.json",
    "kg/mondo-pilot-001/records.ttl",
    "kg/mondo-pilot-001/provenance.ttl",
    "kg/ot2606-evidence-001/records.ttl",
    "kg/ot2606-evidence-001/provenance.ttl",
    "kg/ot2606-context-001/records.ttl"
  ]
}
```

</details>

### Owner scoring — recorded under the supplied review instructions

**A. Source-relative prose labels** (S supported / U unsupported / C contradicted / R unresolved). All factual surfaces are considered. Exact copied propositions are counted once; surface membership is retained. Nonfactual disclaimers and questions are excluded.

| Condition / surfaces | Exact proposition | Label | Basis |
|---|---|---|---|
| M / answer_text | Alzheimer disease type 1 is generally treated as a specific form of Alzheimer disease, so the likely hierarchy is “Alzheimer disease type 1 → Alzheimer disease.” | U | Likely simplified path is not established as the exact recorded hierarchy; no direct-parent relation or equality is inferred. |
| M / answer_text | No recorded disease hierarchy was supplied, so the exact recorded relationship cannot be verified. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | The recorded parent-navigation path is Alzheimer disease type 1 (MONDO:0007088) → early-onset autosomal dominant Alzheimer disease (MONDO:0015140) → familial Alzheimer disease (MONDO:0100087) → Alzheimer disease (MONDO:0004975). | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | Each arrow represents a source-reported immediate parent step, not a separately verified biological relationship. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-1-explanation | Candidate interpretation requiring review: this records the immediate parent of Alzheimer disease type 1 as early-onset autosomal dominant Alzheimer disease. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-2-explanation | Candidate interpretation requiring review: this records familial Alzheimer disease as the next immediate parent. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-3-explanation | Candidate interpretation requiring review: this records Alzheimer disease as the immediate parent of familial Alzheimer disease. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |

Excluded nonfactual material is retained with reasons in the machine-readable review; original answers above remain untouched.

**B. Strict required-fact completion — owner decisions**

| Fact ID | M | G | V |
|---|---|---|---|
| M7-06-F1 | N | Y | Y |

**C. Retained assertion judgments** — statement support, question relevance and citation/source provenance; not a completeness score. Model-only has no retained assertions; precision is undefined.

| Assertion | Support | Relevant? | Provenance correct? | Reason |
|---|---|---|---|---|
| G1 / V1 | S | Y | Y | First immediate-parent step; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G2 / V2 | S | Y | Y | Second immediate-parent step; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G3 / V3 | S | Y | Y | Third immediate-parent step; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |

**D. Qualification and abstention** — applied from frozen rules and owner observations.

| Condition | Qualification | Required abstention | Excessive abstention |
|---|---|---|---|
| M | Y | Not applicable | N |
| G | Y | Not applicable | N |
| V | Y | Not applicable | N |

Grounded respects the frozen source boundaries despite any detail omissions. Model-only Q08/Q10/Q12 fails corpus-only qualification because the owner identifies clinical/treatment scope leakage; other model-only scope qualifications are respected.

Q01–06: no unnecessary withholding is inferred. Model-only lacks corpus access intentionally; grounded detail omissions are not automatically excessive abstention.

**E. Retrieval coverage — separate from output completion**

Frozen supplied G/V packets contain the reference witnesses for: M7-06-F1. Missing fact witness sets: none. Exact statement witnesses and request hash are recorded in `owner-review-scores.json`. A prose omission does not remove evidence from these packets. Model-only retrieval coverage: not applicable, intentionally no retrieval.

**F. Owner comments — supplied observations**

- Model-only used general knowledge to simplify/guess “Alzheimer disease type 1 → Alzheimer disease”, but explicitly admitted it could not verify the recorded hierarchy.
- Grounded returned the exact three-step recorded MONDO path.
- No grounded corpus fact was missed.
- Classification: grounded worked as intended.
- Do NOT describe model-only incompleteness here as a retrieval failure; it had no retrieval by design.

**Residual annotation note:** No outside biomedical knowledge was used to resolve labels.

## M7-07

<!-- BEGIN M7-07 QUESTION -->
Does the graph show that MAPT causes any of the diseases connected to it, or does it only show that source evidence connects them?
<!-- END M7-07 QUESTION -->

### Model-only answer — unchanged

<!-- BEGIN M7-07 MODEL-ONLY ANSWER -->
````text
No graph or source evidence was supplied, so I cannot verify what its edges show. In general, a connection between MAPT and a disease indicates an asserted association supported by a source, not necessarily that MAPT causes the disease. Establishing causation would require evidence beyond the connection itself. This is an unverified development control, not clinical advice.
````
<!-- END M7-07 MODEL-ONLY ANSWER -->

<details><summary>Complete structured claims and unanswered fields — unchanged values</summary>

```json
{
  "claims": [],
  "unanswered": [
    "What do the graph's MAPT–disease edges represent, and what evidence supports each one?"
  ]
}
```

</details>

### KG-grounded answer — unchanged

<!-- BEGIN M7-07 KG-GROUNDED ANSWER -->
````text
The supplied graph records a disease–target association derived from a source evidence occurrence; it does not establish that MAPT causes the disease. The retrieved target is identified by an Ensembl ID, but these packets do not explicitly identify it as MAPT. This is a candidate interpretation of the records, not a reviewed biomedical conclusion.
````
<!-- END M7-07 KG-GROUNDED ANSWER -->

<details><summary>Complete structured claims and unanswered fields — unchanged values</summary>

```json
{
  "claims": [
    {
      "claim_type": "source_assertion",
      "explanation": "The association is recorded as derived from an evidence occurrence, rather than as a causal finding.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseTargetAssociation/7d73780492305001e5f0303ee2ab6c857629dc81e283452083ef5534f8746916",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseTargetAssociation/7d73780492305001e5f0303ee2ab6c857629dc81e283452083ef5534f8746916> <http://www.w3.org/ns/prov#wasDerivedFrom> <https://github.com/subramanyaprasad21/dementia-kg-ai/id/EvidenceOccurrence/d8f5377a0c8887099512b7eed0c27dd998fc10147accc8836bdcbe58ddc56fcc> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "The association points to a disease reference; this link alone does not state biological causality.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseTargetAssociation/7d73780492305001e5f0303ee2ab6c857629dc81e283452083ef5534f8746916",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseTargetAssociation/7d73780492305001e5f0303ee2ab6c857629dc81e283452083ef5534f8746916> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#hasDiseaseReference> <https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/57596fecb3d57365d5bf9a12d4f7dfa64a6956aaf93e55ff57babf878f62500f> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "The association points to a target; this link alone does not state biological causality.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseTargetAssociation/7d73780492305001e5f0303ee2ab6c857629dc81e283452083ef5534f8746916",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseTargetAssociation/7d73780492305001e5f0303ee2ab6c857629dc81e283452083ef5534f8746916> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#hasTarget> <https://github.com/subramanyaprasad21/dementia-kg-ai/id/Target/ae58b26a9aed98f23b8c6143838acfd6c478a272fba179d3cd45f9b3c8df5962> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "The retrieved identifier for that target is an Ensembl ID; the packet does not supply a MAPT label.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseTargetAssociation/7d73780492305001e5f0303ee2ab6c857629dc81e283452083ef5534f8746916",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/Target/ae58b26a9aed98f23b8c6143838acfd6c478a272fba179d3cd45f9b3c8df5962> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#externalIdentifier> \"ENSG00000186868\"^^<http://www.w3.org/2001/XMLSchema#string> ."
    }
  ],
  "unanswered": [
    "Whether the retrieved target identifier denotes MAPT, based on an explicit identity statement in the supplied packets.",
    "Whether MAPT biologically causes any connected disease."
  ]
}
```

</details>

### Local verification — automated, not owner scoring

Grounded and verified prose are identical. Submitted assertions: 4; accepted: 4; rejected: 0.

| Claim | Automated outcome | Reasons |
|---|---|---|
| G1 / V1 | RDF-ASSERTION-SUPPORTED | None |
| G2 / V2 | RDF-ASSERTION-SUPPORTED | None |
| G3 / V3 | RDF-ASSERTION-SUPPORTED | None |
| G4 / V4 | RDF-ASSERTION-SUPPORTED | None |

Model-only is unverified; it has no structured claims in this recorded run. Its prose still requires review.

### Frozen required facts

| Fact ID | Exact frozen requirement |
|---|---|
| M7-07-F1 | The two MAPT source occurrences retain original Pick and OMIM:600274 context with destinations FTD and semantic dementia; a bounded exact-FTD project grouping is represented. |
| M7-07-F2 | The RDF records source associations/assignments, not a causation assertion. |

### Frozen expected behavior and qualifications

**Expected disposition:** qualify

Supported record facts may be reported with the listed boundaries; absent or out-of-scope evidence cannot license the prohibited conclusions.

- No causal conclusion from these records; do not claim MAPT can never be causal in medicine.

### Frozen unsupported claims to penalize

- MAPT causes all connected diseases
- Biological non-causation inferred from an absent edge

### Frozen scoring criteria — verbatim

```json
{
  "scoringDimensions": [
    "source-relative assertion support",
    "human prose support/unsupported/contradicted/unresolved labels",
    "required-fact completion",
    "relevance",
    "provenance accuracy",
    "qualification and bounded abstention",
    "retrieval coverage",
    "failure/usage/cost"
  ],
  "scoringRequirements": {
    "excessiveAbstention": null,
    "proseLabels": "Sole human reviewer assigns supported/unsupported/contradicted/unresolved against frozen evidence; no clinical truth claim.",
    "qualificationPass": "All listed acceptable qualifications relevant to the response must be respected; no listed forbidden claim may be asserted.",
    "requiredAbstention": "Withhold all listed forbidden claims explicitly with a source-scoped explanation; retain useful required facts. Generic refusal or API failure is not success.",
    "requiredFactCompletion": "Each listed fact ID counted once only when correctly conveyed with source scope; all items have a nonzero required-fact denominator. Failures score zero completion.",
    "sharedGeneration": "Identical grounded/verified prose receives identical human prose scoring; retained assertion surfaces scored separately."
  }
}
```

<details><summary>Frozen retrieval scope and source references</summary>

```json
{
  "retrievalScope": {
    "maxPacketBytes": 196608,
    "mode": "hybrid",
    "records": 8,
    "rootIds": [
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseTargetAssociation/7d73780492305001e5f0303ee2ab6c857629dc81e283452083ef5534f8746916",
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/1753f8bb7477cc954771e836b45e64442352ba0682c2fdcb6786bc1d49c2d1c4",
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/866deefd7f3be073959ff3e76a759955e0ffb259fd7dfe9e32ce224700849bcc"
    ],
    "status": "FROZEN"
  },
  "sourceReferences": [
    "manifests/dementia-development-001.json",
    "kg/mondo-pilot-001/records.ttl",
    "kg/mondo-pilot-001/provenance.ttl",
    "kg/ot2606-evidence-001/records.ttl",
    "kg/ot2606-evidence-001/provenance.ttl",
    "kg/ot2606-context-001/records.ttl"
  ]
}
```

</details>

### Owner scoring — recorded under the supplied review instructions

**A. Source-relative prose labels** (S supported / U unsupported / C contradicted / R unresolved). All factual surfaces are considered. Exact copied propositions are counted once; surface membership is retained. Nonfactual disclaimers and questions are excluded.

| Condition / surfaces | Exact proposition | Label | Basis |
|---|---|---|---|
| M / answer_text | No graph or source evidence was supplied, so I cannot verify what its edges show. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| M / answer_text | In general, a connection between MAPT and a disease indicates an asserted association supported by a source, not necessarily that MAPT causes the disease. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| M / answer_text | Establishing causation would require evidence beyond the connection itself. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | The supplied graph records a disease–target association derived from a source evidence occurrence; | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | it does not establish that MAPT causes the disease. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | The retrieved target is identified by an Ensembl ID, but these packets do not explicitly identify it as MAPT. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-1-explanation | The association is recorded as derived from an evidence occurrence, rather than as a causal finding. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-2-explanation | The association points to a disease reference; | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-2-explanation, claim-3-explanation | this link alone does not state biological causality. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-3-explanation | The association points to a target; | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-4-explanation | The retrieved identifier for that target is an Ensembl ID; | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-4-explanation | the packet does not supply a MAPT label. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |

Excluded nonfactual material is retained with reasons in the machine-readable review; original answers above remain untouched.

**B. Strict required-fact completion — owner decisions**

| Fact ID | M | G | V |
|---|---|---|---|
| M7-07-F1 | N | N | N |
| M7-07-F2 | N | Y | Y |

**C. Retained assertion judgments** — statement support, question relevance and citation/source provenance; not a completeness score. Model-only has no retained assertions; precision is undefined.

| Assertion | Support | Relevant? | Provenance correct? | Reason |
|---|---|---|---|---|
| G1 / V1 | S | Y | Y | Source-derived association provenance; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G2 / V2 | S | Y | Y | Disease participant rather than causation; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G3 / V3 | S | Y | Y | Target participant rather than causation; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G4 / V4 | S | Y | Y | Target identifier for the scoped source association; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |

**D. Qualification and abstention** — applied from frozen rules and owner observations.

| Condition | Qualification | Required abstention | Excessive abstention |
|---|---|---|---|
| M | Y | N | Not applicable |
| G | Y | Y | Not applicable |
| V | Y | Y | Not applicable |

Grounded respects the frozen source boundaries despite any detail omissions. Model-only Q08/Q10/Q12 fails corpus-only qualification because the owner identifies clinical/treatment scope leakage; other model-only scope qualifications are respected.

For Q07–12 the strict frozen pass requires source-scoped explanation retaining useful required facts. Model-only general reasoning/no-access admissions are appropriate but do not pass that conjunctive source-specific criterion. Grounded supplies source-specific qualifications and useful details, even when a compound required fact is incomplete (Q10). This does not label model-only retrieval as failed.

**E. Retrieval coverage — separate from output completion**

Frozen supplied G/V packets contain the reference witnesses for: M7-07-F1, M7-07-F2. Missing fact witness sets: none. Exact statement witnesses and request hash are recorded in `owner-review-scores.json`. A prose omission does not remove evidence from these packets. Model-only retrieval coverage: not applicable, intentionally no retrieval.

**F. Owner comments — supplied observations**

- Model-only had no corpus access and used a general principle that association does not establish causation.
- Grounded correctly preserved the critical non-causation boundary.
- However, it omitted the detailed MAPT source-occurrence context required by F1.
- Classification: grounded source-context/evidence-completeness gap.
- Causal qualification itself was good.

**Residual annotation note:** No outside biomedical knowledge was used to resolve labels.

## M7-08

<!-- BEGIN M7-08 QUESTION -->
APP is connected to lecanemab's mechanism. Does that prove that lecanemab effectively treats Alzheimer's disease?
<!-- END M7-08 QUESTION -->

### Model-only answer — unchanged

<!-- BEGIN M7-08 MODEL-ONLY ANSWER -->
````text
No. APP is a precursor of amyloid-beta, and lecanemab targets aggregated amyloid-beta. That mechanistic connection does not, by itself, prove clinical benefit. Clinical efficacy must be evaluated in trials measuring outcomes in people with Alzheimer's disease. Based on model knowledge, a trial in early Alzheimer's disease reported a modest slowing of decline, alongside risks including amyloid-related imaging abnormalities; I cannot verify the evidence or its applicability here because no sources were supplied. This is an unverified development control, not clinical advice.
````
<!-- END M7-08 MODEL-ONLY ANSWER -->

<details><summary>Complete structured claims and unanswered fields — unchanged values</summary>

```json
{
  "claims": [],
  "unanswered": [
    "Which specific clinical evidence and patient population should be assessed?",
    "How should benefits and risks be weighed for the intended use?"
  ]
}
```

</details>

### KG-grounded answer — unchanged

<!-- BEGIN M7-08 KG-GROUNDED ANSWER -->
````text
No. The retrieved mechanism record reports a target-related description, but that does not prove lecanemab effectively treats Alzheimer’s disease. The clinical-indication record reports an approval-stage label, not treatment outcomes. Efficacy cannot be determined from these packets.
````
<!-- END M7-08 KG-GROUNDED ANSWER -->

<details><summary>Complete structured claims and unanswered fields — unchanged values</summary>

```json
{
  "claims": [
    {
      "claim_type": "source_assertion",
      "explanation": "The mechanism record's source description; its clinical interpretation requires review.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/a413f6671dc36fa70a1079361b6b4236fb96a9e594c1785b40f8ee445869f6fb",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/a413f6671dc36fa70a1079361b6b4236fb96a9e594c1785b40f8ee445869f6fb> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#sourceText> \"Amyloid-beta A4 protein inhibitor\"^^<http://www.w3.org/2001/XMLSchema#string> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "The record explicitly limits what can be inferred from its mechanism description.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/a413f6671dc36fa70a1079361b6b4236fb96a9e594c1785b40f8ee445869f6fb",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/a413f6671dc36fa70a1079361b6b4236fb96a9e594c1785b40f8ee445869f6fb> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#limitationText> \"Source gene-indexed mechanism; shared original row and molecular target context retained. No efficacy, gene-wide action or independent confirmation inferred.\"^^<http://www.w3.org/2001/XMLSchema#string> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "This is a source-reported stage label, not an efficacy result.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/ClinicalIndicationRecord/8d409cf761cbae391ba0ac03b3aee9046100d030f6779e9ecaad80c4cd11815b",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/ClinicalIndicationRecord/8d409cf761cbae391ba0ac03b3aee9046100d030f6779e9ecaad80c4cd11815b> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#trialPhaseText> \"APPROVAL\"^^<http://www.w3.org/2001/XMLSchema#string> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "The indication record states that efficacy information was not acquired.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/ClinicalIndicationRecord/8d409cf761cbae391ba0ac03b3aee9046100d030f6779e9ecaad80c4cd11815b",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/ClinicalIndicationRecord/8d409cf761cbae391ba0ac03b3aee9046100d030f6779e9ecaad80c4cd11815b> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#limitationText> \"Source maximum indication stage only. Report locators retained in the linked source description; registry population/status and efficacy not acquired.\"^^<http://www.w3.org/2001/XMLSchema#string> ."
    }
  ],
  "unanswered": [
    "Whether and to what extent lecanemab improves clinical outcomes in people with Alzheimer’s disease."
  ]
}
```

</details>

### Local verification — automated, not owner scoring

Grounded and verified prose are identical. Submitted assertions: 4; accepted: 4; rejected: 0.

| Claim | Automated outcome | Reasons |
|---|---|---|
| G1 / V1 | RDF-ASSERTION-SUPPORTED | None |
| G2 / V2 | RDF-ASSERTION-SUPPORTED | None |
| G3 / V3 | RDF-ASSERTION-SUPPORTED | None |
| G4 / V4 | RDF-ASSERTION-SUPPORTED | None |

Model-only is unverified; it has no structured claims in this recorded run. Its prose still requires review.

### Frozen required facts

| Fact ID | Exact frozen requirement |
|---|---|
| M7-08-F1 | CHEMBL3833321 mechanism is APP-indexed with source text Amyloid-beta A4 protein inhibitor; a separate AD indication carries source maximum APPROVAL. |
| M7-08-F2 | Neither record provides an independently adjudicated efficacy result in the accepted graph. |

### Frozen expected behavior and qualifications

**Expected disposition:** qualify

Supported record facts may be reported with the listed boundaries; absent or out-of-scope evidence cannot license the prohibited conclusions.

- Answer the logical sufficiency issue; do not deny any real-world efficacy or replace missing evidence with model knowledge.

### Frozen unsupported claims to penalize

- APP mechanism proves AD efficacy
- APP-wide inhibition or fresh regulatory validation

### Frozen scoring criteria — verbatim

```json
{
  "scoringDimensions": [
    "source-relative assertion support",
    "human prose support/unsupported/contradicted/unresolved labels",
    "required-fact completion",
    "relevance",
    "provenance accuracy",
    "qualification and bounded abstention",
    "retrieval coverage",
    "failure/usage/cost"
  ],
  "scoringRequirements": {
    "excessiveAbstention": null,
    "proseLabels": "Sole human reviewer assigns supported/unsupported/contradicted/unresolved against frozen evidence; no clinical truth claim.",
    "qualificationPass": "All listed acceptable qualifications relevant to the response must be respected; no listed forbidden claim may be asserted.",
    "requiredAbstention": "Withhold all listed forbidden claims explicitly with a source-scoped explanation; retain useful required facts. Generic refusal or API failure is not success.",
    "requiredFactCompletion": "Each listed fact ID counted once only when correctly conveyed with source scope; all items have a nonzero required-fact denominator. Failures score zero completion.",
    "sharedGeneration": "Identical grounded/verified prose receives identical human prose scoring; retained assertion surfaces scored separately."
  }
}
```

<details><summary>Frozen retrieval scope and source references</summary>

```json
{
  "retrievalScope": {
    "maxPacketBytes": 196608,
    "mode": "hybrid",
    "records": 8,
    "rootIds": [
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/ClinicalIndicationRecord/8d409cf761cbae391ba0ac03b3aee9046100d030f6779e9ecaad80c4cd11815b",
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/a413f6671dc36fa70a1079361b6b4236fb96a9e594c1785b40f8ee445869f6fb"
    ],
    "status": "FROZEN"
  },
  "sourceReferences": [
    "manifests/dementia-development-001.json",
    "kg/mondo-pilot-001/records.ttl",
    "kg/mondo-pilot-001/provenance.ttl",
    "kg/ot2606-evidence-001/records.ttl",
    "kg/ot2606-evidence-001/provenance.ttl",
    "kg/ot2606-context-001/records.ttl"
  ]
}
```

</details>

### Owner scoring — recorded under the supplied review instructions

**A. Source-relative prose labels** (S supported / U unsupported / C contradicted / R unresolved). All factual surfaces are considered. Exact copied propositions are counted once; surface membership is retained. Nonfactual disclaimers and questions are excluded.

| Condition / surfaces | Exact proposition | Label | Basis |
|---|---|---|---|
| M / answer_text | APP is a precursor of amyloid-beta, and lecanemab targets aggregated amyloid-beta. | U | Outside biomedical assertion not established by frozen project evidence. U is source-relative, not a real-world falsity judgment. Owner identifies stronger clinical/treatment scope leakage. |
| M / answer_text | That mechanistic connection does not, by itself, prove clinical benefit. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| M / answer_text | Clinical efficacy must be evaluated in trials measuring outcomes in people with Alzheimer's disease. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| M / answer_text | Based on model knowledge, a trial in early Alzheimer's disease reported a modest slowing of decline, alongside risks including amyloid-related imaging abnormalities; | U | Outside biomedical assertion not established by frozen project evidence. U is source-relative, not a real-world falsity judgment. Owner identifies stronger clinical/treatment scope leakage. |
| M / answer_text | I cannot verify the evidence or its applicability here because no sources were supplied. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | The retrieved mechanism record reports a target-related description, but that does not prove lecanemab effectively treats Alzheimer’s disease. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | The clinical-indication record reports an approval-stage label, not treatment outcomes. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | Efficacy cannot be determined from these packets. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-1-explanation | The mechanism record's source description; | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-1-explanation | its clinical interpretation requires review. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-2-explanation | The record explicitly limits what can be inferred from its mechanism description. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-3-explanation | This is a source-reported stage label, not an efficacy result. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-4-explanation | The indication record states that efficacy information was not acquired. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |

Excluded nonfactual material is retained with reasons in the machine-readable review; original answers above remain untouched.

**B. Strict required-fact completion — owner decisions**

| Fact ID | M | G | V |
|---|---|---|---|
| M7-08-F1 | N | N | N |
| M7-08-F2 | N | Y | Y |

**C. Retained assertion judgments** — statement support, question relevance and citation/source provenance; not a completeness score. Model-only has no retained assertions; precision is undefined.

| Assertion | Support | Relevant? | Provenance correct? | Reason |
|---|---|---|---|---|
| G1 / V1 | S | Y | Y | Source mechanism description; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G2 / V2 | S | Y | Y | Mechanism inference limitation; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G3 / V3 | S | Y | Y | Source maximum indication stage; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G4 / V4 | S | Y | Y | Indication efficacy/acquisition limitation; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |

**D. Qualification and abstention** — applied from frozen rules and owner observations.

| Condition | Qualification | Required abstention | Excessive abstention |
|---|---|---|---|
| M | N | N | Not applicable |
| G | Y | Y | Not applicable |
| V | Y | Y | Not applicable |

Grounded respects the frozen source boundaries despite any detail omissions. Model-only Q08/Q10/Q12 fails corpus-only qualification because the owner identifies clinical/treatment scope leakage; other model-only scope qualifications are respected.

For Q07–12 the strict frozen pass requires source-scoped explanation retaining useful required facts. Model-only general reasoning/no-access admissions are appropriate but do not pass that conjunctive source-specific criterion. Grounded supplies source-specific qualifications and useful details, even when a compound required fact is incomplete (Q10). This does not label model-only retrieval as failed.

**E. Retrieval coverage — separate from output completion**

Frozen supplied G/V packets contain the reference witnesses for: M7-08-F1, M7-08-F2. Missing fact witness sets: none. Exact statement witnesses and request hash are recorded in `owner-review-scores.json`. A prose omission does not remove evidence from these packets. Model-only retrieval coverage: not applicable, intentionally no retrieval.

**F. Owner comments — supplied observations**

- Model-only correctly said mechanism does not prove efficacy.
- But it then introduced outside clinical/model knowledge about trial outcomes and ARIA that was not supplied by the evaluation corpus.
- This is a meaningful model-only outside-knowledge/scope-leakage example.
- Grounded correctly refused to infer efficacy and stayed within the supplied packets.
- However, it omitted important available corpus details required by F1.
- Classification: TWO DISTINCT issues:
  1. model-only outside-clinical-knowledge leakage;
  2. grounded evidence-completeness omission.

**Residual annotation note:** No outside biomedical knowledge was used to resolve labels.

## M7-09

<!-- BEGIN M7-09 QUESTION -->
If two evidence records mention two different targets, can they automatically be treated as two independent confirmations?
<!-- END M7-09 QUESTION -->

### Model-only answer — unchanged

<!-- BEGIN M7-09 MODEL-ONLY ANSWER -->
````text
No. Different targets do not automatically make two evidence records independent confirmations. The records could share a dataset, experimental methods, authors, or an underlying source, and they may support different claims. Independence requires checking their provenance and what each record actually establishes. No records were supplied, so this cannot be assessed here. This is an unverified development control, not clinical advice.
````
<!-- END M7-09 MODEL-ONLY ANSWER -->

<details><summary>Complete structured claims and unanswered fields — unchanged values</summary>

```json
{
  "claims": [],
  "unanswered": [
    "What are the two records, their sources, and their underlying data and methods?",
    "Do the records support the same specific claim?"
  ]
}
```

</details>

### KG-grounded answer — unchanged

<!-- BEGIN M7-09 KG-GROUNDED ANSWER -->
````text
No. Different targets do not automatically make two evidence records independent confirmations. In this packet, the two records name different targets, but a comparison record reports that both source rows reference the same study, nct00594737. That is a reason to review their provenance rather than count them as independent confirmations.
````
<!-- END M7-09 KG-GROUNDED ANSWER -->

<details><summary>Complete structured claims and unanswered fields — unchanged values</summary>

```json
{
  "claims": [
    {
      "claim_type": "source_assertion",
      "explanation": "Candidate interpretation requiring review: the first evidence record names one target.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/DerivedStatement/fd3db67ec6a05fdaa22d8c1407740e44cdbfc775cc25b2239bdfbd15268bd611",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/EvidenceOccurrence/7761d516706013aba8ffe20a7b45209f04fdbb1dbaf649cd6d51917a87dc6a80> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#hasTarget> <https://github.com/subramanyaprasad21/dementia-kg-ai/id/Target/f941f90f41909fda2dfefa50fe5c0d5a521a3b3c234dfd3f17cb845644b8da40> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "Candidate interpretation requiring review: the second evidence record names a different target.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/DerivedStatement/fd3db67ec6a05fdaa22d8c1407740e44cdbfc775cc25b2239bdfbd15268bd611",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/EvidenceOccurrence/b845e08aa2a1a47ad4e331d75ff3b2cc86250fd2c13b82fee2d5044f02c769c6> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#hasTarget> <https://github.com/subramanyaprasad21/dementia-kg-ai/id/Target/95bd026992ad84a3133d0be3a8c3a64073536a4f13a344fdbe744b076668f051> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "Candidate interpretation requiring review: the recorded comparison reports a shared study reference; it does not establish independence or clinical efficacy.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/DerivedStatement/fd3db67ec6a05fdaa22d8c1407740e44cdbfc775cc25b2239bdfbd15268bd611",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/DerivedStatement/fd3db67ec6a05fdaa22d8c1407740e44cdbfc775cc25b2239bdfbd15268bd611> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#resultSummary> \"Both source rows reference nct00594737.\"^^<http://www.w3.org/2001/XMLSchema#string> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "Candidate interpretation requiring review: the comparison explicitly limits its scope and disclaims an independence inference.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/DerivedStatement/fd3db67ec6a05fdaa22d8c1407740e44cdbfc775cc25b2239bdfbd15268bd611",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/DerivedStatement/fd3db67ec6a05fdaa22d8c1407740e44cdbfc775cc25b2239bdfbd15268bd611> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#scopeText> \"Compare only these two source clinicalReportId fields; no independence or efficacy inference.\"^^<http://www.w3.org/2001/XMLSchema#string> ."
    }
  ],
  "unanswered": [
    "Whether either target has an independent confirmation after review of the underlying studies and publications."
  ]
}
```

</details>

### Local verification — automated, not owner scoring

Grounded and verified prose are identical. Submitted assertions: 4; accepted: 4; rejected: 0.

| Claim | Automated outcome | Reasons |
|---|---|---|
| G1 / V1 | RDF-ASSERTION-SUPPORTED | None |
| G2 / V2 | RDF-ASSERTION-SUPPORTED | None |
| G3 / V3 | RDF-ASSERTION-SUPPORTED | None |
| G4 / V4 | RDF-ASSERTION-SUPPORTED | None |

Model-only is unverified; it has no structured claims in this recorded run. Its prose still requires review.

### Frozen required facts

| Fact ID | Exact frozen requirement |
|---|---|
| M7-09-F1 | The two different target occurrences share nct00594737 and the derived comparison is shared-source-established. |

### Frozen expected behavior and qualifications

**Expected disposition:** qualify

Supported record facts may be reported with the listed boundaries; absent or out-of-scope evidence cannot license the prohibited conclusions.

- Different IDs/targets alone do not establish independence; this local example does not show all records everywhere are dependent.

### Frozen unsupported claims to penalize

- Two targets guarantee two independent confirmations

### Frozen scoring criteria — verbatim

```json
{
  "scoringDimensions": [
    "source-relative assertion support",
    "human prose support/unsupported/contradicted/unresolved labels",
    "required-fact completion",
    "relevance",
    "provenance accuracy",
    "qualification and bounded abstention",
    "retrieval coverage",
    "failure/usage/cost"
  ],
  "scoringRequirements": {
    "excessiveAbstention": null,
    "proseLabels": "Sole human reviewer assigns supported/unsupported/contradicted/unresolved against frozen evidence; no clinical truth claim.",
    "qualificationPass": "All listed acceptable qualifications relevant to the response must be respected; no listed forbidden claim may be asserted.",
    "requiredAbstention": "Withhold all listed forbidden claims explicitly with a source-scoped explanation; retain useful required facts. Generic refusal or API failure is not success.",
    "requiredFactCompletion": "Each listed fact ID counted once only when correctly conveyed with source scope; all items have a nonzero required-fact denominator. Failures score zero completion.",
    "sharedGeneration": "Identical grounded/verified prose receives identical human prose scoring; retained assertion surfaces scored separately."
  }
}
```

<details><summary>Frozen retrieval scope and source references</summary>

```json
{
  "retrievalScope": {
    "maxPacketBytes": 196608,
    "mode": "hybrid",
    "records": 8,
    "rootIds": [
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/DerivedStatement/fd3db67ec6a05fdaa22d8c1407740e44cdbfc775cc25b2239bdfbd15268bd611",
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/9bb44911596e3db2ef337067480b7d127897e4c5c7918e8f2ac31bb4d803c66b",
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/bad88e8b10862169dcb3022359308caa2c0da43953e03fdcadaef53999bfcc7b"
    ],
    "status": "FROZEN"
  },
  "sourceReferences": [
    "manifests/dementia-development-001.json",
    "kg/mondo-pilot-001/records.ttl",
    "kg/mondo-pilot-001/provenance.ttl",
    "kg/ot2606-evidence-001/records.ttl",
    "kg/ot2606-evidence-001/provenance.ttl",
    "kg/ot2606-context-001/records.ttl"
  ]
}
```

</details>

### Owner scoring — recorded under the supplied review instructions

**A. Source-relative prose labels** (S supported / U unsupported / C contradicted / R unresolved). All factual surfaces are considered. Exact copied propositions are counted once; surface membership is retained. Nonfactual disclaimers and questions are excluded.

| Condition / surfaces | Exact proposition | Label | Basis |
|---|---|---|---|
| M / answer_text | Different targets do not automatically make two evidence records independent confirmations. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| M / answer_text | The records could share a dataset, experimental methods, authors, or an underlying source, and they may support different claims. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| M / answer_text | Independence requires checking their provenance and what each record actually establishes. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| M / answer_text | No records were supplied, so this cannot be assessed here. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | Different targets do not automatically make two evidence records independent confirmations. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | In this packet, the two records name different targets, but a comparison record reports that both source rows reference the same study, nct00594737. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | That is a reason to review their provenance rather than count them as independent confirmations. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-1-explanation | Candidate interpretation requiring review: the first evidence record names one target. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-2-explanation | Candidate interpretation requiring review: the second evidence record names a different target. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-3-explanation | Candidate interpretation requiring review: the recorded comparison reports a shared study reference; | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-3-explanation | it does not establish independence or clinical efficacy. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-4-explanation | Candidate interpretation requiring review: the comparison explicitly limits its scope and disclaims an independence inference. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |

Excluded nonfactual material is retained with reasons in the machine-readable review; original answers above remain untouched.

**B. Strict required-fact completion — owner decisions**

| Fact ID | M | G | V |
|---|---|---|---|
| M7-09-F1 | N | Y | Y |

**C. Retained assertion judgments** — statement support, question relevance and citation/source provenance; not a completeness score. Model-only has no retained assertions; precision is undefined.

| Assertion | Support | Relevant? | Provenance correct? | Reason |
|---|---|---|---|---|
| G1 / V1 | S | Y | Y | First target participant; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G2 / V2 | S | Y | Y | Distinct second target participant; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G3 / V3 | S | Y | Y | Shared source study comparison; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G4 / V4 | S | Y | Y | Scope of dependency comparison; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |

**D. Qualification and abstention** — applied from frozen rules and owner observations.

| Condition | Qualification | Required abstention | Excessive abstention |
|---|---|---|---|
| M | Y | N | Not applicable |
| G | Y | Y | Not applicable |
| V | Y | Y | Not applicable |

Grounded respects the frozen source boundaries despite any detail omissions. Model-only Q08/Q10/Q12 fails corpus-only qualification because the owner identifies clinical/treatment scope leakage; other model-only scope qualifications are respected.

For Q07–12 the strict frozen pass requires source-scoped explanation retaining useful required facts. Model-only general reasoning/no-access admissions are appropriate but do not pass that conjunctive source-specific criterion. Grounded supplies source-specific qualifications and useful details, even when a compound required fact is incomplete (Q10). This does not label model-only retrieval as failed.

**E. Retrieval coverage — separate from output completion**

Frozen supplied G/V packets contain the reference witnesses for: M7-09-F1. Missing fact witness sets: none. Exact statement witnesses and request hash are recorded in `owner-review-scores.json`. A prose omission does not remove evidence from these packets. Model-only retrieval coverage: not applicable, intentionally no retrieval.

**F. Owner comments — supplied observations**

- Model-only had no corpus access but correctly reasoned that different targets do not automatically mean independent confirmations.
- Grounded supplied the actual corpus-specific reason: both rows reference nct00594737.
- Required fact fully conveyed.
- Classification: grounded worked as intended.
- This is a clean example of baseline general reasoning + grounding supplying the actual provenance evidence.

**Residual annotation note:** No outside biomedical knowledge was used to resolve labels.

## M7-10

<!-- BEGIN M7-10 QUESTION -->
The GRIN1 and GRIN3B records are connected to a Phase 3 study, so does that mean memantine was proven clinically effective and safe for FTD?
<!-- END M7-10 QUESTION -->

### Model-only answer — unchanged

<!-- BEGIN M7-10 MODEL-ONLY ANSWER -->
````text
No. A connection between GRIN1 or GRIN3B records and a Phase 3 study does not establish that memantine was effective or safe for frontotemporal dementia (FTD). A study’s phase or a gene association is not a positive trial result. Based on general knowledge, memantine has not shown convincing clinical benefit in FTD, but I cannot verify the specific study, its outcomes, or its safety findings from the information supplied. This is an unverified development control, not clinical advice.
````
<!-- END M7-10 MODEL-ONLY ANSWER -->

<details><summary>Complete structured claims and unanswered fields — unchanged values</summary>

```json
{
  "claims": [],
  "unanswered": [
    "Which Phase 3 study do the GRIN1 and GRIN3B records refer to?",
    "What did that study report for FTD efficacy and adverse events?"
  ]
}
```

</details>

### KG-grounded answer — unchanged

<!-- BEGIN M7-10 KG-GROUNDED ANSWER -->
````text
No. The supplied records label the linked study as “PHASE_3,” but that label does not establish that memantine was effective or safe for frontotemporal dementia (FTD). The study-record text explicitly says it contains no acquired outcome or efficacy claim. The mechanism records also cannot establish a clinical result. These are candidate interpretations of the supplied records, not reviewed biomedical conclusions.
````
<!-- END M7-10 KG-GROUNDED ANSWER -->

<details><summary>Complete structured claims and unanswered fields — unchanged values</summary>

```json
{
  "claims": [
    {
      "claim_type": "source_assertion",
      "explanation": "Candidate interpretation requiring review: the study record reports a phase label, not a result.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/StudyRecord/37e85a901daeb16e42ea2391acb9e8d5f10a5bd9d378900a93bb156785f123db",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/StudyRecord/37e85a901daeb16e42ea2391acb9e8d5f10a5bd9d378900a93bb156785f123db> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#trialPhaseText> \"PHASE_3\"^^<http://www.w3.org/2001/XMLSchema#string> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "Candidate interpretation requiring review: the record expressly limits what can be concluded about outcomes and efficacy.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/StudyRecord/37e85a901daeb16e42ea2391acb9e8d5f10a5bd9d378900a93bb156785f123db",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/StudyRecord/37e85a901daeb16e42ea2391acb9e8d5f10a5bd9d378900a93bb156785f123db> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#limitationText> \"OT clinical-report context only; arm and registry-version date absent. studyStartDate/publicationDate are not status dates. No acquired population, outcome, approval or efficacy claim.\"^^<http://www.w3.org/2001/XMLSchema#string> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "Candidate interpretation requiring review: the mechanism record itself cautions against inferring efficacy or independent confirmation.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/57e1f91585eea6d91f5772d3babe29fa1241ea3eaf722bbd535ce53135a114c1",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/57e1f91585eea6d91f5772d3babe29fa1241ea3eaf722bbd535ce53135a114c1> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#limitationText> \"Source gene-indexed mechanism; shared original row and molecular target context retained. No efficacy, gene-wide action or independent confirmation inferred.\"^^<http://www.w3.org/2001/XMLSchema#string> ."
    }
  ],
  "unanswered": [
    "Whether memantine was clinically effective for FTD; trial outcomes were not supplied.",
    "Whether memantine was safe for people with FTD; safety results were not supplied.",
    "Whether the linked study enrolled an FTD population or evaluated a particular treatment arm; those details were not acquired in the supplied study record."
  ]
}
```

</details>

### Local verification — automated, not owner scoring

Grounded and verified prose are identical. Submitted assertions: 3; accepted: 3; rejected: 0.

| Claim | Automated outcome | Reasons |
|---|---|---|
| G1 / V1 | RDF-ASSERTION-SUPPORTED | None |
| G2 / V2 | RDF-ASSERTION-SUPPORTED | None |
| G3 / V3 | RDF-ASSERTION-SUPPORTED | None |

Model-only is unverified; it has no structured claims in this recorded run. Its prose still requires review.

### Frozen required facts

| Fact ID | Exact frozen requirement |
|---|---|
| M7-10-F1 | Both clinical StudyRecords carry PHASE_3 and refer to nct00594737; the source records are clinical_precedence. |

### Frozen expected behavior and qualifications

**Expected disposition:** qualify

Supported record facts may be reported with the listed boundaries; absent or out-of-scope evidence cannot license the prohibited conclusions.

- A phase is not an outcome. Historical registry outcomes/population/status are unavailable; no efficacy or safety verdict follows.

### Frozen unsupported claims to penalize

- Phase 3 proves memantine effective and safe for FTD
- Missing outcome means ineffective or unsafe

### Frozen scoring criteria — verbatim

```json
{
  "scoringDimensions": [
    "source-relative assertion support",
    "human prose support/unsupported/contradicted/unresolved labels",
    "required-fact completion",
    "relevance",
    "provenance accuracy",
    "qualification and bounded abstention",
    "retrieval coverage",
    "failure/usage/cost"
  ],
  "scoringRequirements": {
    "excessiveAbstention": null,
    "proseLabels": "Sole human reviewer assigns supported/unsupported/contradicted/unresolved against frozen evidence; no clinical truth claim.",
    "qualificationPass": "All listed acceptable qualifications relevant to the response must be respected; no listed forbidden claim may be asserted.",
    "requiredAbstention": "Withhold all listed forbidden claims explicitly with a source-scoped explanation; retain useful required facts. Generic refusal or API failure is not success.",
    "requiredFactCompletion": "Each listed fact ID counted once only when correctly conveyed with source scope; all items have a nonzero required-fact denominator. Failures score zero completion.",
    "sharedGeneration": "Identical grounded/verified prose receives identical human prose scoring; retained assertion surfaces scored separately."
  }
}
```

<details><summary>Frozen retrieval scope and source references</summary>

```json
{
  "retrievalScope": {
    "maxPacketBytes": 196608,
    "mode": "hybrid",
    "records": 8,
    "rootIds": [
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/9bb44911596e3db2ef337067480b7d127897e4c5c7918e8f2ac31bb4d803c66b",
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/bad88e8b10862169dcb3022359308caa2c0da43953e03fdcadaef53999bfcc7b",
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/57e1f91585eea6d91f5772d3babe29fa1241ea3eaf722bbd535ce53135a114c1",
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/bbe177073d1a5b77b7cd9a6d71dc779d221fd18954938288f7a44b611dd9a45a",
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/StudyRecord/37e85a901daeb16e42ea2391acb9e8d5f10a5bd9d378900a93bb156785f123db",
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/StudyRecord/c8c7596e26bdebf6ed339bdbc792858934fbab83b48ca17459e516b4280585d4"
    ],
    "status": "FROZEN"
  },
  "sourceReferences": [
    "manifests/dementia-development-001.json",
    "kg/mondo-pilot-001/records.ttl",
    "kg/mondo-pilot-001/provenance.ttl",
    "kg/ot2606-evidence-001/records.ttl",
    "kg/ot2606-evidence-001/provenance.ttl",
    "kg/ot2606-context-001/records.ttl"
  ]
}
```

</details>

### Owner scoring — recorded under the supplied review instructions

**A. Source-relative prose labels** (S supported / U unsupported / C contradicted / R unresolved). All factual surfaces are considered. Exact copied propositions are counted once; surface membership is retained. Nonfactual disclaimers and questions are excluded.

| Condition / surfaces | Exact proposition | Label | Basis |
|---|---|---|---|
| M / answer_text | A connection between GRIN1 or GRIN3B records and a Phase 3 study does not establish that memantine was effective or safe for frontotemporal dementia (FTD). | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| M / answer_text | A study’s phase or a gene association is not a positive trial result. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| M / answer_text | Based on general knowledge, memantine has not shown convincing clinical benefit in FTD, | U | Outside biomedical assertion not established by frozen project evidence. U is source-relative, not a real-world falsity judgment. Owner identifies stronger clinical/treatment scope leakage. |
| M / answer_text | but I cannot verify the specific study, its outcomes, or its safety findings from the information supplied. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | The supplied records label the linked study as “PHASE_3,” but that label does not establish that memantine was effective or safe for frontotemporal dementia (FTD). | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | The study-record text explicitly says it contains no acquired outcome or efficacy claim. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | The mechanism records also cannot establish a clinical result. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-1-explanation | Candidate interpretation requiring review: the study record reports a phase label, not a result. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-2-explanation | Candidate interpretation requiring review: the record expressly limits what can be concluded about outcomes and efficacy. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-3-explanation | Candidate interpretation requiring review: the mechanism record itself cautions against inferring efficacy or independent confirmation. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / unanswered-1 | trial outcomes were not supplied. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / unanswered-2 | safety results were not supplied. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / unanswered-3 | those details were not acquired in the supplied study record. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |

Excluded nonfactual material is retained with reasons in the machine-readable review; original answers above remain untouched.

**B. Strict required-fact completion — owner decisions**

| Fact ID | M | G | V |
|---|---|---|---|
| M7-10-F1 | N | N | N |

**C. Retained assertion judgments** — statement support, question relevance and citation/source provenance; not a completeness score. Model-only has no retained assertions; precision is undefined.

| Assertion | Support | Relevant? | Provenance correct? | Reason |
|---|---|---|---|---|
| G1 / V1 | S | Y | Y | Reported study phase; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G2 / V2 | S | Y | Y | Missing outcomes and scope limitation; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G3 / V3 | S | Y | Y | Mechanism cannot establish clinical outcome; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |

**D. Qualification and abstention** — applied from frozen rules and owner observations.

| Condition | Qualification | Required abstention | Excessive abstention |
|---|---|---|---|
| M | N | N | Not applicable |
| G | Y | Y | Not applicable |
| V | Y | Y | Not applicable |

Grounded respects the frozen source boundaries despite any detail omissions. Model-only Q08/Q10/Q12 fails corpus-only qualification because the owner identifies clinical/treatment scope leakage; other model-only scope qualifications are respected.

For Q07–12 the strict frozen pass requires source-scoped explanation retaining useful required facts. Model-only general reasoning/no-access admissions are appropriate but do not pass that conjunctive source-specific criterion. Grounded supplies source-specific qualifications and useful details, even when a compound required fact is incomplete (Q10). This does not label model-only retrieval as failed.

**E. Retrieval coverage — separate from output completion**

Frozen supplied G/V packets contain the reference witnesses for: M7-10-F1. Missing fact witness sets: none. Exact statement witnesses and request hash are recorded in `owner-review-scores.json`. A prose omission does not remove evidence from these packets. Model-only retrieval coverage: not applicable, intentionally no retrieval.

**F. Owner comments — supplied observations**

- Model-only correctly said PHASE_3 does not prove effectiveness or safety.
- It then introduced outside knowledge that memantine has not shown convincing clinical benefit in FTD.
- That outside medical statement was not supplied by this evaluation corpus.
- Grounded stayed within the source boundaries and correctly said phase is not an outcome.
- However, it omitted some required available details: both StudyRecords, shared nct00594737 and clinical_precedence source type.
- Classification: TWO DISTINCT issues:
  1. model-only outside-clinical-knowledge leakage;
  2. grounded provenance/detail completeness omission.

**Residual annotation note:** No outside biomedical knowledge was used to resolve labels.

## M7-11

<!-- BEGIN M7-11 QUESTION -->
Can the graph tell me the complete historical number of association or evidence records for PSEN1 and Alzheimer's disease?
<!-- END M7-11 QUESTION -->

### Model-only answer — unchanged

<!-- BEGIN M7-11 MODEL-ONLY ANSWER -->
````text
No. Without access to the graph or its underlying records, I cannot determine the complete historical number of association or evidence records linking PSEN1 and Alzheimer's disease. Even with graph access, the count would depend on which record types, sources, dates, and versions the graph includes. This is an unverified development control, not clinical advice.
````
<!-- END M7-11 MODEL-ONLY ANSWER -->

<details><summary>Complete structured claims and unanswered fields — unchanged values</summary>

```json
{
  "claims": [],
  "unanswered": [
    "What graph and record types are in scope?",
    "Does the graph retain historical, superseded, and deleted records?",
    "What is the count under a specified scope and time period?"
  ]
}
```

</details>

### KG-grounded answer — unchanged

<!-- BEGIN M7-11 KG-GROUNDED ANSWER -->
````text
No. The supplied packets do not establish a complete historical number of association or evidence records for PSEN1 and Alzheimer's disease. The relevant selection is explicitly limited to enumerated IDs in Open Targets 26.06 and says it is not complete disease coverage or historical rankings. Any total for the requested pair remains unanswered.
````
<!-- END M7-11 KG-GROUNDED ANSWER -->

<details><summary>Complete structured claims and unanswered fields — unchanged values</summary>

```json
{
  "claims": [
    {
      "claim_type": "source_assertion",
      "explanation": "Candidate interpretation requiring review: the recorded scope rules out treating this selection as a complete historical count.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/SelectionContext/54a78318ada19754fa39f361ee17b4dc8fb05c7262cfdc9f5269f028463253ee",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/SelectionContext/54a78318ada19754fa39f361ee17b4dc8fb05c7262cfdc9f5269f028463253ee> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#scopeText> \"Only the enumerated recovered IDs with exact normalized MONDO_0004975 in OT 26.06; not complete disease coverage or historical rankings.\"^^<http://www.w3.org/2001/XMLSchema#string> ."
    }
  ],
  "unanswered": [
    "The complete historical number of association or evidence records for PSEN1 and Alzheimer's disease."
  ]
}
```

</details>

### Local verification — automated, not owner scoring

Grounded and verified prose are identical. Submitted assertions: 1; accepted: 1; rejected: 0.

| Claim | Automated outcome | Reasons |
|---|---|---|
| G1 / V1 | RDF-ASSERTION-SUPPORTED | None |

Model-only is unverified; it has no structured claims in this recorded run. Its prose still requires review.

### Frozen required facts

| Fact ID | Exact frozen requirement |
|---|---|
| M7-11-F1 | The exact-AD local SelectionContext contains the enumerated recovered PSEN1 literature occurrence and declares completeness only for its explicit fixed-ID scope. |
| M7-11-F2 | This corpus does not supply a complete historical PSEN1/AD association/evidence total. |

### Frozen expected behavior and qualifications

**Expected disposition:** mixed

Supported record facts may be reported with the listed boundaries; absent or out-of-scope evidence cannot license the prohibited conclusions.

- Do not substitute a one-row local selection or historical audit-only count for a verified complete total. Distinguish association count from evidence count.

### Frozen unsupported claims to penalize

- One local record is the complete historical total
- No more evidence exists

### Frozen scoring criteria — verbatim

```json
{
  "scoringDimensions": [
    "source-relative assertion support",
    "human prose support/unsupported/contradicted/unresolved labels",
    "required-fact completion",
    "relevance",
    "provenance accuracy",
    "qualification and bounded abstention",
    "retrieval coverage",
    "failure/usage/cost"
  ],
  "scoringRequirements": {
    "excessiveAbstention": null,
    "proseLabels": "Sole human reviewer assigns supported/unsupported/contradicted/unresolved against frozen evidence; no clinical truth claim.",
    "qualificationPass": "All listed acceptable qualifications relevant to the response must be respected; no listed forbidden claim may be asserted.",
    "requiredAbstention": "Withhold all listed forbidden claims explicitly with a source-scoped explanation; retain useful required facts. Generic refusal or API failure is not success.",
    "requiredFactCompletion": "Each listed fact ID counted once only when correctly conveyed with source scope; all items have a nonzero required-fact denominator. Failures score zero completion.",
    "sharedGeneration": "Identical grounded/verified prose receives identical human prose scoring; retained assertion surfaces scored separately."
  }
}
```

<details><summary>Frozen retrieval scope and source references</summary>

```json
{
  "retrievalScope": {
    "maxPacketBytes": 196608,
    "mode": "hybrid",
    "records": 8,
    "rootIds": [
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/3b48e810b77da8e3a8cf3c3c2613c10b0321818543f06a2762da1be90ca8d950",
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/ceefabe649d86c21686cb3476cd3cb58a2907701447958f54a81fa441e40677f",
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/f365eb4f448c10ca07d06c86a6ce5dcad272803814f5addd0252b32ad02d1f04",
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/SelectionContext/54a78318ada19754fa39f361ee17b4dc8fb05c7262cfdc9f5269f028463253ee"
    ],
    "status": "FROZEN"
  },
  "sourceReferences": [
    "manifests/dementia-development-001.json",
    "kg/mondo-pilot-001/records.ttl",
    "kg/mondo-pilot-001/provenance.ttl",
    "kg/ot2606-evidence-001/records.ttl",
    "kg/ot2606-evidence-001/provenance.ttl",
    "kg/ot2606-context-001/records.ttl"
  ]
}
```

</details>

### Owner scoring — recorded under the supplied review instructions

**A. Source-relative prose labels** (S supported / U unsupported / C contradicted / R unresolved). All factual surfaces are considered. Exact copied propositions are counted once; surface membership is retained. Nonfactual disclaimers and questions are excluded.

| Condition / surfaces | Exact proposition | Label | Basis |
|---|---|---|---|
| M / answer_text | Without access to the graph or its underlying records, I cannot determine the complete historical number of association or evidence records linking PSEN1 and Alzheimer's disease. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| M / answer_text | Even with graph access, the count would depend on which record types, sources, dates, and versions the graph includes. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | The supplied packets do not establish a complete historical number of association or evidence records for PSEN1 and Alzheimer's disease. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | The relevant selection is explicitly limited to enumerated IDs in Open Targets 26.06 and says it is not complete disease coverage or historical rankings. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | Any total for the requested pair remains unanswered. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-1-explanation | Candidate interpretation requiring review: the recorded scope rules out treating this selection as a complete historical count. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |

Excluded nonfactual material is retained with reasons in the machine-readable review; original answers above remain untouched.

**B. Strict required-fact completion — owner decisions**

| Fact ID | M | G | V |
|---|---|---|---|
| M7-11-F1 | N | N | N |
| M7-11-F2 | N | Y | Y |

**C. Retained assertion judgments** — statement support, question relevance and citation/source provenance; not a completeness score. Model-only has no retained assertions; precision is undefined.

| Assertion | Support | Relevant? | Provenance correct? | Reason |
|---|---|---|---|---|
| G1 / V1 | S | Y | Y | Fixed enumerated scope rather than full historical total; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |

**D. Qualification and abstention** — applied from frozen rules and owner observations.

| Condition | Qualification | Required abstention | Excessive abstention |
|---|---|---|---|
| M | Y | N | Not applicable |
| G | Y | Y | Not applicable |
| V | Y | Y | Not applicable |

Grounded respects the frozen source boundaries despite any detail omissions. Model-only Q08/Q10/Q12 fails corpus-only qualification because the owner identifies clinical/treatment scope leakage; other model-only scope qualifications are respected.

For Q07–12 the strict frozen pass requires source-scoped explanation retaining useful required facts. Model-only general reasoning/no-access admissions are appropriate but do not pass that conjunctive source-specific criterion. Grounded supplies source-specific qualifications and useful details, even when a compound required fact is incomplete (Q10). This does not label model-only retrieval as failed.

**E. Retrieval coverage — separate from output completion**

Frozen supplied G/V packets contain the reference witnesses for: M7-11-F1, M7-11-F2. Missing fact witness sets: none. Exact statement witnesses and request hash are recorded in `owner-review-scores.json`. A prose omission does not remove evidence from these packets. Model-only retrieval coverage: not applicable, intentionally no retrieval.

**F. Owner comments — supplied observations**

- Model-only correctly avoided inventing a historical total and explained that such counts depend on scope/version/source/record definitions.
- No problematic patient-specific or corpus-specific biomedical claim was added.
- Grounded correctly refused to claim a complete historical total and preserved the bounded selection limitation.
- However, it omitted the local enumerated PSEN1 literature occurrence required by F1.
- Classification: grounded partial scope/count-context completeness issue.
- This is primarily a corpus-scope/accounting problem rather than a biomedical-inference problem.

**Residual annotation note:** No outside biomedical knowledge was used to resolve labels.

## M7-12

<!-- BEGIN M7-12 QUESTION -->
PSEN1 has evidence connected to Alzheimer's disease, and lecanemab has an Alzheimer's indication. Does that mean lecanemab can be given specifically because a patient has a PSEN1-related finding?
<!-- END M7-12 QUESTION -->

### Model-only answer — unchanged

<!-- BEGIN M7-12 MODEL-ONLY ANSWER -->
````text
No. A PSEN1-related finding and lecanemab’s Alzheimer’s indication do not, by themselves, establish that lecanemab should be given because of that finding. Treatment eligibility depends on the specific diagnosis, disease stage, confirmation of amyloid pathology, and the applicable prescribing criteria and safety assessment. Whether a particular PSEN1 variant changes the expected benefit or risk is uncertain; the finding alone is not a treatment indication. This is an unverified development-control answer, not clinical advice.
````
<!-- END M7-12 MODEL-ONLY ANSWER -->

<details><summary>Complete structured claims and unanswered fields — unchanged values</summary>

```json
{
  "claims": [],
  "unanswered": [
    "Which PSEN1 variant or finding is involved, and how is it classified?",
    "Does the patient meet the applicable lecanemab eligibility and safety criteria?",
    "What evidence, if any, establishes lecanemab’s benefit and risk specifically in patients with this PSEN1 finding?"
  ]
}
```

</details>

### KG-grounded answer — unchanged

<!-- BEGIN M7-12 KG-GROUNDED ANSWER -->
````text
No. These packets record an Alzheimer’s disease indication for the drug and a separate PSEN1-related evidence occurrence, but they do not establish that a PSEN1 finding is itself a reason to give lecanemab. The indication record reports a maximum stage of “APPROVAL”; it does not supply patient eligibility, registry population or efficacy information. This is a candidate interpretation of the supplied records, not a treatment recommendation.
````
<!-- END M7-12 KG-GROUNDED ANSWER -->

<details><summary>Complete structured claims and unanswered fields — unchanged values</summary>

```json
{
  "claims": [
    {
      "claim_type": "source_assertion",
      "explanation": "The clinical-indication record links the drug to a disease reference. The supplied question identifies this drug as lecanemab; the statement itself uses a drug identifier.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/ClinicalIndicationRecord/8d409cf761cbae391ba0ac03b3aee9046100d030f6779e9ecaad80c4cd11815b",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/ClinicalIndicationRecord/8d409cf761cbae391ba0ac03b3aee9046100d030f6779e9ecaad80c4cd11815b> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#hasDrug> <https://github.com/subramanyaprasad21/dementia-kg-ai/id/Drug/268032fa0ce6c2abd6a7f4f9d967ff1a0a8ba35c235ddab3fe1bdcbdde8e69f5> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "The record reports a trial-phase text value, not a PSEN1-specific eligibility rule.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/ClinicalIndicationRecord/8d409cf761cbae391ba0ac03b3aee9046100d030f6779e9ecaad80c4cd11815b",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/ClinicalIndicationRecord/8d409cf761cbae391ba0ac03b3aee9046100d030f6779e9ecaad80c4cd11815b> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#trialPhaseText> \"APPROVAL\"^^<http://www.w3.org/2001/XMLSchema#string> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "The record expressly limits what was acquired about the indication.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/ClinicalIndicationRecord/8d409cf761cbae391ba0ac03b3aee9046100d030f6779e9ecaad80c4cd11815b",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/ClinicalIndicationRecord/8d409cf761cbae391ba0ac03b3aee9046100d030f6779e9ecaad80c4cd11815b> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#limitationText> \"Source maximum indication stage only. Report locators retained in the linked source description; registry population/status and efficacy not acquired.\"^^<http://www.w3.org/2001/XMLSchema#string> ."
    },
    {
      "claim_type": "source_assertion",
      "explanation": "A separate evidence occurrence names the target represented in the question as PSEN1; this statement does not connect that finding to drug eligibility.",
      "packet_id": "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/ceefabe649d86c21686cb3476cd3cb58a2907701447958f54a81fa441e40677f",
      "statement": "<https://github.com/subramanyaprasad21/dementia-kg-ai/id/EvidenceOccurrence/4478fdd7719e8e57c23cb47c23442ff4622271b9be95dc50f1a2b1d439682a88> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#hasTarget> <https://github.com/subramanyaprasad21/dementia-kg-ai/id/Target/a5663e0cfac4822a46dbd160d6b8c857b70a982247a0ec326dadb865a970e3c6> ."
    }
  ],
  "unanswered": [
    "Whether a particular PSEN1 finding changes lecanemab eligibility or expected benefit.",
    "Whether the patient meets the applicable indication and other treatment requirements."
  ]
}
```

</details>

### Local verification — automated, not owner scoring

Grounded and verified prose are identical. Submitted assertions: 4; accepted: 4; rejected: 0.

| Claim | Automated outcome | Reasons |
|---|---|---|
| G1 / V1 | RDF-ASSERTION-SUPPORTED | None |
| G2 / V2 | RDF-ASSERTION-SUPPORTED | None |
| G3 / V3 | RDF-ASSERTION-SUPPORTED | None |
| G4 / V4 | RDF-ASSERTION-SUPPORTED | None |

Model-only is unverified; it has no structured claims in this recorded run. Its prose still requires review.

### Frozen required facts

| Fact ID | Exact frozen requirement |
|---|---|
| M7-12-F1 | PSEN1 has a source record normalized to AD, and lecanemab has an AD indication; its represented mechanism is APP-indexed. |
| M7-12-F2 | No represented rule, patient data or treatment-response evidence licenses patient-specific prescribing from that PSEN1 finding. |

### Frozen expected behavior and qualifications

**Expected disposition:** qualify

Supported record facts may be reported with the listed boundaries; absent or out-of-scope evidence cannot license the prohibited conclusions.

- Treat solely as a graph-inference sufficiency question, not real-world prescribing advice. Do not claim a contraindication or deny possible clinical use.

### Frozen unsupported claims to penalize

- Prescribe because of PSEN1
- Patient eligibility, contraindication or treatment response inferred from a shared disease node

### Frozen scoring criteria — verbatim

```json
{
  "scoringDimensions": [
    "source-relative assertion support",
    "human prose support/unsupported/contradicted/unresolved labels",
    "required-fact completion",
    "relevance",
    "provenance accuracy",
    "qualification and bounded abstention",
    "retrieval coverage",
    "failure/usage/cost"
  ],
  "scoringRequirements": {
    "excessiveAbstention": null,
    "proseLabels": "Sole human reviewer assigns supported/unsupported/contradicted/unresolved against frozen evidence; no clinical truth claim.",
    "qualificationPass": "All listed acceptable qualifications relevant to the response must be respected; no listed forbidden claim may be asserted.",
    "requiredAbstention": "Withhold all listed forbidden claims explicitly with a source-scoped explanation; retain useful required facts. Generic refusal or API failure is not success.",
    "requiredFactCompletion": "Each listed fact ID counted once only when correctly conveyed with source scope; all items have a nonzero required-fact denominator. Failures score zero completion.",
    "sharedGeneration": "Identical grounded/verified prose receives identical human prose scoring; retained assertion surfaces scored separately."
  }
}
```

<details><summary>Frozen retrieval scope and source references</summary>

```json
{
  "retrievalScope": {
    "maxPacketBytes": 196608,
    "mode": "hybrid",
    "records": 8,
    "rootIds": [
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/ClinicalIndicationRecord/8d409cf761cbae391ba0ac03b3aee9046100d030f6779e9ecaad80c4cd11815b",
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/3b48e810b77da8e3a8cf3c3c2613c10b0321818543f06a2762da1be90ca8d950",
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/ceefabe649d86c21686cb3476cd3cb58a2907701447958f54a81fa441e40677f",
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/f365eb4f448c10ca07d06c86a6ce5dcad272803814f5addd0252b32ad02d1f04",
      "https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/a413f6671dc36fa70a1079361b6b4236fb96a9e594c1785b40f8ee445869f6fb"
    ],
    "status": "FROZEN"
  },
  "sourceReferences": [
    "manifests/dementia-development-001.json",
    "kg/mondo-pilot-001/records.ttl",
    "kg/mondo-pilot-001/provenance.ttl",
    "kg/ot2606-evidence-001/records.ttl",
    "kg/ot2606-evidence-001/provenance.ttl",
    "kg/ot2606-context-001/records.ttl"
  ]
}
```

</details>

### Owner scoring — recorded under the supplied review instructions

**A. Source-relative prose labels** (S supported / U unsupported / C contradicted / R unresolved). All factual surfaces are considered. Exact copied propositions are counted once; surface membership is retained. Nonfactual disclaimers and questions are excluded.

| Condition / surfaces | Exact proposition | Label | Basis |
|---|---|---|---|
| M / answer_text | A PSEN1-related finding and lecanemab’s Alzheimer’s indication do not, by themselves, establish that lecanemab should be given because of that finding. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| M / answer_text | Treatment eligibility depends on the specific diagnosis, disease stage, confirmation of amyloid pathology, and the applicable prescribing criteria and safety assessment. | U | Outside biomedical assertion not established by frozen project evidence. U is source-relative, not a real-world falsity judgment. Owner identifies stronger clinical/treatment scope leakage. |
| M / answer_text | Whether a particular PSEN1 variant changes the expected benefit or risk is uncertain; | U | Variant-specific benefit/risk is explicitly uncertain and not resolved by the frozen corpus. |
| M / answer_text | the finding alone is not a treatment indication. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | These packets record an Alzheimer’s disease indication for the drug and a separate PSEN1-related evidence occurrence, but they do not establish that a PSEN1 finding is itself a reason to give lecanemab. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | The indication record reports a maximum stage of “APPROVAL”; | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / answer_text | it does not supply patient eligibility, registry population or efficacy information. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-1-explanation | The clinical-indication record links the drug to a disease reference. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-1-explanation | The supplied question identifies this drug as lecanemab; | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-1-explanation | the statement itself uses a drug identifier. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-2-explanation | The record reports a trial-phase text value, not a PSEN1-specific eligibility rule. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-3-explanation | The record expressly limits what was acquired about the indication. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-4-explanation | A separate evidence occurrence names the target represented in the question as PSEN1; | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |
| G/V / claim-4-explanation | this statement does not connect that finding to drug eligibility. | S | Owner observation confirms the source-scoped statement or uncertainty boundary; evaluated against frozen facts/limitations and the actual no-retrieval design. |

Excluded nonfactual material is retained with reasons in the machine-readable review; original answers above remain untouched.

**B. Strict required-fact completion — owner decisions**

| Fact ID | M | G | V |
|---|---|---|---|
| M7-12-F1 | N | N | N |
| M7-12-F2 | N | Y | Y |

**C. Retained assertion judgments** — statement support, question relevance and citation/source provenance; not a completeness score. Model-only has no retained assertions; precision is undefined.

| Assertion | Support | Relevant? | Provenance correct? | Reason |
|---|---|---|---|---|
| G1 / V1 | S | Y | Y | Indication drug participant; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G2 / V2 | S | Y | Y | Indication source stage; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G3 / V3 | S | Y | Y | Indication population/efficacy limitation; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |
| G4 / V4 | S | Y | Y | Separate PSEN1 evidence participant; individual statement is present in its named supplied packet and the linked source context is retained. This does not credit omitted prose facts. |

**D. Qualification and abstention** — applied from frozen rules and owner observations.

| Condition | Qualification | Required abstention | Excessive abstention |
|---|---|---|---|
| M | N | N | Not applicable |
| G | Y | Y | Not applicable |
| V | Y | Y | Not applicable |

Grounded respects the frozen source boundaries despite any detail omissions. Model-only Q08/Q10/Q12 fails corpus-only qualification because the owner identifies clinical/treatment scope leakage; other model-only scope qualifications are respected.

For Q07–12 the strict frozen pass requires source-scoped explanation retaining useful required facts. Model-only general reasoning/no-access admissions are appropriate but do not pass that conjunctive source-specific criterion. Grounded supplies source-specific qualifications and useful details, even when a compound required fact is incomplete (Q10). This does not label model-only retrieval as failed.

**E. Retrieval coverage — separate from output completion**

Frozen supplied G/V packets contain the reference witnesses for: M7-12-F1, M7-12-F2. Missing fact witness sets: none. Exact statement witnesses and request hash are recorded in `owner-review-scores.json`. A prose omission does not remove evidence from these packets. Model-only retrieval coverage: not applicable, intentionally no retrieval.

**F. Owner comments — supplied observations**

- Model-only correctly rejected the inference that a PSEN1 finding alone licenses lecanemab treatment.
- But it moved into outside real-world treatment information: diagnosis, disease stage, amyloid confirmation, prescribing criteria and safety assessment.
- Those details were not supplied by the evaluation corpus.
- This is another meaningful outside-knowledge/scope-leakage case.
- Grounded stayed within supplied evidence and correctly rejected a PSEN1-specific prescribing inference.
- However, it omitted part of the required evidence chain, especially the APP-indexed lecanemab mechanism and explicit PSEN1→AD normalization.
- Classification: TWO DISTINCT issues:
  1. model-only outside-treatment-knowledge leakage;
  2. grounded cross-record evidence-integration omission.

**Residual annotation note:** No outside biomedical knowledge was used to resolve labels.

## Owner review provenance and status

All 12 supplied strict fact decisions and question observations are transcribed. Remaining annotation fields are completed under the owner’s E/F instructions, with their operationalization explicitly recorded rather than represented as newly supplied verbatim human labels. The user remains sole curator/reviewer; no independent review is claimed. Exact source instructions, scoring JSON and computed metrics are versioned alongside this document. The earlier blank version remains in commit 14dcbcb2733bc7896ea649f95cbe4c4c12c785ca and its original integrity receipt is preserved.

## Experimental design note

Model-only intentionally had no access to the project KG/evidence corpus. It is the no-retrieval baseline, not a failed retrieval condition. Its corpus-specific fact incompleteness is expected; judge its uncertainty, general reasoning and outside-knowledge scope separately. A grounded completeness concern means supplied relevant evidence was not fully or correctly used in generated prose. Do not collapse these into a generic AI gap or infer an ontology defect or causal retrieval failure.
