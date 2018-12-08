# Shared configuration for edX docs.

import sys, os, urllib

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
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
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.pngmath',
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
    (PARTNER, COURSE_TEAMS): None, #"https://partners.edx.org/forums/partner-forums",
    (PARTNER, LEARNERS): None, #"https://support.edx.org",
    (PARTNER, RESEARCHERS): "http://edx.readthedocs.org/projects/devdata/en/latest/front_matter/preface.html#resources-for-researchers",
    (PARTNER, DEVELOPERS): "https://open.edx.org/resources/e-mail-lists",
    (OPENEDX, COURSE_TEAMS): "https://open.edx.org/resources/e-mail-lists",
    (OPENEDX, DEVELOPERS): "https://open.edx.org/resources/e-mail-lists",
}

html_context['help_url'] = None

def set_audience(category, audience):
    """Used from specific conf.py files to set the audience for a book."""
    html_context['help_url'] = HELP_LINKS.get((category, audience))

FEEDBACK_FORM_FMT = "https://docs.google.com/forms/d/1T5QGnYb_QnQoMO7T_eatq02miPTY40WVe3cgGphNAdY/viewform?entry.1952574704&entry.241692674={pageid}"

def feedback_form_url(project, page):
    """Create a URL for feedback on a particular page in a project."""
    return FEEDBACK_FORM_FMT.format(pageid=urllib.quote("{}: {}".format(project, page)))

# We want the feedback_form_url function available in HTML templates, but it
# makes html_context un-JSON-able, so don't add it if we are doing JSON.
if the_builder != "json":
    html_context['feedback_form_url'] = feedback_form_url

# General information about the project.

copyright = u'2016, edX Inc.'



# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'opencoursestaff' : ('http://edx.readthedocs.org/projects/open-edx-building-and-running-a-course/en/latest/', None),
    'data' : ('http://edx.readthedocs.org/projects/devdata/en/latest/', None),
    'partnercoursestaff': ('http://edx.readthedocs.org/projects/edx-partner-course-staff/en/latest/', None),
    'insights' : ('http://edx.readthedocs.org/projects/edx-insights/en/latest/', None),
    'xblockapi' : ('http://edx.readthedocs.org/projects/xblock/en/latest/', None),
    'xblocktutorial' : ('http://edx.readthedocs.org/projects/xblock-tutorial/en/latest/', None),
    'installation' : ('http://edx.readthedocs.org/projects/edx-installing-configuring-and-running/en/latest/', None),
    'olx' : ('http://edx.readthedocs.org/projects/edx-open-learning-xml/en/latest/', None),
    'learners' : ('http://edx.readthedocs.org/projects/edx-guide-for-students/en/latest/', None),
    'openlearners' : ('http://edx.readthedocs.org/projects/open-edx-learner-guide/en/latest/', None),
    'opendevelopers' : ('http://edx.readthedocs.org/projects/edx-developer-guide/en/latest/', None),
    'openplatformapi' : ('http://edx.readthedocs.org/projects/edx-platform-api/en/latest/', None),
    'opendataapi' : ('http://edx.readthedocs.org/projects/edx-data-analytics-api/en/latest/', None),
    'openreleasenotes' : ('http://edx.readthedocs.org/projects/open-edx-release-notes/en/latest/', None),
    'partnerreleasenotes': ('http://edx.readthedocs.org/projects/edx-release-notes/en/latest/', None),
    '2014releasenotes' : ('http://edx.readthedocs.org/projects/edx-2013-2014-release-notes/en/latest/', None)
}

extlinks = {
    # :jira:`TNL-4904` becomes: <a href='https://openedx.atlassian.net/browse/TNL-4904'>TNL-4904</a>
    'jira': ('https://openedx.atlassian.net/browse/%s', ''),
}
