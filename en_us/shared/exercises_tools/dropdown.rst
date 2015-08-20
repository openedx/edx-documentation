.. _Dropdown:

#####################
Dropdown Problem
#####################

.. contents::
  :local:
  :depth: 1

**********
Overview
**********

Dropdown problems allow learners to choose from a collection of answer options
that are presented in a dropdown list. Unlike :ref:`multiple choice<Multiple
Choice>` problems, which have answers that are always visible directly below
the question, dropdown problems do not show answer choices until the learner
clicks the dropdown arrow.

.. image:: ../../../shared/building_and_running_chapters/Images/DropdownExample.png
 :alt: A problem component with 3 dropdown problems, 2 marked correct and 1
     incorrect.
 :width: 600

**************************************************
Analyzing Performance on Dropdown Problems
**************************************************

For the dropdown problems in your course, you can use edX Insights to review
aggregated learner performance data and examine submitted answers. For
more information, see `Using edX Insights`_.

********************************
Create a Dropdown Problem
********************************

You can create dropdown problems in the Simple Editor or in the Advanced
Editor. You can set up a problem in the Simple Editor, and then switch to the
Advanced Editor to add more configuration options in XML. However, you cannot
switch back to the Simple Editor from the Advanced Editor. Therefore, you
might want to format the problem as completely as possible before you begin to
use the Advanced Editor.
 
.. _Use the Simple Editor to Create a Dropdown Problem:

========================================================================
Use the Simple Editor to Create a Dropdown Problem
========================================================================

To use the :ref:`Simple Editor<Simple Editor>` to create a dropdown problem,
follow these steps.

#. In the unit where you want to create the problem, under **Add New
   Component** select **Problem**.
#. Select one of the two dropdown problem templates.
   
  * From the list of **Common Problem Types**, select **Dropdown**. 
   
  * From the list of **Common Problems with Hints and Feedback**, select
    **Dropdown with Hints and Feedback**. For more information, see `Use
    Feedback in a Dropdown Problem`_.

    Studio adds the problem to the unit.

3. Select **Edit**. The Simple Editor opens. 
#. Replace the sample problem text with your own text.
#. Determine the text that describes the question you want learners to answer,
   and surround that text with two pairs of angle brackets (``>>question<<``).
   This question text is the accessible label for the problem.
#. Edit your text to place all of the possible answers on the same line,
   separated by commas.
#. Select all of the answer options, and then select **Dropdown** from 
   the toolbar. A double set of brackets ([[ ]]) appears to surround
   the answer options.
#. To identify the problem's answer, locate that answer inside the brackets
   and surround the correct answer with parentheses.
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

    >>What type of data are the following?<<

    Age:
    [[Nominal, Discrete, (Continuous)]]
    Age, rounded to the nearest year:
    [[Nominal, (Discrete), Continuous]]
    Life stage - infant, child, and adult:
    [[(Nominal), Discrete, Continuous]]

========================================================================
Use the Advanced Editor to Edit a Dropdown Problem 
========================================================================

To use the Advanced Editor to edit a dropdown problem, follow these steps.

#. Follow the steps for creating the problem in the :ref:`Simple Editor<Use
   the Simple Editor to Create a Dropdown Problem>`. 
#. Select **Advanced Editor**, and then edit the XML to add the tags and
   attributes you want. An example follows.

**Problem Code**:

.. code-block:: xml

  <problem>
  <p>
    <em>This exercise first appeared in HarvardX's PH207x Health in Numbers: 
    Quantitative Methods in Clinical &amp; Public Health Research course, fall 
    2012.</em>
  </p>
  <p>What type of data are the following?</p>
  <p>Age:</p>
  <optionresponse>
    <optioninput options="('Nominal','Discrete','Continuous')" 
      correct="Continuous" label="Age"/>
  </optionresponse>
  <p>Age, rounded to the nearest year:</p>
  <optionresponse>
    <optioninput options="('Nominal','Discrete','Continuous')" 
      correct="Discrete" label="Age, rounded to the nearest year"/>
  </optionresponse>
  <p>Life stage - infant, child, and adult:</p>
  <optionresponse>
    <optioninput options="('Nominal','Discrete','Continuous')" 
      correct="Nominal" label="Life stage"/>
  </optionresponse>
  </problem>

.. _Use Feedback in a Dropdown Problem:

********************************************
Use Feedback in a Dropdown Problem
********************************************

You can add feedback in a dropdown problem using the simple editor
or the advanced editor. For an overview of feedback in problems, see
:ref:`Adding Feedback and Hints to a Problem`.

In dropdown problems, you can provide feedback for each option that a
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

In the :ref:`Simple Editor<Simple Editor>`, you configure answer feedback with
the following syntax. When you create a new dropdown problem, select the
template **Dropdown with Hints and Feedback**. This template has example
feedback syntax that you can replace.

::

  Wrong Answer {{Feedback for learners who select this answer.}}
  (Correct Answer) {{Feedback for learners who select this answer.}}

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

=========================================
Configure Feedback in the Advanced Editor
=========================================

In the :ref:`Advanced Editor<Advanced Editor>`, you configure answer feedback
with the following syntax.

.. code-block:: xml

    <option correct="False">
      Option Label
      <optionhint>
        Feedback for when learner selects this answer.
      </optionhint>
    </option>

For example, the following problem has feedback for each answer.

.. code-block:: xml

  <optionresponse>
    <optioninput label="A/an ________ is an example of a vegetable.">
      <option correct="False">
        apple 
        <optionhint>
          An apple is the fertilized ovary that comes from an apple tree and 
          contains seeds classifying it as a fruit.
        </optionhint>
      </option>
      <option correct="False">
        pumpkin
        <optionhint>
          A pumpkin is the fertilized ovary of a squash plant and contains 
          seeds classifying it as a fruit.
        </optionhint>
      </option>
      <option correct="True">
        potato 
        <optionhint>
          A potato is an edible part of a plant in tuber form and is 
          classified as a vegetable.
        </optionhint>
      </option>
      <option correct="False">
        tomato 
        <optionhint>
          Many people mistakenly think a tomato is a vegetable. However, 
          because a tomato is the fertilized ovary of a tomato plant and 
          contains seeds it is classified as a fruit.
        </optionhint>
      </option>
    </optioninput>
  </optionresponse>

=========================
Customize Feedback Labels
=========================

By default, the feedback labels shown to learners are **Correct** and
**Incorrect**. If you do not define feedback labels, learners see these terms
when they submit an answer, as in the following example.

.. image:: ../../../shared/building_and_running_chapters/Images/dropdown_feedback.png
 :alt: Image of multiple choice feedback with the standard label.
 :width: 600

You can configure the problem to override the default labels. For example, you
can configure a custom label for a specific wrong answer.

.. image:: ../../../shared/building_and_running_chapters/Images/dropdown_feedback_custom_label.png
 :alt: Image of multiple choice feedback with a custom label.
 :width: 600

.. note::
  The default labels **Correct** and **Incorrect** are displayed in the
  learner's requested language. If you provide custom labels, they are
  displayed to all users as you configure them and are not translated into
  different languages.

Customize Feedback Labels in the Simple Editor
***********************************************

In the :ref:`Simple Editor<Simple Editor>`, you configure custom feedback
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

In the :ref:`Advanced Editor<Advanced Editor>`, you configure custom feedback
labels with the following syntax.

.. code-block:: xml

   <option correct="False">
     Answer 
     <optionhint label="Custom Label">
       Feedback for learners who select this answer.
     </optionhint>
   </option>

For example, the following feedback is configured to use a custom label.

.. code-block:: xml

  <option correct="False">
    tomato 
    <optionhint label="Not Quite">
      Many people mistakenly think a tomato is a vegetable. However, because a 
      tomato is the fertilized ovary of a tomato plant and contains seeds it 
      is classified as a fruit.
    </optionhint>
  </option>

.. _Use Hints in a Dropdown Problem:

********************************************
Use Hints in a Dropdown Problem
********************************************

You can use hints in a dropdown problem, using the simple editor
or the advanced editor. For an overview of hints in problems, see
:ref:`Adding Feedback and Hints to a Problem`.

.. include:: ../../../shared/exercises_tools/Subsection_configure_hints.rst


*************************************************
Award Partial Credit in a Dropdown Problem
*************************************************

You can configure a dropdown problem so that specific incorrect answers award
learners partial credit for the problem. You must use the `Advanced Editor <Use
the Advanced Editor to Edit a Dropdown Problem>`_ to configure partial credit.

In the following example, the learner selected a wrong answer and received
partial credit.

.. image:: ../../../shared/building_and_running_chapters/Images/partial_credit_dropdown.png
 :alt: Image of a dropdown problem with partial credit for an incorrect
     answer.
 :width: 600

You can specify what percentage of the points for the problem a learner
receives for an incorrect answer. If you do not specify the percentage, the
default 50% is used.

For an overview of partial credit in problems, see
:ref:`Awarding Partial Credit for a Problem`.

=================================================================
Configure a Dropdown Problem to Award Partial Credit
=================================================================

To configure a dropdown problem to award partial credit for a specific
answer, you add the following attributes to the problem XML.

* Add the ``partial_credit="points"`` attribute to the
  ``<optionresponse>`` element.

* Add the ``partial`` attribute to the ``<optioninput>`` element. Add each
  answer that you intend to award partial credit as a value for the ``partial``
  attribute. Separate multiple values with a comma (,). For example,
  ``partial="China, Spain"`` indicates that two answers receive partial credit.

  .. Note:: 
    Each value of the ``partial`` attribute must match a value in the
    ``options`` attribute for the problem.

* Optionally, for each answer that you intend to award partial credit, add the
  percentage of the problem, as a decimal, in the ``point_values`` attribute
  for the ``<optioninput>`` element. Separate multiple values with a comma
  (,). 

  The percentage value is used for the answer in the same position in the
  ``partial`` attribute. 

  For example, if you added ``partial="China, Spain"`` and
  y``point_value="0.25, 0.75"`` then the answer "China" earns 25% of the
  points, and "Spain" earns 75% of the points. If you do not add the
  ``point_values`` attribute, 50% is used for all partial credit answers.

For example, the following XML shows the dropdown problem template updated to
provide partial 20% of the problem's points for learners who answer "China".

.. code-block:: xml

  <optionresponse partial_credit="points">
    <optioninput label="Which of the following countries celebrates its 
      independence on August 15?" 
      options="('India','Spain','China','Bermuda')" 
      correct="India"
      partial = "China" 
      point_values = "0.2" >
    </optioninput>
  </optionresponse>


.. _Dropdown Problem XML:

************************
Dropdown Problem XML
************************

========
Template
========

.. code-block:: xml

  <problem>
  <legend>Question text</legend>
  <optionresponse>
    <option correct="False">
      Option Label
      <optionhint>
        Feedback for when learner selects this answer.
      </optionhint>
    </option>
    <option correct="True">
      Option Label
      <optionhint>
        Feedback for when learner selects this answer.
      </optionhint>
    </option>
  </optionresponse>
  <demandhint>
    <hint>Hint 1</hint>
    <hint>Hint 2</hint>
    <hint>Hint 3</hint>
  </demandhint>
  <solution>
    <div class="detailed-solution">
      <p>Explanation or Solution Header</p>
      <p>Explanation or solution text</p>
    </div>
  </solution>
  </problem>

========
Tags
========

* ``<optionresponse>`` (required): Indicates that the problem is a dropdown
  problem.

* ``<option>`` (required): Lists an answer option.
  
* ``<demandhint>`` (optional): Specifies hints for the learner.


**Tag:** ``<optionresponse>``

Indicates that the problem is a dropdown problem.

  Attributes

  .. list-table::
     :widths: 20 80
     :header-rows: 1

     * - Attribute
       - Description
     * - partial_credit (optional)
       - Specifies that the problem can award partial credit.
     * - type (required)
       - If used, must be set to "points".


  Children

  ``<option>``  

**Tag:** ``<option>``

Lists the answer options.

  Attributes

  .. list-table::
     :widths: 20 80

     * - Attribute
       - Description
     * - correct (required)
       - Indicates whether an answer is correct. Possible values are "true"
         and "false". Only one **correct** attribute can be set to "true".
     * - partial (optional)
       - Indicates whether an answer receives partial credit. 
     * - point_value
       - When there are one or more partial answers, indicates the percentage,
         as a decimal, of the points the learner receives for selecting those
         option. If "point_value" is not specified for a partial credit answer,
         50% is used by default.
  
  Children

  ``<optionhint>``

**Tag:** ``<optionhint>``

Specifies a hint for the answer.

**Tag:** ``<demandhint>``

Specifies hints available to the learner.

  Children
  
  ``<hint>``

**Tag:** ``<hint>``

Specifies a hint available to the learner.

  Children
  
  (none)

.. _Using edX Insights: http://edx.readthedocs.org/projects/edx-insights/en/latest/
