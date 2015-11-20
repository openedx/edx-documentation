.. _Adding Course Updates and Handouts:

######################################################
Adding Course Updates and Handouts
######################################################

You add course updates and identify handouts in Studio. Learners see the
course updates and handouts on the **Course Info** page in your course.

.. image:: ../../../shared/Images/course_info.png
 :alt: The Course Info page as it appears to students, with a "Course Updates
       & News" section containing a dated post and a "Course Handouts" frame
       with a list of links.

.. contents:: Section Contents
   :local:
   :depth: 1

.. _Add a Course Update:

**********************
Add a Course Update
**********************

You add updates to notify learners of upcoming exams or deadlines, changes in
the course schedule, or to make other announcements.

To add a course update, follow these steps.

#. From the **Content** menu, select **Updates**.
#. Select **New Update**.
#. Enter your update in the HTML editor that opens.

  * You must use HTML to format your update. The :ref:`visual editor<The Visual
    Editor>` is not provided.
  * If you change the supplied date, the new date appears above the update on
    the **Course Info** page. However, the update is visible to all enrolled
    learners as soon as you post it.

.. note::
  If you copy text from another source and paste it into the HTML editor, be
  sure to proofread the result carefully. Some applications automatically
  change quotation marks and apostrophes from the "straight" version to the
  "smart" version. The HTML editor requires "straight" quotation marks and
  apostrophes.

.. The following step allows installations that use the edX mobile apps to send a push notification to the app when an update is added.
.. Alison, DOC-1814, June 2015

.. only:: Open_edX

    #. Optionally, choose whether to send a notification about your update to
       the edX mobile app.

      * Learners can choose to turn off notifications for individual courses or
        for all courses. The **Course Info** page continues to show all
        updates.
      * All updates appear on the **Course Info** page, even if you do not send
        notifications.

#. Select **Post**. Your update appears on your course's **Course Info** page
   immediately.

.. _Add Course Handouts:

***************************
Identify a Course Handout
***************************

You can identify previously uploaded files as handouts for your course.
Learners see a link on the **Course Info** page for each course handout.

Before you identify a course handout, you :ref:`add the file<Add Files to a
Course>` to your course and copy its Studio URL. You can open the Studio
**Files & Uploads** page in another browser window to make this process
easier.

To identify a course handout, follow these steps.

#. From the **Content** menu, select **Updates**.
#. In the **Course Handouts** panel, select **Edit**.
#. In the editor that opens, use HTML formatting to add a link to the
   previously uploaded file. An example follows.

   .. code-block:: html

     <p><a href="/static/Syllabus_Fall2016.pdf" target="_blank">Syllabus</a></p>
     <p><a href="/static/Glossary_v3.pdf" target="_blank">Glossary</a></p>

#. Select **Save**.
