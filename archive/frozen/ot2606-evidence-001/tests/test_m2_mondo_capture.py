"""Synthetic transport/identity controls, not additional biomedical evidence."""
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
import m2_mondo_capture as m

class Response(io.BytesIO):
    def __init__(self,body=b'{}',status=200,headers=None):
        super().__init__(body);self.code=status;self.headers=headers or {'Content-Length':str(len(body))}

class Contract(unittest.TestCase):
    def test_canonical_order_unicode(self):
        self.assertEqual(m.canonical({'b':'2','a':'1'}),b'{"a":"1","b":"2"}')
        self.assertEqual(m.sha(m.canonical({'b':'2','a':'1'})),m.sha(m.canonical({'a':'1','b':'2'})))
        with self.assertRaises(ValueError):m.canonical({'number':1})

    def test_lossless_numbers_and_type_separation(self):
        a=m.typed(m.parse(b'{"x":1.00,"y":9007199254740993}'))
        self.assertEqual(a['value']['x']['lexeme'],'1.00')
        self.assertEqual(a['value']['y']['lexeme'],'9007199254740993')
        self.assertNotEqual(m.typed(m.parse(b'1')),m.typed('1'))
        self.assertNotEqual(m.typed(True),m.typed('true'))

    def test_missing_empty_null_distinct(self):
        values=[m.field({},'x')]+[m.field({'x':v},'x') for v in [None,'',[],{}]]
        self.assertEqual(len({m.canonical(v) for v in values}),5)

    def test_reject_ambiguous_json(self):
        for body in [b'{"a":1,"a":2}',b'NaN',b'Infinity',b'{']:
            with self.assertRaises(ValueError):m.parse(body)

    def test_order_and_duplicates_retained(self):
        self.assertNotEqual(m.canonical(m.typed(['a','b'])),m.canonical(m.typed(['b','a'])))
        self.assertNotEqual(m.canonical(m.typed(['a'])),m.canonical(m.typed(['a','a'])))

    def test_replay_revision_and_new_capture(self):
        c={'edition':m.EDITION,'versionIri':m.VERSION_IRI,'loaded':'time-a','updated':'time-a'}
        d=m.description('term-0004975',{'label':'synthetic-control'},c)
        self.assertEqual(m.identity(d),m.identity(json.loads(json.dumps(d))))
        self.assertNotEqual(m.identity(d),m.identity(m.description('term-0004975',{'label':'changed-control'},c)))
        self.assertEqual(m.identity(d),m.identity(m.description('term-0004975',{'label':'synthetic-control'},dict(c,loaded='time-b'))))
        a={'profile':'m2-capture-1','execution':'control/1'}
        self.assertNotEqual(m.identity(a),m.identity(dict(a,execution='control/2')))

    def test_finite_scope(self):
        self.assertEqual(len(m.plan()),15);self.assertEqual(len(m.TERMS),8);self.assertEqual(len(m.PARENTS),5)
        self.assertEqual({p for p in m.PARENTS.values()}-set(m.TERMS),set())

    def test_edition_gate(self):
        valid={'version':m.EDITION,'config':{'versionIri':m.VERSION_IRI},'status':'LOADED','loaded':'a','updated':'b'}
        self.assertEqual(m.edition(valid)['loaded'],'a')
        for change in [{'version':'other'},{'loaded':None},{'status':'LOADING'}]:
            with self.assertRaises(m.Stop):m.edition(dict(valid,**change))

    def test_parent_scope_and_completeness(self):
        def row(t):return {'obo_id':'MONDO:'+t,'iri':'http://purl.obolibrary.org/obo/MONDO_'+t,'ontology_name':'mondo','is_obsolete':False}
        data={'_embedded':{'terms':[row('0017160'),row('9999999')]},'page':{'number':0,'totalPages':1,'totalElements':2}}
        projection,result=m.project('parents-0010857',data)
        self.assertEqual(result['verified'],'yes');self.assertEqual(len(projection['parents']),1)
        self.assertEqual(projection['excludedRows'],'1')
        data['page']['totalPages']=2
        with self.assertRaises(m.Stop):m.project('parents-0010857',data)
        data['page']['totalPages']=1;data['_embedded']['terms'][0]=row('9999998')
        with self.assertRaises(m.Stop):m.project('parents-0010857',data)

    def batch(self,root,response):
        b=m.Batch(Path(root)/'test-batch');b.opener=type('Opener',(),{'open':lambda _,*a,**k:response})()
        return b

    def test_error_body_counted_and_retained(self):
        with tempfile.TemporaryDirectory() as root:
            b=self.batch(root,Response(b'failure',503))
            with self.assertRaises(m.Stop):b.fetch('metadata-before',m.API)
            self.assertEqual((b.state['requests'],b.state['bytes']),(1,7))
            self.assertEqual(b.state['records'][0]['receipt']['rawSha256'],m.sha(b'failure'))

    def test_byte_ceiling_stops_and_no_reset(self):
        with tempfile.TemporaryDirectory() as root,patch.object(m,'MAX_BYTES',5):
            b=self.batch(root,Response(b'12345678'))
            with self.assertRaises(m.Stop):b.fetch('metadata-before',m.API)
            self.assertEqual(b.state['bytes'],5)
            with self.assertRaises(m.Stop):b.fetch('metadata-after',m.API)
            self.assertEqual(b.state['requests'],1)
            with self.assertRaises(FileExistsError):m.Batch(b.root)

    def test_request_limit_truncation_and_compression(self):
        with tempfile.TemporaryDirectory() as root:
            b=self.batch(root,Response(b'{}',headers={'Content-Length':'8'}))
            with self.assertRaises(m.Stop):b.fetch('metadata-before',m.API)
            b.state['requests']=100
            with self.assertRaises(m.Stop):b.fetch('metadata-after',m.API)
        with tempfile.TemporaryDirectory() as root:
            b=self.batch(root,Response(b'encoded',headers={'Content-Encoding':'gzip'}))
            with self.assertRaises(m.Stop):b.fetch('metadata-before',m.API)
            self.assertEqual(b.state['bytes'],0)

    def test_redirect_not_followed(self):
        self.assertIsNone(m.NoRedirect().redirect_request(None,None,302,'',{},m.API))
        with tempfile.TemporaryDirectory() as root:
            b=self.batch(root,Response(b'moved',302,{'Location':'https://example.invalid/'}))
            with self.assertRaises(m.Stop):b.fetch('metadata-before',m.API)
            self.assertEqual((b.state['requests'],b.state['bytes']),(1,5))

    def test_no_repository_raw_storage(self):
        with self.assertRaises(m.Stop):m.Batch(Path(m.__file__).resolve().parents[1]/'raw-forbidden')

if __name__=='__main__':unittest.main()
