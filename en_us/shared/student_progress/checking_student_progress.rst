.. _Checking Student Progress and Issuing Certificates:

###############
Ending a Course
###############

This topic describes how to complete several end-of-course tasks.

.. contents::
   :local:
   :depth: 1

For more information, see the following other topics about certificates.

* :ref:`Setting Up Certificates`
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


.. _Issuing Certificates:

********************
Issuing Certificates
********************

.. only:: Open_edX

  .. note::
   Before you can issue certificates, the administrator for your instance of
   Open edX must configure the platform to allow course teams to generate and
   issue certificates. For more information, see
   :ref:`installation:Generate Certificates for a Course` and
   :ref:`installation:Enable Certificates` in *Installing, Configuring, and
   Running the Open edX Platform*.

Studio automatically generates certificates for both self-paced courses and
instructor-paced courses. When certificates become available, options for
learners to view their certificates are available on the learner dashboard,
the learner **Profile** page, and the course **Progress** page.

You can specify when you want to make certificates available.

* For self-paced courses, by default, Studio generates certificates for
  learners when they have completed enough of the course, and with a high
  enough grade, to qualify for a certificate.

  If you want Studio to generate certificates only after learners have
  completed the course, you can disable this feature. For more information,
  see :ref:`Allow Learners to Receive Early Certificates`.

* For instructor-paced courses, three options are available.

 * By default, certificates become available to learners 48
   hours after your course end date. If you change your course end date,
   Studio automatically adjusts the date for certificates as well.

 * You can specify a different date to make certificates available. For more
   information, see :ref:`Specify an Alternative Certificates Available
   Date`.

 * You can allow learners to receive their certificates when they have
   completed enough of the course, and with a high enough grade, to qualify
   for a certificate. For more information, see :ref:`Allow Learners to
   Receive Early Certificates`.

.. _Issue Certificates on a Specified Date:

======================================
Issue Certificates on a Specified Date
======================================

If you do not want Studio to generate certificates 48 hours after the course
end date, you can specify the date when you want Studio to generate
certificates. You can change this date at any time.

For more information about how to specify a day to issue certificates, see
:ref:`Specify an Alternative Certificates Available Date`.

.. _Allow Learners to Receive Early Certificates:

================================================
Allow Learners to Receive Early Certificates
================================================

To allow learners to receive certificates before the course end date or before
they have completed the course, you use the **Enable Student-Generated
Certificates** setting on the instructor dashboard.

.. note::
  If the administrator has configured the site correctly (see
  :ref:`installation:Enable Automatic Certificate Generation` in
  *Installing, Configuring, and Running the Open edX Platform*),
  self-paced courses issue certificates to learners as soon as
  learners have completed enough of the course, with a high enough
  grade, to earn a certificate. You do not have to change any
  settings.

#. View the live version of your course.

#. In the LMS, select **Instructor**, and then select **Certificates**.

#. Select **Enable Student-Generated Certificates**.

   To prevent learners from receiving early certificates, select **Disable
   Student-Generated Certificates**.

.. _Allow Learners to Download Certificates:

Allow Learners to Download Early Certificates
*********************************************************

To allow learners to download early certificates, you modify the
**Certificates Display Behavior** advanced setting in Studio.

#. In Studio, on the **Settings** menu, select **Advanced Settings**.

#. On the **Advanced Settings** page, locate **Certificates Display Behavior**.

#. In the **Certificates Display Behavior** field, enter ``"early_no_info"``.
   Be sure that you include the double quotation marks.

#. Select **Save Changes**.



