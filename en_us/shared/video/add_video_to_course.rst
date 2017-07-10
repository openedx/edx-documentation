.. _Add a Video to a Course:

################################
Step 4. Add a Video to a Course
################################

After you have uploaded your video files to a hosting service, you can add the
video to your course.

To add a video to a course, you create a video component in a unit in Studio,
and then you add the following information for the video to the video
component.

* A display name for the component.

* The video location.

  .. only:: Partners

    For courses on edx.org, you use the **video ID** that the upload process
    automatically creates for your video. You find this video ID on the **Video
    Uploads** page in Studio. For more information, see :ref:`Create a Video
    Component`.

    For courses on Edge, you use the **video URL** that is created for the
    video when you upload the video to YouTube or another site. The video URL
    might resemble one of the following examples.

  .. only:: Open_edX

    The video location is the video URL that is created when you upload the
    video to YouTube or to another hosting site. The video URL might resemble
    one of the following examples.

  * ``http://youtu.be/OEoXaMPEzfM``
  * ``http://www.youtube.com/watch?v=OEoXaMPEzfM``
  * ``https://s3.amazonaws.com/edx-course-videos/edx-edx101/EDXSPCPJSP13-G030300.mp4``

* The video transcript. When you add the transcript to the video component, you
  can upload .srt files, or you can import subtitles or closed captions from
  YouTube.

  For more information about obtaining a transcript, see :ref:`Create the
  Transcript`.

  .. only:: Partners

     For courses on edx.org, a transcript for the video is available when the
     video has a status of "Ready" on the **Video Uploads** page. Your
     captioning service provider might deliver .srt files to you, or might add
     subtitles or closed captions to your videos on YouTube.

.. _Create a Video Component:

*********************************
Create a Video Component
*********************************

.. only:: Partners

  .. note::
    For courses on edx.org, the first step is to copy the video ID. Courses on
    Edge do not follow this procedure.

    To copy the video ID, follow these steps.

    #. Open the course in Studio.

    #. On the **Content** menu, select **Video Uploads**.

    #. In the **Previous Uploads** list, locate the video that you want to
       include in the course.

    #. Select the value in the **Video ID** column for the video. The video ID
       is assigned when you upload a video.

    #. Right-click the value, and then select **Copy**. Be sure to select and
       copy the entire video ID value. You will paste this value into the
       **Video ID** field for a video component. For more information, see
       :ref:`Add the edX Video ID to a Video Component`.

    Note that the course team can add a video to their course as soon as the
    unique video ID is visible in the **Previous Uploads** list on the **Video
    Uploads** page. However, for a video to play successfully, the status for
    the file must be “Ready”. Processing takes 24 hours to complete for all
    encodings and all video hosting sites.

    You can also download a report of all uploaded videos on the **Video
    Uploads** page: select **Download available encodings (.csv)**. The report
    includes the video ID for every uploaded file.

To add a video and its transcript to your course, follow these steps.

#. In Studio, locate the unit that you want, and then select **Video** under
   **Add New Component**.

#. When the new video component appears, select **Edit**.

   The video editor opens to the **Basic** page.

#. In the **Component Display Name** field, enter the name that you want
   learners to see for this video.

   This name appears as a heading above the video in the LMS, and it identifies
   the video for you in Insights. If you do not enter a display name, the
   platform specifies “video” for you.

.. only:: Partners

  4. Add the video ID or video URL.

     * If your course will be on edx.org, locate the **Video ID** field, and
       then paste the video ID for the video file. For more information, see
       :ref:`Create a Video Component`.

       .. note::
         When you add the video ID, you do not need to add values to the
         **Default Video URL**, **Video File URLs**, or **YouTube ID** fields.
         The video ID automatically associates your video component with files
         on YouTube and AWS that are optimized for viewing with different
         devices and bandwidths. The URLs that are associated with the video ID
         override any existing values in other fields.

     * If your course will be on Edge, locate the **Default Video URL** field,
       and then enter the URL of the video.

.. only:: Open_edX

  4. Add the video URL. To do this, locate the **Default Video URL** field, and
     then enter the URL that was created when you uploaded the video to YouTube
     or to another site.

   .. note::
     If you have created multiple versions that use different encodings or
     hosting services, add the URL for each video by selecting **Add URLs for
     additional versions** below the **Default Video URL** field. The first
     listed video that is compatible with the learner’s computer plays. **These
     URLs cannot be YouTube URLs.**


5. Add the transcript to the video. To do this, locate **Default Timed
   Transcript**, and then select one of the following options.

   .. only:: Partners

     For edx.org courses, select one of the following options.

     * To upload an .srt file from your computer, select **Upload New
       Transcript**, and then select the .srt file from your computer.

     * To import YouTube subtitles or captions, select **Import from YouTube**.

     For Edge courses, select one of the following options.

   * If Studio already has a transcript for this video, Studio automatically
     adds the transcript in the **Default Timed Transcript** field. This
     situation can occur when you reuse a video from an existing course. You do
     not have to make any changes.

   * If edX does not have a transcript for the video, but YouTube has a
     transcript, Studio automatically finds the YouTube transcript and asks if
     you want to import it. To use this YouTube transcript, select **Import
     YouTube Transcript**.

   * If both edX and YouTube have a transcript for your video, but the edX
     transcript is out of date, you receive a message asking if you want to
     replace the edX transcript with the YouTube transcript. To use the YouTube
     transcript, select **Yes, replace the edX transcript with the YouTube
     transcript**.

   * If neither edX nor YouTube has a transcript for your video, and your
     transcript uses the .srt format, select **Upload New Transcript** to
     upload the transcript file from your computer.

     .. note::

        * If you want to provide a transcript in a format such as .pdf, do not
          use the **Default Timed Transcript** field to upload the transcript.
          For more information, see :ref:`Additional Transcripts`.

        * If your transcript uses the .sjson format, do not use this field.
          For more information, see :ref:`Steps for sjson files`.

6. Optionally, select **Advanced** to set more options for the video. For a
   description of each option, see :ref:`Video Advanced Options`.

#. Select **Save** to save the video component.

To test the transcript with the video, after you have saved the video, select
the **Show transcript** (”) icon in the video player’s control bar. The
transcript file scrolls while the video file plays. You can also test the
transcript by selecting the **CC** icon.


