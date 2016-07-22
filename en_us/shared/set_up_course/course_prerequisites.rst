.. _Set Course Prerequisites:

#########################
Set Course Prerequisites
#########################

You might want to make sure that your learners have a specific set of skills
and knowledge before they take your course.

.. contents::
 :local:
 :depth: 1


.. _Specify Prerequisite Courses:

****************************
Specify Prerequisite Courses
****************************

You can require that your learners pass a particular edX course before they
enroll in your course. Learners see information about course prerequisites on
the course **About** page.

.. image:: ../../../shared/images/PrereqAboutPage.png
  :width: 500
  :alt: A course About page with prerequisite course information circled.

If learners have not completed the prerequisite course, they can enroll in your
course and then see your course on their learner dashboards. However, unlike
with other courses, the dashboard does not provide a link to the course
content. The dashboard includes a link to the **About** page for the
prerequisite course. Learners can enroll in the prerequisite course from the
**About** page.

.. image:: ../../../shared/images/Prereq_StudentDashboard.png
  :width: 500
  :alt: The learner dashboard with an available course and a course that is
      unavailable because it has a prerequisite.

To define one course as the prerequisite for another, you must be the course
creator in both the current course and in the prerequisite course.

To specify a prerequisite course, follow these steps.

#. In Studio, open your course.
#. On the **Settings** menu, select **Schedule & Details**.
#. On the **Schedule & Details** page, locate the **Requirements** section.
#. Under **Prerequisite Course**, select a course from the list.
#. Select **Save Changes**.

.. note:: Currently, you can specify only one prerequisite course.

.. _Require an Entrance Exam:

****************************
Require an Entrance Exam
****************************

You can require your learners to pass an entrance exam before they access your
course materials. If you include an entrance exam, learners who enroll in your
course can only access the **Entrance Exam** page until they pass the exam.
After learners pass the exam, they can access all released materials in your
course.

To require an entrance exam, follow these steps.

#. In Studio, open your course.
#. On the **Settings** menu, select **Schedule & Details**.
#. On the **Schedule & Details** page, locate the **Requirements** section.
#. Select the **Require students to pass an exam before accessing course
   materials** check box.
#. Select **Save Changes**.

After you save your changes, Studio automatically creates an **Entrance Exam**
section in your course outline. To add content to your entrance exam, go to the
course outline.

==================================
Best Practices for Entrance Exams
==================================

We strongly recommend that you follow several guidelines to help you and your
learners have a positive experience with entrance exams.

* Make sure that your beta testers include the entrance exam when they test
  your other course content.

* Make sure that you mention the entrance exam in the course description on
  your course **About** page. Otherwise, learners will not know about the
  entrance exam before they enroll in your course and try to access course
  content.

* Add an announcement to the **Course Updates & News** page that contains
  information and instructions for learners who need to take the exam. When
  learners first try to access content in a course that has an entrance exam,
  they see the **Course Updates & News** page. We suggest that you include the
  following information.

  * To begin the course entrance exam, learners select **Entrance Exam**.

  * After learners complete the entrance exam, they must select
    **Entrance Exam** again or refresh the page in their browsers. When the
    page refreshes, learners can see all currently available course content.

================================================
Create an Entrance Exam from the Course Outline
================================================

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
