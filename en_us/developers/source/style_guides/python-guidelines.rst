..  _edx_python_guidelines:

######################
EdX Python Style Guide
######################

This section describes the requirements and conventions used to contribute
Python programming to the edX platform.

.. contents::
 :local:
 :depth: 2

**********
Principles
**********

Generally, do not edit files just to change the style.  But do aim for this
style with new or modified code.

See also :ref:`code_quality`.


==================================
Write a Good repr() for Each Class
==================================

.. FIXME: This was a section under "General Python" in the wiki. It's not
.. really syntax or organization. So I promoted it. Does this make sense on its
.. own here?

Each class should have a `__repr__() method
<https://docs.python.org/2/reference/datamodel.html#object.__repr__>`_ defined,
so that calling `repr()` on an instance of the class returns something
meaningful that distinguishes objects from each other to a human being. This is
useful for debugging purposes.


***********************
Syntax and Organization
***********************

Follow `PEP 8`_.

* 4-space indents (no tabs)
* Names like this:  modules_and_packages, functions_and_methods, local_variables, GLOBALS, CONSTANTS, MultiWordClasses
* Acronyms should count as one word:  RobustHtmlParser, not RobustHTMLParser
* Trailing commas are good: they prevent having to edit the last line in a list when adding a new last line.  You can use them in lists, dicts, function calls, etc.
* EXCEPT: we aren't (yet) limiting code lines to 79 characters.  Use 120 as a limit for code.  Please use 79 chars as a limit for docstring lines though, so that the text remains readable.

.. contents::
 :local:
 :depth: 2

===================
Breaking Long Lines
===================

Follow these guidelines:

* Try to refactor the code to not need such long lines.  This is often the best option, and is often overlooked for some reason.  More, shorter lines are good.

* If you need to break a function call over more than one line, put a newline after the open paren, and move the arguments to their own line.  DO NOT indent everything to where the open paren is.  This makes the code too indented, and makes different function calls near each other indented different amounts.

# NO NO NO!::

    results = my_object.some_method(arg1,    # this is very
                                    arg2,    # very ugly and makes
                                    arg3,    # the code squished over on the right.
                                    )

# YES::

    results = my_object.some_method(
        arg1,
        arg2,
        arg3,
    )

# OR::

    results = my_object.some_method(
        arg1, arg2, arg3
    )

Important points:

* Do not over-indent to make things line up with punctuation on the first line.
* Closing paren should be on a line by itself, indented the same as the first line.
* The first line ends with the open paren.

=============
Imports Order
=============

PEP8 recommends a most-general to most-specific import order, which means this order:

* Standard library imports
* Third Party Library imports
* Local imports

Alphabetize each group of imports, and use a single blank line to separate
groups.

.. note:: Most Open edX repositories use the `isort`_ library, which will
   automatically order imports to follow PEP8.

*******************************
Pylint Guidelines and Practices
*******************************

* For unused args, you can prefix the arguments with an underscore (_) to mark
  them as unused (as convention), and pylint will accept that.

* Adding a TODO in one place requires you to make a pylint fix in another (just
  to force us to clean up more code).

* No bare ``except`` clauses. ``except:`` should be ``except Exception:``, which
  will prevent it from catching system-exiting exceptions, which we probably
  should not be doing anyway. If we need to, we can catch ``BaseException``
  (There's no point in catching ``BaseException``, that includes the exceptions
  we didn't want to catch with ``except:`` in the first place.)  (ref:
  http://docs.python.org/2/library/exceptions.html#bltin-exceptions). Catching
  ``Exception``, however, will still generate a Pylint warning ("W0703: catching
  too general exception.")  If you still feel that catching ``Exception`` is
  justified, silence the pylint warning with a pragma: ``# pylint: disable=broad-
  except``.

* Although we try to be vigilant and resolve all quality violations, some
  Pylint violations are just too challenging to resolve, so we opt to ignore
  them via use of a pragma. A pragma tells Pylint to ignore the violation in
  the given line. An example is::

   self.assertEquals(msg, form._errors['course_id'][0])  # pylint: disable=protected-access

  The pragma starts with a ``#`` two spaces after the end of the line. We
  prefer that you use the full name of the error (``pylint: disable=unused-
  argument`` as opposed to ``pylint: disable=W0613``), so that it is more clear what
  you are disabling in the line.

===========================
Classes Versus Dictionaries
===========================

.. FIXME: Is this really a subsection of the Pylint section? Should it be
.. promoted or a part of a different section?

It's better to use a class or a ``namedtuple`` to pass around data that has a
fixed shape than to use a ``dict``. It makes it easier to debug (because there
is a fixed, named set of attributes), and it helps prevent accidental errors
of either setting new attributes into the dictionary (which might, for
instance, get serialized unexpectedly), or might be typos.

**********
Docstrings
**********

Follow `PEP 257`_.

* Write docstrings for all modules, classes, and functions.
* Always format docstrings using the multi-line convention, even if there's only
  one line of content (see below).
* Use three double-quotes for all docstrings.
* Start with a one-line summary. If you can't fit a summary onto one line, think
  harder, or refactor the code.
* Write in Sphinx-friendly prose style. Put double backquotes around code names
  (variables, parameters, methods, etc).

The preferred style is so-called "Google Style" with readable headers for
different sections, and all arguments and return values defined.

.. note:: There is one exception to the preferred style. REST APIs created
   using Django REST Framework (DRF) must use a hybrid format that is suitable
   both for DRF and ReadTheDocs. For more information see the
   `edX REST API Conventions`_.

For additional information see these references.

* `Google Python Style Guide`_
* `Example Google Style Python Docstrings`_ (from Sphinx)

Here's how you write documentation in a mostly "Google Style" manner::

    def func(arg1, arg2):
        """
        Summary line.

        Extended description of function.

        Arguments:
            arg1 (int): Description of arg1
            arg2 (str): Description of arg2

        Returns:
            bool: Description of return value
        """

.. note:: There are some exceptions:

  * The summary line is on the second line, including single-line comments
    (see below)
  * Use the full word "Arguments", although "Args" is also acceptable.

Most of our code is written using an older style::

    def calculate_grade(course, student):
        """
        Sum up the grade for a student in a particular course.

        Navigates the entire course, adding up the student's grades. Note that
        blah blah blah, and also beware that blah blah blah.

        `course` is an `EdxCourseThingy`. The student must be registered in the
        course, or a `NotRegistered` exception will be raised.

        `student` is an `EdxStudentThingy`.

        Returns a dict with two keys: `total` is a float, the student's total
        score, and `outof` is the maximum possible score.
        """

If you only have a single line in your docstring, first consider that this is
almost certainly not enough documentation, and write some more. But if you do
have just one line, format it in a similar way to a multi-line docstring::

    def foo(a, b):
        """
        Computes the foo of a and b.
        """

Not like this::

    def foo(a, b):
        """Computes the foo of a and b.""" # NO NO NO

We intentionally stray from `PEP 257`_ in this case.  The formatting
inconsistency between single and multi-line docstrings can result in merge
conflicts when upstream and downstream branches change the same docstring.  See
this `GitHub comment <https://github.com/openedx/edx-documentation/pull/999#issuecomment-215537490>`_
for more context.

**********
References
**********

* `PEP 8`_
* `PEP 257`_
* `Google Python Style Guide`_
* `Django Coding Style`_
* `The Hitchhiker’s Guide to Python`_
* `Pythonic Sensibilities`_

.. _Django Coding Style: https://docs.djangoproject.com/en/1.11/internals/contributing/writing-code/coding-style/
.. _edX REST API Conventions: https://openedx.atlassian.net/wiki/display/AC/edX+REST+API+Conventions#edXRESTAPIConventions-docstringsDocstringFormat
.. _Example Google Style Python Docstrings: http://www.sphinx-doc.org/en/stable/ext/example_google.html#example-google
.. _Google Python Style Guide: https://google.github.io/styleguide/pyguide.html?showone=Comments#Comments
.. _isort: https://github.com/timothycrosley/isort
.. _PEP 8: http://www.python.org/dev/peps/pep-0008/
.. _PEP 257: http://www.python.org/dev/peps/pep-0257/
.. _Pythonic Sensibilities: http://www.nilunder.com/blog/2013/08/03/pythonic-sensibilities/
.. _The Hitchhiker’s Guide to Python: https://python-guide.readthedocs.io/
