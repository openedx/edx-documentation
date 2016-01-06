.. _Open edX Cypress Release:

####################################
Open edX Cypress Release
####################################

This page lists the highlights of the Cypress release.

.. note::
 With the :ref:`Open edX Dogwood Release`, the Cypress release is no longer
 supported. This page remains in these release notes as a record of when new
 features were included in Open edX.

.. contents::
 :depth: 1
 :local:

**************
New Features
**************

The following new features are included in the Open edX Cypress release.

.. contents::
 :depth: 1
 :local:

=========
Badges
=========

Badges provide a way for learners to share their course achievements. For
courses that have badges enabled, learners receive a badge when they receive a
course certificate, and have the option of sharing their badges to a badging
site such as Mozilla Backpack.

Open edX supports Open Badges, an open standard originally developed by the
Mozilla Foundation. For more information about Open Badges, see
http://openbadges.org/.

For more information, see the following documentation.

* For information about enabling badges on your instance of Open edX, see
  `Enabling Badges`_ in *Installing, Configuring, and Running the Open edX
  Platform*.

* For information about setting up a course for learners to receive badges, see
  `Enable or Disable Badges for Your Course`_ in *Building and Running an Open
  edX Course*.

* For information about badges for learners, see `Upload a Badge to Mozilla
  Backpack`_ in the *Open edX Learner's Guide*.

=========
Cohorts
=========

Course teams now create and manage cohorts on the Instructor Dashboard in the
LMS, instead of on the **Advanced Settings** page in Studio. Course teams can
use the new Cohorts page there to add and rename cohorts, change a cohort's
assignment method, associate cohorts with content groups, and specify whether
course-wide and content-specific discussions are divided by cohort.

For more information, see `Including Learner Cohorts`_ in *Building and Running
an Open edX Course*.

==========================
Course Certificates
==========================

You can now create one certificate configuration per course. This configuration
serves as the template for certificates issued for all of the enrollment tracks
available for your course (such as "honor code" or "verified"). Honor code
certificates use the organization logo and signatory information, but do not
include signature images, which are used only for verified certificates.

For more information, see `Setting Up Course Certificates`_ in *Building and
Running an Open edX Course*.

==========================
Course Search
==========================

Learners can now search much of the content of your Open edX courses, including
the course title, description, text, and video transcripts. Learners can search
for a term in an individual course, or for that term in all of the courses in
which they are enrolled, whether the course is active or archived.

When the search engine returns results, either for an individual course or
across all courses, you can select any search result to view that result in the
courseware.

For more information, see the following documentation.

* For information about enabling course search on your instance of Open edX,
  see `Enable Course Search`_ in *Installing, Configuring, and Running the Open
  edX Platform*.

* For information about setting up a course for learners to be able to search
  its content, see `Course Search`_ in *Building and Running an Open edX
  Course*.

* For information about searching courses for learners, see `Searching the
  Course`_ in the *Open edX Learner's Guide*.

=====================
Creative Commons
=====================

Course teams can now specify either "All Rights Reserved" or a Creative Commons
license for a course. Course teams can also select different license options
for each video.

For more information, see the following documentation.

* For information about configuring your Open edX instance, see `Enabling
  Course and Video Licensing`_ in *Installing, Configuring, and Running the
  Open edX Platform*.

* For information about licensing course content, see `Licensing a Course`_ in
  *Building and Running an Open edX Course*.

* For information about licensing for learners, see `Course and Video
  Licenses`_ in the *Open edX Learner's Guide*.

=====================
Custom Courses
=====================

Course teams can create a custom course experience (CCX) to reuse
course content. By using a CCX, course teams can run some or all of an existing
course for a group of students on a new schedule.

For information about enabling CCX in your instance, see `Enabling Custom
Courses`_ in *Installing, Configuring, and Running the Open edX Platform*.

For information about using CCX, see `Creating a Custom Course`_ in *Building
and Running an Open edX Course*.

====================================================
Grade Report Enhancements
====================================================

The grade report now includes new columns with certificate status and
enrollment track information. When course teams generate the grade report from
the Instructor Dashboard, they can see the following additional information for
each learner.

* Enrollment track, to identify the learner's enrollment mode as honor,
  verified, or professional education.

* Verification status, to identify learners in the verified or professional
  track who have completed identity verification with edX.

* Certificate eligibility status, to identify learners who have earned the
  passing grade in the course at the time of the grade report generation.

* Certificate delivery status, to identify learners who have received their
  certificates. 

* The type of certificate, for learners who are eligible to receive a
  certificate.

For more information, see `Interpret the Grade Report`_ in *Building and
Running an Open edX Course*.

======================================
Feedback and Hints in Common Problems
======================================

Course teams can now add feedback, hints, or both to the following problem
types.

* Checkbox
* Dropdown
* Multiple choice
* Numerical input
* Text input

In Studio, course teams can use new templates to add sample problems that use
the feedback and hint syntax.

For more information, see `Adding Feedback and Hints to a Problem`_ in
*Building and Running an Open edX Course*.

==========================
HTML Spell Check in Studio
==========================

When you edit an HTML component in Studio, an automated spell checker indicates
any misspelled words. The spell checker automatically uses the dictionary that
is set for your browser.

=====================
Learner Profiles
=====================

With the new Open edX Learner Profile feature, course teams and learners can
share information about themselves with the community. The profile can include
an image that identifies the user on the Open edX site as well as the
user's location and other biographical information. Course teams and other
learners in the course can view others' profiles.

For more information, see `Exploring the Profile Page`_ in *Building and
Running an Open edX Course* and `Exploring the Profile Page for Learners`_ in
the *Open edX Learner's Guide*.

=============
LTI Provider
=============

New options that leverage learning tools interoperability (LTI) are available
in this release.

Previously, course teams could use Studio as a tool consumer: course teams
could set up an LTI component to embed external tools, such as learning
applications and textbooks, into an edX course.

Now, course teams can identify content from their edX courses to embed with
other content on their campus systems. Teams can specify the course units,
videos, and graded and ungraded problems that already exist in an edX course
for launch within a campus LMS such as Blackboard or Canvas. Student scores for
graded content are transferred to the campus system.

Authentication between the campus system and the edX system that provides the
content can be configured either to anonymously provision students or to prompt
for account creation.

==========================
New Studio Templates
==========================

This release includes new templates for HTML and problem components. These
templates provide updated guidelines and examples, accessibility information,
and links to documentation.

======================================================
Original Open Response Assessment Problems Deprecated
======================================================

When you access a course that contains an open response assessment created
using the original version of this assignment type (ORA 1), Studio now displays
the message, “This course uses features that are no longer supported.”

A newer version of the open response assessments feature (ORA 2) was released
over a year ago, and the ability to add ORA 1 problems was removed from Studio
in May 2014.

For information about adding ORA 2 problems to a course, see `Open Response
Assessments`_.

=====================
Poll and Survey Tools
=====================

Course teams can now include two new types of components in courses.

* Use the Poll tool to pose a question to learners and have them select an
  answer from a set list.

  For more information, see `Poll Tool`_ in *Building and Running an Open edX
  Course*.

* Use the Survey tool to pose multiple questions to learners and have them
  select an answer for each question from a set list.

  For more information, see `Survey Tool`_ in *Building and Running an Open edX
  Course*.

When polls and surveys are included in a course, course teams can analyze the
responses and also choose whether to let learners see the aggregate answers for
the class.

======================================
Problem Appearance Changes
======================================

To make the Open edX LMS easier to use on mobile devices, the appearance of
common problem types has changed. For example, a border surrounds options for
multiple choice and checkbox problems, and the entire area within the border is
selectable, making it easier for learners to select an option.

==========================
Problem Grade Report
==========================

For any course, course teams can now calculate grades for problems and generate
a report that can be downloaded from the Instructor Dashboard. This new report
includes, for each graded problem, a learner's earned and possible points, and
her total score, expressed as a decimal.

For more information, see `Generate a Problem Grade Report for Enrolled
Students`_ in *Building and Running an Open edX Course*.

==========================
Randomized Content Blocks
==========================

Course teams can now include a new type of component, a randomized content
block, in their courses. These components randomly draw problems from a
predefined library of components and present them to learners.

Course teams create and maintain libraries of components separately from
courses. All of an organization's course teams can work collaboratively to
develop the problems that the libraries contain. Each library can then be
referenced by randomized content blocks in any of that organization's courses.

For more information, see `Working with Libraries`_ in *Building and Running an
Open edX Course*.

====================================================
Report of Not-Yet Enrolled Students
====================================================

Course teams for invitation-only courses can now track enrollment status from
the Instructor Dashboard. The Data Download page of the Instructor Dashboard
now includes a downloadable report of learners who have been invited to enroll
in a course, but who have not yet done so.

For more information, see the `Enrollment`_ section in *Building and Running an
Open edX Course*.

======================================
Third Party Authentication
======================================

To enhance sign in options for your users, you can enable third party
authentication between institutional authentication systems and your
implementation of Open edX. After you enable third party authentication and
integrate with SAML or OAuth2 identity providers, users can register and sign
in to your Open edX site with their campus or institutional credentials.

For more information, see `Enabling Third Party Authentication`_ in
*Installing, Configuring, and Running the Open edX Platform*.

===================================================
Uploading ORA2 Files to Alternative Storage Systems
===================================================

By default, the Open Response Assessment (ORA2) application stores files that
learners upload in an Amazon S3 bucket.

With the Cypress release, you can configure ORA2 to store files in an alternate
system. To have learners' files stored in a system other than Amazon S3, you
must complete the following steps.

#. Implement the ``BaseBackend`` class defined in the `base.py`_ file. 

   For example, the `S3.py`_ file in the same directory is an implementation of
   ``BaseBackend`` for Amazon S3. You must implement the equivalent class for
   the storage system you intend to use.

#. Configure ORA2 to use your alternative storage system by modifying the value
   of ``backend_setting`` in `init file`_
   to point to your implementation of ``BaseBackend``.

#. Add code to instantiate the new implementation to the `get_backend()``
   function in the ``init.py`` file.

#. Configure ORA2 to use the alternative storage system by modifying the value
   of ``ORA2_FILEUPLOAD_BACKEND`` in the Django settings to point to your
   implementation of ``BaseBackend``.

==========================================
YouTube API 3.0 API Key
==========================================

The Open edX Platform uses `Version 3 of the YouTube API`_, which requires that
the application use an API key.

If you intend for courses on your Open edX instance to include videos that are
hosted on YouTube, you must get a YouTube API key and set the key in the Open
edX Platform.

For more information, see `Set YouTube API Key`_ in *Installing, Configuring,
and Running the Open edX Platform*.

*****************
REST API Changes
*****************

EdX has built and published documentation for the following REST APIs, which
are available in the Open edX Cypress release.

* `Course Structure API Version 0`_

* `User API Version 1.0`_

* `Profile Images API Version 1.0`_

*************
New Events
*************

The following list includes new or changed events in the Open edX Cypress
release.

* The ``context`` field for server events now provides a ``usage_key`` to
  identify XBlock content. The ``usage_key`` member field was added to the
  ``module`` dictionary, which also provides the component ``display_name``.

* Events now include data from two HTTP header fields, ``referer`` and
  ``accept_language``.

* There are new events that record new posts, responses, and comments in course
  discussions.

* There are new events that record which of the problems in a library were
  delivered by a randomized content block component.

* Two instructor events have been added for generating and downloading reports
  from the Instructor Dashboard.

  * ``edx.instructor.report.downloaded``
  * ``edx.instructor.report.requested``

* The following events are now emitted when learners interact with polls and
  surveys.

  * ``xblock.poll.submitted``
  * ``xblock.poll.view_results``
  * ``xblock.survey.submitted``
  * ``xblock.survey.view_results``

For more information about events, see `Events in Tracking Logs`_ in the *edX
Research Guide*. Note that this document is intended for edX partners running
courses on edx.org. However, the event listing applies to Open edX instances as
well.

************************************************
Accessibility Updates
************************************************

In keeping with edX's commitment to creating accessible content for everyone,
everywhere, the Open edX Cypress release contains several accessibility
enhancements in the Open edX LMS and discussions.

* Keyboard navigation in open response assessments has been improved by
  restoring keyboard focus outline indicators.
  
* The LMS now has a region with a role of main and a descriptive aria-label
  allowing users to quickly navigate to the main content area using landmarks.

* Several accessibility problems with numerical input problem types are now
  corrected.

* A current status of the problem is now conveyed to learners who use screen
  readers properly.

* The workflow for checking how ASCII math is converted to MathML or MathJax
  format has been streamlined for screen reader users.
  
* Nonessential information is no longer included in aria-live regions, which
  improves the experience for screen reader users.

* Improvements to the accessibility of discussion posts for screen reader users
  are included in this release.

* HTML ``iframe`` elements now show meaningful title attributes that describe
  the content embedded in the IFrame.

* The main blue colors used throughout the LMS user interface
  were changed to meet WCAG AA guidelines for contrast.

* The LMS now includes an aria-live region to contain HTML for problems. 

* Submission buttons have been removed from the aria-live div scope.

* Several accessibility fixes have been implemented in the course header.

* An aria label has been added to the LMS footer.

* The main region in the Student dashboard now includes the role and aria-
  label attributes.

* Navigation controls in the LMS now have aria-label attributes.

* Focus now changes directly to the content area after the user selects a link
  to a new subsection or unit.

* Unit navigation links are reorganized into a single list. The arrow
  navigation is converted from links to buttons and now includes the disabled
  attribute when appropriate.

* Labels to bypass blocks now use the industry standard text **Skip to main
  content**.

* The current discussion conversation now receives focus and includes an
  accessible label.

* Discussions now include defined regions and landmarks for screen reader
  navigation. The focus is on the discussion when a new topic is loaded, and
  changes to a new post when it appears.

************************************************
Supported Browser Changes
************************************************

Note that in this release the edX platform no longer supports Internet Explorer
9.x.

************************************************
More Information on Cypress Release Changes
************************************************

The `edX Release Notes`_ contain a list of weekly changes that are deployed to
edx.org. Those changes are part of the master branch of the edX Platform in
GitHub.

You can also find `release announcements`_ on open.edx.org, which list changes
in each release on edx.org. You can subscribe to have release announcements
sent to your email account.

Changes listed on 8 July 2015 and before are included in the Cypress release
of Open edX. 

.. include:: links.rst
