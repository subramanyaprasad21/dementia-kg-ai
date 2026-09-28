# Offline inspection and reproducibility

This guide describes the current qualified development corpus and M7 portfolio challenge. It does not authorize fresh acquisition or model calls. Run commands from the repository root.

## Environment and replay levels

The recorded local environment uses **Python 3.12.7, RDFLib 7.1.4, owlrl 7.1.4, pySHACL 0.30.1 and DuckDB 1.5.5**. RDFLib supports graph inspection; owlrl and pySHACL support reasoning/structural tests; DuckDB is used by historical Parquet replay. Standard-library tools handle metric aggregation. Dependencies currently live in an external local runtime; this repository does not provide a portable dependency installer or lockfile. Use an interpreter with the required versions available rather than assuming the original temporary directories exist on another machine.

| Replay level | Inputs and limits |
|---|---|
| Published graph integrity and retrieval | Committed graph files and manifests; RDF dependencies. No network or raw-source download required. |
| Recorded M7 execution and owner metrics | Committed frozen public package, requests/responses, verification and annotations. Offline replay does not regenerate model outputs or redo human review. |
| Full capture-to-release replay | Original raw artifacts outside Git, expected local paths or supported relocation arguments, and historical Git objects used by immutability tests. Missing inputs must not be replaced with current upstream data. |
| Private rubric integrity | Original private freeze directory; public replay explicitly reports that private integrity was not checked when that directory is not supplied. The consolidated owner worksheet also preserves the review material. |

Raw bodies, API credentials and local acquisition material are not installation prerequisites to *inspect* the committed graph. They are prerequisites for relevant full source-replay checks. A fresh clone alone is not sufficient for every historical regression. See each source's release record for retention conditions and artifact locations.

## Verify and inspect the committed corpus

With dependencies available to `python3`:

```sh
export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH=tools:tests
python3 tools/development_corpus.py verify
python3 tools/characterise_development_graph.py
python3 tools/development_retrieval.py 'clinical indication' --anchor CHEMBL3990042 --type ClinicalIndicationRecord --mode hybrid
python3 tools/replay_development_retrieval.py
```

These commands print results without changing the committed corpus. The manifest verifies **191 subjects / 1,112 triples** and pins five asserted RDF inputs. Characterisation distinguishes record connectivity from biological relationships. Retrieval replay reproduces exposed development controls, not a held-out benchmark.

## Replay M7 without generation

```sh
python3 tools/m7_challenge_freeze.py
python3 tools/replay_m7_challenge.py
python3 tools/m7_owner_metrics.py
```

The freeze check verifies public package integrity. Execution replay checks recorded requests/responses and deterministic local assertion verification. Its historical `PENDING` human-scoring fields describe the execution checkpoint; they are not the current review status. The metrics command separately reproduces completed [owner-directed scoring](m7_owner_evaluation_findings.md) through the unchanged metric functions.

No command above calls a model. Do not use the live execution runner to inspect results. Exact recorded prompts, model configuration, usage and failures are preserved in the [M7 experiment directory](../experiments/m7-portfolio-challenge-001/). Deterministic archive replay does not promise that a new API generation would be identical.

## Graph construction entry points

Graph construction uses separate scripts for each source stage:

| Stage | Implementation | Frozen reference |
|---|---|---|
| Mondo RDF records | [m2_mondo_rdf.py](../tools/m2_mondo_rdf.py) | [Mondo release](m2_mondo_release.md) |
| Historical OT evidence RDF | [ot2606_rdf.py](../tools/ot2606_rdf.py) | [OT evidence release](ot2606_release.md) |
| OT mechanism/indication context RDF | [ot2606_context_rdf.py](../tools/ot2606_context_rdf.py) | [Context implementation](ot2606_context_rdf.md) |
| Development union and integrity | [development_corpus.py](../tools/development_corpus.py) | [Development manifest](../manifests/dementia-development-001.json) |

Each exposes `build` and `verify` operations. Building has stage-specific prerequisites and writes artifacts; **do not rebuild over historical records as an inspection step**. Use the committed release files and documented verification first. Provenance attachment, capture identities, source-description identities and RDF record identities remain distinct; the source release documents specify their lineage.

## Tests

Focused packaging verification:

```sh
python3 -m unittest test_m7_owner_metrics test_m7_protocol_checks test_m7_challenge_freeze test_m7_results_replay test_development_corpus test_development_characterisation test_development_retrieval -v
```

Full historical suite, when external source inputs and dependencies are available:

```sh
python3 -m unittest discover -s tests -v
```

The command above runs the full historical suite. This documentation checkpoint ran the focused tests listed below. Source-backed release verification and M1 audit-derived fixture tests have different inputs. The historical M1 completeness defect remains an intentional negative fixture; passing tests do not imply that fixture is fully SHACL conformant.

## Local packaging verification record

For this machine, the available dependencies were exposed with:

```sh
export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH=tools:tests:/private/tmp/ot2606-duckdb-inspection:/private/tmp/dementiagraph-m1-task008-pyshacl
```

This is a record of the local environment, not a portable setup instruction. All seven inspection/replay commands above completed successfully with zero API calls. No acquisition, generation, scoring change or source-artifact rewrite is part of M8 packaging.

Packaging checks: **40 tests passed, 0 failed** in 33.964 seconds (25 M7 metric/protocol/freeze/result checks, two corpus integrity/relocation checks, four characterisation checks and nine retrieval checks). Corpus verification also checked the pinned ontology and historical release hashes. All **40 local Markdown link targets** in the three packaging documents resolve. Git whitespace checks pass. The full historical suite was not rerun for this documentation-only change.
