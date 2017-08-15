.. _Open edX Ginkgo Release:

#########################
Open edX Ginkgo Release
#########################

This page lists the highlights of the Ginkgo release.

The `edX Release Notes`_ contain a summary of changes that are deployed to
edx.org. Those changes are part of the master branch of the edX Platform in
GitHub. You can also find `release announcements`_ on the open.edx.org
website.

Changes listed for July 7, 2017 and before are included in the Ginkgo release
of Open edX. Changes after that point will be in future Open edX releases.

For information about upgrading an existing Open edX installation from the
Ficus relesae to the Ginkgo release, see :ref:`opencoursestaff:upgrade_ficus`.

.. contents::
 :depth: 1
 :local:

************
New Features
************

The Open edX Ginkgo release includes the following updates.

.. contents::
 :depth: 1
 :local:


===
LMS
===

*  The **Course** page now opens to a course outline that serves as the basis
   for a new course home experience. This course outline features a full-page
   course outline that lists all sections and subsections at once. It replaces
   the course outline sidebar on course content pages that listed sections and
   subsections. It allows learners to focus on content consumption and
   progression through the course. For more information, see
   `Course Navigation Changes`_ on the Open edX portal.

*  The **Course** page now includes breadcrumb navigation that learners can
   select from any course page to return to the course outline.

*  The video player now uses HLS video playback when YouTube videos are not
   available. HLS causes the player to continually check each learner's internet
   connection and adjust video playback, so that learners are always viewing the
   highest quality video possible for their internet connection.

*  Search functionality is available on the **Outline** page.

*  Learners now receive an email when they've submitted a proctored exam that
   lets them know their exam has been received, as well as when to expect scores.
   This email also provides information about whether the learner has passed or
   failed proctoring and why.

*  Learners can now sort inline discussions by most votes, most activity, and
   recent activity.

*  Learner responses for open responsesassessments can now include more than
   one file. The maximum cumulative upload size has been increased to 10 MB.

*  The LMS is compliant with Web Content Accessibility Guidelines (WCAG) 2.0
   level AA. We have made a number of accessibility improvements that, among
   other things, provide easier navigation using keyboards, screen readers,
   or other assistive technology.


===============================
Studio and Course Author Tools
===============================

*  Course teams that use cohorts can now select specific content groups from
   the View this course as option in the LMS to preview content exactly as a
   learner in that content group would see it.

*  Course staff can now send emails to learners based on their enrollment track,
   so you can reach all verified or audit track learners at one time. For more
   information, see :ref:`opencoursestaff:Bulk Email`.

*  Course authors can move components from one location to another in a course.

*  Drag and drop problems can be rescored.

*  The default permissions have been changed so that new Studio users cannot
   author courses unless an admin has added them to the course creator group.

*  The student profile report that is available from the **Data Download**
   page on the instructor dashboard includes two new columns: enrollment mode
   and verification status.

*  The **Video ID** field is now available on the **Basic** tab of a video
   component as well as on the **Advanced** tab.

*  You can upload transcripts for videos that are not hosted on YouTube on the
   **Basic** tab of a video component.

* The problem component for open response assessments has been renamed from
  "Peer Assessment" to "Open Response Assessment."

* The instructor dashboard includes an **Open Response Assessent** tab to help
  locate and access open response assessments and provide data about learner
  progress in completing responses and peer assessments.

* The **Show Results** setting for problems allows course teams to hide
  problem results from learners, including both whether the learner answered
  the problem correctly and the learner's score, either temporarily or
  permanently. Using this feature, course teams can hide exam scores until
  the exam due date, or administer surveys without revealing responses.

=======================
Insights and Analytics
=======================

*  A new **Courses** page in Insights provides a dashboard view of all of your
   courses. For information, see :ref:`insights:Courses_Page`.

*****************
Service Upgrades
*****************

=================
Catalog Service
=================

The Catalog service has been upgraded to RabbitMQ 3.6.9.

=======================
Credentials Service
=======================

The Credentials service now requires Python 3.5.

======================
E-Commerce Service
======================

* The Open edX platform now supports only the integrated Otto
  receipt page. Users can no longer redirect to the ``LMS/shopping_cart``
  receipt page.

* The Open edX platform now supports only the Secure Acceptance
  Silent Order POST integration for CyberSource. To use this integration, users
  must create a new profile in the business center.

* The merchant notifications endpoint has been removed.

* Django Oscar has been upgraded to version 1.4.

* The Course Administration Tool has been updated to use the user account
  associated with the OAuth credentials rather than individual users' accounts.
  The user associated with the OAuth credentials (at edx.org, we use the
  username ``ecommerce_worker``) must  have full create/read/update/delete
  permissions for the following models on LMS.

     * ``commerce.CommerceConfiguration``
     * ``course_modes.CourseMode``
     * ``credit.CreditCourse``
     * ``credit.CreditRequest``

  In addition, if you are using Specially Designated Nationals (SDN) verification,
  this user must have the ``student:userprofile:can_deactivate_users``
  permission.

*******************************
System Upgrades and Updates
*******************************

The Ginkgo release makes version updates to a number of system components.


.. list-table::
   :widths: 60 40
   :header-rows: 1

   * - System
     - Upgraded Version
   * - Catalog Service
     - Django 1.11.x
   * - Credentials Service
     - Django 1.11.x
   * - Django Waffle
     - 0.12.0
   * - E-Commerce Service
     - Django 1.10.x
   * - Search
     - ElasticSearch 1.5
   * - Node
     - Node 6.9
   * - xblock-lti-consumer
     - 1.1.5

* Webpack, a JavaScript module bundler, is now supported in Studio and the LMS.
  See `Webpack`_ for more information.

* ESLint is now used for JavaScript linting. The edX rules are defined in
  https://github.com/edx/eslint-config-edx. Packages are provided for ES5 and
  ES2015+. See `ESLint`_ for more details.


***********************
Deprecated Features
***********************

Several features are deprecated or deleted in the Open edX Ginkgo release.

* The Programs service was deprecated in Ficus. It has been replaced by the Catalog
  service in Ginkgo.
* The Credentials API v2 has replaced the Credentials API v1, which has been
  removed.
* The waffle flag ``unified_course_view``, which can be used for the new view
  of the course outline on a separate page, is deprecated in Ginkgo.  The old
  sidebar navigation and this waffle flag will be fully removed in the next
  release.


.. include:: links.rst
.. include:: ../../links/links.rst
