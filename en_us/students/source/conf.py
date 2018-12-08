# -*- coding: utf-8 -*-
import sys

sys.path.append('../../../')

from shared.conf import *

project = u'EdX Learner\'s Guide'

exclude_patterns = ['links.rst', 'reusables/*', 'SFD_mathformatting.rst']

tags.add('Partners')
product = 'Partners'
set_audience(PARTNER, LEARNERS)


def setup(app):
    app.add_config_value('product', '', True)
