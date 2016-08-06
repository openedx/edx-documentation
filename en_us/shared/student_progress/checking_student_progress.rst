.. _Checking Student Progress and Issuing Certificates:

#####################################################
Assign Final Grades and Enable On-Demand Certificates
#####################################################
.. This chapter will be renamed and expanded to include course wrap-up activities and best practices.

This topic describes how to assign grades and issue certificates to learners in
your course.

.. contents::
   :local:
   :depth: 1

For more information, see the following other topics about certificates.

* :ref:`Setting Up Course Certificates`
* :ref:`Reporting Certificate Data`

****************************************
Overview
****************************************

As you prepare for the end of your course, you can send learners a :ref:`course
farewell<Course Farewell and Certificates>` email message.

To assign a final grade to each learner enrolled in a course, you generate
grades after the **Course End Date** and **Time** have passed. For more
information, see :ref:`Access_grades`.

The learner's final grade and the grading configuration you set in Studio are
used to determine whether the learner has earned a certificate for the course.

****************************************
On-Demand Certificates
****************************************

If you have a self-paced course, you can allow your learners to request their
certificates as soon as they have completed enough of the course with a high
enough grade to qualify for a certificate. Learners might want to request a
certificate right away, or they might wait until they have completed the
course.

========================================
Allow Learners to Request Certificates
========================================

To allow learners to request certificates from the **Progress** page, follow
these steps.

#. View the live version of your course.

#. Select **Instructor**, and then select **Certificates**.

#. Select **Enable Student-Generated Certificates**.

   When they have qualified, learners can request their certificates from the
   **Progress** page.

   To prevent learners from requesting certificates, select **Disable Student-
   Generated Certificates**.

.. only:: Partners

  For information about how learners request certificates, see
  :ref:`learners:SFD On Demand Certificates`.

=====================================================
Communicate to Learners about Requesting Certificates
=====================================================

If your course offers on-demand certificates, we encourage you to include this
information on your course About page, on the **Home** page, and in
communication with your learners.

.. only:: Partners

   Course teams should also discuss additional self-paced settings with their
   edX partner manager during the course announcement process.

==============================================================
Allow Learners to Download Certificates when They Qualify
==============================================================

To allow learners to download certificates from the dashboard when they qualify
for them, you must modify the **Certificates Display Behavior** advanced
setting in Studio.

#. From the **Settings** menu, select **Advanced Settings**.

#. On the **Advanced Settings** page, locate **Certificates Display Behavior**.

#. In the **Certificates Display Behavior** field, enter ``"early_no_info"``.
   Be sure that you include the double quotation marks.

#. Select **Save Changes**.
