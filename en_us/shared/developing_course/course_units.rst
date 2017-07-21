.. _Developing Course Units:

###################################
Developing Course Units
###################################

To work with units in the course outline and develop your course, you need to
understand the following concepts and complete the following tasks.

.. contents::
   :depth: 1
   :local:

You add content to units with :ref:`course components<Developing Course
Components>`.

.. _What is a Unit?:

****************************
What Is a Unit?
****************************

A unit is a part of a :ref:`subsection<Developing Course Subsections>` that
learners view as a single page.

A unit contains one or more :ref:`components<Developing Course Components>`,
such as text with :ref:`HTML<Working with HTML Components>` markup,
:ref:`problems<Working with Problem Components>`, a :ref:`discussion<Working
with Discussion Components>`, or a
:ref:`video<Working with Video Components>`.

****************************
Viewing Units in the Outline
****************************

To view units in the outline, you :ref:`expand<Navigating the Course Outline>`
the parent section and subsection.

.. image:: ../../../shared/images/outline-callouts.png
 :alt: An outline with numbered indicators for the section, subsection, and
  units.
 :width: 400

#. The section.
#. The subsection.
#. The units in the subsection.

****************************
Viewing the Unit Page
****************************

When you select a unit name in the outline, the **Unit** page opens.

The following example shows a unit page with two components, with circles and
text to show different areas and controls in the page.

.. image:: ../../../shared/images/unit-page.png
 :alt: The Unit page with numbered indicators.
 :width: 600

#. A component in the unit.
#. Options for testing the unit.
#. Status panel for the unit.
#. Location of the unit in the course outline.

****************************
Viewing Units as a Learner
****************************

To a learner using the edX learning management system (LMS), each unit in the
subsection is represented by an icon in the unit navigation bar at the top of
the **Course** page. The current unit is indicated with bold underlining in the
unit navigation bar. The components in the current unit appear below the unit
navigation bar.

The following image shows a subsection in the LMS that contains several units.

.. image:: ../../../shared/images/Units_LMS.png
 :alt: A unit in the LMS, with all of the unit icons in the unit navigation bar
  indicated.
 :width: 500

.. _The Unit Workflow:

******************
The Unit Workflow
******************

When you have set up the :ref:`section<Developing Course Sections>` and
:ref:`subsection<Developing Course Subsections>` in the course outline, you
then work with units.

The typical workflow includes these steps.

#. :ref:`Create a unit<Create a Unit>`.
#. :ref:`Add components to the unit<Add a Component>`.
#. :ref:`Modify components in the unit<Developing Course Components>`.

.. The following image could use some re-work to make the contrast greater.

.. image:: ../../../shared/images/workflow-create-unit.png
 :alt: Diagram of the unit development workflow.
 :width: 800

You :ref:`publish the unit<Publish a Unit>` after you add all of its
components. If you make additional modifications, you must publish the unit
again for the changes to be visible to learners.

As you work through these steps, the publishing status of the unit changes.
The publishing status controls the content available to learners, along with
:ref:`release dates<Release Dates>` (in an instructor-paced course). See the
next section for more information.

.. note:: Release dates apply only to instructor-paced courses. For more
  information about instructor-paced and self-paced courses, see :ref:`Setting
  Course Pacing`.

.. _Unit States and Visibility to Students:

*************************************************
Unit Publishing Status and Visibility to Learners
*************************************************

The following information summarizes whether or not learners can see a unit.

* Learners never see a unit with the publishing status `Draft (Never
  Published)`_.

* Learners never see a unit with the publishing status `Visible to Staff
  Only`_. For more information, see :ref:`Hide a Unit from Students`.

* Learners do not see a unit with the publishing status `Published Not Yet
  Released`_ until the :ref:`release date <Release Dates>` (in an
  instructor-paced course). On the release date, the status changes to
  `Published and Live`_.

* If the publishing status is `Published and Live`_, learners see the current
  version of the unit.

* If the publishing status is `Draft (Unpublished Changes)`_, learners see the
  last published version of the unit if the :ref:`release dates<Release Dates>`
  for the containing section and subsection have passed.

* If you used :ref:`access settings<Access Settings>` to specify that a unit
  is available only to specific groups of learners (such as content groups
  associated with particular cohorts, or enrollment track groups), only those
  learners who are in groups to which you have given access can see the unit
  after it is published and live.

For more information, see :ref:`Controlling Content Visibility`. For
information about testing content, see :ref:`Testing Your Course Content`.


.. _Unit Publishing Status:

************************************************
Unit Publishing Statuses
************************************************

As a course author, you work with units that have the following statuses.

.. contents::
   :depth: 1
   :local:


.. _Draft (Never Published):

========================
Draft (Never Published)
========================

When you create a new unit and add components to it, the unit's publishing
status is **Draft (Never Published)**, as shown in the status panel.

.. image:: ../../../shared/images/unit-never-published.png
 :alt: Status panel of a unit that has never been published, with "Draft (Never
     published)" at the top.
 :width: 200

.. note:: The **Release** section applies only to instructor-paced courses. It
 does not appear for units in self-paced courses. For more information about
 instructor-paced and self-paced courses, see :ref:`Setting Course Pacing`.

In Studio, you see the draft content as you develop the unit. Though you do not
see the unit in the LMS, you can :ref:`preview the unit<Preview Unpublished
Content>`.

Learners never see a unit with this status, even after the release date (in an
instructor-paced course). You must :ref:`publish the unit<Publish a Unit>` for
it to be included in the LMS.

.. _Published and Live:

====================
Published and Live
====================

You published the unit and have not modified it. The release dates for the
section and subsection have passed (in an instructor-paced course). You, and
enrolled learners, see the current version of the unit.

.. image:: ../../../shared/images/unit-published.png
 :alt: Status panel of a unit that is published, with "Published and Live" at
     the top.
 :width: 200

The **Release** section applies only to instructor-paced courses. It does not
appear for units in self-paced courses. For more information, see :ref:`Setting
Course Pacing`.

.. _Published Not Yet Released:

====================================
Published (not yet released)
====================================

You published the unit, but the release date is still in the future. Learners
cannot see this unit until the release date passes.

.. image:: ../../../shared/images/unit-published_unreleased.png
 :alt: Status panel of a unit that is published but not released, with
     "Published (not yet released)" at the top.
 :width: 200

This status applies only to instructor-paced courses. It does not apply to
self-paced courses.

.. _Draft (Unpublished Changes):

===========================
Draft (Unpublished changes)
===========================

When you edit a published unit, whether or not it is released, the unit's
publishing status changes to **Draft (Unpublished Changes)**, as shown in the
status panel.

.. image:: ../../../shared/images/unit-pending-changes.png
 :alt: Status panel of a unit that has pending changes, with "Draft
     (Unpublished Changes)" at the top.
 :width: 200

The **Release** section applies only to instructor-paced courses. It does not
appear for units in self-paced courses.

In Studio, you see the draft content as you develop the unit. You can
:ref:`preview the changes to a unit<Preview Unpublished Content>` to test how
your changes will appear to learners after you publish the unit.

If the release date has passed in an instructor-paced course, learners see the
last published version of the unit. If the release date is in the future,
learners cannot see your content. You must :ref:`publish the unit<Publish a
Unit>` for learners to see your changes.

.. _Visible to Staff Only:

===========================
Visible to Staff Only
===========================

When you :ref:`hide a unit from learners<Hide a Unit from Students>`, the
unit's publishing status changes to **Visible to Staff Only**.

The publishing status of a unit also changes to **Visible to Staff Only** if
you hide the parent :ref:`section<Hide a Section from Students>` or
:ref:`subsection<Hide a Subsection from Students>` from learners.

Learners never see a unit with this status, even if it has been published and
the release date has passed (in an instructor-paced course).

.. image:: ../../../shared/images/unit-hide.png
 :alt: Status panel of a unit that is hidden from learners, with an icon and
     "Hide from learners" text visible.
 :width: 200

The **Release** section applies only to instructor-paced courses. It does not
appear for units in self-paced courses.

.. _Create a Unit:

****************************
Create a Unit
****************************

You can create a unit from the outline or create a unit in the same subsection
from the unit page.

To create a unit from the outline, follow these steps.

#. In the outline, expand the subsection in which you want to create a new
   unit.
#. Select **New Unit** at the bottom of the expanded subsection. A new
   page opens for you to add components to the unit.
#. On the unit page, the unit name is selected. Supply an identifying name. A
   descriptive name can help learners locate content in the course. It can
   also help you select content when you analyze performance in edX Insights.
#. :ref:`Add components<Add a Component>` to the new unit as needed.

To create a unit from a unit page, follow these steps.

#. In the **Unit Location** panel, select **New Unit**.

   .. image:: ../../../shared/images/unit_location.png
    :alt: The Unit Location panel in the Unit page.
    :width: 200

   The unit page for the new unit opens automatically.

#. On the unit page, the unit name is selected. Supply an identifying name. A
   descriptive name can help learners locate content in the course. It can
   also help you select content when you analyze performance in edX Insights.

#. :ref:`Add components<Add a Component>` to the new unit as needed.

You must then :ref:`publish the unit<Publish a Unit>` to make it visible to
learners.


.. _Edit a Unit:

**************
Edit a Unit
**************

You can edit a unit in the following ways.

* `Edit the unit name`_
* :ref:`Add components to units<Developing Course Components>`
* `Reorganize Components in Units`_

When you make any of these changes, if you previously published the unit, the
state changes to `Draft (Unpublished Changes)`_. You must then :ref:`publish
the unit<Publish a Unit>` to make your edits visible to learners.

If you are designing your course to :ref:`offer different content<Offering
Differentiated Content>` to different groups of learners, you can also
:ref:`Set access restrictions for the unit<Set Access Restrictions For a
Unit>` to specify which learner groups a unit is available to.


==============================
Edit the Unit Name
==============================

To edit a unit name, on the unit page in Studio, select **Edit** next to the
name.

.. image:: ../../../shared/images/unit-edit-icon.png
  :alt: The Edit icon for the unit name with the mouseover help showing.
  :width: 300

The name field becomes editable. Enter the new name, and then tab or click
outside of the field to save the name.


==============================
Reorganize Components in Units
==============================

You can reorganize components within a unit by dragging and dropping them to
new locations.

To change the location of a component, move your mouse pointer over the **Drag
to reorder** handle on the component toolbar. The pointer changes to a four-
headed arrow. You can then drag the component to the location that you want.

In the image that follows, the handle for the discussion component is selected.

.. image:: ../../../shared/images/unit-drag-selected.png
  :alt: A discussion component selected so that it can be dragged.
  :width: 600

A blue outline indicates where the component will land when you release the
mouse button. For example, in the image below, the discussion component is
being moved to the top of the unit.

.. image:: ../../../shared/images/unit-drag-moved.png
 :alt: A component being dragged to a new location.
  :width: 600


.. _Set Access Restrictions For a Unit:

***********************************
Set Access Restrictions For a Unit
***********************************

If you have more than one enrollment track in your course, or if you have
enabled cohorts, you can limit a unit's availability to specific groups of
learners. For information about offering different content to different learner
groups, see :ref:`Offering Differentiated Content`.

.. note:: A unit's group access settings are inherited by components in the
   unit. If you set additional group access restrictions for a component, make
   sure the component access settings do not contradict the unit access
   settings. For example, you cannot give Group A of learners access to a
   component if Group A does not have access to the unit that contains the
   component.

Tp specify a unit's access settings, follow these steps.

#. In Studio, select **Content**, and then select **Outline**.

#. For the unit that you want to restrict access to, select the **Configure**
   icon in the unit's toolbar.

   .. image:: ../../../shared/images/unit-configure-icon.png
    :alt: The configure icon in a unit's toolbar in the Studio course outline.
    :width: 500

   You can also access the **Restrict access to** option from the gear icon
   next to a unit's name on a unit page in Studio.


   .. image:: ../../../shared/images/unit-access-settings-gear-icon.png
    :alt: The gear icon next to a unit's title on the unit page in Studio is
       another way to launch the unit access settings dialog.
    :width: 400


#. In the unit's **Settings** dialog box, for the **Restrict access to**
   option, select the group type by which you want to restrict access.

   The **Enrollment Track Groups** option is available only if your course has
   more than one :ref:`enrollment track<enrollment_track_g>`. The **Content
   Groups** option is available only if you have created :ref:`content
   groups<About Content Groups>` for use with cohorts.


   .. image:: ../../../shared/images/unit-access-settings.png
    :alt: The visibility and access settings dialog for a unit, with a
    :width: 200

   After you select a group type, you see a list of the groups that exist for
   that group type.


4. Select the checkbox for each group for which you want the current unit to
   be available.

   .. image:: ../../../shared/images/unit-access-groupselected.png
    :alt: The visibility and access settings dialog for a unit, with
       enrollment track groups selected, and two enrollment tracks available for
       selecting.
    :width: 200

#. Select **Save**.

   The groups which have access to the unit are listed under the unit title in
   the Studio course outline, as well as under the unit title on the unit page
   in Studio.

   .. image:: ../../../shared/images/unit-access-indicator.png
    :alt: When a unit has restricted access, a message listing the groups
       which have access to a unit appears under the unit title in the Studio
       course outline.
    :width: 500



.. _Preview a Unit:

****************************
Preview a Unit
****************************

You preview a unit to review and test the content before it is visible to
learners.

You can preview a unit before it is published and before the course is live.
In a live course, after the unit is published and if there are no pending
changes, previewing a unit is exactly the same as viewing the live version of
the unit.

To preview the unit, select **Preview** above the status panel in the Studio
unit page.

The unit opens in preview mode in the LMS.

.. note:: When you are revising a previously published unit, it can be helpful
   to preview your changes in one browser window and :ref:`view the published
   unit<View a Published Unit>` in a second window.

For information about previewing and testing content, see :ref:`Testing Your
Course Content`.


.. _Publish a Unit:

****************************
Publish a Unit
****************************

Publishing a unit makes the current version of the unit in Studio available to
learners. In an instructor-paced course, the release dates for the section and
subsection must also have passed for learners to access a published unit.

You publish a unit that has a status of `Draft (Never Published)`_ or `Draft
(Unpublished Changes)`_. When you publish a unit, the status changes to
`Published and Live`_ or `Published Not Yet Released`_.

You can publish a unit from the unit page or the course outline.

For more information about instructor-paced and self-paced courses, see
:ref:`Setting Course Pacing`.

=======================================
Use the Unit Page to Publish a Unit
=======================================

To publish the unit, select **Publish** in the status panel.



=======================================
Use the Outline to Publish a Unit
=======================================

To publish a unit from the outline, select the **Publish** icon in the box for
the unit.

.. image:: ../../../shared/images/outline-publish-icon-unit.png
 :alt: The Course Outline page with an arrow pointing to the Publish icon for a
     unit.
 :width: 500

.. note::
 The **Publish** icon only appears when there is new or changed content in the
 unit.

.. _Discard Changes to a Unit:

****************************
Discard Changes to a Unit
****************************

When you modify a published unit, your changes are saved in Studio, though the
changes are not visible to learners until you publish the unit again.

If you decide that you never want to publish your changes, you can discard the
changes so that Studio reverts to the last published version of the unit.

To discard changes and revert the Studio version of the unit to the last
published version, select **Discard Changes** in the status panel.

.. caution::
 When you discard changes to a unit, the changes are permanently deleted. You
 cannot retrieve discarded changes or undo the action.

.. _View a Published Unit:

****************************
View a Published Unit
****************************

To view the last published version of a unit in the LMS, select **View Live
Version** at the top of the page.

The unit page opens in the LMS in Staff view. You might be prompted to log in
to the LMS.

If the unit status is `Draft (Unpublished Changes)`_, you do not see your
changes in the LMS until you publish the unit again.

If the unit status is `Draft (Never Published)`_, **View Live Version** is not
enabled.

For information about viewing and testing content, see :ref:`Testing Your
Course Content`.

.. _Hide a Unit from Students:

****************************
Hide a Unit from Learners
****************************

You can prevent learners from seeing a unit regardless of the unit status or
the release schedules of the section and subsection.

For more information, see :ref:`Content Hidden from Students`.

You can hide a unit from learners using the course outline or the unit page.

=======================================
Use the Unit Page to Hide a Unit
=======================================

In the status panel, select **Hide from learners**.

The **Release** section applies only to instructor-paced courses. It does not
appear for units in self-paced courses.

For more information, see :ref:`Controlling Content Visibility`.

=======================================
Use the Outline to Hide a Unit
=======================================

#. Select the **Configure** icon in the unit box.

   .. image:: ../../../shared/images/outline-unit-settings.png
      :alt: The Course Outline page with the Configure icon for a unit
          indicated.
      :width: 500

   The **Settings** dialog box opens.

#. In the **Unit Visibility** section, select **Hide from learners**.

#. Select **Save**.

=======================================
Make a Hidden Unit Visible to Learners
=======================================

Before you make a hidden unit visible to learners, be aware that course content
will immediately be visible to learners, as follows.

* For a hidden unit that previously was published, deselecting **Hide from
  learners** publishes the current content for the unit. If you made changes to
  the unit while is was hidden, those draft changes are published.

* When you make a section or subsection that was previously hidden visible to
  learners, draft content in units is *not* published. Changes you made since
  last publishing units are not made visible to learners.

You can make a hidden unit visible to learners from the unit page or the course
outline. Follow the instructions above and clear the **Hide from learners**
check box.

You are prompted to confirm that you want to make the unit visible to learners.

********************************
Delete a Unit
********************************

You delete a unit from the course outline in Studio.

When you delete a unit, you delete all components within the unit.

.. warning::
 You cannot restore course content after you delete it. To ensure that you do
 not delete any content that you need later, move the unit to a
 hidden section or subsection instead of deleting it.

To delete a unit, follow these steps.

#. On the course outline page in Studio, select the **Delete** icon in the box
   for the unit you want to delete.

   .. image:: ../../../shared/images/unit-delete.png
    :alt: The Course Outline page with the Delete icons for several units
        circled.
    :width: 300

#. When you receive the confirmation prompt, select **Yes, delete this
   unit**.
