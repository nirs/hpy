#-*= coding: utf-8 -*-
""" Execute Hebrew Python scripts """

__author__ = 'Nir Soffer <nirs@freeshell.org'
__credits__ = 'Noam Raphael, Beni Cherniavksy'
__version__ = '0.1.3'

import codecs
import token
import cStringIO

from hpy import htokenize, hebrew

DEBUG = 0

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
    result = cStringIO.StringIO()
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
            result.write(string)
            continue  
        elif type == token.INDENT:
            newline = False
            indent = string
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
            if string in hebrew.keywords:
                result.write(hebrew.keywords[string])
            else:
                result.write(mangle(string))
        else:
            result.write(string.encode('utf-8'))        
                
    return result.getvalue()

def printTokens(readline):
    """ Print tokens in Hebrew Python source (for debugging) """
    for (type, string, (srow, scol), (erow, ecol), line) \
        in htokenize.generate_tokens(readline):
        print '%s (%d, %d): "%s"' % (token.tok_name[type], scol, ecol, string.encode('utf-8'))

def source(path):
    """ Translate Hebrew Python source at path """
    if DEBUG: 
        printTokens(codecs.open(path, 'r', 'utf-8').readline)
    return translate(codecs.open(path, 'r', 'utf-8').readline)

def execute(path):
    """ Execute Hebrew Python source at path """
    translation= source(path)
    if DEBUG: 
        print translation
    code = compile(translation, path, 'exec')
    sandbox = {}
    exec code in sandbox
