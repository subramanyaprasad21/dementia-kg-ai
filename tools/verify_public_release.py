"""Offline public-release verification; no source acquisition or model calls."""
import json
from pathlib import Path

import development_corpus as corpus
import frozen_snapshots as frozen
import m7_challenge_freeze as m7

ROOT = Path(__file__).resolve().parents[1]


def verify():
    historical = {
        'ot2606Authorities': len(frozen.verify_manifest_section(
            ROOT / 'manifests/ot2606-evidence-001.freeze.json',
            'authorities', 'ot2606-evidence-001')),
        'developmentAuthorities': len(frozen.verify_manifest_section(
            ROOT / 'manifests/dementia-development-001.json',
            'files', 'dementia-development-001')),
        'm7PublicAuthorities': len(frozen.verify_manifest_section(
            ROOT / 'evaluations/m7-portfolio-challenge-001/freeze.json',
            'publicFiles', 'm7-portfolio-challenge-001')),
    }
    development = corpus.verify()
    evaluation = m7.verify()
    return {
        'historicalSnapshots': historical,
        'developmentCorpus': {
            'resources': development['resources'],
            'triples': development['triples'],
            'graphSha256': development['graphSha256'],
        },
        'm7': evaluation,
        'networkCalls': 0,
    }


if __name__ == '__main__':
    print(json.dumps(verify(), indent=2))
