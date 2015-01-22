.. _Student Data:

############################
Student Data
############################

You can access data about the individuals who are enrolled in your course at
any time after you create the course.

For information about student data, see the following topics:

* :ref:`PII`

* :ref:`Access_student_data`

* :ref:`Access_anonymized`
  
* :ref:`Track Student Activity`

To supplement the student data available from the Instructor Dashboard, you can
use the charts and reports that are available from edX Insights. For more
information, see `Using edX Insights`_.

.. _PII:

***************************************************************
Guidance for Working with Personal Information
***************************************************************

The information that edX collects from site registrants includes personal
information that can be used to identify, contact, and locate individuals. This
information is available to course authors for the students who are enrolled in
their courses.

Course staff should follow the policies established by their organizations
and comply with the legal requirements of their locales to prevent public
distribution or misuse of this information.

.. **Question**: I just made this statement up. What guidance can/should we give, for immediate publication and in the future? (sent to Tena and Jennifer Adams 31 Jan 14)

.. _Access_student_data:

****************************
Access Student Data
****************************

You can download data about the students who are currently enrolled in your
course in a CSV (comma-separated values) file. For courses that have fewer than
200 students enrolled, you can also view data for enrolled students on the
Instructor Dashboard.

======================
Student-Reported Data
======================

When students register with edX, they select a public username and supply
information about themselves. Most of this information is optional, so not all
of the students who are enrolled in your course provide it.

 .. image:: ../../../shared/building_running_course/Images/Registration_page.png
   :alt: Fields that collect student information during registration

Students then enroll in as many individual courses as they choose, which enrolls
them in each selected course.

You can access this self-reported information for all of the students who are
enrolled in your course:

* username
* name
* email
* year_of_birth
* gender
* level_of_education
* mailing_address
* goals

The student data that is available to course staff always reflects the set of
live, current enrollments. Students can enroll in your course throughout the
defined enrollment period, and they can unenroll from a course at any time.
Students can also change their email addresses and full names at any time. As a
result, you may want to download student data periodically to gain insights into
how the student population changes over time.

.. note:: In the future, edX may also request that students select a language 
 and location. This data is not collected at this time.

.. _View and download student data:

==========================================
Download or View Student Data
==========================================

You can download a report of student data to learn about the individuals who
are enrolled in your course. In addition to the self-reported data collected at
registration, this report includes the user account ID numbers that edX assigns
to each registrant. For courses that include student cohorts, this report
includes the cohort group that is assigned to each student.

When you choose to download student data, a process starts on the edX servers.
The number of students enrolled in your course, and whether your course has the
cohort feature enabled, affect how long this process takes. You can download a
report of student profile information in a CSV (comma-separated values) file
after the process is complete.

For courses with fewer than 200 students enrolled, you also have the option to
view student data on the Instructor Dashboard.

.. note:: In addition to the data for enrolled students, data for the course 
 staff is included in the file or display.

To download student data:

#. View the live version of your course.

#. Click **Instructor**, then click **Data Download**.

#. To download data about enrolled students in a CSV file, click **Download
   profile information as a CSV**.

  A status message indicates that report generation is in progress. This
  process can take some time to complete, but you can navigate away from this
  page and do other work while it runs.

  To track the progress of the report process, reload the page in your browser
  and scroll down to the **Pending Instructor Tasks** section.

4. To open or save a student data report, click the
   ``{course_id}_student_profile_info_{date}.csv`` file name at the bottom of
   the page.

  All student-supplied data is included in this file without truncation.

To view student data:

.. note:: This option is available only for courses with an enrollment of less 
 than 200.

#. View the live version of your course.

#. Click **Instructor**, then click **Data Download**.

#. To display data about enrolled students, click **List enrolled students'
   profile information**. 

   A table of the student data displays, with one row for each enrolled
   student. Longer values, such as student goals, are truncated.

 .. image:: ../../../shared/building_running_course/Images/StudentData_Table.png
  :alt: Table with columns for the collected data points and rows for each 
        student on the Instructor Dashboard

For courses that have the cohorts feature enabled, this report also includes a
Cohort column with each student's assigned cohort group.

.. note:: The columns for language and location are included in this report 
 for backward compatibility only. This data is no longer collected during
 student registration.

.. _Access_anonymized:

********************************
Access Anonymized Student IDs
********************************

Some of the tools that are available for use with the edX platform, including
external graders and surveys, work with anonymized student data. If it becomes
necessary for you to deanonymize previously anonymized data, you can download a
CSV file to use for that purpose.

To download a file of assigned user IDs and anonymized user IDs:

#. View the live version of your course.

#. Click **Instructor**, then click **Data Download**.

#. Click **Get Student Anonymized IDs CSV**.

You are prompted to open or save the {course-id}-anon-id.csv file for your
course. This file contains the user ID that is assigned to each student at
registration and its corresponding edX-wide anonymized user ID and course
specific anonymized user ID. Values are included for every student who ever
enrolled for your course.

To research and deanonymize student data, you can use this file together with
the ``{course_id}_student_profile_info_{date}.csv`` file of student data or the
``{course_id}_grade_report_{date}.csv`` file of grades.

.. _Track Student Activity:

******************************
Track Student Activity
******************************

To monitor student activity during your course, you can review the number of
students who, each week, interacted with your course. To be considered active,
students must visit pages, play videos, add to discussions, submit answers to
problems, or complete other course activities. The active student count is
updated weekly.

To display the number of active students:

#. View the live version of your course.

#. Click **Instructor**, then click **Analytics**. The count of active students
   appears at the top of the page.


.. _Using edX Insights: http://edx-insights.readthedocs.org/en/latest/