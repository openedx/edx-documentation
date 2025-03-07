# -*- coding: utf-8 -*-
import sys

sys.path.append('../../../')

from shared.conf import *
from shared.edxconf import *

project = u'edX.org Learner\'s Guide'

exclude_patterns = ['links.rst', 'reusables/*', 'SFD_mathformatting.rst']

tags.add('Open_edX')
product = 'Open_edX'
set_audience(OPENEDX, LEARNERS)

html_theme_options["announcement"] = "This is the learner's guide for edx.org courses. For Open edX courses, please see the <a href='https://docs.openedx.org/en/latest/learners/index.html'>Open edX Learner's Guide</a>."


def setup(app):
    app.add_config_value('product', '', True)
