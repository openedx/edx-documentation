# -*- coding: utf-8 -*-
import sys, os

sys.path.append('../../../')

from shared.conf import *

html_theme = 'edx_theme'

html_theme_path = ['../../_themes']

html_favicon = '../../_themes/edx_theme/static/css/favicon.ico'

project = u'EdX Documentation Resources'

def setup(app): app.add_javascript('edx_js.js')

html_static_path = ['_static/edx_js.js']
