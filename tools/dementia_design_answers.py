"""Finite design-question evidence interface, not an LLM or held-out benchmark.

Reads existing RDF assertions and verified source intermediates. Does not mint
new identities, claim a complete corpus, or activate M3/M4.
"""
import argparse
from pathlib import Path
import json
from rdflib import Graph
import ot2606_context as context
import ot2606_source as source
import ot2606_rdf as rdf
from validate_ot2606 import answers as evidence_answers


def inputs():
    data=context.extract()
    source.require(source.serialize(data)==(source.ROOT/'extractions/ot2606-context-001.json').read_bytes(),'Changed context intermediate')
    rdf.verify()
    graph=Graph().parse(rdf.OUT/'records.ttl',format='turtle')
    graph.parse(rdf.OUT/'provenance.ttl',format='turtle')
    return evidence_answers(graph),data,context.selections()


def answer(question, evidence, data, selections):
    source.require(question in {'Q01','Q02','Q03','Q04','Q05','Q06','Q07'},'Unknown design question')
    source.require(data['edition']=='26.06','Incompatible context release')
    rows=[(r,source.untyped(r['sourceValues'])) for r in data['records']]
    result=dict(question=question,status='PARTIAL',facts=[],support=[],unanswered=[],
                limitations=['Design question, not held-out evaluation. Source support does not establish biomedical truth.'])
    def add(fact,ref):
        result['facts'].append(fact);result['support'].append(ref)
    def source_rows(table,predicate):
        return [(r,v) for r,v in rows if r['partition']==table and predicate(v)]
    def addrow(fact,record):
        add(fact,dict(kind='source-row',locator=record['lineage'],sourceValueSha256=record['sourceValueSha256']))
    if question in {'Q01','Q03','Q05'}:
        ids={'Q01':['1261ad02e3d662cd23a476af47159a1501d01889','986bb22bf0f7858c36fc773e5b45c08cd9c514fd','98c49197e4989f7d3be8b2f8ee3c7699e2f3d6dc'],
             'Q03':['04e8f548c45ece0c2d428eef5f5aa149f67f1fbd'],
             'Q05':['98c49197e4989f7d3be8b2f8ee3c7699e2f3d6dc','019b39b2b176f9e7df8536022682738d12e32f39']}[question]
        for ident in ids:
            if ident in evidence:add(evidence[ident],dict(kind='rdf-evidence',sourceRecordId=ident))
            else:result['unanswered'].append('Missing evidence '+ident)
        result['unanswered'].append('Historical PanelApp context and biomedical mapping validity are not established.')
        if question=='Q01':result['unanswered'].append('Independent full-text inspection and causal interpretation are not established.')
    elif question=='Q02':
        ids=['ed0b04f2d73abb84a48ed87d556725b1743a425c','0d60abae93f3438f8750a76beb2b41de9b6b3efd']
        present=[evidence[i] for i in ids if i in evidence]
        if len(present)==2:
            shared=sorted(set(present[0]['studyLocators']) & set(present[1]['studyLocators']))
            add(dict(sharedReportLocators=shared,interpretation='Shared report support only; not independent confirmation.'),dict(kind='rdf-comparison',sourceRecordIds=ids))
        else:result['unanswered'].append('Two source occurrences required for shared-report comparison.')
        for r,v in source_rows('drug_mechanism_of_action',lambda v:'CHEMBL807' in v['chemblIds']):
            selected=sorted(set(v['targets']) & {'ENSG00000176884','ENSG00000116032'})
            addrow(dict(drug='CHEMBL807',mechanism=v['mechanismOfAction'],boundedTargets=selected,targetType=v['targetType']),r)
        result['unanswered'].append('Historical datasource composition and primary registry population/status remain unavailable.')
    elif question=='Q04':
        for selection in selections:
            add(dict(anchor=selection['anchor'],target=selection['target'],mode=selection['mode'],count=selection['count'],members=selection['members']),dict(kind='local-selection',hierarchyFileSha256=selection['hierarchyFileSha256'],evidenceFileSha256=selection['evidenceFileSha256'],method=selection['method']))
        result['status']='SUPPORTED-BOUNDED-COMPUTATION' if len(selections)==4 else 'PARTIAL'
        result['limitations'].append('New local operation, not historical GraphQL session replay; no new descendant graph closure.')
    else:
        drugs=['CHEMBL4298021','CHEMBL3833321'] if question=='Q06' else ['CHEMBL3990042']
        for r,v in source_rows('drug_mechanism_of_action',lambda v:bool(set(v['chemblIds']) & set(drugs))):
            addrow(dict(statementType='mechanism',drugIds=sorted(set(v['chemblIds']) & set(drugs)),mechanism=v['mechanismOfAction'],targets=v['targets'],references=v['references']),r)
        for r,v in source_rows('clinical_indication',lambda v:v['drugId'] in drugs):
            addrow(dict(statementType='indication',**v),r)
        if question=='Q06':
            # The verified extraction queries ALL zagotenemab rows in the whole
            # indication file. This absence claim requires that extent receipt.
            expected=source.load(source.ROOT/'extractions/ot2606-context-001.json')
            actual=[r for r in data['records'] if r['partition']=='clinical_indication' and source.untyped(r['sourceValues'])['drugId']=='CHEMBL4298021']
            frozen=[r for r in expected['records'] if r['partition']=='clinical_indication' and source.untyped(r['sourceValues'])['drugId']=='CHEMBL4298021']
            if actual==frozen and actual:
                add(dict(exactFTDIndicationInInspectedList=any(source.untyped(r['sourceValues'])['diseaseId']=='MONDO_0017276' for r in actual)),dict(kind='complete-bounded-list',extractionSha256=source.sha(source.serialize(expected))))
            else:result['unanswered'].append('Inspected list completeness unavailable; no absence assertion.')
            result['unanswered'].append('Historical FTD/MAPT aggregate and independent publication interpretation remain unavailable.')
        else:result['unanswered'].append('Registry population, eligibility, dated status and clinical efficacy cannot be answered from an indication or mechanism.')
        result['limitations'].append('Mechanism, indication stage, trial status and efficacy are distinct; no treatment conclusion.')
    if not result['facts']:result['status']='UNANSWERED'
    return result


def run():
    evidence,data,selections=inputs()
    return {q:answer(q,evidence,data,selections) for q in ['Q01','Q02','Q03','Q04','Q05','Q06','Q07']}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('question',choices=['all','Q01','Q02','Q03','Q04','Q05','Q06','Q07'],default='all',nargs='?');args=parser.parse_args()
    result=run();print(source.serialize(result if args.question=='all' else result[args.question]).decode())
