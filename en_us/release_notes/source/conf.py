# -*- coding: utf-8 -*-
#

import sys, os

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

sys.path.append(os.path.abspath('../../../../'))
sys.path.append(os.path.abspath('../../../'))

#from docs.shared.conf import *

sys.path.insert(0, os.path.abspath('.'))

master_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
#templates_path.append('source/_templates')

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path.append('source/_static')

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# General information about the project.
project = u'edX Release Notes'
copyright = u'2015, edX'

# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
release = ''

#remove directory when content is first added to it, and add to index
exclude_patterns = ['links.rst', 'reusables/*', 'insights/*', 'openedx/*', 'xblocks/*']