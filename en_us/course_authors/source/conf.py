# -*- coding: utf-8 -*-
#

import sys, os

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'


html_theme = 'nature'
#html_theme_path = ["../../.."]


sys.path.append(os.path.abspath('../../../'))
sys.path.append(os.path.abspath('../../'))

#from docs.shared.conf import *

sys.path.insert(0, os.path.abspath('.'))

master_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
#templates_path.append('source/_templates')

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path.append('source/_static')


# General information about the project.
project = u'Building and Running an edX Course'
copyright = u'2014, edX'
last_updated = u'November 4, 2014'

# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
release = ''
