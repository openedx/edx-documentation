
.. _Set up Discussions in Cohorted Courses:

######################################################
Setting up Discussions in Courses with Cohorts
######################################################

This section provides information about setting up discussions for specific
cohorts.

.. contents::
  :local:
  :depth: 1

*********
Overview
*********

In courses that have cohorts enabled, discussion topics can be either divided
by cohort, or unified and accessible to all learners.

Discussion topics that are divided by cohort are visible to all learners but
the posts, responses, and comments within them are divided so that they are
visible only to members of the same cohort. Posts, responses, and comments
within unified discussion topics are visible to all learners in the course,
regardless of cohort.

When you first enable cohorts in your course, the initial behavior for
:ref:`course-wide discussion topics<Coursewide Discussion Topics and Cohorts>`
is different from the behavior of :ref:`content-specific discussion topics
<Content Specific Discussion Topics and Cohorts>`.

By default, course-wide discussion topics are unified because these discussions
are generally used for posts that are of broad interest to all learners in the
course. In contrast, content-specific discussion topics are by default divided
by cohort. You can change discussion topics of either type to be divided or
unified on the instructor dashboard in the LMS.

.. warning:: If you change the cohort settings of discussion topics in a live
   course after learners have begun reading and contributing to discussion
   posts, you are changing their course experience. Learners might see posts
   that were previously not visible to them, or they might no longer see posts
   that were previously available to all learners. If you make changes to
   cohort settings in a running course, be aware of the implications of your
   changes. For more details, see :ref:`Altering Cohort Configuration`.

For information about cohort settings for discussion topics, see the following
topics.

* :ref:`Coursewide Discussion Topics and Cohorts`
* :ref:`Specify Whether CourseWide Discussion Topics are Cohorted`
* :ref:`Content Specific Discussion Topics and Cohorts`
* :ref:`Specify that All ContentSpecific Discussion Topics are Cohorted`
* :ref:`Specify Some ContentSpecific Discussion Topics as Cohorted`

For overview information about discussions in a course, see :ref:`Discussions`.
For information about using cohorts in a course and managing discussions that
are divided by cohort, see :ref:`Cohorts Overview` and :ref:`Moderating
Discussions for Cohorts`.

.. note:: Making discussion topics divided by cohort, described in this and
   the following topics, only divides posts within the discussion topics by
   cohort; the discussion topics are still visible to all learners in the
   course. If you want to make specific content-specific discussion topics
   visible only to certain cohorts, you can implement content groups and
   change the visibility settings on the discussion components. For more
   details, see :ref:`Cohorted Courseware Overview`.

.. _Coursewide Discussion Topics and Cohorts:

***********************************************
Course-Wide Discussion Topics and Cohorts
***********************************************

When you first :ref:`create a course-wide discussion topic<Create CourseWide
Discussion Topics>`, it is unified, and all learners in the course can post,
read, respond, and comment in the topic without regard to their cohort
assignments.

After you add a course-wide topic, you can configure it so that it is divided
by cohort instead. For step-by-step instructions for specifying whether a
course-wide discussion topic is unified or divided by cohort, see
:ref:`Specify Whether CourseWide Discussion Topics are Cohorted`.

====================================================================
Example: Making Some Course-Wide Discussion Topics Divided by Cohort
====================================================================

Course-wide discussion topics are by default unified, so that all learners can
participate. In some instances, however, you might decide that it makes sense
to divide some course-wide discussion topics by cohort, so that members of each
cohort only see and respond to posts made by learners in the same cohort.

For example, in addition to the system-supplied General topic, you add three
new course-wide discussion topics, for a total of four discussion topics.

* General
* Course Q&A
* Announcements
* Brainstorming

The posts that you intend to make to the General and Course Q&A topics, and
the subjects you expect learners to explore there, are appropriate for a
unified learner audience.

However, you decide that it will be useful for the Announcements and
Brainstorming topics to be divided by cohort. For information about specifying
whether course-wide discussion topics are divided by cohort, see :ref:`Specify
Whether CourseWide Discussion Topics are Cohorted`.

You also decide to apply a naming convention so that learners will know the
audience for the discussion topics before they add any posts. For information
about naming conventions, see :ref:`Apply Naming Conventions to Discussion
Topics`.

.. _Specify Whether CourseWide Discussion Topics are Cohorted:

********************************************************************
Specify Whether Course-Wide Discussion Topics are Divided by Cohort
********************************************************************

When you :ref:`create course-wide discussion topics<Create CourseWide
Discussion Topics>`, they are by default unified, and all learners in the
course can see and respond to posts from all other learners. You can change
course-wide discussion topics to be divided by cohort, so that only members of
the same cohort can see and respond to each other's posts.

To change the cohort settings for course-wide discussion topics, follow these
steps.

#. In the LMS, select **Instructor**, then select **Cohorts**.

#. Select **Specify whether discussion topics are divided by cohort**.

#. In the **Course-Wide Discussion Topics** section, select the checkbox next
   to each course-wide discussion topic that you want to divide by cohort.
   Clear the checkbox next to each course-wide discussion topic that you want
   to make unified.

#. Select **Save**.

   The list of course-wide discussion topics is updated to show which topics
   are divided by cohort, and which are unified.

   .. image:: ../../../../shared/images/CohortDiscussionsCourseWide.png
     :alt: Two course-wide discussion topics in list, one cohorted and one
       unified.
     :width: 400

For more information about managing discussions that are divided by cohort, see
:ref:`Moderating Discussions for Cohorts`.

.. _Content Specific Discussion Topics and Cohorts:

**********************************************
Content-Specific Discussion Topics and Cohorts
**********************************************

When you enable the cohort feature for a course, and :ref:`create content-specific discussion topics<Create ContentSpecific Discussion Topics>` by adding
discussion components to units in Studio, these content-specific discussion
topics are by default divided by cohort. A learner who is assigned to one
cohort cannot read or add to the posts, responses, or comments contributed by
the members of another cohort.

If you want all content-specific discussion topics in your course to be
divided by cohort, you do not need to take any action. For more information,
see :ref:`Specify that All ContentSpecific Discussion Topics are Cohorted`.

Alternatively, you can specify that you want most of the content-specific
discussion topics in your course to be unified, and make :ref:`only a few
discussion topics divided by cohort<Specify Some ContentSpecific Discussion
Topics as Cohorted>`.

.. _Specify that All ContentSpecific Discussion Topics are Cohorted:

*****************************************************************
Specify that All Content-Specific Discussion Topics are Cohorted
*****************************************************************

The default behavior for content-specific discussion topics is that they are
divided by cohort when you first :ref:`add them<Create ContentSpecific
Discussion Topics>` in your course. If you want all content-specific
discussion topics in your course to be divided by cohort, you do not need to
take any action.

You can confirm this setting on the Instructor Dashboard **Cohorts** tab.

#. In the LMS, select **Instructor**, then select **Cohorts**.

#. Select **Specify whether discussion topics are divided by cohort**.

  .. image:: ../../../../shared/images/CohortDiscussionsSpecifyLink.png
    :alt: The link in the UI to specify whether content specific discussion
        topics are divided by cohort.
    :width: 800

In the **Content-Specific Discussion Topics** section, you see that the
**Always cohort content-specific discussion topics** option is selected.

All content-specific discussion topics in your course are divided by cohort,
and you cannot change the cohort settings of individual content-specific
discussion topics.

.. image:: ../../../../shared/images/CohortDiscussionsAlwaysCohort.png
 :alt: Content specific discussion topics controls with the "Always cohort
  content specific discussion topics" option selected.
 :width: 500

For information about changing the cohort settings for your content-specific
discussions to make all of them unified except a few, see :ref:`Specify Some
ContentSpecific Discussion Topics as Cohorted`.

.. _Specify Some ContentSpecific Discussion Topics as Cohorted:

**************************************************************************
Specify that Some Content-Specific Discussion Topics are Divided by Cohort
**************************************************************************

The default behavior for content-specific discussion topics is that they are
divided by cohort when you first :ref:`add them<Create ContentSpecific
Discussion Topics>` in your course.

To make only a few of your content-specific discussion topics divided by
cohort, you change the cohort settings for content-specific discussion topics
to make them all unified, and then explicitly select only the topics that you
want to be divided by cohort.

.. warning:: When you change the cohort setting from **Always Cohort Content-
   Specific Discussion Topics** to **Cohort Selected Content-Specific
   Discussion Topics**, you are making all content-specific discussion topics
   in your course unified, unless you explicitly change them to be divided by
   cohort before saving your changes. This means that any posts that were
   previously divided by cohort and restricted to viewing, responding, and
   commenting by members of the same cohort are now visible to all learners in
   your course.

   If you make changes to cohort settings in a running course, be aware of the
   implications of your changes. For more details, see :ref:`Altering Cohort
   Configuration`.

To specify that only some content-specific discussion topics in your course are
divided by cohort, follow these steps.

#. In the LMS, select **Instructor**, then select **Cohorts**.

#. Select **Specify whether discussion topics are divided by cohort**.

   .. image:: ../../../../shared/images/CohortDiscussionsSpecifyLink.png
    :alt: The link in the UI to specify whether content specific discussion
        topics are divided by cohort.
    :width: 800

#. In the **Content-Specific Discussion Topics** section, if it is not already
   selected, select **Cohort selected content-specific discussion topics**.

   .. warning:: If you make changes to cohort settings in a running course, be
      aware of the implications of your changes. For more details, see
      :ref:`Altering Cohort Configuration`.

   All content-specific discussion topics that you add in your course are
   unified and visible to all learners. The list of content-specific
   discussion topics becomes editable.

#. Select the checkbox next to each content-specific discussion topic that you
   want to divide by cohort.

   .. image:: ../../../../shared/images/CohortDiscussionsCohortSelected.png
     :alt: Content specific discussion topics controls with the "Cohort
      selected content specific discussion topics" option selected.
     :width: 500

#. Select **Save**.

   The changes to your content-specific discussions are saved. The
   content-specific discussion topics that you selected are saved as being
   divided by cohort. All other content-specific discussion topics are unified.

For more information about managing discussions that are divided by cohort, see
:ref:`Moderating Discussions for Cohorts`.
