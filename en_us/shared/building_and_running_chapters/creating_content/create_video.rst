.. _Working with Video Components:

#############################
Working with Video Components
#############################

**********************
Introduction to Videos
**********************

You can create videos of your lectures and add them to your course to
supplement other components, such as discussions and problems, to promote
active learning. Adding a video to your course has several steps.

#. :ref:`Create the Video`.
#. :ref:`Create Transcript`.
#. :ref:`Post the Video Online`.
#. :ref:`Create a Video Component`.

Also see:

* :ref:`Video TOC`
* :ref:`Additional Transcripts`
* :ref:`Steps for sjson files`

.. note:: Review :ref:`Best Practices for Accessible Media` before adding 
 videos to your course.

To help course teams protect video assets, the edX video player hides video
URLs from students by default. This functionality is in effect for all video
files, including YouTube videos and videos that you have posted in other
locations. Students can still download videos if you select the **Video
Download Allowed** option for your video components. For more information about
posting non-YouTube videos online, see :ref:`Post the Video Online`. For more
information about options that you can set when you create a video component,
see :ref:`Video Advanced Options` under :ref:`Create a Video Component`.

.. _Create the Video:

************************
Step 1. Create the Video
************************

Your videos can contain whatever content you want to include in the course. The
`Creating Videos`_ section of `edX101 Overview of Creating an edX Course`_ has
some helpful pointers for creating good video content.

.. _Compression Specifications:

====================================
Compression Specifications
====================================

When you create your video, edX recommends the following compression specs.
(Note that these are recommended but not required.)

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

==================
Video Formats
==================

The edX video player supports videos in .mp4, .webm, .mpeg, and .ogg format.
However, to help make sure all standard browsers can play your video, we
strongly recommend that you **use the .mp4 or .webm format**.

.. _Create Transcript:

*********************************************
Step 2. Create or Obtain a Video Transcript
*********************************************

Transcripts are required for your videos. Transcripts are required for deaf or
hard of hearing learners to understand audio content, and helpful for learners
who speak other languages. You can allow students to download transcripts so
that they can read them offline. You associate a transcript with a video when
you create the video component.

Timed transcripts in the SubRip Text (.srt) format are strongly recommended. A
transcript in the .srt format appears next to its associated video and
automatically scrolls as the video plays. A student can click a word in the
transcript to jump to the point in the video where that word is spoken.

To create or obtain a transcript in .srt format, you can work with a company
that provides captioning services. EdX works with `3Play Media
<http://www.3playmedia.com>`_. `YouTube <http://www.youtube.com/>`_ also
provides captioning services.

When you upload an .srt file, a .txt file is created automatically. You can
allow students to download these transcript files. If you allow your students
to download transcripts, a **Download transcript** button appears under the
video. Students can then select either **SubRip (.srt) file** or **Text (.txt)
file** to download the .srt or .txt transcript.

.. image:: ../../../shared/building_and_running_chapters/Images/Video_DownTrans_srt-txt.png
   :width: 500
   :alt: Video status bar showing srt and txt transcript download options

You can also provide transcripts in different formats, such as .pdf, and you
can provide transcripts in different languages. For more information about
these options, see :ref:`Additional Transcripts`.

.. note:: Historically, some courses used .sjson files for video transcripts. 
 Use of .sjson files is no longer recommended; however, if transcripts in your
 course use this format, see :ref:`Steps for sjson files`.

.. _Post the Video Online:

*****************************
Step 3. Post the Video Online
*****************************

All course videos should be posted to YouTube. By default, the edX video player
accesses your YouTube videos.

Because YouTube is not available in all locations, however, we recommend that
you also post copies of your videos on a third-party site such as `Amazon S3
<http://aws.amazon.com/s3/>`_. When a student views a video in your course, if
YouTube is not available in that student's location or if the YouTube video
does not play, the video on the backup site starts playing automatically. You
can also allow the student to download the video from the backup site.

After you post your video online, make sure you have the URL for the video. If
you host copies of your video in more than one place, make sure you have the
URL for each video location.

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
site where you post the videos may have to handle a lot of traffic.

.. note:: The URL for the video that you post on a third-party site must end 
 in .mp4, .webm, .mpeg, or .ogg. (To help make sure all standard browsers can
 play your video, we **strongly** recommend that you use .mp4 or .webm format.)
 EdX cannot support videos that you post on sites such as Vimeo.

If you (or your beta testers or learners) encounter an error when you view a
course video, it might be the result of one of these browser-related problems.

* Verify that the browser is up to date. For example, some older versions of
  the Mozilla Firefox browser did not play .mp4 video files. This problem does
  not occur in more recent versions of this browser.

  For more information, see `Media formats supported by the HTML audio and
  video elements`_.

* Verify that file metadata, particularly the MIME type, is correctly set on
  the host site. Internet Explorer 9 and 10 browsers do not play videos if the
  MIME type is not set. For example, make sure that the HTTP header Content-
  Type is set to video/mp4 for an .mp4 file, or to video/webm for a .webm
  file.

  As an example of how you might set metadata on a video backup site, the
  *Console User Guide* for the Amazon Simple Storage Service provides this
  information about `editing object metadata`_.


.. _Create a Video Component:

********************************
Step 4. Create a Video Component
********************************

#. Under **Add New Component**, click **Video**.

#. When the new video component appears, click **Edit**. The video editor opens
   to the **Basic** tab.

   .. image:: ../../../shared/building_and_running_chapters/Images/VideoComponentEditor.png
    :alt: Image of the video component editor
    :width: 500

   You replace the default values with your own. 
   
3. In the **Component Display Name** field, enter an identifying name for this
   video. This name appears as a heading above the video and as a tooltip in
   the learning sequence at the top of the **Courseware** page.

#. In the **Default Video URL** field, enter the URL of the video. Example
   URLs follow.

   ::
   
      http://youtu.be/OEoXaMPEzfM
      http://www.youtube.com/watch?v=OEoXaMPEzfM
      https://s3.amazonaws.com/edx-course-videos/edx-edx101/EDXSPCPJSP13-G030300.mp4
      https://s3.amazonaws.com/edx-videos/edx101/video4.webm	

.. note:: To be sure all students can access the video, we recommend 
    providing both an .mp4 and a .webm version of your video. To do this, you
    can post additional versions of your videos on the Internet, then add the
    URLs for these versions below the default video URL. **These URLs cannot be
    YouTube URLs**. To add a URL for another version, click **Add URLs for
    additional versions**. The first listed video that is compatible with the
    student's computer plays.

5. Next to **Default Timed Transcript**, select an option. 

   * If edX already has a transcript for this video, Studio automatically
     finds the transcript and associates the transcript with the video. This
     situation can occur when you reuse a video from an existing course.
     
     If you want to modify the transcript, click **Download Transcript for
     Editing**. You can then make your changes and upload the new file by
     clicking **Upload New Transcript**.

   * If edX does not have a transcript for the video, but YouTube has a
     transcript, Studio automatically finds the YouTube transcript and asks if
     you want to import it. To use this YouTube transcript, click **Import
     YouTube Transcript**. (If you want to modify the YouTube transcript,
     import the YouTube transcript into Studio, and then click **Download
     Transcript for Editing**. You can then make your changes and upload the
     new file by clicking **Upload New Transcript**.)

   * If both edX and YouTube have a transcript for your video, but the edX
     transcript is out of date, you receive a message asking if you want to
     replace the edX transcript with the YouTube transcript. To use the YouTube
     transcript, click **Yes, replace the edX transcript with the YouTube
     transcript**.

   * If neither edX nor YouTube has a transcript for your video, and your
     transcript uses the .srt format, click **Upload New Transcript** to upload
     the transcript file from your computer.

     .. note:: 

        * If your transcript uses the .sjson format, do not use this setting.
          For more information, see :ref:`Steps for sjson files`.

        * If you want to provide a transcript in a format such as .pdf,
          do not use this setting to upload the transcript. For more
          information, see :ref:`Additional Transcripts`.

6. Optionally, click **Advanced** to set more options for the video. For a
   description of each option, see :ref:`Video Advanced Options`.

#. Click **Save.**
  
.. _Video Advanced Options:

==================
Advanced Options
==================

The following options appear on the **Advanced** tab in the video component.

.. list-table::
    :widths: 30 70

    * - **Component Display Name**
      - The name that you want your students to see. This is the same as the
        **Display Name** field on the **Basic** tab.
    * - **Default Timed Transcript**
      -  The name of the transcript file that is used in the **Default Timed
         Transcript** field on the **Basic** tab. This field is auto-populated.
         You do not have to change this setting.
    * - **Download Transcript Allowed**
      - Specifies whether you want to allow students to download the timed
        transcript. If you select **True**, a link to download the
        file appears below the video.

        By default, Studio creates a .txt transcript when you upload an .srt
        transcript. Students can download the .srt or .txt versions of the
        transcript when you set **Download Transcript Allowed** to **True**. If
        you want to provide the transcript for download in a different format
        as well, such as .pdf, upload a file to Studio by using the **Upload
        Handout** field.

    * - **Downloadable Transcript URL**
      - The URL for a non-.srt version of the transcript file posted on the
        **Files & Uploads** page or on the Internet. Students see a link to
        download the non-.srt transcript below the video.

        When you add a transcript to this field, only the transcript that you
        add is available for download. The .srt and .txt transcripts become
        unavailable. If you want to provide a downloadable transcript in a
        format other than .srt, we recommend that you upload a handout for
        students by using the **Upload Handout** field. For more information,
        see :ref:`Additional Transcripts`.

    * - **EdX Video ID**
      - An optional field used only by course teams that are working with
        edX to process and host video files.
    * - **Show Transcript**
      - Specifies whether the transcript plays along with the video by default.
    * - **Transcript Languages**
      - The transcript files for any additional languages. For more
        information, see :ref:`Transcripts in Additional Languages`.
    * - **Upload Handout**
      - Allows you to upload a handout to accompany this video. Your handout
        can be in any format. Students can download the handout by clicking
        **Download Handout** under the video.
    * - **Video Available on Web Only**
      - If you select **True**, students are only allowed to play this video
        in a Web browser. If you select **False**, students can use any
        compatible application to play the video, including Web browsers and
        mobile apps.
    * - **Video Download Allowed**
      - Specifies whether students can download versions of this video in
        different formats if they cannot use the edX video player or do not
        have access to YouTube. If you select **True**, you must add
        at least one non-YouTube URL in the **Video File URLs** field.
    * - **Video File URLs**
      - The URL or URLs where you posted non-YouTube versions of the video.
        Every URL should end in .mpeg, .webm, .mp4, or .ogg and cannot be a
        YouTube URL. Each student will be able to view the first listed video
        that is compatible with the student's computer. To allow students to
        download these videos, you must set **Video Download Allowed** to
        **True**.

        To help make sure all standard browsers can play your video, we
        **strongly** recommend that you use the .mp4 or .webm format.

    * - **Video Start Time**
      - The time you want the video to start if you do not want the entire
        video to play. Formatted as HH:MM:SS. The maximum value is 23:59:59.

        Note that YouTube offers an option to play the entire video,
        regardless of the specified start time. When possible, cut your video
        files to the desired length before you upload them.

    * - **Video Stop Time**
      - The time you want the video to stop if you do not want the entire video
        to play. Formatted as HH:MM:SS. The maximum value is 23:59:59.

        Note that YouTube offers an option to play the entire video,
        regardless of the specified stop time. When possible, cut your video
        files to the desired length before you upload them.

    * - **YouTube IDs**
      - If you have uploaded separate video files to YouTube for different
        speeds of your video (YouTube ID for .75x speed, YouTube ID for 1.25x
        speed, YouTube ID for 1.5x speed), enter the YouTube IDs for these
        videos in these fields. These settings are optional, to support video
        play on older browsers.

.. _Video TOC:

***************************
Video Table of Contents
***************************

You can add a table of contents for your video by adding an .srt transcript
file that contains clickable links to different parts of the video. When your
students view the video, they can click the **CC** button at the bottom of the
video player to switch between the main transcript for the video and the table
of contents.

To add a table of contents, you work with a third-party service to create
the .srt transcript file. Then, you use the **Transcript Languages** setting
in the video component to associate the .srt file with the video.

.. image:: ../../../shared/building_and_running_chapters/Images/VideoTOC.png
   :alt: Image of a video with a transcript that has links to different parts
    of the video
   :width: 500

#. After you obtain the .srt transcript file that will function as the
   table of contents, open the video component for the video.

#. On the **Advanced** tab, scroll down to **Transcript Languages**, and then
   click **Add**. 

#. In the drop-down list that appears, select **Table of Contents**. 

   An **Upload** button appears.

#. Click **Upload**, browse to the .srt file for the transcript, and then click
   **Open**.

#. In the **Upload translation** dialog box, click **Upload**.

.. _Additional Transcripts:

**********************
Additional Transcripts
**********************

By default, a .txt file is created when you upload an .srt file, and students
can download an .srt or .txt transcript when you set **Download Transcript
Allowed** to **True**. The **Download Transcript** button appears below the
video, and students see the .srt and .txt options when they move the cursor
over the button.

.. image:: ../../../shared/building_and_running_chapters/Images/Video_DownTrans_srt-txt.png
   :width: 500
   :alt: Video status bar showing srt and txt transcript download options

If you want to provide a downloadable transcript in a format such as .pdf along
with the .srt and .txt transcripts, we recommend that you use the **Upload
Handout** field. When you do this, a **Download Handout** button appears to the
right of the **Download Transcript** button, and students can download the
.srt, .txt, or handout version of the transcript.

.. image:: ../../../shared/building_and_running_chapters/Images/Video_DownTrans_srt-handout.png
   :width: 500
   :alt: Video status bar showing srt, txt, and handout transcript download
    options

To add a downloadable transcript, you use the **Upload Handout** field.

#. Create or obtain your transcript as a .pdf or in another format.
#. In the video component, click the **Advanced** tab.
#. Locate **Upload Handout**, and then click **Upload**.
#. In the **Upload File** dialog box, click **Choose File**.
#. In the dialog box, select the file on your computer, and then click
   **Open**.
#. In the **Upload File** dialog box, click **Upload**.

Before Studio added the **Upload Handout** feature, some courses posted
transcript files on the **Files & Uploads** page or on the Internet, and then
added a link to those files in the video component. **We no longer recommend
this method.**  When you use this method, the **Download Transcript** button
appears, but only the transcript that you add is available for download. The
.srt and .txt transcripts become unavailable.

.. image:: ../../../shared/building_and_running_chapters/Images/Video_DownTrans_other.png
   :width: 500
   :alt: Video status bar showing Download Transcript button without srt and
    txt options

If you want to use this method, you can post your transcript online, and then
add the URL to the transcript in the **Downloadable Transcript URL** field.
However, bear in mind that students will not be able to download .srt or .txt
transcripts.

.. _Transcripts in Additional Languages:

====================================
Transcripts in Additional Languages
====================================

You can provide transcripts for your video in other languages. To do this,
you work with a third-party service to obtain an .srt transcript file for
each language, and then associate the .srt file with the video in Studio.

#. After you obtain the .srt files for additional languages, open the
   video component for the video.

#. On the **Advanced** tab, scroll down to **Transcript Languages**, and then
   click **Add**.

#. In the drop-down list that appears, select the language for the transcript
   that you want to add.

   An **Upload** button appears below the language.

#. Click **Upload**, browse to the .srt file for the language that you want,
   and then click **Open**.

#. In the **Upload translation** dialog box, click **Upload**.

#. Repeat steps 2 - 5 for any additional languages. 

.. note:: Make sure that all your transcript file names are unique to each 
 video and language. If you use the same transcript name in more than one video
 component, the same transcript will play for each video. To avoid this
 problem, you could name your foreign language transcript files according to
 the video's file name and the transcript language.

 For example, you have two videos, named video1.mp4 and video2.mp4. Each video
 has a Russian transcript and a Spanish transcript. You can name the
 transcripts for the first video video1_RU.srt and video1_ES.srt, and name the
 transcripts for the second video video2_RU.srt and video2_ES.srt.

When your students view the video, they can click the **CC** button at the
bottom of the video player to select a language.

.. image:: ../../../shared/building_and_running_chapters/Images/Video_LanguageTranscripts_LMS.png
   :alt: Video playing with language options visible

.. _Steps for sjson files:

**********************
Steps for .sjson Files
**********************

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
   
#. Upload the .sjson file for your video to the **Files & Uploads** page.
#. Create a new video component.
#. On the **Basic** tab, enter the name that you want students to see in the
   **Component Display Name** field.
#. In the **Video URL** field, enter the URL of the video. For example, the URL
   may resemble one of the following.

   ::
   
      http://youtu.be/OEoXaMPEzfM
      http://www.youtube.com/watch?v=OEoXaMPEzfM
      https://s3.amazonaws.com/edx-course-videos/edx-edx101/EDXSPCPJSP13-G030300.mp4

#. Click the **Advanced** tab.
#. In the **Default Timed Transcript** field, enter the file name of your
   video. Do not include `subs_` or `.sjson`. For the example in step 2, you
   would only enter **Lecture1a**.
#. Set the other options that you want.
#. Click **Save**.

.. _Creating Videos: https://courses.edx.org/courses/edX/edX101/2014/courseware/c2a1714627a945afaceabdfb651088cf/9dd6e5fdf64b49a89feac208ab544760/

.. _edX101 Overview of Creating an edX Course: https://www.edx.org/node/5496#.VH8p51fF_FA
.. _Media formats supported by the HTML audio and video elements: https://developer.mozilla.org/en-US/docs/Web/HTML/Supported_media_formats#MP4_H.264_(AAC_or_MP3)
.. _editing object metadata: http://docs.aws.amazon.com/AmazonS3/latest/UG/EditingtheMetadataofanObject.html