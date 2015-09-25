.. _Working with Video Components:

#############################
Working with Video Components
#############################

This section describes how to work with videos for your course.

.. contents::
 :local:
 :depth: 1

************************
Overview
************************

You can create videos and add them to a course to supplement active
learning components, such as discussions and problems. Videos can be
effective for a number of purposes, such as presenting motivating 
material, showing experiments, and reducing cognitive load for complex
content.

=====================
When to use a Video
=====================

Before creating video content, figure out whether video is the best medium by
asking the following questions.

* Should the content be conveyed through text? 
* Through an interactive demonstration? 
* By having learners work through a problem? 
  
=============
Video Length
=============

Keep videos as short as possible.

Learners are much less likely to finish watching a video if it is more than
5-10 minutes long. 

====================
Video Accessibility
====================

Be sure to review :ref:`Creating Accessible Media` before you create videos for
your course.

========================================
Allowing Learners to Download Videos
========================================

To help course teams protect video assets, the edX video player hides video
URLs by default. This functionality is in effect for all video
files, including YouTube videos and videos that are hosted in other locations.

You can allow learners to download videos by selecting the **Video Download
Allowed** option for your video components. 

For more information about posting
videos to hosting sites other than YouTube, see :ref:`Post the Video Online`.

For more information about options that you can set when you create a video
component, see :ref:`Video Advanced Options` under :ref:`Create a Video
Component`.

.. _Create the Video:

************************
Step 1. Create the Video
************************

Your videos can contain whatever content you want to include in the course. The
`Creating Videos`_ section of `edX101 Overview of Creating an edX Course`_ has
some helpful pointers for creating good video content.

When you create videos, follow `Richard Mayer's 12 Principles
<http://hartford.edu/academics/faculty/
fcld/data/documentation/technology/presentation/powerpoint/12_principles_mult
imedia.pdf>`_. The principles in this document are based on extensive
experimental research of student learning.

.. _Compression Specifications:

======================================
Recommended Compression Specifications
======================================

EdX recommends the following video compression specifications. These
specifications are recommended but not required.

.. list-table::
   :widths: 10 20 20
   :stub-columns: 1

   * - Output
     - **Publish to YouTube**
     - **Publish downloadable file to AWS S3**
   * - Codec
     - H.264 .mp4
     - H.264 .mp4
   * - Resolution & Frame Rate (see note)
     - 1920x1080, progressive, 29.97 fps
     - 1280x720, progressive, 29.97 fps
   * - Aspect
     - 1.0
     - 1.0
   * - Bit Rate
     - VBR, 2 pass
     - VBR, 2 pass
   * - Target VBR
     - 5 mbps
     - 1 mbps
   * - Max VBR
     - 7.5 mbps
     - 1.5 mbps
   * - Audio
     - AAC 44.1 / 192 kbps
     - AAC 44.1 / 192 kbps

.. note:: Typically you export at the same frame rate that was used when you
 created the media file. For example, if you create the file in a country that
 uses the PAL system, you export at 25 fps instead of the NTSC standard of
 29.97 fps.

.. _Video Formats:

=======================
Supported Video Formats
=======================

The edX video player supports videos in .mp4, .webm, .mpeg, and .ogg format.
However, to help make sure all standard browsers can play your video, edX
strongly recommends that you use the **.mp4 format**.

.. _Create Transcript:

*********************************************
Step 2. Create or Obtain a Video Transcript
*********************************************

Transcripts are required for your videos. Transcripts are required for deaf or
hard of hearing learners to understand audio content, and helpful for learners
who speak other languages. You can allow learners to download transcripts so
that they can read them offline. You associate a transcript with a video when
you create the video component.

Timed transcripts in the SubRip Text (.srt) format are strongly recommended. A
transcript in the .srt format appears next to its associated video and
automatically scrolls as the video plays. A learner can select a word in the
transcript to jump to the point in the video where that word is spoken.

To create or obtain a transcript in .srt format, you can work with a company
that provides captioning services. 

.. only:: Partners

  EdX works with `3Play Media <http://www.3playmedia.com>`_ and
  `Cielo24 <http://www.cielo24.com/>`_. `YouTube <http://www.youtube.com/>`_
  also provides captioning services.

When you upload an .srt file, a .txt file is created automatically. You can
allow learners to download these transcript files. If you allow your learners
to download transcripts, the video player includes a **Download transcript**
option. Learners can then select either **SubRip (.srt) file** or **Text (.txt)
file** to download the .srt or .txt transcript.

.. image:: ../../../shared/building_and_running_chapters/Images/Video_DownTrans_srt-txt.png
   :width: 500
   :alt: Video status bar showing .srt and .txt transcript download options.

================================
Naming SubRip Text Files
================================

To prevent errors when you upload your video transcripts, edX recommends the
following conventions for naming your transcript files.

* Each transcript file should have a unique identifying name. The name should
  be unique not only across the transcript files for your videos, but across
  all of your course uploads.

* File names that include special characters, such as ç, å, or ó, cause the
  upload option to result in an error. Before you upload a transcript, change
  the file name to remove the special characters.

* Make sure that the file type, ``.srt``, is in lower case. 

* Other than to separate the identifying name from the ``.srt`` file type, file
  names should not include periods.

=========================================
Providing Transcripts in Other Formats
=========================================

You can provide transcripts in formats other than the .srt format, such as
.pdf, and you can provide additional transcript files in different languages.
For more information about these options, see :ref:`Additional Transcripts`.

.. note:: Historically, some courses used .sjson files for video transcripts.
 Use of .sjson files is no longer recommended; however, if transcripts in your
 course use this format, see :ref:`Steps for sjson files`.

.. _Post the Video Online:

*****************************
Step 3. Post the Video Online
*****************************

All course videos should be posted to YouTube. By default, the edX video player
accesses your YouTube videos.

Because YouTube is not available in all locations, however, edX recommends that
you also post copies of your videos on a third-party hosting site such as
`Amazon S3 <http://aws.amazon.com/s3/>`_. When a learner views a video in your
course, if YouTube is not available in that learner's location or if the
YouTube video does not play, the video on the backup site starts playing
automatically. You can also allow the learners to download the video from the
backup site.

After you post your video online, make sure you have the URL for that copy of
the video. If you post copies of your video in more than one place, make sure
you have the URL for each video location.

==================
YouTube
==================

After you create your video, upload the video to `YouTube
<http://www.youtube.com/>`_.

.. note:: YouTube only hosts videos of up to 15 minutes. If you create a
 0.75-speed option, you must make sure that your 1.0-speed video segments are
 only 11.25 minutes long so that YouTube can host all speeds. YouTube offers
 paid accounts that relax this restriction.

==================
Other Sites
==================

You can use any video backup site that you want. However, keep in mind that the
site where you post the videos might need to handle high traffic volume.

.. note:: The URL for the video that you post on a third-party site must end
 in .mp4, .webm, .mpeg, or .ogg. (To help make sure all standard browsers can
 play your video, edX **strongly** recommends that you use .mp4 format.) EdX
 cannot support videos that you post on sites such as Vimeo.

If you (or your beta testers or learners) encounter an error when you view a
course video, it might be the result of one of these browser-related problems.

* Verify that the viewer's browser is up to date. For example, some older
  versions of the Mozilla Firefox browser did not play .mp4 video files, and
  some older versions of the Firefox browser did not play .webm video files.
  These problems do not occur in more recent versions of these browsers.

  For more information, see `Media formats supported by the HTML audio and
  video elements`_.

* Verify that file metadata, particularly the MIME type, is correctly set on
  the host site. Internet Explorer 10 browsers do not play videos if the MIME
  type is not set. For example, make sure that the HTTP header ``Content-Type``
  is set to video/mp4 for an .mp4 file, or to video/webm for a .webm file.

  As an example of how you might set metadata on a video backup site, the
  *Console User Guide* for the Amazon Simple Storage Service provides this
  information about `editing object metadata`_.


.. _Create a Video Component:

********************************
Step 4. Create a Video Component
********************************

.. The following note provides a cross reference to information that applies only to courses running on edx.org. - Alison 24 Jun 15

.. only:: Partners

    .. note:: If you are building a course to run on the edx.org site, in 
     place of this step, you follow the :ref:`Add the edX Video ID to a Video
     Component` procedure. For more information, see the :ref:`Processing Video
     Files Index` section.


To add a video and its transcript to your course, follow these steps.

#. Under **Add New Component**, select **Video**.

#. When the new video component appears, select **Edit**. The video editor
   opens to the **Basic** page.

   .. image:: ../../../shared/building_and_running_chapters/Images/VideoComponentEditor.png
    :alt: Image of the video component editor.
    :width: 600

   You replace the default values with your own.

3. In the **Component Display Name** field, enter an identifying name for this
   video. This name appears as a heading above the video and as a tooltip in
   the learning sequence at the top of the **Courseware** page. It also
   identifies the video for you in Insights.

#. In the **Default Video URL** field, enter the URL of the video. Example
   URLs follow.

   ::

      http://youtu.be/OEoXaMPEzfM
      http://www.youtube.com/watch?v=OEoXaMPEzfM
      https://s3.amazonaws.com/edx-course-videos/edx-edx101/EDXSPCPJSP13-G030300.mp4
      https://s3.amazonaws.com/edx-videos/edx101/video4.webm

.. note:: To be sure that all learners can access a video, you can 
    create multiple versions that use different encodings or hosting services.
    After you post different versions on the Internet, you add each URL below
    the default video URL. **These URLs cannot be YouTube URLs**. To add a URL
    for another version, select **Add URLs for additional versions**. The first
    listed video that is compatible with the learner's computer plays.

5. Next to **Default Timed Transcript**, select an option.

   * If edX already has a transcript for this video, Studio automatically
     finds the transcript and associates the transcript with the video. This
     situation can occur when you reuse a video from an existing course.
     
     If you want to modify the transcript, select **Download Transcript for
     Editing**. You can then make your changes and upload the new file by
     selecting **Upload New Transcript**.

   * If edX does not have a transcript for the video, but YouTube has a
     transcript, Studio automatically finds the YouTube transcript and asks if
     you want to import it. To use this YouTube transcript, select **Import
     YouTube Transcript**. (If you want to modify the YouTube transcript,
     import the YouTube transcript into Studio, and then select **Download
     Transcript for Editing**. You can then make your changes and upload the
     new file by selecting **Upload New Transcript**.)

   * If both edX and YouTube have a transcript for your video, but the edX
     transcript is out of date, you receive a message asking if you want to
     replace the edX transcript with the YouTube transcript. To use the YouTube
     transcript, select **Yes, replace the edX transcript with the YouTube
     transcript**.

   * If neither edX nor YouTube has a transcript for your video, and your
     transcript uses the .srt format, select **Upload New Transcript** to
     upload the transcript file from your computer.

     .. note::

        * If you want to provide a transcript in a format such as .pdf,
          do not use this field to upload the transcript. For more
          information, see :ref:`Additional Transcripts`.

        * If your transcript uses the .sjson format, do not use this field.
          For more information, see :ref:`Steps for sjson files`.

6. Optionally, select **Advanced** to set more options for the video. For a
   description of each option, see :ref:`Video Advanced Options`.

#. Select **Save.**
  
.. _Video Advanced Options:

========================
Setting Advanced Options
========================

The following options appear on the **Advanced** page of the video component.

.. list-table::
    :widths: 30 70

    * - **Component Display Name**
      - The name that you want your learners to see. This is the same as the
        **Display Name** field on the **Basic** tab.
    * - **Default Timed Transcript**
      -  The name of the transcript file that was specified in the **Default
         Timed Transcript** field on the **Basic** page. You do not have to
         change this setting.
    * - **Download Transcript Allowed**
      - Specifies whether you want to allow learners to download the timed
        transcript. If you select **True**, a link to download the
        file appears below the video.

        By default, Studio creates a .txt transcript when you upload an .srt
        transcript. Learners can download the .srt or .txt versions of the
        transcript when you set **Download Transcript Allowed** to **True**. If
        you want to provide the transcript for download in a different format
        as well, such as .pdf, upload a file to Studio by using the **Upload
        Handout** field.

    * - **Downloadable Transcript URL**
      - The URL for a non-.srt version of the transcript file posted on the
        **Files & Uploads** page or on the Internet. Learners see a link to
        download the non-.srt transcript below the video.

        When you add a transcript to this field, only the transcript that you
        add is available for download. The .srt and .txt transcripts become
        unavailable. If you want to provide a downloadable transcript in a
        format other than .srt, edX recommends that you upload a handout for
        learners by using the **Upload Handout** field. For more information,
        see :ref:`Additional Transcripts`.

    * - **EdX Video ID**
      - An optional field used only by course teams that are working with
        edX to process and host video files.

    * - **License**
      - Optionally, you can set the license for the video, if you want to
        release the video with a license different from the overall course
        license.

        * Select **All Rights Reserved** to indicate to learners that you own
          the copyright for the video.

        * Select **Creative Commons** to grant others the right to share and
          use the video. You must then select the Creative Commons license
          options to apply.

          The license options that you select control the copyright notice that
          learners see for the video. For more information, see :ref:`Licensing
          a Course`.

    * - **Show Transcript**
      - Specifies whether the transcript plays along with the video by default.
    * - **Transcript Languages**
      - The transcript files for any additional languages. For more
        information, see :ref:`Transcripts in Additional Languages`.
    * - **Upload Handout**
      - Allows you to upload a handout to accompany this video. Your handout
        can be in any format. Learners can download the handout by selecting
        **Download Handout** under the video. For more information, see
        :ref:`Additional Transcripts`.
    * - **Video Available on Web Only**
      - If you select **True**, learners are only allowed to play this video
        in a Web browser. If you select **False**, learners can use any
        compatible application to play the video, including Web browsers and
        mobile apps.
    * - **Video Download Allowed**
      - Specifies whether learners can download versions of this video in
        different formats if they cannot use the edX video player or do not
        have access to YouTube. If you select **True**, you must add
        at least one non-YouTube URL in the **Video File URLs** field.
    * - **Video File URLs**
      - The URL or URLs where you posted non-YouTube versions of the video.
        Every URL should end in .mp4, .webm, .mpeg, or .ogg and cannot be a
        YouTube URL. Each learners will be able to view the first listed video
        that is compatible with the his or her computer. To allow learners to
        download these videos, you must set **Video Download Allowed** to
        **True**.

        To help make sure all standard browsers can play your video, we
        **strongly** recommend that you use the .mp4 format.

    * - **Video ID**
      - An optional field used only by course teams that are working with
        edX to process and host video files.
    * - **Video Start Time**
      - The time you want the video to start if you do not want the entire
        video to play. Use HH:MM:SS format. The maximum value is 23:59:59.

        .. note:: Learners who download and play the video in the mobile
         app see the entire video file. Only videos that play in a browser
         start playing at the specified start time.

    * - **Video Stop Time**
      - The time you want the video to stop if you do not want the entire video
        to play. Use HH:MM:SS format. The maximum value is 23:59:59.

        .. note:: Learners who download and play the video in the mobile
         app see the entire video file. Only videos that play in a browser
         stop playing at the specified stop time.

    * - **YouTube IDs**
      - If you have uploaded separate video files to YouTube for different
        speeds of your video (YouTube ID for .75x speed, YouTube ID for 1.25x
        speed, YouTube ID for 1.5x speed), enter the YouTube IDs for these
        videos in these fields. These settings are optional, to support video
        play on older browsers.

**********************************
Including Optional Collateral
**********************************

After you add a video component to your course, you can provide optional
collateral to accompany the video.

.. contents:: 
  :local:
  :depth: 1

.. _Video TOC:

==============================
Add a Video Table of Contents
==============================

You can add a table of contents for your video by adding an .srt file that
contains links to different parts of the video. When your learners view the
video, they can select **CC** to switch between the main transcript for the
video and the table of contents.

To add a table of contents, you work with a third-party service to create an
.srt file. Then, you use the **Transcript Languages** setting in the video
component to associate the .srt file with the video.

.. image:: ../../../shared/building_and_running_chapters/Images/VideoTOC.png
   :alt: A video with a transcript that has links to different parts of the
    video.
   :width: 500

#. After you obtain the .srt file that will function as the table of contents,
   open the video component for the video.

#. On the **Advanced** tab, scroll down to **Transcript Languages**, and then
   select **Add**. 

#. Select **Table of Contents**. 

#. Select **Upload**, browse to the .srt file, and then select **Open**.

#. In the **Upload translation** dialog box, select **Upload**.

.. _Additional Transcripts:

============================================================
Add a Supplemental Downloadable Transcript
============================================================

By default, a .txt file is created when you upload an .srt file, and learners
can download either the .srt or .txt transcript when you set **Download
Transcript Allowed** to **True**. **Download Transcript** appears below the
video, and learners see the .srt and .txt options when they move the cursor
over that option.

.. image:: ../../../shared/building_and_running_chapters/Images/Video_DownTrans_srt-txt.png
   :width: 500
   :alt: Video status bar showing .srt and .txt transcript download options.

To provide a downloadable transcript in a format such as .pdf along with the
.srt and .txt transcripts, you use the **Upload Handout** advanced setting.
When you do this, **Download Handout** appears to the right of the **Download
Transcript** in the video player, and learners can download the .srt, .txt, or
handout version of the transcript.

.. image:: ../../../shared/building_and_running_chapters/Images/Video_DownTrans_srt-handout.png
   :width: 500
   :alt: Video status bar showing .srt, .txt, and handout transcript download
    options.

To add a downloadable transcript, follow these steps.

#. Create or obtain your transcript as a .pdf or in another format.
#. In the video component, select **Advanced**.
#. Locate **Upload Handout**, and then select **Upload**.
#. In the **Upload File** dialog box, select **Choose File**.
#. In the dialog box, select the file on your computer, and then select
   **Open**.
#. In the **Upload File** dialog box, select **Upload**.

.. _Transcripts in Additional Languages:

============================================================
Add a Transcript in Another Language
============================================================

You can provide transcripts for your video in other languages. To do this,
you work with a third-party service to obtain an .srt transcript file for
each language, and then associate the .srt file with the video in Studio.

Before you add transcript files, make sure that each one has a unique name. If
you use the same transcript name in more than one video component, the same
transcript will play for each video. To avoid this problem, you could name
your foreign language transcript files according to the video's file name and
the transcript language.

For example, you have two videos, named video1.mp4 and video2.mp4. Each video
has a Russian transcript and a Spanish transcript. You can name the
transcripts for the first video video1_RU.srt and video1_ES.srt, and name the
transcripts for the second video video2_RU.srt and video2_ES.srt.

To add the transcripts to a video component, follow these steps.

#. After you obtain the .srt files for additional languages, open the
   video component for the video.

#. On the **Advanced** tab, scroll down to **Transcript Languages**, and then
   select **Add**.

#. Select the language for the transcript that you want to add.

#. Select **Upload**, browse to the .srt file for the language that you want,
   and then select **Open**.

#. In the **Upload translation** dialog box, select **Upload**.

#. Repeat steps 2 - 5 for any additional languages.

When your learners view the video, they can select **CC** to select a
language.

.. image:: ../../../shared/building_and_running_chapters/Images/Video_LanguageTranscripts_LMS.png
   :alt: Video playing with language options visible.

.. _Steps for sjson files:

==============================
Steps for .sjson Files
==============================

If your course uses .sjson files, you upload the .sjson file for the video
to the **Files & Uploads** page, and then specify the name of the .sjson file
in the video component.

.. note:: Only older courses that have used .sjson files in the past should use
 .sjson files. All new courses should use .srt files.

#. Obtain the .sjson file from a media company such as 3Play.
#. Change the name of the .sjson file to use the following format.

   ``subs_{video filename}.srt.sjson``

   For example, if the name of your video is **Lecture1a**, the name of your
   .sjson file must be **subs_Lecture1a.srt.sjson**.

3. Upload the .sjson file for your video to the **Files & Uploads** page.
#. Edit or create the video component.
#. Select **Advanced**.
#. In the **Default Timed Transcript** field, enter the file name of your
   video. Do not include `subs_` or `.sjson`. For the example in step 2, you
   would only enter **Lecture1a**.
#. Set the other options that you want.
#. Select **Save**.


.. The following include adds procedures for pre-roll videos to the guide for partners only. This feature works only on edx.org.  - Alison 24 Jun 15

.. only:: Partners

    .. include:: ../../../shared/building_and_running_chapters/creating_content/create_preroll_video.rst


.. _Creating Videos: https://courses.edx.org/courses/edX/edX101/2014/courseware/c2a1714627a945afaceabdfb651088cf/9dd6e5fdf64b49a89feac208ab544760/

.. _edX101 Overview of Creating an edX Course: https://www.edx.org/node/5496#.VH8p51fF_FA
.. _Media formats supported by the HTML audio and video elements: https://developer.mozilla.org/en-US/docs/Web/HTML/Supported_media_formats#MP4_H.264_(AAC_or_MP3)
.. _editing object metadata: http://docs.aws.amazon.com/AmazonS3/latest/UG/EditingtheMetadataofanObject.html
