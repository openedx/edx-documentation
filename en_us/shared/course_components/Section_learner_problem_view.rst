.. _Section_learner_problem_view:

************************************
The Learner View of a Problem
************************************

All problems on the edX platform have several component parts.

.. image:: ../../../shared/images/AnatomyOfExercise1.png
  :alt: A problem from a learner's point of view, with numbered callouts for
       elements of the problem.
  :width: 400

#. **Problem text.** The problem text can contain any standard HTML formatting.

#. **Response field.** Learners enter answers in response fields. The
   appearance of the response field depends on the type of the problem.

#. **Rendered answer.** For some problem types, the LMS uses MathJax to render
   plain text as "beautiful math."

#. **Check.** The learner selects **Check** to submit a response or find out if
   his answer is correct. If the answer is correct, a green check mark appears.
   If it is incorrect, a red X appears. When a learner selects **Check**, the
   LMS saves the grade and current state of the problem.

#. **Save.** The learner can select **Save** to save his current response
   without submitting it for a grade. This allows the learner to stop working
   on a problem and come back to it later.

#. **Show Answer.** This button is optional. When the learner selects **Show
   Answer**, the learner sees both the correct answer (see 2 above) and the
   explanation (see 10 below). You define whether the **Show Answer** button is
   visible.

#. **Attempts.** You can set a specific number of attempts or allow unlimited
   attempts for a problem. By default, the course-wide **Maximum Attempts**
   advanced setting is null, meaning that the maximum number of attempts for
   problems is unlimited. If the course-wide **Maximum Attempts** setting is
   changed to a specific number, the **Maximum Attempts** setting for
   individual problems defaults to that number, and cannot be set to unlimited.

   .. image:: ../../../shared/images/AnatomyOfExercise2.png
    :alt: A problem from a learner's point of view, with numbered callouts for
          attempts and showing the answer.
    :width: 500

#. **Feedback.** After a learner selects **Check**, all problems return a green
   check mark or a red X.

#. **Correct answer.** Most problems require that you specify a single correct
   answer.

#. **Explanation.** You can include an explanation that appears when a learner
   selects **Show Answer**.

#. **Reset.** Learners can select **Reset** to clear any input that has not yet
   been submitted, and try again to answer the question.

   * If the learner has already submitted an answer, selecting **Reset** clears
     the submission and, if the problem includes a Python script to randomize
     variables and the randomization setting is **On Reset**, changes the
     values the learner sees in the problem.

   * If the number of **Maximum Attempts** that was set for this problem has
     been reached, **Reset** is not visible.

#. **Hide Answer.**

   .. image:: ../../../shared/images/AnatomyOfExercise3.png
    :alt: A section and its subsections in the course navigation pane, with
        numbered callouts for the graded content icon and the due date.
    :width: 200

#. **Grading.** You can specify whether a group of problems is graded. If a
   group of problems is graded, an icon of a pen and a piece of paper appears
   or that assignment in the course navigation pane.

#. **Due date.** The date that the problem is due. A problem that is past due
   does not offer a **Check** option. It also does not accept answers or
   provide feedback.

.. note:: Problems can be **open** or **closed**. Closed problems do not
          have a **Check** option. Learners can still see questions, solutions,
          and revealed explanations, but they cannot check their work, submit
          responses, or change an earlier score.

There are also some attributes of problems that are not immediately
visible. You can set these attributes in Studio.

* **Accessible Label.** In the problem text, you can identify the text that is,
  specifically, the question that learners need to answer. The text that is
  labeled as the question is used by screen readers, reports, and Insights. For
  more information, see :ref:`Simple Editor`.

*  **Randomization.** In certain types of problems, you can include a Python
   script to randomize the values that are presented to learners. You use this
   setting to define when values are randomized. For more information, see
   :ref:`Randomization`.

*  **Weight.** Different problems in a particular problem set can be
   given different weights.
