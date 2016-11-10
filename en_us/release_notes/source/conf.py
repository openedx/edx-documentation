# -*- coding: utf-8 -*-
import sys

sys.path.append('../../../')

from shared.conf import *

# General information about the project.
project = u'EdX Release Notes'

# remove directory when content is first added to it, and add to index
exclude_patterns = ['links.rst', 'reusables/*', '20??/*/*20??.rst', '20??/*/*20??-??-??.rst', 'coming_soon.rst']

set_audience(PARTNER, COURSE_TEAMS)
