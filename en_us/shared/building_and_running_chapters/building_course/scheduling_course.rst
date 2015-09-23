.. _Scheduling Your Course:

##############################
Setting Start and End Dates
##############################

This section describes how to schedule your course in Studio.

.. contents::
   :local:
   :depth: 1

**********
Overview
**********

The start and end dates you set for your course and for course enrollment are
important for prospective and current learners. As soon as enrollment starts,
prospective learners can see your course in the course catalog, view the
course About page, and enroll in the course. Current learners see your course
start or end date on their dashboards.

.. _View Start and End Dates:

***************************************
View Start and End Dates as a Learner
***************************************

.. or "The Learner View of Start and End Dates"?

Your course start date is visible to both prospective and current learners if
the course has not started or is in progress. The course end date is visible
to enrolled learners after the course ends.

Learners who have not yet enrolled in your course see the course start date on
the About page (sometimes also called the course summary page).

.. image:: ../../../shared/building_and_running_chapters/Images/about-page-course-start.png
 :alt: The course About page, showing the start date.
 :width: 600

Learners who enroll in your course see the start or end date for your course on
their dashboards, depending on whether the course has ended. If the course
has not started or is in progress, learners see the start date. If the course
has ended, learners see the course end date.

.. image:: ../../../shared/building_and_running_chapters/Images/dashboard-course-start-and-end.png
 :alt: The student dashboard with one course not started, one in progress, and one ended.
 :width: 600

.. _Determine Start and End Dates:

*******************************************
Determine Start and End Dates
*******************************************

EdX recommends that you consider your course and enrollment start and end
dates carefully. After you determine the dates for your course, you set these
dates and times on the **Schedule & Details** page in Studio. EdX recommends
that you verify all important dates in Studio one week before you plan to
start the course.

.. only:: Partners

  .. note::
    For courses on edX.org, you must communicate the course start and end dates
    and times to your edX Partner Manager to ensure the information is accurate
    on the course About page.

============================
Course Start Date and Time
============================

The course start date and time specify when learners can access published
course content. By default, the course start date and time are set to
**01/01/2030** at **00:00 UTC** to ensure that your course does not start
before you intend it to. You must change this setting to the correct date and
time for your course.

.. note::  
  If your course is configured to issue certificates, you cannot start the
  course until the required certificates are activated. For more information,
  see :ref:`Activate a Certificate`.

EdX recommends that you set the start time of your course early in the day,
generally 00:00 UTC or earlier. Learners often expect the course to be
available on the start date in their own time zones and try to access course
content during the day. If you do not specify a start time for your course,
learners see the default start time, 00:00 Universal Coordinated Time (UTC).

Learners can see some parts of the course before the course start date. For
example, they can see your **Course Info** page and course-wide discussion
topics as soon as they enroll in your course. For more information, see
:ref:`Create CourseWide Discussion Topics`.

.. note:: 
  You can set a different advertised start date for your course. You might
  want to do this if there is uncertainty about the exact start date. For
  example, you could advertise the start date as Spring 2015. For more
  information, see :ref:`Advertise a Different Start Date`.

============================
Course End Date and Time
============================

The course end date and time specify when learners can no longer earn credit
toward certificates. Learners can continue to complete coursework, but cannot
earn credit after the course ends. Learners who have earned certificates can
view the certificates soon after the course end date.

.. important:: 
  If you do not set a course end date, learners cannot access earned
  certificates.

===============================
Enrollment Start Date and Time
===============================

The enrollment start date and time specify when learners can start to enroll
in the course. Ensure that the enrollment start date is early enough to allow
learners to both enroll in and prepare for the course.

.. _Enrollment End Date and Time:

===============================
Enrollment End Date and Time
===============================

The enrollment end date and time specify when learners can no longer enroll in
the course. Ensure that the enrollment end date is late enough to allow
learners adequate time to enroll. The enrollment end date cannot be later than
the course end date.

.. important:: 
  For partner courses on edx.org, when the enrollment end date passes,
  the course is no longer listed in the course catalog. EdX encourages you to
  keep enrollment open as long as possible. For more information, contact your
  edX Partner Manager.

.. _Set Start and End Dates:

*******************************************
Set Course and Enrollment Dates and Times
*******************************************

You set dates and times for the course and for course enrollment in Studio.

#. From the **Settings** menu, select **Schedule and Details**.

#. Locate the **Course Schedule** section of the **Schedule & Details** page,
   and replace the placeholder dates and times with your own information.

   When you make changes, a **Save Changes** button appears in the lower right
   corner of the page.

#. When you finish entering your dates and times, select **Save Changes**.

.. note:: 
 The Time fields on this page, and the times that learners see, use Universal
 Coordinated Time (UTC).

EdX recommends that you verify that all important dates are correct one week
before you plan to start the course.

.. _Advertise a Different Start Date:

====================================
Advertise a Different Start Date
====================================

You can advertise a start date for your course that is different from the
course start date you set in the **Schedule and Details** page. You might want
to do this if there is uncertainty about the exact start date. For example, you
could advertise the start date as **Spring, 2015**.

To set an advertised start date in Studio, follow these steps.

#. From the **Settings** menu, select **Advanced Settings**.
#. Find the **Course Advertised Start Date** policy key. The default value is
   **null**.
#. Enter the value you want to display as the advertised start date. You can
   use any string, enclosed in double quotation marks. If you format the string
   as a date (for example, as 02/01/2015), the value is parsed and presented to
   learners as as a date.

  .. image:: ../../../shared/building_and_running_chapters/Images/advertised_start.png
   :alt: Image of the advertised start date policy key with a value of "anytime, self-paced".
   :width: 600

4. Select **Save Changes** at the bottom of the page.

Learners now see the value of the **Course Advertised Start Date** policy key
as the course start date on their dashboards.

If you do not change the default course start date (01/01/2030), and the
**Course Advertised Start Date** policy value is ``null``, then the 
dashboard does not list a start date for the course. Learners just see that
the course has not yet started.
