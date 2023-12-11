.. _Create a Video:

##############
Create a Video
##############

Your videos can contain whatever content you want to include in the course. The
following resources can help you to create good video content that is based on
extensive experimental research in student learning.

* The `Creating Video for the edX Platform`_ course
* Richard E. Mayer's `12 Principles of Multimedia Learning`_

When you create video files, keep the following guidelines in mind.

.. contents::
 :local:
 :depth: 1

.. _Video Guidelines:

******************
General Guidelines
******************

* Videos should be as short as possible. Learners are more likely to finish
  watching videos that are no more than 5-10 minutes long.
* Each video file that you upload must be less than 5GB in size.
* Each video should follow established :ref:`file naming conventions <File
  Naming Conventions>` and :ref:`video compression specifications <Video
  Compression Specifications>`.
* For courses on MITx Online, your videos must use the .mp4 or .mov format.


.. _File Naming Conventions:

***********************
File Naming Conventions
***********************

To facilitate identifying and tracking video files, we strongly recommend that
organizations define and use a naming convention for all video files in all
courses. At a minimum, your naming convention should include these elements.

* A course identifier.
* The year of the initial course run.
* A revision or version number.

For example, you might use the following naming convention.

::

  {course number}_{year}_{section}_{subsection}_{unit}_{version}.{type}

This convention might yield the following file name.

::

  SPU27_2015_S1_SS3_U4_v2.mp4

Additionally, when you name your video files, we recommend that you follow
these guidelines.

* Make sure that each video file in your organization has a unique name.
* Include only alphanumeric characters and underscores in video file names.
* Make sure that the video file name contains no special characters, such as ç,
  å, or ó.
* Do not use periods except for the period before the file name extension (for
  example, .mp4).

.. _Video Compression Specifications:

********************************
Video Compression Specifications
********************************
For courses on MITx Online, all videos must comply with the following
specifications.

.. list-table::
   :widths: 10 20
   :stub-columns: 1

   * - :ref:`Codec<codec_g>`
     - H.264 .mp4
   * - Resolution & Frame Rate
     - 1920x1080, progressive, 29.97 fps

       .. note::
         Typically, you export at the same frame rate that was used when you
         created the media file. For example, if you create the file in a
         country that uses the :ref:`PAL<PAL>` system, you export at 25 fps
         instead of the :ref:`NTSC<NTSC>` standard of 29.97 fps.

   * - Aspect
     - 1.0
   * - Bit Rate
     - VBR, 2 pass
   * - Target :ref:`VBR<VBR>`
     - 5 mbps
   * - Max :ref:`VBR<VBR>`
     - 6 mbps
   * - Audio
     - :ref:`AAC<AAC>` 44.1 / 192 kbps


.. include:: ../../../../links/links.rst
