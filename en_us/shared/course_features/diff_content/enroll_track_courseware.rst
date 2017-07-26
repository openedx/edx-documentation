:orphan:

.. _Enrollment Track Specific Courseware Overview:

#######################################################
Creating Course Content for Specific Enrollment Tracks
#######################################################

This section provides information about creating different content for
learners who are enrolled in specific enrollment tracks in your course.

.. contents::
  :local:
  :depth: 1

*********
Overview
*********

If your course has more than one enrollment track, you can create different
course experiences for learners in each enrollment track. You do this by
designating specific components or units in your course as available only to
learners in one or more of the enrollment tracks. Then, learners in each of the
enrollment tracks see only the course content that you have designated for that
track.

To create track-specific content in your course, follow these steps.

#. :ref:`Specify course content as available only to particular enrollment
   track groups<Specify Content as Available Only to Certain Enrollment Tracks>`

#. :ref:`View components or units that are available for each enrollment track
   group<View Components or Units Available Based on Enrollment Track>`

#. :ref:`Preview track-specific course content<Viewing Track Specific
   Courseware>`


.. _About Enrollment Track Groups and Access:

**************************
Enrollment Track Groups
**************************

If your course offers more than one enrollment track (for example, a track
that does not offer certificates, and a certificate track where learners who
pass the course can earn a certificate), an enrollment track group is
automatically created for each enrollment track. You see these groups in
Studio, on the **Group Configurations** page.

Learners who enroll in your course in a particular enrollment track are
automatically included in the appropriate enrollment track group.

======================================
When Learners Change Enrollment Tracks
======================================

Learners select an enrollment track when they first enroll in a course, and in
many cases they will change enrollment tracks during the course run. For
example, learners might upgrade from the audit track to the verified track.

In a course where you offer differentiated content based on enrollment track,
when learners change tracks during the course run, the content that they see
changes. As soon as they change enrollment tracks, learners see only the
content that you make available to all learners and to their current
enrollment track.

As you design your course using differentiated content based on enrollment
track, be aware of maintaining the continuity of learner grades and experience
when learners change from one enrollment track to another.

.. warning:: If a learner changes enrollment tracks after having completed some
   course content in a different enrollment track, only grades from content
   that was available to all learners are kept and are reflected on the learner's
   **Progress** page.


.. _Specify Content as Available Only to Certain Enrollment Tracks:

******************************************************************
Specify Content as Available Only to Particular Enrollment Tracks
******************************************************************

In Studio, you can modify the settings of units or components to give access
only to learners who are in particular enrollment tracks. You cannot specify
entire subsections or sections for restricted access by enrollment track.

You do not need to edit the access settings of units or components that are
intended for all learners. Units or components that you do not restrict access
to are available to all learners enrolled in your course, regardless of the
enrollment track that they are in.

.. note:: Components inherit any group access restrictions that are set for
   their parent unit. If you set additional group access restrictions for a
   component, make sure the component access settings do not contradict the
   unit access settings. For example, you cannot give Group A of learners
   access to a component if Group A does not have access to the unit that
   contains the component.

For details about how to modify unit access settings, see :ref:`Set Access
Restrictions For a Unit`.

For details about how to modify component access settings, see :ref:`Set Access
Restrictions For a Component`.

For details about previewing your course to ensure that learners in an
enrollment track correctly see the content intended for them, see :ref:`View
Components or Units Available Based on Enrollment Track` and :ref:`Viewing
Track Specific Courseware`.

.. note:: In addition to the access settings for content groups, a learner's
   ability to see a course component also depends on whether it is marked as
   visible to staff only, whether the unit is published, and the course's
   release date. For more information about testing course content in general,
   see :ref:`Testing Your Course Content`.


.. _View Components or Units Available Based on Enrollment Track:

*********************************************************************
View Components or Units That Are Available Based on Enrollment Track
*********************************************************************

To view the components or units that are available to learners in each of the
enrollment tracks in your course, follow these steps.

#. In Studio, select **Settings**, and then select **Group Configurations**.

#. On the **Group Configurations** page, locate the enrollment track group for
   which you want to view the usage. Enrollment track groups are shown on this
   page only if more than one enrollment track exists in the course. Each
   enrollment track group corresponds to an enrollment track.

   The enrollment track group's box displays the number of locations (units or
   components) that are designated for learners in the track.

#. Click the enrollment track name to view the names of units and components
   that are designated for learners in the track.

#. Click a linked location name to go to that unit in the course outline, where
   you can change the group access settings for the unit or component.

For more information about previewing your course to ensure that learners in
an enrollment track correctly see the content intended for them, see
:ref:`Viewing Track Specific Courseware`.


.. _Viewing Track Specific Courseware:

**************************************
Viewing Track-Specific Course Content
**************************************

After you restrict access to components to learners in certain enrollment
tracks, you can view your course content as a learner in each enrollment track
to ensure that learners in each track correctly see the content that is
intended for them.

.. note:: In addition to access settings for content groups, a learner's
   ability to see a course component also depends on whether the component is
   marked as visible to staff only, whether the unit is published, and the
   course's release date. For more information about viewing course content in
   various publishing states, see :ref:`View Published Content` and
   :ref:`Preview Unpublished Content`.

Depending on whether you want to view published content or unpublished content,
you choose either **View Live** or **Preview** from the course outline in
Studio. You can then experience the course content as a learner in a particular
group would, by selecting the **View this course as** option for a learner in
the desired enrollment track, as described in :ref:`Roles for Viewing Course
Content`.

For details see :ref:`Testing Your Course Content` and :ref:`Roles for Viewing
Course Content`.
