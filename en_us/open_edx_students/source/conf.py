# -*- coding: utf-8 -*-
import sys, os

sys.path.append('../../../')

from shared.conf import *

html_theme = 'edx_theme'

html_theme_path = ['../../_themes']

html_favicon = '../../_themes/edx_theme/static/css/favicon.ico'

project = u'Open edX Learner\'s Guide'

tags.add('Open_edX')

product = 'Open_edX'

def setup(app):
    app.add_config_value('product', '', True)
