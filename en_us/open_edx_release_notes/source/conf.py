# -*- coding: utf-8 -*-
import sys

sys.path.append("../../../")

from shared.conf import *

project = "Open edX Release Notes"
set_audience(OPENEDX, DEVELOPERS)

# remove directory when content is first added to it, and add to index
exclude_patterns = ["links.rst"]

redirects = {
    "*": "https://docs.openedx.org/en/latest/community/release_notes/$source.html",
}
