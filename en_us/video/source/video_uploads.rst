.. _Uploading Videos in Studio:

###########################
Uploading Videos in Studio
###########################

After a video administrator works with the edX media team to complete
preliminary set up for the entire institution, individual course teams can
begin to upload video files for their courses in Studio. This section describes
how course teams enable the video upload process in Studio, the specifications
met by successful video files, and how course teams upload the files.

* :ref:`Enable Video Upload in Studio` 

* :ref:`Specifications for Successful Video Files` 
  
* :ref:`Upload Video Files`  

.. _Enable Video Upload in Studio:

******************************
Enable Video Upload in Studio
******************************

This procedure only needs to be completed once per course, but it must be
complete before video files can be uploaded.

#. From your institution's video administrator, obtain the YouTube channel ID
   for your course.

.. is this accurate? or is it some other ID obtained in some other way?

#. Open the course in Studio. 

#. Select **Settings**, then **Advanced Settings**.

#. In the **Video Upload Credentials** field, place your cursor between the
   supplied pair of braces.

#. Type ``"course_video_upload_token": "xxxx"`` where ``xxxx`` is the channel
   ID value supplied by your video administrator.

.. accurate?

#. Click **Save Changes**. Studio reformats the name:value pair you just
   entered to indent it on a new line.
   
 .. image:: ../Images/Enable_video_upload.png
  :alt: Video Upload Credentials field with the policy key and token

You can then begin to :ref:`upload video files<Upload Video Files>`.

.. _Specifications for Successful Video Files:

***************************************************
Specifications for Successful Video Files
***************************************************

.. Specs for successful videos -- coming from Rachel, more detailed than the table so far

- sending us their files (per chart)
- single video file, in .mp4 or .mov format, for each video to include in the
  course.
- what file formats are accepted
- what file naming convention is recommended


.. following pasted from create_video.rst

====================================
Compression Specifications
====================================

When you create your video, edX recommends the following compression specs.
(Note that these are recommended but not required.)

.. list-table::
   :widths: 10 20 20
   :stub-columns: 1

   * - Output
     - **Publish to YouTube**
     - **Publish downloadable file to AWS S3**
   * - Codec
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
   * - Target VBR
     - 5 mbps
     - 1 mbps
   * - Max VBR
     - 7.5 mbps
     - 1.5 mbps
   * - Audio
     - AAC 44.1 / 192 kbps
     - AAC 44.1 / 192 kbps

.. note:: Typically you export at the same frame rate that was used when you 
 created the media file. For example, if you create the file in a country that
 uses the PAL system, you export at 25 fps instead of the NTSC standard of
 29.97 fps.

.. _Upload Video Files:

***************************
Upload Video Files 
***************************

#. Open the course in Studio. 

#. Select **Content**, then **Video Uploads**.

#. Add video files to the Video Uploads page. You can drag files to the page
   and drop them, or click **Select files** to locate the files to upload.

.. how many files can be uploaded at once
.. what kind of bandwidth/connection is recommended

Transfer of the files to the edX server begins immediately. The Video Uploads
page displays the status of each file: **Uploading**, followed by either
**Uploading completed** on success or **Uploading failed** if a problem occurs.

* For files that upload successfully, automated processing begin. The process
  results in additional formats for the video file, which are then transferred
  to mutiple hosting services (YouTube CMS and Amazon AWS), ready for students
  to access. You can monitor file statuses during autometed processign. See
  :ref:`Monitor Video Processing`.

* For files that encounter a problem, verify that the file is in .mp4 or .mov
  format and meets the other specifications for successful video processing.
  Then try uploading the file or its replacement again.

.. _Monitor Video Processing: 

================================
Monitor Video Processing
================================

After video files sucessfully reach the edX servers, the Video Uploads page
provides status updates as automated processing takes place.




on success
on failure

Course team checks Video Uploads page for status
  - on success see a unique identifying ID for each video that they uploaded AND a link to play each transcoded file on the host platform
  - on failure course team checks file for corruption and reuploads (if corrupt, need new file, if not, just reupload)



xref to the "FYI" sectionn on Process by edX to transcode


:ref:`Adding Videos to a Course`






