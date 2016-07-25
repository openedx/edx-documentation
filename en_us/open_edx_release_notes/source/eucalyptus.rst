.. _Open edX Eucalyptus Release:

####################################
Open edX Eucalyptus Release
####################################

This page lists the highlights of the Eucalyptus release.

.. contents::
 :depth: 1
 :local:

**************
New Features
**************

The following new features are included in the Open edX Eucalyptus release.

.. contents::
 :depth: 1
 :local:

===================================================
Self-Paced Course Configuration
===================================================

When course teams create a course, they can can now select the way a course is
delivered to learners. You can set a schedule for the course, including due
dates for assignments or exams, or you can allow learners to work at their own
pace. For more information, see :ref:`opencoursestaff:Setting Course Pacing`.

=====
Teams
=====

With the teams feature, a learner can browse topics and then create a team to
take part in group activities within the chosen topic. Teams provide small
group interactions and projects in your course. For more information, see
:ref:`opencoursestaff:CA_Teams_Overview`.

========================
Subsection Prerequisites
========================

Course teams can now control the visibility of subsections based on the scores
that learners earn in other subsections. You can now prevent learners from
viewing content before they earn a minimum score for previous content. For more
information, see :ref:`opencoursestaff:configuring_prerequisite_content`.

=========
Bookmarks
=========

The bookmarks feature allows learners to add a bookmark to any unit in the LMS
so that they can easily find that page later on the **My Bookmarks** page. For
more information, see :ref:`openlearners:SFD Bookmarks`.

=================
Course Navigation
=================

Several changes have been made to the navigation options in the LMS.

* The **Home** page replaces the **Course Info** page. The **Home** page
  appears first among the page navigation options, and opens automatically when
  a learner selects a course on the learner dashboard. This page features
  important course dates in addition to course updates and course handouts.

* **Course** is the new name for the **Courseware** page. This page appears
  after **Home** among the page navigation options.

* Learners can now use the left and right arrow buttons at the ends of the unit
  navigation bar to move to the previous unit or the next unit.

=================================
New Drag and Drop Problem XBlock
=================================

A new mobile-ready, accessible drag and drop problem type is now available.
This version replaces the original drag and drop problem type, which is now
deprecated. For more information, see
:ref:`opencoursestaff:drag_and_drop_problem`.

=======================
Peer Instruction XBlock
=======================

The peer instruction tool emulates the classroom experiences of the Peer
Instruction learning system, which gives students in class opportunities to
discuss questions and arrive at a deeper understanding of concepts. For more
information for course teams, see :ref:`opencoursestaff:UBC Peer Instruction`.
For more information for learners, see
:ref:`openlearners:interactive_multiple_choice`.

****************************
Changes to Analytics Events
****************************

The following analytics events have been added to reflect course navigation
actions in the LMS.

* ``edx.ui.lms.link_clicked``
* ``edx.ui.lms.outline.selected``
* ``edx.ui.lms.sequence.next_selected``
* ``edx.ui.lms.sequence.previous_selected``
* ``edx.ui.lms.sequence.tab_selected``

For more information, see :ref:`data:navigational`.

The following analytics events have been added for the new drag and drop
problem XBlock.

* ``edx.drag_and_drop_v2.feedback.closed``
* ``edx.drag_and_drop_v2.feedback.opened``
* ``edx.drag_and_drop_v2.item.dropped``
* ``edx.drag_and_drop_v2.item.picked_up``
* ``edx.drag_and_drop_v2.loaded``

For more information, see :ref:`data:Drag and Drop Events`.

***********************
Accessibility Updates
***********************

In keeping with edX's commitment to creating accessible content for everyone,
everywhere, the Open edX Eucalyptus release contains numerous accessibility
enhancements and improvements to readability and navigability.

TBD

*********************
Deprecated Features
*********************

Several features are deprecated as of the Open edX Eucalyptus release.

.. contents::
 :depth: 1
 :local:

====================
Deprecated REST APIs
====================

The mobile, course structure, and profile images REST web services are
deprecated.

* Use the ``/api/courses/v1/courses/`` web service instead of the deprecated
  mobile and course structure web services.

* Use the ``/api/user/v1/accounts/`` web service instead of the deprecated
  profile image web service.

For more information about supported and deprecated web services,
see :ref:`openplatformapi:Open edX Platform APIs`.

==============================
Deprecated Tools and XModules
==============================

* The graphical slider tool is no longer available. (:jira:`TNL-3923`)

* The randomize component, a little used tool with provisional support, is now
  deprecated. To provide randomized content, use the supported Content
  Libraries tool to create randomized content blocks. For more information, see
  :ref:`opencoursestaff:Randomized Content Blocks`.

* The crowdsource hinter XModule is no longer available as a course tool. This
  XModule was a prototype version that was not fully supported by edX. It has
  not been used since July 2013.

* The original drag and drop problem type is now deprecated. A new mobile-
  ready, accessible drag and drop problem type is now available.

************************************************
More Information on Eucalyptus Release Changes
************************************************

The `edX Release Notes`_ contain a summary of changes that are deployed to
edx.org. Those changes are part of the master branch of the edX Platform in
GitHub.

You can also find `release announcements`_ on the open.edx.org website. You can
subscribe to have these weekly release announcements sent to your email
account.

Changes listed for 13 July 2016 and before are included in the Eucalyptus
release of Open edX.

.. include:: links.rst
.. include:: ../../links/links.rst

