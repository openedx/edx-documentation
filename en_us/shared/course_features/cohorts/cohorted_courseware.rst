.. _Cohorted Courseware Overview:

###########################################
Creating Cohort-Specific Course Content
###########################################

This section provides information about setting up content for specific
cohorts.

.. contents::
  :local:
  :depth: 1

*********
Overview
*********

If you have :ref:`enabled cohorts<Enabling and Configuring Cohorts>` in your
course, you can create different course experiences for learners in different
cohorts.

You can design your course so that some learners are given different content
than others. You do this by creating :ref:`content groups<About Content
Groups>` in Studio, and designating specific components in your course as
visible only to one or more content groups. Then, if you associate one or more
cohorts with a content group, only the learners in cohorts associated with that
content group can see course content that you have designated for it.

For more details about content groups, see :ref:`About Content Groups`. For an
example of cohort-specific course content, see :ref:`Cohorted Courseware
Example`.

Complete these steps to create cohort-specific content in your course.

In Studio

#. :ref:`Enable cohorts in your course<Enabling and Configuring Cohorts>`.
#. :ref:`Create content groups<Creating Content Groups>`.
#. :ref:`Specify course components as visible only to particular content
   groups<Specify Components in Courseware as Visible Only to Certain Content
   Groups>`.

In the LMS

#. :ref:`Assign learners to cohorts<Options for Assigning Learners to
   Cohorts>`.
#. :ref:`Associate one or more cohorts with a content group<Associate Cohorts
   with Content Groups>`.
#. :ref:`Preview cohort-specific course content<Preview Cohort Specific
   Courseware>`.

.. _Cohorted Courseware Example:

*****************************************
Example: Cohort-Specific Course Content
*****************************************

Suppose that you create two :ref:`cohorts<Cohorts Overview>` in your course:
University Alumni and Current University Students. Learners who are not in
either of these cohorts are automatically placed into a third cohort, the
default cohort, when they access the **Course** or **Discussion** tabs in the
course. For more information about enabling cohorts in your course and
assigning students to cohorts, see :ref:`Enabling and Configuring Cohorts`.

You intend all learners to have substantially the same course experience, with
the exception that only learners in the two university-related cohorts will
receive content that is specific to your university and therefore only of
interest to them.

At the end of every section, you intend to include a video message from various
university officials, including the university president and the dean of your
college. These videos will be shown only to learners in the university and
alumni cohorts. Also at the end of each section, you intend to include a quiz
to test knowledge of the concepts taught in that section. The quiz will be
shown to all learners enrolled in the course.

To achieve this, on the **Group Configurations** page in Studio you create one
content group called "University-Specific Content". In the Instructor
Dashboard, on the **Cohorts** tab, you associate both the "University Alumni"
and the "Current University Students" cohorts with the "University-Specific
Content" content group.

Then, in your course outline, you change the visibility settings for the video
component at the end of each section so that it is visible only to the
"University-Specific Content" content group. You do not need to edit the
visibility settings of the quiz component, because if no content group is
specified in a component's visibility settings, it is visible to all learners.

As a final step, you preview the course in the LMS to ensure that learners see
the content that is intended for them. You confirm that when you view the
course in the role of **Student** (in other words, any learner not in a content
group), you see a quiz at the end of each section, but do not see the
university-related videos. When you view the course as a learner in the
"University-Specific Content" group, you see a university-related video as well
as the quiz at the end of each section.

.. _About Content Groups:

**************
Content Groups
**************

Content groups are virtual groupings of learners who will see a particular set
of course content. You can use content groups to designate specific course
content as visible to particular :ref:`cohorts<Cohorts Overview>` of learners.

You create content groups in Studio, and in your course outline you use the
**Visibility Settings** to designate whether a component is selectively visible
only to one or more content groups. Any course components that do not have an
explicitly restricted visibility setting remain visible to all students,
regardless of their cohort.

Content groups do not have an actual impact on the visibility of a course
component until you associate them with one or more cohorts. If you have
designated certain course content as visible to a content group, and in
addition have associated that content group with one or more cohorts, then
those cohorts will see the designated content.

For an example of using content groups to create cohort-specific course
content, see :ref:`Cohorted Courseware Example`.

.. _Creating Content Groups:

*********************
Create Content Groups
*********************

To create a content group, follow these steps.

#. In Studio, select **Settings**, then select **Group Configurations**.

#. On the **Group Configurations** page, select **New content group**.

   .. image:: ../../../../shared/images/Cohorts_AddContentGroup.png
    :width: 600
    :alt: Button on Group Configurations page for adding first content group.

#. Enter a meaningful name for the content group, then select **Create**.
   The page refreshes to show the name of your new content group.

#. Repeat this step to create as many content groups as you want.

After you create a content group, you can work with your course outline to
specify which components are visible to specific content groups. For details,
see :ref:`Specify Components in Courseware as Visible Only to Certain Content
Groups`.

You associate each content group with one or more cohorts in the LMS, on the
instructor dashboard. For details, see :ref:`Associate Cohorts with Content
Groups`.

.. _View Usage of a Content Group:

*************************************
View Usage of a Content Group
*************************************

To view the units that are visible to a content group, follow these steps.

#. In Studio, select **Settings**, then select **Group Configurations**.

#. On the **Group Configurations** page, locate the content group for which you
   want to view the usage.

   The content group's box displays whether the content group is used in this
   course. If it is used, you see the number of units that it is used in, and
   links to each unit.

#. Select each link to go to that unit in the **Course Outline**, where you can
   :ref:`specify whether that unit is visible to the content group<Specify
   Components in Courseware as Visible Only to Certain Content Groups>`.

For details about previewing your course to ensure that learners in a cohort
correctly see the content intended for them, see :ref:`Preview Cohort Specific
Courseware`. For details about deleting content groups, see :ref:`Delete
Content Groups`.

.. _Delete Content Groups:

*********************
Delete Content Groups
*********************

.. note:: You can delete a content group only if it is not in use in any course
   unit. To delete a content group that is currently in use, you must first
   remove it from any course unit visibility settings that use the content
   group. For information about seeing which units use a content group, see
   :ref:`View Usage of a Content Group`.

#. In Studio, select **Settings**, then select **Group Configurations**.

#. On the **Group Configurations** page, locate the content group that you want
   to delete.

#. Move your cursor over the content group's box, then select the **Delete**
   icon.

#. In the confirmation message, select **Delete** again to confirm the
   deletion.

.. _Specify Components in Courseware as Visible Only to Certain Content Groups:

******************************************************************
Specify Components as Visible Only to Particular Content Groups
******************************************************************

After you create at least one content group, you can edit your course in Studio
and modify the visibility settings of components that you want to make visible
only to particular content groups.

.. note:: You do not need to edit the visibility settings of components that
   are intended for all learners. Components that you do not explicitly
   indicate as visible to a group are visible to all learners enrolled in your
   course, regardless of the cohort that they belong to.

You can specify content as visible to content groups only at the component
level in a unit. You cannot specify entire units, subsections, or sections for
visibility to content groups.

In a separate task, you create cohorts and associate content groups with
cohorts. Then, only the cohorts associated with content groups which you
selected in a component's visibility settings can view the component. See
:ref:`Associate Cohorts with Content Groups` for details about associating
cohorts with content groups.

To specify components as visible only to particular content groups, follow
these steps.

#. In Studio, select **Content**, then select **Outline**.

#. For each component that you want to make visible only to a particular
   content group or groups, select the unit name, then select the **Visibility
   Settings** icon.

   .. image:: ../../../../shared/images/Cohorts_VisibilitySettingInUnit.png
    :alt: A component in the unit page with the visibility setting icon
      highlighted.
    :width: 600

#. In the **Editing visibility** dialog, select **Specific Content Groups**,
   then select the checkbox for each content group for which you want the
   current component to be visible.

   .. image:: ../../../../shared/images/Cohorts_EditVisibility.png
    :width: 400
    :alt: The visibility settings dialog box for a component.

#. Select **Save**.

The **Visibility Settings** icon for the component is now black.

.. image:: ../../../../shared/images/Cohorts_VisibilitySomeGroup.png
   :alt: The black visibility icon for a component, showing that the component
     is restricted
   :width: 200

The publishing details for the course section in the sidebar indicate that some
content is visible only to particular groups.

.. image:: ../../../../shared/images/Cohorts_OnlyVisibleToParticularGroups.png
   :alt: Course outline sidebar showing showing a black unit visibility icon
     and the note indicating that some content in the unit is visible only to a
     particular group.
   :width: 300

For details about previewing your course to ensure that students in a cohort
correctly see the content intended for them, see :ref:`Preview Cohort Specific
Courseware`.

.. note:: In addition to visibility settings for content groups, a learner's
   ability to see a course component also depends on whether it is hidden from
   students, whether the unit is published, and the course's release date. For
   details about previewing course content in general, see :ref:`Preview Course
   Content`.

.. _Associate Cohorts with Content Groups:

*************************************
Associate Cohorts with Content Groups
*************************************

After you create a content group, you can associate it with one or more cohorts
with which you want to share the same special content.

.. note:: A content group can be associated with more than one cohort; a cohort
   cannot be associated with more than one content group.

To associate a cohort with a content group, follow these steps:

#. In the LMS, select **Instructor**, then select **Cohorts**.

#. From the cohorts drop down list, select the cohort to which you want to
   associate your content group.

#. Select the **Settings** tab for the selected cohort.

#. Under **Associated Content Group**, choose the **Select a Content Group**
   option.

#. From the content group drop down list, select the content group that you
   want your cohort to be associated with.

   .. image:: ../../../../shared/images/Cohorts_AssociateWithContentGroup.png
     :alt: Select a content group to associate with the cohort.

#. Select **Save**.

   You have now associated your content group with a cohort. Any course content
   that you :ref:`designate as visible to that content group<Specify Components
   in Courseware as Visible Only to Certain Content Groups>` is visible to
   students in the associated cohort or cohorts.

You can associate additional cohorts with the same or a different content group
by repeating steps 3 to 7.

For an example of using content groups to create cohort-specific course
content, see :ref:`Cohorted Courseware Example`.

.. _Preview Cohort Specific Courseware:

**************************************
Preview Cohort-Specific Course Content
**************************************

After you designate components as being visible only to certain content groups,
you can preview your course content to ensure that each group correctly sees
the content intended for them.

.. note:: In addition to visibility settings for content groups, a learner's
   ability to see a course component also depends on whether it is hidden from
   students, whether the unit is published, and the course's release date. For
   details about previewing course content in general, see :ref:`Preview Course
   Content`.

You can view the course as a member of these groups.

.. list-table::
    :widths: 15 30
    :header-rows: 1

    * - Role
      - When You "View As" This Role
    * - Staff
      - You see all content in the course, including content that is hidden
        from learners.
    * - Student
      - You see any content that is intended for all
        students.
    * - Specific Student
      - You see content that is intended for the student whose email or
        username you specify.
    * - Student in <Content Group Name>
      - You see content that is intended for all learners, as well
        as any content specifically set to be visible to this content group.

#. In Studio, in the course outline, select **Preview**. You see your
   course section in the **Course** section of the LMS.

#. In the navigation bar at the top of the page, select one of the options in
   the **View this course as** drop down list, as described in the table above.

   .. image:: ../../../../shared/images/Cohorts_ViewCourseAs.png
     :alt: The "View this course as" drop down list, with a content group
         selected.
     :width: 400

The course view refreshes and the content is presented as a member of the
selected content group would see it.

After your course is live, you can also see the live version as a learner would
see it, by selecting **View Live** from Studio. For more information, see
:ref:`View Your Live Course`.
