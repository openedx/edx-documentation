###################
edX Documentation
###################

The edx-documentation repository contains source files for most of the
documentation for edX partners and the Open edX community.

* A new site, `docs.openedx.org`_, is currently being built. Before adding new
  documentation to this repo, consider if the documentation should be added, or
  moved, to the new site. See the rationale for this decision, as well as more
  on how the new site is organized, in `this decision document`_.

* API documentation that includes docstrings from code files is stored in the
  repository of that module.

* Documentation source files for Insights is in the edx-analytics-dashboard
  repository.

Documentation for developers, researchers, course staff, and students is
located in the language-specific subdirectories.

.. _docs.openedx.org: https://docs.openedx.org

.. _this decision document: https://docs.openedx.org/en/latest/documentors/decisions/0001-purpose-of-this-repo.html

******************************
View Published Documentation
******************************

edX documentation is published through Read the Docs. Links to all published
documentation are available through `docs.edx.org`_.

.. _docs.edx.org: http://docs.edx.org

******************************
Submit Documentation Issues
******************************

You may submit issues via the `edx-documentation GitHub Issues`_ system.

.. _edx-documentation GitHub Issues: https://github.com/openedx/edx-documentation/issues

**********************************
Contribute to edX Documentation
**********************************

You, the user community, can help update and revise edX documentation.

edX documentation is published from `RST`_ source files using `Sphinx`_.

.. _RST: http://docutils.sourceforge.net/rst.html
.. _Sphinx: http://sphinx-doc.org

To suggest a revision, fork the project, make changes in your fork, and submit
a pull request back to the original project: this is known as the `GitHub
Flow`_.

.. _GitHub Flow: https://github.com/blog/1557-github-flow-in-the-browser

All pull requests need approval from project maintainers, who will look over and
review your contributions.

============================================
Supplying Information with a Pull Request
============================================

The edX documentation team created a template that is automatically added to pull requests. You are strongly encouraged to use this template.

======================
Testing a Contribution
======================

Before submitting a pull request, it is recommended you run the test suite on
your contribution to ensure it can be compiled into HTML format without errors.

You may first need to install `GraphViz <http://graphviz.org/>`_.
See the `Download Page <http://graphviz.org/download/>`_ for more instructions on how to install for your particular Operating System.

To run a test compilation of a contribution, first install the prerequisites.

.. code::

  make requirements

Then run the tests.

.. code::

  ./run_tests.sh

Additionally, you can run tests for a single project. For example, to build an
HTML version of the *Installing, Configuring, and Running the Open edX
Platform* guide, you run this test.

.. code::

  ./run_tests.sh en_us/install_operations/

A convenience script is provided to help you develop new documentation. To use
it you must first install the optional tools, and then run the script.

.. code::

  pip install -r shared/tools.txt
  ./develop.sh en_us/install_operations/

It will output a line of text that looks like this.

::

  Serving on http://127.0.0.1:9090

You can copy this URL into a web browser to see the HTML output for your
project.

The command starts an HTTP server that renders the HTML for the project. This
HTTP server also monitors the project and detects any changes. When you save a
change to a file, the server rebuilds the HTML and refreshes your browser
automatically. In this way you can rapidly see how changes you make will be
rendered as HTML.
