.. _Awarding Partial Credit for a Problem:

***************************************
Awarding Partial Credit for a Problem
***************************************

You can configure the following problem types so that learners can receive
partial credit for a problem if they submit an answer that is partly correct.

* :ref:`Checkbox`
* :ref:`Dropdown`
* :ref:`Multiple Choice`
* :ref:`Numerical Input`

By awarding partial credit for problems, you can motivate learners who have
mastered some of the course content and provide a score that accurately
demonstrates their progress.

For more information about configuring partial credit, see the topic for each
problem type.
  
==========================================
How Learners Receive Partial Credit
==========================================

Learners receive partial credit when submitting an answer in the LMS.

In the following example, the learner selected a wrong answer to a multiple
choice problem and received 25% of the points.

.. image:: ../../../shared/building_and_running_chapters/Images/partial_credit_multiple_choice.png
 :alt: Image of a multiple choice problem with partial credit for an incorrect
     answer.
 :width: 600

.. note:: 
  The course team configured the problem to award 25% of the points for this
  answer.

====================================================
Partial Credit and Reporting on Learner Performance
====================================================

When a learner is awarded partial credit for a problem, only the points earned are added to the grade. However, any problem for which credit is given, in
full or in part, is reported as correct in the following ways.

* Events generated when learners receive partial credit for a problem are
  marked as correct. Specifically, the ``correctness`` field value is
  ``correct``.

  For more information about events, see the `Problem Interaction Events`_ in
  the *EdX Research Guide*.

* The **AnswerValue** in the :ref:`Student_Answer_Distribution` report is
  **1**, for correct.

* The answer is counted as correct in the edX Insights `student performance
  reports`_.

Course teams can see that a learner received partial credit for a problem in
the learner's submission history. The score the learner received out of the
total available score is displayed and the value of the ``correctness`` field
is ``partially-correct``.  For more information, see
:ref:`Student_Answer_Submission`.


.. _Problem Interaction Events: http://edx.readthedocs.org/projects/devdata/en/latest/internal_data_formats/tracking_logs.html#problem-interaction-events 

.. _student performance reports: http://edx.readthedocs.org/projects/edx-insights/en/latest/performance/index.html
