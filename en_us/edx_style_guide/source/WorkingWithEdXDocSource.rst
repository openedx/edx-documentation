.. _Work with edX Documentation Source Files:

###########################################
Working with edX Documentation Source Files
###########################################

This section provides information about the tools used to create edX
documentation, and gives guidelines for translating or updating documentation
in the edx-documentation GitHub repository.

For information, see the following topics.

* :ref:`Documentation Tools and Processes`
* :ref:`Basic rst Formatting`
* :ref:`Documentation Translation Guidelines`
* :ref:`Documentation Translation Process`

See :ref:`ExampleRSTFile.rst<Anchor For ExampleRSTFile>` for examples of most of
the formatting used in edX documentation files.


.. _Documentation Tools and Processes:

*********************************
Documentation Tools and Processes
*********************************

For information about the tools that the edX Documentation team uses to create
documentation, see this wiki page:
https://openedx.atlassian.net/wiki/display/DOC/Documentation+Tools

Our documentation source files are .rst (restructuredText) files. In addition
to basic information that we provide about working with our source files, you
can find resources online, including the `restructuredText Primer <http
://sphinx-doc.org/rest.html>`_ and http://docutils.sourceforge.net/rst.html#user-documentation.

Our documentation source files reside in a GitHub repository: edx-documentation.
The folder structure within the repository is critical to our process and
should not be modified. Each .rst file results in one page of HTML output.

For information about the folder structure, and creating folder for a new
language, see :ref:`Documentation Translation Process`.


.. _Basic rst Formatting:

******************************
Basic Formatting In .rst Files
******************************

This section covers .rst formatting most commonly used in our source files.
For examples of the formatting explained here, refer to
:ref:`ExampleRSTFile.rst<Anchor For ExampleRSTFile>`.

* :ref:`Alignment`
* :ref:`Headings`
* :ref:`Lists`
* :ref:`Comments`
* :ref:`Special Tags`
* :ref:`Image Links`
* :ref:`Tables`
* :ref:`Anchors and Internal Links`
* :ref:`Code Examples`
* :ref:`Other Text Styles`


.. _Alignment:

=========
Alignment
=========

Formatting in .rst files relies on vertical alignment. Exact indents are
important. Text that is on the same line as an .rst tag and text that is
indented to the same level on following lines are interpreted as being part of
the same block.


.. _Headings:

========
Headings
========

The level of a heading is indicated by a series of characters above and below
the heading text.

* H1: pound symbols (#)
* H2: asterisk (*)
* H3: equals symbol (=)

For correct formatting, you must have the same number of the special tag
characters above and below the heading text, and heading text cannot extend
beyond the markers. If translated heading text is longer than the original
English text, make sure to extend the markers so that they are at least the
same length as translated text.

In addition to the first three levels of headings, up to three further levels
can be defined, but are rarely used. These heading levels 4, 5, and 6 have a
row of special characters only below the heading text. Like the top 3 heading
levels, heading text cannot extend beyond the markers. If a translated heading
is longer than the original, extend the markers to at least the same length as
the translated heading.

* H4: asterisk (*)
* H5: equals symbol (=)
* H6: tilde (~)

A heading level that is defined by two rows of a particular special character
above and below the heading text is interpreted as being distinct from a
heading level that uses that same character, but only below the heading text.


.. _Lists:

========
Lists
========

Create automatic numbered lists using the hash symbol
followed by a period, for each item in the numbered list. For example,

#. Select **Advanced Settings**.
#. Find the **Course Advertised Start Date** policy key.
#. Enter the value you want to display.

In some cases, for example if an automatic numbered list is interrupted by
multiple paragraphs or a nested list, you need to enter a number in place of
the hash symbol to restart the numbered list at the correct number.

Create bulleted lists using the asterisk symbol followed by a period, for each
item in the bulleted list. For example,

* Who is teaching the course?
* What university or college is the course affiliated with?
* What topics and concepts are covered in your course?
* Why should a learner enroll in your course?

For both numbered and bulleted lists, ensure that wrapped lines are indented
to align with first character of text in the first line of each list item.

.. note:: Nested lists are supported, but should be checked carefully in
   output to make sure numbering or indented levels are correct.


.. _Comments:

========
Comments
========

Lines beginning with 2 periods and a space indicate comments that are not
visible in output. For example:

``.. This is a comment.``


.. _Special Tags:

============
Special Tags
============

Special tagging for notes, warnings, tables, and code blocks is achieved using
lines beginning with 2 periods, followed by additional syntax.

``.. note::``

``.. warning::``

``.. important::``

``.. list-table::``

``.. code-block::``


.. _Image Links:

============
Image Links
============

Images are included in documentation using special tagging and providing the
path to the image file. Some image links might have additional specifications
such as height, width, or scale.

Alternative text for screen readers is required for each image. Provide text
that is useful to someone who might not be able to see the image. ::

	.. image:: ../../../shared/building_and_running_chapters/Images/about_page.png
           :alt: An image of the course summary page.


.. important:: When you translate existing content, make sure you do not
   change the filepath portion of the image reference. You should only
   translate the alternative text.

   If you replace any original source images with localized images, make sure
   the replacement image files have exactly the same filenames, and replace
   them in the same Images folder location, so that image links within the
   documentation are not broken.

.. _Tables:

======
Tables
======

Tables are tagged using ``.. list-table::``

Each table has the number of columns and their associated relative widths
indicated in a width tag.

For proper formatting, the asterisk indicating each row must align vertically,
and the hyphens indicating each column must also align. Empty cells must be
accounted for, so that each column in a row is always marked, even if there is
no content in the table cell. An example of an empty cell is the second column
in the first row of the following example. ::

  .. list-table::
     :widths: 25 25 50

   * - .. image:: ../../../shared/building_and_running_chapters/Images/AnnotationExample.png
          :width: 100
          :alt: Example annotation problem
     -
     - Annotation problems ask students to respond to questions about a
       specific block of text. The question appears above the text when the
       student hovers the mouse over the highlighted text so that students can
       think about the question as they read.
   * - .. image:: ../../../shared/building_and_running_chapters/Images/PollExample.png
          :width: 100
          :alt: Example poll
     - :ref:`Conditional Module`
     -  You can create a conditional module to control versions of content that
        groups of students see. For example, students who answer "Yes" to a
        poll question then see a different block of text from the students who
        answer "No" to that question.
   * - .. image:: ../../../shared/building_and_running_chapters/Images/JavaScriptInputExample.png
          :width: 100
          :alt: Example JavaScript problem
     - :ref:`Custom JavaScript`
     - Custom JavaScript display and grading problems (also called *custom
       JavaScript problems* or *JS input problems*) allow you to create a
       custom problem or tool that uses JavaScript and then add the problem or
       tool directly into Studio.

For additional examples of tables, see :ref:`the example .rst file<Anchor For ExampleRSTFile>`


.. _Anchors and Internal Links:

================================
Anchors and Internal Links
================================

Cross references use anchors that are placed above the heading for the target
section. Anchors are defined in lines beginning with 2 periods, followed by a
space, underscore and the anchor text, and ending with a colon.

For example, ``.. _Anchors and Internal Links:``

.. note:: Anchor text is never visible in output. It is replaced either by the
   actual text of the target heading, or by link text that you explicitly
   specify. Do not edit or translate anchor text; if you do, the links will break.


Cross references using text of the target topic heading
*******************************************************

For cross references that use the actual text of the target topic’s heading,
use ``:ref:`Anchor_text``` syntax. For example,
::

   Ensure that your course introduction video follows the same
   :ref:`Compression Specifications` and :ref:`Video Formats` guidelines as
   course content videos

where "Compression Specifications" and "Video Formats" are the text for
anchors that exist somewhere in the files that make up the guide. In output,
the actual text of the associated headings is substituted.

In some cases where a file defining a list of links is used, you might see
this alternative syntax for cross references, using an underscore after the
second grave accent character instead of ``:ref:``.  ::

  Ensure that your course introduction video follows the same
  `Compression Specifications`_ and `Video Formats`_ guidelines as
   course content videos


.. note:: For translations, make sure the substituted text reads well as part
   of the containing sentence. If necessary, add link text to use instead
   of the actual heading text.


Cross references using specified link text
**********************************************

For cross references that use specific link text rather than substituting the
actual target heading text, enter your own text followed by the anchor text in
angle brackets. For example,
::

  For more information, see :ref:`the introductory section on
  exercises<Exercises_introduction>`

where ``Exercises_introduction`` is the anchor text that exists somewhere in
the files that make up the guide, and "the introduction section on exercises"
is your preferred link text.

For additional examples of cross-reference formatting, see :ref:`the example
.rst file<Anchor For ExampleRSTFile>`.


.. _Code Examples:

==============
Code Examples
==============


Inline Code
***************

In inline text, any text can be formatting as code (monospace font) by
enclosing the selection within a pair of double "grave accent" characters. For
example, ``these words`` are formatted in a monospace font when the
documentation is output as PDF or HTML.


Code Blocks
***************

For larger blocks of code that are provided as examples in documentation, use
the code-block tag. Here is a code block. For examples, see
:ref:`ExampleRSTFile.rst<Anchor For ExampleRSTFile>`.

        .. code-block:: xml

          <problem>
              <annotationresponse>
                  <annotationinput>
                    <text>PLACEHOLDER: Text of annotation</text>
                      <comment>PLACEHOLDER: Text of question</comment>
                      <comment_prompt>PLACEHOLDER: Type your response below:</comment_prompt>
                      <tag_prompt>PLACEHOLDER: In your response to this question, which tag below
                      do you choose?</tag_prompt>
                    <options>
                      <option choice="incorrect">PLACEHOLDER: Incorrect answer (to make this
                      option a correct or partially correct answer, change choice="incorrect"
                      to choice="correct" or choice="partially-correct")</option>
                      <option choice="correct">PLACEHOLDER: Correct answer (to make this option
                      an incorrect or partially correct answer, change choice="correct" to
                      choice="incorrect" or choice="partially-correct")</option>
                      <option choice="partially-correct">PLACEHOLDER: Partially correct answer
                      (to make this option a correct or partially correct answer,
                      change choice="partially-correct" to choice="correct" or choice="incorrect")
                      </option>
                    </options>
                  </annotationinput>
              </annotationresponse>
              <solution>
                <p>PLACEHOLDER: Detailed explanation of solution</p>
              </solution>
            </problem>


.. _Other Text Styles:

=================
Other Text Styles
=================

Boldface is used for labels that are visible in the user interface. The UI
text is surrounded by double asterisks. For example, **bold**.

Italics are rarely used. Text surrounded by single asterisks is rendered in
*italics*.

Monospace text is used for ``code examples``. Text surrounded by double grave
accent characters (``) is rendered in monospace font. Within the pair of
double grave accents, further text formatting symbols is not recognized. For
more information, see :ref:`Code Examples`.

.. warning:: Make sure double quotation marks and apostrophes are straight (")
   or ('), not curly quotatation marks and apostrophes, which might be
   introduced when text is cut and pasted from other sources or editors.

