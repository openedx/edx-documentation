.. _Working with Problem Components:

################################
Working with Problem Components
################################

This section introduces the core set of problem types that course teams can add
to any course by using the problem component. It also describes editing options
and settings for problem components.

.. contents::
 :local:
 :depth: 1

For information about specific problem types, and the other exercises and tools
that you can add to your course, see :ref:`Create Exercises`.

.. _Adding a Problem:

****************
Adding a Problem
****************

To add interactive problems to a course in Studio, in the course outline, at
the :ref:`unit<The Unit Workflow>` level, you select **Problem**. You then
choose the type of problem that you want to build on the Problem Type Selection
page.

The simple problem types include relatively straightforward CAPA problems such
as single select and text or numeric input. The advanced problem types can be
more complex to set up, such as math expression input, open response
assessment, or custom JavaScript problems.

=====================================
Adding Graded or Ungraded Problems
=====================================

When you :ref:`establish the grading policy<Grading Index>` for your course,
you define the assignment types that count toward learners' grades: for
example, homework, labs, midterm, final, and participation. You specify
one of these assignment types for each of the subsections in your course.

As you develop your course, you can add problem components to a unit in any
subsection. The problem components that you add automatically inherit the
assignment type that is defined at the subsection level. For example, all of
the problem components that you add to a unit in the midterm
subsection are graded.

For more information, see :ref:`Set the Assignment Type and Due Date for a
Subsection`.

.. _Problem Learner View:

.. include:: ../../../shared/course_components/Section_learner_problem_view.rst

.. _Problem Studio View:

*****************************
Editing a Problem in Studio
*****************************

When you select **Problem**, Studio adds a blank problem to the unit and brings
you to the problem editor. From here, you can select 1 of 5 **simple problem
types** or select Advanced problem types for a list of **advanced problem types**.

* For simple problem types, the :ref:`simple editor<Simple Editor>` opens. In
  this editor, you can quickly create problems with question and answer formats.
  Options for scoring, hints, feedback and more can be entered.

* For advanced problem types, the :ref:`advanced editor<Advanced Editor>` opens.
  In this editor you use :ref:`open learning XML (OLX)<edX Open Learning XML Guide>`
  elements and attributes to identify the elements of the problem. Options for scoring,
  feedback and more can be entered.

* For open response assessment problem types, you define the problem elements and
  options by using a graphical user interface. For more information, see
  :ref:`PA Create an ORA Assignment`.

* For drag and drop problem types, you build an interactive assessment in a
  customized interface in which you define areas that learners can drag into target
  zones on a background image. For more information, see
  :ref:`creating_a_drag_and_drop_problem`.

You can switch from the simple editor to the advanced editor at any time by
selecting the **Switch to advanced editor** from the simple editor's settings.

.. note::
 After you save a problem in the advanced editor with complex OLX, you may not
 be able to open it again in the simple editor.

.. _Simple Editor:

==================
The Simple Editor
==================

When you select one of the **simple problem types**, you will be directed to
the simple editor.

*  :ref:`Single Select<Single Select>`

*  :ref:`Multi-select<Multi-select>`

*  :ref:`Dropdown<Dropdown>`

*  :ref:`Numerical Input<Numerical Input>`

*  :ref:`Text Input<Text Input>`

.. _Question and Explanation Fields:

================================
Question and Explanation Fields
================================

The question and explanation fields (and other text fields as well) offer a
number of formatting tools to craft your problem.

.. image:: ../../../shared/images/problem_editor_question_box.png
 :alt: an image of the Problem Editor toolbar and a number associated with 
  each icon in the toolbar.
 :width: 800

#. **Undo/Redo**: Undo or redo changes made to the text field.

#. **HTML Tags**: Applies HTML tags to the selected block of text.

#. **Label**: Applies a “Question” label to the selected text which is picked
   up by screen readers. Screen readers read all of the text that you supply
   for the problem, and then repeat the text that is identified by this label
   immediately before reading the answer choices for the problem. This label
   can be removed by selecting the block of text and clicking this button
   again.

#. **Formatting**: Applies various formatting to the selected text such as
   bold, italicize, underline, color, text alignment, bullet points and
   indentation.

#. **Add Image and Links**: Allows you to add images and links to your text
   field.

#. **Blockquote and Code**: Applies blockquote or code formatting to the
   selected text. This can be removed by selecting the text and clicking this
   button again.

#. **Various Inserts**: Insert tables, emoticons, special characters and page
   breaks using these buttons.

#. **Clear Formatting**: Clears all formatting applied to the selected text.

#. **Accessibility Checker**: allows you to check HTML in the editor for 
   various accessibility problems.

#. **More**: Depending on page size, some of the toolbar may not show. Click
   this button to expand or shrink the toolbar.

The explanation field is almost identical to the question field, only missing
the Label button for marking questions.

.. _Answer Fields:

==============
Answer Fields
==============

Enter your answers below in this section. While what you see below is the
general layout of the answer fields, there are some minor differences between
problem types.

.. image:: ../../../shared/images/problem_editor_answer_box.png
 :alt: An example answer field in the simple editor.
 :width: 600

#. **Correct Answer**: The selected or checked answer(s) are the correct answers.
   Due to the nature of dropdowns only allowing a single selection, the dropdown
   problem type has radio buttons which allow you to select only one correct
   answer. As you cannot enter incorrect answers for numeric input problems,
   the numeric input problem type automatically comes with checked answers.
   The other problem types allow you to select any number of correct answers.

#. **Answer Feedback**: Opens up the feedback panel for an answer option. For
   more information, see the following **Adding Feedback** section.

#. **Delete Answer**: Removes the corresponding line of answer buttons and
   fields.

#. **Add Answer**: Adds a new line of answer buttons and fields.

.. _Adding Feedback:

================
Adding Feedback
================

You can add feedback that displays to learners after they submit an answer.

For example, the following single select problem provides feedback in
response to the selected option when the learner selects **Submit**. In this
case, feedback is given for an incorrect answer.

.. image:: ../../../shared/images/multiple_choice_feedback.png
 :alt: Image of a single select problem with feedback.
 :width: 600

While editing a problem block, you can apply **Answer-specific feedback**
for all problem types. **Group feedback** can only be applied to 
**multi-select** problems.

**Answer-specific feedback** can be added under each answer by pressing
the feedback icon to the right of the answer text. Feedback entered in
these fields are given when the learner selects that answer or when the
learner does not select that answer.

.. image:: ../../../shared/images/problem_editor_feedback_box.png
 :alt: Image of the answer-specific feedback settings.
 :width: 600

.. note::
   The “is not selected” feedback field shown above is only available
   for the **multi-select** problem type.

**Group Feedback** can be found on the collapsible settings to the right of
the problem editor. Feedback entered in this field will display if and
only if the learner selects all of the checked answers. Click the 
**Add group feedback** button to add additional feedback for different
groups of checked answers. **Group feedback** can only be applied for
the **multi-select** problem type.

.. image:: ../../../shared/images/problem_editor_group_feedback_box.png
 :alt: Image of the group feedback settings.
 :width: 300

.. note::
   Feedback for incorrect answers in the **numerical input** problem type
   is not supported.

---------------------------------------------
Best Practices for Providing Feedback
---------------------------------------------

The immediacy of the feedback available to learners is a key advantage of
online instruction and difficult to do in a traditional classroom environment.

You can target feedback for common incorrect answers to the misconceptions that
are common for the level of the learner (for example, elementary, middle, high
school, college).

In addition, you can create feedback that provides some guidance to the learner
about how to arrive at the correct answer. This is especially important in text
input problems, because without such guidance, learners might
not be able to proceed.

You should also include feedback for the correct answer to reinforce why the
answer is correct. Especially in questions where learners are able to guess,
such as single select and dropdown problems, the feedback should provide a
reason why the selection is correct.

.. _Adding Mathematics:

===================
Adding Mathematics
===================

To add mathematics, you can use LaTeX, MathML, or AsciiMath notation. Studio
uses MathJax to render equations. For more information, see :ref:`MathJax in
Studio`.

============
Power Paste
============

Many course authoring teams rely on copying and pasting content from documents 
such as Google docs or Microsoft Word. Correct formatting in Studio and the LMS 
can be most easily realized through Power Paste. To learn how to use Power 
Paste, see :ref:`Power Paste`.

.. _Problem Settings:

****************************************
Defining Settings for Problem Components
****************************************

In addition to the text of the problem and its formatting or OLX
markup, you define the following settings for problem components. To access
these settings, edit the problem. With the exception of **Display Name**,
you can find all of these settings on the right side of your problem. Click
on **Show advanced settings** to view additional options such as
**Show Answer**, **Show reset option** and **Time between attempts**.

.. contents::
  :local:
  :depth: 2

If you do not edit these settings, default values are supplied for your
problems.

.. note::
  If you want to temporarily or permanently hide problem results from learners,
  you use the subsection-level **Results Visibility** setting. You cannot
  change the visibility of individual problems. For more information,
  see :ref:`Problem Results Visibility`.

=============
Display Name
=============

This required setting provides an identifying name for the problem. The display
name appears as a heading above the problem in the LMS, and it identifies the
problem for you in Insights. Be sure to add unique, descriptive display names
so that you, and your learners, can identify specific problems quickly and
accurately.

You can find the display name setting at the top of your problem. To edit,
click the pen symbol to the right of the field and enter the desired text.

The following illustration shows the display name of a problem in Studio, in
the LMS, and in Insights.

.. image:: ../../../shared/images/display_names_problem.png
 :alt: The identifying display name for a problem in Studio, the LMS, and
     Insights.
 :width: 800

For more information about metrics for your course's problem components, see
`Using edX Insights`_.

.. _Problem Type:

========
Type
========

You can change the problem type after your initial selection. The current
problem type is shown with a check mark. Selecting any other problem type will
change your problem to that type while carrying over the content you have already
prepared. Please check your selection for correct answers as these may not carry
over when changing problem types.

.. note:: If you would like to convert your problem into an advanced problem,
  scroll down to the bottom of the settings, click **Show advanced settings**
  and then click **Switch to advanced editor**.

.. _Problem Scoring:

==========
Scoring
==========

These settings allow you to change the amount of points your problem is worth
and the number of attempts a student has for answering it.

---------------
Problem Points
---------------

This setting specifies the total number of points possible for the problem.
This defaults to 1 point. In the LMS, the number of points a problem is worth
appears near the problem's display name. 

.. note::
  The LMS scores all problems. However, only scores for problem
  components that are in graded subsections count toward a learner's final
  grade.

---------------
Attempts
---------------

This setting specifies the number of times that a learner is allowed to try
to answer this problem correctly. You can define a different **Attempts**
value for each problem. Setting the Attempts value to empty means that learners
have an unlimited number of attempts.

A course-wide **Maximum Attempts** setting defines the default value for this
problem-specific setting. Initially, the value for the course-wide setting is
null, meaning that learners can try to answer problems an unlimited number of
times. You can change the course-wide default by selecting **Settings** and
then **Advanced Settings**. Note that if you change the course-wide default
from null to a specific number, you can no longer change the problem-specific
**Attempts** value to unlimited.

Only problems that have an **Attempts** setting of 1 or higher are included in
the answer distribution computations used in edX Insights and the Student
Answer Distribution report.

.. note::
   EdX recommends setting **Maximum Attempts** to unlimited or a
   large number when possible. Problems that allow unlimited attempts encourage
   risk taking and experimentation, both of which lead to improved learning
   outcomes. However, allowing for unlimited attempts might not be feasible in
   some courses, such as those that use primarily single select or dropdown
   problems in graded subsections.

.. _Hints:

=============
Hints
=============

.. include:: ../../../shared/exercises_tools/Subsection_configure_hints.rst

When you add hints, the **Hint** button is automatically displayed to learners.
Learners can access the hints by selecting **Hint** beneath the problem.  A
learner can view multiple hints by selecting **Hint** multiple times.

For example, in the following single select problem, the learner selects
**Hint** after having made one incorrect attempt.

.. image:: ../../../shared/images/multiple_choice_hint.png
 :alt: Image of a single select problem with the first hint.
 :width: 600

The hint text indicates that it is the first of two hints. After the learner
selects **Next Hint**, both of the available hints appear. When all hints have
been used, the **Hint** or **Next Hint** option is no longer available.

.. image:: ../../../shared/images/multiple_choice_hint2.png
 :alt: Image of a single select problem with the second hint.
 :width: 600

-----------------------------------
Best Practices for Providing Hints
-----------------------------------

To ensure that your hints can assist learners with varying backgrounds and
levels of understanding, you should provide multiple hints with different
levels of detail.

For example, the first hint can orient the learner to the problem and help
those struggling to better understand what is being asked.

The second hint can then take the learner further towards the answer.

In problems that are not graded, the third and final hint can explain the
solution for learners who are still confused.

.. _Show Answer:

===============
Show Answer
===============

This setting can be found on the collapsible settings to the right of the
problem editor after clicking Show advanced settings. This will add a
**Show Answer** option to the problem for the learner. The following
options define when the answer is shown to learners.

.. list-table::
   :widths: 15 70

   * - **After All Attempts**
     - Learners will be able to **Show Answer** after they have used all of
       their attempts. Requires max attempts to be set on the problem.

   * - **After All Attempts or Correct**
     - Learners will be able to **Show Answer** after they have used all of
       their attempts or have correctly answered the question. If max attempts
       are not set, the learner will need to answer correctly before they can
       **Show Answer**.

   * - **After Some Number of Attempts**
     - Learners will be able to **Show Answer** after they have attempted the
       problem a minimum number of times (this value is set by the course team
       in Studio).

   * - **Always**
     - Always present the **Show Answer** option.

       Note: If you specify **Always**, learners can submit a response even
       after they select **Show Answer** to see the correct answer.

   * - **Answered**
     - Learners will be able to **Show Answer** after they have correctly
       answered the problem.

   * - **Attempted**
     - Learners will be able to **Show Answer** after they have made at least
       1 attempt on the problem.

       If the problem can be, and is, reset, the answer continues to show.
       (When a learner answers a problem, the problem is considered to be both
       attempted and answered. When the problem is reset, the problem is still
       considered to have been attempted, but is not considered to be
       answered.)

   * - **Attempted or Past Due**
     - Learners will be able to **Show Answer** after they have made at least
       1 attempt on the problem or the problem’s due date is in the past.

   * - **Closed**
     - Learners will be able to **Show Answer** after they have used all
       attempts on the problem or the due date for the problem is in the past.

   * - **Correct or Past Due**
     - Learners will be able to **Show Answer** after they have correctly
       answered the problem or the due date for the problem is in the past.

   * - **Finished**
     - Learners will be able to **Show Answer** after they have used all
       attempts on the problem or the due date for the problem is in the past
       or they have correctly answered the problem.

   * - **Never**
     - Learners and Staff will never be able to **Show Answer**.

   * - **Past Due**
     - Learners will be able to **Show Answer** after the due date for the
       problem is in the past.

An explanation for the correct answer can be entered below. This explanation
is displayed when the learner presses the Show answer option.

.. _Show Answer Number of Attempts:

-------------------
Number of Attempts
-------------------

This setting appears under the Show answer dropdown when the
**After some number of attempts**, **After all attempts** or
**After all attempts or correct** option is selected. This limits when
learners can select the **Show Answer** option for a problem. Learners must
submit at least the specified number of attempted answers for the problem
before the **Show Answer** option is available to them.

.. _Show Reset Button:

=================
Show Reset Button
=================

This setting can be found on the collapsible settings to the right of the
problem editor after clicking **Show advanced settings**. It defines whether a
**Reset** option is available for the problem.

Learners can select **Reset** to clear any input that has not yet been
submitted, and try again to answer the problem.

If the learner has already submitted an answer, selecting **Reset** clears the
submission and, if the problem contains randomized variables and randomization
is set to **On Reset**, changes the values in the problem.

If the number of Maximum Attempts that was set for this problem has been
reached, the **Reset** option is not visible.

This problem-level setting overrides the course-level **Show Reset Button for
Problems** advanced setting.

.. _Time Between Attempts:

=======================
Time Between Attempts
=======================

This setting can be found on the collapsible settings to the right of the
problem editor after clicking **Show advanced settings**. It specifies the
number of seconds that a learner must wait between submissions for a problem
that allows multiple attempts. If the value is 0, the learner can attempt the
problem again immediately after an incorrect attempt.

Adding required wait time between attempts can help to prevent learners from
simply guessing when multiple attempts are allowed.

If a learner attempts a problem again before the required time has elapsed, they
see a message below the problem indicating the remaining wait time. The format
of the message is, "You must wait at least {n} seconds between submissions. {n}
seconds remaining."

.. _Advanced Editor:

***************************************************
The Advanced Editor
***************************************************

If the simple editor cannot fulfill your needs, you might turn your attention
to the Advanced Editor. This editor will allow you to directly edit the open
learning XML (OLX) of your problem. The Advanced Editor can be accessed one of
two ways.

If you are creating a new problem, on the **Select problem type** screen,
select the **Advanced problem types**. This will bring you to a list of advanced
problems with varying levels of support. To create an advanced problem from
scratch, select **Blank advanced problem**.

If you are looking to turn your simple problem into an advanced problem, click
the **Switch to advanced editor** button, which can be found on the collapsible
settings to the right of the problem editor after clicking
**Show advanced settings**.

The Advanced Editor retains several settings from the simple editor such as
**Scoring**, **Show answer**, **Show reset option**, **Time between attempts**
and **MATLAB API Key** as well as introduces the **Randomization** setting.
While the other settings are not shown on the collapsible panes to the right of
the problem editor, they can be added via editing the OLX.

OLX specifications can be found under each problem type in
:ref:`Exercises and Tools Index`.

.. note::
   If you have turned your problem into an advanced problem, it is possible to
   turn it back into a simple problem. When you edit a problem, as long as the
   problem editor can fully parse the OLX, the editor will open as the Simple
   Editor instead of the Advanced Editor.

.. _Advanced Editor Features:

***************************************************
Advanced Editor Features
***************************************************

Since the Advanced Editor allows you to edit the problem directly using the OLX,
there are many more ways to write a problem. Below are several features the
Advanced Editor is capable of:

.. contents::
 :local:
 :depth: 1

.. _Randomization:

===============
Randomization
===============

.. note::
   This Randomization setting serves a different purpose from “problem
   randomization”. This Randomization setting affects how numeric values are
   randomized within a single problem and requires the inclusion of a Python
   script. Problem randomization presents different problems or problem
   versions to different learners. For more information, see
   :ref:`Problem Randomization`.

This setting can be found on the collapsible settings to the right of the
problem editor. For problems that include a Python script to generate numbers
randomly, this setting specifies how frequently the values in the problem
change: each time a different learner accesses the problem, each time a single
learner tries to answer the problem, both, or never.

.. note::
   This setting should only be set to an option other than **Never** for
   problems that are configured to do random number generation.

For example, in this problem, the highlighted values change each time a
learner submits an answer to the problem.

.. image:: ../../../shared/images/Rerandomize.png
 :alt: An image of the same problem shown twice, with color highlighting on
   values that change.
 :width: 800

If you want to randomize numeric values in a problem, you complete both of
these steps.

* Make sure that you edit your problem to include a Python script that randomly
  generates numbers.

* Select an option other than **Never** for the **Randomization** setting.

The edX Platform has a 20-seed maximum for randomization. This means that
learners see up to 20 different problem variants for every problem that has
**Randomization** set to an option other than **Never**. It also means that
every answer for the 20 different variants is reported by the Answer
Distribution report and edX Insights. Limiting the number of variants to a
maximum of 20 allows for better analysis of learner submissions by allowing you
to detect common incorrect answers and usage patterns for such answers.

For more information, see :ref:`Student_Answer_Distribution` in this guide, or
`Review Answers to Graded Problems`_ or `Review Answers to Ungraded Problems`_
in *Using edX Insights*.

.. important::
 Whenever you choose an option other than **Never** for a
 problem, the computations for the Answer Distribution report and edX Insights
 include up to 20 variants for the problem, **even if the problem was not
 actually configured to include randomly generated values**. This can make data
 collected for problems that cannot include randomly generated values,
 (including, but not limited to, all single select, multi-select, dropdown, and
 text input problems), extremely difficult to interpret.

You can choose the following options for the **Randomization** setting.

.. list-table::
   :widths: 15 70
   :header-rows: 1

   * - Option
     - Description
   * - **Always**
     - Learners see a different version of the problem each time they select
       **Submit**.
   * - **On Reset**
     - Learners see a different version of the problem each time they select
       **Reset**.
   * - **Never**
     - All learners see the same version of the problem. For most courses, this
       option is supplied by default. Select this option for every problem in
       your course that does not include a Python script to generate random
       numbers.
   * - **Per Student**
     - Individual learners see the same version of the problem each time they
       look at it, but that version is different from the version that other
       learners see.

.. _Multiple Problems in One Component:

============================================================
Including Multiple Questions in One Component
============================================================

In some cases, you might want to design an assessment that combines multiple
questions in a single problem component. For example, you might want learners
to demonstrate mastery of a concept by providing the correct responses to
several questions, and only giving them credit for a problem if all of the
answers are correct.

Another example involves learners who have slow or intermittent internet
connections. When every problem appears on a separately loaded web page, these
learners can find the amount of time it takes to complete an assignment or exam
discouraging. For these learners, grouping several questions together can
promote increased engagement with course assignments.

When you add multiple questions to a single problem component, the settings
that you define, including the display name and whether to show the **Reset**
button, apply to all of the questions in that component. The answers to all of
the questions are submitted when learners select **Submit**, and the correct
answers for all of the questions appear when learners select **Show Answer**.
By default, learners receive one point for each question they answer correctly.
For more information about changing the default problem points and other
settings, see :ref:`Problem Settings`.

.. important::
  To assure that the data collected for learner interactions with
  your problem components is complete and accurate, include a maximum of 10
  questions in a single problem component.

-------------------------------------------------
Adding Multiple Questions to a Problem Component
-------------------------------------------------

To design an assignment that includes several questions, you add one problem
component and then edit it to add every question and its answer options, one
after the other, in that component. Be sure to identify the text of every
question or prompt with the appropriate OLX ``<label>`` element, and include
all of the other required elements for each question.

* Each question and its answer options are enclosed by the element that
  identifies the type of problem, such as
  ``<multiplechoiceresponse>`` for a single select question or
  ``<formularesponse>`` for a math expression input question.

* You can provide a different explanation for each question with the
  OLX ``<solution>`` element.

As a best practice, edX recommends that you avoid including unformatted
paragraph text between the questions. Screen readers can skip over text that is
inserted among multiple questions.

The questions that you include can all be of the same problem type, such as a
series of text input questions, or you can include questions that use different
problem types, such as both numerical input and math expression input.

.. note::
  You cannot use a :ref:`Custom JavaScript` in a problem component that
  contains more than one question. Each custom JavaScript problem must be in
  its own component.

An example of a problem component that includes a text input question and a
numerical input question follows.

.. code-block:: xml

  <problem>
    <stringresponse answer="Caesar Cardini" type="ci">
      <label>Who invented the Caesar salad?</label>
      <description>Be sure to check your spelling.</description>
      <textline size="20"/>
      <solution>
        <div class="detailed-solution">
          <p>Explanation</p>
          <p>Caesar Cardini is credited with inventing this salad and received
           a U.S. trademark for his salad dressing recipe.</p>
        </div>
      </solution>
    </stringresponse>

    <numericalresponse answer="1924">
      <label>In what year?</label>
      <formulaequationinput/>
      <solution>
        <div class="detailed-solution">
          <p>Explanation</p>
          <p>Cardini invented the dish at his restaurant on 4 July 1924 after
           the rush of holiday business left the kitchen with fewer supplies
           than usual.</p>
        </div>
      </solution>
    </numericalresponse>
  </problem>

.. include:: ../../../shared/exercises_tools/Section_partial_credit.rst

.. include:: ../../../shared/exercises_tools/Section_adding_tooltip.rst

.. _Problem Randomization:

***********************
Problem Randomization
***********************

Presenting different learners with different problems or with different
versions of the same problem is referred to as "problem randomization".

You can provide different learners with different problems by using randomized
content blocks, which randomly draw problems from pools of problems stored in
content libraries. For more information, see :ref:`Randomized Content Blocks`.

.. note::
   Problem randomization is different from the **Randomization** setting
   that you define in Studio. Problem randomization presents different problems
   or problem versions to different learners, while the **Randomization**
   setting controls when a Python script randomizes the variables within a
   single problem. For more information about the **Randomization** setting,
   see :ref:`Randomization`.

.. _Create Randomized Problems:

Creating randomized problems by exporting your course and editing some of your
course's XML files is no longer supported.

.. _Modifying a Released Problem:

*****************************
Modifying a Released Problem
*****************************

.. warning::
 Be careful when you modify problems after they have been
 released. Changes that you make to published problems can affect the learner
 experience in the course and analysis of course data.

After a learner submits a response to a problem, the LMS stores that response,
the score that the learner received, and the maximum score for the problem. For
problems with a **Maximum Attempts** setting greater than 1, the LMS updates
these values each time the learner submits a new response to a problem.
However, if you change a problem or its attributes, existing learner
information for that problem is not automatically updated.

For example, you release a problem and specify that its answer is 3.
After some learners have submitted responses, you notice that the answer
should be 2 instead of 3. When you update the problem with the correct
answer, the LMS does not update scores for learners who originally answered
2 for the problem and received the wrong score.

For another example, you change the number of response fields to
three. Learners who submitted answers before the change have a score of
0, 1, or 2 out of 2.0 for that problem. Learners who submitted answers
after the change have scores of 0, 1, 2, or 3 out of 3.0 for the same
problem.

If you change the points setting for the problem in Studio, however, existing
scores update when the learner's **Progress** page is refreshed. In a live
section, learners will see the effect of these changes.

============
Workarounds
============

If you have to modify a released problem in a way that affects grading, you
have two options to ensure that every learner has the opportunity
to submit a new response and be regraded. Note that both options require you to
ask your learners to go back and resubmit answers to a problem.

*  In the problem component that you changed, increase the number of attempts
   for the problem, and then ask all of your learners to redo the problem.

*  Delete the entire problem component in Studio and replace it with a new
   problem component that has the content and settings that you want. Then ask
   all of your learners to complete the new problem. (If the revisions you must
   make are minor, you might want to duplicate the problem component before you
   delete it, and then revise the copy.)

For information about how to review and adjust learner grades in the LMS, see
:ref:`Adjust_grades`.

.. include:: ../../../links/links.rst
