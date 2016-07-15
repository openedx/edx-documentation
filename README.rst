###################
EdX Documentation
###################

The edx-documentation repository contains source files for most of the
documentation for edX partners and the Open edX community. This repository is
managed by the edX Documentation team.

* API documentation that includes docstrings from code files is stored in the
  repository of that module.

* Documentation source files for Insights is in the edx-analytics-dashboard
  repository.

Documentation for developers, researchers, course staff, and students is
located in the language-specific subdirectories.

******************************
View Published Documentation
******************************

EdX documentation is published through Read the Docs. Links to all published
documentation are available through `docs.edx.org`_.

.. _docs.edx.org: http://docs.edx.org

******************************
Submit Documentation Issues
******************************

We welcome input from the community on any documentation issues.  You can
submit issues to the Documentation project in the `Open edX JIRA board`_.

.. _Open edX JIRA board: https://openedx.atlassian.net

You can also email docs@edx.org.

**********************************
Contribute to edX Documentation
**********************************

You, the user community, can help update and revise edX documentation.

EdX documentation is published from `RST`_ source files using `Sphinx`_.

.. _RST: http://docutils.sourceforge.net/rst.html
.. _Sphinx: http://sphinx-doc.org

To suggest a revision, fork the project, make changes in your fork, and submit
a pull request back to the original project: this is known as the `GitHub
Flow`_.

.. _GitHub Flow: https://github.com/blog/1557-github-flow-in-the-browser

All pull requests need approval from edX. For more information, contact edX at
docs@edx.org.

============================================
Supplying Information with a Pull Request
============================================

The edX documentation team created a template that is automatically added to pull requests. You are strongly encouraged to use this template.

======================
Testing a Contribution
======================

Before submitting a pull request, it is recommended you run the test suite on
your contribution to ensure it can be compiled into HTML format without errors.

To run a test compilation of a contribution, first install the prerequisites.

.. code::

  pip install -r shared/travis_requirements.txt

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

================================
Adding Release Notes
================================

The edX documentation team compiles release notes to describe changes to the
Open edX platform and how they affect learners, course teams, installers, and
other end-users. You can contribute release notes for upcoming releases.

Release notes are set up as a collection of ReStructured Text (.rst) files.
There is one file for each of several categories:

* Analytics
* Documentation
* LMS
* Mobile
* Open edX
* Studio
* The edx.org website

To add a release notes item, you determine the category for the item, run the
``utilities/add-upcoming-release-notes-file.sh`` shell script to determine or
create the .rst file for that category, and then enter the item in the .rst
file. You then submit a pull request for your .rst file. The documentation team
copy edits the file and includes it in the index file for the week's release
notes.

Full instructions follow.

Add a Release Notes Item
************************

To add a release notes item, follow these steps.

1. Change to the edx-documentation directory.

2. Create a new branch.

3. On your branch, run either of the following commands.

   .. code-block:: shell

     $ ./utilities/add-upcoming-release-notes-file.sh

     $ make release-note

4. At the prompt, enter the category that you want, and then press Enter.

   The script returns a message with the name and location of the .rst file
   where you will add your item. If the file does not already exist, the script
   creates the file. The script does not overwrite an existing release notes
   source file for the next upcoming release.

   For example, the file might have the following name.

   ``/edx-documentation/en_us/release_notes/source/2016/lms/lms_2016-07-25.rst``

5. In a text editor, open the file and follow the inline instructions to add
   your note.

6. Save, commit, and push your changes.

7. Open a PR for your branch and resolve any merge conflicts.

   The doc team is tagged automatically when you open your PR and will complete
   any necessary copy editing. The doc team will also include the new files in
   the release notes index.
