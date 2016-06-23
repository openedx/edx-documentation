.. _Multiple Choice:

########################
Multiple Choice Problem
########################

.. note:: EdX offers full support for this problem type.

.. contents::
  :local:
  :depth: 1

**********
Overview
**********

In multiple choice problems, learners select one option from a list of answer
options. Unlike :ref:`dropdown<Dropdown>` problems, whose answer choices
do not appear until the learner clicks the dropdown arrow, answer choices for
multiple choice problems are always visible directly below the question.

.. image:: ../../../shared/images/MultipleChoiceExample.png
 :alt: A multiple choice problem.
 :width: 600

Multiple choice problems can also have several advanced options, such as
presenting a random set of choices to each learner. For more information about
these options, see :ref:`Multiple Choice Advanced Options`.

**************************************************
Analyzing Performance on Multiple Choice Problems
**************************************************

For the multiple choice problems in your course, you can use edX Insights to
review aggregated learner performance data and examine the submitted answers.
For more information, see :ref:`insights:Using edX Insights`.

********************************************************
Pedagogical Considerations for Multiple Choice Questions
********************************************************

EdX recommends the use, whenever possible, of authentic assessments rather than
multiple choice questions for graded problems. Authentic assessments in online
courses tend to lead to better learning outcomes. In addition, authentic
assessments allow for infinite attempts, mastery learning, and more
intellectual risk taking, which lead to substantially better learning outcomes.

Multiple choice questions do have these helpful uses.

* Ungraded multiple choice questions can help students think about a concept in
  the context of knowledge transfer.

* For many subject areas, authentic assessments are either unavailable or
  prohibitively complex to use. In such courses, multiple choice questions can
  act as the only available fallback.

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
Creating a Multiple Choice Problem
****************************************

You can create multiple choice problems in the simple editor or in the
advanced editor. You can set up a problem in the simple editor, and then
switch to the advanced editor to add more configuration options in XML.
However, you cannot switch back to the simple editor from the advanced editor.
Therefore, you might want to format the problem as completely as possible
before you begin to use the advanced editor.

.. _Use the Simple Editor to Create a Multiple Choice Problem:

================================================================
Use the Simple Editor to Create a Multiple Choice Problem
================================================================

To use the :ref:`simple editor<Simple Editor>` to create a checkbox problem,
follow these steps.

#. In the unit where you want to create the problem, under **Add New
   Component** select **Problem**.
#. Select one of the two multiple choice problem templates.

  * From the list of **Common Problem Types**, select **Multiple Choice**.

  * From the list of **Common Problems with Hints and Feedback**, select
    **Multiple Choice with Hints and Feedback**. For more information, see `Use
    Feedback in a Multiple Choice Problem`_.

    Studio adds the problem to the unit.

#. Select **Edit**. The simple editor opens.
#. Replace the sample problem text with your own text.
#. Determine the text that describes the question you want learners to answer,
   and surround that text with two pairs of angle brackets (``>>question<<``).
   This text identifies the question for screen readers, reports, and Insights.
#. Edit your text to place each answer option on a separate line.
#. Select your set of answer options, and then select **Multiple Choice** from
   the toolbar. A pair of parentheses appears next to each answer choice.
#. To identify the correct answer, add an **x** between the parentheses for
   that option.
#. To provide an explanation, select the explanation text and then select
   **Explanation** from the toolbar. ``[explanation]`` appears before
   and after the explanation text.
#. Select **Settings** and provide an identifying **Display Name** for the
   problem.
#. Define additional settings for the problem. For more information, see
   :ref:`Problem Settings`.
#. Select **Save**.

For the example problem illustrated above, the following text is displayed in
the problem component.

::

    >>Lateral inhibition, as was first discovered in the horsehoe crab:<<

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

========================================================================
Use the Advanced Editor to Edit a Multiple Choice Problem
========================================================================

To use the :ref:`advanced editor<Advanced Editor>` to edit a multiple choice
problem, follow these steps.

#. Follow the steps for creating the problem in the :ref:`simple editor<Use
   the Simple Editor to Create a Multiple Choice Problem>`.
#. Select **Advanced Editor**, and then edit the XML to add the tags and
   attributes you want. An example follows.

.. code-block:: xml

  <problem>
  <p>Lateral inhibition, as was first discovered in the horseshoe crab...</p>
  <multiplechoiceresponse>
    <choicegroup type="MultipleChoice" label="Lateral inhibition, as was first discovered
      in the horseshoe crab">
      <choice correct="false">is a property of touch sensation, referring to the ability
      of crabs to detect nearby predators.</choice>
      <choice correct="false">is a property of hearing, referring to the ability of crabs
      to detect low frequency noises.</choice>
      <choice correct="false">is a property of vision, referring to the ability of crabs'
      eyes to enhance contrasts.</choice>
      <choice correct="true">has to do with the ability of crabs to use sonar to detect
      fellow horseshoe crabs nearby.</choice>
      <choice correct="false">has to do with a weighting system in the crab's skeleton
      that allows it to balance in turbulent water.</choice>
    </choicegroup>
  </multiplechoiceresponse>
  <solution>
    <div class="detailed-solution">
      <p>Explanation</p>
      <p>Horseshoe crabs were essential to the discovery of lateral inhibition,
       a property of vision present in horseshoe crabs as well as humans that
       enables enhancement of contrast at edges of objects as was demonstrated in class.
       In 1967, Haldan Hartline received the Nobel prize for his research on vision
       and in particular his research investigating lateral inhibition using
       horseshoe crabs.</p>
    </div>
  </solution>
  </problem>

.. _Use Feedback in a Multiple Choice Problem:

********************************************
Using Feedback in a Multiple Choice Problem
********************************************

You can add feedback in a multiple choice problem using the simple editor
or the advanced editor. For an overview of feedback in problems, see
:ref:`Adding Feedback and Hints to a Problem`.

In multiple choice problems, you can provide feedback for each option that a
learner can select. Use the following guidelines when providing feedback.

* Use feedback for the incorrect answers to target common misperceptions and
  mistakes.

* Ensure feedback provides some guidance to the learner about how to arrive at
  the correct answer.

* Use feedback for the correct answer as an opportunity to reinforce why the
  answer is correct. Because learners are able to guess, ensure that feedback
  provides a reason why the answer is correct for learners who might have
  selected that answer by chance.

=======================================
Configure Feedback in the Simple Editor
=======================================

In the :ref:`simple editor<Simple Editor>`, you configure answer feedback with
the following syntax.  When you create a new multiple choice problem, select
the template **Multiple Choice with Hints and Feedback**. This template has
example feedback syntax that you can replace.

::

  ( ) Answer {{Feedback for learners who select this answer.}}

For example, the following problem has feedback for each possible answer.

::

  >>Which of the following is an example of a vegetable?<<
  ( ) apple {{An apple is the fertilized ovary that comes from an apple tree
  and contains seeds classifying it as a fruit.}}
  ( ) pumpkin {{A pumpkin is the fertilized ovary of a squash plant and
  contains seeds classifying it as a fruit.}}
  (x) potato {{A potato is an edible part of a plant in tuber form and is
  classified as a vegetable}}
  ( ) tomato {{Many people mistakenly think a tomato is a vegetable. However,
  because a tomato is the fertilized ovary of a tomato plant and contains
  seeds it is classified as a fruit.}}

=========================================
Configure Feedback in the Advanced Editor
=========================================

In the :ref:`advanced editor<Advanced Editor>`, you configure answer feedback
with the following syntax.

.. code-block:: xml

    <choice correct="false">
      Choice Label
      <choicehint>
        Feedback for when learner selects this answer.
      </choicehint>
    </choice>

For example, the following problem has feedback for each answer.

.. code-block:: xml

  <multiplechoiceresponse>
    <choicegroup label="Which of the following is an example of a vegetable?"
      type="MultipleChoice">
      <choice correct="false">apple
        <choicehint>An apple is the fertilized
          ovary that comes from an apple tree and contains seeds classifying
          it as a fruit.
        </choicehint>
      </choice>
      <choice correct="false">pumpkin
        <choicehint>A pumpkin is the fertilized
          ovary of a squash plant and contains seeds classifying it as a fruit.
        </choicehint>
      </choice>
      <choice correct="true">potato
        <choicehint>A potato is an edible part of a plant in tuber form and is
          classified as a vegetable.
        </choicehint>
      </choice>
      <choice correct="false">tomato
        <choicehint>Many people mistakenly think a tomato is a vegetable.
         However, because a tomato is the fertilized ovary of a tomato plant
         and contains seeds it is classified as a fruit.
        </choicehint>
      </choice>
    </choicegroup>
  </multiplechoiceresponse>

=========================
Customize Feedback Labels
=========================

By default, the feedback labels shown to learners are **Correct** and
**Incorrect**. If you do not define feedback labels, learners see these terms
when they submit an answer, as in the following example.

.. image:: ../../../shared/images/multiple_choice_feedback.png
 :alt: Multiple choice feedback with the standard label.
 :width: 600

You can configure the problem to override the default labels. For example, you
can configure a custom label for a specific wrong answer.

.. image:: ../../../shared/images/multiple_choice_feedback_custom_label.png
 :alt: Multiple choice feedback with a custom label.
 :width: 600

.. note::
  The default labels **Correct** and **Incorrect** are displayed in the
  learner's requested language. If you provide custom labels, they are
  displayed to all users as you configure them and are not translated into
  different languages.

Customize Feedback Labels in the Simple Editor
***********************************************

In the :ref:`simple editor<Simple Editor>`, you configure custom feedback
labels with the following syntax.

::

  ( ) Answer {{Label:: Feedback for learners who select this answer.}}

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

    <choice correct="true or fale">Answer
      <choicehint label="Custom Label">
        Feedback for learners who select this answer.
      </choicehint>
    </choice>

For example, the following feedback is configured to use a custom label.

.. code-block:: xml

  <choice correct="false">
    tomato
    <choicehint label="Not Quite">
      Many people mistakenly think a tomato is a vegetable. However, because
      a tomato is the fertilized ovary of a tomato plant and contains seeds,
      it is a fruit.
    </choicehint>
  </choice>

.. _Use Hints in a Multiple Choice Problem:

********************************************
Using Hints in a Multiple Choice Problem
********************************************

You can add hints in a multiple choice problem, using the simple editor
or the advanced editor. For an overview of hints in problems, see
:ref:`Adding Feedback and Hints to a Problem`.

.. include:: ../../../shared/exercises_tools/Subsection_configure_hints.rst

.. _Awarding Partial Credit in a Multiple Choice Problem:

****************************************************
Awarding Partial Credit in a Multiple Choice Problem
****************************************************

You can configure a multiple choice problem so that specific incorrect answers
award learners partial credit for the problem. You must use the `advanced
editor <Use the Advanced Editor to Edit a Multiple Choice Problem>`_ to
configure partial credit.

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
answer, you add the following attributes to the problem XML.

* Add the ``partial_credit="points"`` attribute to the
  ``<multiplechoiceresponse>`` element.

* For each answer that you intend to award partial credit, add the
  ``correct="partial"`` attribute to the ``<choice>`` element.

* Optionally, define the percentage of the problem score to award for each
  answer. In the ``point_values`` attribute for the ``<choice>`` element, enter
  the value as a decimal. For example, you can add ``point_value="0.25"`` to
  award 25% of the points to learners who select that answer. The percentage
  awarded should reflect how close the learner has gotten to a full
  understanding of the concept. If you do not add the ``point_value``
  attribute, the system uses a value of 50%.

For example, the following XML shows the multiple choice problem template
updated to provide partial credit for the first answer.

.. code-block:: xml

  <multiplechoiceresponse partial_credit="points">
    <choicegroup label="Which of the following countries has the largest
        population?" type="MultipleChoice">
      <choice correct="partial" point_value="0.25">Brazil</choice>
      <choice correct="false">Germany</choice>
      <choice correct="true">Indonesia</choice>
      <choice correct="false">Russia</choice>
    </choicegroup>
  </multiplechoiceresponse>


.. _Multiple Choice Problem XML:

******************************
Multiple Choice Problem XML
******************************

================
Template
================

.. code-block:: xml

  <problem>
  <p>Question text</p>
  <multiplechoiceresponse>
    <choicegroup type="MultipleChoice" label="label text">
      <choice correct="false" name="a">
        Incorrect choice
        <choicehint>
          Hint for incorrect choice.
        </choicehint>
      </choice>
      <choice correct="true" name="b">
        Correct choice
        <choicehint>
          Hint for correct choice.
        </choicehint>
      </choice>
    </choicegroup>
  </multiplechoiceresponse>
  <demandhint>
    <hint>Hint 1</hint>
    <hint>Hint 2</hint>
  </demandhint>

  <solution>
    <div class="detailed-solution">
    <p>Explanation or solution header</p>
    <p>Explanation or solution text</p>
    </div>
  </solution>
  </problem>

================
Tags
================

* ``<multiplechoiceresponse>`` (required): Indicates that the problem is a
  multiple choice problem.

* ``<choicegroup>`` (required): Indicates the beginning of the list of
  options.

* ``<choice>`` (required): Lists an answer option.

* ``<demandhint>`` (optional): Specifies hints for the learner.

**Tag:** ``<multiplechoiceresponse>``

Indicates that the problem is a multiple choice problem.

  Attributes

  .. list-table::
     :widths: 20 80
     :header-rows: 1

     * - Attribute
       - Description
     * - partial_credit (optional)
       - Specifies that the problem can award partial credit. If used, must be
         set to "points".

  (none)

  Children

  * ``<choicegroup>``
  * All standard HTML tags (can be used to format text).

**Tag:** ``<choicegroup>``

Indicates the beginning of the list of options.

  Attributes

  .. list-table::
     :widths: 20 80
     :header-rows: 1

     * - Attribute
       - Description
     * - label (required)
       - Specifies the name of the response field.
     * - type (required)
       - Must be set to "MultipleChoice".

  Children

  * ``<choice>``

**Tag:** ``<choice>``

Lists an answer option.

  Attributes

  .. list-table::
     :widths: 20 80
     :header-rows: 1

     * - Attribute
       - Description
     * - correct (at least one required)
       - Indicates a correct, incorrect, or partially correct answer.

         * When set to "true", the choice is a correct answer.
         * When set to "false", the choice is an incorrect answer.
         * When set to "partial", the learner receives partial credit for
           selecting the answer.

         You can specify more than one correct or partially correct answer,
         but learners can select only once choice to submit as their answer.

     * - point_value
       - When ``correct="partial"``, indicates the percentage, as a decimal, of
         the points the learner receives for selecting this option. If
         ``point_value`` is not specified for a partial credit answer, 50% is
         used by default.
     * - name
       - A unique name that is used internally to refer to the choice.

  Children

  ``<choicehint>``

**Tag:** ``<choicehint>``

Specifies a hint for the answer.

**Tag:** ``<demandhint>``

Specifies hints available to the learner.

  Children

  ``<hint>``

**Tag:** ``<hint>``

Specifies a hint available to the learner.

  Children

  (none)

.. _Multiple Choice Advanced Options:

*********************************************
Advanced Options for Multiple Choice Problems
*********************************************

Multiple choice problems have several advanced options. You can change the
order of answers in the problem, include explanations that appear when a
learner selects a specific incorrect answer, or present a random set of
choices to each learner. For more information, see the following sections.

* :ref:`Shuffle Answers in a Multiple Choice Problem`
* :ref:`Targeted Feedback in a Multiple Choice Problem`
* :ref:`Answer Pools in a Multiple Choice Problem`

.. _Shuffle Answers in a Multiple Choice Problem:

=============================================
Shuffle Answers in a Multiple Choice Problem
=============================================

Optionally, you can configure a multiple choice problem so that it shuffles
the order of possible answers.

For example, one view of a geography problem could be as follows.

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

You can also have some answers shuffled, but not others. For example, you might
want to include the answer "All of the Above" and have it always appear at the
end of the list, but shuffle the other answers.

You can configure the problem to shuffle answers using the simple editor or
advanced editor. To shuffle the answers, you also edit the problem to set
**Randomization** to a value other than **Never**. For more information, see
:ref:`Randomization`.

Use the Simple Editor to Shuffle Answers
*********************************************

You can configure the problem to shuffle answers in the
:ref:`simple editor<Simple Editor>`.

For example, the following text defines a multiple choice problem before
shuffling is enabled. The ``(x)`` indicates the correct answer.

::

 >>What Apple device competed with the portable CD player?<<
     ( ) The iPad
     ( ) Napster
     (x) The iPod
     ( ) The vegetable peeler

To add shuffling to this problem, add ``!`` between the parentheses of the
first answer.

::

 >>What Apple device competed with the portable CD player?<<
     (!) The iPad
     ( ) Napster
     (x) The iPod
     ( ) The vegetable peeler

To fix an answer's location in a shuffled list, add ``@`` between the
parentheses of that answer.

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

When you complete problem setup in the simple editor, select **Edit** and then
**Settings** to specify an option other than **Never** for the
**Randomization** setting.

Use the Advanced Editor to Shuffle Answers
*********************************************

You can configure the problem to shuffle answers by editing XML in the
:ref:`advanced editor<Advanced Editor>`.

For example, the following XML defines a multiple choice problem before
shuffling is enabled.

.. code-block:: xml

 <problem>
  <p>What Apple device competed with the portable CD player?</p>
  <multiplechoiceresponse>
   <choicegroup type="MultipleChoice">
     <choice correct="false">The iPad</choice>
     <choice correct="false">Napster</choice>
     <choice correct="true">The iPod</choice>
     <choice correct="false">The vegetable peeler</choice>
   </choicegroup>
  </multiplechoiceresponse>
 </problem>


To add shuffling to this problem, add ``shuffle="true"`` to the
``<choicegroup>`` element.

.. code-block:: xml

 <problem>
  <p>What Apple device competed with the portable CD player?</p>
  <multiplechoiceresponse>
   <choicegroup type="MultipleChoice" shuffle="true">
     <choice correct="false">The iPad</choice>
     <choice correct="false">Napster</choice>
     <choice correct="true">The iPod</choice>
     <choice correct="false">The vegetable peeler</choice>
   </choicegroup>
  </multiplechoiceresponse>
 </problem>


To fix an answer's location in the list, add ``fixed="true"`` to the
``choice`` element for the answer.

.. code-block:: xml

 <problem rerandomize="always">
  <p>What Apple device competed with the portable CD player?</p>
  <multiplechoiceresponse>
   <choicegroup type="MultipleChoice" shuffle="true">
     <choice correct="false">The iPad</choice>
     <choice correct="false">Napster</choice>
     <choice correct="true">The iPod</choice>
     <choice correct="false">The vegetable peeler</choice>
     <choice correct="false" fixed="true">All of the above</choice>
   </choicegroup>
  </multiplechoiceresponse>
 </problem>

You can set value randomization as an attribute of the ``problem`` element, as
shown in this example, or select **Edit** and then **Settings** to specify an
option other than **Never** for the **Randomization** setting.

.. _Targeted Feedback in a Multiple Choice Problem:

===============================================
Targeted Feedback in a Multiple Choice Problem
===============================================

You can configure a multiple choice problem so that explanations for incorrect
answers are automatically shown to learners. You can use these explanations to
guide learners towards the right answer. Therefore, targeted feedback is most
useful for multiple choice problems for which learners are allowed multiple
attempts.


Use the Advanced Editor to Configure Targeted Feedback
********************************************************

You configure the problem to provide targeted feedback by editing XML in the
:ref:`advanced editor<Advanced Editor>`.

Follow these XML guidelines.

* Add a ``targeted-feedback`` attribute to the ``<multiplechoiceresponse>``
  element, with no value: ``<multiplechoiceresponse targeted-feedback="">``.
* Add a ``<targetedfeedbackset>`` element before the ``<solution>`` element.
* Within ``<targetedfeedbackset>``, add one or more ``<targetedfeedback>``
  elements.
* Within each ``<targetedfeedback>`` element, enter your explanation for the
  incorrect answer in HTML as markup described below.
* Connect the ``<targetedfeedback>`` element with a specific incorrect answer
  by using the same ``explanation-id`` attribute value for each.
* Use the ``<solution>`` element for the correct answer, with the same
  ``explanation-id`` attribute value as the correct ``<choice>`` element.

For example, the XML for the multiple choice problem follows.

.. code-block:: xml

   <problem>
   <p>What Apple device competed with the portable CD player?</p>
   <multiplechoiceresponse targeted-feedback="">
    <choicegroup type="MultipleChoice">
      <choice correct="false" explanation-id="feedback1">The iPad</choice>
      <choice correct="false" explanation-id="feedback2">Napster</choice>
      <choice correct="true" explanation-id="correct">The iPod</choice>
      <choice correct="false" explanation-id="feedback3">The vegetable peeler</choice>
    </choicegroup>
   </multiplechoiceresponse>
   ...

This is followed by XML that defines the targeted feedback.

.. code-block:: xml

   ...
   <targetedfeedbackset>
     <targetedfeedback explanation-id="feedback1">
       <div class="detailed-targeted-feedback">
         <p>Targeted Feedback</p>
         <p>The iPad came out later and did not directly compete with portable
            CD players.</p>
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

    <solution explanation-id="correct">
     <div class="detailed-solution">
      <p>The iPod directly competed with portable CD players.</p>
     </div>
    </solution>
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

You configure the problem to provide answer pools by editing XML in the
:ref:`advanced editor<Advanced Editor>`.

Follow these XML guidelines.

* In the ``<choicegroup>`` element, add the ``answer-pool`` attribute, with
  the numerical value indicating the number of possible answers in the set.
  For example, ``<choicegroup answer-pool="4">``.

* For each correct answer, to the ``<choice>`` element, add an ``explanation-
  id`` attribute and value that maps to a solution. For example, ``<choice
  correct="true" explanation-id="iPod">The iPod</choice>``.

* For each ``<solution>`` element, add an ``explanation-id`` attribute and
  value that maps back to a correct answer. For example, ``<solution
  explanation-id="iPod">``.

.. note:: If the choices include only one correct answer, you do not have to
 use the ``explanation-id`` in either the ``choice`` or ``<solution>``
 element. You do still use the ``<solutionset>`` element to wrap the
 ``<solution>`` element.

For example, for the following multiple choice problem, a learner will see
four choices. In each set, one of the choices will be one of the two correct
choices. The explanation shown for the correct answer is the one with the same
explanation ID.

.. code-block:: xml

 <problem>
  <p>What Apple devices let you carry your digital music library in your pocket?</p>
   <multiplechoiceresponse>
    <choicegroup type="MultipleChoice" answer-pool="4">
      <choice correct="false">The iPad</choice>
      <choice correct="false">Napster</choice>
      <choice correct="true" explanation-id="iPod">The iPod</choice>
      <choice correct="false">The vegetable peeler</choice>
      <choice correct="false">The iMac</choice>
      <choice correct="true" explanation-id="iPhone">The iPhone</choice>
    </choicegroup>
   </multiplechoiceresponse>

    <solutionset>
        <solution explanation-id="iPod">
        <div class="detailed-solution">
            <p>Explanation</p>
            <p>Yes, the iPod is Apple's portable digital music player.</p>
        </div>
        </solution>
        <solution explanation-id="iPhone">
        <div class="detailed-solution">
            <p>Explanation</p>
            <p>In addition to being a cell phone, the iPhone can store and play your
               digital music.</p>
        </div>
        </solution>
    </solutionset>
 </problem>


