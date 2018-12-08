.. _Setting Details About Your Course:

######################################################
Setting Details About Your Course
######################################################

This topic describes how to set details about your course in Studio. The
details you set determine the information that learners see about the course on
their dashboards and on the course **About** page. For more information,
see :ref:`SFD Dashboard Settings Profile`.

.. only:: Open_edX

  You configure these course details in Studio.

.. only:: Partners

  For courses running on edX Edge, you configure these course details in
  Studio. For courses running on edx.org, you work directly with your partner
  manager to configure some of these course details.

.. contents::
  :local:
  :depth: 1

For information about setting important dates for the course, see
:ref:`Scheduling Your Course`.

For information about setting the licensing for the course, see
:ref:`Licensing a Course`.

.. _The Learner Dashboard:

***********************************
The Learner Dashboard
***********************************

After a learner enrolls in a course, the course is listed on that learner's
dashboard. From the dashboard, a learner can open a course
that has started. If the course has not started, or has already ended, the
dashboard shows the start or end date.

.. image:: ../../../shared/images/dashboard-course-start-and-end.png
 :width: 800
 :alt: An image of two courses in the dashboard, with the start dates and
     times.

For more information, see :ref:`View Start and End Dates`.

.. _The Course About Page:

***********************************
The Course About Page
***********************************

The course **About** page, sometimes called the course summary page, provides
information about your course to learners. In addition to the course
:ref:`start and end dates<Scheduling Your Course>` and an overview of course
objectives, the **About** page can include information such as a course
description with course prerequisites, requirements, and team biographies.
Learners can see the **About** page before they enroll in the course, and
might decide to enroll based on the content of the page.

.. image:: ../../../shared/images/about_page.png
 :alt: An image of the course About page.
 :width: 600

.. only:: Open_edX

  If the CourseTalk widget is enabled for your instance of the Open edX
  platform, the **About** page for every course also includes the CourseTalk
  widget. Learners who have enrolled in your course use this widget to write
  reviews of your course on the **Home** page in the LMS. These reviews are
  then visible on the course **About** page. For more information, see
  :ref:`installation:Add CourseTalk`.

===========================================
Adding Information to the Course About Page
===========================================

.. only:: Open_edX

  You configure the contents of this page in Studio.

.. only:: Partners

  For courses running on edX Edge, you configure the contents of this page in
  Studio, as described in this topic. For courses running on edx.org, you work
  directly with your partner manager to configure the contents of this page.


.. contents::
  :local:
  :depth: 2

.. _Describe Your Course:

Describe Your Course
*********************

Learners see the description of your course on the course **About** page. For
example, the course description is circled in the following course **About**
page.

.. image:: ../../../shared/images/about-page-course-description.png
 :alt: A course About page with the description circled.
 :width: 600

.. only:: Partners

  .. note:: For courses running on edx.org, you must communicate the course
   description to your edX partner manager to ensure that the information
   on the course **About** page is accurate.

Given the diversity of online learners, be sure to review your course
description to ensure that it clearly communicates the target audience, level,
and prerequisites for your course. Use concrete, unambiguous phrasing, such as
a prerequisite of "understand eigenvalue decomposition" rather than
"intermediate linear algebra".

To provide a description for your course, follow these steps.

#. From the **Settings** menu, select **Schedule & Details**.

#. Scroll down to the **Introducing Your Course** section, then locate the
   **Course Overview** field.

   .. image:: ../../../shared/images/course_overview.png
    :alt: Image of the HTML course description.
    :width: 600

#. Overwrite the content as needed for your course, following the directions in
   the boilerplate text. Do not edit HTML tags. For a template that includes
   these placeholders, see the :ref:`A Template For Course Overview`.

#. To test how the description will appear to learners, from the text that
   follows the **Course Overview** field select **your course summary page**.

#. Select **Save Changes**.

.. _Add a Course Image:

Add a Course Image
*********************

The course image that you add in Studio appears on the **About** page for the
course and on the learner dashboard. It must be a minimum of 378 pixels in
width by 225 pixels in height, and in .jpg or .png format. Make sure the image
that you upload maintains the aspect ratio of those dimensions so that the
image appears correctly on the dashboard.

An example of a course on the dashboard with a course image follows.

.. image:: ../../../shared/images/dashboard-course-image.png
 :alt: Image of the course image in the dashboard.
 :width: 600

To add a course image, follow these steps.

#. From the **Settings** menu, select **Schedule & Details**.

#. In the **Course Image** section, select **Upload Course Image**, and then
   follow the prompts to find and upload your image. To specify an image that
   has already been :ref:`added to the course<Add Files to a Course>`, select
   **files & uploads**.

   When you make changes on this page, a panel with options to save or cancel
   your work appears.

#. Select **Save Changes**.

#. View your dashboard to test how the image will appear to learners.

.. only:: Partners

  .. note::
    For courses running on edx.org, the course image that you add in Studio is
    used on the learner dashboard, but does not automatically appear on the
    course **About** page. Work directly with your edX partner manager to set
    up the **About** page assets and course image.

.. _Add a Course Video:

Adding a Course About Video
****************************

The course "about" video should excite and entice potential learners to enroll,
and reveal some of the personality that the course team brings to the course.

This video should answer these key questions.

* Who is teaching the course?
* What university or institution is the course affiliated with?
* What topics and concepts are covered in your course?
* Why should a learner enroll in your course?

This video should deliver your message as concisely as possible and have a run
time of less than 2 minutes.

Before you upload a course about video, make sure that it follows the same
:ref:`Compression Specifications` and :ref:`Video Formats` guidelines as your
course content videos.

.. note::

  * If you upload both a course image and a course about video, the course
    image appears on learner dashboards with a **play** icon superimposed on
    it. If you upload only a course video, the first frame of the the video
    file appears with the **play** icon.

  * The process for adding a course about video is different than the process
    for including videos as part of the content of your course. For more
    information about including video content, see :ref:`Working with Video
    Components`.

.. the "only" directives between these comments introduce the instructions that all open edX sites, and that partners adding a video to Edge, must complete. - Alison 1 Feb 2016

.. only:: Open_edX

  To upload a course about video, follow these steps.

.. only:: Partners

  Add a Course About Video to Edge
  ================================

  To upload a course about video for the edX Edge website only, follow these
  steps.

.. the following procedure applies to both the open edX and partner-Edge audiences.

#. Upload the video file to YouTube. Make note of the code that appears
   between **watch?v=** and **&feature** in the URL. This code appears in
   the green box below.

   .. image:: ../../../shared/images/youtube_vequals_URL.png
    :alt: A YouTube video with the code between watch?v= and &feature
     indicated.

#. From the **Settings** menu, select **Schedule & Details**.

#. Scroll down to the **Course Introduction Video** section.

#. In the field below the video box, enter the YouTube video ID (the code you
   copied in step 1). When you add the code, the video automatically loads in
   the video box.

#. When you make changes, a **Save Changes** option appears at the bottom
   right of the page. Select **Save Changes** after you add the course
   video.

#. View your course **About** page to test how the video will appear to
   learners.

.. only:: Partners

  Add a Course About Video to edx.org
  ===================================

  To add an about video for a course that is running on edx.org only, follow
  these steps.

  #. Locate the video file on your computer. For example, if you use a
     Mac® computer, open Finder and go to the directory that contains the
     video file.

  #. In your browser, go to the edX/Veda video upload page at
     http://veda.edx.org/upload/.

  #. Enter a title for the video that includes the course number and name. For
     example, ``edx101: Creating an edX Course``.

     You can abbreviate the full name of the course. However, the information
     that you enter should clearly identify your course.

  #. Enter the Studio URL for the course. For example,
     ``https://studio.edx.org/course/course-v1:edX+edX101x+2015``.

     If you are adding an about video for an XSeries, or to any other page that
     does not have a Studio URL, see :ref:`XSeries About Video`.

  #. Select **Submit**.

  #. Drag the video file from the local directory into the **Drop files here to
     upload** field. You can also click inside this field to browse to the
     file.

     The file upload process begins immediately.

     .. important:: Do not close the browser tab or window, or use it to go to
      another URL while the file is uploading. When the upload process is
      complete, the message "File Upload Complete" appears.

  .. _XSeries About Video:

  Add an XSeries About Video to edx.org
  =====================================

  To add an about video for an XSeries that is running on edx.org only, follow
  these steps.

  #. Locate the video file on your computer. For example, if you use a Mac
     computer, open Finder and go to the directory that contains the video
     file.

  #. In your browser, go to the edX/Veda video upload page at
     http://veda.edx.org/upload/.

  #. Enter a title for the video that includes the XSeries name. For
     example, ``edx VideoX XSeries: Creating Video for the edX Platform``.

     You can abbreviate the full name of the XSeries. However, the information
     that you enter should clearly identify the XSeries.

  #. In the **edX Studio Course URL** field, add identifying information
     about the XSeries to the Studio URL that is provided. For example,
     ``https://studio.edx.org/course/XSeries_edX_VideoX``.

     The value that you enter in this field does not need to resolve to an
     actual URL, but it must begin with ``https://studio.edx.org/course/``.

  #. Select **Submit**.

  #. Drag the video file from the local directory into the **Drop files here to
     upload** field. You can also click inside this field to browse to the
     file.

     The file upload process begins immediately.

     .. important:: Do not close the browser tab or window, or use it to go to
      another URL while the file is uploading. When the upload process is
      complete, the message "File Upload Complete" appears.

.. _Set Course Effort Expectations:

Set Course Effort Expectations
******************************

The estimated effort that the course requires appears in the course **About**
page.

To set the hours and minutes a week estimate in Studio, follow these steps.

#. From the **Settings** menu, select **Schedule & Details**.

#. In the **Requirements** section, locate the **Hours of Effort per Week**
   field.

#. Enter the number of hours you expect learners to work on this course each
   week.

   When you make changes on this page, a panel with options to save or cancel
   your work appears.

#. Select **Save Changes**.

#. View your course **About** page to test how the requirements will appear to
   learners.

.. _A Template For Course Overview:

Course Overview Template
*************************

Replace the placeholders in the following template with information for your
course.

.. code-block:: html

  <section class="about">
    <h2>About This Course</h2>
    <p>Include your long course description here. The long course description
    should contain 150-400 words.</p>
    <p>This is paragraph 2 of the long course description. Add more paragraphs
    as needed. Make sure to enclose them in paragraph tags.</p>
  </section>
  <section class="prerequisites">
    <h2>Requirements</h2>
    <p>Add information about the skills and knowledge students need to take
    this course.</p>
  </section>
  <section class="course-staff">
    <h2>Course Team</h2>
    <article class="teacher">
      <div class="teacher-image">
        <img src="/static/images/placeholder-faculty.png" align="left"
        style="margin:0 20 px 0" alt="Course Team Image #1">
      </div>
      <h3>Team Member #1</h3>
      <p>Biography of course team member #1</p>
    </article>
    <article class="teacher">
      <div class="teacher-image">
        <img src="/static/images/placeholder-faculty.png" align="left"
        style="margin:0 20 px 0" alt="Course Team Image #2">
      </div>
      <h3>Team Member #2</h3>
      <p>Biography of course team member #2</p>
    </article>
  </section>
  <section class="faq">
    <section class="responses">
      <h2>Frequently Asked Questions</h2>
      <article class="response">
        <h3>Do I need to buy a textbook?</h3>
        <p>No, a free online version of Chemistry: Principles, Patterns, and
        Applications, First Edition by Bruce Averill and Patricia Eldredge
        will be available, though you can purchase a printed version (
        published by FlatWorld Knowledge) if you’d like.</p>
      </article>
      <article class="response">
        <h3>Question #2</h3>
        <p>Your answer would be displayed here.</p>
      </article>
    </section>
  </section>

.. include:: ../../../links/links.rst
