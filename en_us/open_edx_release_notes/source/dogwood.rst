.. _Open edX Dogwood Release:

####################################
Open edX Dogwood Release
####################################

This page lists the highlights of the Dogwood release.

.. contents::
 :depth: 1
 :local:

**************
New Features
**************

The following new features are included in the Open edX Dogwood release.

.. contents::
 :depth: 1
 :local:

==============
New XBlocks
==============

Oppia XBlock
************

`Oppia`_ explorations are short, interactive tutorials. With the Oppia XBlock,
course teams can embed Oppia explorations in courses.

For information about how to install the `Oppia XBlock`_, see the *Installing,
Configuring, and Running the Open edX Platform* guide.

For information about how to enable this tool in Studio and add Oppia
explorations, see :ref:`opencoursestaff:Oppia Exploration Tool` in the
*Building and Running an Open edX Course* guide.

Office Mix XBlock
******************

With `Office Mix`_, course teams can turn PowerPoint presentations into
interactive online lessons that are called mixes. With the Office Mix XBlock,
course teams can embed  mixes in courses.

For information about how to enable this tool in Studio and add mixes to a
course, see :ref:`opencoursestaff:Office Mix Tool` in *Building and Running an
Open edX Course*.

LTI XBlock
***********

A new LTI XBlock is now available. This XBlock is intended to replace the
existing LTI xModule. In addition to all of the functionality previously offered by the xModules, the LTI XBlock also offers course teams the ability to
configure the way that learning tools interoperability (LTI) components open
when learners use them: in a modal window, in a separate web browser window, or
embedded in a course page.

.. note:: The LTI xModule continues to work, but does not provide the new
  launching behavior options.

For more information, see :ref:`opencoursestaff:LTI Component` in the *Building
and Running an Open edX Course* guide.

=====================================
Course Preview as a Specific Learner
=====================================

A new preview mode in the LMS allows course team members to see the courseware
as a specific learner sees it. For courses that use randomized content
from content libraries, course team members can use this feature to view the
content assigned to a specific learner and to adjust a learner's grades if
necessary.

For more information, see :ref:`opencoursestaff:Grades` in *Building and
Running an Open edX Course*.

=================
Partial Credit
=================

In Studio, course teams can now configure the following problem types so that
learners can receive partial credit for a problem if they submit an answer that
is partly correct.

* Checkbox
* Multiple Choice
* Numerical Input
* Write-your-own-grader

For more information, see :ref:`opencoursestaff:Awarding Partial Credit for a
Problem` in *Building and Running an Open edX Course*.

====================================
Open edX Analytics Developer Stack
====================================

Developers who are interested in extending Open edX Insights can now set up a
separate development environment, the Open edX Analytics Developer stack, to
support analytics development. This environment, known as the Analytics
Devstack, includes the edX Analytics Data API and Open edX Insights, as well
as all of the components needed to run the Open edX Analytics Pipeline.

For more information, see :ref:`installation:Installing the Open edX Analytics
Developer Stack` in the *Installing, Configuring, and Running the Open edX
Platform* guide.

========
Insights
========

.. Insights has a version marked that is compatible with Dogwood, but we don't provide installation or support.

===============
Timed Exams
===============

Course teams can now configure a course subsection so that learners have a
specific period of time to complete and submit all problems in that subsection.
Individual learners can be granted more time to complete problems.

For more information, see :ref:`opencoursestaff:Timed Exams` in the *Building
and Running an Open edX Course* guide.

.. To enable this feature for your installation, the ``ENABLE_SPECIAL_EXAMS`` must be set to true (where? turns on proctoring too)

=========================================
Initial Version of Comprehensive Theming
=========================================

The initial version of comprehensive theming is now available. Sites that are
running Open edX can now create and use themes to change the default branding
of the system to present their own brand. Logos, page headers and footers, and
other templates and assets that control the way a site looks are now organized
into specifically named directories and files that can be replaced easily and
without coding changes.

For more information, see :ref:`installation:Changing the Way Open edX Looks`
in the *Installing, Configuring, and Running the Open edX Platform* guide.

========================================================
Additional File Types for Open Response Assessments
========================================================

Course teams can now specify, and learners submit, additional types of files
along with text responses to open response assessment problems. When course
teams edit an open response assessment component in Studio to allow file
uploads, the following options are available.

* Image files in .jpg, .gif, or .png format.

* The image file formats listed above, and also files in .pdf format.

* A custom set of one or more file formats, specified by the course team.

For more information, see :ref:`opencoursestaff:PA Allow Images`.

To protect learners from the transmission of potentially harmful files, this
enhancement also gives system administrators the ability to configure a list of
file types that learners cannot upload.

For more information, see
:ref:`installation:Configuring ORA2 to Prohibit Submission of File Types`.

===============
Certificates
===============

TBD

===========================
Search Feature for DevStack
===========================

When you install the Open edX developer stack, the search feature is now
enabled by default. For more information about how you can configure this
feature, see :ref:`installation:Enable edX Search`. For more information about
how learners can use this feature, see :ref:`openlearners:SFD Search`.

=========================================
TPA Sign In Without Account Activation
=========================================

Learners who register and sign in using third party authentication, such as
with a Google or Facebook account, can now sign in immediately. They can sign
in and enroll in courses even before they follow the activation link that is
sent by email. A reminder message appears on the learner's dashboard until
account activation takes place.

A learner who enters an incorrect email address, and who therefore does not
receive the activation email message, can correct the email address by
selecting the menu next to his username, and then selecting **Account**.

==========================================================
Consistent Team Role Names in Studio and LMS
==========================================================

The labels that identify two of the course team member roles in the LMS now
match the labels for those same roles in Studio. In the LMS, on the Instructor
Dashboard **Membership** page, the "Course Staff" role is now labeled "Staff",
and the "Instructor" role is now labeled "Admin".

No changes were made to the privileges granted by these roles. For more
information, see :ref:`opencoursestaff:Course_Staffing` in the *Building and
Running an Open edX Course* guide.

.. note:: No changes were made to the privileges that system administrators
  set in the Django admin console, or to their labels.

====================================================
Icon Change for Graded Subsections
====================================================

In the LMS, the icon that indicates a graded subsection in the course
navigation is now a paper and pencil symbol instead of an alarm clock.

=========================================
Command Change for SAML Testing
=========================================

The recent edX platform upgrade to Django 1.8 required a change to the
management command used when :ref:`installation:testing an enabled SAML
identity provider<Test an Enabled SAML Provider>`. This command now uses the
syntax ``lms saml --pull`` instead of ``lms saml pull``.

*****************
REST API Changes
*****************

EdX has built and published documentation for the following REST APIs, which
are available in the Open edX Dogwood release.

* TBD

*************
New Events
*************

The following list includes new or changed events in the Open edX Dogwood
release.

* ``edx.certificate.created``
* ``edx.certificate.shared``
* ``edx.certificate.evidence_visited``
* ``edx.forum.response.voted``
* ``edx.forum.thread.voted``
* ``edx.team.activity_updated``
* ``edx.team.changed``
* ``edx.team.created``
* ``edx.team.deleted``
* ``edx.team.learner_added``
* ``edx.team.learner_removed``
* ``edx.team.page_viewed``
* ``edx.team.searched``
* ``microsoft.office.mix.loaded``
* ``microsoft.office.mix.paused``
* ``microsoft.office.mix.played``
* ``microsoft.office.mix.slide.loaded``
* ``microsoft.office.mix.stopped``
* ``oppia.exploration.loaded``
* ``oppia.exploration.state.changed``
* ``oppia.exploration.completed``
* ``play_video``

For more information about these events, see `Events in Tracking Logs`_ in the
*edX Research Guide*. Note that this document is written primarily for edX
partners running courses on edx.org. However, the event listing applies to Open
edX instances as well.

************************************************
Accessibility Updates
************************************************

In keeping with edX's commitment to creating accessible content for everyone,
everywhere, the Open edX Dogwood release contains several accessibility
enhancements in the Open edX LMS and discussions.

* TBD

************************************************
Deprecated Features
************************************************

The following features are deprecated as of the Open edX Dogwood release.

.. contents::
 :depth: 1
 :local:


"shoppingcart" functional should be considered deprecated as of Dogwood and will be removed in a future release. Similar services will be provided by "Otto" going forward
ORA1 code is completely removed

Legacy instructor dash is turned off by default, and will be removed entirely in Eucalyptus


* Support has ended for the "legacy" Instructor Dashboard. The LMS now
  presents a single version of the Instructor Dashboard. The **Revert to
  Legacy Dashboard** option is no longer available.

  The :ref:`installation:Feature Flag Index` in the *Installing, Configuring,
  and Running the edX Platform* guide is updated to reflect this change.


* The **Data Download** page in the Instructor Dashboard now includes an option
  to download a report of all learner submissions for a specified problem.
  Previously, you downloaded this report from the Legacy Instructor Dashboard.


Old code has been removed:
Admin dashboard
abtest_module
Psychometrics
"Licenses" djangoapp
FoldIt XModule
Studio course checklists
Removed support for the outdated ispublic field on the Course Module, including its corresponding ACCESS_REQUIRE_STAFF_FOR_COURSE feature flag.  Instead, operators should use COURSE_CATALOG_VISIBILITY_PERMISSION and COURSE_ABOUT_VISIBILITY_PERMISSION settings.
The "graphical_slider_tool" is deprecated, and will no longer be available starting in in Eucalyptus (the code has been removed from Master).

Several unused and deprecated items have been removed from the edX Platform, including the FoldIt protein simulator XModule and the first version of open response assessments (ORA 1). Courses that used ORA 1 continue to have access to associated data.

Several unused and deprecated items have been removed from the edX Platform, including several Django elements. The following list includes some of these items.
The first version of open response assessments (ORA 1). Courses that used ORA 1 continue to have access to associated data.
The Checklist page previously available from the Studio Tools menu.
The FoldIt protein simulator XModule.
The Psychometrics Django app.
The Licenses Django app.
The “legacy” Instructor Dashboard, including a Django admin dashboard for analytics reports, which were available by view from the legacy Instructor Dashboard.

==================================
Original ORA Problems Deprecated
==================================

When you access a course that contains an open response assessment created
using the original version of this assignment type (ORA 1), Studio now
displays the message, "This course uses features that are no longer supported."

A newer version of the open response assessments feature (ORA 2) was released
over a year ago, and the ability to add ORA 1 problems was removed from Studio
in May 2014.

============
LTI
============

LTI XModule replaced by LTI XBlock.




************************************************
Supported Browser Changes
************************************************

TBD

************************************************
More Information on Dogwood Release Changes
************************************************

The `edX Release Notes`_ contain a summary of changes that are deployed to
edx.org. Those changes are part of the master branch of the edX Platform in
GitHub.

You can also find `release announcements`_ on open.edx.org, which list changes
in each release on edx.org. You can subscribe to have release announcements
sent to your email account.

Changes listed on TBD and before are included in the Dogwood release
of Open edX.

.. include:: ../links.rst








===================
Django 1.8 Upgrade
===================

The upgrade from Django 1.4 to Django 1.8 includes the following changes as well as several additional
changes. For more information, see the `Django 1.8 Upgrade Release Notes`_ page
on the edX wiki or the `Django 1.8 pull request`_ in GitHub.

Transactions
*********************

* For Django 1.8, edX recommends that you use the ``transaction.atomic``
  decorator to start transactions for the code. For more information, see the
  `Database Transactions`_ page on the `Django website`_.

* The ``commit_on_success`` decorator is no longer available. You can use the
  new ``outer_atomic`` decorator instead.

* To avoid exceptions when you create models, edX recommends that you use the
  following pattern.

    ::

     if need_to_create_model:
        try:
            with transaction.atomic():
                MyFancyModel.create(**kwargs)
        except IntegrityError:
            # Model has already been created.
            log.warning("Something...")

Pip
****

* The ``egg_name`` value in each GitHub-based ``requirements.txt`` line must
  match the ``name`` value in the ``setup.py`` file of the repository.

* To avoid errors, you must always specify a version number in a URL-based
  requirements file line.

* New dependencies should use the "editable" (``-e``) prefix only when necessary.


Model Migrations
*********************

* All Django Python South schema migrations have been incorporated into each
  initial "0001" Django schema migration.

* Data migrations that seed data are now idempotent. All other data migrations
  have been discarded.

Model Meta Classes
*********************

* The ``app_label`` attribute has been added to several different models. For
  more information, see `app_label`_ on the `Django website`_.

More Information
*********************

To view the release notes for Django versions 1.5—1.8, see the following
resources.

* `Django 1.5`_
* `Django 1.6`_
* `Django 1.7`_
* `Django 1.8`_

=========================================
Upgrade to Django 1.8.7
=========================================

As a follow up to the upgrade of the edX platform to Django 1.8.5, this release
upgrades the edX platform to Django 1.8.7.

For more information, see the Django release notes for `1.8.6`_ and `1.8.7`_.

