import copy
import sys
import tempfile
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'tools'))
import ot2606_source as source
import ot2606_release as release

class EvidenceRelease(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.result=release.verify()
    def test_exact_bounded_release_inventory_and_originals(self):
        self.assertEqual(self.result['ot']['resources'],92);self.assertEqual(self.result['ot']['triples'],581)
        self.assertEqual(self.result['combined']['resources'],152);self.assertEqual(self.result['combined']['triples'],898)
        self.assertEqual(self.result['combined']['findings'],{'Warning':2});self.assertFalse(self.result['combined']['rawSHACLConforms'])
        self.assertEqual(self.result['combined']['unexpectedSubstantiveAssertions'],0)
        self.assertEqual(self.result['availability'],{'VERIFIED':9,'PARTIALLY VERIFIED':26,'UNAVAILABLE':21})
        self.assertEqual(source.serialize(self.result),release.MANIFEST.read_bytes())
    def test_changed_manifest_rejected(self):
        with tempfile.TemporaryDirectory() as t:
            p=Path(t)/'release.json';bad=copy.deepcopy(self.result);bad['combined']['rawSHACLConforms']=True;p.write_bytes(source.serialize(bad))
            with self.assertRaisesRegex(ValueError,'Release manifest'):release.verify(p)
