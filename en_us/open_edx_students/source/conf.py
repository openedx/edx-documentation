# -*- coding: utf-8 -*-
import sys, os

sys.path.append('../../../')

from shared.conf import *

html_theme = 'edx_theme'

html_theme_path = ['../../_themes']

html_favicon = '../../_themes/edx_theme/static/css/favicon.ico'

project = u'Open edX Learner\'s Guide'

exclude_patterns = ['links.rst', 'reusables/*', 'SFD_mathformatting.rst']

tags.add('Open_edX')
product = 'Open_edX'
set_audience(OPENEDX, LEARNERS)

def setup(app):
    app.add_config_value('product', '', True)
