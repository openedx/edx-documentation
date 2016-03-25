.. _Timed Exams:

###################
Timed Exams
###################

This topic describes how to add and manage timed exams in your course.

.. contents::
  :local:
  :depth: 2

**********
Overview
**********

You can configure a :ref:`subsection <Developing Course Subsections>`
in your course so that learners have a set amount of time to complete and
submit all problems in that subsection.

If a learner goes over the time limit you set, she can no longer submit
answers to problems in that subsection. The learner does not receive points for
unsubmitted problems.

Course teams can grant individual learners more time to complete problems in
the subsection.

.. note::
  Although you can configure an ungraded subsection to be timed, typically
  you would set a time limit on graded subsections, such as for mid-term or
  final exams.

.. only:: Partners

  Timed exams are different than :ref:`proctored exams<CA_ProctoredExams>`.
  While both types of exams have a time limit, learners are only monitored
  during proctored exams.

*******************
Enable Timed Exams
*******************

To enable timed exams in your course, follow these steps.

#. In Studio, select **Settings**, then select **Advanced Settings**.

#. Locate the **Enable Timed Exams** field. The default value is ``false``.

#. Change the value of the setting to ``true``.

#. Select **Save Changes**. You can now create timed exams in your course.

*****************************
Set a Subsection to be Timed
*****************************

Ensure that you have enabled timed exams in the course. Then follow these
steps.

#. Add and :ref:`develop a subsection <Developing Course Subsections>` as you
   would any other subsection.

#. Select the **Configure** icon for the subsection.

   .. image:: ../../../shared/images/subsections-settings-icon.png
    :alt: A subsection in the course outline with the configure icon indicated.
    :width: 600

   The **Settings** dialog box opens to the **Basic** tab.

#. In the **Grading** section, set the :ref:`assignment type and due date<Set
   the Assignment Type and Due Date for a Subsection>` for the subsection.

#. Select the **Advanced** tab.

#. In the **Set as a Special Exam** section, select **Timed**.

   .. only:: Partners

     If your course has the proctored exam feature enabled, the
     **Advanced** tab also shows options for :ref:`proctored and practice
     proctored exams<CA_ProctoredExams>`.

#. In the **Time Allotted** field, enter the length of time that you want
   learners to have to complete the problems in the subsection. Enter the time
   as HH:MM, where HH is hours and MM is minutes.

#. Select **Save**.

*****************************************
Grant Learners More Time for a Timed Exam
*****************************************

From the instructor dashboard, a course team member can grant a learner
extra time to complete a timed exam.

#. View the live version of your course.

#. Select **Instructor**, and then select **Special Exams**.

#. Expand the **Allowance Section**.

   .. image:: ../../../shared/images/inst_dash_special_exams.png
    :alt: The Allowance Section in the Instructor Dashboard.
    :width: 600

#. Select **Add Allowance**.

   .. image:: ../../../shared/images/new_allowance.png
    :alt: The Allowance Section in the Instructor Dashboard.
    :width: 400

#. Select the subsection that contains the timed exam.

#. For **Allowance Type**, select **Additional Time (minutes)**.

#. In the **Value** field, enter the number of extra minutes that you are
   granting the learner.

   .. note:: Enter a whole number greater than 0.

#. Enter the learner's **Username** or **Email**.

#. Select **Save**.
