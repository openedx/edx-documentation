.. _Section_learner_problem_view:

************************************
The Learner View of a Problem
************************************

All problems on the edX platform have these component parts, some of which can
be configured. For configurable options, you can specify whether and when
an option is available in problems.

.. image:: ../../../shared/images/AnatomyOfExercise.png
  :alt: A problem from a learner's point of view, with numbered callouts for
       elements of the problem.
  :width: 600

#. **Problem text.** The problem text can contain any standard HTML
   formatting.

   Within the problem text for each problem component, you must identify a
   question or prompt, which is, specifically, the question that learners need
   to answer. This question or prompt also serves as the required accessible
   label, and is used by screen readers, reports, and Insights. For more
   information about identifying the question text in your problem, see
   :ref:`Simple Editor`.

#. **Response field.** Learners enter answers in response fields. The
   appearance of the response field depends on the type of the problem.

#. **Rendered answer.** For some problem types, the LMS uses MathJax to render
   plain text as "beautiful math."

#. **Submit.** When a learner selects **Submit** to submit a response for a
   problem, the LMS saves the grade and current state of the problem. The
   LMS immediately provides feedback about whether the response is correct
   or incorrect, as well as the problem score. The **Submit** option remains
   available if the learner has unused attempts remaining, so that they can
   try to answer the problem again.

     .. note::
       If you want to temporarily or permanently hide learners' results for
       the problem, see :ref:`Problem Results Visibility`.

#. **Attempts.** You can set a specific number of attempts or allow unlimited
   attempts for a problem. By default, the course-wide **Maximum Attempts**
   advanced setting is null, meaning that the maximum number of attempts for
   problems is unlimited.

   In courses where a specific number has been specified for **Maximum
   Attempts** in Advanced Settings, if you do not specify a value for **Maximum
   Attempts** for an individual problem, the number of attempts for that
   problem defaults to the number of attempts defined in Advanced Settings.

#. **Save.** The learner can select **Save** to save their current response
   without submitting it for grading. This allows the learner to stop working
   on a problem and come back to it later.

#. **Reset.** You can specify whether the **Reset** option is available for a
   problem. This setting at the problem level overrides the default setting
   for the course in **Advanced Settings**.

   If the **Reset** option is available, learners can select **Reset** to
   clear any input that has not yet been submitted, and try again to answer
   the question.

   * If the learner has already submitted an answer, selecting **Reset** clears
     the submission and, if the problem includes a Python script to randomize
     variables and the randomization setting is **On Reset**, changes the
     values the learner sees in the problem.

   * If the problem has already been answered correctly, **Reset** is not
     available.

   * If the number of **Maximum Attempts** that was set for this problem has
     been reached, **Reset** is not available.

#. **Show Answer.** You can specify whether this option is available for a
   problem. If a learner selects **Show Answer**, the learner sees both the
   correct answer and the explanation, if any.

   If you specify a number in **Show Answer: After Some Number of Attempts**, the learner
   must submit at least that number of attempted answers before the **Show 
   Answer** option is available for the problem.

#. **Feedback.** After a learner selects **Submit**, an icon appears beside
   each response field or selection within a problem. A green check mark
   indicates that the response was correct, a green asterisk (*) indicates that
   the response was partially correct, and a red X indicates that the response
   was incorrect. Underneath the problem, feedback text indicates whether the
   problem was answered correctly, incorrectly, or partially correctly, and
   shows the problem score.

   .. image:: ../../../shared/images/AnatomyOfExercise2.png
     :alt: A problem from a learner's point of view, with callouts showing the
           feedback elements of an answered problem.
     :width: 600

   .. note::
     If you want to temporarily or permanently hide learners' results for
     the problem, see :ref:`Problem Results Visibility`.

In addition to the items above, which are shown in the example, problems also
have the following elements.

* **Correct answer.** Most problems require that you specify a single correct
  answer.

     .. note::
       If you want to temporarily or permanently hide learners' results for
       the problem, see :ref:`Problem Results Visibility`.

* **Explanation.** You can include an explanation that appears when a learner
  selects **Show Answer**.

* **Grading.** You can specify whether a group of problems is graded.

* **Due date.** The date that the problem is due. Learners cannot submit
  answers for problems whose due dates have passed, although they can select
  **Show Answer** to show the correct answer and the explanation, if any.

.. note::
   Problems can be **open** or **closed**. Closed problems, such as problems
   whose due dates are in the past, do not accept further responses and cannot
   be reset. Learners can still see questions, solutions, and revealed
   explanations, but they cannot submit responses or reset problems.

There are also some attributes of problems that are not immediately
visible. You can set these attributes in Studio.

* **Accessible Label.** Within the problem text, you can identify the text
  that is, specifically, the question that learners need to answer. The text
  that is labeled as the question is used by screen readers, reports, and
  Insights. For more information, see :ref:`Simple Editor`.

* **Randomization.** In certain types of problems, you can include a Python
  script to randomize the values that are presented to learners. You use this
  setting to define when values are randomized. For more information, see
  :ref:`Randomization`.
