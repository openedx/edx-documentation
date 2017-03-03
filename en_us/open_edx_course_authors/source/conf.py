# -*- coding: utf-8 -*-
import sys

sys.path.append('../../../')

from shared.conf import *

tags.add('Open_edX')
set_audience(OPENEDX, COURSE_TEAMS)

product = 'Open_edX'


def setup(app):
    app.add_config_value('product', '', True)

project = u'Building and Running an Open edX Course: Ficus Release'
