"""Offline integration controls; require the approved external capture directory."""
import copy
import json
import os
import shutil
import socket
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
import m2_mondo_freeze as f

MANIFEST_HASH = 'b7763d83f41e61c9d8bc617189dc04826609926f83e480289e33f4ac9cc8bb0a'

class Freeze(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.artifacts=Path(os.environ.get('MONDO_PILOT_ARTIFACTS',str(f.DEFAULT_ARTIFACTS)))
        if not cls.artifacts.is_dir():
            raise RuntimeError('Approved offline artifacts required; set MONDO_PILOT_ARTIFACTS. No automatic download/skip.')
        cls.original={p.name:f.capture.sha(p.read_bytes()) for p in cls.artifacts.iterdir() if p.is_file()}
        cls.raw=f.DEFAULT_MANIFEST.read_bytes();cls.manifest=json.loads(cls.raw)

    @classmethod
    def tearDownClass(cls):
        assert cls.original=={p.name:f.capture.sha(p.read_bytes()) for p in cls.artifacts.iterdir() if p.is_file()}

    def setUp(self):
        self.guard=patch.object(socket.socket,'connect',side_effect=AssertionError('Network forbidden'))
        self.guard.start();self.addCleanup(self.guard.stop)

    def mutated_manifest(self,mutation):
        with tempfile.TemporaryDirectory() as directory:
            obj=copy.deepcopy(self.manifest);mutation(obj)
            path=Path(directory)/'freeze.json';path.write_bytes(f.serialize(obj))
            with self.assertRaises(f.capture.Stop):f.verify(path,self.artifacts)

    def test_01_deterministic_manifest_and_offline_replay(self):
        self.assertEqual(f.capture.sha(self.raw),MANIFEST_HASH)
        self.assertEqual(f.serialize(f.build(self.artifacts)),self.raw)
        self.assertEqual(f.serialize(f.build(self.artifacts)),self.raw)
        self.assertEqual(f.verify(artifacts=self.artifacts)['status'],'pass')
        reordered=dict(reversed(list(self.manifest.items())))
        self.assertEqual(f.serialize(reordered),self.raw)

    def test_02_exact_independent_allowlists_and_rows(self):
        self.assertEqual(self.manifest['terms'],['MONDO:0004975','MONDO:0017276','MONDO:0008243',
            'MONDO:0010857','MONDO:0017160','MONDO:0007088','MONDO:0015140','MONDO:0100087'])
        pairs=[(a['child'],a['parent']) for a in self.manifest['parentAssertions']]
        self.assertEqual(pairs,[('MONDO:0010857','MONDO:0017160'),('MONDO:0017160','MONDO:0017276'),
            ('MONDO:0007088','MONDO:0015140'),('MONDO:0015140','MONDO:0100087'),('MONDO:0100087','MONDO:0004975')])
        entries={e['slot']:e for e in self.manifest['responses']}
        excluded=0
        for a in self.manifest['parentAssertions']:
            rows=json.loads((self.artifacts/entries[a['responseSlot']]['artifact']).read_bytes())['_embedded']['terms']
            self.assertEqual(len(a['acceptedRowPointers']),1)
            for pointer in a['acceptedRowPointers']:
                self.assertEqual(rows[int(pointer.rsplit('/',1)[1])]['obo_id'],a['parent'])
            for pointer in a['excludedRawRowPointers']:
                self.assertNotIn(rows[int(pointer.rsplit('/',1)[1])]['obo_id'],self.manifest['terms'])
                excluded+=1
        self.assertEqual(excluded,6)

    def test_03_digests_identity_linkage_and_time_separation(self):
        captures=set();descriptions=set();total=0
        for entry in self.manifest['responses']:
            body=(self.artifacts/entry['artifact']).read_bytes();total+=len(body)
            self.assertEqual(f.capture.sha(body),entry['sha256'])
            self.assertEqual(entry['sha256'],entry['captureReceipt']['rawSha256'])
            self.assertEqual(f.capture.identity(entry['captureReceipt']),entry['captureId'])
            self.assertEqual(f.capture.identity(entry['descriptionReceipt']),entry['descriptionId'])
            self.assertEqual(entry['captureReceipt']['sourceContext'],self.manifest['sourceContext'])
            self.assertNotEqual(entry['captureReceipt']['started'],self.manifest['sourceContext']['loaded'])
            captures.add(entry['captureId']);descriptions.add(entry['descriptionId'])
        self.assertEqual((len(captures),len(descriptions),total),(15,14,130541))

    def test_04_permissions_and_provenance_preserved(self):
        ledger=json.loads((self.artifacts/'ledger.json').read_bytes())
        self.assertEqual(self.manifest['permissions'],ledger['license'])
        self.assertEqual(self.manifest['permissions']['identifier'],'CC-BY-4.0')
        self.assertEqual(self.manifest['sourceContext']['edition'],'2026-09-01')
        self.assertEqual(self.manifest['sourceContext']['loaded'],'2026-09-24T00:09:08.017393439')
        self.assertTrue(any('Two uninstrumented' in x for x in self.manifest['limitations']))
        self.assertEqual(self.manifest['contracts']['projection'],'mondo-ols-minimum-1')

    def test_05_missing_raw_artifact_detected(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)/'copy';shutil.copytree(self.artifacts,root)
            (root/'02-term-0004975.json').unlink()
            with self.assertRaises(FileNotFoundError):f.verify(artifacts=root)

    def test_06_changed_raw_bytes_detected(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)/'copy';shutil.copytree(self.artifacts,root)
            path=root/'02-term-0004975.json';path.write_bytes(path.read_bytes()+b' ')
            with self.assertRaises(f.capture.Stop):f.verify(artifacts=root)

    def test_07_changed_ledger_not_rebaselined(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)/'copy';shutil.copytree(self.artifacts,root)
            path=root/'ledger.json';data=json.loads(path.read_bytes());data['license']['identifier']='CC0'
            path.write_text(json.dumps(data))
            with self.assertRaisesRegex(f.capture.Stop,'Pinned acquisition ledger'):f.build(root)

    def test_08_changed_manifest_identity_or_permissions_rejected(self):
        self.mutated_manifest(lambda x:x['responses'][0].update(captureId='urn:corrupted'))
        self.mutated_manifest(lambda x:x['responses'][0].update(descriptionId='urn:corrupted'))
        self.mutated_manifest(lambda x:x['permissions'].update(identifier='CC0'))

    def test_09_scope_and_row_reclassification_rejected(self):
        self.mutated_manifest(lambda x:x['terms'].append('MONDO:9999999'))
        self.mutated_manifest(lambda x:x['parentAssertions'][0].update(parent='MONDO:0004975'))
        self.mutated_manifest(lambda x:x['parentAssertions'][0].update(excludedRawRowPointers=[]))

    def test_10_relocation_preserves_manifest(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)/'relocated';shutil.copytree(self.artifacts,root)
            self.assertEqual(f.serialize(f.build(root)),self.raw)
            self.assertEqual(f.verify(artifacts=root)['manifestSha256'],MANIFEST_HASH)

    def test_11_noncanonical_manifest_and_duplicate_keys_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'manifest.json'
            for raw in [json.dumps(self.manifest,indent=2).encode(),b'{"a":"b","a":"c"}\n']:
                path.write_bytes(raw)
                with self.assertRaises(ValueError):f.verify(path,self.artifacts)

    def test_12_cli_refuses_to_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'manifest.json';path.write_bytes(self.raw)
            result=subprocess.run([sys.executable,str(f.ROOT/'tools/m2_mondo_freeze.py'),'build',
                '--artifacts',str(self.artifacts),'--manifest',str(path)],capture_output=True)
            self.assertNotEqual(result.returncode,0)
            self.assertIn(b'FileExistsError',result.stderr)
            self.assertEqual(path.read_bytes(),self.raw)

if __name__=='__main__':unittest.main()
