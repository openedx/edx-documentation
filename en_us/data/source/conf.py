# -*- coding: utf-8 -*-
import sys, os

sys.path.append('../../../')

from shared.conf import *

html_theme = 'edx_theme'

html_theme_path = ['../../_themes']

html_favicon = '../../_themes/edx_theme/static/css/favicon.ico'

project = u'EdX Research Guide'
set_audience(PARTNER, RESEARCHERS)

# Do not attempt to publish .rst files if they are included in
# other .rst files. This suppresses WARNINGs about documents not
# being included in any toctree.
exclude_patterns = ['internal_data_formats/special_exam_events.rst',
'internal_data_formats/special_exam_development_events.rst',
'internal_data_formats/special_exam_events_overview.rst']
