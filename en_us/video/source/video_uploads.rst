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

.. _Specifications for Successful Video Files:

***************************************************
Specifications for Successful Video Files
***************************************************

Your videos can contain whatever content you want to include in the course.
The `Creating Videos`_ section of `edX101 Overview of Creating an edX Course`_
has some helpful pointers for creating good video content.

=========================
Supported Video Formats
=========================

The automated processing that takes place at edX transforms each of your
uploaded video files into several different formats. For this process to
succeed, you must upload videos in **.mp4** or **.mov** format.

===========================
Compression Specifications
===========================

For best results, your video files should have these compression specifications.

.. list-table::
   :widths: 40 40
   :stub-columns: 1

   * - Output
     - Transfer to edX Studio
   * - Codec
     - H.264 .mp4
   * - Resolution & Frame Rate (see note)
     - 1920x1080, progressive, 29.97 fps
   * - Aspect
     - 1.0
   * - Bit Rate
     - VBR, 2 pass
   * - Target VBR
     - 5 mbps
   * - Max VBR
     - 7.5 mbps
   * - Audio
     - AAC 44.1 / 192 kbps

.. note:: Typically you export at the same frame rate that was used when you 
 created the media file. For example, if you create the file in a country that
 uses the PAL system, you export at 25 fps instead of the NTSC standard of
 29.97 fps.

.. _Enable Video Upload in Studio:

******************************
Enable Video Upload in Studio
******************************

This procedure needs to be completed only once per course in Studio.

#. Work with your institution's video administrator to obtain the edX video
   identifier for your course. The edX media team defines a unique video
   identifier for each course.

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
  :alt: Video Upload Credentials field with the course_video_upload_token
      policy key and a token value

#. Refresh your browser page. The Studio **Content** menu updates to include
   the **Video Uploads** option.

Team members can then begin to :ref:`upload video files<Upload Video Files>`.

.. _Upload Video Files:

***************************
Upload Video Files 
***************************

Before you upload video files, you must :ref:`enable this feature in
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
  results in additional video file formats, which are then transferred
  to multiple hosting services (YouTube CMS and Amazon AWS), ready for students
  to access. You can monitor file statuses during automated processing. See
  :ref:`Monitor Video Processing`.

  .. note:: Automated processing takes 24 hours to complete.

* For files that encounter a problem, verify that the file is in .mp4 or .mov
  format and meets the other specifications for successful video processing.
  See :ref:`Specifications for Successful Video Files`. Then try uploading the
  file (or its replacement) again. 

.. _Monitor Video Processing: 

================================
Monitor Video Processing
================================

After video files successfully reach the edX servers, automated processing
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
  processing fails more than once for a file, contact the edX media team at
  ``media@edx.org``.


.. xref to the "FYI" section on Process by edX to transcode

.. _Creating Videos: https://courses.edx.org/courses/edX/edX101/2014/courseware/c2a1714627a945afaceabdfb651088cf/9dd6e5fdf64b49a89feac208ab544760/

.. _edX101 Overview of Creating an edX Course: https://www.edx.org/node/5496#.VH8p51fF_FA
