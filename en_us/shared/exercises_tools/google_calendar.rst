.. _Google Calendar Tool:

#####################
Google Calendar Tool
#####################

This chapter describes how to embed Google calendars in your course. For more
information, see any of the following topics.

* `Overview`_

* `Embedding a Google Calendar in Your Course`_

  * `Enable Google Calendars in the Course`_

    * `Enable Google Calendars in edX Studio`_
    * `Enable Google Calendars in OLX`_

  * `Make the Google Calendar Public and Obtain Its ID`_
  * `Add a Google Calendar in the Courseware`_

    * `Add a Google Calendar Component in edX Studio`_
    * `Add a Google Calendar XBlock in OLX`_

* `Editing Google Calendars`_

You can also use Google Drive files, such as documents, spreadsheets, and
images, in your course. For more information, see :ref:`Google Drive Files
Tool`.

*********
Overview 
*********

You can embed a Google calendar in your course so that students see the calendar
in the courseware. You can use a  Google calendar to share quiz dates, office
hours, or other schedules of interest to students. For example:

.. image:: ../../../shared/building_and_running_chapters/Images/google-calendar.png
  :alt: A Google calendar in courseware

*******************************************
Embedding a Google Calendar in Your Course
*******************************************

Embedding a Google calendar in your course has three steps.

#. :ref:`Enable Google calendars in your course<Enable Google Calendars in the
   Course>` by using :ref:`Studio<Enable Google Calendars in edX Studio>` or
   :ref:`OLX<Enable Google Calendars in OLX>`.

#. :ref:`Make the Google calendar public and obtain its ID<Make the Google
   Calendar Public and Obtain Its ID>`.

#. :ref:`Add the Google calendar to your course<Add a Google Calendar in the
   Courseware>` by using :ref:`Studio<Add a Google Calendar Component in edX
   Studio>` or :ref:`OLX<Add a Google Calendar XBlock in OLX>`.


.. _Enable Google Calendars in the Course:

======================================
Enable Google Calendars in the Course
======================================

You can enable Google Calendars in the course by using either Studio or OLX.

.. _Enable Google Calendars in edX Studio:

Enable Google Calendars in edX Studio
**********************************************

To enable Google Calendars in your course:

#. From the **Settings** menu, select **Advanced Settings**.
#. In the **Advanced Module List** field, place your cursor between the braces,
   and then type ``"google-calendar"``. If you see other values in this field,
   add a comma after the closing quotation mark for the last value, and then
   type ``"google-calendar"``. For example:
   
   .. image:: ../../../shared/building_and_running_chapters/Images/google-advanced-setting.png
    :alt: Advanced modules setting for Google Calendars

#. At the bottom of the page, select **Save Changes**.

.. _Enable Google Calendars in OLX:

Enable Google Calendars in OLX
**********************************************

To enable Google Calendars in your course, you edit the XML file that defines
the course structure. You locate the ``course`` element's ``advanced-modules``
attribute, and add the string ``google-calendar`` to it.

For example, the following XML code enables Google Calendars in a course. It
also enables Google Drive files.

.. code-block:: xml

  <course advanced_modules="[&quot;google-document&quot;, 
      &quot;google-calendar&quot;]" display_name="Sample Course" 
      start="2014-01-01T00:00:00Z">
      ...
  </course>

For more information, see `The Courseware Structure`_.

.. _Make the Google Calendar Public and Obtain Its ID:

===================================================
Make the Google Calendar Public and Obtain Its ID
===================================================

Before you can add a Google calendar to your course, you must make the calendar
public and obtain its ID.

.. important:: 
 The tasks described in this section rely on the use of third-party software.
 Because the software is subject to change by its owner, the steps provided
 here are intended as guidelines and not as an exact procedure.

Make the Google Calendar Public
**********************************************


#. Open the Google calendar.
#. From the **Settings** menu, select **Settings**.
#. Select the **Calendars** tab.
   
   You might have multiple calendars on the **Calendars** tab. Find the
   calendar that you want to share in your courseware.

#. In the row for the calendar to share, in the **Sharing** column, select
   **Edit Settings**.
#. Click the **Share this Calendar** tab, and then select **Make this calendar
   public**.
   
  .. image:: ../../../shared/building_and_running_chapters/Images/google-calendar-settings.png
   :alt: Google calendar settings

7. Select **Save**.
   
   The **Calendar Settings** page closes, and you return to the **Calendars**
   tab. You continue by :ref:`obtaining the Google calendar's ID<Obtain the
   Google Calendar ID>`.

.. _Obtain the Google Calendar ID:

Obtain the Google Calendar ID
**********************************************

#. On the **Calendars** tab, click the name of the calendar.
#. Select the **Calendar Details** tab.
#. Next to the **Calendar Address** label, look to the right of the three
   colored **XML**, **ICAL**, and **HTML** buttons. In parentheses, you can see
   the calendar ID.

   .. image:: ../../../shared/building_and_running_chapters/Images/google-calendar-address.png
     :width: 600
     :alt: Image of Calendar Address label with the calendar ID to the right

   The calendar ID resembles the following text.

   ``abcdefghijklmnop1234567890@group.calendar.google.com``

   Select and copy the calendar ID. You use this value to configure the Google
   calendar component in your course.

.. _Add a Google Calendar in the Courseware:

========================================
Add a Google Calendar in the Courseware
========================================

To add a Google calendar in the courseware, you create aan advanced component
in Studio or create a Google calendar XBlock in OLX.

.. _Add a Google Calendar Component in edX Studio:

Add a Google Calendar Component in edX Studio
**********************************************

Make sure that you :ref:`enable Google Calendars in your course<Enable Google
Calendars in edX Studio>` before you add the Google Calendar component.

To add a Google calendar component:

#. On the **Course Outline** page, open the unit where you want to add the
   Google calendar component.

#. Under **Add New Component** click **Advanced**, and then select **Google
   Calendar**.
   
   The new component is added to the unit, with the default edX Google calendar
   embedded.

   .. image:: ../../../shared/building_and_running_chapters/Images/google-calendar-studio.png
    :width: 600
    :alt: The Google calendar component in a unit page

#. In the new component, select **Edit**.
   
   .. image:: ../../../shared/building_and_running_chapters/Images/google-calendar-edit.png
    :width: 600
    :alt: The Google calendar editor

#. In the **Display Name** field, type the name for the component.

#. In the **Public Calendar ID** field, paste the calendar ID you copied in the
   `Obtain the Google Calendar ID`_ task.

#. For the **Default View** field, select **Month**, **Week**, or **Agenda**.
   
   This is the initial view that your students have of the calendar. Each
   student can change his or her view.

#. Select **Save**.

You can then :ref:`Preview Course Content` to see how the unit with the Google
calendar will appear to students.


.. _Add a Google Calendar XBlock in OLX:

Add a Google Calendar XBlock in OLX
**********************************************

To add a Google calendar XBlock in OLX, create the ``google-calendar`` element.
You can embed this element in the ``vertical`` element, or you can embed this
element in its own file that is referenced within the vertical. For more
information, see `The Courseware Structure`_.

For example:

.. code-block:: xml

  <google-calendar url_name="4115e717366045eaae7764b2e1f25e4c" 
    calendar_id="abcdefghijklmnop1234567890@group.calendar.google.com" 
    default_view="1" display_name="Class Schedule"/>

The value of the ``calendar_id`` attribute is the calendar ID that you copied
in the `Obtain the Google Calendar ID`_ task.

.. note:: 
  The edX Learning Management System sets the height and width values for
  Google Calendars. If you add these attributes, the LMS overrides your
  changes.

**************************
Editing Google Calendars
**************************

When you make changes to a Google calendar that is embedded in your course,
students see the updates immediately. You make changes to calendars with the
Google user interface. You do not need to edit the Google Calendar component.


.. _The Courseware Structure: http://edx.readthedocs.org/projects/edx-open-learning-xml/en/latest/organizing-course/course-xml-file.html