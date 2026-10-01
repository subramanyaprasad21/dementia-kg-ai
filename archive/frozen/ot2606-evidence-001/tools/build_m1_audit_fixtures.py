"""Offline replay of the finite owner-approved audit-derived fixture specification."""
import json
import re
import subprocess
from collections import Counter
from pathlib import Path
from rdflib import Graph, Namespace, URIRef, Literal, RDF
from m1_fixture_identity import (ROOT, BASE, XSD, canonical, digest, strict_load,
                                normalized_payload, receipt, identify, Registry)

D = Namespace(BASE + 'ontology#')
PROV = Namespace('http://www.w3.org/ns/prov#')
FIX = ROOT / 'fixtures/m1'
SOURCE = 'docs/source_audit.md'
PIN = '229540ce7383d9b47a7f7688099522fed7777d44'


def lit(field, value, datatype=XSD+'string'):
    return dict(field=field, form='literal', value=value, datatype=datatype, language=None)


def link(field, value):
    return dict(field=field, form='iri', value=value, datatype=None, language=None)


def section_bytes(raw, heading):
    lines = raw.splitlines(keepends=True)
    starts = [i for i, l in enumerate(lines) if re.sub(br'^#+ ', b'', l.rstrip(b'\r\n')).decode() == heading and l.startswith(b'#')]
    if len(starts) != 1:
        raise ValueError('Non-unique/missing section: ' + heading)
    start = starts[0]
    level = len(lines[start]) - len(lines[start].lstrip(b'#'))
    end = len(lines)
    for i in range(start+1, len(lines)):
        match = re.match(br'^(#+) ', lines[i])
        if match and len(match[1]) <= level:
            end = i
            break
    return b''.join(lines[start:end])


def passage(raw, selection):
    block = section_bytes(raw, selection['heading'])
    lines = block.decode().splitlines(keepends=True)
    hits = [i for i, line in enumerate(lines) if selection['needle'] in line]
    if len(hits) != 1:
        raise ValueError('Non-unique passage needle: ' + selection['needle'])
    start = hits[0]
    end = start + selection.get('line_count', 1)
    if end > len(lines):
        raise ValueError('Passage outside section')
    locator = SOURCE + '#' + selection['heading']
    return block, locator, locator + ';lines=' + str(start+1) + '-' + str(end), ''.join(lines[start:end])


def graph_text(graph):
    prefixes = {'dkg': str(D), 'dgkr': BASE+'id/', 'rdf': str(RDF), 'rdfs': 'http://www.w3.org/2000/01/rdf-schema#', 'owl': 'http://www.w3.org/2002/07/owl#', 'xsd': XSD, 'prov': str(PROV)}
    for key, val in prefixes.items():
        graph.bind(key, Namespace(val), replace=True)
    def key(t):
        return tuple(str(x) for x in t) + (str(getattr(t[2], 'datatype', '') or ''), str(getattr(t[2], 'language', '') or ''))
    return ''.join('@prefix '+p+': <'+v+'> .\n' for p,v in prefixes.items()) + '\n' + '\n'.join(' '.join(n.n3() for n in t)+' .' for t in sorted(graph, key=key)) + '\n'


def build(spec=None, ledger=None):
    spec = spec or strict_load((FIX/'audit_fixture_spec.json').read_text())
    ledger = ledger or strict_load((FIX/'execution_ledger.json').read_text())
    if spec['source_commit'] != PIN or ledger['batch'] != 'm1-audit-fixtures':
        raise ValueError('Unapproved source/batch')
    raw = subprocess.check_output(['git','show',PIN+':'+SOURCE], cwd=ROOT)
    execution = ledger['executions'][0]
    if execution['reference'] != 'm1-audit-fixtures/1':
        raise ValueError('Only the initial recorded execution is admitted by this replay')
    if len({x['reference'] for x in ledger['executions']}) != len(ledger['executions']):
        raise ValueError('Execution reference reuse')
    refs, records, passages = {}, {}, {}
    graph, registry = Graph(), Registry()

    def add(alias, kind, origin, inputs, assertions, provenance):
        if alias in refs:
            raise ValueError('Duplicate alias')
        assertions = normalized_payload(assertions)
        hashed = assertions
        if kind == 'StudyRecord':
            hashed = [a for a in assertions if a['field'] != 'hasPopulationScope']
        elif kind == 'SelectionMembership':
            hashed = [a for a in assertions if a['field'] in {'selectedOccurrence','inSelectionContext'}]
        rec = receipt(kind, origin, inputs, hashed)
        iri = registry.add(rec, hashed)
        refs[alias] = iri
        graph.add((URIRef(iri), RDF.type, PROV.Entity if kind == 'SourceSlice' else D[kind]))
        for a in assertions:
            pred = PROV.wasDerivedFrom if a['field'] == 'prov:wasDerivedFrom' else D[a['field']]
            obj = URIRef(a['value']) if a['form'] == 'iri' else Literal(a['value'], datatype=URIRef(a['datatype']) if a['datatype'] else None, lang=a['language'], normalize=False)
            graph.add((URIRef(iri), pred, obj))
        records[alias] = dict(iri=iri, receipt=rec, canonical=canonical(rec).decode(), identityPayload=hashed, assertions=assertions, passages=provenance, nullReasons={k: ('not-applicable: no disambiguator for this authority referent' if k == 'disambiguator' else 'not-applicable: no project execution claimed for audit transcription' if k == 'execution' else 'reason-unknown: no value asserted from the selected audit passage; see scoped limitations') for k,v in rec['inputs'].items() if v is None})

    # Referent identity is independent of source-description links. Establish it
    # before source slices so citation provenance is navigable in the RDF itself.
    referent_kinds={'Target','Drug','Publication','Study'}
    for record in spec['records']:
        if record['kind'] in referent_kinds:
            add(record['alias'],record['kind'],record['origin'],record['inputs'],record['assertions'],record['passages'])

    for alias, selection in spec['passages'].items():
        block, section_locator, locator, quote = passage(raw, selection)
        sid = 'snapshot:'+selection['heading']
        if sid not in refs:
            h = digest(block)
            add(sid,'SourceSnapshot','audit-transcription', dict(provider='project-audit', dataset=SOURCE, edition=PIN, projection='audit-section-v1', locator=section_locator, artifactDigest=h), [lit('sourceAuthority','project-audit'),lit('snapshotVersion',PIN),lit('sourceLocator',section_locator),lit('artifactDescription','Pinned Git audit section; audit-section-v1; SHA-256 '+h+'. Not an upstream response archive.')], [])
        passages[alias] = dict(snapshot=refs[sid], locator=locator, quote=quote, sectionDigest=digest(block))
        add('slice:'+alias,'SourceSlice','audit-transcription',dict(snapshotKey=refs[sid],locator=locator,scope='Exact attributed project-audit passage'),[link('inSnapshot',refs[sid]),lit('sourceLocator',locator),lit('sourceText',quote),lit('scopeText','Attributed historical project audit; no independent upstream reproduction.')]+([link('citesPublication',refs['pub-'+alias[6:]])] if alias.startswith('paper-') else []),[alias])

    def resolve(value):
        if isinstance(value, str):
            if value.startswith('@'): return refs[value[1:]]
            if value.startswith('$snapshot:'): return passages[value[10:]]['snapshot']
            if value.startswith('$locator:'): return passages[value[9:]]['locator']
            if value.startswith('$quote:'): return passages[value[7:]]['quote']
            if value == '$execution': return execution['reference']
            if value == '$observedAt': return execution['observed_at']
            return value
        if isinstance(value, list): return [resolve(v) for v in value]
        if isinstance(value, dict): return {k:resolve(v) for k,v in value.items()}
        return value
    pending = [r for r in spec['records'] if r['kind'] not in referent_kinds]
    while pending:
        next_pending = []
        for record in pending:
            try:
                inputs, assertions = resolve(record['inputs']), resolve(record['assertions'])
            except KeyError:
                next_pending.append(record)
                continue
            add(record['alias'],record['kind'],record['origin'],inputs,assertions,record['passages'])
        if len(next_pending) == len(pending):
            raise ValueError('Unresolved dependency/cycle: '+str([r['alias'] for r in pending]))
        pending = next_pending
    # Only the approved population attachment is deferred; mappingContext is ordinary.
    for item in spec['population_attachments']:
        owner, population = refs[item['studyRecord']], refs[item['population']]
        graph.add((URIRef(owner),D.hasPopulationScope,URIRef(population)))
        records[item['studyRecord']]['assertions'].append(link('hasPopulationScope',population))
    validate(graph, records)
    return graph, dict(profile='m1-id-1', source_commit=PIN, source_blob_sha256=digest(raw), execution=execution['reference'], records=records, passages=passages, questions=spec['questions'], limitations=spec['limitations'])


def enum_catalogue():
    text=(ROOT/'docs/m1_implementation_mechanics.md').read_text()
    table=text.split('## 4. G03')[1].split('### Operational definitions')[0]
    result={}
    for line in table.splitlines():
        cells=[c.strip() for c in line.split('|')[1:-1]]
        if len(cells)==3 and ' / ' in cells[0] and not cells[0].startswith('Field /'):result[cells[0].split(' / ')[0]]=set(cells[1].split(', '))
    ordinary=set('field:'+x for x in re.findall(r'`field:([^`]+)`',text.split('### 5.1')[1].split('### 5.2')[0]))
    composite=set(re.findall(r'requirement:[a-z-]+',text.split('### 5.2')[1].split('### 5.3')[0]))
    return result, ordinary|composite


def validate(graph, records):
    """Finite structural checks; no biomedical truth or SHACL claim."""
    schema=Graph().parse(ROOT/'ontology/dementiagraph-v.ttl')
    from rdflib.namespace import OWL
    fields=set(schema.subjects(RDF.type,OWL.ObjectProperty))|set(schema.subjects(RDF.type,OWL.DatatypeProperty))
    classes=set(schema.subjects(RDF.type,OWL.Class))
    enums,tokens=enum_catalogue()
    kind={URIRef(r['iri']):r['receipt']['kind'] for r in records.values()}
    owners={'mappingContext':{'MappingRecord'},'mappingInput':{'MappingRecord'},'reportedDestination':{'MappingRecord'},'candidateDestination':{'MappingRecord'},'hasPopulationScope':{'StudyRecord','SourceSlice'},'selectedOccurrence':{'SelectionMembership'},'queryAnchor':{'SelectionContext'},'pathStep':{'HierarchyPath'},'childReference':{'HierarchyStep'},'parentReference':{'HierarchyStep'},'trialStatusText':{'StudyRecord'},'statusDate':{'StudyRecord'},'sourceText':{'MechanismRecord','PopulationScope','StudyRecord','SourceSlice'},'expectedField':{'MissingnessRecord'},'mappingStatus':{'MappingRecord'},'missingnessReason':{'MissingnessRecord'},'dependencyStatus':{'DerivedStatement'}}
    owners.update({'originRole':{'DiseaseTargetAssociation'},'selectionMode':{'SelectionContext','DiseaseTargetAssociation'},'inclusionKind':{'SelectionMembership'},'inspectionDepth':{'InspectionRecord'},'materialKind':{'InspectionRecord'},'accessOutcome':{'InspectionRecord'},'interpretationOutcome':{'InspectionRecord'},'reviewerType':{'InspectionRecord'}})
    for s,p,o in graph:
        if s not in kind: raise ValueError('Undeclared fixture subject')
        if p==RDF.type:
            if o not in classes: raise ValueError('Unapproved class')
            continue
        if p not in fields: raise ValueError('Unapproved predicate')
        name=str(p).removeprefix(str(D))
        if name in owners and kind[s] not in owners[name]: raise ValueError('Wrong owner '+name)
        if p in set(schema.subjects(RDF.type,OWL.ObjectProperty)):
            if not isinstance(o,URIRef) or o not in kind: raise ValueError('Dangling object')
        elif not isinstance(o,Literal): raise ValueError('Nonliteral data value')
        if name in enums and (str(o) not in enums[name] or o.datatype!=URIRef(XSD+'string')): raise ValueError('Invalid enum')
        if name=='expectedField' and str(o) not in tokens: raise ValueError('Invalid missingness field')
        if name=='mappingContext' and kind[o] not in {'EvidenceOccurrence','SourceSlice'}: raise ValueError('Wrong mapping context')
    info=set(kind.values())-{'Target','Drug','Publication','Study'}
    signatures={
        'inSnapshot':(info,{'SourceSnapshot'}),'contextRecord':(info,info),
        'reportedEvidence':({'DiseaseTargetAssociation'},{'EvidenceOccurrence'}),
        'mappingContext':({'MappingRecord'},{'EvidenceOccurrence','SourceSlice'}),
        'mappingInput':({'MappingRecord'},{'DiseaseConceptReference'}),
        'reportedDestination':({'MappingRecord'},{'DiseaseConceptReference'}),
        'candidateDestination':({'MappingRecord'},{'DiseaseConceptReference'}),
        'queryAnchor':({'SelectionContext'},{'DiseaseConceptReference'}),
        'selectedOccurrence':({'SelectionMembership'},{'EvidenceOccurrence'}),
        'inSelectionContext':({'SelectionMembership','DerivedStatement','DiseaseTargetAssociation'},{'SelectionContext'}),
        'justificationPath':({'SelectionMembership'},{'HierarchyPath'}),
        'pathStep':({'HierarchyPath'},{'HierarchyStep'}),
        'childReference':({'HierarchyStep'},{'DiseaseConceptReference'}),
        'parentReference':({'HierarchyStep'},{'DiseaseConceptReference'}),
        'citesPublication':(info,{'Publication'}),'refersToStudy':(info,{'Study'}),
        'indicationStudyRecord':({'ClinicalIndicationRecord'},{'StudyRecord'}),
        'hasPopulationScope':({'StudyRecord','SourceSlice'},{'PopulationScope'}),
        'subjectRecord':({'DerivedStatement'},info),'comparatorRecord':({'DerivedStatement'},info),
        'sharedInput':({'DerivedStatement'},info|{'Study','Publication'}),
        'inspectedRecord':({'InspectionRecord'},info),
        'aboutRecord':({'InspectionRecord','MissingnessRecord'},set(kind.values())),
        'observationContext':({'MissingnessRecord'},{'InspectionRecord','SelectionContext','DerivedStatement'}),
        'hasTarget':({'DiseaseTargetAssociation','EvidenceOccurrence','MechanismRecord'},{'Target'}),
        'hasDrug':({'MechanismRecord','ClinicalIndicationRecord'},{'Drug'}),
        'hasDiseaseReference':({'DiseaseTargetAssociation','ClinicalIndicationRecord'},{'DiseaseConceptReference'}),
    }
    for name,(left,right) in signatures.items():
        for subject,obj in graph.subject_objects(D[name]):
            if kind[subject] not in left or kind[obj] not in right:raise ValueError('Signature violation '+name)
    for subject,obj in graph.subject_objects(PROV.wasDerivedFrom):
        if kind[subject] not in info or kind[obj] not in info:raise ValueError('Wrong derivation participants')
    missing_keys=set()
    for node,k in kind.items():
        for field in enums:
            if len(list(graph.objects(node,D[field])))>1:raise ValueError('Multiple enum states')
        if k=='MappingRecord' and len(list(graph.objects(node,D.mappingContext)))!=1:raise ValueError('Missing mapping context')
        if k=='DerivedStatement' and str(graph.value(node,D.dependencyStatus))=='independence-assessed-with-limits':
            inputs=list(graph.objects(node,PROV.wasDerivedFrom))
            if len(inputs)==2 and set(graph.objects(inputs[0],D.refersToStudy))&set(graph.objects(inputs[1],D.refersToStudy)):
                raise ValueError('Controlled shared-trial inputs do not justify independent confirmation')
        if k=='SelectionMembership':
            for field in ['selectedOccurrence','inSelectionContext']:
                if len(list(graph.objects(node,D[field])))!=1: raise ValueError('Missing membership structure')
            context=graph.value(node,D.inSelectionContext)
            if str(graph.value(context,D.selectionMode))=='direct-only' and str(graph.value(node,D.inclusionKind))=='descendant-selected':raise ValueError('Contradictory selection')
        if k=='MissingnessRecord':
            for field in ['aboutRecord','expectedField','missingnessReason','observationContext','rationale']:
                if len(list(graph.objects(node,D[field])))!=1:raise ValueError('Missing missingness structure')
            owner=graph.value(node,D.aboutRecord)
            if kind[owner]=='MissingnessRecord':raise ValueError('Recursive missingness')
            token=str(graph.value(node,D.expectedField))
            if token.startswith('field:'):
                field=token[6:]
                pred=PROV.wasDerivedFrom if field=='prov:wasDerivedFrom' else D[field]
                if (owner,pred,None) in graph:raise ValueError('Field is present, not missing')
            identity=tuple(graph.value(node,D[f]) for f in ['aboutRecord','expectedField','observationContext','missingnessReason'])
            if identity in missing_keys:raise ValueError('Duplicate missingness observation')
            missing_keys.add(identity)


def decision(graph, records, request):
    """Small controlled question checks, not free-text biomedical adjudication."""
    ref=lambda alias:URIRef(records[alias]['iri'])
    if request=='shared-trial':
        a,b=ref('e-grin1'),ref('e-grin3b')
        shared=set(graph.objects(a,D.refersToStudy))&set(graph.objects(b,D.refersToStudy))
        return 'shared-source-established' if shared else 'unresolved'
    if request=='q03-original':
        m=ref('map-pick')
        return str(graph.value(graph.value(m,D.mappingInput),D.externalIdentifier))
    if request in {'ad-path','ftd-path'}:
        path=records[request]
        steps=path['receipt']['inputs']['stepKeys']
        nodes=[URIRef(x) for x in steps]
        if set(graph.objects(ref(request),D.pathStep))!=set(nodes):return 'not-established-by-bundle'
        pairs=[(graph.value(n,D.childReference),graph.value(n,D.parentReference)) for n in nodes]
        if any(a is None or b is None for a,b in pairs):return 'not-established-by-bundle'
        if any(pairs[i][1]!=pairs[i+1][0] for i in range(len(pairs)-1)):return 'not-established-by-bundle'
        if len({a for a,b in pairs}|{pairs[-1][1]})!=len(pairs)+1:return 'not-established-by-bundle'
        expected={'ad-path':('MONDO:0007088','MONDO:0004975'),'ftd-path':('MONDO:0010857','MONDO:0017276')}[request]
        if tuple(str(graph.value(n,D.externalIdentifier)) for n in [pairs[0][0],pairs[-1][1]])!=expected:return 'not-established-by-bundle'
        return 'complete-for-declared-scope'
    if request=='mapping-ambiguity':
        nodes=[ref(x) for x in ['map-psen-ge','map-mapt-inclusive']]
        original=[graph.value(graph.value(n,D.mappingInput),D.externalIdentifier) for n in nodes]
        destinations=[graph.value(graph.value(n,D.reportedDestination),D.externalIdentifier) for n in nodes]
        return 'mapping-ambiguous' if all(str(graph.value(n,D.mappingStatus))=='unresolved' for n in nodes) and original[0]==original[1] and destinations[0]!=destinations[1] else 'not-assessed'
    if request in {'genetic-confirmation','ftd-treatment','clinical-benefit','current-approval','phase-implies-completion','termination-implies-failure','global-mapping-equivalence','universal-absence'}:
        return 'not-established-by-bundle'
    raise ValueError('Not a frozen controlled request')


def main():
    graph,receipt_bundle=build()
    text=graph_text(graph)
    receipt_bundle['bundle_sha256']=digest(text.encode())
    (FIX/'audit_derived.ttl').write_text(text)
    (FIX/'identity_receipts.json').write_text(json.dumps(receipt_bundle,ensure_ascii=False,indent=2,sort_keys=True)+'\n')
    print(json.dumps(dict(records=len(receipt_bundle['records']),types=dict(Counter(r['receipt']['kind'] for r in receipt_bundle['records'].values())),triples=len(graph)),sort_keys=True))

if __name__=='__main__':main()
