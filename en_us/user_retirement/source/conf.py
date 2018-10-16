# -*- coding: utf-8 -*-
import sys

sys.path.append('../../../')

from shared.conf import *

project = u'User Retirement Guide for Open edX Administrators'

set_audience(OPENEDX, DEVELOPERS)

extensions = ['sphinx.ext.graphviz']
