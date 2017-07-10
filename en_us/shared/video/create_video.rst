.. _Create the Video:

#########################
Step 1. Create the Video
#########################

Your videos can contain whatever content you want to include in the course. The
following resources can help you to create good video content that is based on
extensive experimental research in student learning.

* The `Creating Videos`_ section of `Overview of Creating an edX Course`_
* Richard E. Mayer's `12 Principles of Multimedia Learning`_

.. _Compression Specifications:

******************************
Guidelines for Video Files
******************************

When you create video files, keep the following guidelines in mind.

* Videos should be as short as possible. Learners are more likely to finish
  watching videos that are no more than 5-10 minutes long.
* Each video file that you upload must be less than 5GB in size.
* Each video should follow established :ref:`file naming conventions <File
  Naming Conventions>` and :ref:`video compression specifications <Video
  Compression Specifications>`.
* The edX video player supports videos in .mp4, .mpeg, .webm, and .ogg format.
  However, to help make sure all standard browsers can play your video, edX
  **strongly** recommends that you use the .mp4 format.

Additionally, for information about ensuring that your videos are available to
learners who use the edX mobile apps, see :ref:`installation:Configuring Video
Modules for Mobile`.

  .. only:: Partners

    .. note::
      For courses on edx.org, in a later step, you upload your videos to edX,
      and edX then automatically transforms each of your uploaded video files
      into several different formats. For this process to succeed, you must
      upload videos in .mp4 or .mov format. For more information, see
      :ref:`Uploading Videos in Studio`.

.. _File Naming Conventions:

=======================
File Naming Conventions
=======================

Each video file must have a unique name. We strongly recommend that
organizations define a naming convention for video files, and apply that
convention to videos for all courses to facilitate identifying and tracking
video files.

At a minimum, your naming convention should include these elements.

* A course identifier.
* The year of the initial course run.
* A revision or version number.

For example, you might use the following naming convention.

::

  {course number}_{year}_{section}_{subsection}_{unit}_{version}.{type}

This convention might yield the following file name.

::

  SPU27_2015_S1_SS3_U4_v2.mp4

.. note::
  Include only alphanumeric characters and underscores in video file names. Do
  not use periods except for the period before the file name extension (for
  example, .mp4).


.. _Video Compression Specifications:

=================================
Video Compression Specifications
=================================

After you create a video, you upload the video to a hosting site so that the
video is available for viewing. In a later step, you create a video component,
and then you add a link to the video that you uploaded.

You might upload your videos to YouTube, or you may use a different site such
as Amazon Web Services (AWS) Simple Storage Service (S3). Different sites have
different compression specifications. The following video compression
specifications are strongly recommended, but not required.

.. only:: Partners

  .. important::
    Videos for courses on edx.org must comply with the following specifications
    for YouTube videos.

.. list-table::
   :widths: 10 20 20
   :stub-columns: 1

   * - Output
     - **Publish to YouTube**
     - **Publish downloadable file to AWS S3**
   * - :ref:`Codec<codec_g>`
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
   * - Target :ref:`VBR<VBR>`
     - 5 mbps
     - 1 mbps
   * - Max :ref:`VBR<VBR>`
     - 7.5 mbps
     - 1.5 mbps
   * - Audio
     - :ref:`AAC<AAC>` 44.1 / 192 kbps
     - :ref:`AAC<AAC>` 44.1 / 192 kbps

.. note::
 Typically, you export at the same frame rate that was used when you created
 the media file. For example, if you create the file in a country that uses the
 :ref:`PAL<PAL>` system, you export at 25 fps instead of the :ref:`NTSC<NTSC>`
 standard of 29.97 fps.

.. include:: ../../../links/links.rst
