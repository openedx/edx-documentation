.. _Additional Video Options:

###################################
Specifying Additional Video Options
###################################

When you create a video component, you can specify additional options such as
download options for the video and transcript, video license options, and a
start and stop time for the video.

.. contents::
  :local:
  :depth: 1

.. _Enable Video and Transcript Downloads:

********************************************
Enable Video and Transcript Downloads
********************************************

You can allow learners to download videos and transcript files that you have
provided so that they can view them offline.

To enable video and transcript downloads, follow these steps.

#. In the video component, select the **Advanced** page.
#. For **Video Download Allowed**, select **True** to allow learners to
   download the video.
#. For **Download Transcript Allowed**, select **True** to allow learners to
   download an .srt or .txt video transcript.
#. Select **Save**.

To test transcript downloads for the video, select **Download transcript** in
the video player’s control bar. You can download either the SubRip (.srt)
format or text (.txt) format.

.. _Video Advanced Options:

********************
Set Advanced Options
********************

The following options appear on the **Advanced** page of the video component.

.. list-table::
    :widths: 30 70

    * - **Component Display Name**
      - The name that you want your learners to see. This is the same as the
        **Display Name** field on the **Basic** page.
    * - **Default Timed Transcript**
      - This is the same as the **Default Timed Transcript** setting on the
        **Basic** page. You can specify the default timed transcript on either
        page.
    * - **Download Transcript Allowed**
      - Specifies whether you want to allow learners to download the .srt or
        .txt transcript. (By default, Studio creates a .txt transcript when you
        upload an .srt transcript.) If you select **True**, a link to download
        the file appears below the video.

        If you want to provide a downloadable transcript in a different format
        as well, such as .pdf, see :ref:`Additional Transcripts`.

    * - **Downloadable Transcript URL**
      - The URL for a non-.srt version of the transcript file posted on the
        internet. Learners see a link to download the non-.srt transcript below
        the video.

        .. important::
          When you add a transcript to the **Downloadable Transcript URL**
          field, only the transcript that you add is available for download.
          The .srt and .txt transcripts become unavailable. If you want to
          provide a downloadable transcript in addition to the .srt and .txt
          transcripts, edX recommends that you upload a handout for learners by
          using the **Upload Handout** field. For more information, see
          :ref:`Additional Transcripts`.

    * - **License**
      - Optionally, you can set the license for the video, if you want to
        release the video with a license different from the overall course
        license.

        * Select **All Rights Reserved** to indicate to learners that you own
          the copyright for the video.

        * Select **Creative Commons** to grant others the right to share and
          use the video. You must then select the Creative Commons license
          options that you want.

          The license options that you select control the copyright notice that
          learners see for the video. For more information, see :ref:`Licensing
          a Course`.

    * - **Show Transcript**
      - Specifies whether the transcript appears next to the video by default.
        If this is set to **False**, learners can still view transcripts by
        selecting the **Show Transcript** (”) icon.
    * - **Transcript Languages**
      - The transcript files for any additional languages. For more
        information, see :ref:`Transcripts in Additional Languages`.
    * - **Upload Handout**
      - Allows you to upload a handout to accompany the video, such as a PDF
        transcript or other handout. Learners can download the handout by
        selecting **Download Handout** under the video. The procedure for
        adding handouts is the same as the procedure for adding a supplemental
        transcript. For more information, see :ref:`Additional Transcripts`.
    * - **Video Available on Web Only**
      - If you select **True**, learners can only play this video in a web
        browser. If you select **False**, learners can use any compatible
        application to play the video, including web browsers and mobile apps.
    * - **Video Download Allowed**
      - Specifies whether learners can download the video. If you select
        **True**, you must add at least one URL in the **Video File URLs**
        field.
    * - **Video File URLs**
      - The URL or URLs where you posted different versions of the video. On
        the **Basic** tab, if you added URLs by selecting **Add URLs for
        additional versions** below the **Default Video URL** field , the URLs
        are listed in the fields next to **Video File URLs**.

        Every URL must end in .mp4, .mpeg, .webm, or .ogg. Learners will view
        the first listed video that is compatible with their computer or mobile
        device.

        For the best experience for mobile users, make sure that the URL for
        the 360p version of the video is the first URL in the list.

        To help make sure all standard browsers can play your video, we
        **strongly** recommend that you use the .mp4 format.

    * - **Video ID**
      - The identifier that the video process assigns to the video. This field
        is the same as the **Video ID** setting on the **Basic** page. Only
        courses on edx.org use this field.

    * - **Video Start Time**
      - The time you want the video to start if you do not want the entire
        video to play. Use HH:MM:SS format. The maximum value is 23:59:59.

        .. note::
           Learners who play video in the mobile app see the entire video file.
           Only videos that play in a browser start playing at the specified
           start time.

    * - **Video Stop Time**
      - The time you want the video to stop if you do not want the entire video
        to play. Use HH:MM:SS format. The maximum value is 23:59:59.

        .. note::
           Learners who play video in the mobile app see the entire video file.
           Only videos that play in a browser stop playing at the specified
           stop time.

    * - **YouTube IDs**
      - As of March 2018, edX no longer supports videos on YouTube.


