.. _Specify Prerequisite Courses and Exams:

#########################################
Specifying Prerequisite Courses and Exams
#########################################

In Studio, you can specify that learners must complete a specific edX course
before they can take another edX course. You can also require learners to
complete an entrance exam before they can access your course content.

For more information about course prerequisite options, see :ref:`Set Course
Prerequisites`.

.. _Specify Prerequisite Courses:

****************************
Prerequisite edX Courses
****************************

To define one course as the prerequisite for another, you must be the course
creator in both the current course and in the prerequisite course.

To specify a prerequisite course, follow these steps.

#. In Studio, open your course.
#. On the **Settings** menu, select **Schedule & Details**.
#. On the **Schedule & Details** page, locate the **Requirements** section.
#. Under **Prerequisite Course**, select a course from the list.
#. Select **Save Changes**.

.. note:: Currently, you can specify only one prerequisite course.

For more information about prerequisite edX courses, see :ref:`Prerequisite edX
Courses`.

.. _Require an Entrance Exam:

****************************
Require an Entrance Exam
****************************

To require an entrance exam, follow these steps.

#. In Studio, open your course.
#. On the **Settings** menu, select **Schedule & Details**.
#. On the **Schedule & Details** page, locate the **Requirements** section.
#. Select the **Require students to pass an exam before accessing course
   materials** option.
#. Select **Save Changes**.

After you save your changes, Studio automatically creates an **Entrance Exam**
section in your course outline. To add content to your entrance exam, go to the
course outline.

=======================
Create an Entrance Exam
=======================

You create your course entrance exam from the course outline in Studio.
Creating entrance exam content is just like creating other course content. For
more information, see :ref:`Course Components Index`.

==================================
Adjust Scores in the Entrance Exam
==================================

If you find an error in the exam after learners have taken it, and corrections
to the exam are unavoidable, you have several options to rescore the exam for
individual learners. These options are available on the instructor dashboard.

In the LMS, select **Instructor** to access the instructor dashboard, and then
select **Student Admin**. In the **Entrance Exam Grade Adjustment** section,
the following options are available.

* **Reset Student Attempts**: Reset the value for one particular learner's
  attempts back to zero so that the learner can begin work over again. For more
  information, see :ref:`reset_attempts`.

* **Rescore Student Submission**: Rescore the responses that a learner has
  submitted. For more information, see :ref:`rescore`.

* **Delete Student State for Problem**: Delete a learner's entire history for
  the exam from the database. For more information, see :ref:`delete_state`.

Another option on the instructor dashboard is **Show Background Task History
for Student**. If you reset learner attempts, rescore learner submissions, or
delete learner state, the operation runs in the background. If you want to see
a record of all the operations that have run for the entrance exam, select
**Show Background Task History for Student**.
