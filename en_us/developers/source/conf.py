# -*- coding: utf-8 -*-
import sys, os

sys.path.append('../../../')

from shared.conf import *

html_theme = 'edx_theme'

html_theme_path = ['../../_themes']

html_favicon = '../../_themes/edx_theme/static/css/favicon.ico'

project = u'Open edX Developer\'s Guide'
set_audience(OPENEDX, DEVELOPERS)

exclude_patterns = ['i18n.rst', 'i18n_translators_guide.rst']
