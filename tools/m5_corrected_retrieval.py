"""Explicit Q01-Q07 retrieval mapping revision; offline only, no model calls.

Historical m5_pilot_plan and pilot artifacts remain replayable unchanged.
"""
import re
from decimal import Decimal
from rdflib.namespace import RDF
import m5_evidence_answers as ai

D = ai.retrieval.D
OUTPUT = 'assessments/m5-corrected-retrieval-plan.json'
# Exact source IDs from the approved questions, not positional engineering cases.
PSEN = ('1261ad02e3d662cd23a476af47159a1501d01889',
        '986bb22bf0f7858c36fc773e5b45c08cd9c514fd',
        '98c49197e4989f7d3be8b2f8ee3c7699e2f3d6dc')
CLINICAL = ('ed0b04f2d73abb84a48ed87d556725b1743a425c',
            '0d60abae93f3438f8750a76beb2b41de9b6b3efd')
PICK = '04e8f548c45ece0c2d428eef5f5aa149f67f1fbd'
APP = '8bac3794c7e23d4dc3e7b44e3b2e1af8dcccc4fe'
SEMANTIC = '019b39b2b176f9e7df8536022682738d12e32f39'
BUDGET = dict(k=8, max_bytes=196608)
GAPS = {
 'Q01': ['Primary PanelApp edition, article-inspection text and exact text-mining spans are not in these RDF packets.'],
 'Q02': ['Historical datasource composition, registry population/status and adjudicated independence are unavailable.'],
 'Q03': ['Panel edition, primary abstract inspection and upstream normalization method remain unavailable; no Pick parent step is asserted by this frozen five-step slice.'],
 'Q04': ['Historical direct/inclusive counts and complete selection results are non-RDF context, not supplied here. Paths do not prove historical query membership.'],
 'Q05': ['Authoritative mapping adjudication and annotated source-xref detail are not supplied; no canonical repair is justified.'],
 'Q06': ['Mechanism publication inspection and full indication-list completeness are not established by these RDF packets. The association is a bounded project grouping, not a historical aggregate.'],
 'Q07': ['The primary registry population/status, report linkage inside excluded raw description JSON, and mechanism-study inspection are not supplied.']}

def questions():
    document=(ai.corpus.ROOT/'docs/competency_questions.md').read_text()
    sections=re.findall(r'^### (Q0[1-7]) —[^\n]*\n(.*?)(?=^### |^## |\Z)',document,re.MULTILINE|re.DOTALL)
    result={qid:re.search(r'^\*\*.*?\*\* (.+\?)$',block,re.MULTILINE).group(1) for qid,block in sections}
    if len(sections)!=7 or set(result)!={f'Q0{i}' for i in range(1,8)}:
        raise ValueError('Expected exactly the approved seven question identifiers')
    return result

def one(values):
    values=set(values)
    if len(values)!=1:
        raise ValueError('Missing or ambiguous intended query participant')
    return next(iter(values))

def scopes(g):
    def has(s,p,text): return text in {str(v) for v in g.objects(s,p)}
    def typed(t): return set(g.subjects(RDF.type,D[t]))
    def evidence(ident):
        return one({s for s in typed('EvidenceOccurrence') if has(s,D.sourceRecordIdentifier,ident)})
    def mapping(ident): return one(typed('MappingRecord') & set(g.subjects(D.mappingContext,evidence(ident))))
    def drug(t,ident):
        found={s for s in typed(t) for d in g.objects(s,D.hasDrug) if has(d,D.externalIdentifier,ident)}
        if not found: raise ValueError('Missing drug query records')
        return found
    def hierarchy(child):
        return one(s for s in typed('HierarchyStep') for d in g.objects(s,D.childReference) if has(d,D.externalIdentifier,child))
    mapts=one(s for s in typed('DiseaseTargetAssociation') for t in g.objects(s,D.hasTarget) if has(t,D.externalIdentifier,'ENSG00000186868'))
    dependency=one(s for s in typed('DerivedStatement') if set(g.objects(s,D.subjectRecord))=={evidence(CLINICAL[1])} and set(g.objects(s,D.comparatorRecord))=={evidence(CLINICAL[0])})
    missing={s for s in typed('MissingnessRecord') if set(g.objects(s,D.aboutRecord)) & {mapping(i) for i in PSEN[:2]}}
    selected={
      'Q01': {mapping(i) for i in PSEN}|missing,
      'Q02': {mapping(i) for i in CLINICAL}|drug('MechanismRecord','CHEMBL807')|{dependency},
      'Q03': {mapping(PICK)},
      'Q04': {mapping(i) for i in (APP,SEMANTIC,PICK)}|{hierarchy(i) for i in ('MONDO:0007088','MONDO:0015140','MONDO:0100087','MONDO:0010857','MONDO:0017160')},
      'Q05': {mapping(PSEN[2]),mapping(SEMANTIC),hierarchy('MONDO:0010857'),hierarchy('MONDO:0017160')},
      'Q06': {mapts}|drug('MechanismRecord','CHEMBL4298021')|drug('ClinicalIndicationRecord','CHEMBL4298021')|drug('MechanismRecord','CHEMBL3833321')|drug('ClinicalIndicationRecord','CHEMBL3833321'),
      'Q07': drug('MechanismRecord','CHEMBL3990042')|drug('ClinicalIndicationRecord','CHEMBL3990042')}
    expected={'Q01':5,'Q02':5,'Q03':1,'Q04':8,'Q05':4,'Q06':6,'Q07':2}
    if {q:len(s) for q,s in selected.items()} != expected:
        raise ValueError('Unexpected finite query scope; review rather than truncate')
    return {q:sorted(map(str,s)) for q,s in selected.items()}

def prepare(qid, mode='hybrid'):
    g=ai.corpus.load(); roots=scopes(g)[qid]
    types=sorted({str(t) for s in roots for t in g.objects(ai.retrieval.URIRef(s),RDF.type)})
    p=ai.prepare(questions()[qid],[],mode,types,allowed_roots=roots,**BUDGET)
    if {r['packet']['id'] for r in p['retrieval']['results']}!=set(roots) or p['retrieval']['skippedForBudget']:
        raise ValueError('Intended query context omitted; no silent truncation or fallback')
    return p

def build():
    old=ai.corpus.read(ai.corpus.ROOT/'assessments/m5-pilot-plan.json')
    historical={q['questionId']:q for q in old['questions']}
    rows=[]
    for qid,question in sorted(questions().items()):
        p=prepare(qid)
        assert question==historical[qid]['question']
        requests={c:dict(sha256=ai.corpus.digest(ai.corpus.encode(ai.request_for(p,c))),bytes=len(ai.corpus.encode(ai.request_for(p,c)))) for c in ('model_only','retrieval')}
        assert requests['model_only']['sha256']==historical[qid]['requests']['model_only']['sha256']
        rows.append(dict(questionId=qid,question=question,allowedRoots=p['retrieval']['allowedRoots'],recordTypes=p['retrieval']['recordTypes'],
                         packets=[dict(id=r['packet']['id'],sha256=r['packet']['sha256']) for r in p['retrieval']['results']],
                         usedPacketBytes=p['retrieval']['budget']['usedPacketBytes'],requests=requests,gaps=GAPS[qid],
                         completeQuestionSupport=False,reuseModelOnly=(qid!='Q07'),
                         retrievalChanged=requests['retrieval']['sha256']!=historical[qid]['requests']['retrieval']['sha256']))
    calls=8
    request_bytes=sum(q['requests']['retrieval']['bytes'] for q in rows)+rows[-1]['requests']['model_only']['bytes']
    return dict(profile='m5-question-retrieval-revision-2',liveAuthorized=False,questions=rows,retrievalBudget=BUDGET,
                corpusManifestSha256=ai.corpus.digest((ai.corpus.ROOT/ai.corpus.MANIFEST).read_bytes()),
                followup=dict(generations=calls,serializedRequestBytes=request_bytes,
                              roughInputTokenRange=[(request_bytes+3)//4,(request_bytes+1)//2],
                              tokenEstimateMethod='Heuristic 2-4 UTF-8 bytes/token, not a tokenizer result or guarantee; authorized API counting must enforce actual ceiling',inputTokensCeiling=800000,outputTokensCeiling=32768,
                              standardTokenCostCeilingUSD=str((Decimal(800000)*2+Decimal(32768)*10)/1000000),
                              pricingBasis='Previously approved $2/M input and $10/M output; not freshly checked offline',
                              requestsIncludingCounting=16,proposedCumulativeGenerationAttempts=22,proposedCumulativeHTTPRequests=44,
                              cumulativeConservativeInputTokens=917141,cumulativeConservativeOutputTokens=48529,
                              cumulativeReservationUpperBoundUSD='2.735402',
                              priorAccountingReference='experiments/m5-development-pilot-001/ledger.json',
                              modelOnlyReused=['Q01','Q02','Q03','Q04','Q05','Q06'],newModelOnly=['Q07'],newGrounded=list(questions()),
                              verification='Same grounded output locally checked, no extra generation'),
                limitations=['Development only; no relevance labels, accuracy claims or held-out evaluation',
                             'Explicit finite query candidates; not a benchmark of unrestricted retrieval ranking',
                             'Equal grounded context for retrieval and verified conditions; model-only intentionally has no KG',
                             'Packet budget is now 8/192KiB to avoid truncating approved multi-record questions; API per-call token cap remains 100000',
                             'Historical pilot and M4 engineering controls are unchanged'])

if __name__=='__main__':
    print(ai.corpus.encode(build()).decode(),end='')
