# -*- coding: utf-8 -*-
import sys

sys.path.append('../../../')

from shared.conf import *

project = u'Building and Running an MITx Online Course'

tags.add('Partners')
set_audience(PARTNER, COURSE_TEAMS)

product = 'Partners'

root_doc = 'https://github.com/jakirschner/QA-MITx-documentation/en_us/course_authors/source/index'

def setup(app):
    app.add_config_value('product', '', True)
