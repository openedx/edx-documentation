.. _Institution_Data:

#######################
Institution-wide Data
#######################

The data package includes a report of data collected across all of an
institution's edx.org or edge.edx.org courses. This report is typically more
useful to administrative or marketing teams, rather than research teams.

.. recast in plural when another report is added

.. _Email Opt In Report:

*********************
Email Opt In Report
*********************

When students enroll in a course on edx.org, they can specify whether they
want to receive email from the organization that presents the course.

The ``{org}-email_opt_in-{site}-analytics.csv`` file reports the email
preference selected by each student enrolled in your institution's courses.
You can use this information to develop a distribution list for campaigns that
introduce new or related courses to students.

.. note:: Your data package includes a .csv file for the edx.org site only. 
  At this time, students can specify an email preference only on edx.org.

The file contains data in these columns.

::

  email,full_name,course_id,is_opted_in_for_email,preference_set_datetime


=========
email
=========

The email address that the student used to register a user account on the
site. For more information, see the ``auth_user.email``
:ref:`column<auth_user>`.

=========
full_name
=========

The name that the student supplied. For more information, see the
``auth_userprofile.name`` :ref:`column<auth_userprofile>`.

=========
course_id
=========

The ID of the course run in which the student is enrolled. For more
information, see the ``student_courseenrollment.course_id``
:ref:`column<student_courseenrollment>`.

===========================
is_opted_in_for_email
===========================

True or False. By default, this preference is set to True. If a student is
enrolled in more than one course, the option that the student selected most
recently applies to all of the courses.

===========================
preference_set_datetime
===========================

Indicates when the student selected this preference. If a student is enrolled
in more than one of your institution's courses, the date and time when the
student most recently selected an email preference applies to all of the
courses.
