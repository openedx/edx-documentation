.. _Awarding Partial Credit for a Problem:

***************************************
Awarding Partial Credit for a Problem
***************************************

You can configure the following problem types so that learners can receive
partial credit for a problem if they submit an answer that is partly correct.

* :ref:`Checkbox <Awarding Partial Credit in a Checkbox Problem>`
* :ref:`Multiple Choice <Awarding Partial Credit in a Multiple Choice Problem>`
* :ref:`Numerical Input <Awarding Partial Credit in a Numerical Input Problem>`
* :ref:`Write-Your-Own Grader <Award Half Credit>`

By awarding partial credit for problems, you can motivate learners who have
mastered some of the course content and provide a score that accurately
demonstrates their progress.

For more information about configuring partial credit, see the topic for each
problem type.

.. only:: Partners

  .. note::
    Support for partial credit problems in courses on edx.org and edX
    Edge is provisional. Ensure that you test such problems thoroughly before
    releasing them to learners. For more information, contact your edX program
    manager.

==========================================
How Learners Receive Partial Credit
==========================================

Learners receive partial credit when they submit an answer in the LMS.

In the following example, the course team configured a multiple choice problem
to award 25% of the possible points (instead of 0 points) for one of the
incorrect answer options. The learner selected this incorrect option, and
received 25% of the possible points.

.. image:: ../../../shared/images/partial_credit_multiple_choice.png
 :alt: Image of a multiple choice problem with partial credit for an incorrect
     answer.
 :width: 500


====================================================
Partial Credit and Reporting on Learner Performance
====================================================

When a learner receives partial credit for a problem, the LMS only adds the
points that the learner earned to the grade. However, the LMS reports any
problem for which a learner receives credit, in full or in part, as correct in
the following ways.

* Events that the system generates when learners receive partial credit for a
  problem indicate that the answer was correct. Specifically, the
  ``correctness`` field has a value of ``correct``.

  For more information about events, see `Problem Check Event`_ in
  the *EdX Research Guide*.

* The **AnswerValue** in the :ref:`Student_Answer_Distribution` report is
  **1**, for correct.

* The edX Insights `student performance reports`_ count the answer as
  correct.

Course teams can see that a learner received partial credit for a problem in
the learner's submission history. The submission history shows the score that
the learner received out of the total available score, and the value in the
``correctness`` field is ``partially-correct``.  For more information, see
:ref:`Student_Answer_Submission`.


.. _Problem Check Event: http://edx.readthedocs.org/projects/devdata/en/latest/internal_data_formats/tracking_logs.html#problem-check-server

.. _student performance reports: http://edx.readthedocs.org/projects/edx-insights/en/latest/performance/index.html
