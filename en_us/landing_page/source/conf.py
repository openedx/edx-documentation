# -*- coding: utf-8 -*-
import sys

sys.path.append('../../../')

from shared.conf import *

project = u'EdX Documentation Resources'


def setup(app): app.add_js_file('edx_js.js')

html_static_path = ['_static/edx_js.js']
