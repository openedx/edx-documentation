# -*- coding: utf-8 -*-

import sys, os

sys.path.append('../../../')

from shared.conf import *

html_theme = 'edx_theme'

html_theme_path = ['../../_themes']

html_favicon = '../../_themes/edx_theme/static/css/favicon.ico'

tags.add('OLX')
product = 'OLX'
set_audience(OPENEDX, DEVELOPERS)

def setup(app):
    app.add_config_value('product', '', True)

# General information about the project.
project = u'EdX Open Learning XML Guide - Alpha Version'
