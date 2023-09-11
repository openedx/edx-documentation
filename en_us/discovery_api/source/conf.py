# -*- coding: utf-8 -*-
import sys

sys.path.append('../../../')

from shared.conf import *
from shared.edxconf import *

project = u'Discovery Service API Guide'

tags.add('Partners')
set_audience(PARTNER, COURSE_TEAMS)

product = 'Partners'


def setup(app):
    app.add_config_value('product', '', True)
