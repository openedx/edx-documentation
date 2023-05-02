# -*- coding: utf-8 -*-
import sys

sys.path.append('../../../')

from shared.conf import *
from shared.edxconf import *

project = u'Building and Running an MITx Online Course'

tags.add('Partners')
set_audience(PARTNER, COURSE_TEAMS)

product = 'Partners'

root_doc = 'index'

def setup(app):
    app.add_config_value('product', '', True)
