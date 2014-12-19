# -*- coding: utf-8 -*-
#

import sys, os
#from path import path

sys.path.append('../../../../')

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    #import sphinx_rtd_theme
    #html_theme = 'sphinx_rtd_theme'
    #html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
    html_theme = 'edx_theme'
    html_theme_path = ["../.."]

if on_rtd:  # only import and set the theme if we're building docs locally
    #import sphinx_rtd_theme
    #html_theme = 'sphinx_rtd_theme'
    #html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
    html_theme = 'edx_theme'
    html_theme_path = ["../.."]

#sys.path.append(os.path.abspath('../../../'))
#sys.path.append(os.path.abspath('../../'))

#from docs.shared.conf import *

sys.path.insert(0, os.path.abspath('.'))

master_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
templates_path = ["."]
templates_path.append('_templates')

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["."]
html_static_path.append('source/_static')


# General information about the project.
project = u'Building and Running an edX Course'
copyright = u'2014, edX'
last_updated = u'November 4, 2014'

# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
release = ''
