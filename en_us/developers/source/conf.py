# -*- coding: utf-8 -*-
import sys

sys.path.append('../../../')

from shared.conf import *

project = u'Open edX Developer\'s Guide'
set_audience(OPENEDX, DEVELOPERS)

exclude_patterns = ['i18n.rst', 'i18n_translators_guide.rst']

redirects = {
    "*": "https://docs.openedx.org/en/latest/developers/references/developer_guide/$source.html",
}
