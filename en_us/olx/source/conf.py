# -*- coding: utf-8 -*-

import sys

sys.path.append('../../../')

from shared.conf import *

tags.add('OLX')
product = 'OLX'
set_audience(OPENEDX, DEVELOPERS)

# General information about the project.
project = u'Open edX Open Learning XML Guide - Alpha Version'

redirects = {
    "*": "https://docs.openedx.org/en/latest/educators/navigation/olx.html",
}
