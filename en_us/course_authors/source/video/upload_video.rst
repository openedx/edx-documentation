.. _Upload a Video on edX:

#################
Uploading a Video
#################

For more information, see the following topics.

.. contents::
 :local:
 :depth: 2

.. _Uploading a Video for an edx org Course:

******************************************
Uploading a Video for an MITx Online Course
******************************************

For MITx Online courses, you use MIT's ODL Video Services (OVS) to upload your videos to the **Video Uploads** page. The MITx Online video process then creates multiple formats and sources for your videos.

.. important::
  You will not use the video upload feature on your course's **Video Uploads** page. This will result in an error and your upload attempt will fail.

.. _Automated Video Process:

=======================
Automated Video Process
=======================

So that the MITx Online video player can automatically play videos in the best format
for a learner's device and internet connection, after you upload a video for an
MITx Online course, an automated video process creates multiple formats and sources
for every video. The process also assigns a single video ID to the video that
represents all of the formats and hosting locations for the video.

* For all videos, you must obtain transcripts
  from a third party provider. You later :ref:`add the video transcripts <Add a Transcript>` when you create a video component.

.. note::
  If a step in the process does not complete successfully, the process automatically tries again multiple times. If the process does not complete successfully after multiple tries, an :ref:`error status <Video Processing Statuses>` appears in the list of videos on the **Video Uploads** page as well as within the video component.

#. The course team :ref:`uploads a video file via MIT's ODL Video Services (OVS)<Upload a video to an MITx Online Course>`.
#. The process assigns a unique video ID to the video. This video ID represents all of the files and hosting locations that the automated process creates.

.. important::
  As soon as the automated video process has assigned a video ID to the video, you can add the video to the course. However, the video is not visible in the course until the automated process is complete. The process can take up to 24 hours.
3. The process encodes video files in different formats.
#. The process uploads the video files to the hosting service.

Either before or after the course team :ref:`uploads a video file <Upload a video to an MITx Online Course>`, the course team :ref:`obtains transcripts <Obtain a Video Transcript>`
from a transcript provider. When the MITx Online video process is complete, and the
course team has obtained transcripts from the transcript provider, the course
team creates a video component and adds the video ID and transcript to the
component. For more information, see :ref:`Add a Video to a Course <Add a Video to a Course>`.

.. _Upload a video to an MITx Online Course:

====================================
Upload a Video to an MITx Online Course
====================================

To upload video files, follow these steps.

.. note::
  This process requires you to use your MIT Dropbox account. If you are unfamiliar with how to use your MIT Dropbox account, please see the `documentation <https://ist.mit.edu/dropbox>`_ on the IS&T website.

1. Load your course videos onto your MIT Dropbox account. (You will navigate to your Dropbox later from ODL Video Services to upload the videos to your course.)

.. note::
  Video types are limited to .mov and .mp4 files, and video sizes must be under 5 GB
2. Go to `ODL Video Services <https://video.odl.mit.edu/>`_. You will need to sign in with your Kerberos account.
3. Choose the collection associated with your course:

.. image:: ../../../shared/images/find_collection.png
  :width: 300
  :alt: The ODL Video Services library, with a list of collections. The collection associated with a course will have the course number listed in its title.

.. note::
  You may want to use the **Find** command on your browser to look for your course number. Also note that there are several pages of collections, and you may have to use the arrows at the bottom of the page to navigate to another page to find your collection.

4. Click **Add Videos from Dropbox**:

.. image:: ../../../shared/images/add_from_dropbox.png
 :width: 300
 :alt: On the screen with a list of videos associated with your course, click the "Add Videos from Dropbbox" link in the upper right hand corner of the page.

5. A pop-up will open showing your Dropbox account.
#. Select the videos you would like to upload by clicking the checkboxes. Please select the videos you would like to add (see #6 in the image below). Then click the **Choose** button (see #7 in the image below).

.. image:: ../../../shared/images/select_videos.png
 :width: 300
 :alt: From your Dropbox you will be able to click a check box next to any of the videos you want to upload and then click "Choose."

.. important::
  Please do not attempt to upload more than five videos at a time, as it may result in an error.

7. OVS will take a few minutes to upload and process the videos. You will see the status change inside the collection folder. You do not have to remain on the page for process to run. If the process is successful, the video will appear in **Video Uploads**, under the **Content** menu.

.. note::
  **Video uploads, even very large ones, should take less than two hours to complete.** If you have a video that is still processing after two hours, try uploading it again. If it still does not work, please report the issue to your assigned educational technologist.
  
.. note::
  Once you have uploaded a video to your OVS collection, you may delete it from your Dropbox. It will not affect the video collection.

After the automated video process is complete, the course team creates a video
component and adds the video ID to the video component. For more information,
see :ref:`Add a Video to a Course`.


.. _Monitor Video Processing:

========================
Monitor Video Processing
========================

After your video files are successfully uploaded, the video processing service
begins.

.. note::
  This service takes up to 24 hours to complete.

A list of every file that you attempt to upload to the MITx Online servers appears in
the **Previous Uploads** section of the **Video Uploads** page. The list
includes each file's status in the encoding and hosting workflow. In addition,
you can download a report of the video files that you uploaded. For more
information, see :ref:`Reporting Video Status`.

.. _Video Processing Statuses:

Video Processing Statuses
*************************

The encoding and hosting process assigns the following statuses to video files.

.. list-table::
  :widths: 25 75
  :header-rows: 1

  * - Status
    - Description
  * - **Failed**
    - Files did not complete processing successfully. If this status appears,
      follow these steps.

      #. Verify that you can play your original .mp4 or .mov file and that the
         file meets all :ref:`specifications <Video Guidelines>` for successful
         video processing.
      #. Remove the video file from the **Video Uploads** page by selecting the
         "Remove this video" icon for the video.
      #. Upload the original file again, or upload a replacement file.

      There might be failure instances where a small error message will be displayed
      under the **Failed** status. In most of the cases when the error message is displayed, there
      is a possibility of corruption in the uploaded file (either during the upload or the original
      video file itself). However, if processing fails more than one time for a file, contact MITx Online support at ``mitxonline-support@mit.edu``.

  * - **Failed Duplicate**
    - Files failed to upload because the system identified the files as
      duplicates.
  * - **In Progress**
    - Files are undergoing processing to create additional file formats, or are
      waiting for successful transfer to the host sites.
  * - **Invalid Token**
    - A configuration problem has occurred. If this status appears, contact MITx Online support at ``mitxonline-support@mit.edu``.
  * - **Ready**
    - The encoding process is complete for your files. When you click the names
      of these files, a file on one of the external host sites plays. The
      encoding process might take 24 hours after you upload a file.

      .. note::
        For all courses, the "Ready" status means that the **encoding** process
        is complete. It does not refer to the **transcript** creation process.

        For courses that have integrated transcripts through 3Play Media or
        cielo24, the video is not ready for you to add to the course, or for
        learners to view, until the "Ready" status changes to "Transcript
        Ready", signifying that the transcript creation process is complete.

        For courses that do not have integrated transcripts, you must make sure
        that each video has a transcript. For more information, see :ref:`Non
        Integrated Transcripts`.

  * - **Transcription in Progress**
    - The encoding process has completed, and video transcripts are being
      created.

      If a video has this status longer than the time that you specified for
      the **Transcript Turnaround** time, follow these steps.

      #. Verify that the file that you uploaded is in .mp4 or .mov format and
         that the file meets all :ref:`specifications <Video Guidelines>` for
         successful video processing.
      #. Remove the video file from the **Video Uploads** page by selecting the
         "Remove this video" icon for the video.
      #. Upload the original file again, or upload a replacement file.

      If this problem occurs more than one time for a file, contact MITx Online
      support at ``mitxonline-support@mit.edu``.

  * - **Transcript Ready**
    - Both the video encoding and transcript creation processes are complete.
      The video and transcripts are ready to add to your course and for
      learners to view.

  * - **Partial Failure**
    - This status appears when the transcription process has been started for more than one languages
      and either one or more processes fail. This indicate a combination of successful and unsuccessful
      transcription processes.

  * - **Transcript Failed**
    - All the transcription processes have failed.

  * - **Unknown**
    - A configuration problem has occurred. If this status appears, contact MITx Online support at ``mitxonline-support@mit.edu``.
  * - **Uploaded**
    - The file has successfully completed uploading to the MITx Online servers.
  * - **Uploading**
    - The file has not yet reached the MITx Online servers. If a video has this status
      for more than 48 hours, follow these steps.

      #. Verify that the file that you uploaded is in .mp4 or .mov format and
         that the file meets all :ref:`specifications <Video Guidelines>` for
         successful video processing.
      #. Remove the video file from the **Video Uploads** page by selecting the
         "Remove this video" icon for the video.
      #. Upload the original file again, or upload a replacement file.

      If this problem occurs more than one time for a file, contact MITx Online support at ``mitxonline-support@mit.edu``.



.. _Reporting Video Status:

Downloading the Available Encodings Report
******************************************

The Available Encodings report is a comma separated values (.csv) file that
provides detailed information about the video files that you have uploaded.
This report includes the status of the encoding and hosting process for each
video file that you have uploaded, the identifier for the video, and the URLs
for each encoding format. The MITx Online encoding and hosting process produces these
alternative formats to ensure optimal playback quality for your learners.

You can view the Available Encodings report in a spreadsheet application or
text editor.

To download the Available Encodings report, follow these steps.

#. Open the course in Studio.

#. On the **Content** menu, select **Video Uploads**.

#. On the **Video Uploads** page, click **Download available encodings (.csv)**.

#. Use a spreadsheet application or text editor to open the .csv file.

The .csv file includes the following columns.

* The file **Name**.

* The file **Duration**. If the upload process has not yet determined how long
  the file is, **Pending** appears in the **Duration** column for a video.

* The **Date Added**, which shows the date and time that you uploaded the
  video file.

* The unique, identifying **Video ID**. When you add a video component to your
  course, you supply the video ID for the file you want to add. For more
  information, see :ref:`Add a Video to a Course`.

* The **Status** of the encoding and hosting process for the file. For more
  information, see :ref:`Video Processing Statuses`.

The .csv file also includes a column for each of the formats that are the
result of the MITx Online encoding and hosting process. These columns include the URL
of a host site only after the format is successfully generated and delivered to
its destination.

* **desktop_mp4 URL**: The location of a 720p resolution video file in .mp4
  format. Learners who view course videos with mp4 players view this file.

* **desktop_webm URL**: The location of a 720p resolution video file in .webm
  format. Learners who view course videos with webm players view this file.

  .. note::
    The encoding and hosting process no longer creates .webm versions of the
    video files that you upload. Modern web browsers do not require the webm
    format. The .csv file includes the **desktop_webm URL** column to show the
    webm URLs for videos uploaded before this change. When you upload a new
    video, the column will remain empty, even after the encoding and hosting
    process is complete.

* **mobile_low URL**: The location of a 360p resolution video file. Learners
  who download and view course videos on mobile devices view this file.

.. _Delete Videos from Upload Page:

=========================================
Remove Videos from the Video Uploads Page
=========================================

A list of every file that has been uploaded to the MITx Online servers appears in the
**Previous Uploads** section of the **Video Uploads** page. You can remove
videos from the **Previous Uploads** list without affecting course content
that uses the video ID of successfully uploaded videos.

To remove a video from the **Previous Uploads** list, follow these steps.

#. Open the course in Studio.

#. On the **Content** menu, select **Video Uploads**.

#. In the **Previous Uploads** list, locate the row for the video that you
   want to remove, then select the "X" icon in the **Action** column.

#. In the confirmation dialog box that appears, select **Remove** to remove
   the video.

The selected video is removed from the **Previous Uploads** list. Course
content that uses the video ID of the removed video is not affected.
