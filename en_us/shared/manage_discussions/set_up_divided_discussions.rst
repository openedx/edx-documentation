.. _About Divided Discussions:

###################################
About Divided Discussion Topics
###################################

This section provides information about setting up discussions that are
divided by learner groups (cohorts) within your course.

.. contents::
  :local:
  :depth: 1

For overview information about discussions in a course, see :ref:`Discussions`.

For more information about creating differentiated course content for learners
in different groups (cohorts), see :ref:`Offering Differentiated Content`.


******************************
What Are Divided Discussions?
******************************

With divided discussions, discussion topics are visible to all learners, but
the posts, responses, and comments within these topics are divided so that
learners participate in the discussion only with other members of the same
group (cohort).

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

You can also appoint learners as Community TAs or Group Commmunity
TAs to help you to moderate course discussions. You might use Group
Community TAs if the content of discussion topics by one group (cohort) should not be
shared with another group. Group Community TAs are themselves members of
learner groups (cohorts) that you use in your course. As discussion moderators, they can
only see and respond to posts by other members of their own group (cohort). For information,
see :ref:`Assigning_discussion_roles`.

For more information about managing discussions, see :ref:`Managing Divided
Discussion Topics` and :ref:`Running_discussions`.

.. note::

  Another method of providing different discussion experiences for learners in
  different groups in your course is to use the access settings of discussion
  components. For example, you can add multiple discussion components and use
  each component's access settings to restrict access to each discussion
  component to a specific content group. You can then assign these content
  groups to learner groups (cohorts). For more information,
  see :ref:`Setting Up Divided Discussions`.


.. _Setting Up Divided Discussions:

******************************
Setting Up Divided Discussions
******************************

.. note::
   You must set up divided discussions before your course starts. You cannot
   divide discussions after the course start date.


By default, all :ref:`course-wide discussion topics<Create CourseWide
Discussion Topics>` and :ref:`content-specific discussion topics<Create
ContentSpecific Discussion Topics>` are unified: all learners can interact
with all posts, responses, and comments. You can change discussion topics of
either type to be divided or unified on the discussions configuration page
(see :ref:`Create CourseWide Discussion Topics`).


.. warning::
   If you change settings of discussion topics in a live course after learners
   have begun reading and contributing to discussion posts, you are changing
   their course experience. Learners might see posts that were previously not
   visible to them, or they might no longer see posts that were previously
   available to all learners.

For information about settings for discussion topics, see the following
topics.

.. contents::
  :local:
  :depth: 1

.. _Divide All Content Specific Discussion Topics:

**********************************************
Divide All Content-Specific Discussion Topics
**********************************************

When you :ref:`create content-specific discussion topics<Create
ContentSpecific Discussion Topics>` by adding discussion components to units
in Studio, these discussion topics are by default unified. All learners in the
course can see and respond to posts from all other learners. You can change
content-specific discussion topics to be divided, so that only members of the
same group (cohort) can see and respond to each other's posts. To do so, follow
the steps below.

.. warning:: If you make changes to discussion division settings in a running
   course, be aware that learners will be affected by your changes.

1. Navigate to edx discussion provider configuration page
(see :ref:`Configuring Edx Discussions`).

2. Turn on the toggle for **Divide discussions by cohort** to divide all
   content-specific discussion topics by cohort.

.. image:: ../../../shared/images/Discussions_toggle_cohort.png
   :width: 300
   :alt: An image showing the toggle for dividing content-specific discussion topics

3. Click **Save** at the bottom-right of the configuration page.

All content-specific discussion topics in the course are now divided
by cohort.

For information about managing discussions that are divided, see
:ref:`Managing Divided Discussion Topics`.

.. _Divide Course Wide Discussion Topics:

*************************************
Divide Course-Wide Discussion Topics
*************************************

When you create :ref:`course-wide discussion topics<Create CourseWide
Discussion Topics>`, they are by default unified. All learners in the
course can see and respond to posts from all other learners.

.. note::
   To divide course-wide discussion topics, you will first need to divide
   content-specific discussion topics. Consequently, course-wide discussion
   topics cannot be divided without dividing all content-specific
   discussion topics.

.. warning:: If you make changes to discussion division settings in a running
   course, be aware that learners will be affected by your changes.

To specify that one or more course-wide discussion topics are divided,
follow these steps.

1. Navigate to edx discussion provider configuration page (see :ref:`Configuring Edx Discussions`).

2. Turn on the toggle for **Divide discussions by cohort** to divide all
   content-specific discussion topics by cohort.

.. image:: ../../../shared/images/Discussions_toggle_cohort.png
   :width: 300
   :alt: An image showing the toggle for dividing content-specific discussion topics

3. Turn on the toggle for **Divide course-wide discussion topics** to divide all
   course-wide discussion topics by cohort.

.. image:: ../../../shared/images/Discussion_toggle_cohort_coursewide.png
   :width: 300
   :alt: An image showing the toggle and options for dividing course-wide discussion topics

4. Uncheck the topic names that you want to keep unified.

5. Click **Save** at the bottom-right of the configuration page.

For information about managing discussions that are divided, see :ref:`Managing
Divided Discussion Topics`.
