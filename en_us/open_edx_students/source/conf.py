# -*- coding: utf-8 -*-
import sys

sys.path.append('../../../')

from shared.conf import *

project = u'Open edX Learner\'s Guide: Palm Release'

exclude_patterns = ['links.rst', 'reusables/*', 'SFD_mathformatting.rst']

tags.add('Open_edX')
product = 'Open_edX'
set_audience(OPENEDX, LEARNERS)


def setup(app):
    app.add_config_value('product', '', True)
