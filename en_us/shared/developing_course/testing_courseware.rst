.. _Testing Your Course Content:

###########################
Testing Your Course Content
###########################

The way your course looks in Studio is different from the way that learners
will see and experience it when it is live in the LMS. As a best practice, you
should test content continually as you build your course, by interacting with
the course content from a learner's point of view.

The method that you choose for experiencing the course content as a learner
depends on the publishing status of the content.

* For published and released content, use :ref:`View Live<View Published
  Content>`.

* For draft and unreleased content, use :ref:`Preview<Preview Unpublished
  Content>`.

For more information, see the following topics.

.. contents::
  :local:
  :depth: 1

Beta testing your course is another way to evaluate course content. For
information about setting up a beta test for your course, see
:ref:`Beta_Testing`.

To test content before a course has started, you can add yourself as a beta
tester on the instructor dashboard. Make sure to set the course start date and
the appropriate **Days Early for Beta** value. For more information, see
:ref:`Beta_Testing`.


.. _View Published Content:

**************************************
Viewing Published and Released Content
**************************************

If your course has started, you can view published and released course content
from the point of view of a learner. When you select **View Live** or **View
Live Version** from the course outline in Studio, you can choose specific views
in the LMS to experience the course content exactly as a particular learner
would.

.. note:: For courses that have not started, **View Live** mode provides only
   **Staff** view, and you can only view content that has a publishing
   status of Published.

In courses that have started, when you use **Staff** view in **View Live**
mode, keep the following points in mind.

* In addition to units that have a publishing status of :ref:`published and
  live<Published and Live>` you also see units that are published but not yet
  released.

* You see published units that are in :ref:`Visible to Staff Only` or
  :ref:`Draft (Unpublished Changes)` status, regardless of the release dates of
  the containing section or subsection, but you see only the latest published
  version of such units.

* You do not see units that are in :ref:`Draft (Never Published)` status. To
  see these units, you must use Preview mode, as described in :ref:`Preview
  Unpublished Content`.

* If you view the course in a role other than **Staff**, you do not have
  access to the **Instructor** tab or to staff functions such as **View Unit in
  Studio**, **Staff Debug Info**, or **Submission History**.

For information about unit publishing statuses, see :ref:`Unit Publishing
Status`.

========================================
View Published and Released Content
========================================

To view published and released content as it would appear to members of
different groups, follow these steps.

#. From the Studio **Course Outline** page, select **View Live**.
   Alternatively, from a unit page, select **View Live Version**.

   A separate browser tab opens for the course in the LMS.

#. In the LMS, select one of the **View this course as** options, as described
   in :ref:`Roles for Viewing Course Content`.

The course view refreshes to present published course content as a learner in
the selected group would see it.

For more information about each view, see :ref:`Staff View`, :ref:`Student
View`, or :ref:`Specific Student View`. For more information about viewing
cohort-specific course content, see :ref:`Viewing Cohort Specific Courseware`.


.. _Preview Unpublished Content:

************************
Previewing Draft Content
************************

Before your course has started, or before you release content to learners, you
can test how the content will appear when it is released.

Similar to :ref:`viewing published content<View Published Content>`, you can
choose specific views in the LMS to experience draft or unreleased course
content as learners belonging to different groups would, but you select
**Preview** from the course outline in Studio instead of **View Live**.

In **Preview** mode, if you use one of the student-based **View course as**
options, you can see draft course content unrestricted by release date. You
see any content that has a publishing status of :ref:`Published and Live` as
well as content with publishing statuses of :ref:`Draft (Never Published)` or
:ref:`Draft (Unpublished Changes)`.

When you use **Staff** view in preview mode, you also see any content that is
:ref:`Visible to Staff Only`.


=============================
Preview Draft Content
=============================

To preview draft content and see how it would appear to members of different
groups when it is released, follow these steps.

#. From a unit page in the **Course Outline** in Studio, select **Preview**.

   A separate browser tab opens for the course in the LMS.

#. In the LMS, select one of the **View this course as** options, as described
   in :ref:`Roles for Viewing Course Content`.

The course view refreshes to present course content as it is currently
configured in Studio, and as a learner in the selected group would see it.

.. note:: If you use randomized content blocks in your course, you cannot
   preview unpublished units that contain content from randomized content
   blocks, because the randomized content is not assigned until after the unit
   is published. For information about viewing the actual content that has
   been assigned to a particular learner from a randomized content block in a
   live course, see :ref:`Specific Student View`.


.. _Roles for Viewing Course Content:

***************************************
Viewing Course Content Based on Roles
***************************************

When you select **View Live** or **Preview** from the course outline in Studio,
you can see how it would appear to members of different groups by selecting one
of the **View this course as** options in the LMS.

   .. image:: ../../../shared/images/Groups_ViewCourseAs.png
     :alt: The "View this course as" drop down list, with a group selected.

The following table summarizes the content that is available in either **View
Live** mode or **Preview** mode when you choose a role for viewing the
content.

.. list-table::
    :widths: 15 20 20
    :header-rows: 1

    * - "View this course as" Role
      - In "View Live" Mode
      - In "Preview" Mode

    * - :ref:`Staff<Staff View>`
      - You see content that has any of the publishing statuses
        :ref:`Published and Live`, :ref:`Published Not Yet Released`, or
        :ref:`Draft (Unpublished Changes)`. In **Staff** view, you also see
        content that is :ref:`Visible to Staff Only`.
      - In addition to the content you would see in "View Live" mode, you also
        see content that is in :ref:`Draft (Never Published)` status. In
        **Staff** view, you also see content that is :ref:`Visible to Staff
        Only`.

    * - :ref:`Learner<Student View>`
      - You see content that has a status of :ref:`Published and Live`, and
        that is intended for all learners. For example, you see content that
        is not intended for a specific cohort group. In **Student** view, you
        do not see content that is :ref:`Visible to Staff Only`.
      - In addition to the content that you would see in "View Live" mode, you
        also see content that has a status of :ref:`Draft (Never Published)`
        or :ref:`Draft (Unpublished Changes)`. In **Student** view, you do not
        see content that is :ref:`Visible to Staff Only`.

    * - :ref:`Specific Learner<Specific Student View>`
      - You see content that has a status of :ref:`Published and Live`, and is
        intended for the specific learner whose email or username you enter.
      - **Specific student** view is not available for unpublished content or
        if the course has not started.

    * - :ref:`Learner in a Specific Content Group<Student in Content Group
        View>`
      - You see content that has a status of :ref:`Published and Live` that
        would be available to learners who belong to the specified content
        group.
      - In addition to the content you would see in "View Live" mode, you also
        see content that has a status of :ref:`Draft (Never Published)` or
        :ref:`Draft (Unpublished Changes)` that would be available to learners
        who belong to the specified content group.

    * - :ref:`Learner in an Enrollment Track<Learner in Enrollment Track Group
        View>`
      - You see content that has a status of :ref:`Published and Live` that
        would be available to learners who are in the specified enrollment
        track.
      - In addition to the content you would see in "View Live" mode, you also
        see content that has a status of :ref:`Draft (Never Published)` or
        :ref:`Draft (Unpublished Changes)` that would be available to learners
        who are in the specified enrollment track.

.. note:: When a unit's state is :ref:`Published and Live`, the preview and
   the live versions of the course are exactly the same. In this case,
   selecting either **View Live** or **Preview** gives you the same view of
   that unit.


.. _Staff View:

===========
Staff View
===========

Staff view displays content in your course as any member of the course team
would experience it.

When you view your course content using **Staff** view, you can execute tests
to make sure that your course works the way you intend. For example, before
the release date of a subsection, members of the course team can work through
the problems to verify that the correct answer receives a green check for
correct, and that any answer other than the correct one receives a red X for
incorrect.

When you use **Staff** view in the LMS, you can go back to Studio to edit
course content in the following ways.

* On a unit page, select **View Unit in Studio** to open the unit within the
  course outline in Studio.

* From the instructor dashboard, select **View Course in Studio** to open the
  course outline in Studio.

* On the **Progress** page, select **View Grading in Studio** to open the
  **Grading** page in Studio.


.. _Student View:

============
Learner View
============

Learner view displays content in your course as an enrolled learner in your
course would experience it.

.. note:: If your course uses randomized content blocks, or if your course is
   designed so that learners in different enrollment track groups or content
   groups are shown different content, you can select an option from the **View
   Course As** dropdown list to see the content that a specific learner sees, or
   that a learner in a specific group sees. For more information, see
   :ref:`Specific Student View` or :ref:`Viewing Cohort Specific Courseware`.


.. _Specific Student View:

=====================
Specific Learner View
=====================

.. note:: This view is available only if your course has started, and only for
   content that has a status of :ref:`Published and Live`.

Specific learner view displays published content in your live course as the
learner that you specify experiences it. When you view the **Progress** page,
the page displays grades and progress for the learner that you have specified.

When you view your course content as **Specific student**, be aware of the
following limitations.

* You cannot view open response assessment problems as a specific learner.

* In courses with randomized content blocks, you see the actual problem that
  was assigned to a specific learner. This view allows you to evaluate a
  request to adjust a grade or reset the number of attempts for a problem. For
  details about adjusting grades or resetting attempts, see
  :ref:`Adjust_grades`.


.. _Student in Content Group View:

=================================
Learner in a Content Group View
=================================

This view displays content as a learner who belongs to the specified content
group would experience it. You can use this view to verify that content
designed for learners in a specific content group is displaying as intended.

For details about content groups, and about creating and previewing cohort-specific
content, see :ref:`About Content Groups`, :ref:`Cohorted Courseware Overview`,
and :ref:`Viewing Cohort Specific Courseware`.

.. _Learner in Enrollment Track Group View:

=========================================
Learner in an Enrollment Track Group View
=========================================

This view displays content as a learner who is in a specific enrollment track
would experience it. You can use this view to verify that content designed for
learners in a specific enrollment track is displaying as intended.

For more information about enrollment track groups, and about creating and
previewing enrollment track based content, see :ref:`About Enrollment Track
Groups and Access` and :ref:`Enrollment Track Specific Courseware Overview`.


