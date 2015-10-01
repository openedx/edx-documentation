
import sys, os

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

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
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.intersphinx', 'sphinx.ext.coverage', 'sphinx.ext.pngmath', 'sphinx.ext.mathjax', 'sphinx.ext.ifconfig']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

if on_rtd:
    html_context = {
       "on_rtd" : on_rtd,
       "google_analytics_id" : '',
       "disqus_shortname" : 'edx',
       "github_base_account" : 'edx',
       "github_project" : 'edx-documentation',
    }

# General information about the project.

copyright = u'2015, edX'

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
    'openreleasenotes' : ('http://edx.readthedocs.org/projects/open-edx-release-notes/en/latest/', None)
}
