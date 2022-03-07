import sys

sys.path.append('../../../')

from shared.conf import *

project = u'Open edX Translation Processes'

set_audience(OPENEDX, DEVELOPERS)

exclude_patterns = ['links.rst']

def setup(app):
    app.add_config_value('product', '', True)
