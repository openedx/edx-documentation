.. _code_quality:

************
Code Quality
************

We use a variety of tools to check for errors and vulerabilities, and to enforce
a coding standard and coding style.

To check the quality of your pull request, go to the top level of the edx-
platform codebase and run the following command. ::

    $ paver run_quality

Most other repos use the command ::

    $ make quality

The following topics provide additional details on the tools that we use.

.. contents::
   :depth: 1
   :local:

Clean Code
==========

Here are the primary tools we use to keep our code clean.

* We use the `pep8`_ tool to follow `PEP-8`_ guidelines.
* We use `pylint`_ for static analysis and to uncover trouble spots in our
  code.

Our codebase is far from perfect, but the goal is to steadily improve its
quality over time. To do this, we wrote a pypi package called `diff-cover`_,
which includes the tool diff-quality. The diff-quality tool reports on quality
violations only on lines that have changed in a pull request. Using this tool,
we can ensure that pull requests do not introduce new quality violations, and
also clean up existing violations in the process of introducing other changes.

To run diff-quality along with our other quality based tools, go to the top
level of the edx-platform codebase and run the following command. ::

    $ paver run_quality

You can also use the ``paver run_pep8`` and ``paver run_pylint`` commands to
run only pep8 or pylint.

This will print a report of the quality violations that your branch has made.

Although we try to be vigilant in resolving all quality violations, some
Pylint violations are too challenging to resolve, so we opt to ignore them via
use of a pragma. A pragma tells Pylint to ignore the violation in the given
line. An example is::

    self.assertEquals(msg, form._errors['course_id'][0])  # pylint: disable=protected-access

The pragma starts with a ``#`` two spaces after the end of the line. We prefer
that you use the full name of the error (``pylint: disable=unused-argument``
as opposed to ``pylint: disable=W0613``), to make more clear what you are
disabling in the line.

.. _PEP-8: http://legacy.python.org/dev/peps/pep-0008/
.. _pep8: https://pypi.python.org/pypi/pep8
.. _coverage.py: https://pypi.python.org/pypi/coverage
.. _pylint: http://pylint.org/
.. _diff-cover: https://github.com/Bachmann1234/diff-cover

Safe Code
=========

To keep our code safe from Cross Site Scripting (XSS) vulnerabilities,
the XSS Linter is also run as part of ``paver run_quality``.

To run the XSS Linter against your current branch, run the following
command.

.. code-block:: bash

   paver run_xsscommitlint

For more options for running the XSS Linter, or instructions for
fixing violations, see :ref:`XSS Linter`.
