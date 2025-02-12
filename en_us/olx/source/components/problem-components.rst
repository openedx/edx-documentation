.. _Problem Components:

#################################
Problem Components
#################################

The problem component allows you to add interactive exercises to the verticals
in your course. You can add many different types of exercises and problems.
This section covers the basics of problem components: what they look like to
you and your learners, and the options that every problem component has.

.. contents::
   :local:
   :depth: 1

*********************************************
Problem Component Overview
*********************************************

The format for edX problems is based on the `LON-CAPA XML format`_, although
the two are not quite compatible. In the edX variant, problems are composed of
the following types of tags.

* ``inputtypes`` are similar to XBlocks. They define ways for users to enter
  input into the problem.
* ``responsetypes`` are graders. They define how inputs are mapped to grades.
* ``hinters`` are used to provide feedback to problems.
* Standard HTML tags are used for formatting.

OLX is designed to allow mixing and matching of ``inputtypes``,
``responsetypes``, and ``hinters``. For example, a numerical grader could match
7+-0.1%. Ideally, you could use this grader with any ``inputtype`` that returns
numbers as its output, including a text box, equation input, slider, or
multiple choice question. In practice, this does not always work. For example,
in the example described above, a multiple choice question would not give an
output in a format a numerical grader could handle.

In addition, in many cases, there is a 1:1 mapping between graders and inputs.
For some types of inputs (especially discipline-specific specialized ones),
only one grader is needed.

The most general grader is ``customresponse``. This grader uses Python code to
evaluate the input. By design, this ought to work with any inputtype, although
there are bugs mixing this with a small number of the newer inputtypes.

Like LON-CAPA, OLX allows embedding of code to generate parameterized problems.
Unlike LON-CAPA, edX supports Python (and not Perl). Otherwise, the syntax for
parameterizing problems is approximately identical.


=====================================
Creating Graded or Ungraded Problems
=====================================

All problems receive a point score. However, when you establish the grading
policy for your course, you specify the assignment types that will count toward
learners' grades; for example, homework, lab, midterm, and final.

As you develop your course, you can add problem components to the units in any
subsection. The problem components that you add automatically inherit the
assignment type that is defined at the subsection level. You can only set
assignment types at the subsection level, not at the unit or individual
component level.

For more information, see :ref:`Grading Policy`.

.. _Problem Student View:

.. include:: ../../../shared/course_components/Section_learner_problem_view.rst

******************
Problem Settings
******************

In addition to the text of the problem, problems that you create have the
following settings.

.. contents::
  :local:
  :depth: 1

This section describes the OLX elements and attributes that you define for the
problem settings. For a detailed description of each setting, see
:ref:`Problem Settings`.

===============
Display Name
===============

Using OLX, you set the display name as an attribute of the ``<problem>``
element.

.. code-block:: xml

  <problem display_name="Geography Homework"></problem>

==============================
Maximum Attempts
==============================

Using OLX, you set the maximum attempts as an attribute of the ``<problem>``
element.

.. code-block:: xml

  <problem max_attempts="3"></problem>


.. _Problem Weight:

==============================
Problem Weight
==============================

Using OLX, you set the component weight as an attribute of the ``<problem>``
element.

.. code-block:: xml

  <problem weight="2.0"></problem>

.. _Randomization:

===============
Randomization
===============

Using OLX, you set value randomization as an attribute of the ``<problem>``
element.

.. code-block:: xml

  <problem rerandomize="always"></problem>

You can specify the following values for this attribute.

* always
* on_reset
* never
* per_student

.. _Show Answer:

===============
Show Answer
===============

Using OLX, you set the show answer preference as an attribute of the
``<problem>`` element.

.. code-block:: xml

  <problem showanswer="correct_or_past_due"></problem>

You can specify the following values for this attribute.

* always
* answered
* attempted
* closed
* correct_or_past_due
* finished
* past_due
* never

.. _Show Reset Button:

=================
Show Reset Button
=================

Using OLX, you set the show reset button preference as an attribute of the
``<problem>`` element.

.. code-block:: xml

  <problem show_reset_button="true"></problem>

.. _Modifying a Released Problem:

*********************************
Modifying a Released Problem
*********************************

.. warning:: Be careful when you modify problems after they have been
 released! Changes that you make to published problems can affect the learner
 experience in the course and analysis of course data.

After a learner submits a response to a problem, the LMS stores the learner's
response, the score that the learner received, and the maximum score for the
problem. For problems with a **Maximum Attempts** setting greater than 1, the
LMS updates these values each time the learner submits a new response to a
problem. However, if you change a problem or its attributes,
existing learner information for that problem is not automatically updated.

For example, you might release a problem and specify that its answer is 3.
After some learners have submitted responses, you notice that the answer
should be 2 instead of 3. When you update the problem with the correct
answer, the LMS does not update scores for learners who answered 2 for the
original problem and thus received the wrong score.

For another example, you might change the number of response fields to
three. Learners who submitted answers before the change have a score of
0, 1, or 2 out of 2.0 for that problem. Learners who submitted answers
after the change have scores of 0, 1, 2, or 3 out of 3.0 for the same
problem.

If you change the weight setting for the problem in Studio, however, existing
learner scores update when the learner's **Progress** page is refreshed. In a
live section, learners will see the effect of these changes.

===============
Workarounds
===============

If you have to modify a released problem in a way that affects grading, you
have two options within Studio to assure that every learner has the opportunity
to submit a new response and be regraded. Note that both options require you to
ask your learners to go back and resubmit answers to a problem.

*  In the problem component that you changed, increase the number of attempts
   for the problem. Then ask all your learners to redo the problem.

*  Delete the entire Problem component in Studio and create a new Problem
   component with the content and settings that you want. (If the revisions you
   must make are minor, duplicate the problem component before you delete it
   and revise the copy.) Then ask all your learners to complete the new
   problem.


.. _Multiple Problems in One Component:

***********************************
Multiple Problems in One Component
***********************************

You can create a problem that includes more than one response type. For
example, you might want to create a numerical input problem and then include a
multiple choice problem that refers to the numerical input problem. Or,
you might want a learner to be able to check the answers to many problems at
one time. To do this, you can include multiple problems inside a single
``<problem>`` element. The problems can be different types.

Each question and its answer options are enclosed by the element that
identifies the type of problem, such as ``<multiplechoiceresponse>`` for a
multiple choice question or ``<formularesponse>`` for a math expression input
question.

You can provide a different explanation for each question by using the
``<solution>`` element.

As a best practice, edX recommends that you avoid including unformatted
paragraph text between the questions. Screen readers can skip over text that is
inserted among multiple questions.

Elements such as the **Submit**, **Show Answer**, and **Reset** buttons, as
well as the settings that you select for the problem component, apply to all
of the problems in that component. Thus, if you set the maximum number of
attempts to 3, the learner has three attempts to answer the entire set of
problems in the component as a whole rather than three attempts to answer each
problem individually. If a learner selects **Submit**, the LMS scores all of
the problems in the component at once. If a learner selects **Show Answer**,
the answers for all the problems in the component appear.

.. note::
  You cannot use a :ref:`Custom JavaScript` in a component that contains more
  than one problem. Each custom JavaScript problem must be in its own
  component.

.. include:: ../../../shared/exercises_tools/Section_adding_hints.rst

.. include:: ../../../shared/exercises_tools/Section_partial_credit.rst

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
   in Studio. Problem randomization offers different problems or problem
   versions to different learners, whereas the **Randomization** setting
   controls when a Python script randomizes the variables within a single
   problem. For more information about the **Randomization** setting, see
   :ref:`Randomization`.


.. _Create Randomized Problems:

====================================
Create Randomized Problems
====================================

.. note:: Creating randomized problems by exporting your course and editing
   some of your course's XML files is no longer supported.

You can provide different learners with different problems by using randomized
content blocks, which randomly draw problems from pools of problems stored in
content libraries. For more information, see
:ref:`partnercoursestaff:Randomized Content Blocks`.

.. include:: ../../../shared/exercises_tools/Section_adding_tooltip.rst

.. include:: ../../../links/links.rst
