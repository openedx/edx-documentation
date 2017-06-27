.. _Uploading Videos in Studio:

###########################
Uploading Videos in Studio
###########################

.. note::
  **This process applies only to courses that run on the edx.org site.** For
  information about adding video files to courses that run on Edge, see
  :ref:`Step 3. Upload a Video for an edx Edge Course <Post the Video Online>`.

After a video administrator works with edX Partner Support to complete
:ref:`preliminary setup<Video Getting Started>` for the entire institution,
individual course teams can begin to upload video files for their courses in
Studio. This section describes the steps to upload the files and how to
monitor video processing at edX.

.. removed "how course teams enable the video upload process in Studio", which is commented out below in this file.

.. contents::
  :local:
  :depth: 1

The edX video processing service creates additional file formats that are
transferred to the YouTube content management system (CMS) and Amazon Web
Services (AWS). These formats and hosting locations are all associated with a
single video ID that the video processing service creates. After video
processing is complete, you make videos available to learners by adding video
components in Studio and entering the video IDs in the components.

.. _Enable Video Upload in Studio2:

.. ******************************
.. Enable Video Upload in Studio
.. ******************************

.. This procedure needs to be completed only once per course in Studio.

.. #. Work with your institution's video administrator to obtain the video
   identifier for your course. The edX partner support team defines a unique video
   identifier for each course.

.. #. Open the course in Studio.

.. #. Select **Settings**, then **Advanced Settings**.

.. #. In the **Video Upload Credentials** field, place your cursor between the
   supplied pair of braces.

.. #. Type ``"course_video_upload_token": "xxxx"`` where ``xxxx`` is the unique
   edX identifier for your course. This ID value is an 8-20 character hash
   string.

.. #. Click **Save Changes**. Studio reformats the name:value pair you just
   entered to indent it on a new line.

 .. image:: Images/Enable_video_upload.png
  :alt: Video Upload Credentials field with the course_video_upload_token
      policy key and a token value

.. #. Refresh your browser page. The Studio **Content** menu updates to include
   the **Video Uploads** option.

.. Team members can then begin to :ref:`upload video files<Upload Video Files>`.

.. _Upload Video Files:

***************************
Upload Video Files
***************************

.. note::
  Before you can upload video files, the video upload feature must be enabled
  for the course. Your video administrator coordinates this task with the edX
  partner support team. For more information, see :ref:`Create YouTube
  Channels`.

#. Open the course in Studio.

#. On the **Content** menu, select **Video Uploads**.

#. Add video files to the **Video Uploads** page. You can drag files to the
   page and drop them, or click **Select files** to locate the files to
   upload.

   A rectangular tile appears on the page for each file and shows the video
   file name, a progress bar, and the status of the file upload process. When
   the file has been successfully uploaded, the tile disappears, and an entry
   for the video appears under **Previous Uploads** with a status of
   "Uploaded".

   .. important::
    You must leave the **Video Uploads** page open in your browser until the
    upload process is complete for all files.

#. (optional) Specify a thumbnail image for the video. The thumbnail image is
   the image that learners see before the video begins to play. To do this,
   hover the cursor over **Add Thumbnail**, select an image from your computer,
   and then select **Open**.

   If a thumbnail image exists for the video and you want to change the image,
   hover the cursor over the image, and then select **Edit Thumbnail**. Select
   an image from your computer, and then select **Open**.

.. how many files can be uploaded at once
.. what kind of bandwidth/connection is recommended

After you have uploaded video files, the edX video processing service begins.
You can check the progress of a video file through the service at any time. For
more information, see :ref:`Monitor Video Processing` and :ref:`Reporting Video
Status`.

.. _Delete Videos from Upload Page:

*****************************************
Remove Videos from the Video Uploads Page
*****************************************

A list of every file that has been uploaded to the edX servers appears in the
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


.. _Monitor Video Processing:

***************************
Monitor Video Processing
***************************

After your video files are successfully uploaded, the video processing service
begins.

.. note::
  This service takes up to 24 hours to complete.

A list of every file that you attempt to upload to the edX servers appears in
the **Previous Uploads** section of the **Video Uploads** page. The list
includes each file's status in the encoding and hosting workflow. In addition,
you can download a report of the video files that you uploaded. For more
information, see :ref:`Reporting Video Status`.

.. _Video Processing Statuses:

===========================
Video Processing Statuses
===========================

The encoding and hosting process assigns the following statuses to video files.

* **Failed** files did not complete processing successfully. Verify that you
  can play your original .mp4 or .mov file and that it meets the other
  specifications for successful video processing. Then upload the file, or a
  replacement file, again. If processing fails more than once for a file,
  contact edX partner support at ``partner-support@edx.org``.

  For more information, see :ref:`Specifications for Successful Video Files`.

* **Failed Duplicate** is the status for files that failed to upload because
  the system identified the files as duplicates.

* **In Progress** files are undergoing processing to create additional file
  formats or waiting for successful transfer to the host sites.

* **Invalid Token** indicates a configuration problem. If this status appears,
  contact edX partner support at ``partner-support@edx.org``.

* **Ready** files are ready for inclusion in your course and for learners to
  view.  When you click the names of these files, a file hosted on one of the
  external host sites plays. Processing continues at video hosting sites for 24
  hours after you upload a file.

  For more information, see :ref:`Adding Videos to a Course`.

* **Unknown** indicates a configuration problem. If this status appears,
  contact edX partner support at ``partner-support@edx.org``.

* **Uploaded** files have successfully completed uploading to the edX servers.

* **Uploading** files have not yet reached the edX servers successfully. For
  files that encounter a problem, verify that the file that you uploaded is in
  .mp4 or .mov format and meets the other specifications for successful video
  processing. Then try uploading the file (or its replacement) again.

  For more information, see :ref:`Specifications for Successful Video Files`.

For more information, see :ref:`Video Encoding and Hosting Overview`.

.. _Reporting Video Status:

==========================================
Downloading the Available Encodings Report
==========================================

The Available Encodings report is a comma separated values (.csv) file that
provides detailed information about the video files that you have uploaded.
This report includes the status of the encoding and hosting process for each
video file that you have uploaded, the identifier for the video, and the URLs
for each encoding format. The edX encoding and hosting process produces these
alternative formats to ensure optimal playback quality for your learners.

You can view the Available Encodings report in a spreadsheet application or
text editor.

To download the Available Encodings report, follow these steps.

#. Open the course in Studio.

#. On the **Content** menu, select **Video Uploads**.

#. On the **Video Uploads** page, click **Download available encodings
   (.csv)**.

#. Use a spreadsheet application or text editor to open the .csv file.

The .csv file includes the following columns.

* The file **Name**.

* The file **Duration**. If the upload process has not yet determined how long
  the file is, **Pending** appears in the **Duration** column for a video.

* The **Date Added**, which shows the date and time that you uploaded the
  video file.

* The unique, identifying **Video ID**. When you add a video component to your
  course, you supply the video ID for the file you want to add. See
  :ref:`Adding Videos to a Course`.

* The **Status** of the encoding and hosting process for the file. See
  :ref:`Video Processing Statuses`.

The .csv file also includes a column for each of the formats that are the
result of the edX encoding and hosting process. These columns include the URL
of a host site only after the format is successfully generated and delivered to
its destination.

* **desktop_mp4 URL**: The AWS location of a 720p resolution video file in mp4
  format. This file is delivered to learners who do not have access to YouTube
  and view course videos with mp4 players.

* **desktop_webm URL**: The AWS location of a 720p resolution video file in
  webm format. This file is delivered to learners who do not have access to
  YouTube and view course videos with webm players.

  .. note::
    The encoding and hosting process no longer creates webm versions of the
    video files that you upload. Modern web browsers do not require the webm
    format. The .csv file includes the **desktop_webm URL** column to show the
    webm URLs for videos uploaded before this change. When you upload a new
    video, the column will remain empty, even after the encoding and hosting
    process is complete.

* **mobile_low URL**: The AWS location of a 360p resolution video file. This
  file is delivered to learners who download and view course videos on mobile
  devices.

* **youtube URL**: The YouTube location of a 1080p resolution video. By
  default, the edX video player delivers this video.





