###############################
edX Documentation (Deprecated)
###############################

Note: This repository is now deprecated. See `the associated DEPR ticket`_.

The edx-documentation repository contains source files for most of the
documentation for edx.org partners and learners.

* A new site, `docs.openedx.org`_, now hosts documentation for the Open edX community.
  See the rationale for the decision to move to a new site, as well as more
  on how the new site is organized, in `this decision document`_.

* API documentation that includes docstrings from code files is stored in the
  repository of that module.

* Documentation source files for Insights (deprecated) is in the edx-analytics-dashboard
  repository.

Documentation for developers, researchers, course staff, and students is
located in the language-specific subdirectories.

.. _docs.openedx.org: https://docs.openedx.org

.. _this decision document: https://docs.openedx.org/en/latest/documentors/decisions/0001-purpose-of-this-repo.html

.. _the associated DEPR ticket: https://github.com/openedx/edx-documentation/issues/2319

******************************
View Published Documentation
******************************

edX documentation is published through Read the Docs. Links to all published
documentation are available through `docs.edx.org`_.

.. _docs.edx.org: http://docs.edx.org

**********************************
About edX Documentation
**********************************

edX documentation is published from `RST`_ source files using `Sphinx`_.

.. _RST: http://docutils.sourceforge.net/rst.html
.. _Sphinx: http://sphinx-doc.org

======================
Testing
======================

You may first need to install `GraphViz <http://graphviz.org/>`_.
See the `Download Page <http://graphviz.org/download/>`_ for more instructions on how to install for your particular Operating System.

To run a test compilation, first install the prerequisites.

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
