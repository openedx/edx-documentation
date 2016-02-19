# -*- coding: utf-8 -*-
import sys, os

sys.path.append('../../../')

from shared.conf import *

html_theme = 'edx_theme'

html_theme_path = ['../../_themes']

html_favicon = '../../_themes/edx_theme/static/css/favicon.ico'

# General information about the project.
project = u'EdX 2013-2014 Release Notes'

#remove directory when content is first added to it, and add to index
exclude_patterns = ['links.rst', 'reusables/*', '20??/*/*20??.rst']

