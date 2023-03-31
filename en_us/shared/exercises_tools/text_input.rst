.. _Text Input:

########################
Text Input Problem
########################

.. note:: EdX offers full support for this problem type.

The text input problem type is a simple problem type that can be added to any
course. At a minimum, text input problems include a question or prompt and a
response field for free form answer text. By adding hints, feedback, or both,
you can give learners guidance and help when they work on a problem.

.. contents::
  :local:
  :depth: 2

For more information about the simple problem types, see
:ref:`Working with Problem Components`.

**********
Overview
**********

In text input problems, learners enter text into a response field. The
response can include numbers, letters, and special characters such as
punctuation marks. Because the text that the learner enters must match the
instructor's specified answer exactly, including spelling and punctuation, edX
recommends that you specify more than one correct answer for text input
problems to allow for differences in capitalization and typographical errors.

=============================
Example Text Input Problem
=============================

In the LMS, learners enter a value into a response field to complete a text
input problem. An example of a completed text input problem follows.

.. image:: ../../../shared/images/TextInputExample.png
 :alt: A correctly answered text input problem shown in the LMS. The text
  entered by the learner exactly matches one of the acceptable answer options,
  which appear below the response along with the explanation.

******************************
Adding a Text Input Problem
******************************

You add text input problems in Studio by selecting the **Problem** component.
In the problem editor, select the **Text Input** option. Fill in the fields on
this screen to create your problem.

.. image:: ../../../shared/images/problem_editor_text_input.png
 :alt: An image of the problem editor in Studio. The various inputs and
    sections are labeled, and are referenced below.
 :width: 800

Creating a text input problem is as simple as:

#. Editing the **Display Name**. Click the pen symbol to edit.
#. Filling in the **Question** field.
#. Filling in the **Explanation** field. When this is shown to learners is
   based on the selection in the **Show answer** panel on the right.
#. Filling in the **Answer** fields. Select the correct answer(s) by ticking
   off the checkbox(es). Additional answers can be added by clicking the
   **Add answer** button. Answers can be deleted by clicking the trash can
   icon. Feedback can be provided for each answer. More information on feedback
   can be found in the following section.
#. Selecting and filling in any desired settings on the right.

If you have any questions on the specifics of using the simple editor, please check
out :ref:`Simple Editor` and :ref:`Problem Settings`.

=============================
Adding Feedback
=============================

For an overview of feedback in problems, see :ref:`Adding Feedback and Hints to
a Problem`. In text input problems, you can provide feedback for the correct
answer or for a specified incorrect answer. Use feedback on incorrect answers
as an opportunity to address common learner misconceptions. Feedback for text
input questions should also provide guidance to the learner on how to arrive at
the correct answer.

If you define multiple correct responses for the question, you can define
feedback for each response.

You can add answer-specific feedback for each answer in a text input problem.
You can access the feedback panel shown below by clicking the button to the
right of the answer text.

.. image:: ../../../shared/images/problem_editor_feedback_box.png
 :alt: an image of the feedback section. There are options for when the student's
    answer is selected.
 :width: 600

Simply enter your feedback message in this text field. It will display when the
learner submits this answer.

=============================
Adding Hints
=============================

You can add hints to a text input problem using the simple editor or the
advanced editor. For an overview of hints in problems, see
:ref:`Adding Feedback and Hints to a Problem`.

.. include:: ../../../shared/exercises_tools/Subsection_configure_hints.rst

.. _Editing Text Input Problems using the Advanced Editor:

*********************************************************************
Editing Text Input Problems using the Advanced Editor
*********************************************************************

If the simple editor is not enough to meet your needs, you can switch over to the
advanced editor. In the setting panels on the right of the editor, click 
**Show advanced settings**, then scroll down and click 
**Switch to advanced editor**.

You can use the advanced editor to identify the elements of a text input problem
with OLX. For more information, see :ref:`Text Input Problem XML`. To format
equations, you can use MathJax. For more information, see :ref:`MathJax in Studio`.

You can see the OLX for the example problem from the Overview section below.

.. code-block:: xml

  <problem>
  <stringresponse answer="Nanjing University" type="ci">
    <label>What was the first post-secondary school in China to allow both
     male and female students?</label>
    <description>Answer with a name from the modern period.</description>
    <additional_answer answer="National Central University"/>
    <additional_answer answer="Nanjing Higher Normal Institute"/>
    <additional_answer answer="Nanking University"/>
    <textline size="20"/>
    <solution>
      <div class="detailed-solution">
        <p>Explanation</p>
        <p>Nanjing University first admitted female students in 1920.</p>
      </div>
    </solution>
  </stringresponse>
  </problem>

.. note:: You can begin work on the problem in the simple editor, and then
  switch to the advanced editor. However, after you save any advanced OLX
  changes you make in the advanced editor, you may not be able to cannot
  switch back to the simple editor.

=============================
Adding Feedback
=============================

In the advanced editor, you configure answer feedback with the following syntax.

.. code-block:: xml

  <problem>
    <stringresponse answer="Correct Answer" type="ci">
      <label>Question text</label>
      <correcthint>Feedback for the correct answer</correcthint>
      <stringequalhint answer="Incorrect Answer">Hint for the incorrect answer</stringequalhint>
      <textline size="20"/>
    </stringresponse>
  </problem>

For example, the following problem has feedback for the correct answer and two
common incorrect answers.

.. code-block:: xml

  <problem>
    <stringresponse answer="Alaska" type="ci">
      <label>What is the largest state in the U.S. in terms of land area?</label>
      <correcthint>Alaska is the largest state in the U.S. in terms of not
      only land area, but also total area and water area. Alaska is 576,400
      square miles, more than double the land area of the second largest
      state, Texas.</correcthint>
      <stringequalhint answer="Texas">While many people think Texas is the
      largest state in terms of land area, it is actually the second
      largest and contains 261,797 square miles.</stringequalhint>
      <stringequalhint answer="California">California is the third largest
      state and contains 155,959 square miles.</stringequalhint>
      <textline size="20"/>
    </stringresponse>
  </problem>

.. include:: ../../../shared/exercises_tools/Subsection_customizing_feedback_labels.rst

=============================
Adding Hints
=============================

.. include:: ../../../shared/exercises_tools/Subsection_configure_hints_advanced.rst

==========================================================
Adding Text after the Response Field
==========================================================

You might want to include a word, phrase, or sentence after the response field
in a text input problem to help guide your learners or resolve ambiguity.

.. image:: ../../../shared/images/MC_trailing_text.png
 :alt: Text input problem with the word "Institute" after the response
    field.
 :width: 500

To do this, you use the advanced editor.

In the problem, locate the ``textline`` element. This element creates the
response field for the problem and is a child of the ``stringresponse``
element.

To add text after the response field, add the ``trailing_text`` attribute
together with the text that you want to use inside the ``textline`` element.  An example follows.

.. code-block:: xml

  <problem>
    <stringresponse answer="Ashmun" type="ci">
      <label>What Pennsylvania school was founded in 1854 to provide
        educational opportunities for African-Americans?</label>
      <textline size="20" trailing_text="Institute"/>
    </stringresponse>
  </problem>

==========================================================
Case Sensitivity and Text Input Problems
==========================================================

By default, text input problems do not require a case sensitive response. You
can change this default to require a case sensitive answer.

To make a text input response case sensitive, you use the advanced editor.

In the advanced editor, the ``stringresponse`` element has a ``type``
attribute. By default, the value for this attribute is set to ``ci``, for "case
insensitive". An example follows.

.. code-block:: xml

    <problem>
      <stringresponse answer="Paris" type="ci">
      .
      .
      .
      </stringresponse>
    </problem>

Learners who submit an answer of either "Paris" or "paris" are scored
as correct.

To make the response case sensitive, change the value of the ``type``
attribute to ``cs``.

.. code-block:: xml

    <problem>
      <stringresponse answer="Paris" type="cs">
      .
      .
      .
      </stringresponse>
    </problem>

Learners who submit an answer of "Paris" are scored as correct, but
learners who submit an answer of "PARIS" are scored as incorrect.

==========================================================
Response Field Length in Text Input Problems
==========================================================

You should preview the unit to ensure that the length of the response input
field accommodates the correct answer, and provides extra space for possible
incorrect answers.

If the default response field is not long enough, you can change it
using the advanced editor.

In the advanced editor, the ``textline`` element has a ``size`` attribute. By
default, the value for this attribute is set to ``20``. An example follows.

.. code-block:: xml

    <problem>
      <stringresponse answer="Democratic Republic of the Congo" type="ci">
        .
        .
        .
        <textline size="20"/>
      </stringresponse>
    </problem>

To change the response field length, change the value of the ``size``
attribute.

.. code-block:: xml

    <problem>
      <stringresponse answer="Democratic Republic of the Congo" type="ci">
        .
        .
        .
        <textline size="40" />
      </stringresponse>
    </problem>

===============================================================
Allowing Regular Expressions as Answers for Text Input Problems
===============================================================

You can configure a text input problem to allow a regular expression as an
answer. Allowing learners to answer with a regular expression can minimize the
number of distinct correct responses that you need to define for the problem:
if a learner responds with the correct answer formed as a plural instead of a
singular noun, or a verb in the past tense instead of the present tense, the
answer is marked as correct.

To do this, you use the advanced editor.

In the advanced editor, the ``stringresponse`` element has a ``type``
attribute. You can set the value for this attribute to ``regexp``, with or
without also including ``ci`` or ``cs`` for a case insensitive or case
sensitive answer. An example follows.

.. code-block:: xml

    <problem>
      <stringresponse answer="string pattern" type="regexp ci">
        .
        .
        .
      </stringresponse>
    </problem>

The regular expression that the learner enters must contain, in whole or in
part, the answer that you specify.

In this example, learners who submit an answer of "string pattern", "String
Patterns", "string patterned", or "STRING PATTERNING" are all scored as
correct, but learners who submit an answer of "Strings Pattern" or "string
patern" are scored as incorrect.

.. _Text Input Problem XML:

********************************
Text Input Problem XML Reference
********************************

==============
Template
==============

.. code-block:: xml

  <problem>
    <stringresponse answer="Correct answer 1" type="ci regexp">
      <label>Question text</label>
      <description>Optional tip</description>
      <correcthint>Provides feedback when learners submit the correct
       response.</correcthint>
      <additional_answer answer="Correct answer 2"/>
      <additional_answer answer="Correct answer 3"/>
      <stringequalhint answer="Incorrect answer 1">Provides feedback when
       learners submit the specified incorrect response.</stringequalhint>
      <stringequalhint answer="Incorrect answer 2">Provides feedback when
       learners submit the specified incorrect response.</stringequalhint>
      <textline size="20" />
    </stringresponse>
    <demandhint>
      <hint>The first text string to display when learners request a hint.</hint>
      <hint>The second text string to display when learners request a hint.</hint>
    </demandhint>
  </problem>

=========
Elements
=========

For text input problems, the ``<problem>`` element can include this
hierarchy of child elements.

.. code-block:: xml

  <stringresponse>
      <label>
      <description>
      <additional_answer>
      <correcthint>
      <stringequalhint>
      <textline>
      <solution>
  <demandhint>
      <hint>

In addition, standard HTML tags can be used to format text.

---------------------
``<stringresponse>``
---------------------

Required. Indicates that the problem is a text input problem.

^^^^^^^^^^
Attributes
^^^^^^^^^^

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``answer`` (required)
     - Specifies the correct answer.

       Note that if you do not also add the ``type`` attribute and set it to
       ``regexp``, the learner's answer must match the value for this
       attribute exactly.

   * - ``type`` (optional)
     - Specifies whether the problem requires a case sensitive response and
       if it allows regular expressions.

       * If ``type="ci"``, the problem is not case sensitive.
       * If ``type="cs"``, the problem is case sensitive.
       * If ``type="regexp"``, the problem allows regular expressions.

       You can also combine these values in a space separated list. For
       example, ``<stringresponse type="regexp cs">`` specifies that the
       problem allows regular expressions and is case sensitive.

^^^^^^^^^^
Children
^^^^^^^^^^

* ``<label>``
* ``<description>``
* ``<textline>``
* ``<additional_answer>``
* ``<correcthint>``
* ``<stringequalhint>``
* ``<solution>``

---------------------
``<label>``
---------------------

Required. Identifies the question or prompt. You can include HTML tags within
this element.

^^^^^^^^^^
Attributes
^^^^^^^^^^

None.

^^^^^^^^^^
Children
^^^^^^^^^^

None.

---------------------
``<description>``
---------------------

Optional. Provides clarifying information about how to answer the question. You
can include HTML tags within this element.

^^^^^^^^^^
Attributes
^^^^^^^^^^

None.

^^^^^^^^^^
Children
^^^^^^^^^^

None.

---------------------
``<textline>``
---------------------

Required. Creates a response field in the LMS where the learner enters a text
string.

^^^^^^^^^^
Attributes
^^^^^^^^^^

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``size``
     - Optional. Specifies the size, in characters, of the response field in
       the LMS. Defaults to 20.
   * - ``hidden``
     - Optional. If set to "true", learners cannot see the response field.
   * - ``correct_answer``
     - Optional. Lists the correct answer to the problem.
   * - ``trailing_text``
     - Optional. Specifies text to appear immediately after the response field.

.. reviewers, note that I could not get "correct_answer" to work ^^. The answer attribute of stringresponse is required and overrides whatever I put in here. Can this attribute be removed or marked as deprecated? - Alison 10 Aug

^^^^^^^^^^
Children
^^^^^^^^^^

None.

------------------------
``<additional_answer>``
------------------------

Optional. Specifies an additional correct answer for the problem. A problem can
contain an unlimited number of additional answers.

^^^^^^^^^^
Attributes
^^^^^^^^^^

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``answer``
     - Required. The text of the alternative correct answer.

^^^^^^^^^^
Children
^^^^^^^^^^

``<correcthint>``

------------------------
``<correcthint>``
------------------------

Optional. Specifies feedback to appear after the learner submits a correct
answer.

^^^^^^^^^^
Attributes
^^^^^^^^^^

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``label``
     - Optional. The text of the custom feedback label.

^^^^^^^^^^
Children
^^^^^^^^^^

None.

------------------------
``<stringequalhint>``
------------------------

Optional. Specifies feedback to appear after the learner submits an incorrect
answer.

^^^^^^^^^^
Attributes
^^^^^^^^^^

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``answer``
     - Required. The text of the incorrect answer.
   * - ``label``
     - Optional. The text of the custom feedback label.

^^^^^^^^^^
Children
^^^^^^^^^^

None.

------------------------
``<solution>``
------------------------

Optional. Identifies the explanation or solution for the problem, or for one of
the questions in a problem that contains more than one question.

This element contains an HTML division ``<div>``. The division contains one or
more paragraphs ``<p>`` of explanatory text.

------------------------
``<demandhint>``
------------------------

Optional. Specifies hints for the learner. For problems that include multiple
questions, the hints apply to the entire problem.

^^^^^^^^^^
Attributes
^^^^^^^^^^

None.

^^^^^^^^^^
Children
^^^^^^^^^^

``<hint>``

------------------------
``<hint>``
------------------------

Required. Specifies additional information that learners can access if needed.

^^^^^^^^^^
Attributes
^^^^^^^^^^

None.

^^^^^^^^^^
Children
^^^^^^^^^^

None.
