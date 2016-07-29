.. _Scheduling Your Course:

##############################
Setting Start and End Dates
##############################

This section describes how to schedule your course in Studio.

.. contents::
   :local:
   :depth: 1

For information about providing other information for your course, see
:ref:`Setting Details About Your Course`.

**********
Overview
**********

The start and end dates you set for your course and for course enrollment are
important for prospective and current learners. As soon as enrollment starts,
prospective learners can see your course in the course catalog, view the
course **About** page, and enroll in the course. Current learners see your
course start or end date on their dashboards.

.. only:: Partners

   .. note:: Only edX staff members can define the enrollment dates for
    courses on edx.org.

.. _Determine Start and End Dates:

*******************************************
Determining Start and End Dates
*******************************************

EdX recommends that you consider your course start and end dates, and its
enrollment start and end dates, carefully. After you determine the dates for
your course, you set these dates and times on the **Schedule & Details** page
in Studio. EdX recommends that you verify all important dates in Studio one
week before you plan to start the course.

.. contents::
  :local:
  :depth: 1

============================
Course Start Date and Time
============================

The course start date and time specify when learners can access published
course content. By default, the course start date and time are set to
**01/01/2030** at **00:00 UTC** to ensure that your course does not start
before you intend it to. You must change this setting to the correct date and
time for your course.

EdX recommends that you set the start time of your course early in the day,
generally 00:00 UTC or earlier. Learners often expect the course to be
available on the start date in their own time zones and try to access course
content during the day. If you do not specify a start time for your course,
learners see the default start time, 00:00 Coordinated Universal Time (UTC).
The course start time and other course dates and times are displayed in
learners' own time zones, if they have specified a time zone in account
settings.

.. note::
  You can set a different advertised start date for your course. You might do
  this if the exact start date is uncertain. For example, you could advertise
  the start date as "Coming Soon". For more information, see
  :ref:`Advertise a Different Start Date`.

Although learners cannot access any part of your course before the course
start date, course team members who are enrolled in the course and who have
the staff, admin, or beta tester role can see published content in the course
before the course start date. For information about testing your course
content before the course start date, see :ref:`Beta_Testing`.


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

.. only:: Partners

  Only edX staff members can define the enrollment dates for
  courses on edx.org.

The enrollment start date and time specify when learners can start to enroll
in the course. Ensure that the enrollment start date is early enough to allow
learners to both enroll in and prepare for the course.

.. _Enrollment End Date and Time:

===============================
Enrollment End Date and Time
===============================

.. only:: Partners

  Only edX staff members can define the enrollment dates for
  courses on edx.org.

The enrollment end date and time specify when learners can no longer enroll in
the course. Ensure that the enrollment end date is late enough to allow
learners adequate time to enroll. The enrollment end date cannot be later than
the course end date.

.. only:: Partners

  .. important::
    For partner courses running on edx.org, when the enrollment end date
    passes, the course is no longer listed in the course catalog. EdX
    encourages you to keep enrollment open as long as possible.

.. _Set Start and End Dates:

*******************************************
Set Course and Enrollment Dates and Times
*******************************************

To set dates and times for the course and for course enrollment in Studio,
follow these steps.

#. From the **Settings** menu, select **Schedule & Details**.

#. In the **Course Schedule** section, replace the placeholder dates and times
   with your own information.

   When you make changes on this page, a panel with options to save or cancel
   your work appears.

#. Select **Save Changes**.

.. note:: The times that you set, and the times that learners see, are in
 Coordinated Universal Time (UTC). You might want to verify that you have
 specified the times that you intend by using a time zone converter such as
 `Time and Date Time Zone Converter`_.

EdX recommends that you verify that all important dates are correct one week
before you plan to start the course.

.. _Advertise a Different Start Date:

====================================
Advertise a Different Start Date
====================================

You can advertise a start date for your course that is different from the
course start date you set in the **Schedule & Details** page. You might want
to do this if the exact start date is uncertain.

You can enter a specific date or a description. For example, you could
advertise the start date as either "15 Oct 2016" or "Anytime, self-paced".

To set an advertised start date in Studio, follow these steps.

#. From the **Settings** menu, select **Advanced Settings**.

#. Locate the **Course Advertised Start Date** field. The default value is
   ``null``.

#. Enter the start date that you want learners to see for your course in
   MM/DD/YYYY format.

   A date value entered in MM/DD/YYYY format appears to learners in DD Mon YYYY
   format. For example, 10/15/2016 appears as 15 Oct 2016.

#. Add quotation marks (``" "``) before and after the start date value. An
   example follows.

   ::

     "Anytime, self-paced"

#. Select **Save Changes**.

   A message lets you know whether your changes were saved successfully.

.. note:: If you do not change the default course start date (01/01/2030),
 and the **Course Advertised Start Date** policy value is ``null``, then no
 start date appears for the course. Learners just see that the course has not
 yet started.

.. _View Start and End Dates:

***************************************
View Start and End Dates as a Learner
***************************************

Learners can view the start date for a course on the course **About** page,
and, after they enroll in the course, on their dashboards.

.. image:: ../../../shared/images/about-page-course-start.png
 :alt: The course About page, showing the start date.
 :width: 800

.. only:: Open_edX

  To find the URL of your course's **About** page in Studio, select
  **Settings** and then **Schedule & Details**.

After learners enroll in your course, the course appears on their course
dashboards. To access the dashboard, learners select their usernames and then
**Dashboard**.

.. image:: ../../../shared/images/dashboard-course-start-and-end.png
 :alt: The learner dashboard with a course in progress, one that has ended, one
  that is self-paced and can be started any time, and one that has not
  started.
 :width: 800

For a course that is in progress or has not yet started, the start date is
shown. For a course that has ended, the course end date is shown.

.. only:: Partners

  .. note:: These sample images are from the edX Edge website. They show
   an **About** page and a learner dashboard on an instance powered by Open
   edX. On the `edx.org`_ website these pages present the same information, but
   are styled differently.

.. include:: ../../../links/links.rst
