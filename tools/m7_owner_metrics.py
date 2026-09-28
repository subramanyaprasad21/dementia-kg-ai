"""Replay owner-directed annotations through unchanged frozen M7 metric functions.

Offline only. No annotation inference, source acquisition, model calls or changes
of scoring definitions. Annotation provenance remains explicit in the input.
"""
import json
import hashlib
from pathlib import Path
import m7_protocol_checks as frozen

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'experiments/m7-portfolio-challenge-001'


def read(path):return json.loads(Path(path).read_bytes())
def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def calculate(directory=BASE):
    directory=Path(directory);scores=read(directory/'owner-review-scores.json')
    if digest(directory/'owner-review-instructions.txt')!=scores['ownerInstructionSha256']:
        raise ValueError('Owner instruction provenance changed')
    if digest(directory/'verification.json')!=scores['verificationSha256']:
        raise ValueError('Automated verification changed')
    public=read(ROOT/'evaluations/m7-portfolio-challenge-001/questions.json')
    ids=[q['id'] for q in public['items']]
    if [d['id'] for d in scores['details']]!=ids:raise ValueError('Review item scope changed')
    items=[dict(id=d['id'],category='answerable' if n<6 else 'insufficient',requiredFactIds=[f['id'] for f in d['requiredFacts']]) for n,d in enumerate(scores['details'])]
    annotations=scores['annotations']
    for i,d in enumerate(scores['details']):
        g,v=annotations['grounded'][i],annotations['verified'][i]
        for field in ('proseLabels','supportedFactIds','qualificationPass','abstentionPass','excessiveAbstention'):
            if g[field]!=v[field]:raise ValueError('Identical generated prose scored differently')
        for condition in annotations:
            a=annotations[condition][i]
            units=d['prose']['model_only' if condition=='model_only' else 'grounded']['propositions']
            if a['proseLabels']!=[u['label'] for u in units]:raise ValueError('Prose label lineage mismatch')
    result={c:frozen.aggregate(items,a) for c,a in annotations.items()}
    coverage=[]
    for n,record in enumerate(scores['coverage'],1):
        path=directory/f'{n*2:02d}.generation.request.json'
        if digest(path)!=record['requestSha256']:raise ValueError('Frozen retrieval request changed')
        packets=json.loads(read(path)['input'])['packets']
        supplied={line for p in packets for line in p['text'].splitlines()}
        if set(record['requiredSupport'])!=set(items[n-1]['requiredFactIds']):raise ValueError('Coverage fact scope changed')
        coverage.append(dict(id=record['id'],value=frozen.retrieval_coverage(record['requiredSupport'],supplied)))
    return dict(profile='m7-owner-directed-metrics-1',conditions=result,
        pairedPrecision=frozen.paired_precision_difference(items,annotations['grounded'],annotations['verified']),
        groundedRetrievalCoverage=coverage,modelOnlyRetrievalCoverage='NOT-APPLICABLE: intentional no-retrieval condition',
        annotationSha256=digest(directory/'owner-review-scores.json'),
        provenance=scores['provenance'],limitations=['Development-overlapping portfolio challenge; no superiority, clinical or independent-validation claim','Proposition segmentation and source-support witness indexing are owner-directed review operations, not newly frozen gold','Original raw generation and automatic verification artifacts remain unchanged'])

if __name__=='__main__':print(json.dumps(calculate(),indent=2,sort_keys=True))
