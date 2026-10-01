"""Offline, hash-pinned qualified corpus; no new source or identity profile."""
import argparse
import hashlib
import json
from pathlib import Path
from rdflib import Graph
import m2_mondo_rdf as rdf

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = 'manifests/dementia-development-001.json'
RELEASES = [f'manifests/{name}.kg-release.json' for name in
            ('mondo-pilot-001', 'ot2606-evidence-001', 'ot2606-context-001')]
GRAPHS = ['kg/mondo-pilot-001/records.ttl', 'kg/mondo-pilot-001/provenance.ttl',
          'kg/ot2606-evidence-001/records.ttl', 'kg/ot2606-evidence-001/provenance.ttl',
          'kg/ot2606-context-001/records.ttl']
CONTEXT = ['assessments/ot2606-context-001.selections.json',
           'extractions/ot2606-association-001.partial.json',
           'assessments/primary-evidence-001.inspection.json',
           'assessments/dementia-design-answers.json',
           'assessments/continued-m2-readiness.json',
           'manifests/ot2606-association-001.attempt.json',
           'manifests/primary-evidence-001.attempt.json',
           'docs/m2_closure_decision.md']
GAPS = ['Historical PanelApp 265/PSEN1, 474/MAPT and 540/MAPT editions',
        'Historical NCT00594737 and NCT03658135 population/status',
        'FTD GRIN1/GRIN3B datasource composition',
        'PMID33303932 body inspection']


def digest(data):
    return hashlib.sha256(data).hexdigest()


def encode(value):
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False) + '\n').encode()


def read(path):
    return json.loads(path.read_bytes())


def graph(root=ROOT):
    result = Graph()
    for name in GRAPHS:
        result.parse(root / name, format='turtle')
    return result


def build(root=ROOT):
    files = {}
    for name in RELEASES:
        release = read(root / name)
        pins = release['files']
        if isinstance(pins, list):
            pins = {p['path']: p['sha256'] for p in pins}
        for path, expected in pins.items():
            if digest((root / path).read_bytes()) != expected:
                raise ValueError('Historical release mismatch: ' + path)
            if path in files and files[path] != expected:
                raise ValueError('Conflicting release pin: ' + path)
            files[path] = expected
    for name in RELEASES + GRAPHS + CONTEXT:
        files[name] = digest((root / name).read_bytes())
    g = graph(root)
    if (len(set(g.subjects())), len(g)) != (191, 1112):
        raise ValueError('Unexpected qualified corpus inventory')
    return dict(profile='qualified-development-corpus-1', files=files,
                graphFiles=GRAPHS, nonRdfContextFiles=CONTEXT,
                graphSha256=digest(rdf.serialize(g)), resources=191, triples=1112,
                unresolved=GAPS, fullCorpusComplete=False, heldOut=False,
                acceptance='owner-approved-qualified-development',
                rawSourceReplay='Separate existing release tools and external raw artifacts required; no network fallback',
                scope='Frozen Mondo slice plus historical OT26.06 evidence/context; design material only')


def verify(root=ROOT):
    manifest = read(root / MANIFEST)
    if manifest != build(root):
        raise ValueError('Development manifest differs from verified inputs')
    return manifest


def load(root=ROOT):
    verify(root)
    return graph(root)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation', choices=['build', 'verify'])
    args = parser.parse_args()
    if args.operation == 'build':
        with (ROOT / MANIFEST).open('xb') as stream:
            stream.write(encode(build()))
    print(json.dumps({k: v for k, v in verify().items() if k != 'files'}, indent=2))
