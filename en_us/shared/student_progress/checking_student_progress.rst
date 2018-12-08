.. _Checking Student Progress and Issuing Certificates:

###############
Ending a Course
###############
.. This chapter will be renamed and expanded to include course wrap-up activities and best practices.

This topic describes how to complete several end-of-course tasks.

.. contents::
   :local:
   :depth: 1

For more information, see the following other topics about certificates.

* :ref:`Setting Up Course Certificates`
* :ref:`Reporting Certificate Data`

****************************************
Sending a Farewell Message
****************************************

As you prepare for the end of your course, you can send learners a :ref:`course
farewell<Course Farewell and Certificates>` email message.

**********************
Assigning Final Grades
**********************

To assign a final grade to each learner enrolled in a course, you generate
grades after the course end date and time have passed. For more information,
see :ref:`Access_grades`.

The learner's final grade and the grading configuration you set in Studio
determine whether the learner has earned a certificate for the course.

********************
Issuing Certificates
********************

Typically, you generate and issue certificates after the course ends for
instructor-paced courses, or at specific intervals for self-paced courses.

For self-paced courses, you can also allow learners to request and download
certificates before they have completed all of the course materials. To receive
these on-demand certificates, learners must have completed enough of the
course, and with a high enough grade, to qualify for a certificate.

===================================
Issue Course-Generated Certificates
===================================

.. only:: Partners

   For most courses, you work with your edX partner manager to issue
   certificates. For instructor-paced courses, you must assign final grades
   before you can issue certificates. For more information, contact your edX
   partner manager.

.. only:: Open_edX

   If the administrator of your instance of Open edX has configured your
   instance to allow course teams to generate and issue certificates, you can
   issue certificates for your course. For more information, see
   :ref:`installation:Generate Certificates for a Course`.

   If your Open edX administrator has not configured your instance to allow
   course teams to generate and issue certificates, you must work with your
   administrator to issue your course certificates. For more information, see
   :ref:`installation:Enable Certificates`.

=======================================================
Allow On-Demand Certificates (Self-Paced Courses Only)
=======================================================

You can allow your learners to receive on-demand certificates as soon as they
qualify for a certificate in your course. This process has two steps.

#. :ref:`Allow learners to request certificates<Allow Learners to Request
   Certificates>`.
#. :ref:`Allow learners to download certificates<Allow Learners to Download
   Certificates>`.

.. only:: Partners

  For information about how learners request certificates, see
  :ref:`learners:SFD On Demand Certificates`.

.. note::
  If your course offers on-demand certificates, we encourage you to include
  this information on your course About page, on the **Home** page, and in
  communication with your learners.

.. _Allow Learners to Request Certificates:

Allow Learners to Request On-Demand Certificates
********************************************************

To allow learners to request on-demand certificates, you modify the **Enable
Student- Generated Certificates** setting on the Instructor Dashboard.

#. View the live version of your course.

#. In the LMS, select **Instructor**, and then select **Certificates**.

#. Select **Enable Student-Generated Certificates**.

   When they have qualified, learners can request their certificates from the
   **Progress** page.

   To prevent learners from requesting certificates, select **Disable
   Student-Generated Certificates**.

.. _Allow Learners to Download Certificates:

Allow Learners to Download On-Demand Certificates
*********************************************************

To allow learners to download on-demand certificates, you modify the
**Certificates Display Behavior** advanced setting in Studio.

#. In Studio, on the **Settings** menu, select **Advanced Settings**.

#. On the **Advanced Settings** page, locate **Certificates Display Behavior**.

#. In the **Certificates Display Behavior** field, enter ``"early_no_info"``.
   Be sure that you include the double quotation marks.

#. Select **Save Changes**.
