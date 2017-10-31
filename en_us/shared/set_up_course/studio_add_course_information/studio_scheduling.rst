.. _Set Schedule and Pacing:

#################################################
Set the Course Run Schedule and Pacing in Studio
#################################################

.. only:: Partners

  .. note::
    This information applies to Edge courses. If your course will run on
    edx.org, see :ref:`Pub Course Run Creation`.

After you determine the start and end dates for a course run, and whether you
want your course run to be self-paced or instructor-paced, you specify these
settings on the **Schedule & Details** page in Studio.

For more information about determining how to schedule your course, see
:ref:`Scheduling Your Course`.

.. _Set Start and End Dates:

*******************************************
Set Start and End Dates and Times in Studio
*******************************************

.. only:: Partners

 To set dates and times for the course in Studio, follow these steps.

.. only:: Open_edX

 To set dates and times for the course and for course enrollment in Studio,
 follow these steps.

.. note::
 EdX recommends that you verify all important dates in Studio one week before
 you plan to start the course.

#. On the **Settings** menu, select **Schedule & Details**.

#. In the **Course Schedule** section, replace the placeholder dates and times
   with your own information.

   When you make changes on this page, a panel with options to save or cancel
   your work appears.

#. Select **Save Changes**.

.. note::
  The times that you set are in Coordinated Universal Time (UTC). You might
  want to verify that you have specified the times that you intend by using a
  time zone converter such as `Time and Date Time Zone Converter`_.

.. _Advertise a Different Start Date:

====================================
Advertise a Different Start Date
====================================

You can advertise a start date for your course that is different from the
course start date you set in the **Schedule & Details** page. You might want
to do this if the exact start date is uncertain.

You can enter a specific date or a description. For example, you could
advertise the start date as either "15 Oct 2016" or "Anytime, self-paced".

To set an advertised start date in Studio, follow these steps.

#. On the **Settings** menu, select **Advanced Settings**.

#. Locate the **Course Advertised Start Date** field. The default value is
   ``null``.

#. Enter the start date that you want learners to see for your course in
   MM/DD/YYYY format.

   A date value entered in MM/DD/YYYY format appears to learners in DD Mon YYYY
   format. For example, 10/15/2016 appears as 15 Oct 2016.

#. Add quotation marks (``" "``) before and after the start date value. An
   example follows.

   ::

     "Anytime, self-paced"

#. Select **Save Changes**.

   A message lets you know whether your changes were saved successfully.

.. note::
 If you do not change the default course start date (01/01/2030), and the
 **Course Advertised Start Date** policy value is ``null``, no start date
 appears for the course. Learners just see that the course has not yet started.

.. _Set Course Pacing:

************************************
Set Pacing for Your Course in Studio
************************************

.. only:: Open_edX

    Before you can use this feature to set up a self-paced course, it must be
    enabled using the Open edX Django admin panel. Follow these steps, or
    contact your Open edX site administrator for assistance.

    #. Log in to your Open edX Django Admin panel.
    #. In the **Self_Paced** section, locate **Self paced configurations**, and
       then select **Add**.
    #. Select the **Enabled** and **Enable course home page improvements**
       checkboxes.
    #. Select **Save**.

To set the pacing for your course, follow these steps.

.. note::
 You cannot change the course pacing after the course start date has passed.

#. On the **Settings** menu, select **Schedule & Details**.
#. Scroll down to the **Course Pacing** section.
#. Under **Course Pacing**, select either **Instructor-Paced** or
   **Self-Paced**.
#. Select **Save Changes**.


.. include:: ../../../../links/links.rst
