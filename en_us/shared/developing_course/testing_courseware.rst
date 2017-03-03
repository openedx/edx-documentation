.. _Testing Your Course Content:

###########################
Testing Your Course Content
###########################

The way your course looks in Studio is different from the way that learners
will see and experience it when it is live in the LMS.

The method that you choose for experiencing the course content as a learner
depends on the publishing status of the content.

* For published and released content, use :ref:`View Live<View Published
  Content>`.

* For draft and unreleased content, use :ref:`Preview<Preview Unpublished
  Content>`.

For more information, see the following topics.

.. contents::
  :local:
  :depth: 2

.. note:: If you use content groups in your course to designate content as
  visible only to particular students, see :ref:`Preview Cohort Specific
  Courseware`.

For information about setting up a beta test for your course, see
:ref:`Beta_Testing`.

.. _Preview Course Content:

*************************
Preview Course Content
*************************

You can preview course content before the course is live, or before you publish
specific units in a live course, to test how content will appear to students
when it is released.

When you preview course content, you see the latest course content that is
configured in Studio. You see content in units with the publishing status
:ref:`Draft (Never Published)`, :ref:`Draft (Unpublished Changes)`, or
:ref:`Visible to Staff Only`.

* You do not see units that are in :ref:`Draft (Never Published)` status. To
  see these units, you must use Preview mode, as described in :ref:`Preview
  Unpublished Content`.

.. note:: If you use randomized content blocks in your course, you cannot
   preview unpublished units that contain content from randomized content
   blocks, because the randomized content is not assigned until after the unit
   is published. For information about viewing the actual content that has
   been assigned to a particular student from a randomized content block in a
   live course, see :ref:`Specific Student View`.

For example, you :ref:`publish a unit<Publish a Unit>` that includes a video
component and a discussion component.

.. image:: ../../../shared/images/test-unit-studio.png
 :alt: A unit in Studio with video and discussion components.
 :width: 600

Students see the same content in the LMS.

.. image:: ../../../shared/images/test-unit-lms.png
 :alt: The unit in the LMS.
 :width: 600

You later decide to add a knowledge check problem to the unit, between the
video and the discussion. Before you publish this change, you can see how the
question will look to students by previewing the unit in the LMS.

When you select **Preview** and select to view the course as a **Student**, you
see the unit in the LMS with the multiple choice question. This preview shows
how students will experience the unit after you :ref:`publish the
change<Publish a Unit>`.

.. I am getting different results. If the content is not published, I can Preview, but if I change to student view I get thrown out of the course. I think that the "View As" control in LMS is not useful with Preview, only with View Live. Opened DOC-2825  Alison 27 Mar 2016

.. image:: ../../../shared/images/test-unit-lms-added-comp.png
 :alt: The unit in the LMS, showing a video, a problem, and a discussion
  component.
 :width: 600

In the live course, students continue to see the existing content, without the
multiple choice question, until you :ref:`publish the change<Publish a Unit>`.

.. note:: When the unit's state is :ref:`Published and Live`, the preview and
   the live version of the course are exactly the same. Selecting either
   of **View Live** or **Preview** gives you the same view.



.. _View Your Live Course:

******************************************
View Your Live Course
******************************************

While you are working in Studio, you can test your live course by viewing it in
the LMS as all students, or a particular student, would see it. You can see
your course in :ref:`Staff View`, :ref:`Student View`, or :ref:`Specific
Student View`. If you are using content groups to designate specific content as
visible only to particular content groups, you can see your course as a content
group would see it.

You can view the course as a member of these groups.

.. list-table::
    :widths: 15 30
    :header-rows: 1

    * - Role
      - When You "View As" This Role
    * - Staff
      - You see all content in the course, including content that is hidden
        from students.
    * - Student
      - You see any content that is intended for all students.
    * - Specific Student
      - You see content that is intended for the student whose email or
        username you specify.
    * - Student in <Content Group Name>
      - You see content that is intended for all students, as well as any
        content specifically set to be visible to this content group.

To switch to your live course and see how it appears to members of the groups
in the table above, follow these steps.

#. From the Studio **Course Outline** page, select **View Live**.
   Alternatively, from a unit page, select **View Live Version**.

   A separate browser tab opens for the course in the LMS.

#. In the LMS, select one of the **View this course as** options, as described
   in the table above.

The course view refreshes to present course content as a member of the selected
group would see it.

For details about each view, see :ref:`Staff View`, :ref:`Student View`, or
:ref:`Specific Student View`.


.. _Staff View:

=================
Staff View
=================

To view your live course as any member of the course team would see it, follow
these steps.

#. Open the course in the LMS.
#. At the top of any page, next to **View this course as**, select **Staff**.

* You see all units that are :ref:`Published and Live`. For units that are
  :ref:`Draft (Unpublished Changes)` or :ref:`Visible to Staff Only`, you
  see the last published version of the unit. You see these units
  regardless of the release dates of the containing section or subsection.

* You do not see units that are :ref:`Draft (Never Published)`. To
  see these units, you must use Preview mode as described in :ref:`Preview
  Course Content`.

* You can select **Instructor** to access the instructor dashboard, which has
  options and reports that help you :ref:`run your course<Managing Live Course
  Index>`.

When you view your course in **Staff View**, you can execute tests to make sure
that your course works the way you intend. For example,  before the release
date of a subsection, members of the course team can work through the problems
to verify that the correct answer gets a green check for correct, and that any
answer other than the correct one gets a red X for incorrect.

.. _Student View:

============
Student View
============

To view your live course as learners see it, follow these steps.

#. Open the course in the LMS.
#. At the top of any page, next to **View this course as**, select **Student**.

.. note::
  If your course has not started, you cannot see the content on the **Course**
  page when you use the **Student** view. To see this content before the course
  has started, add yourself as a beta tester on the instructor dashboard. Make
  sure to set the course start date and the **Days Early for Beta** setting so
  that you can see the content that you want. For more information, see
  :ref:`Beta_Testing`.

.. note:: If you have enabled your course for cohorts and have designated some
  content as visible only to certain content groups, you can select a content
  group from the **View Course As** dropdown list to see the content exactly
  as a student in a cohort associated with that content group will see it. For
  more information, see :ref:`Preview Cohort Specific Courseware`.

When you view content as a student, be aware of the following limitations.

* You do not see sections or subsections that have not yet been released.

* If the section and subsection are released, you see units that are
  :ref:`Published and Live`. For units that are :ref:`Draft (Unpublished
  Changes)`, you see the last published version of the unit.

* You do not see units that are :ref:`Draft (Never Published)` or
  :ref:`Visible to Staff Only`. To see these units, you must switch back to
  Instructor view or use Preview mode as described in :ref:`Preview Course
  Content`.

.. _Specific Student View:

=====================
Specific Student View
=====================

.. note::
  If your course has not started, you cannot see the content on the **Course**
  page when you use the **Specific student** view. To see this content before
  the course has started, add yourself as a beta tester on the Instructor
  Dashboard. Make sure to set the course start date and the **Days Early for
  Beta** setting so that you can see the content that you want. For more
  information, see :ref:`Beta_Testing`.

In the LMS, to view your live course as one particular learner sees it, select
**Specific student** from the **View this course as** list. Then, enter that
learner's username or email address.

When you view content as a specific student, be aware of the following
limitations.

* In courses with randomized content blocks, you see the actual problem that
  was assigned to a specific learner. This view allows you to evaluate a
  request to adjust a grade or reset the number of attempts for a problem. For
  details about adjusting grades or resetting attempts, see
  :ref:`Adjust_grades`.

* You cannot view open response assessment problems as a specific student.

* You do not see sections or subsections that have not yet been released.

* If the section and subsection are released, you see units that are
  :ref:`Published and Live`. For units that are
  :ref:`Draft (Unpublished Changes)`, you see the last published version of the
  unit.

* You do not see units that are :ref:`Draft (Never Published)` or
  :ref:`Visible to Staff Only`. To see these units, you must switch back to
  Staff view or use Preview mode as described in :ref:`Preview Course Content`.


*************************************
Open Studio from Your Live Course
*************************************

When you are viewing your course in the LMS as **Staff View**, you can open
Studio directly.

* On a unit page, select **View Unit in Studio**.

  The unit page opens in Studio.

* After you select **Instructor** to access the instructor dashboard, select
  **View Course in Studio** to open the course outline in Studio.

  For information about the tasks you can complete from the instructor
  dashboard, see :ref:`Managing Live Course Index`.

* Select the **Progress** page, and then select **View Grading in Studio** to
  open the **Grading** page in Studio.

  For information about checking a student's progress, see
  :ref:`Review_grades`.
