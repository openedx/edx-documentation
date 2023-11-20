# -*- coding: utf-8 -*-
import sys

sys.path.append('../../../')

from shared.conf import *
from shared.edxconf import *

project = u'EdX Learner\'s Guide'

tags.add('Partners')
product = 'Partners'
set_audience(PARTNER, LEARNERS)


def setup(app):
    app.add_config_value('product', '', True)
