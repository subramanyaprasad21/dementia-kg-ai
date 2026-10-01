import shutil
import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import development_corpus as c


class DevelopmentCorpus(unittest.TestCase):
    def test_release_replay_and_explicit_limits(self):
        manifest = c.verify()
        self.assertEqual(c.encode(manifest), (c.ROOT / c.MANIFEST).read_bytes())
        self.assertEqual((len(set(c.load().subjects())), len(c.load())), (191, 1112))
        self.assertFalse(manifest['fullCorpusComplete'])
        self.assertFalse(manifest['heldOut'])
        self.assertEqual(len(manifest['unresolved']), 4)

    def test_relocation_alteration_and_missing_graph_rejected(self):
        manifest = c.verify()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in list(manifest['files']) + [c.MANIFEST]:
                target = root / name
                target.parent.mkdir(parents=True, exist_ok=True)
                source = (c.ROOT / name) if name == c.MANIFEST else (c.SNAPSHOT / name)
                shutil.copyfile(source, target)
            self.assertEqual(c.verify(root), manifest)
            target = root / c.GRAPHS[-1]
            target.write_bytes(target.read_bytes() + b'\n')
            with self.assertRaisesRegex(ValueError, 'Historical release mismatch'):
                c.verify(root)
            target.unlink()
            with self.assertRaises(FileNotFoundError):
                c.verify(root)
