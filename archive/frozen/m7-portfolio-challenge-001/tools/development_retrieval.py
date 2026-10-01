"""Offline lexical-vector, asserted-graph and hybrid retrieval. No answer synthesis."""
import argparse
from collections import Counter, deque
import math
import re
from rdflib import Graph, Literal, URIRef
from rdflib.namespace import RDF, OWL
import development_corpus as corpus
from m2_mondo_rdf import DKG as D, PROV

ROOT_TYPES = {D[n] for n in ('EvidenceOccurrence', 'MappingRecord', 'HierarchyStep',
    'MechanismRecord', 'ClinicalIndicationRecord', 'StudyRecord', 'DiseaseTargetAssociation',
    'SelectionContext', 'SelectionMembership', 'DerivedStatement', 'MissingnessRecord')}
ANCHOR_FIELDS = {D[n] for n in ('externalIdentifier', 'sourceRecordIdentifier', 'sourceLabel')}
MODES = ('vector', 'graph', 'hybrid')


def tokens(text):
    # Search index only: never changes source identifiers or RDF identity.
    return re.findall(r'\w+(?:[:-]\w+)*', text.lower())


def packets(graph):
    """Lossless statements in a bounded outward two-hop record neighbourhood.

    Raw provenance JSON literals are not promoted into retrieval facts. Their
    locators remain. No incoming join, ID merge or inferred assertion is added.
    """
    roots = sorted({s for t in ROOT_TYPES for s in graph.subjects(RDF.type, t)}, key=str)
    result = []
    for root in roots:
        seen = {root: 0}
        queue = deque([root])
        facts = set()
        while queue:
            subject = queue.popleft()
            for p, o in graph.predicate_objects(subject):
                if p == D.sourceText and (subject, RDF.type, PROV.Entity) in graph:
                    continue
                facts.add((subject, p, o))
                if p != RDF.type and isinstance(o, URIRef) and (o, None, None) in graph:
                    if seen[subject] < 2 and o not in seen:
                        seen[o] = seen[subject] + 1
                        queue.append(o)
        triples = sorted(f'{s.n3()} {p.n3()} {o.n3()} .' for s, p, o in facts)
        text = '\n'.join(triples)
        result.append(dict(id=str(root), types=sorted(str(t) for t in graph.objects(root, RDF.type)),
                           text=text, sha256=corpus.digest(text.encode()),
                           limitation='Asserted record neighbourhood only; retrieval is not claim verification.'))
    return result


def vector_scores(documents, query):
    """Smoothed IDF, log term frequency, L2 cosine; no neural embeddings."""
    counts = [Counter(tokens(d['text'])) for d in documents]
    frequencies = Counter(term for c in counts for term in c)
    idf = {t: math.log((1+len(documents))/(1+n))+1 for t, n in frequencies.items()}
    def vector(count):
        values = {t: (1+math.log(n))*idf[t] for t, n in count.items() if t in idf}
        norm = math.sqrt(sum(v*v for v in values.values()))
        return {t: v/norm for t, v in values.items()} if norm else {}
    q = vector(Counter(tokens(query)))
    return {d['id']: sum(value*q.get(t, 0) for t, value in vector(c).items())
            for d, c in zip(documents, counts)}


def graph_score(document, anchors):
    """All exact supplied anchors must occur in the asserted neighbourhood.

    The anchors are owner/developer supplied query inputs, not inferred disease
    equivalences. Each matched resource remains separate.
    """
    if not anchors:
        return 0.0, []
    g = Graph().parse(data=document['text'], format='nt')
    root = URIRef(document['id'])
    paths = {root: []}
    queue = deque([root])
    while queue:
        subject = queue.popleft()
        for p, o in sorted(g.predicate_objects(subject), key=lambda pair: tuple(map(str, pair))):
            if p != RDF.type and isinstance(o, URIRef) and o not in paths and len(paths[subject]) < 2:
                paths[o] = paths[subject] + [[str(subject), str(p), str(o)]]
                queue.append(o)
    matches = []
    for anchor in anchors:
        found = []
        for subject in paths:
            if str(subject) == anchor:
                found.append(dict(anchor=anchor, resource=str(subject), path=paths[subject], field=None))
            for p, o in g.predicate_objects(subject):
                if p in ANCHOR_FIELDS and isinstance(o, Literal) and str(o) == anchor:
                    found.append(dict(anchor=anchor, resource=str(subject), path=paths[subject], field=str(p)))
        if not found:
            return 0.0, []
        matches.append(min(found, key=lambda v: (len(v['path']), v['resource'], v['field'] or '')))
    return sum(1/(1+len(v['path'])) for v in matches), matches


def retrieve(graph, text, anchors=(), mode='hybrid', k=5, max_bytes=65536,
             record_types=(), required_predicates=(), allowed_roots=None):
    if mode not in MODES or not isinstance(k, int) or isinstance(k, bool) or not 1 <= k <= 100:
        raise ValueError('Invalid retrieval mode or record budget')
    if not isinstance(max_bytes, int) or isinstance(max_bytes, bool) or not 1 <= max_bytes <= 1048576:
        raise ValueError('Invalid byte budget')
    schema = Graph().parse(corpus.ROOT/'ontology/dementiagraph-v.ttl', format='turtle')
    declared_properties = set(schema.subjects(RDF.type, OWL.ObjectProperty)) | set(schema.subjects(RDF.type, OWL.DatatypeProperty))
    if not set(map(URIRef, record_types)) <= ROOT_TYPES or not set(map(URIRef, required_predicates)) <= declared_properties:
        raise ValueError('Undeclared or inapplicable schema filter')
    documents = packets(graph)
    if allowed_roots is not None:
        if not allowed_roots or len(set(allowed_roots)) != len(allowed_roots) or not set(allowed_roots) <= {d['id'] for d in documents}:
            raise ValueError('Invalid explicit query root scope')
    # Schema filters apply equally to every comparator.
    candidates = [d for d in documents if
                  (allowed_roots is None or d['id'] in allowed_roots) and
                  (not record_types or set(d['types']) & set(record_types)) and
                  all((URIRef(d['id']), URIRef(p), None) in graph for p in required_predicates)]
    query = ' '.join([text, *anchors])
    vectors = vector_scores(documents, query)
    graphs = {d['id']: graph_score(d, anchors) for d in candidates}
    if not anchors and (record_types or required_predicates or allowed_roots):
        # Explicit type/predicate query, not interpretation of free text.
        graphs = {d['id']: (1.0, []) for d in candidates}
    def ranked(scores):
        return sorted((i for i in scores if scores[i] > 0), key=lambda i: (-scores[i], i))
    vr = ranked({d['id']: vectors[d['id']] for d in candidates})
    gr = ranked({i: value[0] for i, value in graphs.items()})
    if mode == 'vector':
        scores = {i: vectors[i] for i in vr}
    elif mode == 'graph':
        scores = {i: graphs[i][0] for i in gr}
    else:
        scores = Counter()
        for ranking in (vr, gr):
            for rank, ident in enumerate(ranking, 1):
                scores[ident] += 1/(60+rank)
    by_id = {d['id']: d for d in candidates}
    selected, skipped, size = [], [], 0
    for ident in ranked(scores):
        if len(selected) >= k:
            break
        document = by_id[ident]
        cost = len(corpus.encode(document))
        if size+cost > max_bytes:
            skipped.append(ident)
            continue
        selected.append(dict(score=scores[ident], packet=document, anchorPaths=graphs[ident][1]))
        size += cost
    result = dict(mode=mode, query=dict(text=text, anchors=list(anchors)),
                recordTypes=list(record_types), requiredPredicates=list(required_predicates),
                corpusPacketCount=len(documents), eligiblePackets=len(candidates),
                budget=dict(records=k, packetBytes=max_bytes, usedPacketBytes=size),
                results=selected, skippedForBudget=skipped,
                status='RETRIEVED-NOT-ADJUDICATED' if selected else 'NO-RETRIEVABLE-SUPPORT',
                scope='RDF assertions only; no source-intermediate aggregate, local Q04 computation or article-inspection oracle',
                limitation='No results means retrieval insufficiency, never biological negation; scores are not confidence.')
    if allowed_roots is not None:
        result['allowedRoots'] = list(allowed_roots)
        result['limitation'] += ' Explicit question-scoped RDF records only; source-intermediate query counts, article inspections and unacquired primary records are not supplied.'
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('text')
    parser.add_argument('--anchor', action='append', default=[])
    parser.add_argument('--mode', choices=MODES, default='hybrid')
    parser.add_argument('--type', action='append', default=[], help='Approved local class name')
    parser.add_argument('--require', action='append', default=[], help='Approved local property on root')
    parser.add_argument('--k', type=int, default=5)
    parser.add_argument('--max-bytes', type=int, default=65536)
    args = parser.parse_args()
    result = retrieve(corpus.load(), args.text, args.anchor, args.mode, args.k, args.max_bytes,
                      [str(D[t]) for t in args.type], [str(D[p]) for p in args.require])
    print(corpus.encode(result).decode(), end='')
