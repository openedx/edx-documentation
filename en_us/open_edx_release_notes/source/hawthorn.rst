.. _Open edX Hawthorn Release:

#########################
Open edX Hawthorn Release
#########################

This page lists the highlights of the Hawthorn release of the Open edX platform.

The `edX Release Notes`_ contain a summary of changes that are deployed to
edx.org. Those changes are part of the master branch of the edX Platform in
GitHub. You can also find `release announcements`_ on the open.edx.org
website.

Changes listed for July 6, 2018 and before are included in the Hawthorn release
of Open edX. Changes after that point will be in future Open edX releases.

.. contents::
 :depth: 1
 :local:

*************************
New and Improved Features
*************************

The Open edX Hawthorn release includes the following updates.

.. contents::
 :depth: 1
 :local:


========================
LMS and Learner Features
========================

* We’ve enhanced the learner profiles so that they now include the date a
  learner joined the platform and any course credentials they have received.
  This links to social media accounts and helps learners share information with
  one another. 
* Learners now have the ability to purchase all the courses in a
  program in just one transaction. This avoids the hassle of having to enter
  payment information multiple times.
* New discussion notifications now send an email message the first time a 
  learner's post receives a comment. The message contains the comment and a 
  link back to the course discussions for easy access. Inline discussions are 
  expanded by default. This change has led to a threefold increase in 
  discussion participation on edx.org.​


===============================
Studio and Course Author Tools
===============================

* Course teams now have the ability to override learner scores for individual 
  problems. This can be done through a setting on both the instructor dashboard 
  and the Staff Debug viewer.
* Course Reviews can now be viewed and added by learners from within the course 
  experience. Open edX system administrators can configure a reviews provider 
  such as CourseTalk to allows learners to leave reviews for a particular course.
* Proctored exams have been improved, enabling course teams to add specific exam 
  instructions in the Studio proctored exam settings.
* The Files & Uploads page has been updated to significantly simplify the 
  experience of adding all types of files to a course. This includes the 
  ability to search and a Hide File Preview option.
* The ORA problem editor has been improved. A new interface offers the same 
  formatting options for the prompt that are available for HTML components. 
  You no longer have to create a separate HTML component above the ORA 
  assignment.
* Weekly course highlight messages can now be sent to encourage learners to 
  remain engaged with self-paced courses. Specify a few highlights for each 
  course section, and the platform sends out a weekly email message that lists 
  these highlights. Courses on edx.org that enabled weekly highlights had 
  higher verification rates than ones without.
* The HTML components have been updated to give you even more easy formatting 
  options such as aligning your text the way you want: aligned to the left or 
  right, centered, or fully justified. Images to HTML components can be added 
  right inside the HTML component itself, without having to upload files 
  beforehand.
* The Video Uploads page is enabled by default. For course teams who partner 
  with 3Play Media and cielo24, transcripts (including translations of 
  transcripts) are added to Studio automatically.​
* You can establish a password policy to require a minimum strength and 
  complexity for passwords. For more information, see `Password Policy`_


*******************************
System Upgrades and Updates
*******************************

The Hawthorn release makes version updates to a number of system components.

.. list-table::
   :widths: 60 40
   :header-rows: 1

   * - System
     - Upgraded Version
   * - edxapp
     - Django 1.11.x
   * - Mongo
     - Mongo 3.2
   * - Search
     - ElasticSearch 1.5
   * - Node
     - Node 8
   * - xblock-lti-consumer
     - 1.1.5
   * - Queueing
     - Redis replaces Rabbit


***********************
Deprecated Features
***********************

Several features are deprecated or deleted in the Open edX Hawthorn release.

* The waffle flag ``unified_course_view``, which can be used for the new view
  of the course outline on a separate page, was deprecated in Ginkgo.  The old
  sidebar navigation and this waffle flag will be fully removed in the next
  release. We recommend switching this flag to ``True``, so that you will not
  experience any change with the next release.
* ``django-simple-history`` has been deprecated and removed.
* The ``LogoutViewConfiguration`` model has been removed. Single logout is now 
  permanently enabled. This meants that logging out of the LMS or an IDA logs 
  you out of all systems.


.. include:: links.rst
.. include:: ../../links/links.rst
