.. _Adding Course Updates and Handouts:

######################################################
Adding Course Updates and Handouts
######################################################

This topic describes how to add course updates and handouts in Studio.

* :ref:`The Learner View of Course Updates and Handouts`
* :ref:`Add a Course Update`
* :ref:`Add Course Handouts`

.. _The Learner View of Course Updates and Handouts:

************************************************
The Learner View of Course Updates and Handouts
************************************************

Learners see the course updates and handouts on the **Course Info** tab in your
course:

.. image:: ../../../shared/building_and_running_chapters/Images/course_info.png
 :width: 600
 :alt: Image of the Course Info page

.. _Add a Course Update:

**********************
Add a Course Update
**********************

You add updates to notify learners of exams, changes in the course schedule, or
anything else of an urgent nature.

To add a course update:

#. From the **Content** menu, select **Updates**. 

#. Select **New Update**.

#. Enter your update in the HTML editor that opens.

  .. note::  
    You must enter the update in HTML. The :ref:`visual editor<The Visual
    Editor>` is not supported for course handouts.

4. Select **Save**.

.. _Add Course Handouts:

**********************
Add Course Handouts
**********************

You can add course handouts that are visible to students on the **Course Info**
page. To add an uploaded file to the course handouts, you need its URL.

.. note:: 
 You must :ref:`add files to a course<Add Files to a Course>` before
 you can add them as course handouts.

#. From the **Content** menu, select **Updates**. 

#. In the **Course Handouts** panel, select **Edit**.

#. Edit the HTML to add links to the files you uploaded. Add HTML in the
   following format.

   ``<li><a href="<Studio URL">handout link text</a></li>`` 

   For more information, see :ref:`Add a Link in an HTML Component`.

#. Select **Save**.
