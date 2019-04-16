# -*- coding: utf-8 -*-
import sys

sys.path.append('../../../')

from shared.conf import *

project = u'Registrar API Guide'

set_audience(OPENEDX, DEVELOPERS)

extensions = [
  'sphinxcontrib.openapi',
  'sphinx.ext.graphviz']
