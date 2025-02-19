# -*- coding: utf-8 -*-
import sys

sys.path.append('../../../')

from shared.conf import *

project = u'Open edX Learner\'s Guide'

exclude_patterns = ['links.rst', 'reusables/*', 'SFD_mathformatting.rst']

tags.add('Open_edX')
product = 'Open_edX'
set_audience(OPENEDX, LEARNERS)

redirects = {
    "*": "https://docs.openedx.org/en/latest/learners/index.html",
}
