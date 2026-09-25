"""M2.5 bounded reference checks; no alignment dataset or production resolver."""
import copy
import json
import os
import socket
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import m2_mondo_extract as extract

ROOT = Path(__file__).resolve().parents[1]
DECISION = ROOT / 'assessments/mondo-pilot-001.normalization.json'
EXTRACTION_SHA = '43d7537f1f8e14340160d9581e8891db7f2dbe60a903c3910648295aae091882'
DECISION_SHA = '0df85aa9649a0318015732c8fa5bcecb4fd549dc0a67f6c76a8ee795992bafa7'
PAIRS = [('MONDO:0010857', 'MONDO:0017160'),
         ('MONDO:0017160', 'MONDO:0017276'),
         ('MONDO:0007088', 'MONDO:0015140'),
         ('MONDO:0015140', 'MONDO:0100087'),
         ('MONDO:0100087', 'MONDO:0004975')]


class UnresolvedReference(ValueError):
    pass


def require(condition, reason):
    if not condition:
        raise UnresolvedReference(reason)


def text(fields, key):
    value = fields[key]
    require(value['state'] == 'present' and value['value']['type'] == 'string',
            'endpoint must be a present source string')
    return value['value']['value']


def endpoint(reference, concepts):
    """Exact source ID AND IRI; labels and xrefs never provide fallback candidates."""
    identifier, iri = text(reference, 'obo_id'), text(reference, 'iri')
    candidates = [c for c in concepts
                  if text(c['sourceValues'], 'obo_id') == identifier
                  or text(c['sourceValues'], 'iri') == iri]
    require(len(candidates) == 1, 'missing or ambiguous endpoint')
    concept = candidates[0]
    values = concept['sourceValues']
    require((text(values, 'obo_id'), text(values, 'iri')) == (identifier, iri),
            'conflicting identifier/IRI')
    require(text(values, 'ontology_name') == 'mondo', 'incompatible authority')
    return concept


def resolve(candidate, trusted, manifest):
    """Read-only assessment against verified source context, not an identity merge.

    Input-byte verification is performed by the caller, separately. Mutations reach
    this function directly, exercising lookup, ambiguity, scope and lineage checks.
    The returned references are original objects; no dataset or identity is minted.
    """
    require(candidate['sourceContext'] == manifest['sourceContext'], 'incompatible edition/context')
    resolved = []
    for assertion in candidate['parentAssertions']:
        child = endpoint(assertion['child'], candidate['concepts'])
        parent = endpoint(assertion['parent'], candidate['concepts'])
        resolved.append((assertion, child, parent))
    actual = [(text(a['child'], 'obo_id'), text(a['parent'], 'obo_id')) for a, _, _ in resolved]
    require(actual == PAIRS, 'direction or accepted projection')
    require(actual == [(a['child'], a['parent']) for a in manifest['parentAssertions']],
            'frozen parent allowlist')
    # Frozen source record and row provenance qualify reference matching. Comparing
    # complete lineage preserves locators, contexts, digests and both identity levels.
    baseline = {c['recordKey']: c for c in trusted['concepts']}
    require(len(candidate['concepts']) == 8, 'concept scope')
    require(len({c['recordKey'] for c in candidate['concepts']}) == 8, 'duplicate record key')
    for concept in candidate['concepts']:
        require(concept['recordKey'] in baseline, 'unexpected concept')
        original = baseline[concept['recordKey']]
        require(concept['lineage'] == original['lineage'], 'concept lineage')
        require(concept == original, 'source values or unsupported correspondence')
    for (assertion, child, parent), original in zip(resolved, trusted['parentAssertions']):
        require(assertion['lineage'] == original['lineage'] and
                assertion['childLineage'] == original['childLineage'], 'assertion lineage')
        require(assertion['childLineage'] == child['lineage'], 'child lineage resolution')
        require(assertion == original, 'source assertion changed')
        for key in ('sourceDescriptionId', 'captureId'):
            require(assertion['lineage'][key] != parent['lineage'][key],
                    'parent response and term identities collapsed')
    require(candidate['excludedRawRows'] == trusted['excludedRawRows'], 'excluded provenance')
    for key in set(candidate) | set(trusted):
        if key not in {'concepts', 'parentAssertions', 'excludedRawRows'}:
            require(key in candidate and key in trusted and candidate[key] == trusted[key],
                    'context or unsupported correspondence')
    return resolved


class ReferenceConsistency(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.artifacts = Path(os.environ.get('MONDO_PILOT_ARTIFACTS', str(extract.freeze.DEFAULT_ARTIFACTS)))
        cls.paths = [extract.OUTPUT, DECISION, extract.freeze.DEFAULT_MANIFEST]
        cls.paths += list(cls.artifacts.iterdir())
        cls.before = {p: extract.capture.sha(p.read_bytes()) for p in cls.paths}
        require(cls.before[extract.OUTPUT] == EXTRACTION_SHA, 'extraction digest')
        require(cls.before[DECISION] == DECISION_SHA, 'decision digest')
        require(cls.before[extract.freeze.DEFAULT_MANIFEST] == extract.MANIFEST_HASH, 'freeze digest')
        with patch.object(socket.socket, 'connect', side_effect=AssertionError('Network forbidden')):
            extract.verify(artifacts=cls.artifacts)
        cls.original = json.loads(extract.OUTPUT.read_bytes())
        cls.manifest = json.loads(extract.freeze.DEFAULT_MANIFEST.read_bytes())

    @classmethod
    def tearDownClass(cls):
        assert cls.before == {p: extract.capture.sha(p.read_bytes()) for p in cls.paths}

    def check(self, candidate):
        with patch.object(socket.socket, 'connect', side_effect=AssertionError('Network forbidden')):
            return resolve(candidate, self.original, self.manifest)

    def reject(self, mutation, reason):
        candidate = copy.deepcopy(self.original)
        mutation(candidate)
        with self.assertRaisesRegex(UnresolvedReference, reason):
            self.check(candidate)

    def test_01_pinned_inputs_and_no_transformation_decision(self):
        decision = json.loads(DECISION.read_bytes())
        self.assertEqual(decision['input']['sha256'], EXTRACTION_SHA)
        self.assertEqual(decision['transformations'], [])
        self.assertEqual(self.original['freeze']['sha256'], extract.MANIFEST_HASH)

    def test_02_all_endpoints_positive_and_identity_preservation(self):
        candidate = copy.deepcopy(self.original)
        candidate['concepts'].reverse()  # Lookup must not rely on array position.
        before = copy.deepcopy(candidate)
        result = self.check(candidate)
        self.assertEqual(len(result), 5)
        self.assertEqual([(text(c['sourceValues'], 'obo_id'), text(p['sourceValues'], 'obo_id'))
                          for _, c, p in result], PAIRS)
        for assertion, child, parent in result:
            self.assertIs(assertion, candidate['parentAssertions'][result.index((assertion, child, parent))])
            self.assertTrue(any(parent is c for c in candidate['concepts']))
            self.assertEqual(assertion['childLineage'], child['lineage'])
            for key in ('captureId', 'sourceDescriptionId', 'sourceRecordLocator'):
                self.assertNotEqual(assertion['lineage'][key], parent['lineage'][key])
        self.assertEqual(candidate, before)

    def test_03_missing_child_or_parent_candidate(self):
        for identifier in PAIRS[0]:
            self.reject(lambda d: d['concepts'].__setitem__(slice(None),
                        [c for c in d['concepts'] if text(c['sourceValues'], 'obo_id') != identifier]),
                        'missing or ambiguous endpoint')

    def test_04_conflicting_identifier_iri_and_authority(self):
        for side in ('child', 'parent'):
            self.reject(lambda d: d['parentAssertions'][0][side]['iri']['value'].update(value='urn:conflict'),
                        'conflicting identifier/IRI')
        self.reject(lambda d: d['concepts'][3]['sourceValues']['ontology_name']['value'].update(value='other'),
                    'incompatible authority')

    def test_05_duplicate_and_ambiguous_candidates(self):
        self.reject(lambda d: d['concepts'].append(copy.deepcopy(d['concepts'][3])),
                    'missing or ambiguous endpoint')
        def ambiguous(d):
            extra = copy.deepcopy(d['concepts'][3])
            extra['sourceValues']['iri']['value']['value'] = 'urn:different'
            d['concepts'].append(extra)
        self.reject(ambiguous, 'missing or ambiguous endpoint')

    def test_06_incompatible_source_edition(self):
        self.reject(lambda d: d['sourceContext'].update(edition='2026-09-02'), 'incompatible edition/context')
        self.reject(lambda d: d['sourceContext'].update(versionIri='urn:other-release'), 'incompatible edition/context')

    def test_07_reversed_direction_and_excluded_row_promotion(self):
        def reverse(d):
            a = d['parentAssertions'][0]
            a['child'], a['parent'] = a['parent'], a['child']
        self.reject(reverse, 'direction or accepted projection')
        def promote(d):
            d['parentAssertions'][0]['lineage'] = copy.deepcopy(d['excludedRawRows'][0]['lineage'])
        self.reject(promote, 'assertion lineage')
        self.reject(lambda d: d['parentAssertions'].append(copy.deepcopy(d['parentAssertions'][0])),
                    'direction or accepted projection')

    def test_08_altered_or_collapsed_lineage(self):
        for key in ('sourceDescriptionId', 'captureId', 'sourceRecordLocator', 'freeze'):
            for role in ('lineage', 'childLineage'):
                self.reject(lambda d: d['parentAssertions'][0][role].update({key: 'altered'}), 'assertion lineage')
            self.reject(lambda d: d['concepts'][4]['lineage'].update({key: 'altered'}), 'concept lineage')
        def collapse(d):
            a = d['parentAssertions'][0]
            parent = endpoint(a['parent'], d['concepts'])
            a['lineage'] = copy.deepcopy(parent['lineage'])
        self.reject(collapse, 'assertion lineage')

    def test_09_xrefs_and_labels_cannot_supply_correspondence(self):
        # Source xrefs (including equivalence-like text) survive as annotations only.
        self.assertEqual(len(self.check(copy.deepcopy(self.original))), 5)
        def label_and_xref_only(d):
            values = d['concepts'][3]['sourceValues']
            values['obo_id']['value']['value'] = 'MONDO:9999999'
            values['iri']['value']['value'] = 'http://purl.obolibrary.org/obo/MONDO_9999999'
            # Original label and all xrefs remain; neither rescues the absent ID/IRI.
        self.reject(label_and_xref_only, 'missing or ambiguous endpoint')
        self.reject(lambda d: d.update(equivalences=[{'predicate': 'owl:sameAs', 'basis': 'source xref'}]),
                    'unsupported correspondence')
        self.reject(lambda d: d['concepts'][0].update(sameAs='xref-derived'), 'unsupported correspondence')


if __name__ == '__main__':
    unittest.main()
