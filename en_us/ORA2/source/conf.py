# -*- coding: utf-8 -*-
#
import sys, os

sys.path.append('../../../')

from shared.conf import *

html_theme = 'edx_theme'

html_theme_path = ['../../_themes']

html_favicon = '../../_themes/edx_theme/static/css/favicon.ico'
project = u'Creating a Peer Assessment'

exclude_patterns = ['PeerAssessment.rst', 'PeerAssessment_Students.rst', 'read_me.rst']
