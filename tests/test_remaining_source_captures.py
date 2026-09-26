import sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
import verify_remaining_sources as v

class RemainingCaptures(unittest.TestCase):
 def test_primary_replay_rights_and_exact_scope(self):
  result=v.inspect();self.assertEqual(result['requests'],11);self.assertEqual(result['bytes'],801988)
  self.assertEqual(len(result['publicationLocators']),15);self.assertEqual(len(result['articles']),4)
  self.assertEqual(v.source.serialize(result),(v.source.ROOT/'assessments/primary-evidence-001.inspection.json').read_bytes())
 def test_altered_primary_body_fails(self):
  with tempfile.TemporaryDirectory() as temp:
   root=Path(temp)
   for file in v.primary.ROOT.iterdir():
    if file.is_file():(root/file.name).symlink_to(file)
   file=root/'PMC7852392.article.xml';file.unlink();file.write_text('<changed/>')
   with self.assertRaisesRegex(ValueError,'Changed captured'):v.inspect(root)
 def test_association_scalar_replay_and_missing_column(self):
  result=v.association.recover_projection();row=v.source.untyped(result['sourceValues'])
  self.assertEqual(row['targetId'],'ENSG00000186868');self.assertEqual(row['evidenceCount'],5056)
  self.assertEqual(v.source.serialize(result),(v.source.ROOT/'extractions/ot2606-association-001.partial.json').read_bytes())
  with tempfile.TemporaryDirectory() as temp:
   root=Path(temp)
   for file in v.association.ROOT.iterdir():
    if file.is_file():(root/file.name).symlink_to(file)
   column=root/'10.0.4.values';self.assertTrue(column.exists());column.unlink()
   with self.assertRaises(FileNotFoundError):v.association.recover_projection(root)
