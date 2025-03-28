# Shared configuration for edX docs.

import datetime
import os
import sys
import urllib
from pathlib import Path

# What release line is this?  Use "master" for master, and the release name
# on release branches.  Zebrawood should have "zebrawood".
release_line = "master"

# The slug that is used by ReadTheDocs for this version of the projects.
project_version = "latest" if (release_line == "master") else f"open-release-{release_line}.master"

# on_rtd is whether we are on readthedocs.io, this line of code grabbed from docs.readthedocs.io
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# OK, this is gross: I don't know of a way to find out what builder is running,
# so let's examine the command line, and take the word after -b.
try:
    the_builder = sys.argv[sys.argv.index("-b") + 1]
except ValueError:
    the_builder = None

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

master_doc = 'index'

# The suffix of source filenames.
source_suffix = '.rst'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.extlinks',
    'sphinx.ext.graphviz',
    'sphinx_reredirects',
    'notfound.extension',
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

html_theme = 'sphinx_book_theme'
path_to_docs = '/'.join(Path.cwd().parts[-3:])

# html_theme_path = []
html_theme_options = {
    "repository_url": "https://github.com/openedx/edx-documentation",
    "repository_branch": "master",
    "path_to_docs": path_to_docs,
    "home_page_in_toc": True,
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "navigation_with_keys": False,
    # Please don't change unless you know what you're doing.
    "extra_footer": """
        <a rel="license" href="https://creativecommons.org/licenses/by-sa/4.0/">
            <img
                alt="Creative Commons License"
                style="border-width:0"
                src="https://i.creativecommons.org/l/by-sa/4.0/80x15.png"/>
        </a>
        <br>
        These works by
            <a
                xmlns:cc="https://creativecommons.org/ns#"
                href="https://openedx.org"
                property="cc:attributionName"
                rel="cc:attributionURL"
            >The Axim Collaborative</a>
        are licensed under a
            <a
                rel="license"
                href="https://creativecommons.org/licenses/by-sa/4.0/"
            >Creative Commons Attribution-ShareAlike 4.0 International License</a>.
    """
}
html_theme_options['navigation_depth'] = 3

html_logo = "https://logos.openedx.org/open-edx-logo-color.png"
html_favicon = "https://logos.openedx.org/open-edx-favicon.ico"

# Help and Feedback links.  These are customized for the category and audience
# of the book.  Add a line to the book's conf.py like this:
#
#   set_audience(PARTNER, COURSE_TEAMS)
#

# Categories
PARTNER = object()
OPENEDX = object()
EDX = object()

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
        'help_url': "https://openedx.org/community/connect/",
        'help_link_text': "Get Help",
    },
    (OPENEDX, LEARNERS): {
        'help_url': None,
        'help_link_text': None,
    },
    (OPENEDX, COURSE_TEAMS): {
        'help_url': "https://openedx.org/community/connect/",
        'help_link_text': "Get Help",
    },
    (OPENEDX, DEVELOPERS): {
        'help_url': "https://openedx.org/community/connect/",
        'help_link_text': "Get Help",
    },
    (EDX, LEARNERS): {
        'help_url': "https://help.edx.org",
        'help_link_text': "Get Help",
    }
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

# General information about the project.

print(html_context)

copyright = '{year}, The Axim Collaborative'.format(year=datetime.datetime.now().year)

# Intersphinx manages the connections between books.
# Normally the references in a book are downloaded from readthedocs.  But you
# can also provide a local file to look in.  It's easier to fix broken
# references betweeen books if you can do a local build and use the local
# reference files.  These helper functions are for both reducing the repetition
# in the mapping dictionary, and for optionally specifying a local file to look
# in if it exists.
#
# We often use the same directory to build two books (edX vs Open edX).  In
# those cases, only use ism_location for one book, not both, or we'll be
# looking for A's references in an index built for B.
#
# openedx_rtd_url is for books that are branched and built for specific Open
# edX releases.  edx_rtd_url is for books that are not.

def edx_rtd_url(slug):
    """Make a RTD URL for a book that doesn't branch for each release."""
    return f"https://edx.readthedocs.io/projects/{slug}/en/latest/"

def openedx_rtd_url(slug):
    """Make a RTD URL for a book that branches for each release."""
    return f"https://edx.readthedocs.io/projects/{slug}/en/{project_version}/"

def ism_location(dir_name):
    """Calculate the intersphinx_mapping location to use for a book.

    `dir_name` is the directory name under edx-documentation/en_us for the book.

    """
    objects_inv = f"../../{dir_name}/build/html/objects.inv"
    if os.path.exists(objects_inv):
        return (objects_inv, None)
    else:
        return None

intersphinx_mapping = {
    "opencoursestaff" : ("https://docs.openedx.org/en/latest/", None),
    "data" : (edx_rtd_url("devdata"), ism_location("data")),
    "partnercoursestaff": (edx_rtd_url("edx-partner-course-staff"), ism_location("course_authors")),
    "insights" : (edx_rtd_url("edx-insights"), None),
    "xblockapi" : ("https://docs.openedx.org/projects/xblock/en/latest/", None),
    "xblocktutorial" : ("https://docs.openedx.org/projects/xblock/en/latest/", None),
    "installation" : ("https://docs.openedx.org/en/latest/", None),
    "olx" : ("https://docs.openedx.org/en/latest/", None),
    "learners" : ("", ism_location("students_redirect")),
    "openlearners" : (openedx_rtd_url("open-edx-learner-guide"), ism_location("edx_students")),
    "opendevelopers" : ("https://docs.openedx.org/en/latest/", None),
    "opendataapi" : (edx_rtd_url("edx-data-analytics-api"), None),
    "openreleasenotes" : ("https://docs.openedx.org/en/latest/", None),

}

extlinks = {
    # :jira:`TNL-4904` becomes: <a href='https://openedx.atlassian.net/browse/TNL-4904'>TNL-4904</a>
    'jira': ('https://openedx.atlassian.net/browse/%s', 'Jira Issue %s'),
}

# sphinx-notfound-page
# https://github.com/readthedocs/sphinx-notfound-page
notfound_context = {
    "title": "Page Not Found",
    "body": """
<h1>Page Not Found</h1>

<p>Sorry, we couldn't find that page. Try using the search box or visiting <a href="https://docs.openedx.org/en/latest/">docs.openedx.org</a>, our new documentation site.</p>
""",
}