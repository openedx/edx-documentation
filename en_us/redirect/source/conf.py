# -*- coding: utf-8 -*-
import sys, os

sys.path.append('../../../')

from shared.conf import *

def setup(app): app.add_javascript('file.js')

html_static_path = ['_static/file.js']
