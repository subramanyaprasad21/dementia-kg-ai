"""M3 descriptive statistics over asserted RDF; no inference or biological ranking."""
import argparse
from collections import Counter, deque
from rdflib import URIRef
from rdflib.namespace import RDF
import development_corpus as corpus
from m2_mondo_rdf import DKG as D, PROV

OUTPUT = 'assessments/dementia-development-001.characterisation.json'
SEMANTIC = {D[p] for p in ('hasTarget', 'hasDrug', 'hasDiseaseReference',
    'mappingInput', 'reportedDestination', 'mappingContext', 'childReference',
    'parentReference', 'citesPublication', 'reportedEvidence',
    'inSelectionContext', 'selectedOccurrence', 'refersToStudy')}
SOURCE_TYPES = ('EvidenceOccurrence', 'MappingRecord', 'HierarchyStep',
                'MechanismRecord', 'ClinicalIndicationRecord', 'StudyRecord')


def components(nodes, edges):
    adjacency = {n: set() for n in nodes}
    for a, b in edges:
        if a in adjacency and b in adjacency:
            adjacency[a].add(b)
            adjacency[b].add(a)
    unseen = set(nodes)
    sizes = []
    while unseen:
        queue = [min(unseen, key=str)]
        found = set(queue)
        while queue:
            for neighbour in adjacency[queue.pop()] - found:
                found.add(neighbour)
                queue.append(neighbour)
        unseen -= found
        sizes.append(len(found))
    return sorted(sizes, reverse=True)


def distances(graph, start, predicates, max_hops=4):
    result = {start: 0}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if result[node] >= max_hops:
            continue
        for predicate, target in graph.predicate_objects(node):
            if predicate in predicates and isinstance(target, URIRef) and target not in result:
                result[target] = result[node] + 1
                queue.append(target)
    return result


def analyse(graph):
    nodes = set(graph.subjects())
    types = Counter(str(t) for _, t in graph.subject_objects(RDF.type))
    all_edges = {(s, o) for s, p, o in graph if p != RDF.type and o in nodes}
    semantic_edges = {(s, o) for s, p, o in graph if p in SEMANTIC and o in nodes}
    semantic_nodes = {n for edge in semantic_edges for n in edge}
    coverage = {}
    for name in SOURCE_TYPES:
        owners = set(graph.subjects(RDF.type, D[name]))
        qualified = {s for s in owners if list(graph.objects(s, D.sourceLocator)) and
                     any(list(graph.objects(snapshot, PROV.wasDerivedFrom)) and
                         list(graph.objects(snapshot, D.snapshotVersion))
                         for snapshot in graph.objects(s, D.inSnapshot))}
        coverage[name] = dict(records=len(owners), withLocatorVersionAndDerivation=len(qualified),
                              missing=sorted(map(str, owners - qualified)))
    evidence = set(graph.subjects(RDF.type, D.EvidenceOccurrence))
    publications = set(graph.subjects(RDF.type, D.Publication))
    paths = Counter()
    for start in evidence:
        for target, length in distances(graph, start, SEMANTIC).items():
            if target in publications:
                paths[str(length)] += 1
    return dict(
        triples=len(graph), subjectResources=len(nodes), types=dict(sorted(types.items())),
        predicateCounts=dict(sorted(Counter(str(p) for _, p, _ in graph).items())),
        resourceConnectivity=dict(edges=len(all_edges), componentSizes=components(nodes, all_edges),
                                  definition='Undirected URI edges between subjects; excludes rdf:type; includes provenance'),
        semanticProjection=dict(nodes=len(semantic_nodes), edges=len(semantic_edges),
                                componentSizes=components(semantic_nodes, semantic_edges),
                                excludedIsolates=len(nodes-semantic_nodes),
                                predicates=sorted(map(str, SEMANTIC)),
                                definition='Explicit selected record-participant links; active endpoints only, not biological interactions'),
        evidenceSourceCounts=dict(sorted(Counter(str(v) for s in evidence for v in graph.objects(s, D.evidenceSourceType)).items())),
        snapshotAuthorityCounts=dict(sorted(Counter(str(v) for s in graph.subjects(RDF.type, D.SourceSnapshot)
                                                    for v in graph.objects(s, D.sourceAuthority)).items())),
        sourceRecordProvenance=coverage,
        evidencePublicationPaths=dict(maxHops=4, directed=True, shortestPathCountsByLength=dict(sorted(paths.items())),
                                      interpretation='Record reachability only; source dependence and biological support are not inferred'))


def build():
    manifest = corpus.verify()
    return dict(profile='m3-qualified-development-1', corpusManifestSha256=corpus.digest((corpus.ROOT/corpus.MANIFEST).read_bytes()),
                assertedGraphSha256=manifest['graphSha256'], statistics=analyse(corpus.graph()),
                limitations=['Purposively selected finite development corpus, not disease-wide coverage',
                             'Source descriptions, captures and referents are different resources',
                             'No centrality-based biomedical importance, causal paths or graph advantage demonstrated',
                             'No cross-source identifier equality or additional hierarchy inferred'])


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--write', action='store_true')
    args = p.parse_args()
    data = corpus.encode(build())
    if args.write:
        with (corpus.ROOT/OUTPUT).open('xb') as stream:
            stream.write(data)
    else:
        print(data.decode(), end='')
