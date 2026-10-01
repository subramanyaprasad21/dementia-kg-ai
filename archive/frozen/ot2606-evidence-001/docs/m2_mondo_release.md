# M2.9 — reproducible Mondo-only KG slice

This completes M2.1–M2.9 **for the already captured Mondo subset only**, under the owner's continuous offline authorization and approved `m2-rdf-record-1` extension. M0/M1 closure and historical artifacts are unchanged. Full-corpus M2 is incomplete. This release is not the complete dementia KG or a research-results release.

## Artifacts and inventory

`manifests/mondo-pilot-001.kg-release.json` is a deterministic in-place release manifest; it references existing graph parts rather than copying a second graph dataset. SHA-256: `609bec7db19eb07931deeb7523076d055d5042de44ef607ba9306b324601a0f4`.

| Artifact | Purpose |
| --- | --- |
| `kg/mondo-pilot-001/records.ttl` | 31 immutable local source records, 186 triples |
| `kg/mondo-pilot-001/record-identities.json` | Exact m2-rdf-record-1 receipts, owned assertion payloads and source-slot lineage |
| `kg/mondo-pilot-001/provenance.ttl` | 29 original capture/description metadata resources, 131 triples |
| `manifests/mondo-pilot-001.kg-release.json` | File hashes, graph union hash, frozen source/edition/permissions, external artifact digests and dependencies |
| `tools/m2_mondo_release.py` / `tests/test_m2_mondo_release.py` | Offline deterministic packaging, integrity, relocation and negative controls |

The asserted union has **60 resources / 317 triples**: 13 SourceSnapshots, 13 DiseaseConceptReferences, five HierarchySteps, 14 source descriptions and 15 capture metadata resources. There are exactly **eight external Mondo concepts**, not thirteen diseases. The five accepted source-reported parent assertions remain unchanged; six additional raw parent rows are excluded from accepted research assertions. No named graphs, new ontology terms, ontology imports, additional inference rules or duplicate normalized/aligned dataset were introduced.

Canonical sorted union SHA-256: `40529ab9a3b2b1340b7afa537331aea08a95d6e063ef49bbbc0a099b03c9bb7b`. This is the generated canonical union representation's digest, not an invented raw source digest. Both component Turtle files can be parsed and unioned without blank-node identity issues.

## Version, provenance and permissions

Edition is `2026-09-01`; version IRI is `http://purl.obolibrary.org/obo/mondo/releases/2026-09-01/mondo-international.owl`. OLS loaded/updated remains `2026-09-24T00:09:08.017393439`, with no invented timezone. Fifteen capture timestamps/receipts remain separate from source edition and fourteen descriptions. All original response byte hashes and identity replay verify offline. RDF local records have independent m2-rdf-record-1 identities; neither M1 audit identities nor whole-response IDs impersonate individual parent assertions.

Attribution: **Mondo Disease Ontology contributors; delivered by EMBL-EBI OLS**. The frozen permission record identifies [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and its original [provider declaration](https://mondo.monarchinitiative.org/#license). This task uses the already verified permission record without a new network request. Changes made by the project: bounded source projection, technical reference assessment and deterministic RDF/provenance serialization; no source-value transformation or biomedical mapping correction. Source wording and annotations remain attributed; no endorsement is implied.

Raw responses and acquisition ledger remain outside Git. The release references their basenames/digests via the unchanged freeze manifest and local root hint. A reviewer needs those permitted byte-identical local artifacts to reproduce raw-source verification; a Git checkout alone is insufficient. Relocation uses `MONDO_PILOT_ARTIFACTS`, not rewritten provenance or substituted upstream downloads. The release verifier fails on missing/changed artifacts, changed release inventory, modified file/graph hashes, changed rights or different dependency versions. It never silently fetches or repairs inputs.

## Reproduction

Validated with Python 3.12.7, RDFLib 7.1.4, owlrl 7.1.4 and pySHACL 0.30.1. The manifest also pins all eight versions reported by the existing validator environment. No package was installed or upgraded. The current isolated dependency directory is `/private/tmp/dementiagraph-m1-task008-pyshacl`; a future environment must make the recorded versions available, since that temporary directory is not itself an archived runtime.

```sh
export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH=/private/tmp/dementiagraph-m1-task008-pyshacl
# Optional: point this to a relocated, byte-identical capture directory.
# export MONDO_PILOT_ARTIFACTS=/path/to/mondo-pilot-001
python3 tools/m2_mondo_release.py verify
python3 tools/validate_m2_mondo.py
python3 -m unittest discover -s tests -v
```

The release references validated M2.8 commit `1adcd3ac513bae6f16482b1ccb7a7c35de98dd0a` and pins the release builder/test files by content hash; it does not invent a circular self-commit hash. This report is outside the manifest hash inventory so final test results can be recorded after manifest verification. The enclosing Git commit preserves the report. The manifest itself is verified by deterministic byte regeneration and the explicit digest above. `build` is create-only and refuses an existing manifest. Graph generation and provenance functions reproduce bytes in memory; verification does not overwrite historical artifacts.

## Acceptance and limits

- M2.6 focused tests: four passed; identity-extension tests: four passed.
- M2.7 focused tests: three passed; M2.8 focused tests: six passed; release tests: three passed.
- SHACL/Meta-SHACL: true raw conformance, zero violations/warnings for this Mondo slice, with inference/advanced/JS/rule iteration/imports disabled.
- Semantic acceptance: exact source-backed reference/pair/edition/locator fidelity and full graph/provenance replay; reversed relations, missing/wrong participants, source-context changes, unsupported equivalence and provenance loss rejected.
- OWL RL control: no new substantive local-property assertions, derived-source links or equality between distinct resources; no reported engine diagnostic. Existing generalized-RDF/literal-comparison limitations remain documented, not solved here.
- Historical M1 audit fixtures retain their known completeness defect and negative-fixture disposition. A clean Mondo graph is not a claim that the M1 baseline became fully conformant.

This release provides bounded source fidelity and structural/semantic engineering verification. It does not establish independent biomedical validation, historical OLS-response reproduction, full Mondo ontology-release reproduction, statistical evidence independence, clinical correctness or complete R1–R14 biomedical acceptance. The two preparatory uninstrumented lookups remain disclosed. Graph advantage remains **NOT YET DEMONSTRATED**.

Open Targets 26.06 remains the central full-corpus acquisition/mapping dependency; 26.09 is not substituted. Other planned source records, historical versions/permissions and contextual mapping judgments still require their scoped acquisition/adjudication decisions. No blocked route was re-investigated. The M3 roadmap covers structural statistics, connectivity, paths and research-justified graph analysis/limitations; M4 covers LLM, vector, KG, hybrid and ontology-grounded retrieval baselines. Neither begins from this subset release automatically. Full-corpus readiness must be resolved or any explicitly bounded later study separately authorized, rather than treating this slice as a complete research corpus.

## Final integration results

Complete regression suite: **170 tests passed in 222.850 seconds**, exit status 0, comprising all 150 baseline tests and 20 new identity/RDF/provenance/validation/release tests. Log: `/private/tmp/dementiagraph-mondo-kg-release-tests.log`. The full run includes historical M1 negative-fixture expectations and all Mondo source/identity/representation/reference regressions. Focused release tests also verify offline relocation, missing/modified raw input rejection, metadata/hash/permission tamper rejection and duplicate-key rejection.

All three earlier source artifact digests remain exact; no previously tracked M1 or M2 file was modified or deleted. New Python syntax, whitespace and Git diff checks pass. Raw response bodies and ledger remain outside the repository. The Mondo-only release is complete within its authorized scope; no unresolved material verification failure was observed. No additional acquisition, M3/M4 work or push occurred.
