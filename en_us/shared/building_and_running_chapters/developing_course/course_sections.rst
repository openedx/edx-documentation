.. _Developing Course Sections:

###################################
Developing Course Sections
###################################

To develop sections in your course, you must first understand the following
topics.

.. contents:: 
  :local:
  :depth: 2

****************************
What Is a Section?
****************************

A section is the topmost category in your course. A section can represent a
time period in your course, a chapter, or another organizing principle. A
section contains one or more subsections.

********************************
Viewing Sections in the Outline
********************************

The following example shows four sections, all collapsed, in the course
outline.

.. image:: ../../../shared/building_and_running_chapters/Images/sections-outline.png
 :alt: Four sections in the outline.

******************************
The Learner View of a Section
******************************

Learners see sections in the **Courseware** tab. Learners can expand one
section at a time to see its contents. In the following example, three sections
are circled, and the third one is expanded to show its subsections.

.. image:: ../../../shared/building_and_running_chapters/Images/sections_student.png
 :alt: The learner view of the course with two sections circled.

************************************************
Sections and Visibility to Learners
************************************************

Learners cannot see any content in the section if the section's release date is
unscheduled or has not passed.

If a section's release date has passed, learners can see content in the section
if:

* The release date for the subsection that contains that content has passed.
* The unit has been published.
* The unit is not hidden from learners.

************************************************
Release Statuses of Sections
************************************************

As an course author, you control the release status of sections.  For the
content of a section to be visible to learners, the section must be released.
See the following topics for more information about the possible release
statuses of sections.

* `Unscheduled`_
* `Scheduled`_
* `Released`_
* `Released with Unpublished Changes`_
* `Staff Only Content`_

========================
Unscheduled
========================

If you do not change the :ref:`course start date<Set Start and End Dates>`
default value, ``1/1/2030 00:00:00 UTC``, when you create a new section, its
release date will appear as ``Unscheduled``. When the section release date is
unscheduled, learners cannot see any content in that section, regardless of
the publishing status of that content.

If you have modified the course start date, when you create a new section, the
default release date is the course start date.

The following example shows how an unscheduled section displays in the
outline, summarized with a gray bar.

.. image:: ../../../shared/building_and_running_chapters/Images/section-unscheduled.png
 :alt: An unscheduled section.

To make the content available to learners, you must schedule the release date.

==========
Scheduled
==========

A section that is scheduled for release on a future date will not be visible to
learners until after the release date. Regardless of the publishing status of
content within the section, the entire section will not visible to learners.

The following example shows how a section that is scheduled for release
displays in the outline, summarized with a green bar.

.. image:: ../../../shared/building_and_running_chapters/Images/section-future.png
 :alt: A section scheduled to release in the future.

The scheduled date must pass for the section to be visible to learners.

===========================
Released
===========================

A section that is released is visible to learners; however, learners see only
subsections within the section that are also released, and units that are
published.

The following example shows how a released section displays in the outline,
summarized with a blue bar.

.. image:: ../../../shared/building_and_running_chapters/Images/section-released.png
 :alt: A released section.

==================================
Released with Unpublished Changes
==================================

If you change a unit in a released section but do not publish the changes,
learners see the last published version of the modified unit.

The following example shows how a released section with unpublished changes 
displays in the outline, with a yellow bar. The section is expanded to show
the unit with unpublished changes.

.. image:: ../../../shared/building_and_running_chapters/Images/section-unpublished-changes.png
 :alt: A section with unpublished changes.

You must publish the unit for learners to see the updates.

===========================
Staff Only Content
===========================

A section can contain a unit that is hidden from learners and available to
members of the course team only. That unit is not visible to learners,
regardless of the release date of the section or subsection.

The following example shows how a section that contains a unit that is hidden
from learners displays in the outline, summarized with a black bar.

.. image:: ../../../shared/building_and_running_chapters/Images/section-hidden-unit.png
 :alt: A section with a hidden unit.


.. _Create a Section:

****************************
Create a Section
****************************

If you do not change the :ref:`course start date<Set Start and End Dates>`
default value, ``1/1/2030``, when you create a new section, its release date
will be ``Unscheduled``. 

If you have modified the course start date, when you create a new section, the
default release date is the course start date.

.. caution:: 
 If the course start date is in the past, newly created sections are
 immediately visible to learners.

To create a new section, follow these steps.

#. On the **Course Outline** page, select **New Section**. This option appears
   at both the top of the page and below the current sections in the outline.
   
   A new section appears at the end of the course content, with the section
   name selected.

#. Enter the name for the new section. A descriptive name can help learners
   locate content in the courseware. It can also help you select content when
   you analyze performance in edX Insights.

#. :ref:`Add subsections<Create a Subsection>` to the new section as needed.
   
It is recommended that you :ref:`test course content <Testing Your Course
Content>` as you create new sections.

********************************
Change a Section Name
********************************

To edit a section name, move your cursor over the section name to show the
**Edit** icon.

.. image:: ../../../shared/building_and_running_chapters/Images/section-edit-icon.png
  :alt: The Edit Section Name icon.

Select the **Edit** icon next to the section name. The name field becomes
editable. Enter the new name, and then tab or click outside of the field to
save the name.

.. _Set a Section Release Date:

********************************
Set a Section Release Date
********************************

To set the section release date, follow these steps.

#. Select the **Configure** icon in the section box.
   
   .. image:: ../../../shared/building_and_running_chapters/Images/section-settings-box.png
    :alt: The section settings icon circled.

   The **Settings** dialog box opens.

#. Enter the release date and time for the section. 

  .. note:: The time that you set, and the time that learners see, is in
   Coordinated Universal Time (UTC). You might want to verify that you have
   specified the time that you intend by using a time zone converter such as
   `Time and Date Time Zone Converter
   <http://www.timeanddate.com/worldclock/converter.html>`_

#. Select **Save**.

For more information, see :ref:`Release Dates`.

.. _Publish all Units in a Section:

********************************
Publish all Units in a Section
********************************

To publish all new and changed units in a section, select the **Publish** icon
in the box for the section.

.. image:: ../../../shared/building_and_running_chapters/Images/outline-publish-icon-section.png
 :alt: Publishing icon for a section.

.. note:: 
 The **Publish** icon only appears when there is new or changed content within
 the section.

For more information about statuses and visibility to learners, see :ref:`Unit
Publishing Status`.

.. _Hide a Section from Students:

********************************
Hide a Section from Learners
********************************

You can hide all content in a section from learners, regardless of the status
of subsections and units within the section.

For more information, see :ref:`Content Hidden from Students`.

To hide a section from learners, follow these steps.

#. Select the **Configure** icon in the section box.
   
   .. image:: ../../../shared/building_and_running_chapters/Images/section-settings-box.png
    :alt: The section settings icon circled.

   The **Settings** dialog box opens.

#. In the **Student Visibility** section, select **Hide from students**.

#. Select **Save**.

Now, none of the content in the section is visible to learners.

To make the section visible to students, repeat these steps and clear the
**Hide from students** check box.

.. warning::
 When you clear the **Hide from students** check box for a section, not all
 content in the section is necessarily made visible to learners. If you
 explicitly set a subsection or unit to be hidden from learners, it remains
 hidden from learners. Unpublished units remain unpublished, and changes to
 published units remain unpublished.

********************************
Delete a Section
********************************

When you delete a section, you delete all subsections and units within the
section.

.. warning::  
 You cannot restore course content after you delete it. To ensure you do not
 delete content you may need later, you can move any unused content to a
 section in your course that you set to never release.

To delete a section, follow these steps.

#. Select the **Delete** icon in the section that you want to delete.

  .. image:: ../../../shared/building_and_running_chapters/Images/section-delete.png
   :alt: The section with Delete icon circled.

2. When you receive the confirmation prompt, select **Yes, delete this
   section**.
