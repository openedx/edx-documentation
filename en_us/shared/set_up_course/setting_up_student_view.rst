.. _Setting Details About Your Course:

######################################################
Setting Details About Your Course
######################################################

This topic describes how to set details about your course in Studio. The
details you set affect the information learners see about the course on their
dashboards. For more information, see :ref:`SFD Dashboard Settings Profile`.

.. contents::
  :local:
  :depth: 1

For information about setting important dates for the course, see
:ref:`Scheduling Your Course`.

For information about setting the course license, see :ref:`Licensing a
Course`.

.. _The Course About Page:

***********************************
The Course About Page
***********************************

The following example shows the course About page. Learners can see the
About page before they enroll in the course, and may decide to enroll
based on the content of the page.

.. image:: ../../../shared/images/about_page.png
 :alt: An image of the course About page.
 :width: 600

You configure the contents of this page in Studio, as described in this topic.

.. note:: Given the diversity of MOOC learners, be careful to clearly
   communicate the target audience, level, and prerequisites for your course.
   Aim for concrete, unambiguous words. For example, your description of a
   course prerequisite might include ``understand eigenvalue decomposition``
   rather than ``intermediate linear algebra``).

.. _The Learner Dashboard:

***********************************
The Learner Dashboard
***********************************

After a learner enrolls in your course, the course is listed on that learner's
**Current Courses** dashboard with the course image. From the dashboard, a
learner can open a course that has started. If the course has not started, the
learner can see the start date, as explained in :ref:`Scheduling Your Course`.

.. image:: ../../../shared/images/dashboard-course-start-and-end.png
 :width: 600
 :alt: An image of two courses in the dashboard, with the start dates and
     times.

.. _Describe Your Course:

************************
Describe Your Course
************************

Learners see the description of your course on the course About page.

An example of a course description, titled "About this course", follows.

.. image:: ../../../shared/images/about-page-course-description.png
 :alt: Image of a course summary with a description.
 :width: 600

.. note:: For courses on edX.org, you must communicate the course description
 to your edX partner manager, to ensure the content is accurate on the course
 About page.

#. From the **Settings** menu, select **Schedule & Details**.

#. Scroll down to the **Introducing Your Course** section, then locate the
   **Course Overview** field.

   .. image:: ../../../shared/images/course_overview.png
    :alt: Image of the HTML course description.
    :width: 600

#. Overwrite the content as needed for your course, following the directions in
   the boilerplate text. Do not edit HTML tags. For a template that includes
   placeholders, see :ref:`A Template For Course Overview`.

#. Select **your course summary page** in the text beneath the field to test
   how the description will appear to learners.

#. When you make changes, a **Save Changes** button appears at the bottom right
   of the page. Select **Save Changes** when you have completed the course
   description.

.. _Add a Course Image:

************************
Add a Course Image
************************

The course image that you add in Studio appears on the dashboard. It should be
a minimum of 378 pixels in width by 225 pixels in height, and in .jpg or .png
format. Make sure the image that you upload maintains the aspect ratio of those
dimensions so that the image appears correctly on the dashboard.

An example of a course on the dashboard with a course image follows.

.. image:: ../../../shared/images/dashboard-course-image.png
 :alt: Image of the course image in the dashboard.
 :width: 600

#. From the **Settings** menu, select **Schedule & Details**.

#. Scroll down to the **Course Image** section.

#. To select an image from your computer, click **Upload Course Image**, then
   follow the prompts to find and upload your image.

#. When you make changes, a **Save Changes** button appears at the bottom right
   of the page. Select **Save Changes** when you have added the course image.

#. View your dashboard to test how the image will appear to learners.

.. note::
  On edX.org, the course image you add in Studio is used on the learner
  dashboard, but does not automatically appear on the course About page. Work
  directly with your edX partner manager to set up the About page assets and
  course image for the course summary page.

.. _Add a Course Video:

*********************************
Adding a Course About Video
*********************************

The course "about" video appears on the course **About** page.

An example of the dashboard for a course with an about video follows.

.. image:: ../../../shared/images/about-page-course-video.png
 :alt: Image of the course about video in the course summary page.
 :width: 600

The purpose of the about video is to entice potential learners to enroll, and
reveal some of the personality that the course team brings to the course.

An about video should answer these key questions.

* Who is teaching the course?
* What university or college is the course affiliated with?
* What topics and concepts are covered in your course?
* Why should a learner enroll in your course?

The video should deliver your message as concisely as possible and have a run
time of less than 2 minutes.

Before you upload a course about video, make sure that it follows the same
:ref:`Compression Specifications` and :ref:`Video Formats` guidelines as your
course content videos.

.. note:: If you upload both a course image and a course about video, the
  course image appears on learner dashboards with a **play** icon superimposed
  on it. If you upload only a course video, the first frame of the the video
  file appears with the **play** icon.

.. the "only" directives between these comments introduce the instructions that all open edX sites, and that partners adding a video to Edge, must complete. - Alison 1 Feb 2016

.. only:: Open_edX

  To upload a course about video, follow these steps.

.. only:: Partners

  ================================
  Add a Course About Video to Edge
  ================================

  To upload a course about video for the `edX Edge`_ website, follow these steps.

.. the following procedure applies to both audiences.

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

  ===================================
  Add a Course About Video to edx.org
  ===================================

  For courses running on `edx.org`_ only, follow these steps.

  #. Locate the video file on your computer. For example, on a Mac,
     open Finder and go to the directory that contains the video file.

  #. In your browser, go to the edX/Veda video upload page at
     http://veda.edx.org/upload/.

  #. Enter a title for the video that includes the course number and name. For
     example, ``edx101: Creating an edX Course``.

     You can abbreviate the full name of the course. However, the information
     that you enter should clearly identify your course.

  #. Enter the Studio URL for the course. For example,
     ``https://studio.edx.org/course/course-v1:edX+edX101x+2015``.

  #. Select **Submit**.

  #. Drag the video file from the local directory into the **Drop files here to
     upload** field. You can also click inside this field to browse to the
     file.

     The file upload process begins immediately.

     .. important:: Do not close the browser tab or window, or use it to go to
      another URL while the file is uploading. When the upload process is
      complete, the message "File Upload Complete" appears.

.. _Set Course Effort Expectations:

*******************************
Set Course Effort Expectations
*******************************

The estimated effort the course requires appears in the course About page.

You set the hours and minutes a week estimate in Studio.

#. From the **Settings** menu, select **Schedule & Details**.

#. Scroll down to the **Requirements** section.

#. In the **Hours of Effort per Week** field, enter the number of hours you
   expect learners to work on this course each week.

#. When you make changes, a **Save Changes** button appears at the bottom right
   of the page. Select **Save Changes** when you have added the estimated
   effort.

#. View your course About page to test how the requirements will appear to
   learners.

.. _A Template For Course Overview:

************************************************
 A Template For Your Course Overview
************************************************

Replace the placeholders in the following template with your information.

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

