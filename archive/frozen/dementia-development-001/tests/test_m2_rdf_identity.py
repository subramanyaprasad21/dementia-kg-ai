import copy
import sys
import unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import m2_rdf_identity as identity


class IdentityExtension(unittest.TestCase):
    def setUp(self):
        self.description = identity.BASE + 'm2-source-description-1/' + '1' * 64
        self.inputs = dict(descriptionId=self.description, edition='2026-09-01', versionIri='urn:control:edition', loaded='source-time', updated='source-time', locator='term-control')
        self.registry = identity.Registry({self.description: self.inputs})
        self.payload = [dict(field='sourceAuthority', form='literal', value='EMBL-EBI-OLS', datatype=identity.core.XSD+'string', language=None)]

    def test_replay_and_payload_revision(self):
        a = self.registry.add('SourceSnapshot', self.inputs, self.payload)
        self.assertEqual(a, self.registry.add('SourceSnapshot', dict(reversed(list(self.inputs.items()))), self.payload))
        changed = copy.deepcopy(self.payload); changed[0]['value'] = 'changed control'
        self.assertNotEqual(a, self.registry.add('SourceSnapshot', self.inputs, changed))

    def test_invalid_origin_lineage_and_m1_reuse(self):
        for origin in ['audit-transcription', 'project-operation', 'referent']:
            with self.assertRaises(ValueError): self.registry.add('SourceSnapshot', self.inputs, self.payload, origin=origin)
        for key in self.inputs:
            bad = dict(self.inputs); bad.pop(key)
            with self.assertRaises(ValueError): self.registry.add('SourceSnapshot', bad, self.payload)
        bad = dict(self.inputs, edition='other')
        with self.assertRaises(ValueError): self.registry.add('SourceSnapshot', bad, self.payload)
        ref = dict(snapshotKey=identity.BASE+'SourceSnapshot/'+'2'*64, locator='x', role='reported-participant', authority='MONDO', identifier='MONDO:0004975', label='x')
        with self.assertRaisesRegex(ValueError, 'Unregistered snapshot'): self.registry.add('DiseaseConceptReference', ref, [])
        with self.assertRaises(ValueError): identity.identify(dict(profile='m1-id-1', kind='SourceSnapshot', origin='audit-transcription', inputs=self.inputs, contentRevision='0'*64))

    def test_collision_and_supplied_identity(self):
        iri = self.registry.add('SourceSnapshot', self.inputs, self.payload)
        with self.assertRaises(ValueError): self.registry.add('SourceSnapshot', self.inputs, self.payload, iri=iri+'x')
        changed = copy.deepcopy(self.payload); changed[0]['value'] = 'other'
        with patch.object(identity, 'identify', return_value=iri):
            with self.assertRaisesRegex(ValueError, 'collision'): self.registry.add('SourceSnapshot', self.inputs, changed)

    def test_unknown_terms_and_extra_keys(self):
        with self.assertRaises(ValueError): identity.receipt('NewClass', {}, [])
        with self.assertRaises(ValueError): identity.receipt('SourceSnapshot', dict(self.inputs, captureId='forbidden'), [])
        bad = copy.deepcopy(self.payload); bad[0]['field'] = 'sameAs'
        with self.assertRaises(ValueError): identity.receipt('SourceSnapshot', self.inputs, bad)
