.. _Controlling Content Visibility:

###################################
Controlling Content Visibility
###################################

As a member of the course team, you must carefully control which content is
visible to learners and when.

You control content visibility through these features in Studio.

.. contents::
  :local:
  :depth: 1

These features work together to control content visibility for learners.


.. _Release Dates:

***********************
Release Dates
***********************

In instructor-paced courses, you can specify release dates and times for
sections and subsections. By defining release dates, you ensure that course
content is available to learners on a planned schedule, without requiring
manual intervention while the course is running.

.. note:: Self-paced courses do not have release dates for sections and
  subsections. For more information about instructor-paced and self-paced
  courses, see :ref:`Setting Course Pacing`.

By default, a subsection inherits the release date and time of the section it
is in. You can change the release date of the subsection to another date.

Published units are not visible to learners until the scheduled release date
and time. When the section and subsection have different release schedules,
published units are not visible until both dates have passed.

Course team members can access content that has not been released by
:ref:`previewing the course <Preview Unpublished Content>`.

.. note::
   When you set release times in Studio, times are in Coordinated Universal
   Time (UTC). You might want to verify that you have specified the times that
   you intend by using a time zone converter such as `Time and Date Time Zone
   Converter <http://www.timeanddate.com/worldclock/converter.html>`_.

   Learners who have specified a time zone in their account settings see course
   dates and times converted to their specified time zone. Learners who have
   not specified a time zone in their account settings see course dates and
   times on their dashboards, in the body of the course, and on their
   **Progress** pages in the time zone that their browsers specify. Learners
   see other course dates and times in UTC.

For more information about setting release dates in an instructor-paced course,
see the following topics.

* :ref:`Set a Section Release Date`
* :ref:`Set a Subsection Release Date`

***********************
Unit Publishing Status
***********************

You publish units to make them visible to learners. In both instructor-paced
and self-paced courses, units must be published to be visible to learners.
Learners see the last published version of a unit if the section and subsection
it is in are released.

Learners do not see units that have never been published, and they do not see
unpublished changes to units or components within units. Therefore, you can
make changes to units in released subsections without disrupting the learner
experience.

For more information, see :ref:`Unit Publishing Status`.

You can publish all changes in a section or subsection at once, or publish
changes to individual units. For more information about publishing units, see
the following topics.

* :ref:`Publish all Units in a Section`
* :ref:`Publish all Units in a Subsection`
* :ref:`Publish a Unit`


.. _Content Hidden from Students:

*******************
Visibility Settings
*******************

You can use the visibility controls in Studio to hide content from learners in
both instructor-paced and self-paced courses.

You might choose to hide a unit from learners, for example, when that unit
contains an answer to a problem in another unit in the same subsection. After
the problem's due date, you can make the unit that contains the answer
visible. You might also permanently hide a unit from learners if that unit
provides instructions or guidance that is intended only for the course team.
Only course team members would see that unit in the course.

Content that is hidden by being excluded from the course outline is never
available to learners, regardless of the release and publishing status.

.. important:: Content that you make "invisible" to learners by excluding it
   from the course outline is also excluded from grading. As a best practice,
   do not hide sections, subsections, or units that contain graded content by
   excluding them from the course outline.

   Instead, if you want to prevent learners from accessing graded content at
   certain times, you can use options to hide content based on due date or
   course end date. For more information, see :ref:`Hiding Graded Content` and
   :ref:`Hide a Subsection After its Due Date`.

You can hide content at different levels, as described in the following topics.

* :ref:`Sections<Hide a Section from Students>`
* :ref:`Subsections<Hide a Subsection from Students>`
* :ref:`Units<Hide a Unit from Students>`

.. note:: Units and subsections inherit visibility settings from their parent
   subsections or sections. Be aware that when you make a previously hidden
   section or subsection visible to learners, all child subsections or units
   also become visible, unless you have explicitly hidden the subsection or
   unit. Subsections or units that are explicitly hidden remain hidden
   even when you change the visibility of their parent section or subsection.


.. _Hiding Graded Content:

=====================
Hiding Graded Content
=====================

Grading is affected if you hide sections, subsections, or units that contain
graded problems in such a way that they are not included in the course
navigation. When the platform performs grading for a learner, the grading
process does not include problems that are not included in that learner's
course outline.

.. note:: As a best practice, do not hide graded sections, subsections, or
   units by excluding them from the course outline. Content that is hidden in
   this way is not included when the platform performs grading for learners.

   Instead, if you want to prevent learners from accessing the content of a
   subsection while the subsection itself remains visible in the course
   navigation, you can use the option to hide a subsection or timed exam's
   content based on date. In instructor-led courses, you can hide a subsection
   based on its due date. In self-paced courses, you can hide a subsection
   based on the course's end date. For more details, see :ref:`Hide a
   Subsection After its Due Date`.


.. _Content Groups:

**************
Content Groups
**************

If you have cohorts enabled in your course, you can use content groups to
designate particular components in your course as visible only to specific
groups of learners.

For details, see :ref:`About Content Groups` and :ref:`Cohorted Courseware
Overview`.

.. _configuring_prerequisite_content:

*******************************************
Configuring Prerequisite Course Subsections
*******************************************

You can hide subsections of your course until learners complete other,
prerequisite subsections. If a subsection has a prerequisite, it is not
visible in the course navigation unless a learner has earned a minimum score in
the prerequisite subsection.

.. _enabling_subsection_gating:

=================================
Enable Subsection Prerequisites
=================================

To enable prerequisite subsections in a course, follow these steps.

#. From the **Settings** menu, select **Advanced Settings**.

#. In the **Enable Subsection Prerequisites** field, enter ``true``.

#. Select **Save Changes**.

.. _creating_a_prerequisite_subsection:

==================================
Create a Prerequisite Subsection
==================================

To prevent learners from seeing a subsection of your course until they have
earned a minimum score in a prerequisite subsection, follow these steps.

.. note::
    Make sure that you configure subsection prerequisites in the order that you
    intend for learners to encounter them in the course content. The
    prerequisite configuration controls do not prevent you from creating a
    circular chain of prerequisites that will permanently hide them from
    learners.

#. Enable subsection prerequisites for your course. For more information, see
   :ref:`enabling_subsection_gating`.

#. Select the **Configure** icon for the subsection that must be completed
   first. This is the prerequisite subsection.

   .. image:: ../../../shared/images/subsections-settings-icon.png
     :alt: A subsection in the course outline with the configure icon
      indicated.
     :width: 600

#. Select the **Advanced** tab.

#. Select **Use as a Prerequisite** > **Make this subsection
   available as a prerequisite to other content**.

#. Select **Save**.

#. Select the **Configure** icon for the subsection that
   will be hidden until the prerequisite is met.

#. Select the **Advanced** tab.

#. In the **Limit Access** > **Prerequisite** menu, select the name of the
   subsection you want to specify as the prerequisite.

#. Enter the percent of the total score that learners must earn in the
   **Minimum Score** field. A learner's score for all problems in the
   prerequisite subsection must be equal to or greater than this percentage in
   order to satisfy the prerequisite and display the current subsection.

   For example, if the prerequisite subsection includes four problems and each
   problem is worth the same number of points, set the **Minimum Score** to
   ``75`` to require at least three correct answers.

#. Select **Save**.

#. In the course outline, if a subsection has a prerequisite, the prerequisite
   name appears under the subsection name.

  .. note:: Prerequisite course subsection settings are not retained when
     you :ref:`export or import a course<Exporting and Importing a Course>`, or when you :ref:`re-run a course<Rerun a Course>`.
