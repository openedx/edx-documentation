# -*- coding: utf-8 -*-
import sys, os

sys.path.append('../../../')

from shared.conf import *

html_theme = 'edx_theme'

html_theme_path = ['../../_themes']

html_favicon = '../../_themes/edx_theme/static/css/favicon.ico'

project = u'Building and Running an edX Course'

tags.add('Partners')

product = 'Partners'

def setup(app):
    app.add_config_value('product', '', True)
