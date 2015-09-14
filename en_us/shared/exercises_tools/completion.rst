.. _completion:

##################
Completion XBlock
##################

The completion XBlock allows students to mark given sections of the
courseware as done. This helps students track progress through
ungraded sections (such as reading text, watching video, or
participating in forums), and gives students a way to signal indicate
to both themselves and the instructors that they did, indeed, perform
the required activities. The block, in both finished and unfinished
states, will look like this to the students:

.. image:: ../../../shared/building_and_running_chapters/Images/done_xblock.png
  :alt: A screenshot of the Completion XBlock

We do not recommend using this block for graded activities, since
those come with their own progress indicators.

Note that this is a ***graded*** component. If used in a graded
portion of the course, it will show up as part of the student's final
grade. If used in an ungrade portion of the course, it will show up 

******************************************
Add a Completion XBlock to a Studio Course
******************************************

To add a Completion XBlock to a course:

#. Add the Completion XBlock advanced component. 

    #. On the **Settings** menu, click **Advanced Settings**.

    #. Make sure that **done** is in the field for the
    **Advanced Module List** policy key. For example, if you have no
    other advanced module, this field should be:

       ``["done"]``

    #. At the bottom of the page, click **Save Changes**.

       The page refreshes automatically. At the top of the page, you
       should see a notification that your changes have been saved.

    #. Go to the unit in the course outline where you want to add the
       Completion XBlock

#. Under **Add New Component**, select **Advanced**.
#. Select **Completion**.
#. Optionally, in the component that appears, select **Edit**. 
#. Click **Save**.

****************************************
Add a Completion XBlock to an OLX Course
****************************************

To add a completion XBlock to an OLX course, it is sufficient to add
the tag ***done*** to the OLX. However, we strongly encourage you to
also specify a ***url_name*** such that the markup would look like:

.. code-block:: xml

    <done url_name="video_3_completion"/>

If you would prefer to position the XBlock differently, the optional
***align** tag can be set to left, right, or center. This is sometimes
helpful for improving overall aesthetics when used with other XBlocks.
