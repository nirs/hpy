#-*= coding: utf-8 -*-
""" Execute Hebrew Python scripts 

@copyright: (c) 2006 by Nir Soffer <nirs@freeshell.org>
@license: GNU GPL, see COPYING for details.
"""
__author__ = 'Nir Soffer <nirs@freeshell.org'
__credits__ = 'Amit Aronovitch, Kobi Zamir, Beni Cherniavksy, Noam Raphael'
__version__ = '0.3'

import codecs
import token
import os

from StringIO import StringIO

from hpy import htokenize, hebrew

prefix = 'hpy_'

def pythonString(s):
    """ Return ASCII safe name for non ASCII identifier 
    e.g. פריט ==> hpy_d7a4d7a8d799d798
    """
    if s in hebrew.pythonNames:
        return hebrew.pythonNames[s]
    else:
        try:
            return s.encode('ascii')
        except UnicodeEncodeError:
            return prefix + s.encode('utf-8').encode('hex')

def hebrewString(pythonString):
    """ Return unicode string from mangaled string """
    if pythonString in hebrew.hebrewNames:
        return hebrew.hebrewNames[pythonString]
    else:
        if pythonString.startswith(prefix):
            return pythonString[4:].decode('hex').decode('utf-8')
        else:
            return pythonString

def translate(readline, func):
    """ Translate HPython source to Python source """
    result = StringIO()
    position = 0
    indent = ''
    newline = True
    
    for (type, string, (srow, scol), (erow, ecol), line) \
        in htokenize.generate_tokens(readline):
        
        # Add missing whitespace before tokens
        result.write(u' ' * (scol - position))
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
            indent = u' ' * ecol
            continue            
        elif newline:
            newline = False
            result.write(indent)
        
        # Handle other tokens
        if type == token.NAME:
            result.write(func(string))
        else:
            result.write(string)
                
    return result.getvalue()

def translateString(s, func):
    readline = StringIO(s).readline
    return translate(readline, func)

def printTokens(path):
    """ Print tokens in Hebrew Python module """
    readline = codecs.open(path, 'rU', 'utf-8').readline
    for (type, string, (srow, scol), (erow, ecol), line) \
        in htokenize.generate_tokens(readline):
        name = token.tok_name[type]
        print '%s (%d, %d): "%s"' % (name, scol, ecol, 
                                     string.encode('utf-8'))

def source(path):
    """ Translate Hebrew Python module at path """
    readline = codecs.open(path, 'rU', 'utf-8').readline
    return translate(readline, pythonString)

def execute(path):
    """ Execute Hebrew Python module at path """
    code = compile(source(path), path, 'exec')
    sandbox = {}
    exec code in sandbox

def compileModule(path):
    """ Compile Hebrew Python module to standard Python module

    Raise ValueError if path looks like a Python module, becuase it will
    overwrite the source.
    """
    base, extension = os.path.splitext(path)
    if extension == '.py':
        raise ValueError('compiling Python module will overwrite the source.') 
    python = source(path)
    file = base + '.py'
    f = codecs.open(file, 'wb', 'utf-8')
    try:
        f.write(python)
    finally:
        f.close()
    
