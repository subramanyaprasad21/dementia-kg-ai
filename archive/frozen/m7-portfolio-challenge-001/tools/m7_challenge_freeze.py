"""Offline integrity checks for the owner-approved overlapping challenge set.

No model client. Private rubric content is never used to build model requests.
The historical holdout validator remains unchanged and is not bypassed under
its old designation: this is a distinct, explicitly overlapping protocol.
"""
import argparse
import hashlib
import json
from pathlib import Path
import development_corpus as corpus
import m5_evidence_answers as ai
import m5_corrected_retrieval as development
import m7_protocol_checks as metrics

BASE = corpus.ROOT / 'evaluations/m7-portfolio-challenge-001'
DESIGNATION = 'Development-overlapping portfolio challenge set'

def read(path):
    return json.loads(Path(path).read_bytes())

def check_digest(path, expected):
    if hashlib.sha256(Path(path).read_bytes()).hexdigest() != expected:
        raise ValueError('Frozen artifact digest mismatch: ' + Path(path).name)

def validate_public(data):
    if set(data) != {'profile', 'designation', 'heldOut', 'items'}:
        raise ValueError('Unexpected public fields; keep rubric private')
    if data['profile'] != 'm7-portfolio-questions-1' or data['designation'] != DESIGNATION or data['heldOut'] is not False:
        raise ValueError('Wrong evaluation designation')
    if [x['id'] for x in data['items']] != [f'M7-{i:02d}' for i in range(1,13)]:
        raise ValueError('Twelve ordered owner questions required')
    seen = set()
    for n, item in enumerate(data['items'], 1):
        if set(item) != {'id','question','intendedCategory','rootIds'}:
            raise ValueError('Private or unexpected item fields')
        question = item['question']
        if not isinstance(question,str) or not question.strip() or len(question.encode()) > 4096 or question in seen:
            raise ValueError('Invalid question text')
        seen.add(question)
        if item['intendedCategory'] != ('answerable' if n <= 6 else 'qualification-abstention'):
            raise ValueError('Owner allocation changed')
        if not item['rootIds'] or len(item['rootIds']) > 8 or sorted(set(item['rootIds'])) != item['rootIds']:
            raise ValueError('Invalid fixed retrieval scope')
    return True

def verify_private(manifest, directory):
    directory = Path(directory)
    for name, digest in manifest['privateFiles'].items():
        if Path(name).name != name:
            raise ValueError('Unsafe private artifact path')
        check_digest(directory/name,digest)
    rubric=read(directory/'rubric.json')
    if rubric['frozen'] is not True or rubric['authorship'] != 'assistant-prepared; owner-authored questions; no independent gold authorship':
        raise ValueError('Wrong rubric status/authorship')
    if rubric['independentReviewCompleted'] or rubric['individualHumanReferenceReviewAttested']:
        raise ValueError('Unwarranted review attestation')
    return rubric

def verify(private_directory=None):
    manifest=read(BASE/'freeze.json')
    for name,digest in manifest['publicFiles'].items():
        check_digest(corpus.ROOT/name,digest)
    corpus.verify()
    protocol=read(BASE/'protocol.json'); metrics.budget(protocol)
    data=read(BASE/'questions.json');validate_public(data)
    receipts=read(BASE/'retrieval-checks.json')
    if protocol['designation']!=DESIGNATION or protocol['executionAuthorized'] is not False:
        raise ValueError('Freeze is not live execution authorization')
    rubric=verify_private(manifest,private_directory) if private_directory else None
    if rubric and [x['id'] for x in rubric['items']] != [x['id'] for x in data['items']]:
        raise ValueError('Private/public item mismatch')
    dev={metrics.canonical_question(q) for q in development.questions().values()}
    for item,receipt in zip(data['items'],receipts):
        if metrics.canonical_question(item['question']) in dev:
            raise ValueError('Unexpected exact development wording duplicate')
        # Deliberately only public question and roots cross this boundary.
        prepared=ai.prepare(item['question'],allowed_roots=item['rootIds'],k=8,max_bytes=196608)
        baseline=ai.request_for(prepared,'model_only')
        grounded=ai.request_for(prepared,'retrieval')
        if grounded!=ai.request_for(prepared,'verified'):
            raise ValueError('Grounded conditions differ')
        if json.loads(baseline['input'])!={'question':item['question']}:
            raise ValueError('Evidence leaked into model-only condition')
        if {x['packet']['id'] for x in prepared['retrieval']['results']}!=set(item['rootIds']):
            raise ValueError('Missing intended retrieval root')
        actual=dict(id=item['id'],modelOnlyRequestSha256=corpus.digest(corpus.encode(baseline)),
                    groundedRequestSha256=corpus.digest(corpus.encode(grounded)),
                    packetSha256={x['packet']['id']:x['packet']['sha256'] for x in prepared['retrieval']['results']},
                    usedPacketBytes=prepared['retrieval']['budget']['usedPacketBytes'])
        if actual!=receipt:raise ValueError('Request/packet replay mismatch')
        if rubric:
            private=next(x for x in rubric['items'] if x['id']==item['id'])
            if private['question']!=item['question'] or private['retrievalScope']['rootIds']!=item['rootIds']:
                raise ValueError('Private text/scope mismatch')
    if len(receipts)!=12:raise ValueError('Missing receipts')
    return dict(questions=12,designation=DESIGNATION,publicIntegrity=True,
                privateIntegrity=('verified' if rubric else 'not-checked'),apiCalls=0)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--private-directory');args=p.parse_args()
    print(json.dumps(verify(args.private_directory),indent=2))
