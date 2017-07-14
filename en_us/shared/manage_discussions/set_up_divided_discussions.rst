.. _About Divided Discussions:

###################################
About Divided Discussion Topics
###################################

This section provides information about setting up discussions that are
divided by learner groups (such as cohorts or enrollment tracks) within your
course.

.. contents::
  :local:
  :depth: 1

For overview information about discussions in a course, see :ref:`Discussions`.

For more information about creating differentiated course content for learners
in different groups, see :ref:`Offering Differentiated Content`.


******************************
What are Divided Discussions?
******************************

Divided discussion topics are visible to all learners, but the posts,
responses, and comments within these topics are divided so that learners
participate in the discussion only with other members of the same group
(either the same cohort or the same enrollment track).

.. note:: You can choose only one group type by which to divide discussions,
   even if your course uses cohorts and also has multiple enrollment tracks.

For example, you have two enrollment tracks in your course ("Free" and
"Certificate"). If you choose to divide discussions based on enrollment track
groups, and specify that a course-wide discussion topic called "Assignments"
is divided, then although all learners see the topic, learners in the "Free"
track interact only with posts, responses, and comments from other learners in
the "Free" track, and learners in the "Certificate" track interact only with
posts, responses, and comments from learners in the "Certificate" track.

Discussion topics that are not divided are unified, meaning that all learners
in the course can see and respond to posts, responses, and comments from any
other learner in the course.

=======================================
Best Practices for Divided Discussions
=======================================

If you divide discussions, a good practice is to use a naming convention for
discussion topics, so that learners clearly understand the audience for a
discussion topic before they add posts to that topic. For information about
naming conventions, see :ref:`Apply Naming Conventions to Discussion Topics`.

You can also choose to appoint learners as Community TAs or Group Commmunity
TAs to help you to moderate course discussions. You might choose to use Group
Community TAs if the content of discussion topics by one group should not be
shared with another group. Group Community TAs are themselves members of
groups that you use in your course (such as cohorts or enrollment tracks). As
discussion moderators, they can only see and respond to posts by other members
of their own group. For information, see :ref:`Assigning_discussion_roles`.

For more information about managing discussions, see :ref:`Managing Divided
Discussion Topics` and :ref:`Running_discussions`.

.. note::

  Another method of providing different discussion experiences for learners in
  different groups in your course is to use the access settings of discussion
  components. For example, you can add multiple discussion components and use
  each component's access settings to restrict access to each discussion
  component to a specific group of learners. With this method, you are not
  limited to choosing the same single group type by which to divide all
  discussions. For more information, see :ref:`Setting Up Divided Discussions`.


.. _Example Dividing Discussion Topics Based on Enrollment Track:

***************************************************************
Example: Dividing Discussion Topics Based on Enrollment Track
***************************************************************

In this example, you are developing a course that has two enrollment tracks:
"Free" and "Certificate". You plan to create differentiated content based on
enrollment track, so that learners in each track have a complete course
experience, but have different assignments and projects.

You will need to decide whether any of the :ref:`course-wide discussion
topics<Create CourseWide Discussion Topics>` and :ref:`content-specific
discussion topics<Create ContentSpecific Discussion Topics>` should be divided
based on enrollment track.

=============================
Course-Wide Discussion Topics
=============================

As you develop your course, you add three new course-wide discussion topics, so
that in addition to the default "General" topic, you have a total of four
course-wide discussion topics.

* General
* Course Announcements
* Assignment FAQs
* Final Project Ideas

In the "General" and "Course Announcement" topics, you and other course team
members intend to add posts that are relevant for all learners in your course,
regardless of what enrollment track they are in. You will not divide these
topics, because discussions in these topics are appropriate for a unified
learner audience.

However, you will divide the "Assignment FAQs" and "Final Project Ideas"
topics based on enrollment track, because the assignments and final projects
that learners experience will differ based on whether they are enrolled in the
"Free" track or the "Certificate" track.

Although all learners see course-wide discussion topics called "Assignment
FAQs" and "Final Project Ideas", discussions within these topics are divided.
Learners in the "Free" track only interact in discussions with other "Free"
track learners, and learners in the "Certificate" track only interact in
discussions with other "Certificate" learners.

==================================
Content-Specific Discussion Topics
==================================

You decide that content-specific discussion topics within the course should
not be divided. Instead, because learners in each enrollment track are
receiving different content, you will use the access settings at the component
level to restrict access to each discussion component to the group of learners
who can access the accompanying content.

======================
Example Implementation
======================

You implement your decisions by completing the following tasks.

* In the **Discussions** tab on the instructor dashboard in the LMS, you specify
  that you want to use enrollment tracks as the group type for dividing
  discussions.

* After you make your group type selection, lists of the course-wide and
  content-specific discussion topics appear on the **Discussions** page.

* Under **Course-Wide Discussion Topics** you select the checkboxes next to the
  "Assignment FAQs" and "Final Project Ideas" topics, and leave the others
  unselected, then click **Save** for that section.

* In Studio, in each unit where you have created differentiated content for
  learners in each enrollment track, you add two discussion components. You
  use the component access settings to make one component available only to
  learners in the "Free" enrollment track, and the other component available
  only to learners in the "Certificate" enrollment track.

* You test the course to make sure that learners in each track see the
  intended content, using the "View As" options in the LMS to view the content
  first as a learner in the "Free" enrollment track and then as a learner in
  the "Certificate" enrollment track.


.. _Setting Up Divided Discussions:

******************************
Setting Up Divided Discussions
******************************

In courses where either cohorts or multiple enrollment tracks are enabled, you
see options to divide discussion topics based on the available group types.

.. note:: You can choose only one group type by which to divide discussions,
   even if your course uses cohorts and also has multiple enrollment tracks.

The group type that you choose for dividing discussions is used to divide all
discussion topics in the course, both course-wide and content-specific.

By default, all :ref:`course-wide discussion topics<Create CourseWide
Discussion Topics>` and :ref:`content-specific discussion topics<Create
ContentSpecific Discussion Topics>` are unified: all learners can interact
with all posts responses, and comments. You can change discussion topics of
either type to be divided or unified on the instructor dashboard in the LMS.

.. note:: In courses that started prior to April 10, 2017, in courses with
   cohorts enabled and "cohorts" selected as the type of group by which
   discussions are divided, content-specific discussion topics are by default
   divided.

.. warning:: If you change settings of discussion topics in a live course
   after learners have begun reading and contributing to discussion posts, you
   are changing their course experience. Learners might see posts that were
   previously not visible to them, or they might no longer see posts that were
   previously available to all learners.

For information about settings for discussion topics, see the following
topics.

* :ref:`Specify the Group Type for Dividing Discussions`
* :ref:`Specify Which Course Wide Discussion Topics are Divided`
* :ref:`Content Specific Discussion Topics and Groups`
* :ref:`Specify that All ContentSpecific Discussion Topics are Divided`
* :ref:`Specify Some ContentSpecific Discussion Topics are Divided`


.. _Specify the Group Type for Dividing Discussions:

**********************************************************
Specify The Group Type for Dividing Discussions
**********************************************************

.. note:: You can choose only one group type by which to divide discussions,
   even if your course uses cohorts and also has multiple enrollment tracks.

The group type that you choose for dividing discussions is used to divide all
discussion topics in the course, both course-wide and content-specific.

To specify the group type for dividing discussions, follow these steps.

#. In the LMS, select **Instructor**, then select **Discussions**.

    .. note:: The **Discussions** tab is available only if you have enabled
       cohorts or have multiple enrollment tracks in your course.

#. Under **Specify whether discussion topics are divided**, select the option
   to use for dividing discussion topics. You only see options that are
   applicable for your course. For example, if cohorts are not enabled in your
   course, you do not have an option to divide discussions based on cohorts.
   If you do not have more than one enrollment track in your course, you do
   not have an option to divide discussions based on enrollment track.


   .. image:: ../../../shared/images/DivideDiscussionsGroupType.png
      :alt: An image showing the options for selecting the group type for
            dividing discussions.

   After you specify the group type for dividing discussions, you see the
   lists of existing course-wide discussion topics and content-specific
   discussion topics.

For information about specifying which course-wide topics and which content-
specific topics are divided, see :ref:`Specify Which Course Wide Discussion
Topics are Divided`, :ref:`Specify that All ContentSpecific Discussion Topics
are Divided`, and :ref:`Specify Some ContentSpecific Discussion Topics are
Divided`.


.. _Specify Which Course Wide Discussion Topics are Divided:

**********************************************************
Specify Which Course-Wide Discussion Topics are Divided
**********************************************************

When you create :ref:`course-wide discussion topics<Create CourseWide Discussion
Topics>` or :ref:`content-specific discussion topics<Create ContentSpecific
Discussion Topics>`, they are by default unified. All learners in the course can
see and respond to posts from all other learners.

After you have specified the group type for dividing discussions, you can
specify which of your discussion topics are divided.

.. warning:: If you make changes to discussion division settings in a running
   course, be aware that learners will be affected by your changes.

To specify that one or more discussion topics are divided, follow these steps.

#. In the LMS, select **Instructor**, then select **Discussions**.

#. Under the section for **Course-Wide Discussion Topics** select the
   checkbox next to each course-wide discussion topic that you want to divide.
   Clear the checkbox next to each course-wide discussion topic that you want
   to make unified.

   .. image:: ../../../shared/images/DivideDiscussionsCourseWide.png
      :alt: An image showing the checkboxes for specifying which course-wide
        topics are divided.


#. Select **Save** for that section.

   The list of course-wide discussion topics is updated to show which topics
   are divided, and which are unified.

For information about dividing content-specific discussions, see :ref:`Specify
that All ContentSpecific Discussion Topics are Divided` and :ref:`Specify Some
ContentSpecific Discussion Topics are Divided`.

For information about managing discussions that are divided, see :ref:`Managing
Divided Discussion Topics`.


.. _Content Specific Discussion Topics and Groups:

**********************************************
Content-Specific Discussion Topics and Groups
**********************************************

When you :ref:`create content-specific discussion topics<Create
ContentSpecific Discussion Topics>` by adding discussion components to units
in Studio, these discussion topics are by default unified. All learners in the
course can see and respond to posts from all other learners. You can change
content-specific discussion topics to be divided, so that only members of the
same group can see and respond to each other's posts.

If you want all content-specific discussion topics that you add in your course
to be always divided, follow the steps in the topic :ref:`Specify that All
ContentSpecific Discussion Topics are Divided`.

If you want only some content-specific discussion topics to be divided,
following the steps in the topic :ref:`Specify Some ContentSpecific Discussion
Topics are Divided`.

.. _Specify that All ContentSpecific Discussion Topics are Divided:

*****************************************************************
Specify that All Content-Specific Discussion Topics are Divided
*****************************************************************

When you first :ref:`add content-specific topics<Create ContentSpecific
Discussion Topics>` in your course, by default they are unified.

If you want all content-specific discussion topics in your course to be
divided, follow these steps.

.. warning:: If you make changes to discussion division settings in a running
   course, be aware that learners will be affected by your changes.

#. In the LMS, select **Instructor**, then select **Discussions**.

   In the **Content-Specific Discussion Topics** section the **Divide the
   selected content-specific discussion topics** option is selected by default.
   Content-specific topics that exist are listed, but none of them should be
   selected, indicating that these topics are not divided.

#. If it is not already selected, select **Always divide content-specific
   discussion topics**.

#. Click **Save** at the bottom of the **Content-Specific Discussion Topics**
   section.

   All content-specific discussion topics in the course are now divided, based on
   the group type that you :ref:`specified for dividing discussions<Specify the
   Group Type for Dividing Discussions>`, and you cannot change the division
   settings of individual content-specific discussion topics.

For information about dividing only some content-specific discussions, see
:ref:`Specify Some ContentSpecific Discussion Topics are Divided`.

For information about managing discussions that are divided, see
:ref:`Managing Divided Discussion Topics`.


.. _Specify Some ContentSpecific Discussion Topics are Divided:

*****************************************************************
Specify That Some Content-Specific Discussion Topics are Divided
*****************************************************************

The default division setting for content-specific discussion topics is that
they are unified. The **Divide the selected content-specific discussion
topics** option is selected by default. Content-specific topics that exist are
listed, but none of them should be selected, indicating that these topics are
not divided. On this setting, content-specific discussion topics are unified
when you first :ref:`add them<Create ContentSpecific Discussion Topics>` in
your course.

To specify that only some of your content-specific discussion topics are
divided, you change the division setting for content-specific discussion
topics and then explicitly select only the topics that you want to divide.

.. warning:: If you change the setting from **Always divide content-specific
   discussion topics** to **Divide the selected content-specific discussion
   topics**, all content-specific discussion topics are unified, unless you
   explicitly specify which discussion topics are divided before saving your
   changes. This means that any posts that were previously divided are now
   shared by all learners in your course.

To specify that only some content-specific discussion topics in your course are
divided, follow these steps.

.. warning:: If you make changes to discussion division settings in a running
   course, be aware that learners will be affected by your changes.

#. In the LMS, select **Instructor**, then select **Discussions**.

#. In the **Content-Specific Discussion Topics** section, if it is not already
   selected, select **Divide the selected content-specific discussion topics**.

   .. image:: ../../../shared/images/DivideDiscussionsContentSpecific.png
      :alt: An image showing the checkboxes for specifying which content-specific
        topics are divided.

   The list of content-specific discussion topics becomes editable.

#. Select the checkbox next to each content-specific discussion topic that you
   want to divide.

#. Click **Save** at the bottom of the **Content-Specific Discussion Topics**
   section.

   The changes to your content-specific discussions are saved. The content-
   specific discussion topics that you selected are now divided, and learners
   in the group type that you specified only interact with other learners in
   their group. All other content-specific discussion topics are unified.

For information about always dividing content-specific discussions, see
:ref:`Specify that All ContentSpecific Discussion Topics are Divided`.

For information about managing discussions that are divided, see
:ref:`Managing Divided Discussion Topics`.
