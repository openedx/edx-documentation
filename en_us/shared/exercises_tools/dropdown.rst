.. _Dropdown:

#####################
Dropdown Problem
#####################

.. note:: EdX offers full support for this problem type.

The dropdown problem type is a core problem type that can be added to any
course. At a minimum, dropdown problems include a question or prompt and
several answer options. By adding hints, feedback, or both, you can give
learners guidance and help when they work on a problem.

.. contents::
  :local:
  :depth: 2

For more information about the core problem types, see
:ref:`Working with Problem Components`.

**********
Overview
**********

In dropdown problems, learners select one option from a list of answer options.
Unlike :ref:`multiple choice<Multiple Choice>` problems, where the answer
choices are always visible directly below the question, the answer options for
dropdown problems do not appear until the learner selects the dropdown arrow.

================================
Example Dropdown Problem
================================

In the LMS, learners select a single answer option to complete a dropdown
problem. An example of a completed dropdown problem follows.

.. image:: ../../../shared/images/DropdownExample.png
 :alt: A problem component that contains a series of three dropdown problems.
     The questions have been answered, and two are marked incorrect and one
     correct.
 :width: 600

In this example, a single problem component contains multiple questions, all of
them using the dropdown problem type. To add the example illustrated
above, you enter the following text and Markdown formatting in the simple
editor in Studio.

::

  >>What type of data is age?<<
  [[Nominal, Discrete, (Continuous)]]
  ---
  >>What type of data is age, when rounded to the nearest year?<<
  [[
  Nominal
  (Discrete)
  Continuous
  ]]
  ---
  >>What type of data is life stage (for example, infant, child, or adult)?<<
  [[(Nominal), Discrete, Continuous]]

.. note:: You separate :ref:`multiple questions<Multiple Problems in
  One Component>` in a problem component with three hyphen (``---``)
  characters. You can separate the answer options with either comma (``,``)
  characters or new lines.

The OLX markup for this example problem follows.

.. code-block:: xml

  <problem>
    <optionresponse>
      <label>What type of data is age?</label>
      <optioninput options="('Nominal','Discrete','Continuous')"
       correct="Continuous"></optioninput>
    </optionresponse>
    <optionresponse>
      <label>What type of data is age, when rounded to the nearest year?</label>
      <optioninput options="('Nominal','Discrete','Continuous')"
       correct="Discrete"></optioninput>
      </optionresponse>
    <optionresponse>
      <label>What type of data is life stage (for example, infant, child, or adult)?</label>
      <optioninput options="('Nominal','Discrete','Continuous')"
       correct="Nominal"></optioninput>
    </optionresponse>
  </problem>

============================================
Analyzing Performance on Dropdown Problems
============================================

For the dropdown problems in your course, you can use edX Insights to review
aggregated learner performance data and examine submitted answers. For
more information, see :ref:`insights:Using edX Insights`.

********************************
Adding a Dropdown Problem
********************************

You add dropdown problems in Studio by selecting the **Problem**
component type and then using either the simple editor or the advanced editor
to specify the prompt and the answer options.

.. contents::
  :local:
  :depth: 1

.. note:: You can begin work on the problem in the simple editor, and then
  switch to the advanced editor. However, after you save any changes you make
  in the advanced editor, you cannot switch back to the simple editor.

=================================================
Use the Simple Editor to Add a Dropdown Problem
=================================================

When you add a dropdown problem, you can choose one of these templates.

* **Dropdown**

* **Dropdown with Hints and Feedback**

These templates include the Markdown formatting that you use in the simple
editor to add a problem without, or with, hints and feedback.

.. include:: ../../../shared/exercises_tools/Section_simple_editor.rst

========================================================================
Use the Advanced Editor to Add a Dropdown Problem
========================================================================

You can use the advanced editor to identify the elements of a dropdown
problem with OLX. For more information, see :ref:`Dropdown Problem XML`.

.. include:: ../../../shared/exercises_tools/Section_advanced_editor.rst

.. _Use Feedback in a Dropdown Problem:

********************************************
Adding Feedback to a Dropdown Problem
********************************************

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

You can add feedback in a dropdown problem using the simple editor or the
advanced editor.

=========================================
Configuring Feedback in the Simple Editor
=========================================

You can configure feedback in the :ref:`simple editor<Simple Editor>`.  When
you add a dropdown problem, select the template **Dropdown with Hints and
Feedback**. This template has example feedback syntax that you can replace.

::

  [[
  Wrong Answer {{Feedback for learners who select this answer.}}
  Wrong Answer {{Feedback for learners who select this answer.}}
  (Correct Answer) {{Feedback for learners who select this answer.}}
  ]]

.. note:: When you include feedback, you might find it more convenient to use
  new lines to separate the answer options.

For example, the following problem has feedback for each possible answer.

::

  >>A/an ________ is an example of a vegetable.<<

  [[
    apple {{An apple is the fertilized ovary that comes from an apple tree and
      contains seeds classifying it as a fruit.}}
    pumpkin {{A pumpkin is the fertilized ovary of a squash plant and contains
      seeds classifying it as a fruit.}}
    (potato) {{A potato is an edible part of a plant in tuber form and is
      classified as a vegetable}}
    tomato {{Many people mistakenly think a tomato is a vegetable. However,
      because a tomato is the fertilized ovary of a tomato plant and contains
      seeds it is classified as a fruit.}}
  ]]

===========================================
Configuring Feedback in the Advanced Editor
===========================================

In the advanced editor, you configure answer feedback with the following
syntax.

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

===========================
Customizing Feedback Labels
===========================

By default, the feedback labels shown to learners are **Correct** and
**Incorrect**. If you do not define feedback labels, learners see these terms
when they submit an answer, as in the following example.

::

  Incorrect:
  An apple is the fertilized ovary that comes from an apple tree and contains
  seeds classifying it as a fruit.

You can configure the problem to override the default labels. For example, you
can configure a custom label for a specific wrong answer.

::

  Not Quite:
  Many people mistakenly think a tomato is a vegetable. However, because a
  tomato is the fertilized ovary of a tomato plant and contains seeds it is
  classified as a fruit.

.. note::
  The default labels **Correct** and **Incorrect** display in the learner's
  requested language. If you provide custom labels, they display as you define
  them to all learners. They are not translated into different languages.

Customize Feedback Labels in the Simple Editor
***********************************************

In the :ref:`simple editor<Simple Editor>`, you configure custom feedback
labels with the following syntax.

::

  [[
  Incorrect Answer {{Label:: Feedback for learners who select this answer.}}
  .
  .
  .
  ]]

That is, you provide the label text, followed by two colon (:) characters,
before the feedback text.

For example, the following feedback is configured to use a custom label.

::

  [[
  tomato {{Not Quite:: Many people mistakenly think a tomato is a
  vegetable. However, because a tomato is the fertilized ovary of a tomato
  plant and contains seeds, it is a fruit.}}
  .
  .
  .
  ]]

Customize Feedback Labels in the Advanced Editor
*************************************************

In the :ref:`advanced editor<Advanced Editor>`, you configure custom feedback
labels with the following syntax.

.. code-block:: xml

   <option correct="False">Answer
     <optionhint label="Custom Label">Feedback for learners who select this answer.</optionhint>
   </option>

For example, the following feedback is configured to use a custom label.

.. code-block:: xml

  <option correct="False">tomato
    <optionhint label="Not Quite">Many people mistakenly think a tomato is a
     vegetable. However, because a tomato is the fertilized ovary of a tomato
     plant and contains seeds it is classified as a fruit.</optionhint>
  </option>

.. _Use Hints in a Dropdown Problem:

************************************
Adding Hints to a Dropdown Problem
************************************

You can add hints to a dropdown problem using the simple editor
or the advanced editor. For an overview of hints in problems, see
:ref:`Adding Feedback and Hints to a Problem`.

.. include:: ../../../shared/exercises_tools/Subsection_configure_hints.rst


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

``<optionresponse>``
*********************

Required. Indicates that the problem is a dropdown problem.

Attributes
==========

None.

Children
========

* ``<label>``
* ``<description>``
* ``<optioninput>``
* ``<solution>``


``<label>``
***********

Required. Identifies the question or prompt.

Attributes
==========

None.

Children
========

None.

``<description>``
*****************

Optional. Provides clarifying information about how to answer the question.

Attributes
==========

None.

Children
========

None.

``<optioninput>``
*******************

Required. Designates an answer option.

Attributes
==========

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

Children
========

* ``<option>``
* ``<optionhint>``

``<option>``
**************

Designates an answer option. Either a set of ``<option>`` child elements or the
``options`` attribute for ``<optioninput>`` is required.

Attributes
==========

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

``<optionhint>``
****************

Optional. Specifies feedback for the answer.

Attributes
==========

None.

Children
========

None.

``<solution>``
**************

Optional. Identifies the explanation or solution for the problem, or for one of
the questions in a problem that contains more than one question.

This element contains an HTML division ``<div>``. The division contains one or
more paragraphs ``<p>`` of explanatory text.

``<demandhint>``
****************

Optional. Specifies hints for the learner. For problems that include multiple
questions, the hints apply to the entire problem.

Attributes
==========

None.

Children
========

``<hint>``

``<hint>``
**********

Required. Specifies additional information that learners can access if needed.

Attributes
==========

None.

Children
========

None.
