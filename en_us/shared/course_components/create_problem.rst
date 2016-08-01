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

To add interactive problems to a course in Studio, In the course outline in
Studio, at the :ref:`unit<The Unit Workflow>` level, you select **Problem**.
You then choose the type of problem that you want to add from a list of
**Common Problem Types** or **Advanced** problem types.

The common problem types include relatively straightforward CAPA problems such
as multiple choice and text or numeric input. The advanced problem types can be
more complex to set up, such as math expression input, peer assessment, or
custom JavaScript problems.

The common and advanced problem types that the problem component lists are the
core set of problems that every course team can include in a course. You can
also enable more exercises and tools for use in your course. For more
information, see :ref:`Enable Additional Exercises and Tools`.

=====================================
Adding Graded or Ungraded Problems
=====================================

When you :ref:`establish the grading policy<Grading Index>` for your course,
you define the assignment types that count toward learners' grades: for
example, homework, labs, midterm, final, and ungraded. You specify
one of these assignment types for each of the subsections in your course.

As you develop your course, you can add problem components to a unit in any
subsection. The problem components that you add automatically inherit the
assignment type that is defined at the subsection level. For example, all of
the problem components that you add to a unit in an ungraded subsection are
ungraded, all of the problem components that you add to a unit in the midterm
subsection are graded, and so on.

For more information, see :ref:`Set the Assignment Type and Due Date for a
Subsection`.

.. _Problem Learner View:

.. include:: ../../../shared/course_components/Section_learner_problem_view.rst

.. _Problem Studio View:

*****************************
Editing a Problem in Studio
*****************************

When you select **Problem** and choose one of the problem types, Studio adds an
example problem of that type to the unit. To replace the example with your own
problem, you select **Edit** to open the example problem in an editor.

The editing interface that opens depends on the type of problem you choose.

* For common problem types, the :ref:`simple editor<Simple Editor>` opens. In
  this editor, you use Markdown-style formatting indicators to identify the
  elements of the problem, such as the prompt and the correct and incorrect
  answer options.

* For advanced problem types (with the exception of :ref:`peer assessment<Open
  Response Assessments 2>`), the :ref:`advanced editor<Advanced Editor>` opens.
  In this editor you use OLX (open learning XML) tags, elements, and attributes
  to identify the elements of the problem.

  For peer assessment problem types, you define the problem elements and
  options by using a graphical user interface. For more information, see
  :ref:`PA Create an ORA Assignment`.

You can switch from the simple editor to the advanced editor at any time by
selecting **Advanced Editor** from the simple editor's toolbar.

.. note:: After you save a problem in the advanced editor, you cannot open it
 again in the simple editor.

.. _Simple Editor:

==================
The Simple Editor
==================

When you edit one of the :ref:`common problem types<Adding a Problem>`, the
simple editor opens with an example problem that you can use as a template for
adding Markdown formatting.

.. ...with a template that...^

*  :ref:`Checkbox` and Checkboxes with Hints and Feedback

*  :ref:`Dropdown` and Dropdown with Hints and Feedback

*  :ref:`Multiple Choice` and Multiple Choice with Hints and Feedback

*  :ref:`Numerical Input` and Numerical Input with Hints and Feedback

*  :ref:`Text Input` and Text Input with Hints and Feedback

Blank common problems do not provide an example problem, but they also open in
the simple editor by default.

==========================
Adding Markdown Formatting
==========================

The following image shows a multiple choice problem in the simple
editor.

.. image:: ../../../shared/images/MultipleChoice_SimpleEditor.png
 :alt: An example multiple choice problem in the simple editor, with numbered
   callouts for each formatting option.
 :width: 600

The simple editor includes a toolbar with options that provide the required
Markdown formatting for different types of problems. When you select an option
from the toolbar, formatted sample text appears in the simple editor.
Alternatively, you can apply formatting to your own text by selecting the text
and then one of the toolbar options.

Descriptions of the Markdown formatting that you use in the simple editor
follow.

#. **Heading**: Identifies a title or heading by adding a
   series of equals signs (``=``) below it on the next line.

#. **Multiple Choice**: Identifies an answer option for a multiple choice
   problem by adding a pair of parentheses (``( )``) before it. To identify the
   correct answer option, you insert an ``x`` within the parentheses:
   (``(x)``).

#. **Checkboxes**: Identifies an answer option for a checkboxes problem by
   adding a pair of brackets (``[ ]``) before it. To identify the correct
   answer option or options, you insert an ``x`` within the brackets:
   (``[x]``).

#. **Text Input**: Identifies the correct answer for a text input problem by
   adding an equals sign (``=``) before the answer value on the same line.

#. **Numerical Input**: Identifies the correct answer for a numerical input
   problem by adding an equals sign (``=``) before the answer value on the same
   line.

#. **Dropdown**: Identifies a comma-separated list of values as the set of
   answer options for a dropdown problem by adding two pairs of brackets (``[[
   ]]``) around the list. To identify the correct answer option, you add
   parentheses (``( )``) around that option.

#. **Explanation**: Identifies the explanation for the
   correct answer by adding an ``[explanation]`` tag to the lines before and
   after the text. An explanation appears only after learners select **Show
   Answer**. You define when the **Show Answer** option is available to
   learners by using the :ref:`Show Answer` setting.

#. **Advanced Editor** link: Opens the problem in the :ref:`advanced
   editor<Advanced Editor>`, which shows the OLX markup for the problem.

#. **Question Mark** icon: Opens a list of formatting hints.

#. **Accessible Label**: Identifies the prompt, or question, that learners need
   to answer. The toolbar does not have an option that provides this
   formatting, so you add two pairs of inward-pointing angle brackets (``>>
   <<``) around the question text. For example, ``>>Is this the question?<<``.

.. Optionally, you can add guidance that helps learners answer the question as
   part of the accessible label. For example, when you add a checkbox problem
   that is only correct when learners select three of the answer options, you
   might include the tip "Be sure to select all that apply." To add this
   description, you include it after the question within the angle brackets,
   and then you separate the question and the description by inserting a pair
   of pipe symbols (``||``) between them. For example, ``>>Which of the
   following choices is correct? ||Be sure to select all that apply.<<``.

   * Screen readers read all of the text that you supply for the problem, and
     then repeat the text that is identified as the accessible label
     immediately before reading the answer choices for the problem.

   * The :ref:`Student_Answer_Distribution` report uses the text with this
     formatting to identify each problem.

   * Insights also uses the text with this formatting to identify each problem.
     For more information, see `Using edX Insights`_.

When you enter text, note that the simple editor cannot interpret certain
symbol characters correctly. These symbols are reserved HTML characters:
greater than (>), less than (<), and ampersand (&). If you enter text that
includes these characters, the simple editor cannot save your edits. To resolve
this problem, replace these characters in your problem text with the HTML
entities that represent them.

* To enter >, type ``&gt;``.
* To enter <, type ``&lt;``.
* To enter &, type ``&amp;``.

.. _Advanced Editor:

====================
The Advanced Editor
====================

When you edit one of the :ref:`advanced problem types<Adding a Problem>`, the
advanced editor opens with an example problem. The advanced editor is an XML
editor that shows the OLX markup for a problem. You edit the following advanced
problem types in the advanced editor.

* :ref:`Circuit Schematic Builder`

* :ref:`Custom JavaScript Display and Grading<Custom JavaScript>`

* :ref:`Custom Python-Evaluated Input<Write Your Own Grader>`

* :ref:`Drag and Drop<drag_and_drop_problem>` (Deprecated)

* :ref:`Image Mapped Input`

* :ref:`Math Expression Input`

* :ref:`Problem Written in LaTeX`

* :ref:`Problem with Adaptive Hint` and Problem with Adaptive Hint in LaTex

* :ref:`Molecular Structure<Molecule Editor>`

For the :ref:`Peer Assessment<Open Response Assessments 2>` advanced problem
type, a dialog box opens for problem setup.

Blank advanced problems do not provide an example problem, but they also open
in the advanced editor by default.

The following image shows the OLX markup in the advanced editor for the same
example multiple choice problem that is shown in the simple editor above.

.. image:: ../../../shared/images/MultipleChoice_AdvancedEditor.png
 :alt: An example multiple choice problem in the advanced editor.
 :width: 600

For more information about the OLX markup to use for a problem, see the topic
that describes that problem type.

.. _Problem Settings:

****************************************
Defining Settings for Problem Components
****************************************

In addition to the text of the problem and its Markdown formatting or OLX
markup, you define the following settings for problem components. To access
these settings, you edit the problem and then select **Settings**.

.. contents::
  :local:
  :depth: 1

If you do not edit these settings, default values are supplied for your
problems.

===============
Display Name
===============

This required setting provides an identifying name for the problem. The display
name appears as a heading above the problem in the LMS, and it identifies the
problem for you in Insights. Be sure to add unique, descriptive display names
so that you, and your learners, can identify specific problems quickly and
accurately.

The following illustration shows the display name of a problem in Studio, in
the LMS, and in Insights.

.. image:: ../../../shared/images/display_names_problem.png
 :alt: The identifying display name for a problem in Studio, the LMS, and
     Insights.
 :width: 800

For more information about metrics for your course's problem components, see
`Using edX Insights`_.

=================
Maximum Attempts
=================

This setting specifies the number of times that a learner is allowed to try to
answer this problem correctly. You can define a different **Maximum Attempts**
value for each problem.

A course-wide **Maximum Attempts** setting defines the default value for this
problem-specific setting. Initially, the value for the course-wide setting is
null, meaning that learners can try to answer problems an unlimited number of
times. You can change the course-wide default by selecting **Settings** and
then **Advanced Settings**. Note that if you change the course-wide default
from null to a specific number, you can no longer change the problem-specific
**Maximum Attempts** value to unlimited.

Only problems that have a **Maximum Attempts** setting of 1 or higher are
included in the answer distribution computations used in edX Insights and the
Student Answer Distribution report.

.. note:: EdX recommends setting **Maximum Attempts** to unlimited or a
   large number when possible. Problems that allow unlimited attempts encourage
   risk taking and experimentation, both of which lead to improved learning
   outcomes. However, allowing for unlimited attempts might not be feasible in
   some courses, such as those that use primarily multiple choice or dropdown
   problems in graded subsections.

.. _Problem Weight:

==============================
Problem Weight
==============================

.. note:: The LMS scores all problems. However, only scores for problem
  components that are in graded subsections count toward a learner's final
  grade.

This setting specifies the total number of points possible for the problem. In
the LMS, the problem weight appears near the problem's display name.

.. image:: ../../../shared/images/ProblemWeight_DD.png
 :alt: A problem component with three questions, with the possible
       number of points, 3, circled.
 :width: 500

By default, each response field, or answer space, in a problem component is
worth one point. You increase or decrease the number of points for a problem
component by setting its **Problem Weight**.

In the example shown above, a single problem component includes three separate
questions. To respond to these questions, learners select answer options from
three separate dropdown lists, the response fields for this problem. By
default, learners receive one point for each question that they answer
correctly.

For information about how to define a problem that includes more than one
question, see :ref:`Multiple Problems in One Component`.

Computing Scores
****************

The score that a learner earns for a problem is the result of the
following formula.

**Score = Weight × (Correct answers / Response fields)**

*  **Score** is the point score that the learner receives.

*  **Weight** is the problem's maximum possible point score.

*  **Correct answers** is the number of response fields that contain correct
   answers.

*  **Response fields** is the total number of response fields in the problem.

**Examples**

The following are some examples of computing scores.

*Example 1*

A problem's **Problem Weight** setting is left blank. The problem has two
response fields. Because the problem has two response fields, the
maximum score is 2.0 points.

If one response field contains a correct answer and the other response
field contains an incorrect answer, the learner's score is 1.0 out of 2
points.

*Example 2*

A problem's weight is set to 12. The problem has three response fields.

If a learner's response includes two correct answers and one incorrect
answer, the learner's score is 8.0 out of 12 points.

*Example 3*

A problem's weight is set to 2. The problem has four response fields.

If a learner's response contains one correct answer and three incorrect
answers, the learner's score is 0.5 out of 2 points.

.. _Randomization:

===============
Randomization
===============

.. note:: This **Randomization** setting serves a different purpose from
 "problem randomization". This **Randomization** setting affects how numeric
 values are randomized within a single problem and requires the inclusion of a
 Python script. Problem randomization presents different problems or problem
 versions to different learners. For more information, see :ref:`Problem
 Randomization`.

For problems that include a Python script to generate numbers randomly, this
setting specifies how frequently the values in the problem change: each time a
different learner accesses the problem, each time a single learner tries to
answer the problem, both, or never.

.. note:: This setting should only be set to an option other than **Never**
 for problems that are configured to do random number generation.

For example, in this problem, the highlighted values change each time a learner
submits an answer to the problem.

.. image:: ../../../shared/images/Rerandomize.png
 :alt: An image of the same problem shown twice, with color highlighting on
   values that change.
 :width: 800

If you want to randomize numeric values in a problem, you complete both of
these steps.

* Make sure that you edit your problem to include a Python script that randomly
  generates numbers.

* Select an option other than **Never** for the **Randomization** setting.

..  For more information, see :ref:`Use Randomization in a Numerical Input Problem`.
..  ^^ add back to first bullet when DOC-2175 gets done - Alison 30 Jul 15

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

.. important:: Whenever you choose an option other than **Never** for a
 problem, the computations for the Answer Distribution report and edX Insights
 include up to 20 variants for the problem, **even if the problem was not
 actually configured to include randomly generated values**. This can make data
 collected for problems that cannot include randomly generated values,
 (including, but not limited to, all multiple choice, checkboxes, dropdown, and
 text input problems), extremely difficult to interpret.

You can choose the following options for the **Randomization** setting.

.. list-table::
   :widths: 15 70
   :header-rows: 1

   * - Option
     - Description
   * - **Always**
     - Learners see a different version of the problem each time they select
       Check.
   * - **On Reset**
     - Learners see a different version of the problem each time they select
       Reset.
   * - **Never**
     - All learners see the same version of the problem. For most courses, this
       option is supplied by default. Select this option for every problem in
       your course that does not include a Python script to generate random
       numbers.
   * - **Per Student**
     - Individual learners see the same version of the problem each time they
       look at it, but that version is different from the version that other
       learners see.

.. _Show Answer:

===============
Show Answer
===============

This setting adds a **Show Answer** option to the problem. The following
options define when the answer is shown to learners.

.. list-table::
   :widths: 15 70

   * - **Always**
     - Always show the answer when the learner selects the **Show Answer**
       button.
   * - **Answered**
     - Show the answer after the learner tries to answer the problem.

       If the problem can be, and is, reset, the answer is not shown until the
       learner tries the problem again. (When a learner answers a problem, the
       problem is considered to be both attempted and answered. When the
       problem is reset, the problem is still attempted, but not yet
       answered.)
   * - **Attempted**
     - Show the answer after the learner tries to answer the problem.

       If the problem can be, and is, reset, the answer continues to show.
       (When a learner answers a problem, the problem is considered to be
       both attempted and answered. When the problem is reset, the problem is
       still attempted, but not yet answered.)
   * - **Closed**
     - Show the answer after the learner has used up all his attempts to answer
       the problem or the due date has passed.
   * - **Finished**
     - Show the answer after the learner has answered the problem correctly,
       the learner has no attempts remaining, or the problem due date has
       passed.
   * - **Correct or Past Due**
     - Show the answer after the learner has answered the problem correctly or
       the problem due date has passed.
   * - **Past Due**
     - Show the answer after the due date for the problem has passed.
   * - **Never**
     - Never show the answer. In this case, the **Show Answer** option does not
       appear next to the problem in Studio or in the LMS.

.. _Show Reset Button:

=================
Show Reset Button
=================

This setting defines whether a **Reset** option is available for the problem.

Learners can select **Reset** to clear any input that has not yet been
submitted, and try again to answer the problem.

If the learner has already submitted an answer, selecting **Reset** clears the
submission and, if the problem contains randomized variables and randomization
is set to **On Reset**, changes the values in the problem.

If the number of Maximum Attempts that was set for this problem has been
reached, the **Reset** option is not visible.

This problem-level setting overrides the course-level **Show Reset Button for
Problems** advanced setting.

.. _Timer Between Attempts:

=======================
Timer Between Attempts
=======================

This setting specifies the number of seconds that a learner must wait between
submissions for a problem that allows multiple attempts. If the value is 0, the
learner can attempt the problem again immediately after an incorrect attempt.

Adding required wait time between attempts can help to prevent learners from
simply guessing when multiple attempts are allowed.

If a learner attempts a problem again before the required time has elapsed, she
sees a message below the problem indicating the remaining wait time. The format
of the message is, "You must wait at least {n} seconds between submissions. {n}
seconds remaining."

.. _Multiple Problems in One Component:

***************************************************
Including Multiple Questions in One Component
***************************************************

In some cases, you might want to design an assessment that combines multiple
questions in a single problem component. For example, you might want learners
to demonstrate mastery of a concept by providing the correct responses to
several questions, and only giving them credit for problem if all of the
answers are correct.

Another example involves learners who have slow or intermittent internet
connections. When every problem appears on a separately loaded web page, these
learners can find the amount of time it takes to complete an assignment or exam
discouraging. For these learners, grouping several questions together can
promote increased engagement with course assignments.

When you add multiple questions to a single problem component, the settings
that you define, including the display name and whether to show the **Reset**
button, apply to all of the questions in that component. The answers to all of
the questions are submitted when learners select **Check**, and the correct
answers for all of the questions appear when learners select **Show Answer**.
By default, learners receive one point for each question they answer correcty.
For more information about changing the default problem weight and other
settings, see :ref:`Problem Settings`.

.. important:: To assure that the data collected for learner interactions with
  your problem components is complete and accurate, include a maximum of 10
  questions in a single problem component.

================================================
Adding Multiple Questions to a Problem Component
================================================

To design an assignment that includes several questions, you add one problem
component and then edit it to add every question and its answer options, one
after the other, in that component. Be sure to identify the text of every
question or prompt with the appropriate Markdown formatting (``>> <<``) or OLX
tag, and include all of the other required elements for
each question you include.

.. ``<label></label>`` insert after OLX above

The questions that you include can all be of the same problem type, such as a
series of text input questions, or you can include questions that use different
problem types, such as both numerical input and math expression input.

.. note::
  You cannot use a :ref:`Custom JavaScript` in a problem component that
  contains more than one question. Each custom JavaScript problem must be in
  its own component.

.. An example of a problem component with two text input questions follows. In the
.. simple editor, the problem has the following Markdown formatting.

.. ::

..  >>Who invented the Caesar salad?||Be sure to check your spelling.<<

..  = Caesar Cardini

..  >>In what year?<<

..  = 1924

.. In the advanced editor, the problem has the following OLX markup.

.. ::

..   <problem>
..   <stringresponse answer="Caesar Cardini">
..   <label>Who invented the Caesar salad?</label>
..   <description>Be sure to check your spelling.</description>
..   </stringresponse>
..   <numericalresponse answer="1924">
..   <label>In what year?</label>
..   </numericalresponse>
..   </problem>

.. ^^placeholder, need to verify in the sandbox. - Alison 4 Aug 2016

.. include:: ../../../shared/exercises_tools/Section_adding_hints.rst

.. include:: ../../../shared/exercises_tools/Section_partial_credit.rst

.. include:: ../../../shared/exercises_tools/Section_adding_tooltip.rst

.. _Problem Randomization:

***********************************
Problem Randomization
***********************************

Presenting different learners with different problems or with different
versions of the same problem is referred to as "problem randomization".

You can provide different learners with different problems by using randomized
content blocks, which randomly draw problems from pools of problems stored in
content libraries. For more information, see :ref:`Randomized Content Blocks`.

.. note:: Problem randomization is different from the **Randomization** setting
   that you define in Studio. Problem randomization presents different problems
   or problem versions to different learners, while the **Randomization**
   setting controls when a Python script randomizes the variables within a
   single problem. For more information about the **Randomization** setting,
   see :ref:`Randomization`.

.. _Create Randomized Problems:

Creating randomized problems by exporting your course and editing some of your
course's XML files is no longer supported.

.. _Modifying a Released Problem:

*********************************
Modifying a Released Problem
*********************************

.. warning:: Be careful when you modify problems after they have been
 released. Changes that you make to published problems can affect the learner
 experience in the course and analysis of course data.

After a learner submits a response to a problem, the LMS stores that response,
the score that the learner received, and the maximum score for the problem. For
problems with a **Maximum Attempts** setting greater than 1, the LMS updates
these values each time the learner submits a new response to a problem.
However, if you change a problem or its attributes, existing learner
information for that problem is not automatically updated.

For example, you release a problem and specify that its answer is 3.
After some learner have submitted responses, you notice that the answer
should be 2 instead of 3. When you update the problem with the correct
answer, the LMS does not update scores for learners who originally answered
2 for the problem and received the wrong score.

For another example, you change the number of response fields to
three. Learners who submitted answers before the change have a score of
0, 1, or 2 out of 2.0 for that problem. Learners who submitted answers
after the change have scores of 0, 1, 2, or 3 out of 3.0 for the same
problem.

If you change the weight setting for the problem in Studio, however, existing
scores update when the learner's **Progress** page is refreshed. In a live
section, learners will see the effect of these changes.

===============
Workarounds
===============

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
