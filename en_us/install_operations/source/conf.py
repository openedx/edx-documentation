# -*- coding: utf-8 -*-
import sys

sys.path.append('../../../')

from shared.conf import *

# General information about the project.
project = u'Installing, Configuring, and Running the Open edX Platform'
set_audience(OPENEDX, DEVELOPERS)

# remove directory when content is first added to it, and add it to index
exclude_patterns = ['links.rst', 'configuration/configure_milestone_app.rst']

# overrides the navigation depth setting from shared/conf.py
html_theme_options['navigation_depth'] = 2

redirects = {
    "configuration/user_retire/index": "https://docs.openedx.org/projects/edx-platform/en/latest/references/docs/scripts/user_retirement/docs/index.html",
    "configuration/user_retire/driver_setup": "https://docs.openedx.org/projects/edx-platform/en/latest/references/docs/scripts/user_retirement/docs/driver_setup.html",
    "configuration/user_retire/implementation_overview": "https://docs.openedx.org/projects/edx-platform/en/latest/references/docs/scripts/user_retirement/docs/implementation_overview.html",
    "configuration/user_retire/service_setup": "https://docs.openedx.org/projects/edx-platform/en/latest/references/docs/scripts/user_retirement/docs/service_setup.html",
    "configuration/user_retire/special_cases": "https://docs.openedx.org/projects/edx-platform/en/latest/references/docs/scripts/user_retirement/docs/special_cases.html",
    "*": "https://docs.openedx.org/en/latest/site_ops/install_configure_run_guide/$source.html",
}
