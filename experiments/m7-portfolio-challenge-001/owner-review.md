# M7 owner review worksheet

Reviewer: Subramanya Prasad. Status: NOT SCORED.

Use the unchanged private rubric in the private m7-portfolio-challenge-001 directory. This worksheet includes model outputs, not gold answers. Do not change frozen reference facts or scoring rules.

Grounded and verified prose is identical. Verification filters assertion records only; prose remains unverified. Score all frozen dimensions using the private rubric. Independent review has not occurred.

## M7-01 — model_only

Which drug or drugs in the graph have a mechanism connected to GRIN1 and GRIN3B, and what sources support those connections?

### Unchanged generated prose

I cannot determine which drugs in the graph have mechanisms connected to both GRIN1 and GRIN3B because the graph and its supporting sources were not supplied. From general knowledge, memantine and ketamine act on NMDA receptors, of which GRIN1 is an essential subunit. That does not establish a GRIN3B-specific connection for either drug or show that either appears in the graph. This is an unverified development-control answer, not clinical advice.

### Structured claims

Unanswered fields (model-generated; not a human abstention score):
["Which drugs are present in the graph?", "Which graph connections link drug mechanisms to GRIN1 and GRIN3B?", "What sources support each connection?"]

## M7-01 — retrieval

Which drug or drugs in the graph have a mechanism connected to GRIN1 and GRIN3B, and what sources support those connections?

### Unchanged generated prose

The retrieved mechanism records identify one drug, CHEMBL807, with connections to two target identifiers: ENSG00000176884 (GRIN1) and ENSG00000116032 (GRIN3B). Both records describe its mechanism as “Glutamate [NMDA] receptor negative allosteric modulator” and trace to the same row of Open Targets Platform’s drug_mechanism_of_action table, edition 26.06. These are source-reported connections, not two independent confirmations or evidence of gene-wide action or clinical efficacy.

### Structured claims

1. The drug identifier in the GRIN1-connected mechanism packet is CHEMBL807.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/Drug/d6636d191f768d9a02bdd2d95057639e5c570fa3e78594dce327a0d27b3876b0> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#externalIdentifier> "CHEMBL807"^^<http://www.w3.org/2001/XMLSchema#string> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/57e1f91585eea6d91f5772d3babe29fa1241ea3eaf722bbd535ce53135a114c1`

2. This mechanism record links that drug to the target identified in the packet as ENSG00000176884.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/57e1f91585eea6d91f5772d3babe29fa1241ea3eaf722bbd535ce53135a114c1> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#hasTarget> <https://github.com/subramanyaprasad21/dementia-kg-ai/id/Target/95bd026992ad84a3133d0be3a8c3a64073536a4f13a344fdbe744b076668f051> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/57e1f91585eea6d91f5772d3babe29fa1241ea3eaf722bbd535ce53135a114c1`

3. The first target's recorded identifier is ENSG00000176884.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/Target/95bd026992ad84a3133d0be3a8c3a64073536a4f13a344fdbe744b076668f051> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#externalIdentifier> "ENSG00000176884"^^<http://www.w3.org/2001/XMLSchema#string> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/57e1f91585eea6d91f5772d3babe29fa1241ea3eaf722bbd535ce53135a114c1`

4. The second mechanism record links CHEMBL807 to the target identified in its packet as ENSG00000116032.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/bbe177073d1a5b77b7cd9a6d71dc779d221fd18954938288f7a44b611dd9a45a> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#hasTarget> <https://github.com/subramanyaprasad21/dementia-kg-ai/id/Target/f941f90f41909fda2dfefa50fe5c0d5a521a3b3c234dfd3f17cb845644b8da40> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/bbe177073d1a5b77b7cd9a6d71dc779d221fd18954938288f7a44b611dd9a45a`

5. The second target's recorded identifier is ENSG00000116032.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/Target/f941f90f41909fda2dfefa50fe5c0d5a521a3b3c234dfd3f17cb845644b8da40> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#externalIdentifier> "ENSG00000116032"^^<http://www.w3.org/2001/XMLSchema#string> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/bbe177073d1a5b77b7cd9a6d71dc779d221fd18954938288f7a44b611dd9a45a`

6. The mechanism description is source text, not an independently established biological conclusion.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/57e1f91585eea6d91f5772d3babe29fa1241ea3eaf722bbd535ce53135a114c1> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#sourceText> "Glutamate [NMDA] receptor negative allosteric modulator"^^<http://www.w3.org/2001/XMLSchema#string> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/57e1f91585eea6d91f5772d3babe29fa1241ea3eaf722bbd535ce53135a114c1`

7. The recorded source authority is Open Targets Platform's drug_mechanism_of_action table.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/SourceSnapshot/84363bedf050f9d01fb380554ae9aa39903fad4ea9897e3f67229f3410bdcf11> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#sourceAuthority> "Open Targets Platform / drug_mechanism_of_action"^^<http://www.w3.org/2001/XMLSchema#string> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/57e1f91585eea6d91f5772d3babe29fa1241ea3eaf722bbd535ce53135a114c1`

8. The first connection traces to source file row 3184; the second mechanism packet records the same row and file, so the records should not be counted as independent sources.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/57e1f91585eea6d91f5772d3babe29fa1241ea3eaf722bbd535ce53135a114c1> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#sourceLocator> "{\"fileRowNumber\":\"3184\",\"fileSha256\":\"4a02cef4c182bb0ed20d341c6c4553f6c839b02f3217777fb65993a38e456a29\",\"url\":\"https://ftp.ebi.ac.uk/pub/databases/opentargets/platform/26.06/output/drug_mechanism_of_action/part-00001-10b94b1b-f29a-440c-98e0-c91862b6d2a8-c000.snappy.parquet\"}"^^<http://www.w3.org/2001/XMLSchema#string> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/57e1f91585eea6d91f5772d3babe29fa1241ea3eaf722bbd535ce53135a114c1`

Unanswered fields (model-generated; not a human abstention score):
["The supplied mechanism packets do not state a drug name for CHEMBL807 or explicitly give the GRIN1 and GRIN3B symbols alongside their Ensembl identifiers.", "Independent verification of the mechanism connections and their biological or clinical implications is not supplied."]

## M7-02 — model_only

What disease concepts are the PSEN1 evidence records mapped to in the graph, and if mapping information is missing for any record, why?

### Unchanged generated prose

I cannot determine which disease concepts the PSEN1 evidence records are mapped to because no graph records or mapping information were supplied. I also cannot determine whether any mappings are missing or why. Although PSEN1 is commonly associated with familial early-onset Alzheimer disease, that general knowledge does not establish how these particular records are mapped. This is an unverified development-control response, not clinical advice.

### Structured claims

Unanswered fields (model-generated; not a human abstention score):
["Which disease concepts are assigned to each PSEN1 evidence record in the graph?", "Are any records missing a disease-concept mapping, and if so, what is the documented reason?"]

## M7-02 — retrieval

What disease concepts are the PSEN1 evidence records mapped to in the graph, and if mapping information is missing for any record, why?

### Unchanged generated prose

The supplied PSEN1 evidence records report two disease-concept destinations: MONDO_0017276 for a Genomics England record and one Europe PMC record, and MONDO_0004975 for another Europe PMC record. The Genomics England record has a stated mapping input, OMIM:600274, labelled “Dementia, frontotemporal.” Both Europe PMC records have a reported destination but lack the original disease mapping input: their missingness records attribute this to original disease input columns being absent from the historical Europe PMC Parquet schema. These are source-reported mappings marked validity-unreviewed, not reviewed biomedical equivalences.

### Structured claims

1. Candidate interpretation: this is the reported destination for the Genomics England evidence record.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/3b48e810b77da8e3a8cf3c3c2613c10b0321818543f06a2762da1be90ca8d950> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#reportedDestination> <https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/115e9f610af71460664bb63b5e5cf112710effd9027cd0ed71d4cfe3528eb29e> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/3b48e810b77da8e3a8cf3c3c2613c10b0321818543f06a2762da1be90ca8d950`

2. Candidate interpretation: the destination's recorded identifier is MONDO_0017276.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/115e9f610af71460664bb63b5e5cf112710effd9027cd0ed71d4cfe3528eb29e> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#externalIdentifier> "MONDO_0017276"^^<http://www.w3.org/2001/XMLSchema#string> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/3b48e810b77da8e3a8cf3c3c2613c10b0321818543f06a2762da1be90ca8d950`

3. Candidate interpretation: this record supplies an original mapping input, unlike the two Europe PMC records.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/08501ee3ac587ca779987f31b5db4192c5299e442d309286f36abcb8975e1a26> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#sourceLabel> "Dementia, frontotemporal"^^<http://www.w3.org/2001/XMLSchema#string> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/3b48e810b77da8e3a8cf3c3c2613c10b0321818543f06a2762da1be90ca8d950`

4. Candidate interpretation: this is the recorded identifier of that input.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/08501ee3ac587ca779987f31b5db4192c5299e442d309286f36abcb8975e1a26> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#externalIdentifier> "OMIM:600274"^^<http://www.w3.org/2001/XMLSchema#string> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/3b48e810b77da8e3a8cf3c3c2613c10b0321818543f06a2762da1be90ca8d950`

5. Candidate interpretation: one Europe PMC record reports this destination.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/f365eb4f448c10ca07d06c86a6ce5dcad272803814f5addd0252b32ad02d1f04> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#reportedDestination> <https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/5c9ccec62fe78b3e3bb8f60611bec066644f4beb6ef4a343232ebf91a22e723d> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/f365eb4f448c10ca07d06c86a6ce5dcad272803814f5addd0252b32ad02d1f04`

6. Candidate interpretation: that Europe PMC destination has the recorded identifier MONDO_0017276.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/5c9ccec62fe78b3e3bb8f60611bec066644f4beb6ef4a343232ebf91a22e723d> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#externalIdentifier> "MONDO_0017276"^^<http://www.w3.org/2001/XMLSchema#string> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/f365eb4f448c10ca07d06c86a6ce5dcad272803814f5addd0252b32ad02d1f04`

7. Candidate interpretation: the other Europe PMC record reports this destination.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/ceefabe649d86c21686cb3476cd3cb58a2907701447958f54a81fa441e40677f> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#reportedDestination> <https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/c049c408b5f38644d770b361909e043473b21df50c171a69f0e3039bd51abacc> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/ceefabe649d86c21686cb3476cd3cb58a2907701447958f54a81fa441e40677f`

8. Candidate interpretation: that destination has the recorded identifier MONDO_0004975; no source label for it is supplied here.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/c049c408b5f38644d770b361909e043473b21df50c171a69f0e3039bd51abacc> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#externalIdentifier> "MONDO_0004975"^^<http://www.w3.org/2001/XMLSchema#string> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/ceefabe649d86c21686cb3476cd3cb58a2907701447958f54a81fa441e40677f`

9. Candidate interpretation requiring review: this records why the original mapping input is missing for the Europe PMC record reporting MONDO_0017276, not why its destination is missing.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/MissingnessRecord/6e936f84b8434a6a8c7479f36d0792a0b60dc3745021234dcc88164983e3a394> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#rationale> "Original disease input columns absent in the historical Europe PMC Parquet schema; not evidence of biological absence or a reproduced GraphQL null."^^<http://www.w3.org/2001/XMLSchema#string> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/MissingnessRecord/6e936f84b8434a6a8c7479f36d0792a0b60dc3745021234dcc88164983e3a394`

10. Candidate interpretation requiring review: the same stated schema limitation applies to the Europe PMC record reporting MONDO_0004975.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/MissingnessRecord/af7a7011477848f8309397edf525843d62d42708f7064b29444593d8fdb9ec21> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#rationale> "Original disease input columns absent in the historical Europe PMC Parquet schema; not evidence of biological absence or a reproduced GraphQL null."^^<http://www.w3.org/2001/XMLSchema#string> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/MissingnessRecord/af7a7011477848f8309397edf525843d62d42708f7064b29444593d8fdb9ec21`

Unanswered fields (model-generated; not a human abstention score):
["The original disease mapping inputs for the two Europe PMC records cannot be recovered from the supplied packets.", "The upstream mapping methods and biomedical validity of the reported assignments are not established by these packets."]

## M7-03 — model_only

Which disease concepts connected to APP are represented in the current evidence corpus, and what are their sources?

### Unchanged generated prose

No evidence corpus was supplied, so I cannot determine which disease concepts connected to APP are represented in it or identify their sources. From model knowledge, APP is associated with Alzheimer’s disease and cerebral amyloid angiopathy, but that does not establish that either appears in the current corpus. This is an unverified development-control answer, not clinical advice.

### Structured claims

Unanswered fields (model-generated; not a human abstention score):
["Which APP-connected disease concepts are represented in the current evidence corpus?", "What are the sources for those concepts?"]

## M7-03 — retrieval

Which disease concepts connected to APP are represented in the current evidence corpus, and what are their sources?

### Unchanged generated prose

The supplied records connect the APP target (ENSG00000142192) to a Genomics England evidence occurrence whose source disease is “Alzheimer disease 1, familial” (OMIM:104300) and whose reported destination is MONDO_0007088. Mondo labels that destination “Alzheimer disease type 1” (MONDO:0007088) and reports an immediate-parent path through “early-onset autosomal dominant Alzheimer disease” (MONDO:0015140), “familial Alzheimer disease” (MONDO:0100087), and “Alzheimer disease” (MONDO:0004975). The Genomics England record is supplied through Open Targets Platform 26.06; the hierarchy comes from Mondo via EMBL-EBI OLS, edition 2026-09-01. This is a candidate reading of the retrieved records, not a validated disease association or a claim that the mapping establishes biomedical equivalence.

### Structured claims

1. The Genomics England evidence occurrence has the target whose recorded Ensembl identifier is ENSG00000142192; the packet does not supply a target-symbol triple.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/EvidenceOccurrence/796696cbe1d8a518d5e57a122ddff4d49ed47f7ef40eeef4ab45186e7956ffe6> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#hasTarget> <https://github.com/subramanyaprasad21/dementia-kg-ai/id/Target/ab286f8dc660098033c6eae4a04a8c626c2d0429bb6df202af6d91888683c3ea> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/e10a18e680a100ce9ab8dea84d460991ae41e86378a939068732300c8a7a8ec7`

2. The source disease label attached to the occurrence’s mapping input is “Alzheimer disease 1, familial”; its identifier is OMIM:104300.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/ed6dfb77e60621587045037175e0c6bfe61e86e6f650a09b9eb0a1ae384379ac> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#sourceLabel> "Alzheimer disease 1, familial"^^<http://www.w3.org/2001/XMLSchema#string> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/e10a18e680a100ce9ab8dea84d460991ae41e86378a939068732300c8a7a8ec7`

3. The Genomics England mapping reports a MONDO_0007088 destination; its recorded status is validity-unreviewed, not an equivalence determination.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/afa9d8c09be76fef8779912526900975a7533e58b4740b43fd4af38bd44ef0fd> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#externalIdentifier> "MONDO_0007088"^^<http://www.w3.org/2001/XMLSchema#string> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/e10a18e680a100ce9ab8dea84d460991ae41e86378a939068732300c8a7a8ec7`

4. Mondo’s label for MONDO:0007088 is “Alzheimer disease type 1.”

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/94956f7d1148eef0e6a25454e94d4aa318f7f757457667eee343de4280c299da> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#sourceLabel> "Alzheimer disease type 1"^^<http://www.w3.org/2001/XMLSchema#string> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/HierarchyStep/9dbc4821c39c5ceb692fc73095131c200359c653dfc6ce0a0b355fadb756b8f8`

5. The next Mondo concept on the reported immediate-parent path is “early-onset autosomal dominant Alzheimer disease” (MONDO:0015140).

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/bcd3ca8a4dfbf567bb35be1b516ad2278c40cc18254bcb2e6cd4cf75870edd80> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#sourceLabel> "early-onset autosomal dominant Alzheimer disease"^^<http://www.w3.org/2001/XMLSchema#string> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/HierarchyStep/9dbc4821c39c5ceb692fc73095131c200359c653dfc6ce0a0b355fadb756b8f8`

6. Mondo records “familial Alzheimer disease” (MONDO:0100087) as the next concept on that parent path.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/8f1c74a3739d161dc1d7e3ec70e5de9d2ca810daf052041b5e2d6695d0c5168e> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#sourceLabel> "familial Alzheimer disease"^^<http://www.w3.org/2001/XMLSchema#string> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/HierarchyStep/677460eea8f681aaa0de334dc1973cfea6d9552515da4d0d8aab9a6c94ec73a3`

7. Mondo records “Alzheimer disease” (MONDO:0004975) above familial Alzheimer disease on the reported immediate-parent path.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/56e84bf4b4a25940c7a39128c743710b469a768016bee72e1e1f922fc4cff8db> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#sourceLabel> "Alzheimer disease"^^<http://www.w3.org/2001/XMLSchema#string> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/HierarchyStep/e63bdc528cafa7ca08d8e902f71f4de3f96f826e5d4053778898020df9cc3850`

Unanswered fields (model-generated; not a human abstention score):
["Whether these retrieved packets exhaust all APP-connected disease concepts in the current corpus.", "Whether the reported Genomics England disease mapping establishes biomedical equivalence or a validated APP–disease association."]

## M7-04 — model_only

Do GRIN1, GRIN3B and APP point to the same study or report, or different ones? If two of the three share one, tell me which two, and explain where the third one's evidence comes from.

### Unchanged generated prose

I can’t determine whether GRIN1, GRIN3B and APP point to the same study or report from the information provided. No study identifiers, reports or source records were supplied, so I can’t verify whether two share a source or where the third gene’s evidence comes from. This is an unverified development control, not clinical advice.

### Structured claims

Unanswered fields (model-generated; not a human abstention score):
["Which studies or reports are linked to GRIN1, GRIN3B and APP?", "Do any two genes share the same source, and what is the source for the third?"]

## M7-04 — retrieval

Do GRIN1, GRIN3B and APP point to the same study or report, or different ones? If two of the three share one, tell me which two, and explain where the third one's evidence comes from.

### Unchanged generated prose

GRIN1 and GRIN3B point to the same reported study, nct00594737, in two Open Targets clinical_precedence records. APP’s supplied evidence comes instead from an Open Targets genomics_england record concerning “Alzheimer disease 1, familial”; it is not presented here as a clinical report for that study. This is a comparison of the supplied records, not an assessment of biological relationships or study outcomes.

### Structured claims

1. The GRIN1-linked occurrence refers to the shared study. Candidate interpretation requiring review.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/EvidenceOccurrence/7761d516706013aba8ffe20a7b45209f04fdbb1dbaf649cd6d51917a87dc6a80> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#refersToStudy> <https://github.com/subramanyaprasad21/dementia-kg-ai/id/Study/613b6fe05a946c8ee1c2d055f0a28809bdeb1c1be593d0115d1b6d543b9cc4b7> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/DerivedStatement/fd3db67ec6a05fdaa22d8c1407740e44cdbfc775cc25b2239bdfbd15268bd611`

2. The GRIN3B-linked occurrence refers to that same study. Candidate interpretation requiring review.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/EvidenceOccurrence/b845e08aa2a1a47ad4e331d75ff3b2cc86250fd2c13b82fee2d5044f02c769c6> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#refersToStudy> <https://github.com/subramanyaprasad21/dementia-kg-ai/id/Study/613b6fe05a946c8ee1c2d055f0a28809bdeb1c1be593d0115d1b6d543b9cc4b7> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/DerivedStatement/fd3db67ec6a05fdaa22d8c1407740e44cdbfc775cc25b2239bdfbd15268bd611`

3. The shared study has this recorded identifier. Candidate interpretation requiring review.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/Study/613b6fe05a946c8ee1c2d055f0a28809bdeb1c1be593d0115d1b6d543b9cc4b7> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#externalIdentifier> "nct00594737"^^<http://www.w3.org/2001/XMLSchema#string> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/DerivedStatement/fd3db67ec6a05fdaa22d8c1407740e44cdbfc775cc25b2239bdfbd15268bd611`

4. APP’s supplied occurrence is classified as genomics_england evidence. Candidate interpretation requiring review.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/EvidenceOccurrence/796696cbe1d8a518d5e57a122ddff4d49ed47f7ef40eeef4ab45186e7956ffe6> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#evidenceSourceType> "genomics_england"^^<http://www.w3.org/2001/XMLSchema#string> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/e10a18e680a100ce9ab8dea84d460991ae41e86378a939068732300c8a7a8ec7`

5. The source disease label associated with the APP evidence is recorded literally here. Candidate interpretation requiring review.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/ed6dfb77e60621587045037175e0c6bfe61e86e6f650a09b9eb0a1ae384379ac> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#sourceLabel> "Alzheimer disease 1, familial"^^<http://www.w3.org/2001/XMLSchema#string> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/e10a18e680a100ce9ab8dea84d460991ae41e86378a939068732300c8a7a8ec7`

Unanswered fields (model-generated; not a human abstention score):
["Whether APP has any connection to nct00594737 outside the supplied records."]

## M7-05 — model_only

What indication and development stage does the graph record for gosuranemab?

### Unchanged generated prose

I can’t determine what indication and development stage the graph records for gosuranemab because no graph data was supplied. From general knowledge, gosuranemab was studied in phase 2 trials for progressive supranuclear palsy and Alzheimer’s disease, but that does not establish the graph’s entry. This is an unverified development control, not clinical advice.

### Structured claims

Unanswered fields (model-generated; not a human abstention score):
["Which indication and development stage are recorded in the graph for gosuranemab?"]

## M7-05 — retrieval

What indication and development stage does the graph record for gosuranemab?

### Unchanged generated prose

The graph records gosuranemab’s indication as MONDO_0017276 and its maximum indication stage as PHASE_1. The original condition label is not supplied, so the indication cannot be named from these packets. This is a candidate interpretation of source records, not a clinical efficacy conclusion.

### Structured claims

1. The clinical indication record links to this disease reference; the reference gives the indication identifier. Its limitation text says the original condition label is absent.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/0c038db53a8a2bf551c9132876e6809475e576353f8220ef6aaf38eee63e76ab> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#externalIdentifier> "MONDO_0017276"^^<http://www.w3.org/2001/XMLSchema#string> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/ClinicalIndicationRecord/ea2d65dcef2e7e8b4e9ee8aafd5a521c804b67b40862850878061133a1a1d3c6`

2. The record reports PHASE_1 as its source maximum indication stage, not as evidence of efficacy or current trial status.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/ClinicalIndicationRecord/ea2d65dcef2e7e8b4e9ee8aafd5a521c804b67b40862850878061133a1a1d3c6> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#trialPhaseText> "PHASE_1"^^<http://www.w3.org/2001/XMLSchema#string> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/ClinicalIndicationRecord/ea2d65dcef2e7e8b4e9ee8aafd5a521c804b67b40862850878061133a1a1d3c6`

Unanswered fields (model-generated; not a human abstention score):
["The original condition label for MONDO_0017276 is not supplied."]

## M7-06 — model_only

How does Alzheimer disease type 1 connect to Alzheimer disease through the recorded disease hierarchy?

### Unchanged generated prose

Alzheimer disease type 1 is generally treated as a specific form of Alzheimer disease, so the likely hierarchy is “Alzheimer disease type 1 → Alzheimer disease.” No recorded disease hierarchy was supplied, so the exact recorded relationship cannot be verified. This is an unverified development control, not clinical advice.

### Structured claims

Unanswered fields (model-generated; not a human abstention score):
["What exact parent–child relationship does the recorded disease hierarchy specify?"]

## M7-06 — retrieval

How does Alzheimer disease type 1 connect to Alzheimer disease through the recorded disease hierarchy?

### Unchanged generated prose

The recorded parent-navigation path is Alzheimer disease type 1 (MONDO:0007088) → early-onset autosomal dominant Alzheimer disease (MONDO:0015140) → familial Alzheimer disease (MONDO:0100087) → Alzheimer disease (MONDO:0004975). Each arrow represents a source-reported immediate parent step, not a separately verified biological relationship.

### Structured claims

1. Candidate interpretation requiring review: this records the immediate parent of Alzheimer disease type 1 as early-onset autosomal dominant Alzheimer disease.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/HierarchyStep/9dbc4821c39c5ceb692fc73095131c200359c653dfc6ce0a0b355fadb756b8f8> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#parentReference> <https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/bcd3ca8a4dfbf567bb35be1b516ad2278c40cc18254bcb2e6cd4cf75870edd80> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/HierarchyStep/9dbc4821c39c5ceb692fc73095131c200359c653dfc6ce0a0b355fadb756b8f8`

2. Candidate interpretation requiring review: this records familial Alzheimer disease as the next immediate parent.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/HierarchyStep/677460eea8f681aaa0de334dc1973cfea6d9552515da4d0d8aab9a6c94ec73a3> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#parentReference> <https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/8f1c74a3739d161dc1d7e3ec70e5de9d2ca810daf052041b5e2d6695d0c5168e> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/HierarchyStep/677460eea8f681aaa0de334dc1973cfea6d9552515da4d0d8aab9a6c94ec73a3`

3. Candidate interpretation requiring review: this records Alzheimer disease as the immediate parent of familial Alzheimer disease.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/HierarchyStep/e63bdc528cafa7ca08d8e902f71f4de3f96f826e5d4053778898020df9cc3850> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#parentReference> <https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/56e84bf4b4a25940c7a39128c743710b469a768016bee72e1e1f922fc4cff8db> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/HierarchyStep/e63bdc528cafa7ca08d8e902f71f4de3f96f826e5d4053778898020df9cc3850`

Unanswered fields (model-generated; not a human abstention score):
[]

## M7-07 — model_only

Does the graph show that MAPT causes any of the diseases connected to it, or does it only show that source evidence connects them?

### Unchanged generated prose

No graph or source evidence was supplied, so I cannot verify what its edges show. In general, a connection between MAPT and a disease indicates an asserted association supported by a source, not necessarily that MAPT causes the disease. Establishing causation would require evidence beyond the connection itself. This is an unverified development control, not clinical advice.

### Structured claims

Unanswered fields (model-generated; not a human abstention score):
["What do the graph's MAPT–disease edges represent, and what evidence supports each one?"]

## M7-07 — retrieval

Does the graph show that MAPT causes any of the diseases connected to it, or does it only show that source evidence connects them?

### Unchanged generated prose

The supplied graph records a disease–target association derived from a source evidence occurrence; it does not establish that MAPT causes the disease. The retrieved target is identified by an Ensembl ID, but these packets do not explicitly identify it as MAPT. This is a candidate interpretation of the records, not a reviewed biomedical conclusion.

### Structured claims

1. The association is recorded as derived from an evidence occurrence, rather than as a causal finding.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseTargetAssociation/7d73780492305001e5f0303ee2ab6c857629dc81e283452083ef5534f8746916> <http://www.w3.org/ns/prov#wasDerivedFrom> <https://github.com/subramanyaprasad21/dementia-kg-ai/id/EvidenceOccurrence/d8f5377a0c8887099512b7eed0c27dd998fc10147accc8836bdcbe58ddc56fcc> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseTargetAssociation/7d73780492305001e5f0303ee2ab6c857629dc81e283452083ef5534f8746916`

2. The association points to a disease reference; this link alone does not state biological causality.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseTargetAssociation/7d73780492305001e5f0303ee2ab6c857629dc81e283452083ef5534f8746916> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#hasDiseaseReference> <https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseConceptReference/57596fecb3d57365d5bf9a12d4f7dfa64a6956aaf93e55ff57babf878f62500f> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseTargetAssociation/7d73780492305001e5f0303ee2ab6c857629dc81e283452083ef5534f8746916`

3. The association points to a target; this link alone does not state biological causality.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseTargetAssociation/7d73780492305001e5f0303ee2ab6c857629dc81e283452083ef5534f8746916> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#hasTarget> <https://github.com/subramanyaprasad21/dementia-kg-ai/id/Target/ae58b26a9aed98f23b8c6143838acfd6c478a272fba179d3cd45f9b3c8df5962> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseTargetAssociation/7d73780492305001e5f0303ee2ab6c857629dc81e283452083ef5534f8746916`

4. The retrieved identifier for that target is an Ensembl ID; the packet does not supply a MAPT label.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/Target/ae58b26a9aed98f23b8c6143838acfd6c478a272fba179d3cd45f9b3c8df5962> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#externalIdentifier> "ENSG00000186868"^^<http://www.w3.org/2001/XMLSchema#string> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/DiseaseTargetAssociation/7d73780492305001e5f0303ee2ab6c857629dc81e283452083ef5534f8746916`

Unanswered fields (model-generated; not a human abstention score):
["Whether the retrieved target identifier denotes MAPT, based on an explicit identity statement in the supplied packets.", "Whether MAPT biologically causes any connected disease."]

## M7-08 — model_only

APP is connected to lecanemab's mechanism. Does that prove that lecanemab effectively treats Alzheimer's disease?

### Unchanged generated prose

No. APP is a precursor of amyloid-beta, and lecanemab targets aggregated amyloid-beta. That mechanistic connection does not, by itself, prove clinical benefit. Clinical efficacy must be evaluated in trials measuring outcomes in people with Alzheimer's disease. Based on model knowledge, a trial in early Alzheimer's disease reported a modest slowing of decline, alongside risks including amyloid-related imaging abnormalities; I cannot verify the evidence or its applicability here because no sources were supplied. This is an unverified development control, not clinical advice.

### Structured claims

Unanswered fields (model-generated; not a human abstention score):
["Which specific clinical evidence and patient population should be assessed?", "How should benefits and risks be weighed for the intended use?"]

## M7-08 — retrieval

APP is connected to lecanemab's mechanism. Does that prove that lecanemab effectively treats Alzheimer's disease?

### Unchanged generated prose

No. The retrieved mechanism record reports a target-related description, but that does not prove lecanemab effectively treats Alzheimer’s disease. The clinical-indication record reports an approval-stage label, not treatment outcomes. Efficacy cannot be determined from these packets.

### Structured claims

1. The mechanism record's source description; its clinical interpretation requires review.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/a413f6671dc36fa70a1079361b6b4236fb96a9e594c1785b40f8ee445869f6fb> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#sourceText> "Amyloid-beta A4 protein inhibitor"^^<http://www.w3.org/2001/XMLSchema#string> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/a413f6671dc36fa70a1079361b6b4236fb96a9e594c1785b40f8ee445869f6fb`

2. The record explicitly limits what can be inferred from its mechanism description.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/a413f6671dc36fa70a1079361b6b4236fb96a9e594c1785b40f8ee445869f6fb> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#limitationText> "Source gene-indexed mechanism; shared original row and molecular target context retained. No efficacy, gene-wide action or independent confirmation inferred."^^<http://www.w3.org/2001/XMLSchema#string> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/a413f6671dc36fa70a1079361b6b4236fb96a9e594c1785b40f8ee445869f6fb`

3. This is a source-reported stage label, not an efficacy result.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/ClinicalIndicationRecord/8d409cf761cbae391ba0ac03b3aee9046100d030f6779e9ecaad80c4cd11815b> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#trialPhaseText> "APPROVAL"^^<http://www.w3.org/2001/XMLSchema#string> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/ClinicalIndicationRecord/8d409cf761cbae391ba0ac03b3aee9046100d030f6779e9ecaad80c4cd11815b`

4. The indication record states that efficacy information was not acquired.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/ClinicalIndicationRecord/8d409cf761cbae391ba0ac03b3aee9046100d030f6779e9ecaad80c4cd11815b> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#limitationText> "Source maximum indication stage only. Report locators retained in the linked source description; registry population/status and efficacy not acquired."^^<http://www.w3.org/2001/XMLSchema#string> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/ClinicalIndicationRecord/8d409cf761cbae391ba0ac03b3aee9046100d030f6779e9ecaad80c4cd11815b`

Unanswered fields (model-generated; not a human abstention score):
["Whether and to what extent lecanemab improves clinical outcomes in people with Alzheimer’s disease."]

## M7-09 — model_only

If two evidence records mention two different targets, can they automatically be treated as two independent confirmations?

### Unchanged generated prose

No. Different targets do not automatically make two evidence records independent confirmations. The records could share a dataset, experimental methods, authors, or an underlying source, and they may support different claims. Independence requires checking their provenance and what each record actually establishes. No records were supplied, so this cannot be assessed here. This is an unverified development control, not clinical advice.

### Structured claims

Unanswered fields (model-generated; not a human abstention score):
["What are the two records, their sources, and their underlying data and methods?", "Do the records support the same specific claim?"]

## M7-09 — retrieval

If two evidence records mention two different targets, can they automatically be treated as two independent confirmations?

### Unchanged generated prose

No. Different targets do not automatically make two evidence records independent confirmations. In this packet, the two records name different targets, but a comparison record reports that both source rows reference the same study, nct00594737. That is a reason to review their provenance rather than count them as independent confirmations.

### Structured claims

1. Candidate interpretation requiring review: the first evidence record names one target.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/EvidenceOccurrence/7761d516706013aba8ffe20a7b45209f04fdbb1dbaf649cd6d51917a87dc6a80> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#hasTarget> <https://github.com/subramanyaprasad21/dementia-kg-ai/id/Target/f941f90f41909fda2dfefa50fe5c0d5a521a3b3c234dfd3f17cb845644b8da40> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/DerivedStatement/fd3db67ec6a05fdaa22d8c1407740e44cdbfc775cc25b2239bdfbd15268bd611`

2. Candidate interpretation requiring review: the second evidence record names a different target.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/EvidenceOccurrence/b845e08aa2a1a47ad4e331d75ff3b2cc86250fd2c13b82fee2d5044f02c769c6> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#hasTarget> <https://github.com/subramanyaprasad21/dementia-kg-ai/id/Target/95bd026992ad84a3133d0be3a8c3a64073536a4f13a344fdbe744b076668f051> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/DerivedStatement/fd3db67ec6a05fdaa22d8c1407740e44cdbfc775cc25b2239bdfbd15268bd611`

3. Candidate interpretation requiring review: the recorded comparison reports a shared study reference; it does not establish independence or clinical efficacy.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/DerivedStatement/fd3db67ec6a05fdaa22d8c1407740e44cdbfc775cc25b2239bdfbd15268bd611> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#resultSummary> "Both source rows reference nct00594737."^^<http://www.w3.org/2001/XMLSchema#string> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/DerivedStatement/fd3db67ec6a05fdaa22d8c1407740e44cdbfc775cc25b2239bdfbd15268bd611`

4. Candidate interpretation requiring review: the comparison explicitly limits its scope and disclaims an independence inference.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/DerivedStatement/fd3db67ec6a05fdaa22d8c1407740e44cdbfc775cc25b2239bdfbd15268bd611> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#scopeText> "Compare only these two source clinicalReportId fields; no independence or efficacy inference."^^<http://www.w3.org/2001/XMLSchema#string> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/DerivedStatement/fd3db67ec6a05fdaa22d8c1407740e44cdbfc775cc25b2239bdfbd15268bd611`

Unanswered fields (model-generated; not a human abstention score):
["Whether either target has an independent confirmation after review of the underlying studies and publications."]

## M7-10 — model_only

The GRIN1 and GRIN3B records are connected to a Phase 3 study, so does that mean memantine was proven clinically effective and safe for FTD?

### Unchanged generated prose

No. A connection between GRIN1 or GRIN3B records and a Phase 3 study does not establish that memantine was effective or safe for frontotemporal dementia (FTD). A study’s phase or a gene association is not a positive trial result. Based on general knowledge, memantine has not shown convincing clinical benefit in FTD, but I cannot verify the specific study, its outcomes, or its safety findings from the information supplied. This is an unverified development control, not clinical advice.

### Structured claims

Unanswered fields (model-generated; not a human abstention score):
["Which Phase 3 study do the GRIN1 and GRIN3B records refer to?", "What did that study report for FTD efficacy and adverse events?"]

## M7-10 — retrieval

The GRIN1 and GRIN3B records are connected to a Phase 3 study, so does that mean memantine was proven clinically effective and safe for FTD?

### Unchanged generated prose

No. The supplied records label the linked study as “PHASE_3,” but that label does not establish that memantine was effective or safe for frontotemporal dementia (FTD). The study-record text explicitly says it contains no acquired outcome or efficacy claim. The mechanism records also cannot establish a clinical result. These are candidate interpretations of the supplied records, not reviewed biomedical conclusions.

### Structured claims

1. Candidate interpretation requiring review: the study record reports a phase label, not a result.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/StudyRecord/37e85a901daeb16e42ea2391acb9e8d5f10a5bd9d378900a93bb156785f123db> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#trialPhaseText> "PHASE_3"^^<http://www.w3.org/2001/XMLSchema#string> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/StudyRecord/37e85a901daeb16e42ea2391acb9e8d5f10a5bd9d378900a93bb156785f123db`

2. Candidate interpretation requiring review: the record expressly limits what can be concluded about outcomes and efficacy.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/StudyRecord/37e85a901daeb16e42ea2391acb9e8d5f10a5bd9d378900a93bb156785f123db> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#limitationText> "OT clinical-report context only; arm and registry-version date absent. studyStartDate/publicationDate are not status dates. No acquired population, outcome, approval or efficacy claim."^^<http://www.w3.org/2001/XMLSchema#string> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/StudyRecord/37e85a901daeb16e42ea2391acb9e8d5f10a5bd9d378900a93bb156785f123db`

3. Candidate interpretation requiring review: the mechanism record itself cautions against inferring efficacy or independent confirmation.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/57e1f91585eea6d91f5772d3babe29fa1241ea3eaf722bbd535ce53135a114c1> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#limitationText> "Source gene-indexed mechanism; shared original row and molecular target context retained. No efficacy, gene-wide action or independent confirmation inferred."^^<http://www.w3.org/2001/XMLSchema#string> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/MechanismRecord/57e1f91585eea6d91f5772d3babe29fa1241ea3eaf722bbd535ce53135a114c1`

Unanswered fields (model-generated; not a human abstention score):
["Whether memantine was clinically effective for FTD; trial outcomes were not supplied.", "Whether memantine was safe for people with FTD; safety results were not supplied.", "Whether the linked study enrolled an FTD population or evaluated a particular treatment arm; those details were not acquired in the supplied study record."]

## M7-11 — model_only

Can the graph tell me the complete historical number of association or evidence records for PSEN1 and Alzheimer's disease?

### Unchanged generated prose

No. Without access to the graph or its underlying records, I cannot determine the complete historical number of association or evidence records linking PSEN1 and Alzheimer's disease. Even with graph access, the count would depend on which record types, sources, dates, and versions the graph includes. This is an unverified development control, not clinical advice.

### Structured claims

Unanswered fields (model-generated; not a human abstention score):
["What graph and record types are in scope?", "Does the graph retain historical, superseded, and deleted records?", "What is the count under a specified scope and time period?"]

## M7-11 — retrieval

Can the graph tell me the complete historical number of association or evidence records for PSEN1 and Alzheimer's disease?

### Unchanged generated prose

No. The supplied packets do not establish a complete historical number of association or evidence records for PSEN1 and Alzheimer's disease. The relevant selection is explicitly limited to enumerated IDs in Open Targets 26.06 and says it is not complete disease coverage or historical rankings. Any total for the requested pair remains unanswered.

### Structured claims

1. Candidate interpretation requiring review: the recorded scope rules out treating this selection as a complete historical count.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/SelectionContext/54a78318ada19754fa39f361ee17b4dc8fb05c7262cfdc9f5269f028463253ee> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#scopeText> "Only the enumerated recovered IDs with exact normalized MONDO_0004975 in OT 26.06; not complete disease coverage or historical rankings."^^<http://www.w3.org/2001/XMLSchema#string> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/SelectionContext/54a78318ada19754fa39f361ee17b4dc8fb05c7262cfdc9f5269f028463253ee`

Unanswered fields (model-generated; not a human abstention score):
["The complete historical number of association or evidence records for PSEN1 and Alzheimer's disease."]

## M7-12 — model_only

PSEN1 has evidence connected to Alzheimer's disease, and lecanemab has an Alzheimer's indication. Does that mean lecanemab can be given specifically because a patient has a PSEN1-related finding?

### Unchanged generated prose

No. A PSEN1-related finding and lecanemab’s Alzheimer’s indication do not, by themselves, establish that lecanemab should be given because of that finding. Treatment eligibility depends on the specific diagnosis, disease stage, confirmation of amyloid pathology, and the applicable prescribing criteria and safety assessment. Whether a particular PSEN1 variant changes the expected benefit or risk is uncertain; the finding alone is not a treatment indication. This is an unverified development-control answer, not clinical advice.

### Structured claims

Unanswered fields (model-generated; not a human abstention score):
["Which PSEN1 variant or finding is involved, and how is it classified?", "Does the patient meet the applicable lecanemab eligibility and safety criteria?", "What evidence, if any, establishes lecanemab’s benefit and risk specifically in patients with this PSEN1 finding?"]

## M7-12 — retrieval

PSEN1 has evidence connected to Alzheimer's disease, and lecanemab has an Alzheimer's indication. Does that mean lecanemab can be given specifically because a patient has a PSEN1-related finding?

### Unchanged generated prose

No. These packets record an Alzheimer’s disease indication for the drug and a separate PSEN1-related evidence occurrence, but they do not establish that a PSEN1 finding is itself a reason to give lecanemab. The indication record reports a maximum stage of “APPROVAL”; it does not supply patient eligibility, registry population or efficacy information. This is a candidate interpretation of the supplied records, not a treatment recommendation.

### Structured claims

1. The clinical-indication record links the drug to a disease reference. The supplied question identifies this drug as lecanemab; the statement itself uses a drug identifier.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/ClinicalIndicationRecord/8d409cf761cbae391ba0ac03b3aee9046100d030f6779e9ecaad80c4cd11815b> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#hasDrug> <https://github.com/subramanyaprasad21/dementia-kg-ai/id/Drug/268032fa0ce6c2abd6a7f4f9d967ff1a0a8ba35c235ddab3fe1bdcbdde8e69f5> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/ClinicalIndicationRecord/8d409cf761cbae391ba0ac03b3aee9046100d030f6779e9ecaad80c4cd11815b`

2. The record reports a trial-phase text value, not a PSEN1-specific eligibility rule.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/ClinicalIndicationRecord/8d409cf761cbae391ba0ac03b3aee9046100d030f6779e9ecaad80c4cd11815b> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#trialPhaseText> "APPROVAL"^^<http://www.w3.org/2001/XMLSchema#string> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/ClinicalIndicationRecord/8d409cf761cbae391ba0ac03b3aee9046100d030f6779e9ecaad80c4cd11815b`

3. The record expressly limits what was acquired about the indication.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/ClinicalIndicationRecord/8d409cf761cbae391ba0ac03b3aee9046100d030f6779e9ecaad80c4cd11815b> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#limitationText> "Source maximum indication stage only. Report locators retained in the linked source description; registry population/status and efficacy not acquired."^^<http://www.w3.org/2001/XMLSchema#string> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/ClinicalIndicationRecord/8d409cf761cbae391ba0ac03b3aee9046100d030f6779e9ecaad80c4cd11815b`

4. A separate evidence occurrence names the target represented in the question as PSEN1; this statement does not connect that finding to drug eligibility.

```text
<https://github.com/subramanyaprasad21/dementia-kg-ai/id/EvidenceOccurrence/4478fdd7719e8e57c23cb47c23442ff4622271b9be95dc50f1a2b1d439682a88> <https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#hasTarget> <https://github.com/subramanyaprasad21/dementia-kg-ai/id/Target/a5663e0cfac4822a46dbd160d6b8c857b70a982247a0ec326dadb865a970e3c6> .
```
Citation: `https://github.com/subramanyaprasad21/dementia-kg-ai/id/MappingRecord/ceefabe649d86c21686cb3476cd3cb58a2907701447958f54a81fa441e40677f`

Unanswered fields (model-generated; not a human abstention score):
["Whether a particular PSEN1 finding changes lecanemab eligibility or expected benefit.", "Whether the patient meets the applicable indication and other treatment requirements."]
