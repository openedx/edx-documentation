.. _Adding Course Updates and Handouts:

######################################################
Adding Course Updates and Handouts
######################################################

You add course updates and identify handouts in Studio. Learners see the
course updates and handouts on the **Home** page in your course.

.. image:: ../../../shared/images/course_info.png
 :alt: The Home page as it appears to students, with a "Course Updates
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
the course schedule, or to make other announcements. Updates are visible to
enrolled learners as soon as you post them.

Each update requires a date for identification and sorting purposes. In the
LMS, updates display on the **Home** page in reverse chronological order (most
recent at the top), based on the date associated with each update.

To add a course update, follow these steps.

#. From the **Content** menu, select **Updates**.
#. Select **New Update**.
#. Create your update in the text editor that opens.

   * Enter text for the update, using HTML tags for formatting. This editor is
     like the :ref:`raw HTML editor<The Raw HTML Editor>` that is provided for
     HTML components. The :ref:`visual editor<The Visual Editor>` is not
     provided.

     .. note:: If you copy text from another source and paste it into the text
        editor, proofread the result carefully. Some applications automatically
        change quotation marks and apostrophes from the "straight" version to
        the "smart" or "curly" version. The editor requires "straight"
        quotation marks and apostrophes.

   * Specify a date for this update. By default, today's date is already
     entered. You can change the date using the calendar tool, or by entering
     some other valid date. This date is used only for identification and
     sorting purposes and does not control when the date becomes visible to
     learners.

#. Select **Post**. Your update appears on your course's **Home** page
   immediately.


.. The following step allows installations that use the edX mobile apps to send
.. a push notification to the app when an update is added. Alison, DOC-1814,
.. June 2015

.. only:: Open_edX

    #. Optionally, choose whether to send a notification about your update to
       the edX mobile app.

      * Learners can choose to turn off notifications for individual courses or
        for all courses. The **Home** page continues to show all
        updates.
      * All updates appear on the **Home** page, even if you do not send
        notifications.




.. _Add Course Handouts:

***************************
Identify a Course Handout
***************************

You can identify previously uploaded files as handouts for your course.
Learners see a link on the **Home** page for each course handout.

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
