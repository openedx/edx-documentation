.. _Pub Creating a Course Run:

#####################
Creating a Course Run
#####################


This topic describes the process of creating and finalizing a course run.

.. contents::
  :local:
  :depth: 1

In Publisher, a course run contains the following information.


.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Required
     - Optional
   * - Start and end date

       Staff

       Pacing

       ㅤEnrollment track (default is audit)

       Content language

       Transcript languages

     - Program association

       Estimated effort

       Length

       ㅤVideo language

       ㅤ

       ㅤ

.. note::
 Course certificates are associated with course runs. However, you configure
 course certificates in Studio. For more information, see :ref:`Setting Up
 Certificates`.

For more information about how to determine this information for your course
run, see :ref:`Planning Course Run Information`.


.. _Pub Course Run Creation and Finalization:

***************************
Course Run Creation Process
***************************

The course run creation process in Publisher includes the following steps.

.. note::
 You can create and edit a course run at any time after you create a course.
 However, you must finalize the course before you can send a course run to the
 edX project coordinator (PC) for review.

#. :ref:`Create the course run<Pub Create a Course Run>`. In this step, you
   provide only basic information about the course run, and Publisher creates a
   page for the course run.
#. :ref:`Receive a Studio URL <Pub Receive a Studio URL>` from the edX PC.
#. :ref:`Edit the course run <Pub Edit a Course Run>`, adding all required
   information for the About page.
#. :ref:`Send the course run to the edX PC for review <Pub Send a Course for
   Marketing Review>`.
#. :ref:`Review the edX PC feedback, and then finalize the course run <Pub
   Finalize a Course Run>`.

.. _Pub Create a Course Run:

*******************
Create a Course Run
*******************

To create a course run in Publisher, follow these steps.

.. note::
  If one or more course runs have been published, Publisher pre-fills some
  information on the **New Course Run** page based on the last published course
  run.

#. Use one of the following methods to open the **New Course Run** page.

   * On the dashboard, select **Add a Course Run**. Then, on the **New Course
     Run** page, select the course that you want in the **Find Course** list.
   * On the **Courses** page, select the course that you want. Then, on the
     page for the course, select **Add Run**.
   * When you create a new course, select **I want to add a run to this course
     at this time** at the bottom of the page, and then select **Create New
     Course**.

#. On the **New Course Run** page, enter the following information.

   * The course start and end dates. Times are in universal coordinated time
     (UTC).
   * Course pacing.
   * Available certificate types, if any, and the prices for the certificates.

#. Select **Create New Course Run**.

The page for the course run opens. This page lists the course run information
that you have entered and the additional course run information that is
required for edX to create an About page.

At the top of the course run page, "breadcrumbs" are visible that list the name
of the course and the course run. For example, the breadcrumbs may be ``Courses
> Creating an edX Course > Self-paced: June 1, 2017``.

You can edit course run information at any time before you send the course run
to the edX PC for review. For more information, see :ref:`Pub Edit a Course
Run`.

.. _Pub Receive a Studio URL:

**************************************
Receive a Studio URL for a Course Run
**************************************

.. note::
 You can edit a course run before you receive a Studio URL for the course run.
 However, the course run must have a Studio URL before you send the course run
 to the PC for review.

When you create a course run, Publisher automatically sends a notification to
the edX PC. The edX PC then creates a Studio URL for the course run. This
process can take up to two business days.

When the edX PC creates the Studio URL, this information automatically appears
in the **Studio URL** field on the course run page. Additionally, Publisher
sends an email notification to the course team that the Studio URL has been
created. The email notification contains a link to the course run in Studio and
to the course run page in Publisher.

After the edX PC has created the Studio URL for the course run, the course team
has the the following options.

* Enter content for the course run in Studio. To access the course run in
  Studio, select the link in the notification email, or select the **Studio
  URL** link on the course run page.
* Continue editing the course run in Publisher. For more information, see
  :ref:`Pub Edit a Course Run`.
* Send the course run to the edX PC for review. For more information, see
  :ref:`Pub Send a Course Run for Review`.

.. _Pub Edit a Course Run:

*******************
Edit a Course Run
*******************

.. note::
 You can edit a course run before you receive a Studio URL for the course run.
 However, the course run must have a Studio URL before you send the course run
 to the PC for review.

 Additionally, you do not have to enter all of the required information for the
 course run at one time. You can return to the course run page and add
 information at any time before you send the course run for review.

To edit a course run, follow these steps.

#. Use one of the following methods to open the page for the course run.

   * On the dashboard, select the **In Development** tab, and then select the
     course run that you want. You can identify the course run by the start
     date.
   * On the **Courses** page, select the course that you want. When the page
     for the course opens, under **Course Runs**, select the course run.

     You can identify a course run by the course run's pacing and start date.
     For example, the name of a course run may be "Self-paced: June 01, 2017"
     or "June 1, 2017 - Self-paced".

#. On the page for the course run, select **Edit**.

#. Add the required information for the course run in the fields on the page.

   * To specify an instructor, enter two or more letters in the **Instructor**
     field, and then select an instructor from the list. If the instructor is
     not listed, select **Add New Instructor**, and then fill out the form that
     opens.

#. When you have made your changes, select **Update Course Run**.

.. _Pub Send a Course Run for Review:

********************************************
Send a Course Run to the edX PC for Review
********************************************

After you have finished editing the course run and the course run has a Studio
URL, you can send the course run for review by the edX PC.

To send the course run for review, follow these steps.

#. Use one of the following methods to open the page for the course run.

   * On the dashboard, select the **In Development** tab, and then select the
     course run that you want. You can identify the course run by the start
     date.
   * On the **Courses** page, select the course that you want. When the page
     for the course opens, under **Course Runs**, select the course run.

#. On the page for the course run, select **Send for Review**.

.. _Pub Finalize a Course Run:

*********************
Finalize a Course Run
*********************

To finalize a course run, you mark it as reviewed in Publisher.

#. Use one of the following methods to open the page for the course run.

   * On the dashboard, select the **In Development** tab, and then select the
     course run that you want. You can identify the course run by the start
     date.
   * On the **Courses** page, select the course that you want. When the page
     for the course opens, under **Course Runs**, select the course run.

#. On the course run page, finalize the course. To do this, under **Reviews**,
   select **Mark as Reviewed**.

   The status changes to **Reviewed**.

When you mark a course run as reviewed, the Publisher tool automatically sends
a notification to the edX publisher. The edX publisher then creates a preview
of the About page for the course run, and the course team accepts or declines
the About page preview. For more information, see :ref:`Pub Publishing an About
Page`.

.. _Pub Add a Comment to the Course Run:

********************************
Add a Comment to the Course Run
********************************

You and other Publisher users can add a comment to a course run at any time.
When you add a comment, the comment is visible to anyone who views the course
run page. Additionally, Publisher sends an email notification that includes the
comment to the PC for the course run.

To add a comment to a course run, follow these steps.

#. Use one of the following methods to open the page for the course run.

   * On the dashboard, select the **In Development** tab, and then select the
     course run that you want. You can identify the course run by the start
     date.
   * On the **Courses** page, select the course that you want. When the page
     for the course opens, under **Course Runs**, select the course run.

#. On the page for the course, enter your text in the **Comment** field, and
   then select **Add comment**.


