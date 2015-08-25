.. _Working with Problem Components:

################################
Working with Problem Components
################################

This section covers the basics of problem components: what they look like to
you and your learners, and the options that every problem component has. 

.. contents::
 :local:
 :depth: 1

For more information about individual problem types, see :ref:`Create
Exercises`.

******************************
Overview
******************************

The problem component allows you to add interactive, automatically
graded exercises to your course content. You can create many different
types of problems in Studio.

******************************
Graded Problems
******************************

All problems receive a point score, but, by default, problems do not count
toward a learner's grade. 

To have problems to count toward the grade, change the assignment type of the
subsection that contains the problems. For more information, see :ref:`Set the
Assignment Type and Due Date for a Subsection`.

.. _Problem Learner View:

************************************
The Learner View of a Problem
************************************

All problems on the edX platform have several component parts.

.. image:: ../../../shared/building_and_running_chapters/Images/AnatomyOfExercise1.png
 :alt: An image of a problem from a learner's point of view, with callouts for 
       elements of the problem.
  :width: 500

#. **Problem text.** The problem text can contain any standard HTML formatting.

#. **Response field with the learner's answer.** Learners enter answers
   in *response fields*. The appearance of the response field depends on
   the type of the problem.

#. **Rendered answer.** For some problem types, Studio uses MathJax to
   render plain text as "beautiful math".

#. **Check button.** The learner selects **Check** to submit a response or find
   out if his answer is correct. If the answer is correct, a green check mark
   appears. If it is incorrect, a red X appears. When the learner selects the
   **Check** button, the Learning Management System saves the grade and current
   state of the problem.

#. **Save button.** The learner can select **Save** to save her current
   response without submitting it for a grade. This allows the learner to
   stop working on a problem and come back to it later.

#. **Show Answer button.** This button is optional. When the learner
   selects **Show Answer**, she sees both the correct answer (see 2
   above) and the explanation (see 10 below). You define whether
   the **Show Answer** button is visible.

#. **Attempts.** You can set a specific number of attempts, or allow
   unlimited attempts for a problem. By default, the course-wide **Maximum
   Attempts** advanced setting is null, meaning that the maximum number of
   attempts for problems is unlimited. If the course-wide **Maximum Attempts**
   setting is changed to a specific number, the **Maximum Attempts** setting
   for individual problems defaults to that number, and cannot be set to
   unlimited.

   .. image:: ../../../shared/building_and_running_chapters/Images//AnatomyOfExercise2.png
    :alt: An image of a problem from a learners's point of view, with 
       callouts for attempts and showing the answer.
    :width: 500

#. **Feedback.** After a learner selects **Check**, all problems return a
   green check mark or a red X.

   .. image:: ../../../shared/building_and_running_chapters/Images//AnatomyofaProblem_Feedback.png
    :alt: An image of a feedback checkmark and x from a learner's point of view.

#. **Correct answer.** Most problems require that you specify 
   a single correct answer.

#. **Explanation.** You can include an explanation that
   appears when a learner selects **Show Answer**.

#. **Reset button.** Learners can select **Reset** to clear any input that has
   not yet been submitted, and try again to answer the question. 

  - If the learner has already submitted an answer, selecting **Reset** clears
    the submission and, if the problem includes a Python script to randomize
    variables and the randomization setting is **On Reset**, changes the values
    the learner sees in the problem.
  - If the number of Maximum Attempts that was set for this problem has been
    reached, the **Reset** button is not visible.

#. **Hide Answer button.**

   .. image:: ../../../shared/building_and_running_chapters/Images//AnatomyOfExercise3.png
    :alt: An image of a graded assignment shown in the left pane of the LMS for a course.
    :width: 200

#. **Grading.** You can specify whether a group of problems
   is graded. If a group of problems is graded, a clock icon appears for
   that assignment in the left pane.

   .. image:: ../../../shared/building_and_running_chapters/Images//clock_icon.png
    :alt: An image of the clock icon, signifying that the problems are graded.

#. **Due date.** The date that the problem is due. A problem that is
   past due does not have a **Check** button. It also does not accept
   answers or provide feedback.

.. note:: Problems can be **open** or **closed.** Closed problems do not 
          have a **Check** button. Learners can still see questions, solutions,
          and revealed explanations, but they cannot check their work, submit
          responses, or change an earlier score.

There are also some attributes of problems that are not immediately
visible. You can set these attributes in Studio.

* **Randomization.** In certain types of problems, you can include a Python
  script to randomize the values that are presented to learners. You use this
  setting to define when values are randomized.

* **Weight.** Different problems in a particular problem set can be
   given different weights.

* **Label.** To improve accessibility for learners who have disabilities, each
  problem needs a descriptive label. The label typically contains part or all
  of the text of the question in the problem. Most templates include a space
  for a label. You can find example labels in the documentation for each
  problem or tool type.

.. _Problem Studio View:

************************************
The Studio View of a Problem
************************************

All problems are written in XML. However, Studio offers two interfaces for
editing problem components: the Simple Editor and the Advanced Editor.

*  The Simple Editor allows you to edit problems visually, without
   having to work with XML. 

*  The Advanced Editor converts the problem to edX's XML standard and
   allows you to edit that XML directly.

You can switch at any time from the Simple Editor to the Advanced Editor by
selecting **Advanced Editor** in the top right corner of the Simple Editor
interface. However, after you save a problem in the Advanced Editor, you cannot
open it again in the Simple Editor.

.. _Simple Editor:

=================
The Simple Editor
=================

When you select the following problem types, the Simple Editor opens with a
preformatted example problem.

*  :ref:`Checkbox`: In checkbox problems, learners select one or more options
   from a list of possible answers.

*  :ref:`Dropdown`: In dropdown problems, learners select one answer from a
   dropdown list.

*  :ref:`Multiple Choice`: Multiple choice problems require learners to
   select one answer from a list of choices that appear directly below
   the question.

*  :ref:`Numerical Input`: Numerical input problems require answers that
   include only integers, fractions, and a few common constants and
   operators.

*  :ref:`Text Input`: In text input problems, learners enter a short text
   answer to a question.

The following image shows an example multiple choice problem in the Simple
Editor.

.. image:: ../../../shared/building_and_running_chapters/Images//MultipleChoice_SimpleEditor.png
 :alt: An image of the simple editor with numbered callouts for options and an 
   example multiple choice problem to demonstrate the formatting.
 :width: 450

The Simple Editor includes a toolbar with options that provide the required
formatting for different types of problems. When you select an option from the
toolbar, formatted sample text appears in the Simple Editor. Alternatively,
you can apply formatting to your own text by selecting the text and then one
of the toolbar options.

Descriptions of the toolbar options follow.

  1. **Heading 1**: Format text as a first level heading.
  2. **Multiple Choice**: Identify the text on each selected line as an answer
     option for a multiple choice problem.
  3. **Checkboxes**: Identify the text on each selected line as an answer
     option for a checkboxes problem.
  4. **Text Input**: Identify the correct answer for a text input problem.
  5. **Numerical Input**: Identify the correct answer, with an optional
     tolerance, for a numerical input problem.
  6. **Dropdown**: Identify a comma-separated list as the answer options for a
     dropdown problem.
  7. **Explanation**: Format text as an explanation that appears when learners
     select **Show Answer**.
  8. Open the problem in the Advanced Editor.
  9. Open a list of formatting hints.
  10. **Accessible Label**: Identify the question as the problem's accessible
      label. No toolbar option is available, but when you surround text with
      two pairs of angle brackets pointing inward (``>>question<<``), screen
      readers use that text as the accessible label for the problem. In
      addition, edX Insights uses the accessible label to identify the question
      in each problem. For more information, see `Using edX Insights`_.

.. _Advanced Editor:

===================
The Advanced Editor
===================

The **Advanced Editor** opens a problem in XML. Templates for problems such as
such as drag and drop and math expression input open directly in the Advanced
Editor.

The following image shows the multiple choice problem above in the Advanced
Editor instead of the Simple Editor.

.. image:: ../../../shared/building_and_running_chapters/Images//MultipleChoice_AdvancedEditor.png
 :alt: An image of a problem in the advanced editor.
 :width: 450

The following problem templates open in the Advanced Editor.

* :ref:`Circuit Schematic Builder` In circuit schematic problems, learners
  create and modify circuits on an interactive grid and submit computer-
  generated analyses of the circuits for grading.

* :ref:`Custom JavaScript` With custom JavaScript problems, you can create a
  custom problem or tool that uses JavaScript and add it directly into Studio.

* :ref:`Drag and Drop` Drag and drop problems require learners to drag text or
  objects to a specific location on an image.

* :ref:`Image Mapped Input` Image mapped input problems require learners to
  select a specific location on an image.

* :ref:`Math Expression Input` Math expression input problems require learners
  to enter a mathematical expression as text, such as e=m\*c^2.

* :ref:`Problem with Adaptive Hint` These problems can give learners feedback
  or hints based on their responses. Problems with adaptive hints can be text
  input or multiple choice problems.

* :ref:`Problem Written in LaTeX` This problem type allows you to convert
  problems that you previously wrote in LaTeX into the edX format. Note that
  this problem type is a prototype, and is not supported.

* :ref:`Write Your Own Grader` Custom Python-evaluated input (also called
  "write-your-own-grader" problems evaluate learners' responses using an
  embedded Python script that you create. These problems can be of any type.

.. _Problem Settings:

******************
Problem Settings
******************

In addition to the text of the problem, problems that you create using a
problem component have the following settings. To access these settings you
select **Settings** in the component editor.

.. contents::
  :local:
  :depth: 1

===============
Display Name
===============

This setting indicates the name of your problem. This name appears for learners
as a heading above the problem and as a tooltip in the learning sequence at the
top of the **Courseware** page.

.. image:: ../../../shared/building_and_running_chapters/Images/ProbComponent_LMS_DisplayName.png
 :alt: An image of the problem in a unit page from a learners's point of view.
 :width: 500

In addition, edX Insights uses the display name to identify each problem.
Unique, descriptive display names help you identify problems quickly and
accurately for analysis. For more information, see `Using edX Insights`_.

==============================
Maximum Attempts
==============================

This setting specifies the number of times that a learner is allowed to attempt
answering a problem. By default, the course-wide **Maximum Attempts**
advanced setting is null, meaning that the maximum number of attempts for
problems is unlimited. If the course-wide **Maximum Attempts** setting is
changed to a specific number, the **Maximum Attempts** setting for individual
problems defaults to that number, and cannot be set to unlimited.

.. note:: edX recommends setting **Maximum Attempts** to either unlimited or a
   very large number. Unlimited attempts allow for mastery learning and
   encourages risk taking and experimentation, both of which lead to improved
   learning outcomes. Allowing for unlimited attempts might be impossible in
   some courses, such as those where grading is primarily based on multiple
   choice questions.

.. note:: Only questions that have a **Maximum Attempts** setting of 1 or
   higher are included in the answer distribution computations used in edX
   Insights and the Student Answer Distribution report.

.. _Problem Weight:

==============================
Problem Weight
==============================

.. note:: The Learning Management System stores scores for all problems, but
  scores only count toward a learner's final grade if they are in a subsection
  that is graded.

This setting specifies the total number of points possible for the
problem. The problem weight appears next to the problem's display name.

.. image:: ../../../shared/building_and_running_chapters/Images/ProblemWeight_DD.png
 :alt: An image of a problem from a learner's point of view, with the possible
       number of points, 3, circled.
 :width: 500

By default, each response field, or "answer space", in a problem component is
worth one point. Any problem component can have multiple response fields. For
example, the problem component above contains one dropdown problem that has
three separate questions, and also has three response fields.

You can increase or decrease the weight for a problem component by entering a
**Problem Weight**.

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

A problem's **Weight** setting is left blank. The problem has two
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

For problems that include a Python script to generate numbers randomly, this
setting specifies how frequently the values in the problem change: each time a
different learner accesses the problem, each time a single learner tries to
answer the problem, both, or never.

.. note:: This setting should only be set to an option other than **Never** 
 for problems that are configured to do random number generation.

For example, in this problem, the highlighted values change each time a learner
submits an answer to the problem.

.. image:: ../../../shared/building_and_running_chapters/Images/Rerandomize.png
 :alt: An image of the same problem shown twice, with color highlighting on 
   values that change.
 :width: 800

If you want to randomize numeric values in a problem, you complete both of
these steps.

* Make sure that you edit your problem to include a Python script that randomly
  generates numbers. 

..  For more information, see :ref:`Use Randomization in a
  Numerical Input Problem`.
.. ^^ add back when DOC-2175 gets done - Alison 30 Jul 15  

* Select an option other than **Never** for the **Randomization** setting. 

.. note:: The **Randomization** setting serves a different purpose from
 "problem randomization". The **Randomization** setting affects how numeric
 values are randomized within a single problem and requires the inclusion of a
 Python script. Problem randomization offers different problems or problem
 versions to different learners. For more information, see :ref:`Problem
 Randomization`.

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
 include up to 20 variants for the problem, even if the problem was not
 actually configured to include randomly generated values. This can make data
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

This setting defines when learners are shown the answers to a problem and has
the following options

.. list-table::
   :widths: 15 70
   
   * - **Always** 
     - Always show the answer when the learner selects the **Show Answer**
       button.
   * - **Answered** 
     - Show the answer after the learner tries to answer the problem. 
       
       If the question can be, and is, reset, the answer is not shown until the
       learner tries the problem again. (When a learner answers a question, the
       question is considered to be both attempted and answered. When the
       question is reset, the question is still attempted, but not yet
       answered.)
   * - **Attempted** 
     - Show the answer after the learner tries to answer the problem.
       
       If the question can be, and is, reset, the answer continues to show.
       (When a learner answers a question, the question is considered to be
       both attempted and answered. When the question is reset, the question is
       still attempted, but not yet answered.)
   * - **Closed**
     - Show the answer after the learner has used up all his attempts to answer
       the problem or the due date has passed.
   * - **Finished**
     - Show the answer after the learner has answered the problem correctly,
       the learner has no attempts left, or the problem due date has passed.
   * - **Correct or Past Due**
     - Show the answer after the learner has answered the problem correctly or
       the problem due date has passed.
   * - **Past Due**
     - Show the answer after the due date for the problem has passed.
   * - **Past Due**
     - Never show the answer. In this case, a **Show Answer** button does not
       appear next to the problem in Studio or in the LMS.

.. _Show Reset Button:

=================
Show Reset Button
=================

This setting defines whether a **Reset** button is visible on the problem.

Learners can select **Reset** to clear any input that has not yet been
submitted, and try again to answer the problem. 

If the learner has already submitted an answer, selecting **Reset** clears the
submission and, if the problem contains randomized variables and randomization
is set to **On Reset**, changes the values in the problem. 

If the number of Maximum Attempts that was set for this problem has been
reached, the **Reset** button is not visible.

This problem-level setting overrides the course-level **Show Reset Button for
Problems** setting.

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


.. _Modifying a Released Problem:

*********************************
Modifying a Released Problem
*********************************

.. warning:: Be careful when you modify problems after they have been 
 released. Changes that you make to published problems can affect the learner
 experience in the course and analysis of course data.

After a learner submits a response to a problem, the edX Learning Management
System (LMS) stores that response, the score that the learner
received, and the maximum score for the problem. For problems with a **Maximum
Attempts** setting greater than 1, the LMS updates these values each time the
learner submits a new response to a problem. However, if you change
a problem or its attributes, existing learner information for that problem is
not automatically updated.

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
   for the problem, then ask all your learners to redo the problem.

*  Delete the entire problem component in Studio and create a new Problem
   component with the content and settings that you want, then ask all your
   learners to complete the new problem. (If the revisions you must make are
   minor, duplicate the problem component before you delete it and revise the
   copy.)

For information about how to review and adjust learner grades in the LMS, see
:ref:`Grades`.

.. _Multiple Problems in One Component:

***********************************
Multiple Problems in One Component
***********************************

You might want to create a problem that has more than one response type. For
example, you might want to create a numerical input problem and then include a
multiple choice question about that numerical input problem. Or, you might
want a learner to be able to check the answers to many problems at one time. To
do this, you can include multiple problems inside a single problem component.
The problems can be different types.

.. note:: 
  You cannot use a :ref:`Custom JavaScript` in a component that contains more
  than one problem. Each custom JavaScript problem must be in its own
  component.

To create multiple problems in one component, create a new Blank Advanced
problem component, and then add the XML for each problem in the component
editor. You only need to include the XML for the problem and its answers. You
do not have to include the code for other elements, such as the **Check**
button.

Elements such as the **Check**, **Show Answer**, and **Reset** buttons, as well
as the settings that you select for the problem component, apply to all of the
problems in that component. Thus, if you set the maximum number of attempts to
3, the learner has three attempts to answer the entire set of problems in the
component as a whole rather than three attempts to answer each problem
individually. If a learner selects **Check**, the LMS scores all of the
problems in the component at once. If a learner selects **Show Answer**, the
answers for all the problems in the component appear.

.. include:: ../../../shared/exercises_tools/Section_adding_hints.rst

.. include:: ../../../shared/exercises_tools/Section_partial_credit.rst

.. _Problem Randomization:

***********************************
Problem Randomization
***********************************

You might want to present different learners with different problems, or
different versions of the same problem. To do this, you create a problem
component for each problem or version in Studio, and then edit your course
outside of Studio, in OLX, to randomize the problem that learners see.

Note that *problem randomization* is different from the **Randomization**
setting in Studio. The **Randomization** setting controls when a Python script
within a single problem randomizes variables. Problem randomization offers
different problems or problem versions to different learners.

.. note:: Creating problems with versions that can be randomized requires you 
 to export your course, edit some of your course's XML files in a text editor,
 and then re-import your course. We recommend that you create a backup copy of
 your course before you do this. We also recommend that you only edit your
 course files in the text editor if you are very familiar with editing XML.

============
Terminology
============

Sections, subsections, units, and components have different names in the
**Course Outline** view and in the list of files that you'll see after you
export your course and open the .xml files for editing. The following table
lists the names of these elements in the **Course Outline** view and in a list
of files.

.. list-table::
   :widths: 15 15
   :header-rows: 0

   * - Course Outline View
     - File List
   * - Section
     - Chapter
   * - Subsection
     - Sequential
   * - Unit
     - Vertical
   * - Component
     - Discussion, HTML, problem, or video

For example, when you want to find a specific section in your course, look in
the **Chapter** directory when you open the list of files that your course
contains. To find a unit, look in the **Vertical** directory.

.. _Create Randomized Problems:

==========================
Create Randomized Problems
==========================

#. In the unit where you want to create a randomized problem, create a separate
   problem component for each version or problem that you want to randomize.
   For example, if you want to offer four versions or problems, create
   four separate problem components. Make a note of the 32-digit unit ID that
   appears in the **Unit Identifier** field under **Unit Location**.

#. Export your course. For more information, see
   :ref:`Exporting and Importing a Course`. Save and extract the .tar.gz file
   that contains your course in a memorable location so that you can find
   it easily.

#. In the list of directories and files, open the **Vertical** directory.

   .. note:: If your unit is not published, open the **Drafts** directory, and 
    then open the **Vertical** directory in the **Drafts** folder.

#. In the **Vertical** folder, locate the .xml file that has the same name as
   the unit ID that you noted in step 1, and then open the file in a text
   editor such as Sublime. For example, if the unit ID is
   ``e461de7fe2b84ebeabe1a97683360d31``, open the
   ``e461de7fe2b84ebeabe1a97683360d31.xml`` file.

   The file contains a list of all the components in the unit, together with
   the URL names of the components. For example, the following file contains
   four problem components.

   .. code-block:: xml
     
       <vertical display_name="Test Unit">
          <problem url_name="d9d0ceb3ffc74eacb29501183e26ad6e"/>
          <problem url_name="ea66d875f4bf4a9898d8e6d2cc9f3d6f"/>
          <problem url_name="2616cd6324704f85bc315ec46521485d"/>
          <problem url_name="88987707294d4ff0ba3b86921438d0c0"/>
       </vertical>

#. Add ``<randomize> </randomize>`` tags around the components for the problems
   that you want to randomize.

   .. code-block:: xml
      
       <vertical display_name="Test Unit">
         <randomize>
            <problem url_name="d9d0ceb3ffc74eacb29501183e26ad6e"/>
            <problem url_name="ea66d875f4bf4a9898d8e6d2cc9f3d6f"/>
            <problem url_name="2616cd6324704f85bc315ec46521485d"/>
            <problem url_name="88987707294d4ff0ba3b86921438d0c0"/>
         </randomize>
       </vertical>

#. After you add the ``<randomize> </randomize>`` tags, save and close the .xml
   file.

#. Re-package your course as a .tar.gz file.

   For information about how to do this on a Mac, see `How to Create a Tar GZip
   File from the Command Line <http://osxdaily.com/2012/04/05/create-tar-gzip/>`_.

   For information about how to do this on a Windows computer, see `How to Make
   a .tar.gz on Windows <http://stackoverflow.com/questions/12774707/how-to-make-a-tar-gz-on-windows>`_.

#. In Studio, re-import your course.

.. note::

  * After you implement randomization, you can only see one of the versions or
    problems in Studio. You can edit that single problem directly in Studio,
    but to edit any of the other problems, you must export your course, edit
    the problems in a text editor, and then re-import the course. The same
    procedure applies to all course team members, regardless of their assigned
    roles.
  
  * A .csv file for learner responses contains the responses to each of the
    problems in the problem bank.

.. include:: ../../../shared/exercises_tools/Section_adding_tooltip.rst

.. _Using edX Insights: http://edx.readthedocs.org/projects/edx-insights/en/latest/

.. _Review Answers to Graded Problems: http://edx.readthedocs.org/projects/edx-insights/en/latest/performance/Performance_Answers.html#review-answers-to-graded-problems

.. _Review Answers to Ungraded Problems: http://edx.readthedocs.org/projects/edx-insights/en/latest/performance/Performance_Ungraded.html#review-answers-to-ungraded-problems
