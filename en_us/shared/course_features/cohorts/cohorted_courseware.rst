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
than others. You do this by creating :ref:`content groups<About Content Groups>`
in Studio, and restricting access to specific components in your course to one
or more content groups. Then, if you associate one or more cohorts with a
content group, only the learners in cohorts associated with that content group
can see course content that you have designated for it.

For more details about content groups, see :ref:`About Content Groups`. For an
example of cohort-specific course content, see :ref:`Cohorted Courseware
Example`.

Complete these steps to create cohort-specific content in your course.

In Studio

#. :ref:`Enable cohorts in your course<Enabling and Configuring Cohorts>`.
#. :ref:`Create content groups<Creating Content Groups>`.
#. :ref:`Specify components or units as available only to particular content
   groups<Specify Content as Available Only to Certain Content Groups>`.

In the LMS

#. :ref:`Assign learners to cohorts<Options for Assigning Learners to
   Cohorts>`.
#. :ref:`Associate one or more cohorts with a content group<Associate Cohorts
   with Content Groups>`.
#. :ref:`Preview cohort-specific course content<Viewing Cohort Specific
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

Then, in your course outline, you change the access settings for the video
component at the end of each section so that it is access is available only to
the "University-Specific Content" content group. You do not need to edit the
access settings of the quiz component, because if no content group is
specified in a component's access settings, that component is available to all
learners.

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
content as available to particular :ref:`cohorts<Cohorts Overview>` of learners.

You create content groups in Studio, and in your course outline you use the
**Access Settings** to designate whether a component is selectively available
only to one or more content groups. Any course components that do not have an
explicit restricted access setting are available to all learners, regardless of
their cohort.

Content groups do not have an actual impact on the availability of a course
component until you associate them with one or more cohorts. If you have
designated certain course content as restricted to a content group, and in
addition have associated that content group with one or more cohorts, then
only learners in those cohorts will see the designated content.

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
specify which components are available to specific content groups. For details,
see :ref:`Specify Components in Courseware as Available Only to Certain Content
Groups`.

You associate each content group with one or more cohorts in the LMS, on the
instructor dashboard. For details, see :ref:`Associate Cohorts with Content
Groups`.


.. _Specify Content as Available Only to Certain Content Groups:

******************************************************************
Specify Content as Available Only to Particular Content Groups
******************************************************************

In Studio, you can modify the settings of units or components to give access
only to learners who are in cohorts associated with particular content groups.
You cannot specify entire subsections or sections for restricted access by
particular content groups.

You do not need to edit the access settings of units or components that are
intended for all learners. Units or components that you do not restrict access
to are available to all learners enrolled in your course, regardless of the
cohort that they belong to.

.. note:: If a unit has group access restrictions set, all of its child
   components inherit these group access restrictions unless you explicitly
   set different group access restrictions for individual child components.

For details about how to modify unit access settings, see :ref:`Set Access
Restrictions For a Unit`.

For details about how to modify component access settings, see :ref:`Set Access
Restrictions For a Component`.

For details about previewing your course to ensure that learners in a cohort
correctly see the content intended for them, see :ref:`View Usage of a Content
Group` and :ref:`Viewing Cohort Specific Courseware`.

.. note:: In addition to access settings for content groups, a learner's
   ability to see a course component also depends on whether it is marked as
   visible to staff only, whether the unit is published, and the course's
   release date. For details about testing course content in general, see
   :ref:`Testing Your Course Content`.


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
   that you :ref:`designate as available to that content group<Specify Components
   in Courseware as Available Only to Certain Content Groups>` is available to
   learners in the associated cohort or cohorts.

You can associate additional cohorts with the same or a different content group
by repeating steps 3 to 7.

For an example of using content groups to create cohort-specific course
content, see :ref:`Cohorted Courseware Example`.


.. _Viewing Cohort Specific Courseware:

**************************************
Viewing Cohort-Specific Course Content
**************************************

After you restrict access to units or components to particular content groups,
you can view your course content as a member of a content group to ensure that
members of each group correctly see the content intended for them.

.. note:: In addition to access settings for content groups, a learner's
   ability to see a unit or component also depends on whether it is marked as
   visible to staff only, whether the unit is published, and the component's
   release date. For details about viewing course content in various publishing
   states, see :ref:`View Published Content` and :ref:`Preview Unpublished
   Content`.

Depending on whether you want to view published content or unpublished content,
you choose either **View Live** or **Preview** from the course outline in
Studio. You can then experience the course content as a learner in a particular
group would, by selecting the **View this course as** option for a learner in
the desired content group, as described in :ref:`Roles for Viewing Course
Content`.

For details about testing course content, see :ref:`Testing Your Course
Content`.


.. _View Usage of a Content Group:

*************************************
View Usage of a Content Group
*************************************

To view the components or units that have been made available to learners in
each of the content groups in your course, follow these steps.

#. In Studio, select **Settings**, then select **Group Configurations**.

#. On the **Group Configurations** page, locate the content group for which you
   want to view the usage.

   The content group's box displays the number of locations (units or
   components) that are designated for learners in cohorts associated with
   that content group.

#. Click the content group name to view the names of units and components that
   that are specified as available to learners in the group.

#. Click a linked location name to go to that unit in the course outline, where
   you can change the group access settings for the unit or component.

For details about previewing your course to ensure that learners in a cohort
correctly see the content intended for them, see :ref:`Viewing Cohort Specific
Courseware`.


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
