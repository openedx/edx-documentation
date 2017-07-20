# Shared configuration for edX docs.

import datetime
import os
import sys
import urllib

import edx_theme

# on_rtd is whether we are on readthedocs.io, this line of code grabbed from docs.readthedocs.io
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# OK, this is gross: I don't know of a way to find out what builder is running,
# so let's examine the command line, and take the word after -b.
the_builder = sys.argv[sys.argv.index("-b") + 1]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

master_doc = 'index'

# The suffix of source filenames.
source_suffix = '.rst'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

html_use_smartypants = True

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'edx_theme',
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.extlinks',
]

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

html_context = {}

if on_rtd:
    html_context["on_rtd"] = on_rtd
    html_context["google_analytics_id"] = ''
    html_context["disqus_shortname"] = 'edx'
    html_context["github_base_account"] = 'edx'
    html_context["github_project"] = 'edx-documentation'

html_theme = 'edx_theme'

html_theme_path = [edx_theme.get_html_theme_path()]

html_favicon = os.path.join(edx_theme.get_html_theme_path(), 'edx_theme', 'static', 'css', 'favicon.ico')

# Help and Feedback links.  These are customized for the category and audience
# of the book.  Add a line to the book's conf.py like this:
#
#   set_audience(PARTNER, COURSE_TEAMS)
#

# Categories
PARTNER = object()
OPENEDX = object()

# Audiences
COURSE_TEAMS = object()
LEARNERS = object()
RESEARCHERS = object()
DEVELOPERS = object()

HELP_LINKS = {
    (PARTNER, COURSE_TEAMS): {
        'help_url': None, #"https://partners.edx.org/forums/partner-forums",
        'help_link_text': None,
    },
    (PARTNER, LEARNERS): {
        'help_url': "https://support.edx.org",
        'help_link_text': "Contact Support",
    },
    (PARTNER, RESEARCHERS): {
        'help_url': "http://edx.readthedocs.io/projects/devdata/en/latest/front_matter/preface.html#resources-for-researchers",
        'help_link_text': "Get Help",
    },
    (PARTNER, DEVELOPERS): {
        'help_url': "https://open.edx.org/getting-help",
        'help_link_text': "Get Help",
    },
    (OPENEDX, LEARNERS): {
        'help_url': None,
        'help_link_text': None,
    },
    (OPENEDX, COURSE_TEAMS): {
        'help_url': "https://open.edx.org/getting-help",
        'help_link_text': "Get Help",
    },
    (OPENEDX, DEVELOPERS): {
        'help_url': "https://open.edx.org/getting-help",
        'help_link_text': "Get Help",
    },
}

# Defaults for the help links.
html_context.update({
    'help_url': None,
    'help_link_text': None,
    'feedback_form_link_text': "Give Doc Feedback",
})

def set_audience(category, audience):
    """Used from specific conf.py files to set the audience for a book."""
    help_data = HELP_LINKS.get((category, audience))
    if help_data:
        html_context.update(help_data)

FEEDBACK_FORM_FMT = "https://docs.google.com/forms/d/1T5QGnYb_QnQoMO7T_eatq02miPTY40WVe3cgGphNAdY/viewform?entry.1952574704&entry.241692674={pageid}"

def feedback_form_url(project, page):
    """Create a URL for feedback on a particular page in a project."""
    return FEEDBACK_FORM_FMT.format(pageid=urllib.quote("{}: {}".format(project, page)))

# We want the feedback_form_url function available in HTML templates, but it
# makes html_context un-JSON-able, so don't add it if we are doing JSON.
if the_builder != "json":
    html_context['feedback_form_url'] = feedback_form_url

# General information about the project.

copyright = '{year}, edX Inc.'.format(year=datetime.datetime.now().year)



# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'opencoursestaff' : ('http://edx.readthedocs.io/projects/open-edx-building-and-running-a-course/en/latest/', None),
    'data' : ('http://edx.readthedocs.io/projects/devdata/en/latest/', None),
    'partnercoursestaff': ('http://edx.readthedocs.io/projects/edx-partner-course-staff/en/latest/', None),
    'insights' : ('http://edx.readthedocs.io/projects/edx-insights/en/latest/', None),
    'xblockapi' : ('http://edx.readthedocs.io/projects/xblock/en/latest/', None),
    'xblocktutorial' : ('http://edx.readthedocs.io/projects/xblock-tutorial/en/latest/', None),
    'installation' : ('http://edx.readthedocs.io/projects/edx-installing-configuring-and-running/en/latest/', None),
    'olx' : ('http://edx.readthedocs.io/projects/edx-open-learning-xml/en/latest/', None),
    'learners' : ('http://edx.readthedocs.io/projects/edx-guide-for-students/en/latest/', None),
    'openlearners' : ('http://edx.readthedocs.io/projects/open-edx-learner-guide/en/latest/', None),
    'opendevelopers' : ('http://edx.readthedocs.io/projects/edx-developer-guide/en/latest/', None),
    'openplatformapi' : ('http://edx.readthedocs.io/projects/edx-platform-api/en/latest/', None),
    'opendataapi' : ('http://edx.readthedocs.io/projects/edx-data-analytics-api/en/latest/', None),
    'openreleasenotes' : ('http://edx.readthedocs.io/projects/open-edx-release-notes/en/latest/', None),
    'partnerreleasenotes': ('http://edx.readthedocs.io/projects/edx-release-notes/en/latest/', None),
    '2014releasenotes' : ('http://edx.readthedocs.io/projects/edx-2013-2014-release-notes/en/latest/', None)
}

extlinks = {
    # :jira:`TNL-4904` becomes: <a href='https://openedx.atlassian.net/browse/TNL-4904'>TNL-4904</a>
    'jira': ('https://openedx.atlassian.net/browse/%s', ''),
}
