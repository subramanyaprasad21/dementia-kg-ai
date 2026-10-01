# Frozen historical authorities

This directory separates immutable historical evidence from the living project files.

The JSON manifests under `manifests/` and `evaluations/` remain unchanged. Their original path-to-SHA-256 mappings are preserved exactly. For public-release maintenance, the bytes named by those manifests are copied into versioned snapshot roots here and are verified against the existing digests.

Snapshots:

- `ot2606-evidence-001/` — authority files named by `manifests/ot2606-evidence-001.freeze.json`.
- `dementia-development-001/` — files named by `manifests/dementia-development-001.json`.
- `m7-portfolio-challenge-001/` — public files named by `evaluations/m7-portfolio-challenge-001/freeze.json`.

The snapshots are not new research results and do not replace the original manifests. They provide immutable byte authorities so current documentation, packaging, and compatibility wrappers can evolve without rewriting historical provenance.
