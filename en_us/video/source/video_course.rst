.. _Adding Videos to a Course:

#############################
Adding Videos to a Course
#############################

After automated processing of an :ref:`uploaded video file<Uploading Videos in
Studio>` is complete, you can include it in your course. To do so, you
:ref:`copy the unique ID<Copy the edX Video ID>` assigned to an uploaded video
and :ref:`add it to a video component<Add the edX Video ID to a Video
Component>`.

.. _Copy the edX Video ID:

************************
Copy the edX Video ID
************************
 
#. Open the course in Studio. 

#. Select **Content**, then **Video Uploads**.

#. In the Previous Uploads list, locate the video that you want to include in
   the course.

#. Select the value in the **Video ID** column for the video. A value appears
   in this column only after video processing is complete and successful for
   the video.

#. Right-click and select **Copy**. You can then paste this value in to the
   **EdX Video ID** field for a video component.

.. to come: how to download a CSV

.. _Add the edX Video ID to a Video Component:

************************************************
Add the edX Video ID to a Video Component
************************************************

This section describes the process that you follow in place of the `Step 4.
Create a Video Component`_ section in the *Building and Running an edX Course*
guide. This section assumes that you are familiar with the process described in
the `Developing Your Course`_ chapter.

You complete these steps in Studio on the Course Outline page: from the
**Content** menu select **Outline**.

#. Select or add a unit, and then click **Video** to add a video component. To
   edit an existing video component, locate the video component window and then
   click **Edit**. The Editing: Video popup opens to the Basic tab.
   
#. In the **Component Display Name** field, enter the identifying name that you
   want students to see for this video.

#. Delete the value in the **Default Video URL** field. This field must be
   blank.

#. To supply captions for the video, you select one of the options for the
   **Default Timed Transcript** field.

.. Rachel is that ^ correct, or should they always use the Upload New Transcript option (and not the Import YouTube Transcript option)?

   Captions are required for all videos. See `Step 2. Create or Obtain a Video
   Transcript`_ in the *Building and Running an edX Course* guide.

5. At the top of the Editing: Video popup click **Advanced**. Additional fields
   appear below the **Component Display Name** and **Default Timed Transcript**
   fields.

#. Complete the **Download Transcript Allowed** and **Downloadable Transcript
   URL** fields.

#. In the **EdX Video ID** field, paste the ID of the video file that you want
   to play. See :ref:`Copy the edX Video ID`.
   
#. Complete the **Show Transcript** and **Transcript Languages** fields.

#. Optionally, in the **Upload Handout** field include an accompanying file in
   any format.

#. Set the **Video Download Allowed** field to **True** or **False** to define
   whether students can download this video.

.. Rachel is that ^ correct? should they always select True?

11. Do not supply any values for the **Video File URLs** field. This field must
    be blank.

#. Optionally, supply a **Video Start Time** or a **Video Stop Time** if you
   do not want the entire video to play.

#. Do not supply any values for the **YouTube ID** speed fields. These fields
   must remain blank.

#. Click **Save**.


.. _Step 2. Create or Obtain a Video Transcript: http://edx.readthedocs.org/projects/edx-partner-course-staff/en/latest/creating_content/create_video.html#step-2-create-or-obtain-a-video-transcript


.. _Step 4. Create a Video Component: http://edx.readthedocs.org/projects/edx-partner-course-staff/en/latest/creating_content/create_video.html#step-4-create-a-video-component

.. _Developing Your Course: http://edx.readthedocs.org/projects/edx-partner-course-staff/en/latest/developing_course/index.html#developing-your-course-index
