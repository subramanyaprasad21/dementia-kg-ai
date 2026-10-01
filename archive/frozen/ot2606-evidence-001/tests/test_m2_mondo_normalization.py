"""Bounded M2.4 no-change assessment; validators inspect values, never transform them."""
import copy
import json
import os
import re
import socket
import sys
import unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
import m2_mondo_extract as extract

ROOT=Path(__file__).resolve().parents[1]
DECISIONS=ROOT/'assessments/mondo-pilot-001.normalization.json'
DIGEST='43d7537f1f8e14340160d9581e8891db7f2dbe60a903c3910648295aae091882'

class InvalidRepresentation(ValueError):pass

def require(ok,reason):
    if not ok:raise InvalidRepresentation(reason)

def field_matches(value,source,key):
    # Existing lossless source encoder is the approved target representation.
    require(value==extract.capture.field(source,key),'source-value:'+key)

def lexical(value):return value['value']['value']

def validate(candidate,original,manifest,sources):
    """Content checks separate from input-digest gate so mutations exercise real rules."""
    require(set(candidate)==set(original),'top-level fields')
    for key in set(original)-{'concepts','parentAssertions','excludedRawRows'}:
        require(candidate[key]==original[key],'context:'+key)
    require(len(candidate['concepts'])==8,'concept count')
    require(len(candidate['parentAssertions'])==5,'parent count')
    require(len(candidate['excludedRawRows'])==6,'excluded count')
    for record,baseline in zip(candidate['concepts'],original['concepts']):
        require(set(record)==set(baseline),'concept fields')
        for key in set(record)-{'sourceValues'}:require(record[key]==baseline[key],'concept metadata:'+key)
        values=record['sourceValues'];source=sources[baseline['lineage']['responseSlot']]
        require(set(values)==set(extract.capture.FIELDS),'selected fields')
        for key in extract.capture.FIELDS:field_matches(values[key],source,key)
        identifier=lexical(values['obo_id']);iri=lexical(values['iri'])
        require(re.fullmatch(r'MONDO:[0-9]{7}',identifier) is not None,'MONDO syntax')
        require(iri=='http://purl.obolibrary.org/obo/MONDO_'+identifier.split(':')[1],'IRI consistency')
        require(lexical(values['ontology_name'])=='mondo','source ontology')
    expected=[(a['child'],a['parent']) for a in manifest['parentAssertions']]
    observed=[]
    for record,baseline in zip(candidate['parentAssertions'],original['parentAssertions']):
        require(set(record)==set(baseline),'parent fields')
        for key in set(record)-{'child','parent'}:require(record[key]==baseline[key],'parent metadata:'+key)
        source=sources[baseline['lineage']['responseSlot']]
        pointer=baseline['lineage']['sourceRecordLocator']['jsonPointer']
        parent=source['_embedded']['terms'][int(pointer.rsplit('/',1)[1])]
        child=sources[baseline['childLineage']['responseSlot']]
        for side,raw in [('child',child),('parent',parent)]:
            require(set(record[side])==set(baseline[side]),'participant fields')
            for key,value in record[side].items():field_matches(value,raw,key)
        observed.append((lexical(record['child']['obo_id']),lexical(record['parent']['obo_id'])))
    require(observed==expected,'directed parent allowlist')
    require(candidate['excludedRawRows']==original['excludedRawRows'],'exclusion provenance')
    return {'status':'pass','concepts':'8','acceptedParents':'5','excludedRawRows':'6','transformations':[]}

class Normalization(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root=Path(os.environ.get('MONDO_PILOT_ARTIFACTS',str(extract.freeze.DEFAULT_ARTIFACTS)))
        cls.hashes={p.name:extract.capture.sha(p.read_bytes()) for p in cls.root.iterdir()}
        cls.raw=extract.OUTPUT.read_bytes()
        if extract.capture.sha(cls.raw)!=DIGEST:raise RuntimeError('Approved extraction changed; do not regenerate')
        extract.verify(artifacts=cls.root)
        cls.original=json.loads(cls.raw)
        cls.manifest=json.loads(extract.freeze.DEFAULT_MANIFEST.read_bytes())
        cls.sources={e['slot']:extract.capture.parse((cls.root/e['artifact']).read_bytes())
                     for e in cls.manifest['responses']}

    @classmethod
    def tearDownClass(cls):
        assert extract.OUTPUT.read_bytes()==cls.raw
        assert cls.hashes=={p.name:extract.capture.sha(p.read_bytes()) for p in cls.root.iterdir()}

    def setUp(self):
        p=patch.object(socket.socket,'connect',side_effect=AssertionError('Network forbidden'))
        p.start();self.addCleanup(p.stop)

    def check(self,value):return validate(value,self.original,self.manifest,self.sources)

    def reject(self,mutation):
        value=copy.deepcopy(self.original);mutation(value)
        with self.assertRaises((InvalidRepresentation,KeyError,TypeError)):self.check(value)

    def test_01_input_integrity_and_unchanged_digest(self):
        self.assertEqual(extract.verify(artifacts=self.root)['sha256'],DIGEST)
        self.assertEqual(self.original['freeze']['sha256'],extract.MANIFEST_HASH)

    def test_02_decision_record_determinism_and_scope(self):
        raw=DECISIONS.read_bytes();d=extract.capture.parse(raw)
        self.assertEqual(extract.freeze.serialize(d),raw)
        self.assertEqual(d['input']['sha256'],DIGEST)
        self.assertEqual(d['transformations'],[])
        self.assertEqual({r['category'] for r in d['decisions']},{'identifiers','labels','annotations',
            'types-and-missingness','edition-and-time','parents-and-exclusions','lineage-and-representation'})
        for row in d['decisions']:
            self.assertEqual(row['transformation'],'none')
            for key in ['originalRepresentation','targetRepresentation','justification','informationLossRisk']:
                self.assertTrue(row[key])
            for name in row['validationTests']:self.assertTrue(callable(getattr(self,name)))

    def test_03_actual_representation_and_no_changes(self):
        value=copy.deepcopy(self.original);before=extract.freeze.serialize(value)
        self.assertEqual(self.check(value)['transformations'],[])
        self.assertEqual(extract.freeze.serialize(value),before)
        self.assertEqual(len(value['concepts']),8);self.assertEqual(len(value['parentAssertions']),5)

    def test_04_identifier_and_iri_mutations(self):
        for value in ['MONDO_0004975','mondo:0004975','MONDO:4975',' MONDO:0004975']:
            with self.subTest(value=value):
                self.reject(lambda d:d['concepts'][0]['sourceValues']['obo_id']['value'].update(value=value))
        self.reject(lambda d:d['concepts'][0]['sourceValues']['iri']['value'].update(value='https://purl.obolibrary.org/obo/MONDO_0004975'))

    def test_05_labels_and_annotations(self):
        self.reject(lambda d:d['concepts'][0]['sourceValues']['label']['value'].update(value='Alzheimer Disease'))
        self.reject(lambda d:d['concepts'][0]['sourceValues']['label']['value'].update(value='Alzheimer disease '))
        self.reject(lambda d:d['concepts'][0]['sourceValues'].update(annotation={'state':'present','value':{'type':'object','value':{}}}))
        self.reject(lambda d:d['concepts'][0]['sourceValues'].pop('obo_xref'))

    def test_06_array_order_and_no_equivalence(self):
        def reorder(d):
            values=d['concepts'][0]['sourceValues']['obo_xref']['value']['value']
            self.assertGreater(len(values),1);values.reverse()
        self.reject(reorder)
        self.reject(lambda d:d.update(equivalences=[{'repaired':'unsupported'}]))
        self.reject(lambda d:d['concepts'][0].update(canonicalDisease='MONDO:0004975'))

    def test_07_missingness_controls(self):
        # Synthetic representation controls only; no invented missing biomedical records.
        sources=[{}, {'v':None},{'v':''},{'v':[]},{'v':{}},{'v':False}]
        wrappers=[extract.capture.field(s,'v') for s in sources]
        self.assertEqual(len({extract.capture.canonical(w) for w in wrappers}),6)
        for i,source in enumerate(sources):
            field_matches(wrappers[i],source,'v')
            for j,wrapper in enumerate(wrappers):
                if i!=j:
                    with self.assertRaises(InvalidRepresentation):field_matches(wrapper,source,'v')
        self.reject(lambda d:d['concepts'][0]['sourceValues'].update(label={'state':'absent'}))

    def test_08_types_and_lexical_precision(self):
        source=extract.capture.parse(b'{"v":1.00}')
        field_matches(extract.capture.field(source,'v'),source,'v')
        for raw in [b'{"v":1}',b'{"v":"1.00"}',b'{"v":null}']:
            with self.assertRaises(InvalidRepresentation):field_matches(extract.capture.field(extract.capture.parse(raw),'v'),source,'v')
        self.reject(lambda d:d['concepts'][0]['sourceValues'].update(is_obsolete={'state':'present','value':{'type':'null'}}))

    def test_09_context_and_timestamp_mutations(self):
        self.reject(lambda d:d['sourceContext'].update(loaded=d['sourceContext']['loaded']+'Z'))
        self.reject(lambda d:d['sourceContext'].update(edition='2026-09-24'))
        self.reject(lambda d:d['concepts'][0]['lineage'].update(captureStarted=d['sourceContext']['loaded']))

    def test_10_parent_direction_and_exclusion_mutations(self):
        def reverse(d):
            p=d['parentAssertions'][0];p['child']['obo_id'],p['parent']['obo_id']=p['parent']['obo_id'],p['child']['obo_id']
        self.reject(reverse)
        self.reject(lambda d:d['parentAssertions'].append(copy.deepcopy(d['excludedRawRows'][0])))
        self.reject(lambda d:d['excludedRawRows'][0].update(disposition='accepted'))
        self.reject(lambda d:d['parentAssertions'][0]['lineage']['sourceRecordLocator'].update(jsonPointer='/_embedded/terms/0'))

    def test_11_lineage_mutations(self):
        for key in ['sourceDescriptionId','captureId','rawSha256','contract']:
            with self.subTest(key=key):
                self.reject(lambda d:d['concepts'][0]['lineage'].update({key:'incorrect'}))
        self.reject(lambda d:d['parentAssertions'][0].pop('childLineage'))
        self.reject(lambda d:d['permissions'].update(identifier='CC0'))

    def test_12_structure_and_omission_mutations(self):
        self.reject(lambda d:d['concepts'].pop())
        self.reject(lambda d:d['concepts'].append(copy.deepcopy(d['concepts'][0])))
        self.reject(lambda d:d['excludedRawRows'].pop())
        self.reject(lambda d:d['parentAssertions'].pop())

if __name__=='__main__':unittest.main()
