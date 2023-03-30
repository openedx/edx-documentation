.. _Dropdown:

#####################
Dropdown Problem
#####################

.. note:: EdX offers full support for this problem type.

The dropdown problem type is a simple problem type that can be added to any
course. Dropdown problems include a question or prompt and
several answer options with a single correct answer. By adding hints, feedback, or both, you can give
learners guidance and help when they work on a problem.

.. contents::
  :local:
  :depth: 2

For more information about the simple problem types, see
:ref:`Working with Problem Components`.

**********
Overview
**********

In dropdown problems, learners select one answer from a list of answer options.
Unlike :ref:`multiple choice<Multiple Choice>` problems, where the answer
choices are always visible directly below the question, the answer options for
dropdown problems do not appear until the learner selects the dropdown arrow.

Dropdown problems can only have one correct answer per question, we recommend
adding a "Both B & C" answer where multiple selections could be correct.

================================
Example Dropdown Problem
================================

In the LMS, learners select a single answer option to complete a dropdown
problem. An example of a dropdown problem from the learner's perspective follows.

.. image:: ../../../shared/images/DropdownExample2.png
 :alt: A problem component that contains three answer choices.
 :width: 400

********************************
Adding a Dropdown Problem
********************************

You add dropdown problems in Studio by selecting the **Problem**
component. In the problem editor, select the **Dropdown** option. Fill in
the fields on this screen to create your problem.

.. image:: ../../../shared/images/problem_editor_dropdown.png
 :alt: An example dropdown problem in the problem editor with number
    indicators labeling the various features.
 :width: 800

Creating a dropdown problem is as simple as:

#. Editing the **Display Name**. Click the pen symbol to edit.
#. Filling in the **Question** field.
#. Filling in the **Explanation** field. When this is shown to learners is
   based on the selection in the **Show answer** panel on the right.
#. Filling in the Answer fields. Select the correct answer by ticking off
   the radio button. Additional answers can be added by clicking the 
   **Add answer** button. Answers can be deleted by clicking the trash can
   icon. Feedback can be provided for each answer. More information on
   feedback can be found in the following section.
#. Selecting and filling in any desired settings on the right.

If you have any questions on the specifics of using the simple editor, please check
out :ref:`Simple Editor` and :ref:`Problem Settings`.

.. _Use Feedback in a Dropdown Problem:

===========================================
Adding Feedback
===========================================

For an overview of feedback in problems, see :ref:`Adding Feedback and Hints to
a Problem`. You can add feedback for each of the answer options you provide in
the problem. Use the following guidelines when providing feedback.

* Use feedback for the incorrect answers to target common misconceptions and
  mistakes.

* Ensure feedback provides some guidance to the learner about how to arrive at
  the correct answer.

* Use feedback for the correct answer to reinforce why the answer is correct.
  Because learners are able to guess, ensure that feedback provides a reason
  why the answer is correct for learners who might have selected that answer by
  chance.

.. image:: ../../../shared/images/problem_editor_feedback_box_2.png
 :alt: An example of an expanded feedback section for dropdown problems showing 
    the 'is selected' feedback field.
 :width: 600

.. _Use Hints in a Dropdown Problem:

===========================================
Adding Hints
===========================================

You can add hints to a dropdown problem. For an overview of hints in problems, see
:ref:`Adding Feedback and Hints to a Problem`.

.. include:: ../../../shared/exercises_tools/Subsection_configure_hints.rst

****************************************************
Editing Dropdown Problems using the Advanced Editor
****************************************************

If the simple editor is not enough to meet your needs, you can switch over to the
advanced editor. In the setting panels on the right of the editor, click 
**Show advanced settings**, then scroll down and click 
**Switch to advanced editor**.

You can use the advanced editor to identify the elements of a checkbox problem
with OLX. For more information, see :ref:`Dropdown Problem XML`. To format equations,
you can use MathJax. For more information, see :ref:`MathJax in Studio`.

You can see the OLX for the example problem from the Overview section below.

.. code-block:: xml

  <problem>
    <optionresponse>
      <label>What type of data is age?</label>
      <optioninput options="('Nominal','Discrete','Continuous')"
      correct="Continuous"></optioninput>
    </optionresponse>
  </problem>

.. note:: You can begin work on the problem in the simple editor, and then
  switch to the advanced editor. However, after you save any advanced OLX
  changes you make in the advanced editor, you may not be able to cannot
  switch back to the simple editor.

=============================
Adding Feedback
=============================

In the advanced editor, you configure feedback with the following syntax.

.. code-block:: xml

  <option correct="False">Option Label
    <optionhint>Feedback for when a learner selects this incorrect answer.</optionhint>
  </option>

For example, the following problem has feedback for each answer.

.. code-block:: xml

  <problem>
    <optionresponse>
      <label>A/an ________ is an example of a vegetable.</label>
      <optioninput>
        <option correct="False">apple
          <optionhint>An apple is the fertilized ovary that comes from an
          apple tree and contains seeds classifying it as a fruit.</optionhint>
        </option>
        <option correct="False">pumpkin
          <optionhint>A pumpkin is the fertilized ovary of a squash plant and
          contains seeds classifying it as a fruit.</optionhint>
        </option>
        <option correct="True">potato
          <optionhint>A potato is an edible part of a plant in tuber form and
          is classified as a vegetable.</optionhint>
        </option>
        <option correct="False">tomato
          <optionhint>Many people mistakenly think a tomato is a vegetable.
          However, because a tomato is the fertilized ovary of a tomato plant
          and contains seeds it is classified as a fruit.</optionhint>
        </option>
      </optioninput>
    </optionresponse>
  </problem>

.. include:: ../../../shared/exercises_tools/Subsection_customizing_feedback_labels.rst

========================================
Adding Hints
========================================

.. include:: ../../../shared/exercises_tools/Subsection_configure_hints_advanced.rst

.. _Dropdown Problem XML:

**********************************
Dropdown Problem OLX Reference
**********************************

========
Template
========

.. code-block:: xml

  <problem>
    <optionresponse>
      <label>Question or prompt text</label>
      <description>Optional information about how to answer the question</description>
      <option correct="False">Option Label
        <optionhint>Feedback for when learner selects this answer.</optionhint>
      </option>
      <option correct="True">Option Label
        <optionhint>Feedback for when learner selects this answer.</optionhint>
      </option>
      <solution>
        <div class="detailed-solution">
          <p>Explanation or Solution Header</p>
          <p>Explanation or solution text</p>
        </div>
      </solution>
    </optionresponse>
    <demandhint>
      <hint>Hint 1</hint>
      <hint>Hint 2</hint>
      <hint>Hint 3</hint>
    </demandhint>
  </problem>

=========
Elements
=========

For dropdown problems, the ``<problem>`` element can include this
hierarchy of child elements.

.. code-block:: xml

  <optionresponse>
      <label>
      <description>
      <optioninput>
            <option>
                <optionhint>
      <solution>
  <demandhint>
      <hint>

In addition, standard HTML tags can be used to format text.

---------------------
``<optionresponse>``
---------------------

Required. Indicates that the problem is a dropdown problem.

^^^^^^^^^^^
Attributes
^^^^^^^^^^^

None.

^^^^^^^^^^^
Children
^^^^^^^^^^^

* ``<label>``
* ``<description>``
* ``<optioninput>``
* ``<solution>``

---------------------
``<label>``
---------------------

Required. Identifies the question or prompt. You can include HTML tags within
this element.

^^^^^^^^^^^
Attributes
^^^^^^^^^^^

None.

^^^^^^^^^^^
Children
^^^^^^^^^^^

None.

---------------------
``<description>``
---------------------

Optional. Provides clarifying information about how to answer the question. You
can include HTML tags within this element.

^^^^^^^^^^^
Attributes
^^^^^^^^^^^

None.

^^^^^^^^^^^
Children
^^^^^^^^^^^

None.

---------------------
``<optioninput>``
---------------------

Required. Designates an answer option.

^^^^^^^^^^^
Attributes
^^^^^^^^^^^

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``options``
     - Either this attribute or a set of ``<option>`` child elements for
       ``<optioninput>`` is required. Accepts a comma separated list of
       values in the following format.

       ``options="('Answer1','Answer2','Answer3')"``

   * - ``correct``
     - Used if the ``options`` attribute is set. Required. Indicates
       which of the answer options is correct.

^^^^^^^^^^^
Children
^^^^^^^^^^^

* ``<option>``
* ``<optionhint>``

---------------------
``<option>``
---------------------

Designates an answer option. Either a set of ``<option>`` child elements or the
``options`` attribute for ``<optioninput>`` is required.

^^^^^^^^^^^
Attributes
^^^^^^^^^^^

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``correct``
     - Required. Indicates whether the answer option is correct or incorrect.
       When set to ``"true"``, the choice is a correct answer. At least one
       required. When set to ``"false"``, the choice is an incorrect answer.

If the ``<option>`` element is used, ``<optionhint>`` is a child of
``<option>``.

---------------------
``<optionhint>``
---------------------

Optional. Specifies feedback for the answer.

^^^^^^^^^^^
Attributes
^^^^^^^^^^^

None.

^^^^^^^^^^^
Children
^^^^^^^^^^^

None.

---------------------
``<solution>``
---------------------

Optional. Identifies the explanation or solution for the problem, or for one of
the questions in a problem that contains more than one question.

This element contains an HTML division ``<div>``. The division contains one or
more paragraphs ``<p>`` of explanatory text.

---------------------
``<demandhint>``
---------------------

Optional. Specifies hints for the learner. For problems that include multiple
questions, the hints apply to the entire problem.

^^^^^^^^^^^
Attributes
^^^^^^^^^^^

None.

^^^^^^^^^^^
Children
^^^^^^^^^^^

``<hint>``

---------------------
``<hint>``
---------------------

Required. Specifies additional information that learners can access if needed.

^^^^^^^^^^^
Attributes
^^^^^^^^^^^

None.

^^^^^^^^^^^
Children
^^^^^^^^^^^

None.
