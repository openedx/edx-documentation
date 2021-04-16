# -*- coding: utf-8 -*-
import sys

sys.path.append('../../../')

from shared.conf import *

# General information about the project.
project = u'Installing, Configuring, and Running the Open edX Platform: Lilac Release'
set_audience(OPENEDX, DEVELOPERS)

# remove directory when content is first added to it, and add it to index
exclude_patterns = ['links.rst', 'configuration/configure_milestone_app.rst']

# overrides the navigation depth setting from shared/conf.py
html_theme_options['navigation_depth'] = 2
