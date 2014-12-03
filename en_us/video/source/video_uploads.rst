.. _Uploading Videos in Studio:

###########################
Uploading Videos in Studio
###########################

After a video administrator works with the edX media team to complete
:ref:`preliminary setup<Video Getting Started>` for the entire institution,
individual course teams can begin to upload video files for their courses in
Studio. This section describes the specifications met by successful video
files, how course teams enable the video upload process in Studio, and how
course teams upload the files.

* :ref:`Specifications for Successful Video Files` 
  
* :ref:`Enable Video Upload in Studio` 

* :ref:`Upload Video Files`  


.. move this section v to another chapter entirely if can't make MVP

.. _Specifications for Successful Video Files:

***************************************************
Specifications for Successful Video Files
***************************************************

TBD 

.. Specs for successful videos -- coming from Rachel
.. - single video file, in .mp4 or .mov format, for each video
.. - what file naming convention is recommended
.. following taken verbatim from B&R create_video.rst

Your video can contain whatever content you want. The `Producing Videos
<https:/ /edge.edx.org/courses/edX/edX101/How_to_Create_an_edX_Course/coursewar
e/93451eee15ed47b0a310c19020e8dc64/a1b0835e986b4283b0f8871d97babb9a/>`_
section of our `edX101
<https://edge.edx.org/courses/edX/edX101/How_to_Create_an_edX_Course/about>`_
course has some helpful pointers for creating good video content.


=========================
Supported Video Formats
=========================

The automated processing that takes place at edX transforms each of your
uploaded video files into several different formats. For this process to
succeed, you must upload videos in .mp4 or .mov format.

.. _Enable Video Upload in Studio:

******************************
Enable Video Upload in Studio
******************************

This procedure needs to be completed only once per course.

#. Work with your institution's video administrator to obtain the edX video
   identifier for your course. The edX media team defines a unique value for
   each course.

#. Open the course in Studio. 

#. Select **Settings**, then **Advanced Settings**.

#. In the **Video Upload Credentials** field, place your cursor between the
   supplied pair of braces.

#. Type ``"course_video_upload_token": "xxxx"`` where ``xxxx`` is the unique
   edX identifier for your course. This ID value is an 8-20 character hash
   string.

#. Click **Save Changes**. Studio reformats the name:value pair you just
   entered to indent it on a new line.
   
 .. image:: Images/Enable_video_upload.png
  :alt: Video Upload Credentials field with the policy key and token

#. Refresh your browser page. The Studio **Content** menu updates to include
   the **Video Uploads** option.

Team members can then begin to :ref:`upload video files<Upload Video Files>`.

.. _Upload Video Files:

***************************
Upload Video Files 
***************************

Before you can upload video files, this feature must be :ref:`enabled in
Studio<Enable Video Upload in Studio>`.

#. Open the course in Studio. 

#. Select **Content**, then **Video Uploads**.

#. Add video files to the Video Uploads page. You can drag files to the page
   and drop them, or click **Select files** to locate the files to upload.

   A rectangular tile appears on the page for each file. The file name, a
   progress bar, and the status of the file upload process appear in the tile.

.. how many files can be uploaded at once
.. what kind of bandwidth/connection is recommended

.. You can use your browser to navigate to other pages while upload is in progress. Return to the Video Uploads page periodically to refresh the status for each file.

* For files that upload successfully, automated processing begins. The process
  results in additional formats for the video file, which are then transferred
  to mutiple hosting services (YouTube CMS and Amazon AWS), ready for students
  to access. You can monitor file statuses during automated processing. See
  :ref:`Monitor Video Processing`.

* For files that encounter a problem, verify that the file is in .mp4 or .mov
  format and meets the other specifications for successful video processing.
  See :ref:`Specifications for Successful Video Files`. Then try uploading the
  file or its replacement again.

.. _Monitor Video Processing: 

================================
Monitor Video Processing
================================

After video files sucessfully reach the edX servers, automated processing
begins. A list of every file that has successfully uploaded to the edX servers
appears in the Previous Uploads section of the Video Uploads page.

* **In Progress** files are undergoing processing to create additional file 
  formats or waiting for successful transfer to the host sites.

* **Complete** files are ready for inclusion in your course and for students to
  view. See :ref:`Adding Videos to a Course`. When you click the names of these
  files, a file hosted on one of the external host sites plays.

* **Failed** files did not complete processing successfully. Verify that you
  can play your original .mp4 or .mov file and that it meets the other
  specifications for successful video processing. See :ref:`Specifications for
  Successful Video Files`. Upload the file, or a replacement file, again. If
  processing fails again, contact the edX media team.

.. xref to the "FYI" section on Process by edX to transcode
