""" Run tests

usage: test [name-specifiers]

To run all tests::

    test
    
To run specific tests module::

    test test_foo
    
To run specific test case::

    test test_foo.test_case
    
To run specific test method::

    test test_foo.test_case.test_this
"""

import sys
import tests

# run expect fully qualified names
names = ['tests.' + name for name in sys.argv[1:]]

result = tests.run(*names)
sys.exit(not result.wasSuccessful())
