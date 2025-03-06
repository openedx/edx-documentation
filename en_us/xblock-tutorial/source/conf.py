# -*- coding: utf-8 -*-

import sys

sys.path.append('../../../')

from shared.conf import *

# General information about the project.
project = u'Open edX XBlock Tutorial'
set_audience(OPENEDX, DEVELOPERS)


redirects = {
    "*": "https://docs.openedx.org/projects/xblock/en/latest/xblock-tutorial/$source.html",
}
