.. _Obtain a Video Transcript:

#########################
Obtain a Video Transcript
#########################



Transcripts are required for all videos. Transcripts help learners with
hearing impairments understand audio content, and they are helpful for learners
who speak other languages.

Transcripts are available to learners in the following ways.

* Learners can select the **Show transcript** (”) icon in the video player’s
  control bar to show the transcript next to the video. The transcript
  automatically scrolls as the video plays. Learners can select a line in the
  transcript to jump to the point in the video where that line is spoken.
* Learners can show the transcript file as overlaid closed captions for the
  video by selecting the **CC** icon in the video player’s control bar.
* You can allow learners to download transcripts so that learners can read the
  transcripts offline. For more information, see :ref:`Enable Video and
  Transcript Downloads`.

****************************
Obtaining a Video Transcript
****************************


.. only:: Partners

  To obtain a transcript in .srt format, you can work with a transcript
  provider such as `3Play Media`_ or `cielo24`_. 3Play Media and cielo24 offer
  a discounted rate for edX.org partners.

  * If your course is on edx.org and you work with 3Play Media or cielo24, you
    can use integrated video transcripts in Studio to obtain transcripts and
    associate them with your videos automatically. For more information, see
    :ref:`Integrated Transcripts`.

  * If you do not work with 3Play Media or cielo24, or your course is on Edge,
    or you must obtain transcripts from a third party transcript provider and
    associate them with your videos manually. For more information, see
    :ref:`Non Integrated Transcripts`.

  .. note::
    For courses on edx.org, transcripts must be in the SubRip Text (.srt)
    format. We strongly recommend that you format your .srt files as plain text
    with no encoding. Encodings such as ``UTF-8`` and ``ANSI - Western Roman``
    can cause errors.

    For courses on Edge, we strongly recommend that your timed transcripts use
    the .srt format.

    If you use a third party transcript provider other than 3Play Media or
    cielo24, make sure that your finished transcripts are in .srt format.

  .. _Integrated Transcripts:

  ======================
  Integrated Transcripts
  ======================

  When you use integrated transcripts, you upload your videos in Studio. The
  edX processing service then creates transcripts, uploads the transcripts, and
  links the transcripts with your videos automatically.

  To use integrated transcripts, you must make sure that settings are correct
  for both your organization and for your individual course.

  .. contents::
   :local:
   :depth: 1

  .. _Add or Change Organization Settings:

  Add or Change Organization Settings
  ***********************************

  .. important::
    Usually, an administrator at your organization establishes organization
    settings with a transcript provider. Do not change any of these settings
    without contacting your organization's administrator.

  Organization settings for integrated transcripts include the following
  settings.

  * The transcript provider.
  * The organization's account credentials for the provider.

  To add or change your organization settings, follow these steps.

  #. Contact either `3Play Media`_ or `cielo24`_, and specify that you are an
     edX partner.

     3Play Media or cielo24 give you credentials that you then enter in Studio.

  #. When you receive account credentials from 3Play Media or cielo24, open
     your course in Studio, and then select **Video Uploads** on the
     **Content** menu.

  #. On the **Video Uploads** page, locate and select **Course Video
     Settings**.

  #. In the **Course Video Settings** panel, specify the settings for your
     organization.

     .. important::
      If the settings for your course are different from the settings for your
      organization, make sure that you contact your organization's
      administrator before you change these settings.

     * If your organization uses 3Play Media, follow these steps.

       #. Under **Automated Transcripts**, select **3Play Media**.

       #. In the **API Key** and **API Secret** fields, enter the credentials
          that you received from 3Play Media.

          .. note::
            edX currently supports 3PlayMedia API **v1** credentials only. Using v3 credentials
            will result in a failure when attempting to submit a transcription or translation job.

       #. Select **Update Settings**.

     * If your organization uses cielo24, follow these steps.

       #. Under **Automated Transcripts**, select **cielo24**.

       #. In the **Username** and **API Key** fields, enter the credentials
          that you received from cielo24.

       #. Select **Update Settings**.


  .. _Add or Change Course Settings:

  Add or Change Course Settings
  *****************************

  The following settings are specific to each individual course. You can change
  these settings without contacting your organization's administrator.

  .. note::
    If you change these settings, the changes take effect for all videos that
    you upload after you make the changes. You cannot change a setting for a
    specific video.

  To add or change course settings, follow these steps.

  #. Open your course in Studio, and then select **Video Uploads** on the
     **Content** menu.

  #. On the **Video Uploads** page, locate and select **Course Video
     Settings**.

  #. In the **Course Video Settings** panel, specify the settings for your
     organization.

     * If your organization uses 3Play Media, select the options that you want
       in the **Transcript Turnaround** and **Video Source Language** fields.

     * If your organization uses cielo24s, select the options that you want in
       the **Transcript Turnaround** and **Transcript Fidelity** fields.

  #. Select **Update Settings**.


  .. _Non Integrated Transcripts:

  ==========================
  Non-Integrated Transcripts
  ==========================

  If you work with a transcript provider other than 3Play Media or cielo24, or
  your course is on Edge, you cannot use the integrated video transcript
  functionality in Studio. Instead, you send your videos to the transcript
  provider, and the provider sends you the completed transcripts. You later
  upload the transcripts when you :ref:`create a video component <Add a Video>`.

  If your course is on Edge, integrated transcript functionality is not
  available even if you work with 3Play Media or cielo24.

.. only:: Open_edX

  When you work with a transcript provider, you send your videos to the
  transcript provider, and the provider sends you the completed transcripts.
  You later upload the transcripts when you :ref:`create a video
  component<Adding a Video to a Course>`.

**********************************
Transcript File Naming Conventions
**********************************

To prevent errors when you upload your video transcripts, we recommend the
following conventions for naming your transcript files.

.. only:: Partners

  .. note::
    If your course uses integrated video transcripts, the edX video processing
    service names your transcripts automatically. For more information, see
    :ref:`Integrated Transcripts`.

* Give each transcript file an identifying name that is unique across all of
  your course uploads, including non-transcript files.
* Make sure that the transcript contains no special characters, such as ç, å,
  or ó.
* Make sure that the file type (``.srt``) is in lowercase.
* Do not include periods in file names other than the period before the .srt
  file type.

.. include:: ../../../../links/links.rst
