.. _Multiple Choice:

########################
Multiple Choice Problem
########################

.. note:: EdX offers full support for this problem type.

The multiple choice problem type is a core problem type that can be added to
any course. At a minimum, multiple choice problems include a question or
prompt and several answer options. By adding hints, feedback, or both, you can
give learners guidance and help when they work on a problem.

.. contents::
  :local:
  :depth: 2

For more information about the core problem types, see
:ref:`Working with Problem Components`.

**********
Overview
**********

In multiple choice problems, learners select one option from a list of answer
options. Unlike :ref:`dropdown<Dropdown>` problems, where the answer choices
do not appear until the learner selects the dropdown arrow, answer choices for
multiple choice problems are immediately visible directly below the question.

Multiple choice problems can also have several advanced options, such as
reordering, or shuffling, the set of answer choices for each learner. For more
information about these options, see :ref:`Multiple Choice Advanced Options`.

================================
Example Multiple Choice Problem
================================

In the LMS, learners select a single answer option to complete a multiple
choice problem. An example of a completed multiple choice problem follows.

.. image:: ../../../shared/images/MultipleChoiceExample.png
 :alt: An incorrectly answered multiple choice problem shown in the LMS. One of
   the answer options was incorrectly selected. An explanation appears below
   the answer options.
 :width: 600

To add the example problem illustrated above, you enter the following text
and Markdown formatting in the simple editor in Studio.

::

    >>Lateral inhibition, as was first discovered in the horseshoe crab:<<

    ( ) is a property of touch sensation, referring to the ability of crabs
    to detect nearby predators.
    ( ) is a property of hearing, referring to the ability of crabs to detect
    low frequency noises.
    (x) is a property of vision, referring to the ability of crabs' eyes to
    enhance contrasts.
    ( ) has to do with the ability of crabs to use sonar to detect fellow
    horseshoe crabs nearby.
    ( ) has to do with a weighting system in the crab's skeleton that allows
    it to balance in turbulent water.

    [Explanation]
    Horseshoe crabs were essential to the discovery of lateral
    inhibition, a property of vision present in horseshoe crabs as well as in
    humans that enables enhancement of contrast at edges of objects as was
    demonstrated in class. In 1967, Haldan Hartline received the Nobel prize
    for his research on vision and in particular his research investigating
    lateral inhibition using horseshoe crabs.
    [Explanation]

The open learning XML (OLX) markup for this example problem follows.

.. code-block:: xml

  <problem>
    <multiplechoiceresponse>
      <label>Lateral inhibition, as was first discovered in the horseshoe crab:</label>
      <choicegroup type="MultipleChoice">
        <choice correct="false">is a property of touch sensation, referring to
         the ability of crabs to detect nearby predators.</choice>
        <choice correct="false">is a property of hearing, referring to the
         ability of crabs to detect low frequency noises.</choice>
        <choice correct="false">is a property of vision, referring to the
         ability of crabs' eyes to enhance contrasts.</choice>
        <choice correct="true">has to do with the ability of crabs to use
         sonar to detect fellow horseshoe crabs nearby.</choice>
        <choice correct="false">has to do with a weighting system in the
         crab's skeleton that allows it to balance in turbulent water.</choice>
      </choicegroup>
      <solution>
        <div class="detailed-solution">
          <p>Explanation</p>
          <p>Horseshoe crabs were essential to the discovery of lateral
           inhibition, a property of vision present in horseshoe crabs as well
           as humans that enables enhancement of contrast at edges of objects
           as was demonstrated in class. In 1967, Haldan Hartline received the
           Nobel prize for his research on vision and in particular his
           research investigating lateral inhibition using horseshoe crabs.</p>
        </div>
      </solution>
    </multiplechoiceresponse>
  </problem>

====================================================
Analyzing Performance on Multiple Choice Problems
====================================================

For the multiple choice problems in your course, you can use edX Insights to
review aggregated learner performance data and examine the submitted answers.
For more information, see :ref:`insights:Using edX Insights`.

===========================================================
Pedagogical Considerations for Multiple Choice Questions
===========================================================

EdX recommends the use, whenever possible, of authentic assessment rather than
multiple choice questions for graded problems. The use of authentic assessment
in online courses tends to lead to better learning outcomes. In addition,
authentic assessment allows for infinite attempts, mastery learning, and more
intellectual risk taking, which lead to substantially better learning outcomes.

Multiple choice questions do have these uses.

* Ungraded multiple choice questions can help students think about a concept in
  the context of knowledge transfer.

* For many subject areas, authentic assessments are either unavailable or
  prohibitively complex to use. In such courses, multiple choice questions can
  act as the only available fall back.

Fortunately, multiple choice questions are among the best studied in assessment
literature. A few guidelines for the creation of such questions follow.

* Organize the set of answers logically. Use consistent phrasing for the
  answers, and when possible, parallel structure.

* Place as many of the words in the stem as possible, and keep the answers as
  concise as possible.

* The distractors should not be substantially shorter, longer, or use different
  structure than the correct answer. The answer options should be as consistent
  in structure, length, and phrasing as possible.

* Avoid using negatives (and especially double negatives) in the question and
  the answers.

* Test higher order thinking (comprehension and critical thinking). Avoid
  simple recall.

* If you specify a finite number of attempts, avoid trick questions and try to
  keep wording clear and unambiguous.

* Make all distractors plausible.

* Use "All of the above" and "None of the above" answer options with caution.
  If a learner can identify at least two correct answers, it can give away the
  answer with only partial comprehension.

****************************************
Adding a Multiple Choice Problem
****************************************

You add multiple choice problems in Studio by selecting the **Problem**
component type and then using either the simple editor or the advanced editor
to specify the prompt and the answer options.

.. contents::
  :local:
  :depth: 1

.. note:: You can begin work on the problem in the simple editor, and then
  switch to the advanced editor. However, after you save any changes you make
  in the advanced editor, you cannot switch back to the simple editor.

================================================================
Use the Simple Editor to Add a Multiple Choice Problem
================================================================

When you add a multiple choice problem, you can choose one of these templates.

* **Multiple Choice**

* **Multiple Choice with Hints and Feedback**

These templates include the Markdown formatting that you use in the
:ref:`simple editor<Simple Editor>` to add a problem without, or with, hints
and feedback.

.. include:: ../../../shared/exercises_tools/Section_simple_editor.rst

========================================================================
Use the Advanced Editor to Add a Multiple Choice Problem
========================================================================

You can use the :ref:`advanced editor<Advanced Editor>` to identify the
elements of a multiple choice problem with OLX. For more information, see
:ref:`Multiple Choice Problem XML`.

.. include:: ../../../shared/exercises_tools/Section_advanced_editor.rst

.. _Use Feedback in a Multiple Choice Problem:

********************************************
Adding Feedback to a Multiple Choice Problem
********************************************

For an overview of feedback in problems, see :ref:`Adding Feedback and Hints to
a Problem`. You can add feedback for each of the answer options you provide in
the problem. Use the following guidelines when providing feedback.

* Add feedback to incorrect answers to target common misconceptions and
  mistakes.

* Ensure feedback provides some guidance to the learner about how to arrive at
  the correct answer.

* Add feedback for the correct answer to reinforce why the answer is correct.
  Because learners are able to guess, ensure that feedback provides a reason
  why the answer is correct for learners who might have selected that answer by
  chance.

You can add feedback in a multiple choice problem using the simple editor
or the advanced editor.

==========================================
Configuring Feedback in the Simple Editor
==========================================

You can configure feedback in the :ref:`simple editor<Simple Editor>`.  When
you add a multiple choice problem, select the template **Multiple Choice
with Hints and Feedback**. This template has example feedback syntax that you
can replace.

::

  ( ) answer {{Feedback for learners who select this answer.}}

For example, the following problem has feedback for every answer option.

::

  >>Which of the following is an example of a vegetable?||You can select only one option.<<

  ( ) apple {{An apple is the fertilized ovary that comes from an apple tree
  and contains seeds classifying it as a fruit.}}
  ( ) pumpkin {{A pumpkin is the fertilized ovary of a squash plant and
  contains seeds classifying it as a fruit.}}
  (x) potato {{A potato is an edible part of a plant in tuber form and is
  classified as a vegetable}}
  ( ) tomato {{Many people mistakenly think a tomato is a vegetable. However,
  because a tomato is the fertilized ovary of a tomato plant and contains
  seeds it is classified as a fruit.}}

============================================
Configuring Feedback in the Advanced Editor
============================================

In the advanced editor, you configure feedback with the following syntax.

.. code-block:: xml

    <choice correct="false">Choice Label
      <choicehint>Feedback for when learner selects this answer.</choicehint>
    </choice>

For example, the following problem has feedback for each answer.

.. code-block:: xml

  <problem>
    <multiplechoiceresponse>
      <label>Which of the following is an example of a vegetable?</label>
      <description>You can select only one option.</description>
      <choicegroup type="MultipleChoice">
        <choice correct="false">apple
          <choicehint>An apple is the fertilized ovary that comes from an apple
           tree and contains seeds classifying it as a fruit.</choicehint>
        </choice>
        <choice correct="false">pumpkin
          <choicehint>A pumpkin is the fertilized ovary of a squash plant
           and contains seeds classifying it as a fruit.</choicehint>
        </choice>
        <choice correct="true">potato
          <choicehint>A potato is an edible part of a plant in tuber form and
           is classified as a vegetable.</choicehint>
        </choice>
        <choice correct="false">tomato
          <choicehint>Many people mistakenly think a tomato is a vegetable.
           However, because a tomato is the fertilized ovary of a tomato plant
           and contains seeds it is classified as a fruit.</choicehint>
        </choice>
      </choicegroup>
    </multiplechoiceresponse>
  </problem>

===========================
Customizing Feedback Labels
===========================

By default, the feedback labels shown to learners are **Correct** and
**Incorrect**. If you do not define feedback labels, learners see these terms
when they submit an answer, as in the following example.

::

  Incorrect: A pumpkin is the fertilized ovary of a squash plant and contains
  seeds classifying it as a fruit.

You can configure the problem to override the default labels. For example, you
can configure a custom label for a specific wrong answer.

::

  Not Quite: Many people mistakenly think a tomato is a vegetable. However,
  because a tomato is the fertilized ovary of a tomato plant and contains seeds
  it is classified as a fruit.

.. note::
  The default labels **Correct** and **Incorrect** display in the learner's
  requested language. If you provide custom labels, they display as you define
  them to all learners. They are not translated into different languages.

Customize Feedback Labels in the Simple Editor
***********************************************

In the :ref:`simple editor<Simple Editor>`, you configure custom feedback
labels with the following syntax.

::

  ( ) Answer {{Label:: Feedback for learners who select this answer.}}

That is, you provide the label text, followed by two colon (:) characters,
before the feedback text.

For example, the following feedback is configured to use a custom label.

::

  ( ) tomato {{Not Quite:: Many people mistakenly think a tomato is a
  vegetable. However, because a tomato is the fertilized ovary of a tomato
  plant and contains seeds, it is a fruit.}}

Customize Feedback Labels in the Advanced Editor
*************************************************

In the :ref:`advanced editor<Advanced Editor>`, you configure custom feedback
labels with the following syntax.

.. code-block:: xml

    <choice correct="true or false">Answer
      <choicehint label="Custom Label">Feedback for learners who select this
       answer.</choicehint>
    </choice>

For example, the feedback for the following answer option is configured to use
a custom label.

.. code-block:: xml

  <choice correct="false">tomato
    <choicehint label="Not Quite">Many people mistakenly think a tomato is a
     vegetable. However, because a tomato is the fertilized ovary of a tomato
     plant and contains seeds, it is a fruit.</choicehint>
  </choice>

.. _Use Hints in a Multiple Choice Problem:

********************************************
Adding Hints to a Multiple Choice Problem
********************************************

You can add hints to a multiple choice problem using the simple editor
or the advanced editor. For an overview of hints in problems, see
:ref:`Adding Feedback and Hints to a Problem`.

.. include:: ../../../shared/exercises_tools/Subsection_configure_hints.rst

.. _Awarding Partial Credit in a Multiple Choice Problem:

****************************************************
Awarding Partial Credit in a Multiple Choice Problem
****************************************************

You can configure a multiple choice problem so that specific incorrect answers
award learners partial credit for the problem. You must use the :ref:`advanced
editor<Advanced Editor>` to configure partial credit.

.. only:: Partners

 .. note::
    Support for partial credit problems in courses on edx.org and edX
    Edge is provisional. Ensure that you test such problems thoroughly before
    releasing them to learners. For more information, contact your edX partner
    manager.

In the following example, the learner selected a wrong answer and received
partial credit.

.. image:: ../../../shared/images/partial_credit_multiple_choice.png
 :alt: A multiple choice problem with partial credit for an incorrect answer.
 :width: 600

You can specify what percentage of the points for the problem a learner
receives for an incorrect answer. If you do not specify the percentage, the
system uses the default of 50%.

For an overview of partial credit in problems, see
:ref:`Awarding Partial Credit for a Problem`.

=================================================================
Configure a Multiple Choice Problem to Award Partial Credit
=================================================================

To configure a multiple choice problem to award partial credit for a specific
answer, you add the following attributes to the problem OLX.

* Add the ``partial_credit="points"`` attribute to the
  ``<multiplechoiceresponse>`` element.

* For each answer that you intend to award partial credit, in the ``<choice>``
  element set the value of the ``correct`` attribute to ``"partial"``.

* Optionally, define the percentage of the problem score to award for each
  answer. Add the ``point_value`` attribute to the ``<choice>`` element, and
  enter its value as a decimal. For example, add ``point_value="0.25"`` to
  award 25% of the points to learners who select that answer. The percentage
  awarded should reflect how close the learner has gotten to a full
  understanding of the concept. If you do not add the ``point_value``
  attribute, the system uses the default of 50%.

For example, the following OLX shows a multiple choice problem that
provides partial credit of 25% for an answer option.

.. code-block:: xml

  <problem>
    <multiplechoiceresponse partial_credit="points">
      <label>Which of the following is a vegetable?</label>
      <choicegroup type="MultipleChoice">
        .
        .
        .
        <choice correct="partial" point_value="0.25">tomato </choice>
      </choicegroup>
    </multiplechoiceresponse>
  </problem>

.. _Multiple Choice Problem XML:

*************************************
Multiple Choice Problem OLX Reference
*************************************

================
Template
================

.. code-block:: xml

  <problem>
    <multiplechoiceresponse>
      <label>Question or prompt text</label>
      <description>Optional information about how to answer the question</description>
      <choicegroup type="MultipleChoice">
        <choice correct="false" name="a">Incorrect choice
          <choicehint>Hint for incorrect choice.</choicehint>
        </choice>
        <choice correct="true" name="b">Correct choice
          <choicehint>Hint for correct choice.</choicehint>
        </choice>
      </choicegroup>
      <solution>
        <div class="detailed-solution">
          <p>Optional header for the explanation or solution</p>
          <p>Optional explanation or solution text</p>
        </div>
      </solution>
    </multiplechoiceresponse>
  <demandhint>
    <hint>Hint 1</hint>
    <hint>Hint 2</hint>
  </demandhint>
  </problem>

=========
Elements
=========

For multiple choice problems, the ``<problem>`` element can include this
hierarchy of child elements.

.. code-block:: xml

  <multiplechoiceresponse>
      <label>
      <description>
      <choicegroup>
            <choice>
                <choicehint>
      <solution>
  <demandhint>
      <hint>

In addition, standard HTML tags can be used to format text.

``<multiplechoiceresponse>``
****************************

Required. Indicates that the problem is a multiple choice problem.

Attributes
==========

  .. list-table::
    :widths: 20 80
    :header-rows: 1

    * - Attribute
      - Description
    * - ``partial_credit``
      - Optional. Specifies that the problem can award partial credit. If used,
        must be set to ``"points"``.

Children
========

* ``<label>``
* ``<description>``
* ``<choicegroup>``
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

``<choicegroup>``
*****************

Required. Indicates the beginning of the list of answer options.

Attributes
==========

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``type``
     - Required. Must be set to ``"MultipleChoice"``.

Additional attributes are available to support
:ref:`advanced options<Multiple Choice Advanced Options>`.

Children
========

``<choice>``

``<choice>``
************

Required. Lists an answer option.

Attributes
==========

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``correct``
     - Indicates a correct, incorrect, or partially
       correct answer.

       * When set to ``"true"``, the choice is a correct answer. At least one
         required.
       * When set to ``"false"``, the choice is an incorrect answer.
       * When set to ``"partial"``, the learner receives partial credit for
         selecting the answer.

       You can specify more than one correct or partially correct answer,
       but learners can select only one choice to submit as their answer.

   * - ``point_value``
     - When ``correct="partial"``, indicates the percentage, as a decimal, of
       the points the learner receives for selecting this option. If
       ``point_value`` is not specified for a partial credit answer, 50% is
       used by default.
   * - ``name``
     - A unique name that is used internally to refer to the choice.

Additional attributes are available to support
:ref:`advanced options<Multiple Choice Advanced Options>`.

Children
========

``<choicehint>``

``<choicehint>``
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
the questions in a problem that includes multiple questions.

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

Children
========

None.

.. _Multiple Choice Advanced Options:

*********************************************
Advanced Options for Multiple Choice Problems
*********************************************

Multiple choice problems have several advanced options. You can change the
order of answers in the problem, include explanations that appear when a
learner selects a specific incorrect answer, or present a random set of
choices to each learner. For more information, see the following sections.

.. contents::
  :local:
  :depth: 1

.. _Shuffle Answers in a Multiple Choice Problem:

=============================================
Shuffle Answers in a Multiple Choice Problem
=============================================

Optionally, you can configure a multiple choice problem so that it shuffles
the order of possible answers.

For example, one view of a problem could be as follows.

::

 What Apple device competed with the portable CD player?

 ( ) The iPad
 ( ) Napster
 ( ) The iPod
 ( ) The vegetable peeler

Another view of the same problem, for a different learner or for the same
learner on a subsequent view of the unit, could be as follows.

::

 What Apple device competed with the portable CD player?

 ( ) The iPad
 ( ) The iPod
 ( ) The vegetable peeler
 ( ) Napster

You can also shuffle some answers, but not others. For example, you might
want to include the answer "All of the above" and have it always appear at the
end of the list, but shuffle the other answers.

You can configure the problem to shuffle answers using the simple editor or
advanced editor. To shuffle the answers, you also edit the problem to set
**Randomization** to a value other than **Never**. For more information, see
:ref:`Randomization`.

Use the Simple Editor to Shuffle Answers
*********************************************

You can configure the problem to shuffle answers in the
:ref:`simple editor<Simple Editor>`. To add shuffling to this problem, you add
an exclamation point character ``!`` between the parentheses formatting for
the first answer option.

::

 >>What Apple device competed with the portable CD player?<<
     (!) The iPad
     ( ) Napster
     (x) The iPod
     ( ) The vegetable peeler

To make the location of an answer fixed in a shuffled list, add ``@`` between
the parentheses formatting for that answer.

::

 >>What Apple device competed with the portable CD player?<<
     (!) The iPad
     ( ) Napster
     (x) The iPod
     ( ) The vegetable peeler
     (@) All of the above

You can combine symbols within the parentheses as necessary. For example, to
show the correct answer in a fixed location, you can use both ``x`` and ``@``.

::

  (x@) The iPod

After you complete problem setup in the simple editor, select **Edit** and then
**Settings** to specify an option other than **Never** for the
**Randomization** setting.

Use the Advanced Editor to Shuffle Answers
*********************************************

You can configure the problem to shuffle answers by editing the OLX in the
:ref:`advanced editor<Advanced Editor>`.

To add shuffling to a problem, you add ``shuffle="true"`` to the
``<choicegroup>`` element.

.. code-block:: xml

  <problem>
    <multiplechoiceresponse>
      <label>What Apple device competed with the portable CD player?</label>
      <choicegroup type="MultipleChoice" shuffle="true">
        <choice correct="false">The iPad</choice>
        <choice correct="false">Napster</choice>
        <choice correct="true">The iPod</choice>
        <choice correct="false">The vegetable peeler</choice>
      </choicegroup>
    </multiplechoiceresponse>
  </problem>

To make the location of an answer fixed in a shuffled list, add
``fixed="true"`` to the ``choice`` element for the answer.

.. I removed the "rerandomize="always" attribute from the <problem> element as it does not work. Looks like you must set this in settings now? Tested on Edge as well as the  sandbox. - Alison 4 Aug 2016

.. code-block:: xml

  <problem>
    <multiplechoiceresponse>
      <label>What Apple device competed with the portable CD player?</label>
      <choicegroup type="MultipleChoice" shuffle="true">
        .
        .
        .
        <choice correct="false" fixed="true">All of the above</choice>
      </choicegroup>
    </multiplechoiceresponse>
  </problem>

Then, you select **Settings** to specify an option other than **Never** for the
**Randomization** setting.

.. _Targeted Feedback in a Multiple Choice Problem:

===============================================
Targeted Feedback in a Multiple Choice Problem
===============================================

You can configure a multiple choice problem so that explanations for specific
answers are automatically shown to learners. You can use these explanations to
guide learners towards the right answer. Therefore, targeted feedback is most
useful for multiple choice problems for which learners are allowed multiple
attempts.

Use the Advanced Editor to Configure Targeted Feedback
********************************************************

You configure the problem to provide targeted feedback by editing the OLX in
the :ref:`advanced editor<Advanced Editor>`.

* Add a ``targeted-feedback`` attribute to the ``<multiplechoiceresponse>``
  element, with no value: ``<multiplechoiceresponse targeted-feedback="">``.

* Add an ``explanation-id`` attribute with a unique value to each of the
  ``<choice>`` elements: ``<choice correct="false"
  explanation-id="feedback1">``.

* You can use the ``<solution>`` element for the correct answer.

* Add a ``<targetedfeedbackset>`` element after the
  ``<multiplechoiceresponse>`` element.

* Within ``<targetedfeedbackset>``, add one or more ``<targetedfeedback>``
  elements.

* Within each ``<targetedfeedback>`` element, add one of the unique identifying
  ``explanation-id`` attributes to map that feedback to a specific answer
  choice.

* Within each ``<targetedfeedback>`` element use HTML formatting, such as
  ``<p></p>`` tags, to enter your explanation for the specified answer option.

For example, the OLX for a multiple choice problem follows, showing a unique ID
for each answer choice. This is immediately followed by OLX that defines the
targeted feedback.

.. code-block:: xml

  <problem>
    <multiplechoiceresponse targeted-feedback="">
      <label>What Apple device competed with the portable CD player?</label>
      <choicegroup type="MultipleChoice">
        <choice correct="false" explanation-id="feedback1">The iPad</choice>
        <choice correct="false" explanation-id="feedback2">Napster</choice>
        <choice correct="true" explanation-id="correct">The iPod</choice>
        <choice correct="false" explanation-id="feedback3">The vegetable peeler</choice>
      </choicegroup>
      <solution explanation-id="correct">
        <div class="detailed-solution">
          <p>The iPod directly competed with portable CD players.</p>
        </div>
      </solution>
    </multiplechoiceresponse>
    <targetedfeedbackset>
      <targetedfeedback explanation-id="feedback1">
        <div class="detailed-targeted-feedback">
          <p>Targeted Feedback</p>
          <p>The iPad came out later and did not directly compete with
           portable CD players.</p>
         </div>
      </targetedfeedback>
      <targetedfeedback explanation-id="feedback2">
        <div class="detailed-targeted-feedback">
          <p>Targeted Feedback</p>
          <p>Napster was not an Apple product.</p>
        </div>
      </targetedfeedback>
      <targetedfeedback explanation-id="feedback3">
        <div class="detailed-targeted-feedback">
          <p>Targeted Feedback</p>
          <p>Vegetable peelers do not play music.</p>
        </div>
      </targetedfeedback>
    </targetedfeedbackset>
  </problem>

.. _Answer Pools in a Multiple Choice Problem:

=============================================
Answer Pools in a Multiple Choice Problem
=============================================

You can configure a multiple choice problem so that a random subset of choices
are shown to each learner. For example, you can add 10 possible choices to the
problem, and each learner views a set of five choices.

The answer pool must have at least one correct answer. It can have more than
one correct answer. In each set of choices shown to a learner, one correct
answer is included. For example, you can configure two correct answers in the
set of choices. One of the two correct answers is included in each set that a
learner views.

Use the Advanced Editor to Configure Answer Pools
**************************************************

You configure the problem to provide answer pools by editing the OLX for the
problem in the :ref:`advanced editor<Advanced Editor>`.

* In the ``<choicegroup>`` element, add the ``answer-pool`` attribute, with the
  numerical value indicating the number of answer options to show to learners.
  For example, ``<choicegroup answer-pool="4">``.

* If you include more than one correct answer among the options, for each
  correct answer add an ``explanation-id`` attribute with a unique value to the
  ``<choice>`` element: ``<choice correct="false" explanation-id="correct1">``.

* If you include more than one correct answer among the options, for each
  ``<solution>`` element, add an ``explanation-id`` attribute and a value that
  maps back to a specific correct answer. For example, ``<solution
  explanation-id="correct1">``.

* Place the ``<solution>`` elements within a ``<solutionset>`` element.

.. note:: If the choices include only one correct answer, you do not have to
 use the ``explanation-id`` in either the ``<choice>`` or ``<solution>``
 element. You do still use the ``<solutionset>`` element to wrap the
 ``<solution>`` element.

For example, for the following multiple choice problem, a learner will see
four choices. In each set, one of the choices will be one of the two correct
choices. The explanation shown for the correct answer is the one with the same
explanation ID.

.. code-block:: xml

  <problem>
    <multiplechoiceresponse>
      <label>What Apple devices let you carry your digital music library in your pocket?</label>
      <description>You can select only one option.</description>
      <choicegroup type="MultipleChoice" answer-pool="4">
        <choice correct="false">The iPad</choice>
        <choice correct="false">Napster</choice>
        <choice correct="true" explanation-id="iPod">The iPod</choice>
        <choice correct="false">The vegetable peeler</choice>
        <choice correct="false">The iMac</choice>
        <choice correct="true" explanation-id="iPhone">The iPhone</choice>
      </choicegroup>
      <solutionset>
        <solution explanation-id="iPod">
          <div class="detailed-solution">
            <p>Explanation</p>
            <p>The iPod is Apple's portable digital music player.</p>
          </div>
        </solution>
        <solution explanation-id="iPhone">
          <div class="detailed-solution">
            <p>Explanation</p>
            <p>In addition to being a cell phone, the iPhone can store and play
             your digital music.</p>
          </div>
        </solution>
      </solutionset>
    </multiplechoiceresponse>
  </problem>
