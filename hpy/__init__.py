#-*= coding: utf-8 -*-
""" Execute Hebrew Python scripts 

@copyright: (c) 2006 by Nir Soffer <nirs@freeshell.org>
@license: GNU GPL, see COPYING for details.
"""
__author__ = 'Nir Soffer <nirs@freeshell.org'
__credits__ = 'Kobi Zamir, Noam Raphael, Beni Cherniavksy'
__version__ = '0.2.1'

import codecs
import token

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

from hpy import htokenize, hebrew

def mangle(s):
    """ Return ASCII safe name for non ASCII identifier 
    e.g. פריט ==> hpy_d7a4d7a8d799d798
    """
    try:
        return s.encode('ascii')
    except UnicodeEncodeError:
        return 'hpy_' + s.encode('utf-8').encode('hex')

def translate(readline):
    """ Translate HPython source to Python source """
    result = StringIO()
    position = 0
    indent = ''
    newline = True
    
    for (type, string, (srow, scol), (erow, ecol), line) \
        in htokenize.generate_tokens(readline):
        
        # Add missing whitespace before tokens
        result.write(' ' * (scol - position))
        position = ecol

        # Handle indentation
        if type == token.NEWLINE:
            newline = True
            result.write(str(string))
            continue  
        elif type == token.INDENT:
            newline = False
            indent = str(string)
            result.write(indent)
            continue
        elif type == token.DEDENT:
            indent = ' ' * ecol
            continue            
        elif newline:
            newline = False
            result.write(indent)
        
        # Handle other tokens
        if type == token.NAME:
            if string in hebrew.names:
                result.write(hebrew.names[string])
            else:
                result.write(mangle(string))
        else:
            result.write(string.encode('utf-8'))
                
    return result.getvalue()

def printTokens(path):
    """ Print tokens in Hebrew Python source """
    readline = codecs.open(path, 'r', 'utf-8').readline
    for (type, string, (srow, scol), (erow, ecol), line) \
        in htokenize.generate_tokens(readline):
        name = token.tok_name[type]
        print '%s (%d, %d): "%s"' % (name, scol, ecol, 
                                     string.encode('utf-8'))

def source(path):
    """ Translate Hebrew Python source at path """
    readline = codecs.open(path, 'r', 'utf-8').readline
    return translate(readline)

def execute(path):
    """ Execute Hebrew Python source at path """
    code = compile(source(path), path, 'exec')
    sandbox = {}
    exec code in sandbox
