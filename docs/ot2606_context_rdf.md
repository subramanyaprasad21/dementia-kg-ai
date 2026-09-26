# Approved OT context RDF implementation

Owner explicitly approved the proposed context identity extension in the conversation, together with the two additional acquisition budgets. This implements the exact four-class scope proposed in `ot2606_context_recovery.md`; the older proposal remains historical. Existing identity profiles, ontology terms, fixtures and source artifacts are unchanged.

`tools/ot2606_context_rdf.py` implements `m2-ot-context-description-1` and `m2-context-record-1` with the proposed finite receipt keys, SHA-256 canonical payloads, file/row scope, registered snapshot/participant checks and collision rejection. Capture-only metadata is excluded from source identity. Physical repackaging changes a file-scoped description, not the biological assertion's independence. Mechanisms without upstream IDs receive no invented source ID. Memantine's two selected target projections retain the same source description.

Only four new record classes are activated: SourceSnapshot, DiseaseConceptReference, MechanismRecord and ClinicalIndicationRecord. Existing authority referents are reused. The eight disease-context rows remain selection inputs, not a new imported disease hierarchy. No source aggregate, clinical population or article-inspection RDF profile is implicitly activated.

## Results

- Context graph: **43 resources / 226 asserted triples**; five mechanisms, four indications, eight snapshots, four normalized disease references, eleven provenance information resources and authority referents.
- Combined accepted source graph: **191 resources / 1,112 asserted triples**. Shared referents are counted once.
- Context SHACL: zero findings, raw conformance true.
- Combined SHACL: zero violations and two existing source-omission warnings; raw conformance false, qualified structural acceptance.
- OWL RL control: no non-reflexive equality or newly inferred local substantive predicate assertions; not biomedical truth or universal consistency certification.
- Five focused tests passed, covering replay/round-trip/inventory, capture separation, payload revision, unregistered lineage, inactive kinds, structural mutation and shared mechanism source context.

`manifests/ot2606-context-001.kg-release.json` pins exact source extraction, capture manifest, ontology/shapes, RDF/receipts and implementation/test hashes. Raw files stay outside Git. Reproduce with the existing Python environment:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=tools:/private/tmp/ot2606-duckdb-inspection:/private/tmp/dementiagraph-m1-task008-pyshacl python3 tools/ot2606_context_rdf.py verify
```

This releases the accepted context slice only. Full M2 question acceptance remains incomplete; do not promote maximum indication stage to each trial's phase/status, population or efficacy. Registry report locators remain in linked source descriptions pending justified primary StudyRecords.
