.. _Student Data:

############################
Learner Data
############################

You can access data about the individuals who are enrolled in your course at
any time after you create the course.

.. contents::
  :local:
  :depth: 2

To supplement the learner data that is available from the instructor dashboard
in the LMS, you can use the charts and reports that are available from edX
Insights. With Insights, you can review demographic and geographic
distributions for enrolled learners. You can also monitor learner activity and
review the number of learners who, each week, interacted with your course. For
more information, see :ref:`Using edX Insights<insights:Overview>`.

.. _PII:

***************************************************************
Guidance for Working with Personal Information
***************************************************************

The information that edX collects from site registrants includes personal
information that can be used to identify, contact, and locate individuals. This
information is available to course team members with the Admin or Staff role
for the learners who are enrolled in their courses.

Members of the course team should follow the policies established by their
organizations and comply with the legal requirements of their locales to
prevent public distribution or misuse of this information.

.. _Access_student_data:

****************************
Accessing Learner Data
****************************

In the LMS, you can download data about the individuals who are currently
enrolled in your course in a .csv (comma-separated values) file. For courses
that have fewer than 200 learners enrolled, you can also view data for enrolled
learners on the instructor dashboard. For more information, see :ref:`View and
download student data`.

For information about course enrollment, see :ref:`Enrollment`.

===========================
About Learner-Reported Data
===========================

When learners create, or register, their user accounts, they select a public
username and supply their full names and email addresses. Learners also have
the option to provide personal demographic information, including highest
level of education completed, gender, year of birth, and preferred language.
Because this information is optional, not all of the learners who are enrolled
in your course provide it.

After learners create an account, they can enroll in as many individual courses
as they choose.

* The learner data that is available from the instructor dashboard reflects the
  set of live, current enrollments. Data for the course team, wha are also
  enrolled in the course, is included.

* Learners can enroll in your course throughout the defined enrollment period,
  and they can unenroll from a course at any time.

* Learners can update their personal information at any time on the
  :ref:`Account Settings<SFD Account Settings>` page.

As a result, you might want to download learner data periodically to gain an
understanding of how the learner population changes over time.

.. _Columns in the Student Profile Report:

============================================
Columns in the Student Profile Report
============================================

The student profile report includes a row for each enrolled learner or course
team member and the following columns.

.. only:: Open_edX

 The descriptions of columns in the following table apply to edx.org. Required
 or optional fields shown to learners during registration and available for
 editing in **Account Settings** might vary for Open edX sites.


.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Column
     - Description
   * - id
     - The user account ID number that the system assigns to each registrant.
   * - username
     - The public username entered by the learner. Usernames are required and
       cannot be changed.
   * - name
     - The full name entered by the learner. A name is required. Learners can
       update this value on the **Account Settings** page.
   * - email
     - The email address entered by the learner. An email address is required.
       Learners can update this value on the **Account Settings** page.
   * - language
     - This column is included for backward compatibility only. This data is
       no longer collected during account creation. The selection that a
       learner makes for language on the **Account Settings** page is not
       included in this report.
   * - location
     - This column is included for backward compatibility only. The selection
       that a learner makes for **Country** during registration or for
       **Country or Region** on the **Account Settings** page is displayed in
       the "country" column of this report.
   * - year_of_birth
     - This value is optional and can be updated on the **Account Settings**
       page.
   * - gender
     - This value is optional and can be updated on the **Account Settings**
       page.
   * - level_of_education
     - This value is optional and can be updated on the **Account Settings**
       page. For a list of the possible values, see the description of the
       :ref:`data:auth_userprofile` table's level_of_education column in the
       *EdX Research Guide*.
   * - mailing_address
     - No longer collected during registration. Previously, this value was
       optional and was supplied only at registration.
   * - goals
     - This value is optional and is supplied only at registration.
   * - enrollment_mode
     - Indicates the enrollment track that the learner is enrolled in, such as
       "audit" or "verified".
   * - verification_status

     - Indicates whether learners who are enrolled in course tracks that require
       ID verification have successfully verified their identities to edX by
       submitting an official photo ID via webcam. The value in this column is
       "N/A" for learners enrolled in course tracks that do not require ID
       verification.

       A value of "Not ID Verified" in this column indicates that the learner is
       enrolled in a course track that requires ID verification (such as
       "verified") but she has not attempted ID verification, or the ID
       verification has failed or expired.

       A value of "ID Verified" indicates that the learner is enrolled in a
       course track that requires ID verification, and her ID verification is
       current and valid.

   * - cohort
     - This column is included only if the course has cohorts enabled. For
       courses that include learner cohorts, shows the name of the cohort group
       that is assigned to the learner. If a learner is not assigned to a
       cohort, the value is ``[unassigned]``.
   * - team
     - This column is included only if the course has teams enabled. For courses
       that include teams, shows the name of the team that the learner belongs
       to. If a learner has not joined a team, the value is ``[unavailable]``.
   * - city
     - Data for this column is not currently collected on edx.org.
   * - country
     - Learners are required to specify **Country** during registration, and can
       update this value on the **Account Settings** page.



.. _View and download student data:

==========================================
Download or View Learner Data
==========================================

You can download a report of learner data to gain more information about the
individuals who are enrolled in your course. For courses with fewer than 200
learners enrolled, you also have the option to view learner data on the
instructor dashboard.

Download Learner Data
***********************

To download learner data, follow these steps.

#. View the live version of your course.

#. Select **Instructor**, and then select **Data Download**.

#. To download data about enrolled learners in a .csv file, select **Download
   profile information as a CSV**.

   A status message indicates that report generation is in progress. The number
   of learners enrolled in your course, and whether your course has the cohort
   feature enabled, affect how long this process takes. This process can take
   some time to complete, but you can navigate away from this page and do other
   work while it runs.

   To track the progress of the report process, reload the page in your browser
   and scroll down to the **Pending Tasks** section.

#. To open or save a student profile report, select the
   ``{course_id}_student_profile_info_{date}.csv`` file name at the bottom of
   the page.

   All learner-supplied data is included in this file without truncation. For
   more information, see :ref:`Columns in the Student Profile Report`.

View Learner Data
***********************

To view learner data, follow these steps.

.. note:: This option is available only for courses with an enrollment of less
 than 200.

#. View the live version of your course.

#. Select **Instructor**, and then select **Data Download**.

#. To display data about enrolled learners, select **List enrolled students'
   profile information**.

   A table of profile data displays, with one row for each enrolled learner.
   Longer values, such as goals, are truncated. For more information, see
   :ref:`Columns in the Student Profile Report`.

.. _Access_anonymized:

********************************
Accessing Anonymized Learner IDs
********************************

Some of the tools that are available for use with the edX platform, including
external graders and surveys, work with anonymized learner data. If it becomes
necessary for you to deanonymize previously anonymized data, you can download a
CSV file to use for that purpose.

To download a file of assigned user IDs and anonymized user IDs, follow these
steps.

#. View the live version of your course.

#. Select **Instructor**, and then select **Data Download**.

#. Select **Get Student Anonymized IDs CSV**.

You are prompted to open or save the {course-id}-anon-id.csv file for your
course. This file contains the user ID that is assigned to each learner at
registration and its corresponding edX-wide anonymized user ID and course
specific anonymized user ID. Values are included for every learner who ever
enrolled for your course.

To research and deanonymize learner data, you can use this file together with
the ``{course_id}_student_profile_info_{date}.csv`` file of learner data or the
``{course_id}_grade_report_{date}.csv`` file of grades.

.. only:: Open_edX

    .. include:: ../../../shared/student_progress/Section_course_student.rst
