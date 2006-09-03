""" tests - test framework

To add a test module, prefix module name with "test_".
"""

import unittest
import os
import fnmatch

def modules():
    """ Generate names specifiers for all test moduleds """
    package = os.path.dirname(__file__)
    names = [__name__ + '.' + name[:-3] for name in
             fnmatch.filter(os.listdir(package), 'test_*.py')]
    names.sort(key=str.lower)
    return names

def suite(*names):
    """ Create a test suite from names specifiers.

    Each name is a dotted name, that may resolve either to a module, a
    test case class within a module, or a test method within a test case
    class. """
    if not names:
        names = modules()
    return unittest.defaultTestLoader.loadTestsFromNames(names)
    
def run(*names):
    """ Run a test suite created with names specifiers """
    return unittest.TextTestRunner().run(suite(*names))
