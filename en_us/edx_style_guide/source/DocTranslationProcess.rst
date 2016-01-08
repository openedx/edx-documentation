.. _Documentation Translation Process:

#########################################
Documentation Translation Process
#########################################

.. important:: Before you begin an edX documentation translation project,
   contact us at docs.edx.org to confirm the language or languages that you
   are translating into, and so that we can make sure the repository is ready
   for you to work with.

To work on translations of edX documentation, you should have a basic
understanding of reStructuredText and formatting in .rst files. For more
information, see :ref:`Work with edX Documentation Source Files`.

In addition, you or another person on the translation team should understand
GitHub repositories and the GitHub pull request process. For more information
about using GitHub, see https://help.github.com.

The basic process for translating edX documentation consists of these steps.

#. Use GitHub to clone the ``edx-documentation`` repository to a location on
   your local file system.

#. Locate the target language folder that we have set up for you. This is your
   working source directory. Language folders, including ``en_us``, exist one
   level below  ``edx-documentation``. Each language folder mirrors the
   ``en_us`` folder.

   .. note:: It is critical that you do not move or rename files within your
      target language folder as you work, otherwise you will break links and
      references.

#. Create a working branch or branches off master to make translation changes.
   Follow best practices for GitHub use. For information, see
   https://help.github.com.

   * Before making new branches, check that your local version of edx-
     documentation/master is up to date.

   * On your branch(es), make edits to the source files using your preferred
     text editor.

	* Save changes in the source files without renaming or moving the files.

	* Commit changes back to GitHub.

	* Create pull requests in GitHub for review purposes.

4. Build draft output and verify that everything renders as it should in both
   HTML and PDF formats. For information, see the "Verify Output" topic on this
   wiki page:

   https://openedx.atlassian.net/wiki/display/DOC/Instructions+for+Updating+Documentation


#. Notify the edX Documentation team when you have changes ready for review
   and testing. The team can also help you generate draft output for review
   and testing.

#. Make any revisions resulting from reviews and testing, then notify the edX
   Documentation team that the pull request is ready to merge into the repository.

#. The edX Documentation team merges translation pull requests into the
   repository.

#. The edX Documentation team updates and builds the readthedocs projects for the
   next release or a planned future release.


For information about working with edX Documentation source files, see
:ref:`Work with edX Documentation Source Files`.

For documentation translation guidelines, see :ref:`Documentation Translation
Guidelines`.


