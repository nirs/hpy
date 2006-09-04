#-*- coding: utf-8 -*-
import os
import tempfile
import shutil
import unittest
import difflib
import codecs
import hpy


class basic_translation(unittest.TestCase):

    hebrew_line = u'הדפס "שלום עולם!"'
    python_line = u'print "שלום עולם!"'
    hebrew_multiline = u"""
א = 1
ב = 2
"""
    python_multiline = u"""
hpy_d790 = 1
hpy_d791 = 2
"""

    def test_empty_to_python(self):
        self.assertEqual(to_python(u''), u'')

    def test_python_to_python(self):
        self.assertEqual(to_python(self.python_line), self.python_line)

    def test_line_to_python(self):
        self.assertEqual(to_python(self.hebrew_line),
                         self.python_line)
    
    def test_multiline_to_python(self):
        self.assertEqual(to_python(self.hebrew_multiline),
                         self.python_multiline)

    def test_empty_to_hebrew(self):
        self.assertEqual(to_hebrew(u''), u'')

    def test_hebrew_to_hebrew(self):
        self.assertEqual(to_hebrew(self.hebrew_line), self.hebrew_line)

    def test_line_to_hebrew(self):
        self.assertEqual(to_hebrew(self.python_line),
                         self.hebrew_line)

    def test_multiline_to_hebrew(self):
        self.assertEqual(to_hebrew(self.python_multiline),
                         self.hebrew_multiline)


class hebrew_round_trip(unittest.TestCase):
    """ Test example Hebrew modules 
    
    Some of the modules contain Python code, and can not do round trip
    (the Python get translated automatically to Hebrew :-) """

    def test_99bottles(self):
        self.round_trip('99bottles')

    def test_factorial(self):
        self.round_trip('factorial')

    def test_fibonaci(self):
        self.round_trip('fibonaci')

    def test_fractal(self):
        self.round_trip('fractal')

    def test_gtk(self):
        self.round_trip('gtk')

    def test_hello(self):
        self.round_trip('hello')

    def test_tree(self):
        self.round_trip('tree')

    # Helpers
    
    def round_trip(self, name):
        a = self.read(name)
        b = to_hebrew(to_python(a))
        self.assertEqual(a, b, diff(a, b))

    def read(self, module):
        path = 'examples/%s.hpy' % module
        return codecs.open(path, 'rb', 'utf-8').read()


class python_modules(unittest.TestCase):
    """ Test real Python modules """

    def test_re_to_python(self):
        self.to_python('re')

    def test_re_round_trip(self):
        self.round_trip('re')
    
    def test_statvfs_to_python(self):
        self.to_python('statvfs')

    def test_statvfs_round_trip(self):
        self.round_trip('statvfs')

    def test_token_to_python(self):
        self.to_python('token')

    def test_token_round_trip(self):
        self.round_trip('token')

    # Helpers
     
    def to_python(self, name):
        a = self.read(name)
        b = to_python(a)
        self.assertEqual(a, b, diff(a, b)) 
     
    def round_trip(self, name):
        a = self.read(name)
        b = to_python(to_hebrew(a))
        self.assertEqual(a, b, diff(a, b)) 
 
    def read(self, module):
        m = __import__(module)
        path = m.__file__.replace('.pyc', '.py')
        return codecs.open(path, 'rb', 'ascii').read()


class compile_module(unittest.TestCase):

    hebrew = u'''הדפס "שלום עולם!"'''
    python = u'''print "שלום עולם!"'''
    
    def setUp(self):
        self.dir = tempfile.mkdtemp()
        self.hebrew_file = os.path.join(self.dir, 'hello.hpy')
        self.python_file = os.path.join(self.dir, 'hello.py')
        f = codecs.open(self.hebrew_file, 'wb', 'utf-8')
        f.write(self.hebrew)
        f.close()

    def tearDown(self):
        shutil.rmtree(self.dir, ignore_errors=1)

    def test_save_as_python_module(self):
        hpy.compileModule(self.hebrew_file)
        self.assert_(os.path.exists(self.python_file))
    
    def test_translate_to_python(self):
        hpy.compileModule(self.hebrew_file)
        python = codecs.open(self.python_file, 'rb', 'utf-8').read()
        self.assertEqual(python, self.python)
        
    def test_raise_if_python_module(self):
        self.assertRaises(ValueError, hpy.compileModule, self.python_file)
        
        
# Helper functions

def to_python(s):
    return hpy.translateString(s, hpy.pythonString)

def to_hebrew(s):
    return hpy.translateString(s, hpy.hebrewString)

def diff(a, b):
    diff = difflib.unified_diff(a.splitlines(), b.splitlines())
    return '\n'.join(diff).encode('utf-8')


