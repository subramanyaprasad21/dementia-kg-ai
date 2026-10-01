# Source feasibility audit

Task 005 reconciliation (no new source investigation): [D008](decisions/README.md#d008--source-roles), approved at Checkpoint 4, establishes Mondo disease reference/alignment, HPO as a later phenotype vocabulary and OT as a candidate major association/evidence source. Audited release numbers below are observations, **not frozen acquisition versions**. Earlier relationship recommendations are historical: target–drug mechanism and drug–disease indication are now approved core representation needs for Q06/Q07; broad phenotype comparison and process/pathway expansion are deferred. Exact artifacts, source eligibility, snapshots, import strategy and reuse permissions remain later gates. Existing evidence, counts and limitations below are unchanged.

Current review: [Task 004](#task-004-technical-source-review), 2026-09-17. Earlier sections are historical observations; their access/depth limitations are superseded only where Task 004 explicitly records new inspection. Scope freeze is approved at Checkpoint 4; source acquisition is not. M0 FROZEN / M1 ENTRY AUTHORIZED; no M1 work has begun. Earlier status statements remain dated audit history.

Task 002 inspection: 2026-09-16; Task 002A clarification: 2026-09-16–17 (Asia/Kolkata). Status: partial source verification, not source selection or acquisition approval. Recommendations are PROVISIONAL. No full datasets were downloaded. This audit inspected official documentation, release metadata, individual ontology records, small API responses, and HPO browser pages. Counts below are source observations, not experiment results or estimates of biomedical completeness.

## Source records

### Mondo Disease Ontology (Mondo / MONDO)

| Field | Finding |
| --- | --- |
| Authority / maintainer | Monarch Initiative's Mondo project; [official documentation](https://mondo.monarchinitiative.org/) and [repository](https://github.com/monarch-initiative/mondo). |
| Current release observed | [v2026-09-01](https://github.com/monarch-initiative/mondo/releases/tag/v2026-09-01), published 2026-09-01. EBI OLS reports the 2026-09-01 international edition. Neither is a selected project release. |
| Access / format | Official [download catalogue](https://mondo.monarchinitiative.org/pages/download/) lists OWL, OBO, and JSON products; OLS offers individual term metadata. No ontology file acquired. |
| Licence / redistribution | Official documentation identifies CC BY 4.0. Preserve attribution and applicable licence/change information when selecting artifacts; linked third-party databases are not acquired or licensed merely through an xref. |
| Identifier system | MONDO numeric identifiers and persistent OBO IRIs; source cross-references carry distinct mapping qualifications. |
| Entity / relationship types | Disease concepts, labels, scoped synonyms, classification relationships, and annotated external mappings. These are not automatically disease–phenotype observations or causal disease relations. |
| Evidence / provenance | Definition references, mapping annotations, term-tracker references, and release metadata were visible in sampled OLS records. Completeness across a chosen module is NOT YET VERIFIED. |
| Update frequency | Releases are available; a guaranteed schedule is NOT YET VERIFIED. |
| Overlap | EFO incorporates Mondo disease content; Open Targets also consumes Mondo-related content. These are dependent representations, not independent evidence. |
| Limitations | Portal and downstream snapshots can differ. A plain xref is not sufficient evidence for equivalence. Broad diseases, subtypes, susceptibility entities, and phenotype concepts need separate review. |
| Expected question coverage / reason | Disease identity, synonym scope, parent/subtype distinctions, and mapping provenance. Candidate disease reference backbone. |
| Verification status | Four non-obsolete disease records and release metadata verified; import product, mapping strategy, and scope not selected. |

Mondo's [mapping FAQ](https://mondo.monarchinitiative.org/pages/faq/) and product documentation distinguish mappings and ontology editions. A projection using only labels/xrefs would discard distinctions the project may need to test.

### Human Phenotype Ontology (HPO)

| Field | Finding |
| --- | --- |
| Authority / maintainer | Human Phenotype Ontology Consortium; [official site](https://hpo.jax.org/), [documentation](https://obophenotype.github.io/human-phenotype-ontology/), and [repository](https://github.com/obophenotype/human-phenotype-ontology). The site identifies Jackson Laboratory and Berlin Institute of Health affiliations. |
| Current release observed | Ontology release [v2026-09-01](https://github.com/obophenotype/human-phenotype-ontology/releases/tag/v2026-09-01), published 2026-09-03. The annotation snapshot served by the browser is NOT YET VERIFIED; its displayed application version 2.1.4 is not an ontology/annotation release. |
| Access / format | Browser, ontology OWL/OBO/JSON products, and tab-separated phenotype.hpoa annotations. Ontology and annotations are separate artifacts; see [product catalogue](https://obofoundry.org/ontology/hp) and [annotation specification](https://obophenotype.github.io/human-phenotype-ontology/annotations/phenotype_hpoa/). |
| Licence / redistribution | The current [HPO licence page](https://hpo.jax.org/license), inspected in the browser, requires acknowledgement/citation and public version/date information, and says HPO file content/logical relationships must not be altered. It also requests a service acknowledgement. Direct redistribution/transformation of a chosen artifact needs artifact-specific review; do not describe direct HPO reuse as unrestricted CC0. |
| Identifier system | HP identifiers describe phenotypes. Disease annotation identifiers can be MIM/OMIM, ORPHA, or MONDO; similar labels do not establish identical disease scope. |
| Entity / relationship types | Phenotypic abnormalities and their hierarchy; disease-feature annotations; separate gene-related annotation products exist but are not selected. |
| Evidence / provenance | phenotype.hpoa supports reference, evidence code, onset, frequency, sex, modifiers, aspect, biocuration, and a negation qualifier. Preserve qualifiers and source disease identity. |
| Update frequency | A fixed ontology/annotation cadence is NOT YET VERIFIED. Do not infer it from one release. |
| Overlap | Open Targets reuses HPO annotations; HPO disease records link to source databases and Mondo. Duplication must not be counted as independent corroboration. |
| Limitations | Coverage at a genetic/subtype record does not establish coverage for the whole dementia family. Browser search is not an exhaustive file-level audit. Current annotation documentation flags additional OMIM reuse requirements for IEA-derived annotations. |
| Expected question coverage / reason | Source-qualified phenotype retrieval, phenotype hierarchy, annotation provenance, and eventual comparison where coverage and permission permit. |
| Verification status | Ontology release, formats, licence page, annotation semantics, an FTD subtype page, and a vascular search checked. Complete four-disease annotation coverage and redistributable subset remain NOT YET VERIFIED. |

The [annotation specification](https://obophenotype.github.io/human-phenotype-ontology/annotations/phenotype_hpoa/) distinguishes PCS, TAS, and IEA evidence and mentions contacting OMIM for reuse of IEA annotations in other software products. Open Targets' licence table separately labels HPO CC0. These are different statements about different distribution routes. This audit does not resolve that discrepancy into a blanket legal conclusion.

### Open Targets Platform

| Field | Finding |
| --- | --- |
| Authority / maintainer | Open Targets; [official Platform documentation](https://platform-docs.opentargets.org/) and [Platform](https://platform.opentargets.org/). |
| Current release observed | Live API reports year 26, month 06, iteration null. [Release notes](https://platform-docs.opentargets.org/release-notes) identify 26.06, released 24 June 2026. Not frozen for this project. |
| Access / format | [GraphQL API](https://platform-docs.opentargets.org/data-access/graphql-api) for bounded queries; [partitioned Parquet downloads](https://platform-docs.opentargets.org/data-access/datasets) for systematic work, with archives and cloud/BigQuery options. Current documentation says pipeline outputs are no longer JSON files; API responses are JSON. |
| Licence / redistribution | [Official licence](https://platform-docs.opentargets.org/licence) marks Platform data CC0 1.0 and code Apache 2.0; it states listed providers agreed to unrestricted use by Platform users. This does not independently license upstream files or publication full text acquired elsewhere. Preserve original source and distribution-route information. |
| Identifier system | EFO/OTAR disease scaffold with multiple retained namespaces; all four sampled disease IDs are MONDO IDs. Ensembl gene IDs identify targets; sampled drugs use ChEMBL IDs. |
| Entity / relationship types | Disease/phenotype, target, drug, variant, study, evidence, associations, and clinical reports/indications. The audit does not propose importing every entity type. |
| Evidence / provenance | Evidence IDs, datasourceId, datatypeId, original identifiers where present, literature references, source-specific fields, and clinical-report sources/URLs. Samples confirm some fields can be null or empty. |
| Update frequency | Official overview documents quarterly updates. Downstream source versions differ; platform release is not a common release date for every constituent source. |
| Overlap | Incorporates EFO/Mondo, HPO, and other upstream resources. Its association scores and phenotype rows cannot independently validate those inputs. |
| Limitations | Associations are heterogeneous; scores are not calibrated confidence or causal proof. Descendant propagation changes coverage. Drugs/clinical candidates are not equivalent to effective or currently approved treatments. Phenotype coverage is uneven. |
| Expected question coverage / reason | Source-qualified disease–target evidence, direct/indirect distinctions, comparative retrieval, and optional drug-mechanism paths. Inclusion is justified by observed coverage, not by prior T2DM use. |
| Verification status | Four disease records, aggregate counts, small evidence/phenotype samples, and one drug-mechanism record checked. Post-filter usable coverage, complete provenance, and pairwise target overlap are NOT YET VERIFIED. |

The [association documentation](https://platform-docs.opentargets.org/associations) defines direct versus descendant-inclusive evidence and warns against interpreting scores as confidence. The [target documentation](https://platform-docs.opentargets.org/target) explains its gene-based representation and limitations for complexes. The [clinical-indication documentation](https://platform-docs.opentargets.org/disease-or-phenotype/drugs) describes aggregation across reports and stages, including a rule that can assign an approval maximum to withdrawal-related records. Preserve that meaning rather than writing an unqualified “treats” relation.

### Justified additional dependencies, not source expansion commitments

| Field | Experimental Factor Ontology (EFO) | Gene Ontology (GO), deferred candidate |
| --- | --- | --- |
| Authority / location / maintainer | [EFO repository](https://github.com/EBISPOT/efo); EMBL-EBI Samples, Phenotypes and Ontologies Team. | [GO documentation](https://geneontology.org/docs/ontology-documentation/); Gene Ontology Consortium. |
| Release observed | [v3.94.0](https://github.com/EBISPOT/efo/releases/tag/v3.94.0), published 2026-09-15. Exact EFO/OTAR version inside OT 26.06: NOT YET VERIFIED. | Current release: NOT YET VERIFIED; not required for the proposed initial scope. |
| Access / formats | Repository releases, OWL, OLS. Exact project artifact deferred. | [Annotation downloads](https://geneontology.org/docs/download-go-annotations/) document GAF and GPAD/GPI plus matching ontology files; no files acquired. |
| Licence / redistribution | OT's licence table reports Apache 2.0 for EFO. Direct artifact and imported-content terms: NOT YET VERIFIED; no import proposed now. | [GO terms](https://geneontology.org/docs/go-citation-policy/) license Consortium data/products under CC BY 4.0, require attribution for public use/redistribution, and request release identification. Software has separate licences. Terms of any separately acquired upstream distribution remain NOT YET VERIFIED. |
| IDs / entities | EFO IDs plus imported MONDO/other IDs; diseases, traits, measurements, experimental factors. | GO IDs; biological process, molecular function, cellular component; annotation subjects are gene products. |
| Relations / provenance | Hierarchy and mappings; imported identifiers and release provenance. Per-mapping evidence must be checked. | [Gene-product annotations](https://geneontology.org/docs/go-annotations/) carry relations, references, and evidence codes; negation matters. |
| Update frequency | NOT YET VERIFIED. | Fixed cadence NOT YET VERIFIED. |
| Overlap / limits | Already part of OT; EFO and Mondo snapshots are not interchangeable. Latest standalone EFO cannot be presumed to reproduce OT 26.06. | OT exposes GO annotations via UniProt; a second acquisition could duplicate content. Normal gene-product function does not establish a disease mechanism. |
| Question coverage / reason | Required to interpret the OT hierarchy and legacy mappings, not to broaden domain scope. | Only needed if an approved question asks about gene-product function/process membership; the proposed core does not require it. |
| Verification status / recommendation | Dependency verified; investigate alignment, no independent import selected. | Capability documented; density and artifact audit incomplete; DEFER. |

No independent drug database, literature corpus, pathway database, or provenance vocabulary is selected. OT exposes drug-mechanism and evidence metadata sufficient to investigate those requirements. Reactome, UniProt, ChEMBL, OMIM, and Orphanet appear as upstream sources or identifiers here, not independently approved acquisitions. A provenance vocabulary needs a later requirements-led comparison; source attribution fields do not choose that model.

## Disease identifiers and observed coverage

Each Mondo identifier below resolved as non-obsolete in EBI OLS's Mondo 2026-09-01 edition. Source: [OLS Mondo metadata](https://www.ebi.ac.uk/ols4/api/ontologies/mondo); term lookup uses `/ols4/api/ontologies/mondo/terms?obo_id=MONDO:NNNNNNN`. These verify source records, not adoption or a final equivalence policy.

| Candidate | Mondo record | OT 26.06 identifier | OT phenotype rows | Distinct target IDs in OT direct associations | Distinct target IDs with descendant inclusion | Drug/clinical-indication count |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| Alzheimer's disease | [MONDO:0004975 — Alzheimer disease](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:0004975) | MONDO_0004975 | 17 | 13,289 | 13,367 | 440 |
| Source-defined Lewy body dementia candidate | [MONDO:0007488 — Lewy body dementia](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:0007488) | MONDO_0007488 | 7 | 1,306 | 1,306 | 21 |
| Vascular dementia | [MONDO:0004648](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:0004648) | MONDO_0004648 | 0 | 808 | 828 | 17 |
| Frontotemporal dementia | [MONDO:0017276](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:0017276) | MONDO_0017276 | 0 | 2,454 | 3,113 | 20 |

These are API aggregate counts with no user-supplied eligibility filters; platform defaults still apply. Task 002A reproduced every table value in OT 26.06. The field-specific interpretation below supersedes the shorthand “direct associated targets”. Target counts include heterogeneous evidence, not just well-supported genetic associations. Phenotype counts are returned rows, not validated unique resolvable phenotypes. Indication counts are not approved-drug counts or drug–target edge counts. No complete target lists or pairwise intersections were acquired. Retained density after evidence-quality and scope filtering is NOT YET VERIFIED.

The following documents the read-only count query against the [official API](https://api.platform.opentargets.org/api/v4/graphql), not an ingestion implementation. Version check: `meta { dataVersion { year month iteration } }`.

```graphql
query Coverage($id: String!) {
  disease(efoId: $id) {
    id
    name
    phenotypes(page: {index: 0, size: 1}) { count }
    direct: associatedTargets(enableIndirect: false, page: {index: 0, size: 3}) {
      count
      rows { target { id approvedSymbol } score }
    }
    indirect: associatedTargets(enableIndirect: true, page: {index: 0, size: 1}) { count }
    drugAndClinicalCandidates { count }
  }
}
```

Executed requests used inline IDs rather than variables, and also selected parents, children, and scoped synonyms. No custom source weights, score threshold, or datasource filters were supplied. Schema introspection resolved current field names. An initial search using argument `query` failed validation; corrected `queryString` requests succeeded. Failed queries supplied no coverage evidence.

The broader dementia record MONDO_0001627 returned seven immediate children, including hereditary dementia, AIDS dementia complex, and childhood-onset dementia; direct versus descendant-inclusive target counts were 3,089 versus 14,795. Thus “all descendants of dementia” would not mean only the four adult candidates. These observations describe OT's hierarchy, not an asserted canonical Mondo closure. A broader neurodegenerative closure was not enumerated.

### Task 002A: count semantics and reproducibility

All twelve requested values reproduced on 2026-09-16 using the `Coverage` query above, with each listed OT identifier supplied as `$id`. The descendant-inclusive comparison values also reproduced unchanged. Transport: HTTP POST, `Content-Type: application/json`, body `{"query": "<Coverage query above>", "variables": {"id": "MONDO_0007488"}}` (substitute each table ID). Endpoint: `https://api.platform.opentargets.org/api/v4/graphql`. `meta.dataVersion` again returned year `26`, month `06`, iteration `null`. No bulk dataset was queried or downloaded.

| Field and all four values (AD / LBD record / vascular / FTD) | One row and count unit | Duplicates / uniqueness | Descendants and filtering | Suitability for comparing coverage |
| --- | --- | --- | --- | --- |
| `phenotypes.count`: **17 / 7 / 0 / 0** | Length of the stored disease record's `phenotypes` array before pagination. A row is a disease–phenotype entry containing a phenotype identifier and a nested evidence list. It is not one publication, patient, or individual evidence assertion. | The API count is array length, not a distinct-identifier operation. Query-time deduplication is absent; repeated nested evidence was observed in Task 002. Uniqueness of all top-level entries and upstream grouping guarantees are NOT YET VERIFIED. HPO/EFO resolution can differ. | Exact stored disease key is queried; no query-time descendant expansion or `enableIndirect` argument. Upstream mapping/propagation into that stored record is NOT YET VERIFIED. Only page index 0/size 1 supplied; no evidence-code, negation, frequency, subtype, or source filter. | Useful as a diagnostic of this endpoint's stored coverage. Unsuitable as comparable counts of clinical symptoms, usable annotations, or disease completeness. Zero is endpoint absence, not clinical absence or absence at subtypes. |
| `associatedTargets(enableIndirect:false).count`: **13,289 / 1,306 / 808 / 2,454** | Distinct target IDs participating in aggregated associations for the fixed disease. One returned row is one target–disease association with aggregate score/components, summarizing potentially many evidence records and sources. For a fixed disease, target IDs and distinct target–disease pairs coincide. | Public API implementation constructs a set of matching target IDs for `count`; repeated evidence does not add another target count. Multiple identifiers referring to biologically related entities are not thereby reconciled. No complete returned target list was independently enumerated. | Explicit `enableIndirect:false` disables OT descendant inclusion. It does not undo upstream disease normalization/mapping. No target list, text/facet filters, datasource selection, custom weights, or score threshold supplied; platform defaults remain. Page size 3 changes returned sample, not count. | Comparable as unfiltered OT direct-association breadth under the same release/parameters only. Not a measure of causal genes, evidence quality, independent support, or scientific usefulness. |
| `drugAndClinicalCandidates.count`: **440 / 21 / 17 / 20** | Number of returned Clinical Indications records. By documented dataset semantics, each consolidates reports for a drug–disease pair, with indication ID and maximum stage. Not a clinical-report, trial, publication, mechanism-edge, or approved-drug count. | Intended uniqueness is drug–disease pair; resolver counts returned rows without `DISTINCT`. Duplicate upstream rows would be counted. Completeness/uniqueness of all four lists and drug entity resolution are NOT YET VERIFIED; do not relabel as verified unique drugs. | Resolver selects the fixed disease ID, with no query-time descendant expansion. Upstream mappings/propagation are NOT YET VERIFIED. No arguments/approval-stage/source filter. Published code uses an internal 3,000-row limit and reports returned length; these observed values are below that limit. | Coarse inventory of represented drug–disease indications, not comparable therapeutic efficacy, approvals, trial volume, or usable drug–target coverage. |

The separate `enableIndirect:true` values **13,367 / 1,306 / 828 / 3,113** count distinct targets after eligible evidence from the queried disease and descendants is considered; they do not count descendants, evidence records, or a sum of per-descendant targets. Datasource propagation rules still apply. Equality of LBD counts does not demonstrate clinical completeness.

Verification layers:

- Live introspection checked `Disease`, `DiseaseHPOs`, `AssociatedTargets`, and `clinicalIndicationsFromDiseaseImp`. The phenotype schema says “annotations”, but its nested row structure and count implementation show why that word must not be read as individual evidence assertions.
- [Official association documentation](https://platform-docs.opentargets.org/associations) defines one association per unique disease–target pair. [Clinical-indication documentation](https://platform-docs.opentargets.org/disease-or-phenotype/drugs) defines aggregation of reports into drug–disease records.
- Read-only inspection of official API source at commit [`018afc7b8f439b456045ea1dc3544c70af0d86bd`](https://github.com/opentargets/platform-api/tree/018afc7b8f439b456045ea1dc3544c70af0d86bd) checked [Backend.scala](https://github.com/opentargets/platform-api/blob/018afc7b8f439b456045ea1dc3544c70af0d86bd/app/models/Backend.scala) (`getDiseaseHPOs`, `getAssociationsEntityFixed`, `getAssociationsDiseaseFixed`, `getClinicalIndications`), [OneToManyQuery.scala](https://github.com/opentargets/platform-api/blob/018afc7b8f439b456045ea1dc3544c70af0d86bd/app/models/db/OneToManyQuery.scala), [Objects.scala](https://github.com/opentargets/platform-api/blob/018afc7b8f439b456045ea1dc3544c70af0d86bd/app/models/gql/Objects.scala), and [Pagination.scala](https://github.com/opentargets/platform-api/blob/018afc7b8f439b456045ea1dc3544c70af0d86bd/app/models/entities/Pagination.scala). Association count uses `assocIds.toSet.size` before response pagination; its preliminary lookup also has a 100,000-row cap, above these observed totals. Exact correspondence between that public source commit and the deployed service build is NOT YET VERIFIED. Implementation observations are corroboration, not a deployment attestation.
- A bounded live query `disease(efoId:"MONDO_0007488") { associatedTargets(enableIndirect:false,page:{index:0,size:1}) { datasources { id weight propagate required } } }` returned default overrides: europepmc/expression_atlas/impc weight 0.2; cancer_biomarkers/ot_crispr_validation/ot_crispr/encore weight 0.5. Every returned setting had `required:false`; expression_atlas had `propagate:false`, the others true. This is the returned settings list, not an exhaustive list of evidence sources. No owner-defined eligibility filter has been applied.

No new biological coverage metric is introduced. No pairwise overlap, retained high-quality target count, or balanced phenotype count is inferred. The previous term “direct associated targets” was directionally correct under OT semantics but underspecified; use **distinct target IDs in OT direct associations (descendant inclusion disabled)**.

### Task 002A: exact candidate boundaries

Source record inspection: OLS Mondo 2026-09-01 individual term records and linked `/parents` and `/children` endpoints; OT 26.06 `disease(efoId:...) { id name description synonyms { relation terms } parents { id name } children { id name } }`. These are source-specific hierarchy observations, not clinical diagnostic rules.

| Concept | Exact source identity and relevant relationships | Proposed project meaning, if later selected |
| --- | --- | --- |
| Alzheimer anchor | Mondo `MONDO:0004975`, OT `MONDO_0004975`, label **Alzheimer disease**. | Fixed source anchor; no automatic inclusion of every familial/subtype record. Keep original disease labels/IDs on mapped evidence. |
| LBD candidate | Mondo `MONDO:0007488`, OT `MONDO_0007488`, label **Lewy body dementia**. Both return parents `MONDO:0001627` dementia and `MONDO:0000510` synucleinopathy. OLS children endpoint reports no children; OT returns an empty children list. | Source-defined MONDO:0007488 slice, with DLB lexical correspondence. NOT an automatically constructed umbrella of DLB plus Parkinson's disease dementia. It is not yet justified to label every mapped source assertion clinically DLB-specific. |
| DLB wording | OT puts **dementia with Lewy bodies**, **DLB**, **cortical Lewy body disease**, **Lewy body disease**, and **lewy body dementia, susceptibility to** in `hasExactSynonym` for MONDO_0007488. Mondo's OLS synonym list also contains these strings; its flat list alone does not preserve synonym scope. | These are lexical annotations on the same source concept, not separately observed parent/child nodes. Preserve source synonym scope, particularly susceptibility wording; do not use string synonymy to collapse clinical or genetic susceptibility assertions. |
| Related wording | OT puts **Lewy body variant of Alzheimer disease**, **dementia, Lewy body**, **diffuse Lewy body disease**, and **diffuse Lewy body disease with gaze palsy** in `hasRelatedSynonym`. OT additionally has exact **Senile dementia of the Lewy body type**, absent from the current OLS flat synonym list. | Related synonyms do not establish equivalence to Alzheimer disease, a mixed-pathology category, or another disease. Keep release-specific synonym sets separate. |
| Broader clinical LBD usage | NIH/NIA describes LBD as including dementia with Lewy bodies and Parkinson's disease dementia. That usage is broader than a project should infer from this source node's label and empty children list. A separate Parkinson's disease dementia mapping in the audited sources is NOT YET VERIFIED. | Parkinson's disease dementia, Parkinson disease, and all synucleinopathies remain outside the candidate boundary unless separately justified. An unsuccessful bounded OLS text search is not proof that no relevant concept exists. |
| FTD alternative | Mondo `MONDO:0017276`, OT `MONDO_0017276`, label **frontotemporal dementia**. Mondo synonyms include FTD, Frontotemporal degeneration, MSTD, frontotemporal lobe dementia (FLDEM). OT additionally calls frontotemporal lobar degeneration an exact synonym. | A source-defined disease-family anchor, not a uniform phenotype or a synonym for every frontotemporal clinical/pathological syndrome. Broad anchor versus named subtype remains undecided. |
| FTD hierarchy | OLS parents: hereditary dementia `MONDO:0015547`, inherited neurodegenerative disorder `MONDO:0024237`; OT also lists dementia `MONDO_0001627` as an immediate parent. Both list children: `MONDO:0000507` inclusion body myopathy with Paget disease of bone and frontotemporal dementia; `MONDO:0008243` Pick disease; `MONDO:0011842` GRN-related frontotemporal lobar degeneration with Tdp43 inclusions; `MONDO:0017160` behavioral variant of frontotemporal dementia. | Preserve source hierarchy and original subtype; do not infer that every clinical FTD case is inherited from these ontology parents, or automatically import all descendants. |
| Phenotype-bearing FTD subtype | HPO disease record ORPHA:275864 links to `MONDO:0017160`, **behavioral variant of frontotemporal dementia** in Mondo/OT hierarchy. Task 002 saw source-qualified annotations here. | Possible narrower candidate requiring a changed boundary. Its phenotype annotations cannot fill broad FTD's zero endpoint count by relabelling them. |

Official clinical context: [NIA LBD overview](https://www.nia.nih.gov/health/lewy-body-dementia/lewy-body-dementia-causes-symptoms-and-diagnosis) explicitly distinguishes the umbrella and two diagnoses in indexed text. Direct NIH page/PDF retrieval was blocked during Task 002A; only the relevant official indexed extracts were usable. Ontology labels, synonyms and relationships above were inspected directly via official APIs. Neither source is silently substituted for the other.

### Sample-level provenance and quality

Samples establish presence and possible failure modes, not prevalence. Evidence requests used `enableIndirect: false`, `size: 1`, and the target ID shown below. Source labels and references are observations, not independently validated biomedical conclusions.

| Disease / target sample | Observed evidence | Consequence |
| --- | --- | --- |
| Alzheimer / APP, ENSG00000142192 | ID `0523ee28e04113553d9d97cb17e7ec21909e75ba`; europepmc / literature; PMID 37569624; original disease fields null. | Literature-linked evidence exists; not every row supplies original disease identifiers. |
| Lewy body / SNCA, ENSG00000145335 | ID `18967be4401bc6cd7a2c0d52a05145b61e918b97`; genomics_england / genetic_literature; OMIM:127750; literature array empty. | Source-specific references and missing-PMID behavior need review. |
| Vascular / APOE, ENSG00000130203 | ID `7f1cc9f072d049b9cec19840d9d9ebf752f3feb0`; gwas_credible_sets / genetic_association; PMID 36653562. | Evidence exists even where phenotype rows are zero. |
| FTD / MAPT, ENSG00000186868 | ID `04e8f548c45ece0c2d428eef5f5aa149f67f1fbd`; genomics_england; original disease “Pick disease”, OMIM:172700; multiple literature IDs. | Even “direct” OT evidence may originate from a differently scoped source label; retain source mapping. |

Two phenotype rows per Alzheimer and Lewy body record were inspected using `phenotypes(page: {index: 0, size: 2})`, selecting `phenotypeHPO { id name }` and `evidence { resource diseaseFromSourceId evidenceType references qualifierNot bioCuration }`. Alzheimer samples included HPO annotations from OMIM:104300 and OMIM:608907, with PCS and TAS evidence respectively. Lewy body samples included IEA annotations from OMIM:127750, repeated identical evidence entries, and one null phenotypeHPO. Null HPO resolution does not prove the row lacks another representation; phenotypeEFO was not inspected in that sample. Do not silently deduplicate, discard, or repair these observations.

A small drug-list request for Lewy body dementia returned 21 indication rows; the first two inspected records were CHEMBL5095419/FOSGONIMETON and CHEMBL636/RIVASTIGMINE, both with `maxClinicalStage: UNKNOWN`. A separate `drug(chemblId: "CHEMBL636")` mechanism query returned inhibitor links to ACHE (ENSG00000087085) and BCHE (ENSG00000114200), with duplicate mechanism rows. This demonstrates drug–target availability, not efficacy, current approval, or complete mechanism provenance. Mechanism-reference fields exist in the schema but their completeness was not sampled.

Direct HPO browser inspection found [behavioral-variant FTD, ORPHA:275864](https://hpo.jax.org/browse/disease/ORPHA:275864), linked by the page to MONDO:0017160, with visible annotations such as disinhibition and memory impairment attributed to Orphanet. This narrower record must not be relabelled as broad FTD. The [vascular dementia search](https://hpo.jax.org/browse/search?q=vascular%20dementia&navFilter=all) returned zero disease results, alongside broad text-matching phenotype hits. Neither observation proves full-file or clinical absence. Complete current direct HPO coverage for each candidate remains NOT YET VERIFIED.

## Relationship-family assessment

Directions describe candidate question traversal, not proposed OWL properties. RETAIN means retain for design consideration, subject to source and scope approval. Density statements refer to observations or explicitly labelled uncertainty.

| Family / recommendation | Source, semantics and direction | Evidence model / density | Ambiguity and question value |
| --- | --- | --- | --- |
| Disease → Phenotype: INVESTIGATE FURTHER | HPO directly or through OT; disease record → annotated feature, not a universal symptom assertion. | Source disease, references, evidence type, qualifiers; OT rows 17/7/0/0, narrower FTD record visible directly. | Qualified comparisons and missingness; broad-family transfer, licence, duplicates and null resolution prevent making it mandatory core content yet. |
| Disease → Target/Gene: RETAIN | OT association connects disease and gene-indexed target; disease → target is traversal, not causal direction. | Source-specific association evidence; abundant but imbalanced counts above. Post-filter density unknown. | Shared/contrasting source-qualified associations and direct/propagated evidence. Not causation or target validation. |
| Target/Gene → Drug: INVESTIGATE FURTHER | Reverse traversal of drug → target mechanism/action in OT. | Mechanism/action and references where supplied; one drug linked to two targets observed, full density unknown. | Bounded multi-hop retrieval; associated target plus interacting drug does not establish treatment or repurposing success. |
| Target/Gene → Biological Process: DEFER | GO gene-product → process annotation; OT exposes GO via UniProt. | References/evidence codes/qualifiers; OT schema confirms aspect/evidence/geneProduct/source fields. Slice density NOT YET VERIFIED. | Functional grouping could be useful, but adds scope and gene/product distinctions; not a disease-specific causal pathway. |
| Disease → Evidence: INVESTIGATE FURTHER | Disease-to-bibliography navigation or view over associations, not generic support. | OT bibliography/evidence/clinical-report routes; disease-specific density not audited. | A paper mentioning a disease does not support every disease claim. Reject an unqualified “paper supports disease” meaning. |
| Association → Evidence: RETAIN | OT association → source records. | Evidence IDs, datasource/datatype, original identifiers and references; missing fields observed. Many-to-one aggregation, full density unknown. | Attribution, evidence-type distinctions, and missing/conflicting support. |
| Entity → Source/Provenance: RETAIN | Entity record → source release; claim/association → assertion source separately. | Source IDs, release and transformation lineage requirements. No local transformation records yet exist. | Identity attribution differs from claim support; universal completeness not demonstrated. |
| Disease → Disease hierarchy/relationship: RETAIN narrowly | Mondo classification and OT/EFO projection; subtype → parent. Mapping is separate. | Release-qualified assertions; finite local parents/children observed, broad closure unmeasured. | Hierarchy-aware retrieval and invalid generalization; reject generic relatedness and unrestricted descendant expansion initially. |

## Reuse and alignment boundary

Reference means using an external identifier with its source meaning; import brings ontology axioms into the reasoning context. Mapping/alignment relates representations; application extension adds only semantics needed by approved questions. These are separate choices.

| Resource | Reference | Import | Mapping/alignment | Application extension |
| --- | --- | --- | --- | --- |
| Mondo | Candidate disease anchors and scoped labels. | DEFER product/module choice until competency questions identify required inferences. | Review exact/close/other-hierarchy/obsolete qualifications and release compatibility; no automatic xref equivalence. | Only later evidence/source-assertion needs; do not recreate a medical taxonomy. |
| HPO | Candidate features and original annotations. | DEFER; annotation reuse and ontology import are separate questions. | Preserve OMIM/ORPHA disease granularity; do not equate similarly named disease and phenotype. | Later source qualifiers if needed, without editing HPO definitions. |
| EFO / OTAR | Retain OT IDs and source hierarchy context. | No whole-EFO import proposed. | Compare the exact OT scaffold with selected Mondo; common IDs do not guarantee common hierarchy/synonyms. | No extension justified now. |
| GO | Only if process questions survive. | DEFER. | Gene-to-product and qualified annotation handling required. | No extension proposed. |

Concrete warnings: Mondo marks Alzheimer xref HP:0002511 as `MONDO:otherHierarchy`; it must not become disease–phenotype equivalence. Its Orphanet:238616 xref is `equivalentObsolete`. Current Mondo FTD synonyms differ from OT 26.06, which includes frontotemporal lobar degeneration among its synonyms. Review rather than automatically union these records. The Lewy body record includes “dementia with Lewy bodies” as an exact synonym in OT; the Task 002A boundary table explains why this does not justify adopting the broader clinical LBD umbrella or asserting clinically pure DLB coverage. Anchor selection remains REQUIRES HUMAN DECISION.

## Open Targets reuse decision

Recommend OT conditionally for association evidence because all four anchors have observed target/indication coverage and samples expose provenance. It is not sufficient alone for balanced phenotype comparison. Reusing disease–target/drug extraction alone would be too close to the T2DM project described in the charter; its repository was not inspected during this task.

The proposed knowledge-level distinction is preserving source-scoped claims, direct/propagated status, original disease identity, mapping uncertainty, missingness, and drug-action versus indication semantics. These are requirements, not a designed ontology. The experimental distinction must be a controlled comparison of a specified retrieval or verification mechanism, including abstention and validator failures. Adding an LLM or changing the disease does not supply that distinction. Source diversity should increase only to satisfy an approved requirement.

## Remaining gates and audit limits

Before adoption: resolve the HPO artifact/distribution route and reuse terms; identify exact OT input ontology versions; choose source/evidence inclusion rules; assess usable coverage and cross-disease overlap after those rules; review disease/subtype boundaries and mapping qualifications; and check retained relationships' provenance completeness. No cutoff, publication list, annotation subset, import module, or mapping is approved.

Web extraction could not render several HPO/OLS pages; direct HPO browser inspection and bounded official OLS/API requests supplied the observations. Raw response files were not saved; queries, parameters, versions, identifiers, and salient observations above form the audit record. A future frozen acquisition must preserve actual artifacts/checksums under separate authorization. Live queries can change; this document is not a substitute for that snapshot.

## Task 003 matched sampling protocol — written before new examples

Date: 2026-09-17 (Asia/Kolkata). This protocol was recorded before Task 003 API example inspection. Task 002/002A examples were already known; this is prospective bounded follow-up, not blinded sampling or a preregistered experiment. All samples are DESIGN material. No owner scope choice or acquisition for a production KG is implied.

| Dimension | Fixed rule |
| --- | --- |
| Anchors | AD MONDO_0004975; source-defined LBD MONDO_0007488; broad FTD MONDO_0017276. No AD/LBD expansion. |
| Association | OT disease-fixed associatedTargets, enableIndirect:false, page index 0 size 3, explicit score-descending order; record release, IDs, scores and datasource scores. Rank by the platform aggregate, not by disease-specific handpicked genes. This favors well-ranked evidence and is not representative prevalence sampling. Ties retain API order and are disclosed. |
| Cross-disease probes | Union of the three sampled target sets (maximum nine IDs). Query that fixed union against each anchor using Bs with descendant inclusion disabled; maximum 27 association cells. Report only this bounded universe, never whole-disease overlap or biological exclusivity. |
| Evidence-source eligibility | Inspect exactly one returned record per association per stratum: genomics_england (curated genetic-literature assertions), gwas_credible_sets (genetic-association evidence), europepmc (literature evidence). Empty strata stay empty; no source substitution. These are audit strata, not approved KG inclusion rules. Other contributing sources remain visible in aggregate metadata but are not reviewed. |
| Evidence sample limit | Three own-anchor targets × three sources × three diseases = at most 27 records. Additionally inspect the lexicographically first shared target ID per pairing in both diseases, only if not already sampled: at most 12 more records. Evidence size 1, enableIndirect:false; preserve returned ID/order, no claim of stable tie order. |
| Reviewable minimum | Association: anchor and target IDs, retrieval release/settings. Source assertion: evidence ID, datasource/datatype, plus original disease identifier or retrievable study/publication/source locator. Missing disease granularity or publication text limits permissible conclusions; missing required fields are logged, not replaced. Metadata reviewability is distinct from adjudicated biological support. |
| Provenance | Preserve aggregate association separately from evidence ID, source disease ID/label, source-specific study/variant/URL when supplied, and publication IDs. Citation existence is not article review. Any derived comparison is labelled an audit calculation. |
| Duplicates | Retain observations and flag repeated record IDs or identical evidence payloads. Count an identical evidence ID only once within the same association/source stratum when summarizing inspected records; do not merge distinct assertions sharing a publication or target. No silent source repair. |
| Hierarchy diagnostic | Inspect immediate parents/children for each anchor. On its first-ranked target only, compare direct versus descendant-inclusive evidence counts and sample at most one evidence per selected stratum with enableIndirect:true (at most nine additional rows); never silently include descendants in the main sample. |
| FTD granularity exception | Inspect MONDO_0017160 (behavioral variant of FTD) separately because Task 002 identified HPO ORPHA:275864. One subtype only, not selected after Task 003 outcomes. Record direct parents/phenotypes and bounded first-target metadata if needed. This explicit extra FTD diagnostic is not part of matched three-anchor coverage or question-count advantages. |
| Phenotypes | First three stored entries per anchor, page 0 size 3; retain HPO and EFO resolution, source disease, qualifier, evidence code, frequency, reference and biocuration. Up to three additional entries for the predeclared bvFTD subtype. At most two nested evidence annotations per entry for manual review; retain truncation information. No replacing an empty broad anchor with its subtype. OT ordering is a returned prefix, not random or identifier-sorted population sampling. |
| Drug/path | For each of the nine own-anchor target slots, inspect first two known-drug rows if the live schema supports this, including disease identity and source metadata. Select at most two distinct drugs per disease from those rows (target rank then returned row order); inspect their mechanism/reference metadata, at most two mechanisms and two references per mechanism. Do not chase alternatives when no path occurs. Clinical indication and approval require their own explicit record; do not infer either from target connectivity. |
| Caps and deviations | At most nine core target samples, 27 cross-probe cells, 39 direct evidence records plus nine hierarchy-diagnostic records, 12 phenotype entries, 18 target/drug rows and six drug records. Schema discovery may precede requests; any unavailable field, unavoidable unpaginated response, cap breach, or changed rule must be disclosed. No process/pathway expansion. |
| Question gate | Draft questions only after reviewing resulting records. Require concrete evidence anchors and answer criteria; label CANDIDATE/REVISE/DEFER/REJECT. Assess memorization/vector alternatives explicitly; no graph-necessity or novelty claim. Count only proposed usable CANDIDATE records and identify template redundancy. No human review or held-out status is presumed. |

### Protocol clarification after schema inspection, before drug examples

OT 26.06 exposes `Target.drugAndClinicalCandidates`, not the proposed paginated `knownDrugs` field. Apply the same replacement field to all nine targets. Inspect its count first; retrieve minimal row metadata only if the count is at most 50 (otherwise defer that target's drug check). Retain only the first two returned rows per target for manual review and the predeclared two-drugs-per-disease cap. This can transmit more than 18 minimal rows because the field is unpaginated; report actual transmission separately from review sample size. No selection based on drug identity or indication is allowed. Nested phenotype evidence is likewise unpaginated: log array length and inspect only the first two annotations per entry. This is a transport asymmetry, not permission to expand the review sample.

Clinical-report clarification before indication examples: for each of the six mechanically selected drugs, inspect its indication identities/stages (each count is below 50). For provenance, inspect at most two reports from the exact sampled disease indication if present; otherwise from the first returned indication, explicitly labelled as another disease. Record transmitted report-ID counts separately if the API cannot paginate. A maximum-stage label alone is not a current jurisdiction-specific approval assessment. No extra drug selection follows this check.


## Task 003 evidence observations

### Execution and limits

Observed 2026-09-17, OT 26.06. Selection returned nine distinct seed target IDs, with no score tie at an own-anchor selection boundary visible in the three returned rows; unreturned boundary ties were not checked. Scores below are descriptive aggregates, not causal probabilities. Query-time directness is not original-source granularity. API rows and selected metadata are transcribed here; full raw datasets and responses are not repository artifacts. Live API ordering and upstream changes limit exact future reruns.

### T3-T: ranked association sample

Sources below list all nonempty datasource score components, not all independently reviewed evidence. Evidence inspection uses only the three predeclared strata.

| Anchor / rank | Target ID, symbol and approved name | Aggregate score | Contributing datasource IDs |
| --- | --- | ---: | --- |
| AD / 1 | ENSG00000142192; APP; amyloid beta precursor protein | 0.806512 | clinical_precedence, eva, gwas_credible_sets, reactome, europepmc |
| AD / 2 | ENSG00000176884; GRIN1; glutamate ionotropic receptor NMDA type subunit 1 | 0.700241 | clinical_precedence, crispr_screen, europepmc |
| AD / 3 | ENSG00000116032; GRIN3B; glutamate ionotropic receptor NMDA type subunit 3B | 0.680431 | clinical_precedence, gwas_credible_sets, europepmc |
| LBD / 1 | ENSG00000145335; SNCA; synuclein alpha | 0.741576 | eva, genomics_england, gwas_credible_sets, uniprot_variants, uniprot_literature, europepmc, impc |
| LBD / 2 | ENSG00000177628; GBA1; glucosylceramidase beta 1 | 0.640584 | eva, gwas_credible_sets, europepmc |
| LBD / 3 | ENSG00000130203; APOE; apolipoprotein E | 0.567491 | gwas_credible_sets, europepmc |
| FTD / 1 | ENSG00000186868; MAPT; microtubule associated protein tau | 0.789339 | uniprot_variants, eva, genomics_england, europepmc, impc, clinical_precedence |
| FTD / 2 | ENSG00000083937; CHMP2B; charged multivesicular body protein 2B | 0.759258 | uniprot_variants, eva, genomics_england, clingen, uniprot_literature, europepmc |
| FTD / 3 | ENSG00000080815; PSEN1; presenilin 1 | 0.698639 | eva, genomics_england, europepmc, impc |

### T3-X: fixed-universe cross-probe

Universe U is exactly the nine target IDs above. Query each anchor using `associatedTargets(Bs:U,enableIndirect:false,orderByScore:"score desc",page:{index:0,size:9}) { count rows { target { id approvedSymbol } score datasourceScores { id score } } }`. Every returned row fits this page. The following are aggregate source components, not a primary-evidence adjudication. Abbreviations: EP=europepmc; GE=genomics_england; GW=gwas_credible_sets; EV=eva; CP=clinical_precedence; EA=expression_atlas; CR=crispr_screen; IM=impc; UV=uniprot_variants; UL=uniprot_literature; CG=clingen; RE=reactome.

| Target | AD sources | LBD sources | FTD sources |
| --- | --- | --- | --- |
| PSEN1 | CP, EA, EP, EV | EP | EP, EV, GE, IM |
| CHMP2B | EA, EP | EP | CG, EP, EV, GE, UL, UV |
| GRIN3B | CP, EP, GW | No returned association | CP |
| APOE | CR, EA, EP, EV, GW | EP, GW | EP, GW |
| APP | CP, EP, EV, GW, RE | EP | EP, IM |
| SNCA | EA, EP | EP, EV, GE, GW, IM, UL, UV | EP |
| GRIN1 | CP, CR, EP | No returned association | CP |
| GBA1 | EP | EP, EV, GW | EP |
| MAPT | CP, EP, EV, GW | EP, GW | CP, EP, EV, GE, IM, UV |

Within U only: AD has 9 returned targets, LBD 7, FTD 9; AD∩LBD=7 and AD∩FTD=9. GRIN1/GRIN3B have no LBD result in this probe, but FTD records are CP-only. These are source coverage distinctions, not disease-exclusive genes. None of these sample intersections estimates full pairwise overlap. PSEN1 (ENSG00000080815) is the lexicographically first shared ID for both pairings and therefore the predeclared deeper comparison, not a post-hoc biological choice. Only two additional associations (AD/PSEN1, LBD/PSEN1) required evidence retrieval because FTD/PSEN1 was already sampled.

### T3-E: direct evidence inventory

For every row below, execute `disease(efoId:D) { evidences(ensemblIds:[T],datasourceIds:[S],enableIndirect:false,size:1) { count rows { id score datasourceId datatypeId diseaseFromSource diseaseFromSourceId diseaseFromSourceMappedId targetFromSourceId studyId literature releaseVersion releaseDate disease { id name } } } }`. D/T/S are the row's anchor, target ID from T3-T, and GE/GW/EP source. The two extra PSEN1 requests omitted release fields. Count is all matching source evidence records; only one row was inspected per nonempty cell. `—` means returned null/empty, not absence of real-world evidence.

| Anchor / target | Source | Matching evidence count | Inspected evidence ID | Original disease / source ID; study ID | Literature PMID(s) |
| --- | --- | ---: | --- | --- | --- |
| AD / APP | GE | 0 | — | — | — |
| AD / APP | GW | 8 | 2f93b64cbb69225b5005dfa288b557040d7cedd5 | —; —; study — | 34099642 |
| AD / APP | EP | 27380 | 0523ee28e04113553d9d97cb17e7ec21909e75ba | —; —; study — | 37569624 |
| AD / GRIN1 | GE | 0 | — | — | — |
| AD / GRIN1 | GW | 0 | — | — | — |
| AD / GRIN1 | EP | 108 | ce18396561e78f5d7b65b84446763462f34a7139 | —; —; study — | 39974092 |
| AD / GRIN3B | GE | 0 | — | — | — |
| AD / GRIN3B | GW | 3 | 102dba5856e74d30a5a9931a6e62afbd530dffc7 | —; —; study — | 40708016 |
| AD / GRIN3B | EP | 6 | dc52fc86fe355b5227138a9687d58e97023cc82b | —; —; study — | 20016182 |
| LBD / SNCA | GE | 3 | 18967be4401bc6cd7a2c0d52a05145b61e918b97 | Dementia, Lewy body; OMIM:127750; study 540 | — |
| LBD / SNCA | GW | 4 | 77a1915e0dbcdab8a5f5fbee114a7ae4a8ba77de | —; —; study — | 35729600 |
| LBD / SNCA | EP | 1455 | 2c511f01c07fb28b0312907859dddd9a17dff442 | —; —; study — | 40113786 |
| LBD / GBA1 | GE | 0 | — | — | — |
| LBD / GBA1 | GW | 2 | 1918dbbb4d632e674b0b5530a934f9b5a71fd39f | —; —; study — | 33589841 |
| LBD / GBA1 | EP | 333 | 388697dfab804a73433f5349dfad218d1f38ff61 | —; —; study — | 29948939 |
| LBD / APOE | GE | 0 | — | — | — |
| LBD / APOE | GW | 12 | ac380c2834568b7397bcc9fa605f563d92ae9405 | —; —; study — | 40374660 |
| LBD / APOE | EP | 348 | 348a4c70898c23b913c348cf8a9408e3f4811d91 | —; —; study — | 36123648 |
| FTD / MAPT | GE | 3 | 04e8f548c45ece0c2d428eef5f5aa149f67f1fbd | Pick disease; OMIM:172700; study 474 | 20301678, 28334843, 9641683, 9789048 |
| FTD / MAPT | GW | 0 | — | — | — |
| FTD / MAPT | EP | 4740 | 122d50b8a7a06485ff2be3f520db9876935b6b7d | —; —; study — | 32444551 |
| FTD / CHMP2B | GE | 2 | 223453935bbc9dec3e6e15dae46cfeb6fd756a0a | Frontotemporal Dementia; —; study 265 | — |
| FTD / CHMP2B | GW | 0 | — | — | — |
| FTD / CHMP2B | EP | 296 | a66373142d4fb76427db3216c49ca9611e06886f | —; —; study — | 37274831 |
| FTD / PSEN1 | GE | 5 | 98c49197e4989f7d3be8b2f8ee3c7699e2f3d6dc | Dementia, frontotemporal; OMIM:600274; study 265 | 22503161, 23028126 |
| FTD / PSEN1 | GW | 0 | — | — | — |
| FTD / PSEN1 | EP | 147 | 986bb22bf0f7858c36fc773e5b45c08cd9c514fd | —; —; study — | 31555645 |
| AD / PSEN1 | GE | 0 | — | — | — |
| AD / PSEN1 | GW | 0 | — | — | — |
| AD / PSEN1 | EP | 6929 | 1261ad02e3d662cd23a476af47159a1501d01889 | —; —; study — | 33008897 |
| LBD / PSEN1 | GE | 0 | — | — | — |
| LBD / PSEN1 | GW | 0 | — | — | — |
| LBD / PSEN1 | EP | 35 | fa93de0b443d3ba571a606f21f9455ec08d7e469 | —; —; study — | 38512130 |

All direct inspected records map to the requested anchor (`diseaseFromSourceMappedId` and resolved disease ID). GE uses datatype genetic_literature and source target symbols; GW uses genetic_association and Ensembl IDs; EP uses literature and Ensembl IDs. Every releaseVersion/releaseDate field requested in the own-anchor evidence sample was null. No repeated evidence IDs occurred across these direct sample cells. Shared publication identifiers would still not establish independent corroboration. Missing original disease fields remain explicit rather than being replaced with the normalized anchor.

The direct audit made 33 source-stratum checks and inspected 20 nonempty evidence rows. Empty cells were retained without substitution. These figures describe the audit, not a source-completeness metric. GE/CHMP2B lacks original disease ID and publication IDs; study 265 is present, but the source record could not be opened. Its upstream assertion is not independently reviewable in this run. Other sampled GE assertions have original identifiers; all inspected GW/EP records have publication locators, but that alone does not validate their claim support.

### T3-H: propagation diagnostic (separate from direct sample)

Same evidence query, setting `enableIndirect:true`, on rank-one APP, SNCA, MAPT only. Counts below include eligible descendant evidence; no descendant records are promoted into the main sample.

| Anchor / target | Source | Direct → inclusive count | First inclusive evidence ID | Mapped disease; original source; PMID(s) |
| --- | --- | --- | --- | --- |
| AD / APP | GE | 0 → 1 | 8bac3794c7e23d4dc3e7b44e3b2e1af8dcccc4fe | MONDO_0007088 Alzheimer disease type 1; OMIM:104300; 22503161, 2111584, 23028126 |
| AD / APP | GW | 8 → 10 | 268a5aeb14dd691e526c727a147550ce48b95328 | EFO_1001870 late-onset Alzheimers disease; —; 34493870 |
| AD / APP | EP | 27380 → 39221 | 0523ee28e04113553d9d97cb17e7ec21909e75ba | MONDO_0004975 Alzheimer disease; —; 37569624 |
| LBD / SNCA | GE | 3 → 3 | 18967be4401bc6cd7a2c0d52a05145b61e918b97 | MONDO_0007488 Lewy body dementia; OMIM:127750; — |
| LBD / SNCA | GW | 4 → 4 | 77a1915e0dbcdab8a5f5fbee114a7ae4a8ba77de | MONDO_0007488 Lewy body dementia; —; 35729600 |
| LBD / SNCA | EP | 1455 → 1455 | 2c511f01c07fb28b0312907859dddd9a17dff442 | MONDO_0007488 Lewy body dementia; —; 40113786 |
| FTD / MAPT | GE | 3 → 10 | 019b39b2b176f9e7df8536022682738d12e32f39 | MONDO_0010857 semantic dementia; OMIM:600274; 20301678, 28334843 |
| FTD / MAPT | GW | 0 → 0 | — | — |
| FTD / MAPT | EP | 4740 → 6462 | 122d50b8a7a06485ff2be3f520db9876935b6b7d | MONDO_0017276 frontotemporal dementia; —; 32444551 |

The AD GE diagnostic returns Alzheimer disease type 1 MONDO_0007088; the AD GW diagnostic returns late-onset AD EFO_1001870. These are expressly diagnostic inclusions, not an expanded AD core. The FTD GE diagnostic returns semantic dementia MONDO_0010857 from original OMIM:600274. Source-level granularity differs even without propagation: direct FTD/MAPT GE evidence says Pick disease, whereas its mapped disease is broad FTD. A narrow original label and a query-time propagated assertion are therefore different phenomena. LBD inclusive rows repeat the direct IDs. The diagnostic adds three new evidence IDs (two AD, one FTD); repetitions are not independent support. The exact ontology path to the returned semantic-dementia record has NOT YET BEEN VERIFIED here.

### T3-P: phenotype entries

Query: `disease(efoId:D) { id name parents { id name } phenotypes(page:{index:0,size:3}) { count rows { phenotypeHPO { id name } phenotypeEFO { id name } evidence { resource diseaseFromSourceId diseaseFromSource qualifierNot evidenceType frequency references bioCuration } } } }`. Preserve both resolutions; only first two nested annotations inspected per entry.

| Anchor | Phenotype resolution | Original disease; source | Negation / code / frequency | Reference / curation | Duplicate or boundary issue |
| --- | --- | --- | --- | --- | --- |
| AD | HPO: HP_0410054 Decreased circulating GABA concentration; EFO: null | OMIM:104300, Alzheimer disease; HPO | false; PCS; null | PMID:17031479; HPO:NicoleVasilevsky[2018-02-23] | One returned annotation |
| AD | HPO: HP_0002354 Memory impairment; EFO: null | OMIM:608907, Alzheimer disease 9, susceptibility to; HPO | false; TAS; null | OMIM:608907; HPO:skoehler[2017-07-13] | One returned annotation |
| AD | HPO: HP_0000734 Disinhibition; EFO: null | OMIM:608907, Alzheimer disease 9, susceptibility to; HPO | false; TAS; null | OMIM:608907; HPO:skoehler[2017-07-13] | One returned annotation |
| LBD | HPO: HP_0000746 Delusion; EFO: HP_0000746 Delusion | OMIM:127750, Dementia, lewy body; HPO | false; IEA; null | OMIM:127750; HPO:iea[2009-02-17] | Two identical inspected annotation payloads |
| LBD | HPO: null; EFO: MONDO_0001627 dementia | OMIM:127750, Dementia, lewy body; HPO | false; IEA; null | OMIM:127750; HPO:iea[2009-02-17] | Two identical inspected annotation payloads |
| LBD | HPO: HP_0001300 Parkinsonism; EFO: HP_0001300 Parkinsonism | OMIM:127750, Dementia, lewy body; HPO | false; IEA; null | OMIM:127750; HPO:iea[2009-02-17] | Two identical inspected annotation payloads |

Six OT entries were reviewed: three AD, three LBD; all nine nested annotation payloads were inspected. FTD and bvFTD OT counts are zero. AD's memory/disinhibition entries originate from an AD9 susceptibility record, not an unqualified all-AD assertion. The LBD row with null phenotypeHPO resolves to dementia MONDO_0001627 in phenotypeEFO; it is not an unresolvable entity and is not an HPO term. Three pairs of identical nested payloads do not provide six independent supports. All sampled OT frequency values are null. Query-time expansion is absent, but original-source mapping is evident; upstream propagation details are still NOT YET VERIFIED.

The separately predeclared [HPO ORPHA:275864 browser record](https://hpo.jax.org/browse/disease/ORPHA:275864) links bvFTD MONDO:0017160. In page order the first three entries were HP:0000474 Thickened nuchal skin fold (Very frequent), HP:0000734 Disinhibition (Very frequent), HP:0030212 Collectionism (Frequent), each linking ORPHA:275864. The unexpected first entry was retained, not silently corrected. This browser exposes frequency labels and source links, but annotation evidence code, negation, biocuration and exact annotation release were NOT YET VERIFIED. Do not interpret a missing displayed qualifier as false. The page renders additional entries; only the first three are part of the manual sample. No export was downloaded. The browser API attempt `getState` was unsupported; reselecting the observed tab supplied the page, with no data mutation.

HPO/OMIM and route-specific reuse concerns from Task 002 remain unresolved. Conclusion: phenotype comparisons stay DEFERRED as core scientific questions for both pairings. Metadata-quality/identity questions remain possible. Direct HPO and OT bvFTD disagree in availability; this is a distribution/mapping observation, not proof of biological absence or source error.


### T3-D: drug/mechanism and indication paths

The nine target count checks and minimal unpaginated drug-row calls transmitted 88 target–drug rows, of which the fixed first-two rule reviewed 14 (APOE and CHMP2B returned none). The reviewed prefixes were: APP—lecanemab/tramiprosate; GRIN1—ralfinamide/amantadine hydrochloride; GRIN3B—neboglamine/CNS-5161; SNCA—prasinezumab/cinpanemab; GBA1—afegostat/afegostat tartrate; MAPT—zagotenemab/gosuranemab; PSEN1—semagacestat/avagacestat. These are clinical-target records, not disease-specific efficacy assertions. The fixed two-drugs-per-disease selection chooses the APP, SNCA and MAPT prefixes, not additional drugs from lower-ranked targets.

Queries: `target(ensemblId:T) { id approvedSymbol drugAndClinicalCandidates { count rows { id maxClinicalStage drug { id name } } } }`; first count-only, then rows only when count ≤50. Mechanisms: `drug(chemblId:C) { id name indications { count } mechanismsOfAction { rows { mechanismOfAction actionType targetName targets { id approvedSymbol } references { source ids urls } } } }`. Each selected drug returned one mechanism row, within cap. All six mechanism rows were inspected; reference object counts were 1/1/2/0/1/1 in table order.

| Selected through | Drug ID / name | OT mechanism action / resolved target | Mechanism provenance | Selected-anchor indication and stage in OT 26.06 |
| --- | --- | --- | --- | --- |
| AD/APP | CHEMBL3833321 lecanemab | INHIBITOR / APP | PMID 25031633 | AD; APPROVAL; PMDA and TTD report metadata inspected |
| AD/APP | CHEMBL149082 tramiprosate | STABILISER / APP | PMIDs 19616185, 28435985 | AD; PHASE_3; TTD and AACT metadata inspected |
| LBD/SNCA | CHEMBL4298077 prasinezumab | BINDING AGENT / SNCA | Prothena source URL; PMIDs 27886407, 29913017 | No MONDO_0007488 record in this drug's returned indication list; Parkinson disease and Mental deterioration records present |
| LBD/SNCA | CHEMBL3833330 cinpanemab | INHIBITOR / SNCA | Empty references array | No MONDO_0007488 record in this drug's returned indication list; Parkinson disease record present |
| FTD/MAPT | CHEMBL4298021 zagotenemab | INHIBITOR / MAPT | PMID 33303932 | No MONDO_0017276 record in returned indication list; AD PHASE_2 and tauopathy UNKNOWN present |
| FTD/MAPT | CHEMBL3990042 gosuranemab | INHIBITOR / MAPT | PMIDs 30581980, 33303932 | FTD PHASE_1; AACT report NCT03658135; TERMINATED in report |

Mechanism references are supplied locators, not publications independently read in this task. Gene-indexed target resolution does not assert that every drug acts on every product/state of that gene. Do not generalize absence from these six drug records to an entire disease or the literature. No current regulatory-approval conclusion is drawn from a platform maximum stage.

Indication query: `drug(chemblId:C) { id name indications { count rows { id disease { id name } maxClinicalStage clinicalReports { id } } } }`. It returned 17 indication records and 61 nested report-ID occurrences; only ten report records selected by the clarification rule were read in detail. Report query: `clinicalReports(clinicalReportsIds:IDS) { id source url type clinicalStage phaseFromSource trialOverallStatus title diseases { diseaseFromSource disease { id name } } }`. The IDs and results below reproduce the inspected subset; the report-ID arrays were not treated as independent evidence totals.

| Drug / indication reviewed | Clinical report IDs | Source / stage / salient provenance |
| --- | --- | --- |
| lecanemab / AD | ae7c4bd51f55ba8bb141fe2e2243f73b3ef6ddb1e4fc300f9270391810b70030; d06xvr/alzheimer disease | PMDA regulatory report and TTD curated resource, both APPROVAL. PMDA URL is a generic approved-drugs index, not an inspected product-specific label. |
| tramiprosate / AD | d09dlp/alzheimer disease; nct00314912 | TTD PHASE_3; AACT PHASE_3, overall status UNKNOWN in OT. No efficacy conclusion. |
| prasinezumab / Mental deterioration | nct07055087 | AACT PHASE_2, NOT_YET_RECRUITING in OT; report also resolves Parkinson disease. Title identifies GBA-associated Parkinson's disease. Neither generic cognitive decline nor SNCA binding licenses an LBD indication. |
| cinpanemab / Parkinson disease | d0tu9w/parkinson disease; nct03318523 | TTD PHASE_2; AACT PHASE_2, TERMINATED. Target-drug stage and trial status are distinct. |
| zagotenemab / AD | nct03518073; d02dzk/alzheimer disease | AACT PHASE_2 COMPLETED; TTD PHASE_1. Aggregation has different contributing stages, not two contradictory efficacy findings. |
| gosuranemab / FTD | nct03658135 | AACT PHASE_1 TERMINATED. Original label frontotemporal lobar degeneration maps to MONDO_0017276; other syndromes and an unresolved traumatic-encephalopathy entry are present. |

Two primary registry lookups used `https://clinicaltrials.gov/api/v2/studies/NCT07055087` and `/NCT03658135`, without result-data analysis. [NCT07055087](https://clinicaltrials.gov/study/NCT07055087) lists Parkinson's disease, prasinezumab and placebo; last posted update 2025-07-08 and status NOT_YET_RECRUITING in the retrieved record. [NCT03658135](https://clinicaltrials.gov/study/NCT03658135) lists primary tauopathies including FTLD with tau inclusions, symptomatic MAPT mutation carriers and other syndromes; retrieved status TERMINATED, reason “BIIB092 program discontinued”, last posted update 2019-12-19. These are dated registry statements, not a fresh clinical assessment. Only one selected trial per second-anchor path was traced upstream; AD's selected PMDA/TTD records were not independently resolved. This depth asymmetry cannot be used to rank disease evidence quality.

### T3-R: publication/source tracing and provenance limits

For the mechanically selected shared PSEN1 target, looked up the one sampled EP publication per disease and the first PMID of the FTD GE sample. Europe PMC REST query: `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:PMID%20AND%20SRC:MED&format=json&resultType=core&pageSize=1` (URL-encode query; substitute PMID). Browser/web article rendering failed; the official REST records supplied titles, DOI and abstracts. Only abstracts/metadata were read, not full text. This is limited claim-support inspection, not scientific adjudication.

| Anchor / record | Primary publication locator | Inspection consequence |
| --- | --- | --- |
| AD/PSEN1 EP 1261ad02e3d662cd23a476af47159a1501d01889 | PMID 33008897; DOI [10.1126/sciadv.abc5802](https://doi.org/10.1126/sciadv.abc5802) | Abstract concerns AD brain glycoproteomics. The specific PSEN1–AD proposition is not established from that abstract alone. |
| LBD/PSEN1 EP fa93de0b443d3ba571a606f21f9455ec08d7e469 | PMID 38512130; DOI [10.7554/eLife.89368](https://doi.org/10.7554/eLife.89368) | Abstract spans multiple neurodegenerative conditions, including DLB and presenilin-1 mutation groups. Their mention does not itself establish PSEN1 causation of DLB. |
| FTD/PSEN1 EP 986bb22bf0f7858c36fc773e5b45c08cd9c514fd | PMID 31555645; DOI [10.3389/fcell.2019.00179](https://doi.org/10.3389/fcell.2019.00179) | Abstract is a broad review of autophagy/storage disorders. It does not by itself adjudicate a specific PSEN1–FTD claim. |
| FTD/PSEN1 GE 98c49197e4989f7d3be8b2f8ee3c7699e2f3d6dc | PMID 22503161; DOI [10.1016/j.neurobiolaging.2012.02.020](https://doi.org/10.1016/j.neurobiolaging.2012.02.020) | Abstract describes PSEN1/PSEN2 mutation/variant screening in a dementia cohort with varied phenotypes, including FTD. This gives more specific context but does not establish causation for every FTD case or every listed variant. |

Exact PanelApp gene-record requests for panel/gene 540/SNCA, 265/CHMP2B, 265/PSEN1 and 474/MAPT at `https://panelapp.genomicsengland.co.uk/api/v1/panels/PANEL/genes/GENE/` all returned HTTP 403. Therefore current PanelApp assertion details and correspondence to the OT source snapshot remain NOT YET VERIFIED. No substitute content was fabricated.

| Layer | Distinguishable with this audit? | Limit for answer verification |
| --- | --- | --- |
| Source assertion | Partly: original disease names/IDs, panel IDs, trial conditions and source references | Missing original fields in GW/EP and blocked PanelApp limit original assertion reconstruction |
| Aggregated association | Yes: disease–target identity, aggregate/source scores, direct/inclusive settings | Score is neither a causal probability nor an independent assertion; aggregate cannot replace supporting records |
| Individual OT evidence | Yes: stable-looking record ID, datasource/datatype, mapped disease, selected provenance fields | IDs are observed identifiers, not guaranteed release-invariant identities; duplicates/source dependencies remain possible |
| Publication/study | Partly: PMID resolution and four abstracts; two trial records; panel study IDs | Citation presence is not entailment; no exhaustive article review, panel snapshot, GWAS credible-set reconstruction or human adjudication |
| Derived/inferred statement | Yes as an explicitly labelled audit derivation: intersections, joins, missing-support judgments | A composed path is not proof of treatment/causality. Clinical-precedence association evidence itself can be derived from drug/indication joins; avoid circular corroboration |

Semantic requirements exposed (not ontology designs): distinguish normalized anchor from original disease scope; distinguish aggregation from source evidence; retain source-specific identifiers and nullable fields; preserve query-time propagation separately from upstream mapping; distinguish mechanism, indication, stage and trial status; record which texts were actually reviewed; distinguish source absence from retrieval failure and biological absence. These requirements can also be represented in relational tables or structured documents. Graph benefit must be tested, not assumed.

Task 003 source result: both pairings have concrete provenance and claim-scope cases. FTD adds an observed broad-label/subtype mismatch and a traceable, narrowly scoped clinical indication. Phenotypes remain deferred. See the evidence-linked question records and qualitative scope recommendation; no disease is selected by sample overlap totals.

## Task 004 technical source review

2026-09-17 (Asia/Kolkata). **TECHNICAL SOURCE REVIEW; DOMAIN-EXPERT ADJUDICATION ABSENT.** Targeted follow-up of existing cases, not another matched coverage sample. No full datasets, efficacy assessment, causal gold labels or source acquisition approval. Source text was inspected transiently; no full-text/API payload files were added. T3 history is preserved.

### T4-method: reproduction and depth

- OT endpoint: `https://api.platform.opentargets.org/api/v4/graphql`; `meta { dataVersion { year month } }` returned 26/06. T3 evidence IDs identify prior observations; all T3 counts were not rerun.
- Europe PMC metadata/abstracts: T3-R REST recipe, `resultType=core`, for PMIDs 22503161, 23028126, 33008897, 31555645, 33303932, 30581980, 25031633, 9641683, 9789048. Body text: `https://www.ebi.ac.uk/europepmc/webservices/rest/PMCID/fullTextXML`. Inspected PSEN1/presenilin paragraphs in PMC7852392; presenilin/frontotemporal paragraphs in PMC6742707; first eight matching body paragraphs for healthy/N-terminal/efficacy in PMC6298197 and protofibril/BAN2401 in PMC4054967. These are **selected relevant full-text passages**, not exhaustive article/supplement review.
- PMC4669567/PMC3475404: PMC browser challenge, Europe PMC page access failure, XML HTTP 500. PMC23724 XML HTTP 500. Free-text locators exist but these attempts did not supply full text. Access failure does not establish absence of support.
- Three PanelApp gene pages below became accessible via the web reader, unlike the T3 API attempts. Details/history inspected; exact OT input versions **NOT YET VERIFIED**. A source's expert-review badge is not expert adjudication of this project.
- Mondo: `https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:ID`, followed by its `parents` link over HTTPS. OLS metadata reports international release 2026-09-01, loaded 2026-09-16. Individual records only; no ontology imported.
- Registries: `https://clinicaltrials.gov/api/v2/studies/NCT03658135` (status, conditions, eligibility, design, outcomes) and `/NCT00594737` (identification, conditions, status, design). No trial-result analysis.

### T4-P: publication support and stopping points

| Publication / case | Actual depth | Bounded conclusion |
| --- | --- | --- |
| [22503161](https://doi.org/10.1016/j.neurobiolaging.2012.02.020), FTD/PSEN1 GE | ABSTRACT ONLY; FULL TEXT NOT REVIEWED; SOURCE ACCESS LIMITED | Dementia-family screening reports mutations/variants and varied phenotypes. Variant-specific segregation/pathology and all-FTD causation are not adjudicated. |
| [23028126](https://doi.org/10.1101/cshperspect.a006296), same GE record | ABSTRACT ONLY; FULL TEXT NOT REVIEWED; SOURCE ACCESS LIMITED | AD genetics review; attachment to an FTD-mapped record does not establish its exact FTD proposition or an independent FTD cohort. |
| [33008897 / PMC7852392](https://europepmc.org/articles/PMC7852392), AD/PSEN1 EP | FULL TEXT: selected relevant body paragraph | Human glycoproteomics compared with an APP/PS1 transgenic mouse dataset; names AD-linked PSEN1 mutation context. Not a new human PSEN1 causal association demonstration. |
| [31555645 / PMC6742707](https://europepmc.org/articles/PMC6742707), FTD/PSEN1 EP | FULL TEXT: selected autophagy/AD/FTD paragraphs | Review discusses presenilin in AD and tau/FTD separately. Inspected passages do not establish PSEN1 causation of FTD. Exact OT text-mining span not recovered; do not declare a confirmed extraction error. |
| [9641683](https://doi.org/10.1038/31508), MAPT panel 474 | ABSTRACT ONLY; FULL TEXT NOT REVIEWED | Inherited FTDP-17 families/tau mutations with historical Pick terminology; not proof of equivalence to every modern Pick/FTD concept. |
| [9789048](https://doi.org/10.1073/pnas.95.22.13103), MAPT panel 474 | ABSTRACT ONLY; FULL TEXT NOT REVIEWED; SOURCE ACCESS LIMITED | Familial PPND/FTDP-17 mutation/tau findings; no warrant for all-FTD generalization. Other panel citations 20301678/28334843 remain unreviewed locators. |
| [30581980 / PMC6298197](https://europepmc.org/articles/PMC6298197), gosuranemab mechanism | FULL TEXT: selected introduction, methods, pharmacodynamic paragraphs | BIIB092 binds N-terminal tau; healthy-participant study concerns target engagement, not clinical FTD benefit. Some background cites unpublished work; tracing stops at this paper. |
| [25031633 / PMC4054967](https://europepmc.org/articles/PMC4054967), lecanemab mechanism | FULL TEXT: selected BAN2401/protofibril discussion | Perspective describes species-specific Aβ targeting, more precise than APP gene indexing. Historical development statements are not current regulatory evidence; underlying binding studies/product labels not adjudicated. |
| [33303932](https://doi.org/10.1038/d41573-020-00217-7), MAPT-drug references | METADATA ONLY; no abstract; FULL TEXT NOT REVIEWED | Title/DOI resolve. Body support for either drug's mechanism/efficacy is NOT YET VERIFIED. Never use the title as a drug-specific result. |

### T4-S: original panel and mapping context

| Record inspected | Established source content | Limit |
| --- | --- | --- |
| [Panel 265 / PSEN1](https://panelapp.genomicsengland.co.uk/panels/265/gene/PSEN1/) | Multiple phenotypes include frontotemporal dementia 600274; history links the two GE citations above. | No isolated variant-specific FTD adjudication. Gene OMIM:104311 is not disease OMIM:600274. |
| [Panel 474 / MAPT](https://panelapp.genomicsengland.co.uk/panels/474/gene/MAPT/) | Pick 172700 and frontotemporal dementia with/without parkinsonism 600274 among several phenotypes; four T3-E publication locators. | Panel-wide citations need not justify every phenotype separately. Gene OMIM:157140 is distinct from these disease IDs. |
| [Panel 540 / MAPT](https://panelapp.genomicsengland.co.uk/panels/540/gene/MAPT/) | Frontotemporal dementia with/without parkinsonism 600274 and Pick 172700 are listed. | Does not itself explain OT's semantic-dementia assignment. |

T3 IDs `98c49197e4989f7d3be8b2f8ee3c7699e2f3d6dc` (PSEN1/panel 265) and `019b39b2b176f9e7df8536022682738d12e32f39` (MAPT/panel 540) share OMIM:600274 but map to MONDO:0017276 and MONDO:0010857. The [OLS semantic-dementia record](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:0010857) annotates OMIM:600274 with description `Orphanet:100069`, **not** `MONDO:equivalentTo`. This distinguishes an annotated xref from an equivalence assertion; it does not reconstruct OT's mapping algorithm. Direct OMIM access failed. Mapping cause, clinical equivalence and preferred repair remain **NOT YET VERIFIED**. Preserve contextual assignments; no global merge or silent correction.

### T4-H: paths versus normalization

Each consecutive child-to-parent step below was checked in both OLS and OT (`disease(efoId:D) { id name parents { id name } }`):

1. Semantic dementia MONDO:0010857 → behavioral variant of frontotemporal dementia MONDO:0017160 → FTD MONDO:0017276.
2. AD type 1 MONDO:0007088 → early-onset autosomal dominant AD MONDO:0015140 → familial AD MONDO:0100087 → AD MONDO:0004975.

These are source classification paths, not independently endorsed clinical taxonomy or executed OWL entailments. Semantic dementia also has progressive non-fluent aphasia MONDO:0015059 as an immediate parent; observed, not traversed. Other branches were not expanded. Agreement between dependent resources is not independent corroboration. This closes the specific T3 path gap without authorizing descendant closure.

OLS places Pick MONDO:0008243 under FTD and annotates OMIM:172700 `MONDO:equivalentTo`. Yet direct MAPT evidence `04e8f548c45ece0c2d428eef5f5aa149f67f1fbd` already maps its original Pick label to broad FTD. **Direct means relative to the normalized anchor**, not unnormalized original scope. APP `8bac3794c7e23d4dc3e7b44e3b2e1af8dcccc4fe` and MAPT `019b39b2b176f9e7df8536022682738d12e32f39` retain narrower normalized diseases and enter T3's inclusive diagnostic through descendants. Counts 0→1 and 3→10 remain dated T3 observations, not newly rerun totals or universal genetic-evidence counts.

### T4-C: clinical-precedence dependency

[OT documentation](https://platform-docs.opentargets.org/evidence#clinical-precedence) defines this evidence through a clinical drug–disease report joined to drug mechanism data. Follow-up inspected one returned row per target:

`disease(efoId:"MONDO_0017276") { evidences(ensemblIds:[T], datasourceIds:["clinical_precedence"], enableIndirect:false, size:1) { count rows { id datasourceId datatypeId diseaseFromSource diseaseFromSourceId diseaseFromSourceMappedId clinicalReportId clinicalStage drug { id name } literature } } }`

| Target T | Selected evidence ID | Matching records / inspected | Shared dependency |
| --- | --- | --- | --- |
| GRIN1 ENSG00000176884 | ed0b04f2d73abb84a48ed87d556725b1743a425c | 3 / 1 | CHEMBL807 memantine; nct00594737; PHASE_3 |
| GRIN3B ENSG00000116032 | 0d60abae93f3438f8750a76beb2b41de9b6b3efd | 3 / 1 | Same drug/report/stage |

Both rows have original FTD label, null original ID, normalized MONDO_0017276, and literature 17545743/21792308/22674572 plus an empty string; these publications were not read. Counts are records, not patients/independent studies/publications. No score threshold or pagination; direct excludes query-time descendants, not upstream normalization. An initial incorrect `chembl` datasource returned zero; discarded as a query diagnostic, not evidence of absent clinical support.

`drug(chemblId:"CHEMBL807") { mechanismsOfAction { rows { mechanismOfAction actionType targetName targets { id approvedSymbol } } } }` resolves an NMDA-receptor mechanism to both genes among receptor subunits. `clinicalReports(clinicalReportsIds:["nct00594737"])` resolves the shared AACT report. Its [primary registry](https://clinicaltrials.gov/study/NCT00594737) describes an open-label single-group pilot, PHASE3/COMPLETED, last posted 2012-06-04. Stage/completion do not establish efficacy. Two selected evidence IDs therefore are not independent genetic confirmations; no claim is made about dependencies among all six returned records. T3-X's clinical-precedence-only finding remains confined to its association/source query.

### T4-D: indication population and mechanism

For T3 gosuranemab FTD indication `c680c47a8cc2571635e1d5c629e51834273a3e67d25ebedfa9e58b729ad65189`, [NCT03658135](https://clinicaltrials.gov/study/NCT03658135) specifies four cohorts (CBS, nfvPPA, symptomatic MAPT carriers, TES), screening against underlying AD and exclusion of several non-tau genetic causes. It is not an unselected all-FTD population. Primary outcome concerns treatment-emergent adverse events; phase PHASE1. TERMINATED/program discontinuation are dated status/reason fields, not failed-efficacy proof. Last posted update remains 2019-12-19. No results reviewed. Preserve population wording; do not invent exact MONDO mappings or silently repair source gene spellings.

T3's zagotenemab–MAPT path supports a platform mechanism and inspected AD/tauopathy indications, not an FTD indication/treatment claim. Its sole cited mechanism publication is metadata-only here, so publication-level mechanism support remains unverified. The healthy-participant paper and lecanemab perspective above show why gene-indexed targets, molecular species, populations and regulatory statements need separate scope. No new current approval conclusion.

### T4 stopping decision

There is enough evidence for bounded technical design questions, not clinical truth, mapping repairs, complete coverage or graph superiority. Inaccessible sources remain explicit limits; positive causal/therapeutic claims stay deferred. HPO/OMIM route-specific reuse and publication redistribution concerns remain unresolved as previously recorded. Reading sources does not authorize distributing full content. Source selections remain Task 005 proposals.
