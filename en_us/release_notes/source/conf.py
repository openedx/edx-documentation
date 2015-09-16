# -*- coding: utf-8 -*-
import sys, os

sys.path.append('../../../')

from shared.conf import *

html_theme = 'edx_theme'

html_theme_path = ['../../_themes']

html_favicon = '../../_themes/edx_theme/static/css/favicon.ico'

# General information about the project.
project = u'edX Release Notes'

#remove directory when content is first added to it, and add to index
exclude_patterns = ['links.rst', 'reusables/*', '2015/analytics/*2015.rst', 
                    '2015/discussions/*2015.rst', '2015/documentation/*2015.rst',
                    '2015/insights/*2015.rst', '2015/lms/*2015.rst',
                    '2015/mobile/*2015.rst', '2015/openedx/*2015.rst', 
                    '2015/ora/*2015.rst', '2015/studio/*2015.rst',
                    '2015/website/*2015.rst', '2015/xblocks/*2015.rst']

