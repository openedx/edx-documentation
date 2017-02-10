.. _Open edX Ficus Release:

######################
Open edX Ficus Release
######################

This page lists the highlights of the Ficus release.

.. contents::
 :depth: 1
 :local:

************
New Features
************

The Open edX Ficus release includes the following updates.

.. contents::
 :depth: 1
 :local:

LMS
===

* New **Next** and **Previous** buttons allow learners to navigate more
  intuitively through courses.

* The **Progress** page loads significantly faster.

* For course problems, the **Check** and **Final Check** buttons are now
  combined in one **Submit** button, and less frequently used actions (such as
  **Save** and **Show Answer**) have been moved to the side. 

* Learners can quickly see whether problems are graded or ungraded.

Discussions
===========

* A post listing view that shows not only post titles, but also the first line
  of each post, is now available on the **Discussions** and **Teams** pages and
  in inline discussions.

* Improvements to the discussions UI: added learner profile pictures to
  discussion posts, a new header area, a more intuitive topic list, and an
  enhanced UI that indicates unread posts, comments, and responses. You can
  also now sort discussions by votes

Studio & Course Author Tools
============================

* Course teams can easily copy and move HTML components in Studio. 

* For rescoring, course teams can now specify that the system will only update
  a learner's score if the process improves the learner's score. For more
  information, see :ref:`opencoursestaff:rescore`.

* CAPA problems now allow HTML formatting. See the following documentation for
  more information about specific functionality:

  * :ref:`opencoursestaff:Multiple Responses in Numerical Input Problems` for
    numerical input problems.

  * :ref:`opencoursestaff:Using the Script Element in Multiple Choice Problems`
    for multiple choice problems.

  * :ref:`opencoursestaff:Using the Script Element in Checkbox Problems` for
    checkbox problems.

* Randomized content block components no longer have the unused Scored field.
  Because grading is set at the subsection level, this action won't affect your
  course. See :ref:`opencoursestaff:Randomized Content Blocks` for more
  information.

* Course teams can create custom pages that only course team members with the
  Staff or Admin role can see.  See :ref:`opencoursestaff:Add Page` for more
  information.

* In open response assessment (ORA) problems, course teams can override the
  grades from peer assessments. For more information, see
  :ref:`opencoursestaff:Override a learner assessment grade`.

* Improvements to the word cloud tool include a new Instructions field and
  accessibility updates.

* In drag and drop problems, course authors can prevent learners from receiving
  feedback until they've dropped all draggable items.

* Added the ability to view a course as a member of a content group.

* In the Student Profile report, added two columns: "enrollment mode" and
  "verification status".


***************************************************
Updates to Analytics Events and Database Tables
***************************************************

* Insights now offers per-learner data and a new "Participated in Discussions
  Last Week" metric.

* Five grading events have been added: 

  * edx.grades.problem.submitted

  * edx.grades.problem.rescored

  * edx.grades.problem.state_deleted

  * edx.grades.subsection.grade_calculated

  * edx.grades.course.grade_calculated



***********************
Accessibility Updates
***********************

In keeping with edX's commitment to creating accessible content for everyone,
everywhere, the Open edX Ficus release contains numerous accessibility
enhancements and improvements to readability and navigability.

.. contents::
 :depth: 1
 :local:

* Improved video player controls make downloading videos, transcripts, and
  handouts easier.

* For learners who use screen readers or keyboards only, core CAPA problem
  types, including checkbox and text input problems, have been updated to make
  identifying and responding to these problems easier.

* Navigating among questions and reviewing survey results easier in the survey
  tool is now easier.

* The contrast has been increased on the sign-in page for Open edX sites.

* In Insights, the <title> element on learner pages now indicates the correct
  view when you switch between learner roster view and learner view.

* Reorganized the HTML structure of the Progress page to be more accessible.

* The course Home page now uses heading levels 1-5 in a way that screen readers
  can more easily process.

* For custom JavaScript problems, the jsinput tag includes a title attribute
  that helps orient non-visual learners.

* The video playback and volume sliders are now visible when learners view
  videos in high contrast mode.

* Made the visual chart on the Progress page more accessible to learners who
  use keyboards and screen readers.



*******************************
System Upgrades and Updates
*******************************

* Administrators can now configure third party authentication differently for
  each of their sites. 

* With Ficus, the operating system for the Open edX platform changes from
  Ubuntu 12.04 to Ubuntu 16.04, the latest long-term support (LTS) version of
  Ubuntu.  Ubuntu 12.04 reaches its end of life in April of this year.
  Unfortunately, upgrading Open edX from Ubuntu 12.04 to Ubunbu 16.04 is not
  possible. If your existing installation of Open edX is based on Ubuntu 12.04,
  we recommend that you build a new system.


.. 
    commented out until we need it...

    *********************
    Deprecated Features
    *********************

    Several features are deprecated, or deleted, by the Open edX Ficus
    release.

    .. contents::
     :depth: 1
     :local:

    TBD


************************************************
More Information on Ficus Release Changes
************************************************

The `edX Release Notes`_ contain a summary of changes that are deployed to
edx.org. Those changes are part of the master branch of the edX Platform in
GitHub.  You can also find `release announcements`_ on the open.edx.org
website.

Changes listed for 10 January 2017 and before are included in the Ficus release
of Open edX.  Changes after that point will be in future Open edX releases.


.. 
    commented out until we need it...

    **************
    Patch Releases
    **************

    ==============================
    2 September 2016: Eucalyptus.2
    ==============================

    * bullet list of the changes...

.. include:: links.rst
.. include:: ../../links/links.rst
