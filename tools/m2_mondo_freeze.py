"""Offline manifest for one approved capture; never fetch, repair or ingest data."""
import argparse
import json
from pathlib import Path
import m2_mondo_capture as capture

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ARTIFACTS = Path('/Users/subramanyaprasad/dementia-kg-ai-source-captures/mondo-pilot-001')
DEFAULT_MANIFEST = ROOT / 'manifests/mondo-pilot-001.freeze.json'
BASELINE = '699f5347d56fb050a1dd58a1fd72121f8e5b0a93'
LEDGER_HASH = '6238dc242bf3207999b379da2d491d9c711e92aca36a473d8f37e76c7ac1792e'
# Independent frozen requirements, not inferred from whichever rows happen to exist.
TERMS = ['MONDO:0004975','MONDO:0017276','MONDO:0008243','MONDO:0010857',
         'MONDO:0017160','MONDO:0007088','MONDO:0015140','MONDO:0100087']
PARENTS = [('MONDO:0010857','MONDO:0017160'),('MONDO:0017160','MONDO:0017276'),
           ('MONDO:0007088','MONDO:0015140'),('MONDO:0015140','MONDO:0100087'),
           ('MONDO:0100087','MONDO:0004975')]
CONTRACT_FILES = ('tools/m2_mondo_capture.py','tests/test_m2_mondo_capture.py','docs/m2_mondo_pilot.md')


def require(condition, message):
    if not condition: raise capture.Stop(message)


def serialize(manifest):
    """Existing JCS subset, UTF-8, exactly one trailing LF; no creation clock."""
    return capture.canonical(manifest) + b'\n'


def build(artifacts=DEFAULT_ARTIFACTS):
    artifacts = Path(artifacts)
    raw_ledger = (artifacts/'ledger.json').read_bytes()
    require(capture.sha(raw_ledger) == LEDGER_HASH, 'Pinned acquisition ledger changed')
    ledger = json.loads(raw_ledger)
    replay = capture.replay(artifacts)
    require(ledger['batch'] == 'mondo-pilot-001', 'Wrong batch')
    require([r['id'] for r in replay['results'] if 'id' in r] == TERMS, 'Term allowlist differs')
    require(len({r['captureId'] for r in ledger['records']}) == 15, 'Capture identity count')
    require(len({r['descriptionId'] for r in ledger['records']}) == 14, 'Description identity count')
    require(replay['sourceContext'] == {
        'edition':'2026-09-01',
        'versionIri':'http://purl.obolibrary.org/obo/mondo/releases/2026-09-01/mondo-international.owl',
        'loaded':'2026-09-24T00:09:08.017393439','updated':'2026-09-24T00:09:08.017393439'},
        'Approved source context differs')
    responses, assertions = [], []
    extra_count = 0
    for entry in ledger['records']:
        receipt = entry['receipt']
        name = entry['rawFile']
        require(Path(name).name == name, 'Artifact name must be relative basename')
        raw = (artifacts/name).read_bytes()
        require(capture.sha(raw) == receipt['rawSha256'], 'Raw digest differs')
        require(receipt['license'] == ledger['license'] == capture.LICENSE, 'Permission metadata differs')
        responses.append({'slot':receipt['slot'],'artifact':name,
                          'bytes':str(len(raw)),'sha256':capture.sha(raw),
                          'captureId':entry['captureId'],'captureReceipt':receipt,
                          'descriptionId':entry['descriptionId'],
                          'descriptionReceipt':entry['descriptionReceipt']})
        if receipt['slot'].startswith('parents-'):
            child = 'MONDO:'+receipt['slot'][8:]
            parent = dict(PARENTS)[child]
            rows = json.loads(raw)['_embedded']['terms']
            accepted = [str(i) for i,row in enumerate(rows) if row.get('obo_id') == parent]
            excluded = [str(i) for i,row in enumerate(rows) if row.get('obo_id') not in TERMS]
            require(len(accepted) == 1 and len(accepted)+len(excluded) == len(rows),
                    'Unexpected additional in-scope parent or duplicate assertion')
            require(len(entry['payload']['parents']) == 1, 'Parent projection expanded')
            extra_count += len(excluded)
            assertions.append({'child':child,'parent':parent,'responseSlot':receipt['slot'],
                               'acceptedRowPointers':['/_embedded/terms/'+i for i in accepted],
                               'excludedRawRowPointers':['/_embedded/terms/'+i for i in excluded],
                               'status':'verified-source-reported-parent'})
    require([(a['child'],a['parent']) for a in assertions] == PARENTS, 'Parent allowlist differs')
    require(extra_count == 6, 'Excluded row count differs')
    return {
        'profile':'m2-mondo-slice-freeze-1','sliceId':'mondo-pilot-001',
        'scope':'Mondo-only captured OLS slice; full M2.1 corpus incomplete',
        'baselineCommit':BASELINE,
        'provider':'EMBL-EBI OLS','ontology':'Mondo Disease Ontology',
        'sourceContext':replay['sourceContext'],
        'capturePeriod':{'started':ledger['started'],'ended':ledger['ended']},
        'artifactRootHint':str(DEFAULT_ARTIFACTS),
        'ledger':{'artifact':'ledger.json','sha256':LEDGER_HASH,'bytes':str(len(raw_ledger))},
        'contracts':{'capture':'m2-capture-1','description':'m2-source-description-1',
                     'projection':'mondo-ols-minimum-1','serialization':'JCS-subset-UTF8-plus-LF',
                     'baselineFiles':[{'path':p,'sha256':capture.sha((ROOT/p).read_bytes())}
                                      for p in CONTRACT_FILES]},
        'terms':TERMS,'parentAssertions':assertions,'responses':responses,
        'inventory':{'rawResponses':'15','rawResponseBytes':str(ledger['bytes']),
                     'captures':'15','distinctDescriptions':'14','excludedParentRows':'6'},
        'permissions':ledger['license'],
        'retention':{'rawBodies':'outside-Git; preserve unchanged with acquisition ledger',
                     'relocation':'override artifact root at verification; preserve basenames and bytes',
                     'redistribution':'not performed; CC-BY-4.0 attribution and changes disclosure required'},
        'limitations':[
            'Open Targets 26.06 bounded historical access remains blocked/unverified.',
            'Full M2.1 acquisition incomplete; this does not freeze the full source corpus.',
            'New OLS capture of declared edition, not reproduction of earlier audit responses.',
            'No complete Mondo release artifact reproduction or biomedical adjudication claimed.',
            'Two uninstrumented preparatory web lookups remain disclosed; their byte totals are unknown.',
            '15 requests / 130541 bytes covers instrumented batch only, not all prior network activity.',
            'Excluded parent rows remain raw provenance only; no additional research assertions.',
            'No M2.3 extraction, normalization, alignment, RDF generation or descendant closure.']}


def verify(manifest=DEFAULT_MANIFEST, artifacts=DEFAULT_ARTIFACTS):
    raw = Path(manifest).read_bytes()
    # parse rejects duplicate keys; serialization rejects untyped numeric/boolean values.
    parsed = capture.parse(raw)
    require(raw == serialize(parsed), 'Noncanonical manifest serialization')
    expected = build(artifacts)
    require(raw == serialize(expected), 'Freeze manifest differs from pinned artifacts/contracts')
    return {'status':'pass','manifestSha256':capture.sha(raw),
            'inventory':expected['inventory'],'ledgerSha256':LEDGER_HASH}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation',choices=['build','verify'])
    parser.add_argument('--artifacts',type=Path,default=DEFAULT_ARTIFACTS)
    parser.add_argument('--manifest',type=Path,default=DEFAULT_MANIFEST)
    args = parser.parse_args()
    if args.operation == 'build':
        content = serialize(build(args.artifacts))
        args.manifest.parent.mkdir(parents=True,exist_ok=True)
        # Never silently overwrite a frozen manifest, even when it appears identical.
        with args.manifest.open('xb') as target: target.write(content)
    print(json.dumps(verify(args.manifest,args.artifacts),indent=2))
