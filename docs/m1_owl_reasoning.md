# M1.4 — OWL reasoning tests and forbidden-entailment verification

Implementation record, pending owner review. Approved input baseline:
`1e3836fce61b79c6ec78a351c2217a6847e8a5c6`.

## Scope and unchanged authority

Only `tests/test_m1_owl_reasoning.py` and this document are created. The conceptual contract sections 14–17, implementation-readiness sections 7/14/16, G01–G06 mechanics and Task 006–008 records govern the checks. No new schema term, axiom, import, inference rule or biomedical assertion is added to the approved ontology or fixtures. The 20/28/39 manifest, Q01–Q07 and R1–R14 remain unchanged.

Audit-derived fixtures still describe the pinned project audit, not independently reproduced historical source evidence. No biomedical data acquisition, retrieval, LLM integration, research experiment or software installation occurs. Every committed input file is compared byte-for-byte with the baseline. Tests create disposable in-memory graph copies; neither closures nor synthetic controls are persisted as source evidence.

## Actual ontology and applicable reasoning

The 355-triple ontology contains only declarations, annotations and version metadata: 20 local classes plus external `prov:Entity`, 27 local object properties plus external `prov:wasDerivedFrom`, 39 datatype properties and one ontology declaration. The only input predicates are `rdf:type`, `rdfs:label`, `rdfs:comment`, `rdfs:isDefinedBy`, `owl:versionIRI` and `owl:versionInfo`.

There are no subclass/subproperty hierarchies, domain/range constraints, equivalence, disjointness, cardinalities, keys, transitivity, property chains or imports in the ontology. Instance input is separately checked for authorized predicates/types, preventing injected OWL axioms from bypassing the schema check. External PROV terms are referenced without importing the PROV-O axiom set.

No new biomedical conclusions are warranted. Built-in consequences such as self-equality, class self-equivalence and relationships to `owl:Thing` are legitimate engine outputs. They must not be confused with equality/equivalence between distinct disease references. Conversely, different IRIs do not establish inequality or biological independence.

The test regime is OWL 2 RL/RDF rule closure, not an OWL DL profile certificate or a complete reasoner for arbitrary ontologies. Relevant standard: [W3C OWL 2 RL/RDF rules](https://www.w3.org/TR/owl2-profiles/#Reasoning_in_OWL_2_RL_and_RDF_Graphs_using_Rules).

## Environment and configuration

Existing isolated dependency path: `/private/tmp/dementiagraph-m1-task008-pyshacl`.
Python 3.12.7; `owlrl 7.1.4`; `rdflib 7.1.4`; existing structural validator `pyshacl 0.30.1`. No dependencies were installed or changed.

```python
DeductiveClosure(
    OWLRL_Semantics,
    axiomatic_triples=False,
    datatype_axioms=False,
    rdfs_closure=False,
    improved_datatypes=True,
)
```

`rdfs_closure=False` does not disable RDF/RDFS-related rules intrinsic to OWL RL. Likewise the two axiom flags do not mean the rule engine generates no built-in datatype or schema consequences. No extensions, extra rules or imports are enabled. Network connection attempts are blocked during reasoning.

The engine expands private graph copies. The input graph is checked for mutation. Diagnostics include both error messages and error nodes without text. The engine's `ErrorMessage`/`error` vocabulary is internal diagnostic output, not an extension to the project ontology. See [OWL-RL closure diagnostics](https://owl-rl.readthedocs.io/en/latest/Closure.html); execution details were checked against the installed 7.1.4 source because hosted documentation may describe older versions.

## Reasoning results

| Input | Input triples | Closure triples | Added triples | Contradiction diagnostics |
| --- | ---: | ---: | ---: | ---: |
| Schema alone | 355 | 953 | 598 | 0 |
| Schema + unchanged audit fixtures | 1,485 | 2,945 | 1,460 | 0 |

These are engine graph sizes, not counts of biomedical facts or research findings. All input assertions are preserved. All added triples fit explicitly reviewed consequence patterns; there are no new project-property assertions, cross-reference equality, or unexpected substantive inferences.

| Added predicate | Schema-only additions | Combined additions | Interpretation |
| --- | ---: | ---: | --- |
| `owl:sameAs` | 328 | 759 | Reflexive only, including engine-level literal consequences |
| `owl:equivalentProperty` | 67 | 67 | Property self-equivalence |
| `rdfs:subPropertyOf` | 67 | 67 | Property self-relationships |
| `rdfs:subClassOf` | 66 | 66 | Self and top/bottom class relationships |
| `owl:equivalentClass` | 23 | 23 | Class self-equivalence |
| `rdf:type` | 47 | 477 | Built-in classes, annotations, datatypes; literal typing; existing individuals typed `owl:Thing` |
| `owl:disjointWith` | 0 | 1 | Built-in `xsd:dateTime` disjoint with `xsd:string`; not domain-class disjointness |

The combined closure's extra type triples comprise 36 datatype declarations, nine annotation-property declarations, two built-in class declarations, 170 `owl:Thing` typings, 257 string-literal typings, two date-literal typings and one dateTime-literal typing.

The broad set of engine-generated triples is not silently discarded. `unexplained_additions` inspects every addition using finite structural patterns for this exact declarations-only scope. Non-reflexive equality, new local claims, nontrivial local class typing or any unrecognized addition fails the check. Counts are recorded observations; tests primarily assert semantics rather than relying on a total alone.

## Eight semantic boundaries

| Test | Actual controlled check | Responsibility and limits |
| --- | --- | --- |
| Mapping → equality | Pick and ambiguous OMIM mappings retain distinct input/destination nodes; neither-direction sameAs/equivalentClass/differentFrom is derived. Existing ambiguity result remains qualified. | OWL non-derivation and application interpretation; no proof of inequality or correct normalization. R2–3; Q03/05 |
| Hierarchy → equivalence | Five audited steps do not produce endpoint equality, equivalence or an endpoint subclass taxonomy. | OWL non-derivation; navigation remains explicit application work. R4–5; Q04 |
| Association → causality | Associations receive no new local-property content, and the whole closure has no unexplained addition. | Limited OWL check only. There is no approved causal predicate; no artificial one is created. Causal readings of scores/prose remain application/manual obligations. R1/14; Q01–02 |
| Shared evidence → independent confirmation | Shared-trial join still finds the common study. No independence-assessment value is derived. A synthetic unjustified independence assertion fails the existing controlled application validator. | Application/provenance with supplementary OWL checks; shared source is not proof of universal statistical dependence. R13–14; Q02 |
| Mechanism → indication/efficacy | Mechanisms acquire neither indication typing nor disease-reference links; existing indication inventory is preserved. Fixed clinical-benefit/treatment requests remain unsupported. | OWL role non-derivation, existing SHACL role checks, application interpretation. R10/14; Q06–07 |
| Trial phase/status → success | Gosuranemab report phase/status/date literals are preserved, with no new local claim. Fixed phase/completion, termination/failure and benefit requests remain unsupported. | Primarily application-level; no invented success predicate. R11/14; Q07 |
| Missing evidence → negation | Remove a shared-study link in memory: closure introduces neither negative property assertions nor inequality; shared-trial comparison becomes unresolved. | Open-world boundary and bounded application result. Absence of a conclusion does not prove biological falsehood. R9/13–14 |
| Incomplete path → complete chain | Remove a required AD path membership in memory: reasoning does not restore it; existing chain check rejects a complete explanation. A pre-existing completeness label is not counted as inferred proof. | Application topology and structural validation, not OWL completeness reasoning. R4–5/9/14; Q04 |

The existing application `decision` helper rejects certain fixed prohibited request labels unconditionally. Reusing these controls does not demonstrate a general biomedical claim evaluator or natural-language understanding. Nontrivial positive controls remain the actual shared-study join, original mapping/ambiguity retrieval and complete-chain evaluation. Full application acceptance is not claimed by this task.

## Engine and detector controls

- **Positive control:** fixture mapping node self-equality and a declared class's subclass relationship to `owl:Thing` are absent from input and present after closure. Thus a no-op engine cannot pass solely through negative tests.
- **Isolated contradiction:** only a disposable `urn:m1-test:contradiction rdf:type owl:Nothing` assertion is supplied. The engine reports `urn:m1-test:contradiction is defined of type 'Nothing'`, and an error node is verified. This is test input, not an added project axiom or biomedical fixture.
- **Forbidden-result detector:** inject sameAs between two distinct source disease-reference IRIs into a copy of the result graph. The detector returns that exact unauthorized triple. This tests detection, not an alleged biomedical inference.

No contradiction was detected on schema or combined baseline under the configured rule regime. That is not universal consistency certification or proof of biomedical correctness.

## Datatype and engine limitations

The fixtures use `xsd:string`, `xsd:date` and `xsd:dateTime`, all recognized by the installed engine. No datatype diagnostic was observed for these inputs. Lexical-preserving fixture loading is reused; original literal spellings and receipts remain unchanged.

Two implementation details limit interpretation:

1. The combined closure retains **698 added triples with literal subjects** internally (generalized RDF). This includes literal self-equality and datatype typing. Such a closure is not persisted or represented as an ordinary asserted Turtle artifact. The detector inspects these triples too; they are not biomedical facts.
2. Installed `owlrl/OWLRL.py` explicitly skips the `dt-eq`/`dt-diff` literal-value comparison rules. Non-supported datatype behavior and arbitrary datatype completeness are not certified. This task does not depend on cross-lexical-form literal equality/inequality, but cannot be cited as testing it.

Recognized literal values and absence of diagnostics do not prove all semantic datatype conditions. If later acceptance depends on omitted datatype comparisons or a richer axiom fragment, it needs a separately scoped decision. No new package is introduced to solve an unused requirement.

## Separation from SHACL and application acceptance

Reasoning is not run inside SHACL and the expanded closure is never supplied as replacement source data to the structural validator. Task 008 retains inference disabled and Meta-SHACL enabled.

| Layer/input | Expected and preserved result |
| --- | --- |
| OWL: schema and combined fixture | No contradiction detected under this bounded regime |
| Raw SHACL: original fixture | Conformance false; exactly 1 Violation + 8 Warnings |
| Project structural acceptance: original fixture | Blocked by missing dependency DerivedStatement `completenessStatus` |
| Raw SHACL: Task 008 in-memory completeness control | Conformance false; 0 Violations + 8 Warnings |
| Project structural acceptance: completeness control | Qualified structural pass; synthetic control is not an identity-valid persisted repair |
| Biomedical interpretation | No biomedical truth, clinical correctness, source completeness or independence certification |

A dedicated new test confirms OWL does not fill the missing completeness field. The unchanged Task 008 tests verify the exact structural findings, including warning categories. No warning or OWL result overrides the defect.

## Verification

Run from the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/private/tmp/dementiagraph-m1-task008-pyshacl python3 -m unittest discover -s tests -p test_m1_owl_reasoning.py -v
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/private/tmp/dementiagraph-m1-task008-pyshacl python3 -m unittest discover -s tests -v
git diff --check
git diff --cached --check
git status --short --untracked-files=all
```

New suite: **18 tests passed** in 1.549 seconds. Complete regression run on 2026-09-23: **73 tests passed in 182.659 seconds**, comprising all 55 existing tests plus the 18 new reasoning tests. Turtle parsing, Meta-SHACL, original baseline 1-Violation/8-Warning and synthetic control 0-Violation/8-Warning assertions all passed. No findings were suppressed. Git diff checks and explicit new-file syntax/whitespace checks passed; no tracked or staged changes exist. The all-input preservation test checks every tracked file in the approved baseline, including all design documents, ontology, fixtures, identity code/receipts and SHACL implementation. Original inventory remains 170 records, 1,130 fixture triples, 48 source passages and 12 audit-section snapshots. Untracked new files receive explicit syntax/whitespace checks because Git diff checks do not inspect them.

## Remaining M1 acceptance obligations

This task supplies bounded M1.4 evidence, pending owner acceptance. It does not close M1. Remaining work includes M1.6 semantic acceptance reconciliation, any uncovered query-time replacement fidelity checks, and an R1–R14 matrix identifying completed, qualified and explicitly deferred obligations. The known completeness defect still needs an authorized disposition before any claim that the persisted computation meets all structural requirements; repair must follow immutable-description identity mechanics.

Ontology-alignment/provenance limitations and Q01–Q07 positive/negative coverage must remain explicit at M1 close. Source acquisition, independent biomedical adjudication, held-out evaluation, general retrieval/claim verification and research experiments remain separately gated later work, not results of this test suite. Graph advantage remains NOT YET DEMONSTRATED.
