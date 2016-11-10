# -*- coding: utf-8 -*-
import sys

sys.path.append('../../../')

from shared.conf import *

project = u'EdX Research Guide'
set_audience(PARTNER, RESEARCHERS)

# Do not attempt to publish .rst files if they are included in
# other .rst files. This suppresses WARNINGs about documents not
# being included in any toctree.
exclude_patterns = ['internal_data_formats/special_exam_events.rst',
'internal_data_formats/special_exam_development_events.rst',
'internal_data_formats/special_exam_events_overview.rst']
