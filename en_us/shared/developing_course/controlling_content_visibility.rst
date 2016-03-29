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

You specify release dates and times for sections and subsections. By defining
release dates, you ensure that content is available to learners on a planned
schedule, without requiring manual intervention while the course is running.

By default, a subsection inherits the release date and time of the section it
is in. You can change the release date of the subsection to another date.

Published units are not visible to learners until the scheduled release date
and time. When the section and subsection have different release schedules,
published units are not visible until both dates have passed.

Prior to release, content is visible to course team members by
:ref:`previewing the course <Preview Course Content>` or :ref:`viewing the live
course as staff<View Your Live Course>`.

.. note:: The release times that you set, and the times that learners see,
   are in Coordinated Universal Time (UTC). You might want to verify that you
   have specified the times that you intend by using a time zone converter such
   as `Time and Date Time Zone Converter
   <http://www.timeanddate.com/worldclock/converter.html>`_

For more information about setting release dates, see the following topics.

* :ref:`Set a Section Release Date`
* :ref:`Set a Subsection Release Date`

***********************
Unit Publishing Status
***********************

You publish units to make them visible to learners. Learners see the last
published version of a unit if the section and subsection it is in are
released.

Learners do not see units that have never been published, and they do not see
unpublished changes to units or components within units.  Therefore, you can
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

*****************************
Content Hidden from Learners
*****************************

You can hide content from learners. Such content is never visible to learners,
regardless of the release and publishing status.

You might hide a unit from learners, for example, when that unit contains an
answer to a problem in another unit of that subsection. After the problem's due
date, you could make the unit with the answer visible.

You could also hide a unit from learners if you wanted to use that unit to
provide instructions or guidance meant only for the course team. Only course
team members would see that unit in the course.

You can hide content at different levels, as described in the following topics.

* :ref:`Sections<Hide a Section from Students>`
* :ref:`Subsections<Hide a Subsection from Students>`
* :ref:`Units<Hide a Unit from Students>`

.. note::
 When you make a previously hidden section or subsection visible to learners,
 some content in the section or subsection may remain hidden. If you have
 explicitly set a subsection or unit to be hidden from learners, this
 subsection or unit remains hidden even when you change the visibility of the
 parent section or subsection. Unpublished units remain unpublished, and
 changes to published units remain unpublished.

.. _Hiding Graded Content:

=====================
Hiding Graded Content
=====================

If you hide a section, subsection, or unit that contains graded problems,
grading is not affected. The hidden problems are still counted when the edX
platform calculates grades. If a problem was visible at one time, and learners
submitted answers for it, they still receive the credit they earned if you
later hide the problem.

.. _Content Groups:

**************
Content Groups
**************

If you have cohorts enabled in your course, you can use content groups to
designate  particular components in your course as visible only to specific
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
Enabling Subsection Prerequisites
=================================

To enable prerequisite subsections in a course, follow these steps.

#. From the **Settings** menu, select **Advanced Settings**.

#. In the **Enable Subsection Prerequisites** field, enter ``true``.

#. Select **Save Changes**.

.. _creating_a_prerequisite_subsection:

==================================
Creating a Prerequisite Subsection
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

#. Select the **Access** tab.

#. Select **Use as a Prerequisite** > **Make this subsection
   available as a prerequisite to other content**.

#. Select **Save**.

#. Select the **Configure** icon for the subsection that
   will be hidden until the prerequisite is met.

#. Select the **Access** tab.

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
