"""Finite offline M1 acceptance queries. No receipts supply query answers.

Results describe pinned audit records, not biomedical truth or upstream completeness.
Synthetic operations below exist only in memory and never amend the execution ledger.
"""
import re
from rdflib import Graph, Namespace, URIRef, Literal, RDF, XSD
from m1_fixture_identity import receipt, identify, normalized_payload
from build_m1_audit_fixtures import PIN, lit, link

D = Namespace('https://github.com/subramanyaprasad21/dementia-kg-ai/ontology#')
PROV = Namespace('http://www.w3.org/ns/prov#')
TEST_EXECUTION = 'm1-semantic-controls/1'


class AcceptanceError(ValueError):
    """The affected bounded result cannot be accepted; not biological falsity."""


def one(g, node, field):
    values = set(g.objects(node, field))
    if len(values) != 1:
        raise AcceptanceError('Expected one ' + str(field) + ' on ' + str(node))
    return next(iter(values))


def typed(g, node, kind):
    if (node, RDF.type, kind) not in g:
        raise AcceptanceError('Wrong participant type: ' + str(node))


def snapshot(g, node):
    typed(g, node, D.SourceSnapshot)
    edition = str(one(g, node, D.snapshotVersion))
    locator = str(one(g, node, D.sourceLocator))
    description = str(one(g, node, D.artifactDescription))
    if (str(one(g, node, D.sourceAuthority)) != 'project-audit' or edition != PIN
            or not locator.startswith('docs/source_audit.md#')
            or 'audit-section-v1' not in description):
        raise AcceptanceError('Outside pinned audit source/projection boundary')
    return dict(iri=node, edition=edition, locator=locator, description=description)


def source(g, node):
    snap = snapshot(g, one(g, node, D.inSnapshot))
    locator = str(one(g, node, D.sourceLocator))
    if not locator.startswith(snap['locator'] + ';lines='):
        raise AcceptanceError('Record locator does not belong to its audit section')
    return dict(snapshot=snap, locator=locator)


def reference(g, node):
    typed(g, node, D.DiseaseConceptReference)
    ids = set(g.objects(node, D.externalIdentifier))
    authorities = set(g.objects(node, D.identifierAuthority))
    if len(ids) > 1 or (ids and len(authorities) != 1):
        raise AcceptanceError('Unqualified or multiple reference identifiers')
    labels = tuple(sorted(str(v) for v in g.objects(node, D.sourceLabel)))
    if not ids and not labels:
        raise AcceptanceError('No observed reference identity')
    return dict(iri=node, identifier=str(next(iter(ids))) if ids else None,
                authority=str(next(iter(authorities))) if authorities else None,
                labels=labels, snapshot=snapshot(g, one(g, node, D.inSnapshot)))


def comparison_key(ref):
    """MONDO lexical join only; never changes raw values, identity or OWL axioms."""
    value=ref['identifier']
    if ref['authority']=='MONDO' and value:
        match=re.fullmatch(r'MONDO[:_]([0-9]{7})',value)
        if match:return ('MONDO',match.group(1))
    if value is None:raise AcceptanceError('No identifier for this bounded identity join')
    return (ref['authority'],value)


def gaps(g, owner):
    result = []
    for n in sorted(g.subjects(D.aboutRecord, owner), key=str):
        if (n, RDF.type, D.MissingnessRecord) in g:
            result.append(dict(iri=n, field=str(one(g,n,D.expectedField)),
                               reason=str(one(g,n,D.missingnessReason)),
                               rationale=str(one(g,n,D.rationale)),
                               observation=one(g,n,D.observationContext)))
    return result


def mappings(g, occurrence):
    typed(g, occurrence, D.EvidenceOccurrence)
    provenance = source(g, occurrence)
    rows = []
    for m in sorted(g.subjects(D.mappingContext, occurrence), key=str):
        typed(g,m,D.MappingRecord)
        if one(g,m,D.mappingContext) != occurrence:
            raise AcceptanceError('Ambiguous context owner')
        rows.append(dict(mapping=m, occurrence=occurrence, provenance=source(g,m),
                         original=[reference(g,n) for n in sorted(g.objects(m,D.mappingInput),key=str)],
                         normalized=[reference(g,n) for n in sorted(g.objects(m,D.reportedDestination),key=str)],
                         candidates=[reference(g,n) for n in sorted(g.objects(m,D.candidateDestination),key=str)],
                         status=str(one(g,m,D.mappingStatus)), gaps=gaps(g,m),
                         contexts=tuple(sorted(g.objects(m,D.contextRecord),key=str))))
    return dict(occurrence=occurrence, provenance=provenance, mappings=rows,
                qualification='record-local assignments; no equivalence or mapping repair',
                unavailable=not rows)


def hierarchy(g, path):
    typed(g,path,D.HierarchyPath)
    psource=source(g,path)
    if str(one(g,path,D.completenessStatus)) != 'complete-for-declared-scope':
        raise AcceptanceError('Path explicitly incomplete/unknown')
    steps=set(g.objects(path,D.pathStep))
    if not steps: raise AcceptanceError('Empty path')
    outgoing={}; incoming={}
    for step in steps:
        typed(g,step,D.HierarchyStep)
        if source(g,step)['snapshot']['iri'] != psource['snapshot']['iri']:
            raise AcceptanceError('Step outside declared path snapshot')
        child=one(g,step,D.childReference); parent=one(g,step,D.parentReference)
        for ref in (child,parent):
            if reference(g,ref)['snapshot']['iri'] != psource['snapshot']['iri']:
                raise AcceptanceError('Endpoint reference outside audited chain context')
        if child in outgoing or parent in incoming:
            raise AcceptanceError('Branch or duplicate edge in single-chain path')
        outgoing[child]=(parent,step); incoming[parent]=child
    starts=set(outgoing)-set(incoming)
    if len(starts)!=1: raise AcceptanceError('No unique chain start')
    start=next(iter(starts)); current=start; seen=set(); ordered=[]
    while current in outgoing:
        if current in seen: raise AcceptanceError('Cycle')
        seen.add(current); parent,step=outgoing[current];ordered.append(step);current=parent
    if len(ordered)!=len(steps): raise AcceptanceError('Disconnected chain')
    return dict(start=reference(g,start),end=reference(g,current),steps=tuple(ordered),
                provenance=psource,qualification='complete named audit chain only; not OWL closure')


def selection(g, context):
    typed(g,context,D.SelectionContext)
    snap=snapshot(g,one(g,context,D.inSnapshot))
    anchor=reference(g,one(g,context,D.queryAnchor))
    mode=str(one(g,context,D.selectionMode)); state=str(one(g,context,D.completenessStatus))
    rows=[]
    for m in sorted(g.subjects(D.inSelectionContext,context),key=str):
        if (m,RDF.type,D.SelectionMembership) not in g: continue
        if one(g,m,D.inSelectionContext)!=context: raise AcceptanceError('Membership context conflict')
        e=one(g,m,D.selectedOccurrence);typed(g,e,D.EvidenceOccurrence)
        kind=str(one(g,m,D.inclusionKind))
        typed(g,one(g,e,D.hasTarget),D.Target)
        if mode=='direct-only' and kind=='descendant-selected':raise AcceptanceError('Direct/descendant conflict')
        rows.append(dict(membership=m,occurrence=e,target=one(g,e,D.hasTarget),
                         inclusion=kind,provenance=source(g,e)))
    return dict(context=context,anchor=anchor,snapshot=snap,mode=mode,state=state,
                rows=rows,occurrences=frozenset(r['occurrence'] for r in rows),
                targets=frozenset(r['target'] for r in rows),
                qualifications=tuple(str(x) for x in g.objects(context,D.limitationText)),
                extent='enumerated graph memberships only; upstream completeness unverified')


def intersection(g, left, right):
    a,b=selection(g,left),selection(g,right)
    if a['mode']!=b['mode']:raise AcceptanceError('Do not mix selection modes')
    if a['snapshot']['edition']!=b['snapshot']['edition']:raise AcceptanceError('Mixed editions')
    shared=a['targets'] & b['targets']
    return dict(targets=shared,left=a,right=b,
                support={t: (frozenset(r['occurrence'] for r in a['rows'] if r['target']==t),
                             frozenset(r['occurrence'] for r in b['rows'] if r['target']==t)) for t in shared},
                qualification='intersection of specified local selections; not exhaustive disease coverage')


def bounded_extent(g, context, declared_inputs):
    """An explicit caller-supplied finite test boundary, never an upstream page count."""
    selected=selection(g,context)
    if selected['occurrences']!=frozenset(declared_inputs):
        raise AcceptanceError('Finite declared inputs do not match enumerated memberships')
    return dict(local_complete=True,upstream_complete=False,source_state=selected['state'],
                qualification='complete only for explicitly declared local input set')


def constituents(g, grouping):
    typed(g,grouping,D.DiseaseTargetAssociation)
    if str(one(g,grouping,D.originRole))!='project-grouping':
        raise AcceptanceError('Source aggregate is not a project grouping')
    target=one(g,grouping,D.hasTarget); disease=reference(g,one(g,grouping,D.hasDiseaseReference))
    contexts=set(g.objects(grouping,D.inSelectionContext))
    if not contexts:raise AcceptanceError('Grouping missing selection context')
    expected=set()
    for c in contexts:
        s=selection(g,c)
        if comparison_key(s['anchor'])!=comparison_key(disease):
            raise AcceptanceError('Grouping anchor mismatch')
        expected.update(r['occurrence'] for r in s['rows'] if r['target']==target)
    actual={n for n in g.objects(grouping,PROV.wasDerivedFrom) if (n,RDF.type,D.EvidenceOccurrence) in g}
    if not expected or actual!=expected:raise AcceptanceError('Missing/extra grouping constituent')
    return frozenset(actual)


def evidence(g, occurrence):
    result=mappings(g,occurrence)
    result.update(target=one(g,occurrence,D.hasTarget),
                  source_id=str(one(g,occurrence,D.sourceRecordIdentifier)),
                  datasource=str(one(g,occurrence,D.evidenceSourceType)))
    pubs=set(g.objects(occurrence,D.citesPublication))
    slices={n for pub in pubs for n in g.subjects(D.citesPublication,pub)
            if (n,RDF.type,PROV.Entity) in g}
    contexts=set(g.objects(occurrence,D.contextRecord)) | slices
    result['publications']=frozenset(pubs)
    result['source_text']=tuple((n,str(t)) for n in sorted(contexts,key=str) for t in g.objects(n,D.sourceText))
    result['reviews']=tuple(dict(iri=r,about=one(g,r,D.aboutRecord),inspected=one(g,r,D.inspectedRecord),
                                depth=tuple(str(v) for v in g.objects(r,D.inspectionDepth)),
                                outcome=str(one(g,r,D.interpretationOutcome)),
                                reviewer_type=str(one(g,r,D.reviewerType)))
                            for r in sorted(g.subjects(RDF.type,D.InspectionRecord),key=str)
                            if (r,D.aboutRecord,occurrence) in g or any((r,D.inspectedRecord,n) in g for n in contexts))
    result['qualification']='attributed audit record; cited paper is not adjudicated claim support'
    return result


def shared_studies(g, left, right):
    for n in (left,right):typed(g,n,D.EvidenceOccurrence);source(g,n)
    studies=set(g.objects(left,D.refersToStudy)) & set(g.objects(right,D.refersToStudy))
    for n in studies:typed(g,n,D.Study)
    return dict(inputs=(left,right),studies=frozenset(studies),
                status='shared-source-established' if studies else 'unresolved',
                qualification='shared study references only; no independent genetic confirmation')


def publication_contexts(g, publications):
    """Attributed audit text, not a claim that the original paper was read now."""
    sources={n for pub in publications for n in g.subjects(D.citesPublication,pub)
             if (n,RDF.type,PROV.Entity) in g}
    return tuple(dict(iri=n,provenance=source(g,n),text=str(one(g,n,D.sourceText)))
                 for n in sorted(sources,key=str))


def clinical(g, drug):
    typed(g,drug,D.Drug); mechanisms=[];indications=[]
    for n in sorted(g.subjects(D.hasDrug,drug),key=str):
        if (n,RDF.type,D.MechanismRecord) in g:
            mechanisms.append(dict(iri=n,target=one(g,n,D.hasTarget),provenance=source(g,n),
                                   text=tuple(str(t) for t in g.objects(n,D.sourceText)),
                                   publications=frozenset(g.objects(n,D.citesPublication)),
                                   audit_publication_context=publication_contexts(g,set(g.objects(n,D.citesPublication)))))
        if (n,RDF.type,D.ClinicalIndicationRecord) in g:
            reports=[]
            for r in sorted(g.objects(n,D.indicationStudyRecord),key=str):
                typed(g,r,D.StudyRecord)
                populations=[]
                for p in g.objects(r,D.hasPopulationScope):
                    typed(g,p,D.PopulationScope)
                    populations.append(dict(iri=p,text=str(one(g,p,D.sourceText))))
                reports.append(dict(iri=r,study=one(g,r,D.refersToStudy),provenance=source(g,r),
                                    populations=populations,status=tuple(str(v) for v in g.objects(r,D.trialStatusText)),
                                    phase=tuple(str(v) for v in g.objects(r,D.trialPhaseText)),
                                    date=tuple(str(v) for v in g.objects(r,D.statusDate)),
                                    text=tuple(str(v) for v in g.objects(r,D.sourceText))))
            indications.append(dict(iri=n,disease=reference(g,one(g,n,D.hasDiseaseReference)),
                                    provenance=source(g,n),reports=reports))
    return dict(drug=drug,mechanisms=mechanisms,indications=indications,
                qualification='reported mechanism/indication only; no efficacy, approval or exhaustive absence claim')


def accept_claim(bundle, claim, *, study=None, disease_id=None):
    """Finite structured claim checks, not free-text QA or biomedical adjudication."""
    if claim=='sampled-shared-target':
        return bool(bundle.get('targets'))
    if claim=='shared-study':
        return study in bundle.get('studies',())
    if claim=='reported-indication':
        return disease_id is not None and any(r['disease']['identifier']==disease_id for r in bundle.get('indications',()))
    if claim=='dated-population-report':
        return any(r['study']==study and r['date'] and r['status'] and r['populations']
                   for i in bundle.get('indications',()) for r in i['reports'])
    if claim in {'causal-confirmation','independent-genetic-confirmation','efficacy',
                 'phase-implies-success','termination-implies-failure','global-absence','mapping-equivalence'}:
        return False  # Explicit policy boundary; positive tests above are graph-sensitive.
    raise AcceptanceError('Outside finite Q01-Q07 claim contract')


def make_record(g, kind, inputs, assertions):
    """In-memory test record: identity-bearing payload uses existing m1-id-1."""
    payload=normalized_payload(assertions);rec=receipt(kind,'project-operation',inputs,payload)
    node=URIRef(identify(rec));result=Graph()
    for triple in g:result.add(triple)
    result.add((node,RDF.type,D[kind]))
    for a in payload:
        p=PROV.wasDerivedFrom if a['field']=='prov:wasDerivedFrom' else D[a['field']]
        value=URIRef(a['value']) if a['form']=='iri' else Literal(a['value'],datatype=URIRef(a['datatype']) if a['datatype'] else None,lang=a['language'],normalize=False)
        result.add((node,p,value))
    return result,node,rec,payload


def comparison_control(g,left,right,context):
    result=shared_studies(g,left,right)
    if not result['studies']:raise AcceptanceError('No shared study to justify positive control')
    if not {left,right}<=selection(g,context)['occurrences']:raise AcceptanceError('Inputs not selected')
    scope='In-memory M1.6 control: complete comparison of exactly two pinned audit occurrences; not upstream completeness.'
    inputs=dict(execution=TEST_EXECUTION,method='shared-study-reference-intersection',methodVersion='1',
                inputKeys=[str(left),str(right)],subjectKey=str(left),comparatorKey=str(right),
                selectionKeys=[str(context)],scope=scope)
    assertions=[link('subjectRecord',str(left)),link('comparatorRecord',str(right)),
                link('inSelectionContext',str(context)),lit('executionReference',TEST_EXECUTION),
                lit('operationMethod',inputs['method']),lit('methodVersion','1'),lit('scopeText',scope),
                lit('completenessStatus','complete-for-declared-scope'),lit('dependencyStatus',result['status']),
                lit('rationale','Computed shared study references for these two inputs only; no independence or clinical adjudication.'),
                lit('resultSummary','Shared study: '+', '.join(sorted(str(s) for s in result['studies'])))]
    assertions += [link('prov:wasDerivedFrom',str(n)) for n in (left,right)]
    assertions += [link('sharedInput',str(n)) for n in result['studies']]
    return make_record(g,'DerivedStatement',inputs,assertions)


def grouping_control(g,context,target):
    s=selection(g,context);members={r['occurrence'] for r in s['rows'] if r['target']==target}
    if not members:raise AcceptanceError('No grouping constituents')
    disease=s['anchor']['iri'];scope='In-memory M1.6 grouping of selected target occurrences only.'
    inputs=dict(originRole='project-grouping',execution=TEST_EXECUTION,diseaseKey=str(disease),targetKey=str(target),
                method='selected-target-group',methodVersion='1',occurrenceKeys=[str(n) for n in members],
                selectionKeys=[str(context)],scope=scope)
    assertions=[lit('originRole','project-grouping'),link('hasTarget',str(target)),link('hasDiseaseReference',str(disease)),
                link('inSelectionContext',str(context)),lit('operationMethod','selected-target-group'),lit('methodVersion','1'),
                lit('scopeText',scope)]+[link('prov:wasDerivedFrom',str(n)) for n in members]
    return make_record(g,'DiseaseTargetAssociation',inputs,assertions)


def membership_explanation(g, membership):
    typed(g,membership,D.SelectionMembership)
    occurrence=one(g,membership,D.selectedOccurrence)
    context=one(g,membership,D.inSelectionContext)
    s=selection(g,context);kind=str(one(g,membership,D.inclusionKind))
    assignments=mappings(g,occurrence)
    paths=[]
    if kind=='descendant-selected':
        for p in g.objects(membership,D.justificationPath):
            chain=hierarchy(g,p)
            end=chain['end'];anchor=s['anchor']
            destinations=[d for row in assignments['mappings'] for d in row['normalized']]
            key=comparison_key
            if key(end)!=key(anchor) or not any(key(d)==key(chain['start']) for d in destinations):
                raise AcceptanceError('Path endpoints do not match normalized disease and query anchor')
            paths.append(chain)
        if not paths:raise AcceptanceError('No complete audited explanation path')
    return dict(occurrence=occurrence,context=context,inclusion=kind,mapping=assignments,paths=paths,
                qualification='selection explanation is distinct from upstream normalization',
                join_basis='MONDO authority plus seven digits; colon/underscore compared only, raw fields and identities preserved')
