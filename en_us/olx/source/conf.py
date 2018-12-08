# -*- coding: utf-8 -*-

import sys

sys.path.append('../../../')

from shared.conf import *

tags.add('OLX')
product = 'OLX'
set_audience(OPENEDX, DEVELOPERS)


def setup(app):
    app.add_config_value('product', '', True)

# General information about the project.
project = u'EdX Open Learning XML Guide - Alpha Version'
