# Project scope

Status: PROVISIONAL. The dementia slice, relationship families, and intended question distribution require owner approval.

## Intended task

The intended task is answering research knowledge questions from a documented evidence collection, with traceable support and an explicit insufficient-evidence response where appropriate. The prospective user is someone investigating biomedical knowledge rather than seeking individual diagnosis or treatment. The precise user profile and answer format remain REQUIRES HUMAN DECISION.

Candidate disease concepts from the handoff include dementia, Alzheimer's disease, dementia with Lewy bodies, vascular dementia, and frontotemporal dementia. These are scope candidates, not an approved concept inventory or asserted ontology hierarchy. Candidate relationships concern phenotypes, targets, drugs, biomarkers, and biological processes/pathways. Proteins and publications may be needed depending on the retained questions and evidence model. No term identifiers, mappings, or schema have been selected.

Scope options include a single disease with a small relationship set, or a small cross-disease slice supporting comparisons. The former may reduce integration work; the latter may support comparative questions but requires adequate shared coverage. Source feasibility must be checked before choosing either. A bounded initial slice is a proposal, not an approved final boundary.

## Exclusions and distinction

Individual clinical decision support, patient treatment recommendations, diagnosis, and claims of biomedical truth from software checks are excluded. A giant custom medical ontology, generic chatbot feature development, and copying the reference course's architecture are outside the intended scope.

Transformation Fidelity remains a separate source-to-CDM transformation project. The T2DM KG remains a separate semantic integration project. DementiaGraph-V should add a controlled study of retrieval, grounding, verification, and their failures; changing only the disease domain would not satisfy that objective.

## Open boundaries

Owner decisions are required on disease inclusion, relationship families, temporal scope, evidence granularity, conflict handling, literature inclusion, and supported research tasks. Time, compute/API budget, human review capacity, and domain expertise availability have not been established. They constrain feasible scope and evaluation depth.

Graph algorithms, embeddings, link prediction, a user interface, services, deployment, and orchestration are not scope commitments. Each needs a specific requirement and, where consequential, an owner decision.
