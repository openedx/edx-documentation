.. _Scheduling Your Course:

#######################
Scheduling a Course Run
#######################

Scheduling, which includes start and end dates as well as whether the course is self-paced or instructor-paced, changes with every course run.

.. only:: Partners

   The scheduling information in this topic is required to create an About
   page. After you determine scheduling for your course run, you enter the
   course run start and end dates and pacing in Publisher when you create a
   course run. For more information, see :ref:`Pub Create a Course Run`. You
   must also enter this information in Studio before the course run begins. For
   more information, see :ref:`Set Schedule and Pacing`.

.. only:: Open_edX

   After you determine scheduling for your course run, you enter this
   information in Studio before the course run begins. For more information,
   see :ref:`Set Schedule and Pacing`.

.. contents::
   :local:
   :depth: 1

.. _Guidelines for Start and End Dates:

*******************************************
Guidelines for Start and End Dates
*******************************************

The start and end dates you set for your course are important for prospective
and current learners. Current learners see your course start or end date on
their dashboards. EdX recommends that you consider your course dates carefully.

============================
Course Start Date and Time
============================

The course start date and time specify when learners can access published
course content. By default, the course start date and time are set to
**01/01/2030** at **00:00 UTC** to ensure that your course does not start
before you intend it to.

EdX recommends the following guidelines for determining a course start date.

* Start on a Tuesday, Wednesday, or Thursday.
* Avoid major U.S. holidays.
* Specify a month, day, and year. If you are unsure of the exact date, specify
  a day that is close to the estimated start date. For example, if your course
  will start near the end of March, specify March 31.
* Set the start time of your course early in the day, generally 00:00
  Coordinated Universal Time (UTC) or earlier. Learners often expect the course
  to be available on the start date in their own time zones and try to access
  course content during the day. If you do not specify a start time for your
  course, the course starts at 00:00 UTC.

Although learners cannot access any part of your course before the course
start date, course team members who are enrolled in the course and who have
the staff, admin, or beta tester role can see published content in the course
before the course start date. For information about testing your course
content before the course start date, see :ref:`Beta_Testing`.

.. note::
  You can set a different advertised start date for your course. You might do
  this if the exact start date is uncertain. For example, you could advertise
  the start date as "Coming Soon". For more information, see
  :ref:`Advertise a Different Start Date`.

============================
Course End Date and Time
============================

The course end date and time specify when learners can no longer earn credit
toward certificates. Learners can continue to complete available coursework,
but cannot earn credit after the course ends. Learners who have earned
certificates can view the certificates soon after the course end date.

In self-paced courses, course teams can make certain course components
unavailable based on the course end date. For example, course teams can make a
final exam unavailable after the end date for a self-paced course. For more
details, see :ref:`Hide a Subsection After its Due Date`.

.. important::
  If you do not set a course end date, learners cannot access earned
  certificates.

.. only:: Open_edX

  ===============================
  Enrollment Start Date and Time
  ===============================

  As soon as enrollment starts, prospective learners can see your course in the
  course catalog, view the course **About** page, and enroll in the course.

  The enrollment start date and time specify when learners can start to enroll
  in the course. Ensure that the enrollment start date is early enough to allow
  learners to both enroll in and prepare for the course.

  .. _Enrollment End Date and Time:

  ===============================
  Enrollment End Date and Time
  ===============================

  The enrollment end date and time specify when learners can no longer enroll
  in the course. Ensure that the enrollment end date is late enough to allow
  learners adequate time to enroll. The enrollment end date cannot be later
  than the course end date.


.. _View Start and End Dates:

========================================================
The Learner's View of Course Start and End Dates
========================================================

When learners browse courses, the start date for each course is visible in the
course catalog and in the course's About page.

.. image:: ../../../../shared/images/course_dates.png
 :alt: Course cards in the course catalog, showing each course's start date.
 :width: 800

.. image:: ../../../../shared/images/about-page-course-start.png
 :alt: The course About page, showing the start date.
 :width: 800

.. only:: Open_edX

  To find the URL of your course's **About** page in Studio, select
  **Settings**, and then select **Schedule & Details**.

After learners enroll in courses, the courses appear on their course
dashboards. To access the dashboard, learners select their usernames and then
select **Dashboard**. For a course that is in progress or has not yet started,
the start date is visible. For a course that has ended, the course end date is
visible.

.. image:: ../../../../shared/images/dashboard-course-start-and-end.png
 :alt: The learner dashboard with a course in progress, one that has ended, one
  that is self-paced and can be started any time, and one that has not
  started.
 :width: 800


.. _Setting Course Pacing:

*************
Course Pacing
*************

This topic describes how to set your course to follow a typical schedule or to
be a self-paced course.

===========================
Overview of Course Pacing
===========================

When you create an edX course, you can set the schedule of the course,
including due dates for assignments or exams, or you can allow learners to work
at their own pace. Courses that follow a schedule that you set are known as
instructor- paced courses. Courses that allow learners to submit assignments at
any time before the course ends, without internal due dates, are known as self-
paced courses.

An indicator for the pacing for your course appears on the **Course Outline**
page. By default, courses are instructor-paced.

.. image:: ../../../../shared/images/Pacing_COIndicator.png
 :width: 600
 :alt: text

.. note::
    You cannot change the course pacing after the course start date has passed.

=======================================
Instructor-Paced and Self-Paced Courses
=======================================

Instructor-paced courses progress at the pace that the course author sets. You
set release dates for content and due dates for assignments, and assignment due
dates are visible in the LMS. Learners cannot access course content before its
release date, and learners must complete assignments by their due dates.

In self-paced courses, learners can access all course materials when the
course begins, and assignments do not have due dates. You do not have the
option to set release dates for course content or due dates for assignments.
The LMS shows indicators for graded assignments but no due dates. Learners can
complete course material at any time before the course end date.

.. image:: ../../../../shared/images/Pacing_SubSettings.png
 :width: 500
 :alt: Side-by-side comparison of subsection settings for instructor-led and
     self-paced courses, showing release and due date options for the
     instructor-led course.

.. note:: If you set due dates for assignments or exams in an instructor-led
   course and later change the course to be self-paced, Studio stores the due
   dates that you previously set. If you change the course back to instructor-
   paced later, Studio restores the due dates.

.. only:: Partners

  For more information about the way learners experience instructor-paced and
  self-paced courses, see :ref:`Differences Between Instructor- and Self-Paced
  Courses<learners:SFD Course Pacing>` in the *edX Learner's Guide*.

.. include:: ../../../../links/links.rst
