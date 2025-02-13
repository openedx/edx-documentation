# -*- coding: utf-8 -*-
import sys

sys.path.append('../../../')

from shared.conf import *

tags.add('Open_edX')
project = u'Building and Running an Open edX Course'

redirects = {
    "*": "https://docs.openedx.org/en/latest/educators/quickstarts/build_a_course.html",
}
