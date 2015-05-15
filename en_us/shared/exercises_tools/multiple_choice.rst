.. _Multiple Choice:

########################
Multiple Choice Problem
########################

In multiple choice problems, learners select one option from a list of answer
options. Unlike :ref:`dropdown<Dropdown>` problems, whose answer choices
do not appear until the learner clicks the dropdown arrow, answer choices for
multiple choice problems are always visible directly below the question.

.. image:: ../../../shared/building_and_running_chapters/Images/MultipleChoiceExample.png
 :alt: Image of a multiple choice problem

For the multiple choice problems in your course, you can use edX Insights to
review aggregated learner performance data and examine the submitted answers.
For more information, see `Using edX Insights`_.

Multiple choice problems can also have several advanced options, such as
presenting a random set of choices to each learner. For more information about
these options, see :ref:`Multiple Choice Advanced Options`.

****************************************
Creating a Multiple Choice Problem
****************************************

You can create multiple choice problems in the Simple Editor or in the
Advanced Editor. You can set up a problem in the Simple Editor, and then
switch to the Advanced Editor to add more configuration options in XML.
However, you cannot switch back to the Simple Editor from the Advanced Editor.
Therefore, you might want to format the problem as completely as possible
before you begin to use the Advanced Editor.

.. _Use the Simple Editor to Create a Multiple Choice Problem:

================================================================
Use the Simple Editor to Create a Multiple Choice Problem
================================================================

To use the :ref:`Simple Editor<Simple Editor>` to create a checkbox problem,
follow these steps.

#. In the unit where you want to create the problem, under **Add New
   Component** select **Problem**.
#. From the list of **Common Problem Types**, select **Multiple Choice**.
   Studio adds an example multiple choice problem to the unit.
#. Select **Edit**. The Simple Editor opens. 
#. Replace the sample problem text with your own text.
#. Determine the text that describes the question you want learners to answer,
   and surround that text with two pairs of angle brackets (``>>question<<``).
   This question text is the accessible label for the problem.
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

For the example problem illustrated above, the following text displays in the
problem component.

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
    Horseshoe crabs were essential to the discovery of lateral inhibition,
    a property of vision present in horseshoe crabs as well as in humans that 
    enables enhancement of contrast at edges of objects as was demonstrated in class. 
    In 1967, Haldan Hartline received the Nobel prize for his research on vision 
    and in particular his research investigating lateral inhibition using 
    horseshoe crabs.
    [Explanation]


========================================================================
Use the Advanced Editor to Edit a Multiple Choice Problem 
========================================================================

To use the :ref:`Advanced Editor<Advanced Editor>` to edit a multiple choice
problem, follow these steps.

#. Follow the steps for creating the problem in the :ref:`Simple Editor<Use
   the Simple Editor to Create a Multiple Choice Problem>`.
#. Select **Advanced Editor**, and then edit the XML to add the tags and
   attributes you want. An example follows.

.. code-block:: xml

  <problem>
  <fieldset>
  <legend>Lateral inhibition, as was first discovered in the horseshoe crab...</legend>
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
  </fieldset>
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


.. _Multiple Choice Problem XML:

******************************
Multiple Choice Problem XML 
******************************

================
Template
================

.. code-block:: xml

  <problem>
  <fieldset>
  <legend>Question text</legend>
  <multiplechoiceresponse>
    <choicegroup type="MultipleChoice" label="label text">
      <choice correct="false" name="a">Incorrect choice</choice>
      <choice correct="true" name="b">Correct choice</choice>
    </choicegroup>
  </multiplechoiceresponse>
  </fieldset>

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

**Tag:** ``<multiplechoiceresponse>``

Indicates that the problem is a multiple choice problem.

  Attributes

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
       - Indicates a correct or incorrect answer. When the attribute is set to
         "true", the choice is a correct answer. When the attribute is set to
         "false", the choice is an incorrect answer. You can specify more than 
         one correct answer, but learners can select only once choice to submit
         as their answer.
     * - name
       - A unique name that the back end uses to refer to the choice.

  Children
  
  (none)

.. _Multiple Choice Advanced Options:

*********************************************
Advanced Options for Multiple Choice Problems
*********************************************

Multiple choice problems have several advanced options. You can change the
order of answers in the problem, include explanations that appear when a
learner selects a specific incorrect answer, or present a random set of
choices to each learner. For more information, see the following topics.

* :ref:`Shuffle Answers in a Multiple Choice Problem`
* :ref:`Targeted Feedback in a Multiple Choice Problem`
* :ref:`Answer Pools in a Multiple Choice Problem`

.. _Shuffle Answers in a Multiple Choice Problem:

=============================================
Shuffle Answers in a Multiple Choice Problem
=============================================

Optionally, you can configure a multiple choice problem so that it shuffles
the order of possible answers.

For example, one view of the problem could be:

.. image:: ../../../shared/building_and_running_chapters/Images/multiple-choice-shuffle-1.png
 :alt: Image of a multiple choice problem

And another view of the same problem, for another learner or for the same
learner of a subsequent view of the unit, could be:

.. image:: ../../../shared/building_and_running_chapters/Images/multiple-choice-shuffle-2.png
 :alt: Image of a multiple choice problem with shuffled answers

You can also have some answers shuffled, but not others. For example, you
might want to have the answer "All of the Above" always appear at the end of
the list, but shuffle other answers.

You can configure the problem to shuffle answers using the Simple Editor or
Advanced Editor.


Use the Simple Editor to Shuffle Answers
*********************************************

You can configure the problem to shuffle answers in :ref:`Simple Editor`.

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

Use the Advanced Editor to Shuffle Answers
*********************************************

You can configure the problem to shuffle answers by editing XML in the
:ref:`Advanced Editor`.

For example, the following XML defines a multiple choice problem before
shuffling is enabled.

.. code-block:: xml

 <problem>
  <fieldset>
  <legend>What Apple device competed with the portable CD player?</legend>
  <multiplechoiceresponse>
   <choicegroup type="MultipleChoice">
     <choice correct="false">The iPad</choice>
     <choice correct="false">Napster</choice>
     <choice correct="true">The iPod</choice>
     <choice correct="false">The vegetable peeler</choice>
   </choicegroup>
  </multiplechoiceresponse>
  </fieldset>
 </problem>


To add shuffling to this problem, add ``shuffle="true"`` to the
``<choicegroup>`` element.

.. code-block:: xml

 <problem>
  <fieldset>
  <legend>What Apple device competed with the portable CD player?</legend>
  <multiplechoiceresponse>
   <choicegroup type="MultipleChoice" shuffle="true">
     <choice correct="false">The iPad</choice>
     <choice correct="false">Napster</choice>
     <choice correct="true">The iPod</choice>
     <choice correct="false">The vegetable peeler</choice>
   </choicegroup>
  </multiplechoiceresponse>
  </fieldset>
</problem>

To fix an answer's location in the list, add ``fixed="true"`` to the
``choice`` element for the answer.

.. code-block:: xml

 <problem>
  <fieldset>
  <legend>What Apple device competed with the portable CD player?</legend>
  <multiplechoiceresponse>
   <choicegroup type="MultipleChoice" shuffle="true">
     <choice correct="false">The iPad</choice>
     <choice correct="false">Napster</choice>
     <choice correct="true">The iPod</choice>
     <choice correct="false">The vegetable peeler</choice>
     <choice correct="false" fixed="true">All of the above</choice>
   </choicegroup>
  </multiplechoiceresponse>
  </fieldset>
 </problem>

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
:ref:`Advanced Editor`.

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
   <fieldset>
   <legend>What Apple device competed with the portable CD player?</legend>
   <multiplechoiceresponse targeted-feedback="">
    <choicegroup type="MultipleChoice">
      <choice correct="false" explanation-id="feedback1">The iPad</choice>
      <choice correct="false" explanation-id="feedback2">Napster</choice>
      <choice correct="true" explanation-id="correct">The iPod</choice>
      <choice correct="false" explanation-id="feedback3">The vegetable peeler</choice>
    </choicegroup>
   </fieldset>
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

The answer pool must have at least one correct answer. It can have more than one
correct answer. In each set of choices shown to a learner, one correct answer is
included. For example, you can configure two correct answers in the set of
choices. One of the two correct answers is included in each set that a learner
views.

Use the Advanced Editor to Configure Answer Pools
**************************************************

You configure the problem to provide answer pools by editing XML in the 
:ref:`Advanced Editor`.

Follow these XML guidelines:

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
  <fieldset>
  <legend>What Apple devices let you carry your digital music library in your pocket?</legend>
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
  </fieldset>

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



.. _Using edX Insights: http://edx.readthedocs.org/projects/edx-insights/en/latest/
