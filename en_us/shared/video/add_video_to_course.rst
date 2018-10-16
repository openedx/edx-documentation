* A display name for the component.
* The video location.

  The video location is the video URL that is created when you upload the video
  to the hosting site. The video URL might resemble the following example.

  ``https://s3.amazonaws.com/edx-course-videos/edx-edx101/EDXSPCPJSP13-G030300.mp4``

* The video transcript.

.. _Add a Video and Transcript:

**************************
Add a Video and Transcript
**************************

To add a video and its transcript, follow these steps.

#. In Studio, locate the unit that you want, and then select **Video** under
   **Add New Component**.

#. When the new video component appears, select **Edit**.

   The video editor opens to the **Basic** page.

#. In the **Component Display Name** field, enter the name that you want
   learners to see for this video.

   This name appears as a heading above the video in the LMS, and it identifies
   the video for you in Insights. If you do not enter a display name, the
   platform specifies “video” for you.

#. Locate the **Default Video URL** field, and then enter the location of your
   video. This is the URL that was created when you uploaded the video to the
   hosting site.

   .. note::
     If you have created multiple versions that use different encodings or
     hosting services, add the URL for each video by selecting **Add URLs for
     additional versions** below the **Default Video URL** field. The first
     listed video that is compatible with the learner's computer plays.

     For the best experience for mobile users, make sure that the URL for the
     360p version of the video is the first URL in the list.

5. Add the .srt transcript to the video. To do this, locate **Default Timed
   Transcript**, and then select one of the following options.

   * If Studio already has a transcript for this video, Studio automatically
     adds the transcript in the **Default Timed Transcript** field. This
     situation can occur when you reuse a video from an existing course. You do
     not have to make any changes.

   * If Studio does not have a transcript for the video, and the
     transcript uses the .srt format, select **Upload New Transcript** to
     upload the .srt transcript file from your computer.

     .. note::

      Only use this option for transcripts in .srt format. If you want to
      provide a transcript in any other format, such as .pdf,
      see :ref:`Additional Transcripts`.

6. Optionally, select **Advanced** to set more options for the video. For a
   description of each option, see :ref:`Video Advanced Options`.

#. Select **Save** to save the video component.

To test the transcript with the video, after you have saved the video, select
the **Show transcript** (”) icon in the video player’s control bar. The
transcript file scrolls while the video file plays. You can also test the
transcript by selecting the **CC** icon.


