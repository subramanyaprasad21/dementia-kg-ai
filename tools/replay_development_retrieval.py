"""Exposed engineering controls, not benchmark questions or relevance labels."""
import argparse
import development_retrieval as r

OUTPUT = 'assessments/dementia-development-001.retrieval.json'
CASES = [
    dict(id='Q01-record-retrieval', text='PSEN1 evidence', anchors=['ENSG00000080815'], types=['EvidenceOccurrence']),
    dict(id='Q02-report-reference', text='shared study', anchors=['nct00594737'], types=['StudyRecord']),
    dict(id='Q03-original-mapping', text='original normalized mapping', anchors=['OMIM:172700'], types=['MappingRecord']),
    dict(id='Q04-persisted-selection-context', text='selection direct', anchors=[], types=['SelectionContext']),
    dict(id='Q05-ambiguous-original', text='source mapping', anchors=['OMIM:600274'], types=['MappingRecord']),
    dict(id='Q06-mechanism', text='mechanism', anchors=['CHEMBL4298021'], types=['MechanismRecord']),
    dict(id='Q07-indication', text='clinical indication', anchors=['CHEMBL3990042'], types=['ClinicalIndicationRecord']),
    dict(id='Q07-unavailable-population', text='population', anchors=['CHEMBL3990042'], types=['ClinicalIndicationRecord'], required=['hasPopulationScope']),
]


def build():
    graph = r.corpus.load()
    results = []
    for case in CASES:
        for mode in r.MODES:
            outcome = r.retrieve(graph, case['text'], case['anchors'], mode,
                                 record_types=[str(r.D[t]) for t in case['types']],
                                 required_predicates=[str(r.D[p]) for p in case.get('required', [])])
            results.append(dict(case=case['id'], mode=mode, status=outcome['status'], budget=outcome['budget'],
                                skippedForBudget=outcome['skippedForBudget'],
                                records=[dict(id=v['packet']['id'], sha256=v['packet']['sha256'], score=v['score'])
                                         for v in outcome['results']]))
    return dict(profile='m4-offline-engineering-controls-1',
                corpusManifestSha256=r.corpus.digest((r.corpus.ROOT/r.corpus.MANIFEST).read_bytes()),
                packetCount=len(r.packets(graph)), cases=CASES, results=results,
                fullQuestionAcceptance=False, heldOut=False,
                limitations=['Graph method requires explicit anchors or schema filters; no automatic entity grounding',
                             'Q04 returns only persisted contexts, not the source-side 0/1 and 3/10 computation',
                             'No independent relevance labels, biomedical correctness score or graph advantage',
                             'RDF-only population; external article inspections and aggregate projection excluded equally',
                             'TF-IDF lexical vectors are not learned semantic embeddings'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    data = r.corpus.encode(build())
    if args.write:
        with (r.corpus.ROOT/OUTPUT).open('xb') as stream:
            stream.write(data)
    else:
        print(data.decode(), end='')
