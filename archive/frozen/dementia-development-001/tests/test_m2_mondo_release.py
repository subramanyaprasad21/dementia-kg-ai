import copy
import shutil
import socket
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
import m2_mondo_release as release
r=release.rdf


class MondoRelease(unittest.TestCase):
    def test_release_replay_and_relocation_offline(self):
        with patch.object(socket.socket,'connect',side_effect=AssertionError('Network forbidden')):
            self.assertEqual(release.verify()['triples'],317)
            with tempfile.TemporaryDirectory() as d:
                relocated=Path(d)/'capture';shutil.copytree(r.artifacts(),relocated)
                self.assertEqual(release.build(root=relocated),release.build())
                self.assertEqual(release.verify(root=relocated)['resources'],60)

    def test_missing_or_changed_external_artifact(self):
        with tempfile.TemporaryDirectory() as d:
            relocated=Path(d)/'capture';shutil.copytree(r.artifacts(),relocated)
            name=release.build()['externalArtifacts']['responses'][0]['artifact']
            path=relocated/name;raw=path.read_bytes();path.unlink()
            with self.assertRaises((ValueError,FileNotFoundError)):release.verify(root=relocated)
            path.write_bytes(raw+b' ')
            with self.assertRaises(ValueError):release.verify(root=relocated)

    def test_release_scope_and_graph_integrity_mutations(self):
        original=release.build()
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/'release.json'
            for mutation in [lambda x:x['inventory'].update(acceptedParents='6'),
                             lambda x:x['files'][0].update(sha256='0'*64),
                             lambda x:x['permissions'].update(identifier='CC0'),
                             lambda x:x.update(graphSha256='0'*64)]:
                changed=copy.deepcopy(original);mutation(changed)
                path.write_bytes(r.extract.freeze.serialize(changed))
                with self.assertRaises(ValueError):release.verify(path)
            path.write_bytes(b'{"profile":"a","profile":"b"}')
            with self.assertRaises(ValueError):release.verify(path)
