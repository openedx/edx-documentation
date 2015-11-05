.. _Anchor For ExampleRSTFile:

#################
Example .rst File
#################

If you work with edX documentation source files, you might find this file
helpful as a reference. This file contains examples of .rst formatting.

Explanations and more context for each type of element is provided in
:ref:`Work with edX Documentation Source Files`.

***************
Heading Levels
***************

::

 #############
 Heading 1
 #############

 *************
 Heading 2
 *************

 ===========
 Heading 3
 ===========

 Heading 4
 ************

 Heading 5
 ===========

 Heading 6
 ~~~~~~~~~~~

***************************
Internal Table of Contents
***************************

.. contents::
  :local:
  :depth: 1

************************************************
Paragraph Text and Commented Text
************************************************

This is an example of regular text in paragraph form. There are no indents. As
a best practice, break lines at about 80 characters, so that each line has its
own line number for commenting in reviews.

.. warning:: Throughout text and code examples, make sure double quotation
   marks and apostrophes are straight (") or ('), not curly quotatation marks
   and apostrophes, which might be introduced when text is cut and pasted from
   other sources or editors.

Boldface is used for labels that are visible in the user interface. The UI
text is surrounded by double asterisks. For example, **bold**.

Italics are rarely used. Text surrounded by single asterisks is rendered in
*italics*.

Monospace text is used for ``code examples``. Text surrounded by double grave
accent characters is rendered in monospace font.

``.. comments can be added in a file by starting a line with 2 periods and a space.``

In English source files, look for comments addressed to translators from writers.

``.. Translators:  In this code example, do not translate such and such.``


***************************************
Ordered and Unordered Lists
***************************************

Use hash symbols for ordered lists.

::

#. Select **Advanced Settings**.
#. Find the **Course Advertised Start Date** policy key.
#. Enter the value you want to display.

.. note::
 Ordered lists usually use numerals. Nested ordered lists (ordered lists inside
 other ordered lists) use letters.

Use asterisks for unordered (bulleted) lists.

::

* Who is teaching the course?
* What university or college is the course affiliated with?
* What topics and concepts are covered in your course?
* Why should a learner enroll in your course?

=======================
Nested Lists or Content
=======================

You can include content including additional lists and code examples inside
lists.

Unordered List inside Ordered List
***************************************

To include an unordered list inside an ordered list, indent the unordered list
three spaces. The first bullet in the unordered list must be flush with the
text in the ordered list.

::

  #. Review your entry to verify that the key is accurate and that it is
     surrounded by quotation marks. If there is a list of keys, they must be
     comma separated.

     * In this example, the key for the Annotation Problem tool is the only
       value in the list.

     * In this example, the key for the Annotation Problem tool is added at
       the beginning of a list of other keys.

  #. Select **Save Changes**.

.. image:: /Images/Lists_UL_inside_OL.png
 :width: 500
 :alt: An unordered (bulleted) list inside an ordered (numbered) list.

Ordered List inside Unordered List
***************************************

To include an ordered list inside an unordered list, indent the ordered list
two spaces. The first number or letter of the ordered list must be flush with
the text in the unordered list.

::

  * Review your entry to verify that the key is accurate and that it is
    surrounded by quotation marks. If there is a list of keys, they must be comma
    separated.

    #. In this example, the key for the Annotation Problem tool is the only
       value in the list.

    #. In this example, the key for the Annotation Problem tool is added at the
       beginning of a list of other keys.

  * Select **Save Changes**.

.. There isn't a screen shot of the above example yet because these lists don't
.. render correctly locally, and searching for an example in the built docs
.. online was taking too much time.

Unordered List inside Unordered List
***************************************

To include an unordered list inside another unordered list, indent the second
unordered list two spaces. The first bullet of the second unordered list must
be flush with the text in the unordered list.

::

  * Review your entry to verify that the key is accurate and that it is
    surrounded by quotation marks. If there is a list of keys, they must be
    comma separated.

    #. In this example, the key for the Annotation Problem tool is the only
       value in the list.

    #. In this example, the key for the Annotation Problem tool is added at the
       beginning of a list of other keys.

  * Select **Save Changes**.

.. image:: /Images/Lists_UL_inside_UL.png
 :width: 500
 :alt: An ordered (numbered) list inside an unordered (bulleted) list.

Ordered List inside Ordered List
***************************************

To include another ordered list inside an ordered list, indent the second
ordered list three spaces. The second ordered list must be flush with the text
in the numbered list. The first ordered list uses numerals, and the second
uses letters.

::

  #. Review your entry to verify that the key is accurate and that it is
     surrounded by quotation marks. If there is a list of keys, they must be
     comma separated.

     #. In this example, the key for the Annotation Problem tool is the only
        value in the list.

     #. In this example, the key for the Annotation Problem tool is added at
        the beginning of a list of other keys.

  #. Select **Save Changes**.

.. There isn't a screen shot of the above example yet because these lists don't
.. render correctly locally, and searching for an example in the built docs
.. online was taking too much time.

Code, Images, and Other Content inside Lists
*********************************************

To include content such as code or an image inside a list, position the code or
image directive flush with the text in the list. That is, indent three spaces
for ordered lists and two spaces for unordered lists.

::

  #. In the ``lms.env.json`` and ``cms.env.json`` files, set the value of
     ``CERTIFICATES_HTML_VIEW`` within the ``FEATURES`` object  to ``true``.

     .. code-block:: bash

       "FEATURES": {
           ...
           'CERTIFICATES_HTML_VIEW': true,
           ...
       }

  #. Save the ``lms.env.json`` and ``cms.env.json`` files.


***************************************
Conditional Text
***************************************

To conditionalize a single paragraph, use either the ``only:: Partners`` or
the ``only:: Open_edX`` directive, and indent the paragraph under the
directive. You can add the conditional text as regular text or as a note.

Make sure to indent the paragraph under the directive.

::

  .. only:: Partners

   Data about course enrollment is available from edX Insights. You can access
   Insights from the Instructor Dashboard for your live course: after you select
   **Instructor**, follow the link in the banner at the top of each page. For
   more information, see `Using edX Insights`_.

  .. only:: Open_edX

      .. note::
        If you want to require an entrance exam for your course, you also create
        the exam in the course outline. Before you can create an exam, you must
        set your course to require an entrance exam in Studio. For more
        information, see :ref:`Require an Entrance Exam`.

To conditionalize more than a paragraph, use either the ``only:: Partners`` or
the ``only:: Open_edX`` directive, and then use an ``include::`` directive
indented under the only directive.

::

  .. only:: Open_edX

     .. include:: ../../../shared/building_and_running_chapters/running_course/Section_course_student.rst



*********************************
Notes and Warnings
*********************************

::

 .. note::
    This is note text. If note text runs over a line, make sure the lines wrap
    and are indented to the same level as the note tag. If formatting is
    incorrect, part of the note might not render in the HTML output.

    Notes can have more than one paragraph. Successive paragraphs must indent
    to the same level as the rest of the note.

.. note::
   This is note text. If note text runs over a line, make sure the lines wrap
   and are indented to the same level as the note tag. If formatting is
   incorrect, part of the note might not render in the HTML output.

   Notes can have more than one paragraph. Successive paragraphs must indent to
   the same level as the rest of the note.


::

  .. warning::
     Warnings are formatted in the same way as notes. In the same way, lines
     must be broken and indented under the warning tag.


.. warning::
   Warnings are formatted in the same way as notes. In the same way, lines must
   be broken and indented under the warning tag.


****************************
Cross-references
****************************

Cross-references use anchors that are placed above the heading for the target
section. Anchors are defined in lines beginning with 2 periods, followed by a
space, underscore and the anchor text, and ending with a colon.

For example, ``.. _Anchors and Internal Links:``

You can also see examples of anchors above the first three headings in this document.

Anchor text is never visible in output. It is always replaced either by the
text of the anchored topic heading, or by the specified link text.

=================================================
Example of cross-reference using anchor only
=================================================

For cross-references that use the actual text of the target topic’s heading,
use ``:ref:`Anchor_text``` syntax. For example,
::

   Ensure that your course introduction video follows the same
   :ref:`Compression Specifications` and :ref:`Video Formats` guidelines as
   course content videos

where "Compression Specifications" and "Video Formats" are the text for
anchors that exist somewhere in the files that make up the guide. In output,
the actual text of the associated headings is substituted.

=======================================================
Example of cross-reference using specified link text
=======================================================

::

  For more information, see :ref:`the introductory section on
  exercises<Exercises_introduction>`

where ``Exercises_introduction`` is the anchor text that exists somewhere in
the files that make up the guide, and "the introduction section on exercises"
is your preferred link text.


============================================
Cross references to external web pages
============================================

This example also includes specific link text before the URL.
::

  `Create a Problem <http://site.Create_Problem.html>`_

============================================
Cross references to edX101 demo course pages
============================================

::

  `Writing Exercises <https://edge.edx.org/courses/edX/edX101/How_to_Create_an
   _edX_Course/courseware/a45de3baa8a9468cbfb1a301fdcd7e86/d15cfeaff0af4dd7be4
   765cd0988d172/1>`_ has more in-depth discussion about problem types, and
   some general pedagogical considerations for adapting to the online format
   and a `Gallery of Response Types <https://edge.edx.org/accounts/login?next=
   /courses/edX/edX101/How_to_Create_an_edX_Course/courseware/a45de3baa8a9468c
   bfb1a301fdcd7e86/3ba055e760d04f389150a75edfecb844/1>`_


****************************
Image References
****************************

Image references look like this.
::

  .. image:: /Images/Course_Outline_LMS.png
     :width: 100
     :alt: A screen capture showing the elements of the course outline in the LMS.


Image links can include optional specifications such as height, width, or
scale. Alternative text for screen readers is required for each image. Provide
text that is useful to someone who might not be able to see the image.


.. _Examples of Tables:

************************************
Tables
************************************

Each example in this section shows the raw formatting for the table followed
by the table as it would render (if you are viewing this file as part of the
Style Guide).

======================================
Example of a table with an empty cell
======================================

The empty cell is the second column in the first row of this table.
::

  .. list-table::
     :widths: 25 25 50

   * - Annotation Problem
     -
     - Annotation problems ask students to respond to questions about a
       specific block of text. The question appears above the text when the
       student hovers the mouse over the highlighted text so that students can
       think about the question as they read.
   * - Example Poll
     - Conditional Module
     - You can create a conditional module to control versions of content that
        groups of students see. For example, students who answer "Yes" to a
        poll question then see a different block of text from the students who
        answer "No" to that question.
   * - Example JavaScript Problem
     - Custom JavaScript
     - Custom JavaScript display and grading problems (also called *custom
       JavaScript problems* or *JS Input problems*) allow you to create a
       custom problem or tool that uses JavaScript and then add the problem or
       tool directly into Studio.

.. list-table::
   :widths: 25 25 50

   * - Annotation Problem
     -
     - Annotation problems ask students to respond to questions about a
       specific block of text. The question appears above the text when the
       student hovers the mouse over the highlighted text so that students can
       think about the question as they read.
   * - Example Poll
     - Conditional Module
     -  You can create a conditional module to control versions of content that
        groups of students see. For example, students who answer "Yes" to a
        poll question then see a different block of text from the students who
        answer "No" to that question.
   * - Exampel JavaScript Problem
     - Custom JavaScript
     - Custom JavaScript display and grading problems (also called *custom
       JavaScript problems* or *JS Input problems*) allow you to create a
       custom problem or tool that uses JavaScript and then add the problem or
       tool directly into Studio.

====================================
Example of a table with a header row
====================================

::

  .. list-table::
     :widths: 15 15 70
     :header-rows: 1

     * - First Name
       - Last Name
       - Residence
     * - Elizabeth
       - Bennett
       - Longbourne
     * - Fitzwilliam
       - Darcy
       - Pemberley


.. list-table::
   :widths: 15 15 70
   :header-rows: 1

   * - First Name
     - Last Name
     - Residence
   * - Elizabeth
     - Bennett
     - Longbourne
   * - Fitzwilliam
     - Darcy
     - Pemberley


===============================================
Example of a table with a boldface first column
===============================================

::

  .. list-table::
     :widths: 15 15 70
     :stub-columns: 1

     * - First Name
       - Elizabeth
       - Fitzwilliam
     * - Last Name
       - Bennett
       - Darcy
     * - Residence
       - Longboure
       - Pemberley


.. list-table::
   :widths: 15 15 70
   :stub-columns: 1

   * - First Name
     - Elizabeth
     - Fitzwilliam
   * - Last Name
     - Bennett
     - Darcy
   * - Residence
     - Longboure
     - Pemberley

==============================================================
Example of a table with a cell that includes an unordered list
==============================================================

The blank lines before and after the unordered list are critical for the list
to render correctly.

::

  .. list-table::
     :widths: 15 15 60
     :header-rows: 1

     * - Field
       - Type
       - Details
     * - ``correct_map``
       - dict
       - For each problem ID value listed by ``answers``, provides:

         * ``correctness``: string; 'correct', 'incorrect'
         * ``hint``: string; Gives optional hint. Nulls allowed.
         * ``hintmode``: string; None, 'on_request', 'always'. Nulls allowed.
         * ``msg``: string; Gives extra message response.
         * ``npoints``: integer; Points awarded for this ``answer_id``. Nulls allowed.
         * ``queuestate``: dict; None when not queued, else ``{key:'', time:''}``
           where ``key`` is a secret string dump of a DateTime object in the form
           '%Y%m%d%H%M%S'. Nulls allowed.

     * - ``grade``
       - integer
       - Current grade value.
     * - ``max_grade``
       - integer
       - Maximum possible grade value.


.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``correct_map``
     - dict
     - For each problem ID value listed by ``answers``, provides:

       * ``correctness``: string; 'correct', 'incorrect'
       * ``hint``: string; Gives optional hint. Nulls allowed.
       * ``hintmode``: string; None, 'on_request', 'always'. Nulls allowed.
       * ``msg``: string; Gives extra message response.
       * ``npoints``: integer; Points awarded for this ``answer_id``. Nulls allowed.
       * ``queuestate``: dict; None when not queued, else ``{key:'', time:''}``
         where ``key`` is a secret string dump of a DateTime object in the form
         '%Y%m%d%H%M%S'. Nulls allowed.

   * - ``grade``
     - integer
     - Current grade value.
   * - ``max_grade``
     - integer
     - Maximum possible grade value.


*****************
Code Formatting
*****************

===========
Inline code
===========

In inline text, any text can be formatted as code (monospace font) by
enclosing the selection within a pair of double "grave accent" characters (`).
For example, ````these words```` are formatted in a monospace font when the
documentation is output as PDF or HTML.

===========
Code blocks
===========


To set text in a code block, end the previous paragaph with 2 colons, leave
one line before the intended code block, and make sure the code block is
indented beyond the first colon.
::

 For example, this is the introductory paragraph
 ::

  <p>and this is the code block following.</p>


Alternatively, use the code-block tag. Optionally, indicate the type of code
after the 2 colons in the tag, which results in the tags within the code block
being displayed in different colors.
::

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

