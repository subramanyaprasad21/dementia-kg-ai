"""Offline M2.3 source-faithful intermediate; no normalization, alignment or RDF."""
import argparse
import json
from pathlib import Path
import m2_mondo_freeze as freeze

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_HASH = 'b7763d83f41e61c9d8bc617189dc04826609926f83e480289e33f4ac9cc8bb0a'
CONTRACT = 'mondo-extraction-1'
OUTPUT = ROOT/'extractions/mondo-pilot-001.json'
FREEZE_REF = {'path':'manifests/mondo-pilot-001.freeze.json','sha256':MANIFEST_HASH,
              'commit':'cc2da11315710b436472305a86fbb898408c5d81'}
capture = freeze.capture


def extract(artifacts=freeze.DEFAULT_ARTIFACTS, manifest=freeze.DEFAULT_MANIFEST):
    # No record is extracted until every input and original identity verifies.
    raw_manifest=Path(manifest).read_bytes()
    freeze.require(capture.sha(raw_manifest)==MANIFEST_HASH,'Approved manifest digest differs')
    freeze.verify(manifest,artifacts)
    frozen=json.loads(raw_manifest)
    artifacts=Path(artifacts)
    entries={e['slot']:e for e in frozen['responses']}
    # Read/rehash the exact bytes used for extraction, guarding replacement after replay.
    sources={}
    for slot,e in entries.items():
        raw=(artifacts/e['artifact']).read_bytes()
        freeze.require(capture.sha(raw)==e['sha256'],'Response changed after verification')
        sources[slot]=capture.parse(raw)

    def lineage(slot,pointer):
        e=entries[slot]
        return {'freeze':FREEZE_REF,'contract':CONTRACT,'responseSlot':slot,
                'artifact':e['artifact'],'rawSha256':e['sha256'],
                'sourceDescriptionId':e['descriptionId'],'captureId':e['captureId'],
                'sourceRecordLocator':{'requestUrl':e['captureReceipt']['request']['url'],
                                       'jsonPointer':pointer},
                'captureStarted':e['captureReceipt']['started'],
                'captureEnded':e['captureReceipt']['ended']}

    concepts=[]
    for identifier in frozen['terms']:
        slot='term-'+identifier.split(':')[1]
        data=sources[slot]
        # Selection uses the manifest key; output values come only from the source body.
        concepts.append({'recordKey':slot,'kind':'concept','assertionOrigin':'source-provided',
                         'projectionRole':'approved-research-concept',
                         'sourceValues':capture.term_projection(data),
                         'lineage':lineage(slot,'')})

    parents=[];excluded=[]
    for assertion in frozen['parentAssertions']:
        slot=assertion['responseSlot'];pointer=assertion['acceptedRowPointers'][0]
        parent=sources[slot]['_embedded']['terms'][int(pointer.rsplit('/',1)[1])]
        child_slot='term-'+assertion['child'].split(':')[1]
        child=sources[child_slot]
        freeze.require(parent['obo_id']==assertion['parent'] and child['obo_id']==assertion['child'],
                       'Approved endpoint differs')
        parents.append({'recordKey':slot+pointer,'kind':'immediate-parent',
                        'assertionOrigin':'source-provided-OLS-parent-response',
                        'projectionRole':'approved-research-parent',
                        'child':{k:capture.field(child,k) for k in ('obo_id','iri','label')},
                        'parent':{k:capture.field(parent,k) for k in
                                  ('obo_id','iri','label','is_obsolete','ontology_name')},
                        'lineage':lineage(slot,pointer),'childLineage':lineage(child_slot,'')})
        # Inventory references only: do not promote excluded row content into records.
        for p in assertion['excludedRawRowPointers']:
            excluded.append({'disposition':'raw-provenance-only','lineage':lineage(slot,p)})
    freeze.require(len(concepts)==8 and len(parents)==5 and len(excluded)==6,'Unexpected output extent')
    return {'contract':CONTRACT,'freeze':FREEZE_REF,'sourceContext':frozen['sourceContext'],
            'projection':'mondo-ols-minimum-1','permissions':frozen['permissions'],
            'concepts':concepts,'parentAssertions':parents,'excludedRawRows':excluded,
            'inventory':{'concepts':'8','parentAssertions':'5','excludedRawRows':'6'},
            'interpretation':[
                'Source lexical values preserved; no normalization or biomedical equivalence resolution.',
                'Context annotations are attributed source text, not asserted mappings or additional entities.',
                'Parent assertions are OLS source-reported navigation, not inferred hierarchy closure.',
                'Excluded raw rows are provenance references, not accepted research assertions.',
                'Mondo-only M2.3 intermediate; full M2.1 and full-corpus M2.2 remain incomplete.',
                'Open Targets 26.06 remains blocked; no substitution.',
                'New OLS capture, not historical-response or full-release reproduction.',
                'Two uninstrumented preparatory lookups remain disclosed in the frozen manifest.',
                'No independent biomedical validation, normalization, alignment or RDF generation.']}


def verify(output=OUTPUT,artifacts=freeze.DEFAULT_ARTIFACTS,manifest=freeze.DEFAULT_MANIFEST):
    expected=freeze.serialize(extract(artifacts,manifest))
    actual=Path(output).read_bytes()
    freeze.require(actual==expected,'Extraction differs from verified source/contract')
    return {'status':'pass','sha256':capture.sha(actual),'bytes':len(actual),
            'concepts':8,'parentAssertions':5,'excludedRawRows':6}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation',choices=['build','verify'])
    parser.add_argument('--artifacts',type=Path,default=freeze.DEFAULT_ARTIFACTS)
    parser.add_argument('--manifest',type=Path,default=freeze.DEFAULT_MANIFEST)
    parser.add_argument('--output',type=Path,default=OUTPUT)
    args=parser.parse_args()
    if args.operation=='build':
        content=freeze.serialize(extract(args.artifacts,args.manifest))
        args.output.parent.mkdir(parents=True,exist_ok=True)
        with args.output.open('xb') as destination:destination.write(content)
    print(json.dumps(verify(args.output,args.artifacts,args.manifest),indent=2))
