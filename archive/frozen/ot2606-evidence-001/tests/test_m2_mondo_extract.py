"""Bounded extraction and mutation checks over the approved external source slice."""
import copy
import json
import os
import shutil
import socket
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
import m2_mondo_extract as x

EXPECTED = [
 ('MONDO:0004975','Alzheimer disease'),('MONDO:0017276','frontotemporal dementia'),
 ('MONDO:0008243','Pick disease'),('MONDO:0010857','semantic dementia'),
 ('MONDO:0017160','behavioral variant of frontotemporal dementia'),
 ('MONDO:0007088','Alzheimer disease type 1'),
 ('MONDO:0015140','early-onset autosomal dominant Alzheimer disease'),
 ('MONDO:0100087','familial Alzheimer disease')]
PAIRS=[('MONDO:0010857','MONDO:0017160'),('MONDO:0017160','MONDO:0017276'),
       ('MONDO:0007088','MONDO:0015140'),('MONDO:0015140','MONDO:0100087'),
       ('MONDO:0100087','MONDO:0004975')]
DIGEST='43d7537f1f8e14340160d9581e8891db7f2dbe60a903c3910648295aae091882'

def lexical(field):return field['value']['value']

class Extraction(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root=Path(os.environ.get('MONDO_PILOT_ARTIFACTS',str(x.freeze.DEFAULT_ARTIFACTS)))
        cls.before={p.name:x.capture.sha(p.read_bytes()) for p in cls.root.iterdir()}
        cls.raw=x.OUTPUT.read_bytes();cls.data=json.loads(cls.raw)
        cls.manifest=json.loads(x.freeze.DEFAULT_MANIFEST.read_bytes())

    @classmethod
    def tearDownClass(cls):
        assert cls.before=={p.name:x.capture.sha(p.read_bytes()) for p in cls.root.iterdir()}

    def setUp(self):
        self.guard=patch.object(socket.socket,'connect',side_effect=AssertionError('Network forbidden'))
        self.guard.start();self.addCleanup(self.guard.stop)

    def mutate_output(self,mutation):
        with tempfile.TemporaryDirectory() as tmp:
            value=copy.deepcopy(self.data);mutation(value)
            path=Path(tmp)/'output.json';path.write_bytes(x.freeze.serialize(value))
            with self.assertRaises(x.capture.Stop):x.verify(path,self.root)

    def test_01_exact_terms_and_source_labels(self):
        self.assertEqual([(lexical(r['sourceValues']['obo_id']),lexical(r['sourceValues']['label']))
                          for r in self.data['concepts']],EXPECTED)
        self.assertEqual(len(self.data['concepts']),8)

    def test_02_exact_parents_and_excluded_rows(self):
        self.assertEqual([(lexical(r['child']['obo_id']),lexical(r['parent']['obo_id']))
                          for r in self.data['parentAssertions']],PAIRS)
        self.assertEqual(len(self.data['excludedRawRows']),6)
        accepted={(r['lineage']['responseSlot'],r['lineage']['sourceRecordLocator']['jsonPointer'])
                  for r in self.data['parentAssertions']}
        excluded={(r['lineage']['responseSlot'],r['lineage']['sourceRecordLocator']['jsonPointer'])
                  for r in self.data['excludedRawRows']}
        self.assertFalse(accepted & excluded)
        self.assertEqual(len(excluded),6)
        self.assertTrue(all(set(r)=={'disposition','lineage'} for r in self.data['excludedRawRows']))

    def test_03_deterministic_offline_replay(self):
        self.assertEqual(x.capture.sha(self.raw),DIGEST)
        self.assertEqual(x.freeze.serialize(x.extract(self.root)),self.raw)
        self.assertEqual(x.freeze.serialize(x.extract(self.root)),self.raw)
        self.assertEqual(x.verify(artifacts=self.root)['status'],'pass')

    def test_04_lineage_and_all_original_context_fields(self):
        entries={e['slot']:e for e in self.manifest['responses']}
        for record in self.data['concepts']+self.data['parentAssertions']+self.data['excludedRawRows']:
            link=record['lineage'];entry=entries[link['responseSlot']]
            self.assertEqual(link['sourceDescriptionId'],entry['descriptionId'])
            self.assertEqual(link['captureId'],entry['captureId'])
            self.assertEqual(link['freeze']['sha256'],x.MANIFEST_HASH)
            self.assertEqual(link['contract'],'mondo-extraction-1')
            self.assertEqual(link['rawSha256'],x.capture.sha((self.root/entry['artifact']).read_bytes()))
        for record in self.data['concepts']:
            source=x.capture.parse((self.root/record['lineage']['artifact']).read_bytes())
            self.assertEqual(set(record['sourceValues']),set(x.capture.FIELDS))
            for key in x.capture.FIELDS:
                self.assertEqual(record['sourceValues'][key],x.capture.field(source,key))
            # Independent raw spelling check, not derived from manifest values.
            ordinary=json.loads((self.root/record['lineage']['artifact']).read_bytes())
            self.assertEqual(lexical(record['sourceValues']['obo_id']),ordinary['obo_id'])
            self.assertEqual(lexical(record['sourceValues']['iri']),ordinary['iri'])
            self.assertEqual(lexical(record['sourceValues']['label']),ordinary['label'])

    def test_05_mapping_annotations_remain_attributed_values(self):
        records={lexical(r['sourceValues']['obo_id']):r for r in self.data['concepts']}
        for identifier,omim,description in [('MONDO:0008243','172700','MONDO:equivalentTo'),
                                          ('MONDO:0010857','600274','Orphanet:100069')]:
            xrefs=records[identifier]['sourceValues']['obo_xref']['value']['value']
            matching=[v['value'] for v in xrefs if v['value'].get('id',{}).get('value')==omim]
            self.assertEqual(len(matching),1);self.assertEqual(matching[0]['description']['value'],description)
        self.assertEqual(set(self.data['concepts'][0]),{'recordKey','kind','assertionOrigin','projectionRole','sourceValues','lineage'})
        self.assertNotIn('mappings',self.data);self.assertNotIn('equivalences',self.data)
        self.mutate_output(lambda d:d['concepts'][0]['sourceValues']['obo_id']['value'].update(value='MONDO_0004975'))

    def test_06_missing_input_stops_before_extraction(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/'copy';shutil.copytree(self.root,root);(root/'02-term-0004975.json').unlink()
            with self.assertRaises(FileNotFoundError):x.extract(root)

    def test_07_changed_source_stops(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/'copy';shutil.copytree(self.root,root)
            p=root/'02-term-0004975.json';p.write_bytes(p.read_bytes()+b' ')
            with self.assertRaises(x.capture.Stop):x.extract(root)

    def test_08_changed_manifest_stops_without_regeneration(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'manifest.json';p.write_bytes(x.freeze.DEFAULT_MANIFEST.read_bytes()+b' ')
            with self.assertRaisesRegex(x.capture.Stop,'Approved manifest digest'):x.extract(self.root,p)

    def test_09_extra_records_and_inferred_relationship_rejected(self):
        self.mutate_output(lambda d:d['concepts'].append(copy.deepcopy(d['concepts'][0])))
        self.mutate_output(lambda d:d['parentAssertions'].append(copy.deepcopy(d['parentAssertions'][0])))
        self.mutate_output(lambda d:d.update(equivalences=[{'inferred':'unapproved'}]))
        self.mutate_output(lambda d:d['parentAssertions'][0]['parent']['obo_id']['value'].update(value='MONDO:0004975'))

    def test_10_changed_provenance_and_permissions_rejected(self):
        self.mutate_output(lambda d:d['concepts'][0]['lineage'].update(sourceDescriptionId='urn:incorrect'))
        self.mutate_output(lambda d:d['concepts'][0]['lineage'].update(captureId='urn:incorrect'))
        self.mutate_output(lambda d:d['permissions'].update(identifier='CC0'))

    def test_11_relocated_artifacts_same_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/'copy';shutil.copytree(self.root,root)
            self.assertEqual(x.freeze.serialize(x.extract(root)),self.raw)

    def test_12_context_and_no_silent_omissions(self):
        self.assertEqual(self.data['sourceContext'],self.manifest['sourceContext'])
        self.assertEqual(self.data['permissions'],self.manifest['permissions'])
        self.mutate_output(lambda d:d['concepts'].pop())
        self.mutate_output(lambda d:d['excludedRawRows'].pop())
        self.mutate_output(lambda d:d['concepts'][0]['sourceValues'].pop('annotation'))

if __name__=='__main__':unittest.main()
