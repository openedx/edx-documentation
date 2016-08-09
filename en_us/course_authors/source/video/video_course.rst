.. _Adding Videos to a Course:

#############################
Adding Videos to a Course
#############################

After automated processing of an :ref:`uploaded video file<Uploading Videos in
Studio>` begins and its status on the **Video Uploads** page is Ready, you can
include it in your course. To do so, you :ref:`copy the unique ID<Copy the edX
Video ID>` that is assigned to an uploaded video and then :ref:`add it to a
video component<Add the edX Video ID to a Video Component>`. A video file,
`Adding a Video ID`_, is also available to show you how to complete this
process.

This section also describes how you :ref:`add a transcript<Add a Video
Transcript>` and associate it with the video file in a video component.

.. _Copy the edX Video ID:

************************
Copy the Video ID
************************

#. Open the course in Studio.

#. Select **Content**, then **Video Uploads**.

#. In the **Previous Uploads** list, locate the video that you want to include
   in the course.

#. Select the value in the **Video ID** column for the video. The video ID is
   assigned when you upload a video.

#. Right-click and select **Copy**. Be sure to select and copy the entire
   video ID value.

   Next, you paste this value into the **Video ID** field for a video
   component. See :ref:`Add the edX Video ID to a Video Component`.

   .. note:: The video ID is available for every uploaded file. However,
    for a video component to deliver its content to learners, the status for
    the file must be Ready on the **Video Uploads** page.

You can also download a report of all uploaded videos on the **Video Uploads**
page: select **Download available encodings (.csv)**. The report includes the
video ID for every uploaded file.

.. to come: how to download a CSV

.. _Add the edX Video ID to a Video Component:

************************************************
Add the Video ID to a Video Component
************************************************

This section describes the procedure that course teams follow to add an
uploaded video file to a video component in an edx.org course. You follow this
procedure in place of the :ref:`Create a Video Component` section in this
guide. This section assumes that you are familiar with the procedures described
in the :ref:`Developing Your Course Index` section.

You complete these steps in Studio. For convenience, :ref:`download the report
of uploaded videos<Reporting Video Status>` and open it on your desktop before
you begin. Alternatively, open a second browser window so that the video IDs on
the **Video Uploads** page appear in one window while you work with video
components in the other.

#. From the **Content** menu select **Outline**. The **Course Outline** page
   opens.

#. Select or add a unit, and then select **Video** to add a video component.

   To edit an existing video component, locate the video component window, and
   then select **Edit**. The Editing: Video dialog box opens to the **Basic**
   tab.

#. For the **Component Display Name**, enter the identifying name that you want
   learners to see for this video.

#. Select the **Advanced** tab for the Editing: Video dialog box.

   Additional fields appear below the **Component Display Name** and **Default
   Timed Transcript** fields.

#. For the **Video ID**, paste in the ID of the video file that you want
   to play. See :ref:`Copy the edX Video ID`.

   When you supply a valid video ID in this field, you associate your video
   component with files on YouTube and AWS that are optimized for viewing with
   different devices and bandwidths. You do not need to add values to the
   **Default Video URL**, **Video File URLs**, or **YouTube ID** fields. The
   URLs that are associated with the video ID override any existing values in
   those fields.

#. Set **Video Download Allowed** to **True** or **False** to define whether
   learners can download this video.

#. Select **Save**. The referenced video appears in the video component.

   .. note:: For the video to appear, a destination URL must be available for
    at least one of the formats and host sites that are the result of the edX
    video process.

To complete video component setup, you add a transcript file for the video.

.. _Add a Video Transcript:

************************************************
Add a Transcript
************************************************

Transcripts are required for your videos. Transcripts are required for deaf or
hard of hearing learners to understand audio content, and helpful for learners
who speak other languages.

Timed transcripts in the SubRip Text (.srt) format are recommended. A
transcript in the .srt format appears next to its associated video and
automatically scrolls as the video plays. A learner can select a word in the
transcript to jump to the point in the video where that word is spoken.

This section briefly describes the procedures that course teams follow to add
transcripts to their videos. For more information, see the :ref:`Create
Transcript` section in this guide.

======================================
Create or Obtain a Transcript
======================================

To create or obtain a transcript in .srt format, you can work with a company
that provides captioning services.

To ensure quality and accuracy of transcripts, edX works with `3Play Media`_.
To request a 3Play Media account at edX's discounted rate, contact 3Play at
http://www.3playmedia.com/edx/.

===================================
Associate a Transcript with a Video
===================================

Before you can associate a transcript with a video, the encoding and hosting
process must be complete for the video file, and its status must be Ready on
the **Video Uploads** page. You make the association between a video file and
a transcript file in Studio, in the video component.

* If your captioning service provider delivers .srt files to you, you can
  upload the .srt file from your computer.

* If your captioning service provider adds subtitles or closed captions to
  your videos on YouTube, you can import those subtitles or captions from
  YouTube.

Studio saves files from either source in the SubRip (.srt) format. Studio also
saves the files in text (.txt) format automatically.

To associate a transcript with a video, follow these steps.

.. note::
 This procedure assumes that you have already created the video component and
 followed the procedures to :ref:`add the video ID<Add the edX Video ID to
 a Video Component>` to it. In addition, you must have the .srt file, or the
 subtitles or captions must be available on YouTube, before you complete
 these steps.

#. On the **Course Outline** page in edX Studio, locate the unit that contains
   the video component, and then select the unit name.

#. Locate the video component window and select **Edit**.

#. Next, either you upload an .srt file or you import YouTube subtitles or
   captions.

   * To upload an .srt file from your computer: For the **Default Timed
     Transcript** select **Upload New Transcript**, and then select the
     .srt file from your computer.

   * To import YouTube subtitles or captions: For the **Default Timed
     Transcript** select **Import from YouTube**.

#. Select **Save**.

To test the transcript with the video, select the **Show transcript** (") icon
in the video player's control bar. The transcript file scrolls while the video
file plays. You can also test the transcript by selecting the **CC** icon.

.. note:: In some cases, two sets of captions can appear when you select
  **CC**. This situation can occur if YouTube is the host service for the video
  and your YouTube account settings for playback are set to always show
  captions. As a result, YouTube and your course might both provide captions
  for the video. To correct this problem, select **CC** again or change your
  YouTube account setting.

============================
Enable Transcript Downloads
============================

You can allow learners to download transcript files so that they can read them
offline. You can enable downloads for transcripts that you upload yourself or
that you import from YouTube.

To enable transcript downloads, follow these steps.

#. On the **Course Outline** page in edX Studio, locate the unit that contains
   the video component, and then select the unit name.

#. Locate the video component window and select **Edit**.

#. Select **Advanced**.

#. Set **Download Transcript Allowed** to **True**.

#. Select **Save**. The referenced files (.srt) and (.txt) are now available
   to download.

To test transcript downloads for the video, select **Download transcript** in
the video player's control bar. You can choose either the SubRip (.srt) format
or text (.txt) format to download.

.. include:: ../../../links/links.rst
