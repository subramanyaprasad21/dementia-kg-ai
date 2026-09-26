"""Offline request/budget plan only. No API calls and no model results."""
import argparse
import re
from decimal import Decimal
import m5_evidence_answers as ai
from m5_openai_adapter import LIMITS
from replay_development_retrieval import CASES

OUTPUT = 'assessments/m5-pilot-plan.json'


def build():
    document = (ai.corpus.ROOT/'docs/competency_questions.md').read_text()
    sections = re.findall(r'^### (Q0[1-7]) —[^\n]*\n(.*?)(?=^### |^## |\Z)', document, re.MULTILINE | re.DOTALL)
    questions = [re.search(r'^\*\*.*?\*\* (.+\?)$', block, re.MULTILINE).group(1) for _, block in sections]
    if len(questions) != 7:
        raise ValueError('Approved seven design questions could not be located exactly')
    rows = []
    for case, question in zip(CASES[:7], questions):
        p = ai.prepare(question, case['anchors'], 'hybrid', [str(ai.retrieval.D[t]) for t in case['types']])
        rows.append(dict(questionId=case['id'][:3], question=question,
                         anchors=case['anchors'], recordTypes=case['types'],
                         evidencePackets=len(p['retrieval']['results']),
                         requests={condition: dict(sha256=ai.corpus.digest(ai.corpus.encode(ai.request_for(p, condition))),
                                                   bytes=len(ai.corpus.encode(ai.request_for(p, condition))))
                                   for condition in ['model_only', 'retrieval']}))
    calls = 2*len(rows)
    input_cap = calls*LIMITS['inputTokensPerCall']
    output_cap = calls*LIMITS['outputTokensPerCall']
    maximum = (Decimal(input_cap)*Decimal(LIMITS['inputUSDPerMillion'])+
               Decimal(output_cap)*Decimal(LIMITS['outputUSDPerMillion']))/1000000
    return dict(profile='m5-offline-pilot-plan-1', liveAuthorized=False, model=ai.MODEL,
                promptVersion=ai.PROMPT_VERSION, questions=rows, generationCalls=calls,
                countRequests=calls, maxHTTPRequests=2*calls, totalInputTokenCeiling=input_cap,
                totalOutputTokenCeiling=output_cap, standardTokenCostCeilingUSD=str(maximum),
                proposedSpendCeilingUSD=LIMITS['reservedUSD'], limits=LIMITS,
                actualModelCalls=0, actualInputTokens=None, actualOutputTokens=None,
                conditions=['model_only', 'retrieval', 'verified-postprocessing-of-identical-retrieval-output'],
                limitations=['Exposed Q01-Q07 only; no held-out evaluation or superiority test',
                             'Manual retrieval anchors select partial RDF support, not complete Q01-Q07 evidence',
                             'Token ceilings are planning bounds; exact input counts require authorized API counting',
                             'Alias model is not a pinned immutable snapshot; returned model and raw responses must be retained',
                             'Pricing must be rechecked before approval/execution; no retry or paid repair loops'])


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--write', action='store_true')
    args = p.parse_args()
    data = ai.corpus.encode(build())
    if args.write:
        with (ai.corpus.ROOT/OUTPUT).open('xb') as stream:
            stream.write(data)
    else:
        print(data.decode(), end='')
