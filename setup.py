#!/usr/bin/env python

import os
from distutils.core import setup
import hpy

setup (name = 'hpy',
       version = hpy.__version__,
       description = hpy.__doc__.splitlines()[0].strip(),
       license = "GNU GPL",
       url = 'http://nirs.freeshell.org/hpy/',
       download_url = 'http://nirs.freeshell.org/hpy/hpy-%s.tar.gz' % hpy.__version__,
       author = 'Nir Soffer',
       author_email = 'nirs@freeshell.org',
       packages = ["hpy",""],
       scripts = ["hpython","hpython"])
