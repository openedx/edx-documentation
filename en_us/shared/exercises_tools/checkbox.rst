.. _Checkbox:

##################
Checkbox Problem
##################

.. note:: EdX offers full support for this problem type.

The checkbox problem type is a core problem type that can be added to any
course. At a minimum, checkbox problems include a question or prompt and
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

In checkbox problems, learners select one or more options from a list of
possible answers. To answer the problem correctly, a learner must select all of
the options that are correct answers, and none of the options that are
incorrect. The course team must set up each checkbox problem to have at least
one correct answer.

As a best practice, be sure that all of the answer choices are unambiguous, and
avoid trick questions. Checkbox problems with ambiguity can be frustrating to
learners, especially if the problems have a limited number of attempts.

=============================
Example Checkbox Problem
=============================

In the LMS, learners both check answer options that they believe are correct
and leave unchecked the answer options that they believe are incorrect to
complete a checkbox problem. An example of a completed checkbox problem
follows.

.. image:: ../../../shared/images/CheckboxExample.png
 :alt: An incorrectly answered checkbox problem shown in the LMS. Of the answer
     options, only two of the three required answer options was checked. An
     explanation appears below the answer options.

To add the example problem illustrated above, in Studio you use the simple
editor to enter the following text and Markdown formatting.

::

  >>Learning about the benefits of preventative health care can be particularly difficult.||Check all of the options below that might be reasons why.<<

  [x] A large amount of time passes between undertaking a preventative measure
  and seeing the result.
  [ ] Non-immunized people will always fall sick.
  [x] If others are immunized, fewer people will fall sick regardless of a
  particular individual's choice to get immunized or not.
  [x] Trust in health care professionals and government officials is fragile.

  [explanation]
  People who are not immunized against a disease might still not fall sick
  from the disease. If someone is trying to learn whether or not preventative
  measures against the disease have any impact, he or she might see these
  people and conclude, since they have remained healthy despite not being
  immunized, that immunizations have no effect. Consequently, he or she would
  tend to believe that immunization (or other preventative measures) have
  fewer benefits than they actually do.
  [explanation]

The OLX (open learning XML) markup for this example checkbox problem follows.

.. code-block:: xml

  <problem>
    <choiceresponse>
      <label>Learning about the benefits of preventative health care can be
      particularly difficult.</label>
      <description>Check all of the options below that might be reasons why.</description>
      <checkboxgroup>
        <choice correct="true">A large amount of time passes between
         undertaking a preventative measure and seeing the result.</choice>
        <choice correct="false">Non-immunized people will always fall sick.</choice>
        <choice correct="true">If others are immunized, fewer people will fall
         sick regardless of a particular individual's choice to get immunized
         or not.</choice>
        <choice correct="true">Trust in health care professionals and
         government officials is fragile.</choice>
      </checkboxgroup>
      <solution>
        <div class="detailed-solution">
          <p>Explanation</p>
          <p>People who are not immunized against a disease might still not
           fall sick from the disease. If someone is trying to learn whether
           or not preventative measures against the disease have any impact,
           he or she might see these people and conclude, since they have
           remained healthy despite not being immunized, that immunizations
           have no effect. Consequently, he or she would tend to believe that
           immunization (or other preventative measures) have fewer benefits
           than they actually do.</p>
        </div>
      </solution>
    </choiceresponse>
  </problem>

==========================================
Analyzing Performance on Checkbox Problems
==========================================

For the checkbox problems in your course, you can use edX Insights to review
aggregated learner performance data and examine submitted answers. For more
information, see :ref:`insights:Using edX Insights`.

**************************
Adding a Checkbox Problem
**************************

You add checkbox problems in Studio by selecting the **Problem** component type
and then using either the simple editor or the advanced editor to specify the
prompt and the answer options.

.. contents::
  :local:
  :depth: 1

.. note:: You can begin work on the problem in the simple editor, and then
  switch to the advanced editor. However, after you save any changes you make
  in the advanced editor, you cannot switch back to the simple editor.

======================================================
Use the Simple Editor to Add a Checkbox Problem
======================================================

When you add a checkbox problem, you can choose one of these templates.

* **Checkboxes**

* **Checkboxes with Hints and Feedback**

These templates include the Markdown formatting that you use in the simple
editor to add a problem without, or with, hints and feedback.

.. include:: ../../../shared/exercises_tools/Section_simple_editor.rst

==================================================
Use the Advanced Editor to Add a Checkbox Problem
==================================================

You can use the advanced editor to identify the elements of a checkbox problem
with OLX. For more information, see :ref:`Checkbox Problem XML`.

.. include:: ../../../shared/exercises_tools/Section_advanced_editor.rst

.. _Use Feedback in a Checkbox Problem:

********************************************
Adding Feedback to a Checkbox Problem
********************************************

For an overview of feedback in problems, see :ref:`Adding Feedback and Hints to
a Problem`. For checkbox problems, you can add feedback for each of the answer
options you provide in the problem. You can also identify different
combinations of answer options that learners are likely to select, and add
compound feedback for those combinations.

You can add feedback to a checkbox problem using the simple editor
or the advanced editor.

=========================================
Adding Feedback for Individual Options
=========================================

In checkbox problems, you can provide feedback for each option that a learner
can select, with distinct feedback depending on whether or not the learner
selects that option. This means that there are several possible types of
feedback.

* The learner selects a correct option. This type of feedback
  should indicate why the option is correct.

* The learner does not select a correct option. This type of feedback should
  indicate that the learner missed checking this option and why it is correct.

* The learner selects an incorrect option. This type of feedback should
  indicate that the learner incorrectly checked this option and why it is
  incorrect.

* The learner does not select an incorrect option. This type of feedback should
  reinforce why the learner correctly left this option unselected.

=============================
Adding Compound Feedback
=============================

You can configure the checkbox problem to provide compound feedback.
Compound feedback is feedback given for a specific combination of options. For
example, if you have three possible option in the problem, you can define
specific feedback for when a learner selects each combination of possible
options.

* A
* B
* C
* A, B
* B, C
* A, C
* A, B, C

For problems with more than three options, providing specific feedback for each
combination can become difficult. For such problems, you might choose to define
compound feedback for more likely combinations of option or for combinations of
option that reflect common learner misunderstandings. If you do not define
feedback for a combination that a learner selects, the learner receives
feedback for the individual selections.

==========================================
Configuring Feedback in the Simple Editor
==========================================

You can configure individual option or compound feedback in the :ref:`simple
editor<Simple Editor>`. When you create a new checkbox problem, select the
template **Checkboxes with Hints and Feedback**. This template has example
formatted feedback that you can replace with your own text.

Configure Feedback for Individual Options
******************************************

In the simple editor, you configure individual option feedback with the
following Markdown formatting.

::

  [x] answer  {{ selected: Feedback when learner selects this option. },
  {unselected: Feedback when the learner does not select this option.}}

.. note:: You can use ``S`` for ``selected`` and ``U`` for unselected.

For example, the following problem has feedback for every answer option,
whether learners select a given option or leave it unselected.

::

  >>Which of the following is an example of a fruit?||Check all that apply.<<

  [x] apple {{ selected: You are correct that an apple is a fruit because it
  is the fertilized ovary that comes from an apple tree and contains seeds. },
  { unselected: Remember that an apple is also a fruit.}}

  [x] pumpkin {{ selected: You are correct that a pumpkin is a fruit because it
  is the fertilized ovary of a squash plant and contains seeds.}, { unselected:
  Remember that a pumpkin is also a fruit.}}

  [ ] potato {{ U: You are correct that a potato is a vegetable because it is
  an edible part of a plant in tuber form.}, { S: A potato is a vegetable, not
  a fruit, because it does not come from the flower on a plant or tree and does
  not contain seeds.}}

  [x] tomato {{ S: You are correct that a tomato is a fruit because it is the
  fertilized ovary of a tomato plant and contains seeds. }, { U: Many people
  mistakenly think a tomato is a vegetable. However, because a tomato is the
  fertilized ovary of a tomato plant and contains seeds it is classified as a
  fruit.}}

Configure Compound Feedback
****************************

In the simple editor, you configure compound feedback after the possible
options, with the following syntax.

::

  {{ ((Answer Combination)) Feedback when learner selects this combination of
  options.}}

For example, the following compound feedback is used when learners select
options **A, B, and D** or **A, B, C, and D**.

::

  {{ ((A B D)) An apple, pumpkin, and tomato are all fruits as they are all the
  fertilized ovaries of a plant and contain seeds. }}

  {{ ((A B C D)) You are correct that an apple, pumpkin, and tomato are all
  fruits as they are all the fertilized ovaries of a plant and contain seeds.
  However, a potato is not a fruit as it is an edible part of a plant in tuber
  form and is classified as a vegetable.  }}

.. note:: If you configure individual option feedback for every answer, and
  you also provide compound feedback, when learners select the exact
  combination of answer choices defined, they only see the compound feedback.
  In this example, learners who select apple (A), pumpkin (B), and tomato (D)
  see the message "An apple, pumpkin, and tomato are all fruits as they are all
  the fertilized ovaries of a plant and contain seeds." They do not also see
  the individual feedback for selecting A, B, and D, and for leaving C
  unselected.

============================================
Configuring Feedback in the Advanced Editor
============================================

You can configure individual option and compound feedback in the advanced
editor.

Configure Individual Option Feedback
*************************************

In the advanced editor, you configure individual option feedback with the
following syntax.

.. code-block:: xml

      <choice correct="true">Choice label
        <choicehint selected="true">Feedback for when learner selects this
         answer.</choicehint>
        <choicehint selected="false">Feedback for when learner does not select
         this answer.</choicehint>
      </choice>

For example, the following problem has feedback for each option, selected or
unselected.

.. code-block:: xml

  <problem>
    <choiceresponse>
      <label>Which of the following is an example of a fruit?</label>
      <description>Check all that apply.</description>
      <checkboxgroup>
        <choice correct="true">apple
          <choicehint selected="true">You are correct that an apple is a fruit
           because it is the fertilized ovary that comes from an apple tree and
           contains seeds.</choicehint>
          <choicehint selected="false">Remember that an apple is also a
           fruit.</choicehint>
        </choice>
        <choice correct="true">pumpkin
          <choicehint selected="true">You are correct that a pumpkin is a fruit
           because it is the fertilized ovary of a squash plant and contains
           seeds.</choicehint>
          <choicehint selected="false">Remember that a pumpkin is also a
           fruit. </choicehint>
        </choice>
        <choice correct="false">potato
          <choicehint selected="true">A potato is a vegetable, not a fruit,
           because it does not come from the flower on a plant or tree and does
           not contain seeds.</choicehint>
          <choicehint selected="false">You are correct that a potato is
           classified as a vegetable because it is an edible part of a plant in
           tuber form.</choicehint>
        </choice>
        <choice correct="true">tomato
          <choicehint selected="true">You are correct that a tomato is
           classified as a fruit because it is the fertilized ovary of a tomato
           plant and contains seeds.</choicehint>
          <choicehint selected="false">Many people mistakenly think a tomato is
           a vegetable. However, because a tomato is the fertilized ovary of a
           tomato plant and contains seeds it is classified as a fruit.</choicehint>
        </choice>
      </checkboxgroup>
    </choiceresponse>
  </problem>

Configure Compound Feedback
***************************

In the advanced editor, you define compound feedback by adding a
``<compoundhint>`` element within the ``<checkboxgroup>`` element.

.. code-block:: xml

          .
          .
          .
        </choice>
        <compoundhint value="Answer Combination">Feedback when learner selects
         this combination of answers.</compoundhint>
      </checkboxgroup>

For example, the following compound feedback is used when learners select
options **A, B, and D** or **A, B, C, and D**.

.. code-block:: xml

          .
          .
          .
        </choice>
        <compoundhint value="A B D">An apple, pumpkin, and tomato are all
         fruits as they all are fertilized ovaries of a plant and contain
         seeds.</compoundhint>
        <compoundhint value="A B C D">You are correct that an apple, pumpkin,
         and tomato are all fruits as they all are fertilized ovaries of a
         plant and contain seeds. However, a potato is not a fruit as it is an
         edible part of a plant in tuber form and is classified as a vegetable.
        </compoundhint>
      </checkboxgroup>

.. _Use Hints in a Checkbox Problem:

********************************************
Adding Hints to a Checkbox Problem
********************************************

You can add hints to a checkbox problem using the simple editor
or the advanced editor. For an overview of hints in problems, see
:ref:`Adding Feedback and Hints to a Problem`.

.. include:: ../../../shared/exercises_tools/Subsection_configure_hints.rst

.. _Awarding Partial Credit in a Checkbox Problem:

*********************************************
Awarding Partial Credit in a Checkbox Problem
*********************************************

You can configure a checkbox problem to award partial credit to learners
who submit an answer that is partly correct. You must use the `advanced editor
<Use the Advanced Editor to Edit a Checkbox Problem>`_ to configure partial
credit.

For an overview of partial credit in problems, see :ref:`Awarding Partial
Credit for a Problem`.

.. only:: Partners

 .. note::
    Support for partial credit problems in courses on edx.org and edX
    Edge is provisional. Ensure that you test such problems thoroughly before
    releasing them to learners. For more information, contact your edX partner
    manager.

In the following example, the learner selected two of the three correct
choices, and did not select any incorrect choices. The learner therefore had
four out of five correct answers. Because the course team set this problem up
to award partial credit for every correct answer selected and every incorrect
answer left unselected (known as `every decision counts`_), the learner earned
80% of the points for this problem.

.. image:: ../../../shared/images/checkbox_partial_credit.png
 :alt: A checkbox choice problem with partial credit for two out of
     three answers.
 :width: 600

You can use the following methods to award partial credit in a checkbox
problem.

.. contents::
  :local:
  :depth: 1

.. _Every Decision Counts:

======================================
Using the Every Decision Counts Method
======================================

You can configure a checkbox problem so that the learner's response for every
option is evaluated and scored. This method is known as every decision counts
(EDC).

With EDC, for each option the learner gets wrong, either by not selecting a
correct option or selecting an incorrect option, the learner's score is
reduced by 1/n, where "n" is the number of options.

For example, if there are four options, each one is worth 25% of the total
score. If a learner's response is wrong for one option, she receives 75% of the
points for the problem.

The following table describes the learner's score for different submissions
for EDC problems with a variety of correct answer options.

.. list-table::
     :widths: 20 20 20 20
     :header-rows: 1

     * - Learner's Selections
       - Correct Answers
       - Incorrect Answers
       - Score
     * - A, B, C
       - A, B, D
       - C
       - 75%
     * - A
       - A, C, D
       - B
       - 75%
     * - A, C
       - A, D
       - B, C
       - 50%
     * - C, D
       -
       - A, B, C, D
       - 0%

Configure an EDC Checkbox Problem
**********************************

To configure an EDC checkbox problem, you add the ``partial_credit="EDC"``
attribute to the ``<choiceresponse>`` element in the problem OLX.

For example, the following OLX shows the checkbox problem template after it is
updated to provide partial credit.

.. code-block:: xml

  <problem>
    <choiceresponse partial_credit="EDC">
      <label>Which of the following is a fruit?</label>
      <description>Check all that apply.</description>
      <checkboxgroup>
        <choice correct="true">apple</choice>
        <choice correct="true">pumpkin</choice>
        <choice correct="false">potato</choice>
        <choice correct="true">tomato</choice>
      </checkboxgroup>
    </choiceresponse>
  </problem>

==========================
Using the By Halves Method
==========================

You can configure a checkbox problem so that for every option that a learner
gets wrong, either by not selecting a correct option or by selecting an
incorrect option, half of the remaining points are deducted from the learner's
score. This method is known as scoring by halves.

.. note:: By design, partial credit by halves requires the number of answer
   options to be more than twice the number of incorrect answers. In addition,
   partial credit is not given for more than two wrong answers, regardless of
   the total number of answer options. In other words, two wrong answers is
   scored at 25% only if there are at least 5 answer options. Three or more
   wrong answers is always scored at 0%, regardless of the number of total
   answer options.

Partial credit using the by halves method is calculated as follows.

* If a learner makes no errors, she receives full credit for the problem.

* If a learner makes one error, she receives 50% of the possible points, as
  long as there are three or more choices in the problem. If a learner makes
  one error and there are only two choices in the problem, no credit is given.

* If a learner makes two errors, she receives 25% of the possible points, as
  long as there are five or more choices in the problem. If a learner makes two
  errors and there are only three choices or four choices in the problem, no
  credit is given.

* If a learner makes three errors, she receives no credit for the problem,
  regardless of how many answer options there are.

The following tables illustrate partial credit score using the halves method,
for problems with an increasing number of total answer options.

.. list-table::
     :widths: 30 30 30
     :header-rows: 1

     * - Number of Incorrect Answers
       - Number of Answer Options
       - Credit Given (%)
     * - 0
       - 2
       - 100
     * - 1
       - 2
       - 0
     * - 2
       - 2
       - 0

.. list-table::
     :widths: 30 30 30
     :header-rows: 1

     * - Number of Incorrect Answers
       - Number of Answer Options
       - Credit Given (%)
     * - 0
       - 3
       - 100
     * - 1
       - 3
       - 0
     * - 2
       - 3
       - 0
     * - 3
       - 3
       - 0

.. list-table::
     :widths: 30 30 30
     :header-rows: 1

     * - Number of Incorrect Answers
       - Number of Answer Options
       - Credit Given (%)
     * - 0
       - 4
       - 100
     * - 1
       - 4
       - 50
     * - 2
       - 4
       - 0
     * - 3
       - 4
       - 0
     * - 4
       - 4
       - 0

.. list-table::
     :widths: 30 30 30
     :header-rows: 1

     * - Number of Incorrect Answers
       - Number of Answer Options
       - Credit Given (%)
     * - 0
       - 5
       - 100
     * - 1
       - 5
       - 50
     * - 2
       - 5
       - 25
     * - 3
       - 5
       - 0
     * - 4
       - 5
       - 0
     * - 5
       - 5
       - 0

.. list-table::
     :widths: 30 30 30
     :header-rows: 1

     * - Number of Incorrect Answers
       - Number of Answer Options
       - Credit Given (%)
     * - 0
       - 7
       - 100
     * - 1
       - 7
       - 50
     * - 2
       - 7
       - 25
     * - 3
       - 7
       - 0
     * - 4
       - 7
       - 0
     * - 5
       - 7
       - 0


Configure a By Halves Checkbox Problem
**************************************

To configure a by halves checkbox problem, you add the
``partial_credit="halves"`` attribute to the ``<choiceresponse>`` element in
the problem OLX.

The following example shows a checkbox problem that provides partial credit by
halves.

.. code-block:: xml

  <problem>
    <choiceresponse partial_credit="halves">
      <label>Which of the following is a fruit?</label>
      <description>Check all that apply.</description>
      <checkboxgroup>
        <choice correct="true">apple</choice>
        <choice correct="true">pumpkin</choice>
        <choice correct="false">potato</choice>
        <choice correct="true">tomato</choice>
      </checkboxgroup>
    </choiceresponse>
  </problem>

.. _Checkbox Problem XML:

******************************
Checkbox Problem OLX Reference
******************************

============
Template
============

.. code-block:: xml

  <problem>
    <choiceresponse>
      <label>Question or prompt text</label>
      <description>Information about how to answer the question</description>
      <checkboxgroup>
        <choice correct="false">Answer option A (incorrect)</choice>
        <choice correct="true">Answer option B (correct)</choice>
        <choice correct="true">Answer option C (correct)</choice>
      </checkboxgroup>
    <solution>
      <div class="detailed-solution">
        <p>Optional header for the explanation or solution</p>
        <p>Optional explanation or solution text</p>
      </div>
    </solution>
    </choiceresponse>
    <demandhint>
      <hint>Hint 1</hint>
      <hint>Hint 2</hint>
    </demandhint>
  </problem>

=========
Elements
=========

For checkbox problems, the ``<problem>`` element can include this hierarchy of
child elements.


.. code-block:: xml

  <choiceresponse>
      <label>
      <description>
      <checkboxgroup>
            <choice>
                <choicehint>
            <compoundhint>
      <solution>
  <demandhint>
      <hint>

In addition, standard HTML tags can be used to format text.

``<choiceresponse>``
*********************

Required. Indicates that the problem is a checkbox problem.

Attributes
==========

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``partial_credit``
     - Optional. Specifies the type of partial credit given. ``EDC`` or
       ``halves``.

Children
========

* ``<label>``
* ``<description>``
* ``<checkboxgroup>``
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

``<checkboxgroup>``
*******************

Required. Indicates the beginning of the list of options.

Attributes
==========

None.

Children
========

* ``<choice>``
* ``<compoundhint>``

``<choice>``
************

Required. Designates an answer option.

Attributes
==========

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``correct``
     - Indicates a correct or incorrect answer.

       * When set to ``"true"``, the choice is a correct answer. At least one
         required.
       * When set to ``"false"``, the choice is an incorrect answer.

Children
========

``<choicehint>``

``<choicehint>``
****************

Optional. Specifies feedback for the answer.

Attributes
==========

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``selected``
     -  Required. ``true`` or ``false``. Indicates if the feedback is given
        when the answer option is selected, or when it is not selected.

Children
========

None.

``<compoundhint>``
******************

Optional. Specifies feedback for a specific combination of answers.

Attributes
==========

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``value`` (at least one required)
     - Indicates the combination of selected answers that triggers this
       feedback. Answers are identified by uppercase letters, in ascending
       alphabetical order.

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

