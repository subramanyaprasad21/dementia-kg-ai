# Source feasibility audit

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
