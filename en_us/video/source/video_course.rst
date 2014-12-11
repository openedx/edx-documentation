.. _Adding Videos to a Course:

#############################
Adding Videos to a Course
#############################

After automated processing of an :ref:`uploaded video file<Uploading Videos in
Studio>` is complete, you can include it in your course. To do so, you
:ref:`copy the unique ID<Copy the edX Video ID>` assigned to an uploaded video
and then :ref:`add it to a video component<Add the edX Video ID to a Video
Component>`.

.. _Copy the edX Video ID:

************************
Copy the edX Video ID
************************
 
#. Open the course in Studio. 

#. Select **Content**, then **Video Uploads**.

#. In the **Previous Uploads** list, locate the video that you want to include in
   the course.

#. Select the value in the **Video ID** column for the video. A value appears
   in this column only after video processing is complete and successful for
   the video.

#. Right-click and select **Copy**. Be sure to select and copy the entire
   video ID value.
   
   Next, you paste this value into the **EdX Video ID** field for a video
   component. See :ref:`Add the edX Video ID to a Video Component`.

.. to come: how to download a CSV

.. _Add the edX Video ID to a Video Component:

************************************************
Add the edX Video ID to a Video Component
************************************************

This section describes the process that course teams follow in place of the
`Step 4. Create a Video Component`_ section in the *Building and Running an
edX Course* guide. This section assumes that you are familiar with the process
described in the `Developing Your Course`_ chapter.

You complete these steps in Studio.

#. From the **Content** menu select **Outline**. The **Course Outline** page
   opens.

#. Select or add a unit, and then click **Video** to add a video component. 
   
   To edit an existing video component, locate the video component window and
   then click **Edit**. The Editing: Video popup opens to the Basic tab.
   
3. In the **Component Display Name** field, enter the identifying name that you
   want students to see for this video.

#. At the top of the Editing: Video popup click **Advanced**. Additional fields
   appear below the **Component Display Name** and **Default Timed Transcript**
   fields.

#. Scroll down to the **EdX Video ID** field and paste in the ID of the video
   file that you want to play. See :ref:`Copy the edX Video ID`.

   When you supply a valid edX video ID in this field, you associate your
   video component with files on YouTube and AWS that are optimized for
   viewing with different devices and bandwidths. You do not need to add
   values to the **Default Video URL**, **Video File URLs**, or the **YouTube
   ID** fields. If those fields already have values, the edX video ID
   overrides them.

#. Set the **Video Download Allowed** field to **True** or **False** to define
   whether students can download this video.

#. Click **Save**. The referenced video appears in the video component.

To complete video component setup, you add transcript files for the video. For
information about completing a video component by adding a transcript, see the
`Step 2. Create or Obtain a Video Transcript`_ section in the *Building and
Running an edX Course* guide.

.. _Step 2. Create or Obtain a Video Transcript: http://edx.readthedocs.org/projects/edx-partner-course-staff/en/latest/creating_content/create_video.html#step-2-create-or-obtain-a-video-transcript

.. _Step 4. Create a Video Component: http://edx.readthedocs.org/projects/edx-partner-course-staff/en/latest/creating_content/create_video.html#step-4-create-a-video-component

.. _Developing Your Course: http://edx.readthedocs.org/projects/edx-partner-course-staff/en/latest/developing_course/index.html#developing-your-course-index