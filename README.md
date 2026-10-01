# DementiaGraph-V

DementiaGraph-V is a research-engineering project for provenance-aware dementia knowledge representation, bounded graph retrieval, grounded LLM answering, and deterministic assertion verification.

The repository contains the completed **M0–M7 development programme** and its public reproducibility artifacts. It is a bounded research prototype, not a comprehensive dementia knowledge base, clinical system, or held-out benchmark. The current results do **not** establish graph superiority, clinical validity, or unseen-question generalisation.

## What is implemented

- **Semantic model:** RDF/OWL representation with explicit disease references, mappings, evidence occurrences, source snapshots, mechanisms, indications, studies, provenance and missingness states.
- **Validation:** SHACL-based structural checks, bounded OWL-RL controls, identity/provenance receipts, immutable release manifests, and negative/mutation tests.
- **Qualified development corpus:** **191 resources / 1,112 asserted triples** assembled from a bounded Mondo slice and historical Open Targets 26.06 evidence/context.
- **Retrieval:** lexical, graph and hybrid retrieval over the same finite corpus, with reciprocal-rank fusion and explicit root/budget controls.
- **Grounded generation:** evidence packets are separated from model-only input; generated structured assertions are retained as exact records.
- **Verification:** local RDF assertion/citation/type checks operate on the grounded output without silently repairing model text.
- **Evaluation:** 24 generated responses across 12 development-overlapping questions, with deterministic replay and single-reviewer scoring.

## Current evaluation result

The M7 portfolio challenge is intentionally **development-overlapping**, so it cannot estimate held-out generalisation.

- 12 questions; 12 model-only and 12 grounded generations.
- 55 structured grounded assertions were submitted; **55/55 passed** the local exact-assertion verifier.
- The verified condition retained the same 55 assertions, so verification produced **no incremental assertion-precision change** on this run.
- Single-reviewer strict required-fact completion was **68.06%**.

The useful result is therefore narrower than “verification improves answers”: the submitted grounded assertions were locally supportable, while complete use of all required evidence remained substantially harder. See [M7 findings](docs/m7_owner_evaluation_findings.md) and [M7 execution results](docs/m7_portfolio_results.md).

## Reproduce the public offline path

Recommended environment: **Python 3.12**.

```sh
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
export PYTHONPATH=tools:tests
```

Then run the portable committed-corpus checks:

```sh
python tools/development_corpus.py verify
python tools/characterise_development_graph.py
python tools/replay_development_retrieval.py
python tools/m7_challenge_freeze.py
python tools/replay_m7_challenge.py
python tools/m7_owner_metrics.py
```

These commands are offline and do not call a model or fetch biomedical sources. Full source-capture replay additionally requires the original external raw artifacts. See [reproducibility.md](docs/reproducibility.md).

## Historical integrity versus living files

Historical release manifests are preserved byte-for-byte. Their authority files are also stored under [`archive/frozen/`](archive/frozen/README.md), where existing SHA-256 mappings can be verified without forcing the live README, packaging files, or compatibility wrappers to remain frozen forever.

This separation is deliberate:

- historical manifests and research artifacts remain immutable evidence;
- archived authority bytes preserve the exact versions named by those manifests;
- current documentation and portability tooling can evolve without rewriting historical provenance.

## Repository map

| Area | Purpose |
|---|---|
| `ontology/` | DementiaGraph-V ontology |
| `validation/` | SHACL shapes and validation rules |
| `kg/` | committed RDF releases |
| `manifests/` | frozen acquisition/release/development manifests |
| `tools/` | construction, validation, retrieval, replay and evaluation tooling |
| `tests/` | semantic, structural, replay, mutation and execution-control tests |
| `evaluations/` | frozen M7 public evaluation package |
| `experiments/` | recorded model execution/replay artifacts |
| `docs/` | design records, milestone reports, limitations and findings |
| `archive/frozen/` | immutable copies of historical authority files |

For a compact project description, see [portfolio_summary.md](docs/portfolio_summary.md). For the research framing and limitations, see [research_questions.md](docs/research_questions.md) and [evaluation_protocol.md](docs/evaluation_protocol.md).

## Scope and limitations

This project does not diagnose dementia, recommend treatment, establish biomedical truth, or replace clinical review. The graph is intentionally bounded and incomplete. Several historical upstream versions remain unresolved, the M7 evaluation has one reviewer and no independent clinical adjudication, and the evaluation questions overlap the development programme. The model identifier is also not a pinned provider-weight snapshot.

These limitations are part of the recorded result, not hidden assumptions.

## Licence and third-party material

This repository is **not released under an open-source licence**. See [LICENSE](LICENSE) for the repository rights statement. External datasets, ontologies, publications and source artifacts retain their own licences and terms; repository inclusion or citation does not relicense them.
