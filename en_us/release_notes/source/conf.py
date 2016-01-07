# -*- coding: utf-8 -*-
import sys, os

sys.path.append('../../../')

from shared.conf import *

html_theme = 'edx_theme'

html_theme_path = ['../../_themes']

html_favicon = '../../_themes/edx_theme/static/css/favicon.ico'

# General information about the project.
project = u'EdX Release Notes'

#remove directory when content is first added to it, and add to index
exclude_patterns = ['links.rst', 'reusables/*', '20??/analytics/*20??.rst',
                    '20??/discussions/*20??.rst', '20??/documentation/*20??.rst',
                    '20??/insights/*20??.rst', '20??/lms/*20??.rst',
                    '20??/mobile/*20??.rst', '20??/openedx/*20??.rst',
                    '20??/ora/*20??.rst', '20??/studio/*20??.rst',
                    '20??/website/*20??.rst', '20??/xblocks/*20??.rst']

