.. _Open edX Dogwood Release:

####################################
Open edX Dogwood Release
####################################

This page lists the highlights of the Dogwood release.

.. contents::
 :depth: 1
 :local:

.. note::
 With the :ref:`Open edX Eucalyptus Release`, the Dogwood release is no longer
 supported. This page remains in these release notes as a record of when new
 features were included in Open edX.

**************
New Features
**************

The following new features are included in the Open edX Dogwood release.

.. contents::
 :depth: 1
 :local:

==============
New LTI XBlock
==============

.. _LTI XBlock:

A new LTI XBlock is now available. This XBlock is intended to replace the
existing LTI XModule. In addition to all of the functionality previously
offered by the XModule, the LTI XBlock also offers course teams the ability to
configure the way that learning tools interoperability (LTI) components open
when learners use them: in a modal window, in a separate web browser window, or
embedded in a course page.

.. note:: The LTI XModule continues to function in courses that include it,
 but it does not provide the new launching behavior options.

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

.. note:: EdX does not currently provide installation or support of Insights
 for Open edX installations.

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

This release includes several updates to web certificates.

* Course team members with the Admin or Staff role can now set the start date
  for a course that is configured to issue certificates before its certificates
  are activated.

* Course teams can now override the course number as well as the course name on
  the certificate.

* Both the course number and the override course number are displayed in the
  certificate set up page in Studio.

* There are now no character limits on the name and title fields of certificate
  signatories.

For more information, see :ref:`opencoursestaff:Setting Up Course Certificates`
in *Building and Running an Open edX Course* or
:ref:`openlearners:Print a Web Certificate` in the *Open edX Learner's Guide*.

As a part of the effort to support XSeries program certificates, edX has
created a new credentials service. In the Dogwood release, program certificates
can be configured on the Django admin console. Additional changes are currently
in progress to move all existing course certificate tools and logic to this new
service. Be sure to watch for more changes in the Eucalyptus release and other
future Open edX releases.

===========================
Search Feature for DevStack
===========================

When you install the Open edX developer stack, the search feature is now
enabled by default. For more information about how you can configure this
feature, see :ref:`installation:Enable edX Search`. For more information about
how learners can use this feature, see :ref:`openlearners:SFD Search`.

=========================
Timed Exams Feature
=========================

This release includes the timed exams feature. Course teams can configure a
course subsection so that learners have a specific period of time to complete
and submit all problems in that subsection.

For more information, see  the :ref:`opencoursestaff:Timed Exams` section in
the *Building and Running an Open edX Course* guide.

.. note::
   Another special exam feature, proctoring, is available for courses on the
   edx.org website. The proctoring feature can be enabled in Open edX, but it
   is not supported for the Dogwood release. This feature requires additional
   configuration and the services of a third-party proctoring vendor such as
   Software Secure to be used effectively.

.. _Otto Ecommerce Service:

=======================
E-commerce Service
=======================

Open edX installations can now add an e-commerce service. The edX
`e-commerce service`_ is a Django application that manages and handles
orders for product catalogs.

For more information about how to install and set up the edX e-commerce
service, configure partners and sites, add assets, and fulfill orders, see
`Adding E-Commerce to the Open edX Platform (Dogwood)`_ in the *Installing,
Configuring, and Running the Open edX Platform* guide.

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

**************************
New and Changed Events
**************************

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
* ``play_video``

For more information about these events, see `Events in Tracking Logs`_ in the
*edX Research Guide*. Note that this document is written primarily for edX
partners running courses on edx.org. However, the event listing applies to Open
edX instances as well.

***********************
Accessibility Updates
***********************

In keeping with edX's commitment to creating accessible content for everyone,
everywhere, the Open edX Dogwood release contains numerous accessibility
enhancements and improvements to readability and navigability.

* In Studio, changes to the **Unit** page make it easier to use a keyboard to
  navigate to the options in the **Add New Component** section of this page. It
  is also easier to use a keyboard to make selections from the list of choices
  that appears when you select the **Advanced** option.

* On course pages in the LMS, options for actions that course team members can
  take, such as **View Unit in Studio** and **Staff Debug Info**, are now pink
  instead of blue. This change increases the contrast between the text and the
  gray background when these options are in a default state.

* In the LMS, the list of topics on the **Discussion** page now uses colors
  that meet WCAG AA guidelines for contrast. As a result, the background color
  of the selected topic is now white instead of light blue.

* The calculator now has a background color that contrasts with the foreground
  on the input label.

* Alert notifications for course wiki articles have been updated to increase
  contrast between the background color and the alert text.

* The left navigation menu presented by the **Courseware** page was
  re-engineered. Navigating through sections, subsections and units using the
  course navigation menu is now significantly improved for keyboard and screen
  reader users.

* Keyboard navigation in open response assessments was improved by restoring
  keyboard focus outline indicators.

===================================
Design Updates to the Video Player
===================================

This release includes several updates to the edX video player.

* The user interface controls for the player appear only after a learner
  selects **play** for a video, and take up less screen space.

* New icon designs are used for the **full screen** and **show transcript**
  options.

* The language menu, for video with transcript in multiple languages, is
  indicated by a drop-down menu icon next to the **show transcript** icon.

* To improve accessibility, all options use an icon font method that
  streamlines delivery.

* To enhance the experience of learners who use screen readers, changes that
  improve spoken announcements and simplify navigation are also included.

*********************
Deprecated Features
*********************

Several features are deprecated as of the Open edX Dogwood release.

.. contents::
 :depth: 1
 :local:

=============
Shoppingcart
=============

The "shoppingcart" functionality is deprecated as of the Dogwood release, and
it will be removed in a future release. Similar services are now provided by
the :ref:`Otto Ecommerce Service`.


.. Removed support for the outdated ``ispublic`` field on the Course Module, including its corresponding ACCESS_REQUIRE_STAFF_FOR_COURSE feature flag.  Instead, operators should use COURSE_CATALOG_VISIBILITY_PERMISSION and COURSE_ABOUT_VISIBILITY_PERMISSION settings.


==================
Studio Checklist
==================

The **Tools** menu in Studio no longer offers the **Checklists** option. For a
template checklist, see the :ref:`opencoursestaff:Course Launch Checklist`
topic in the *Building and Running an Open edX Course* guide.

=========================
Original ORA Problems
=========================

When you access a course that contains an open response assessment created
using the original version of this assignment type (ORA 1), Studio now
displays the message, "This course uses features that are no longer supported."

A newer version of the open response assessments feature (ORA 2) was released
over a year ago, and the ability to add ORA 1 problems was removed from Studio
in May 2014.

============================
Legacy Instructor Dashboard
============================

Support has ended for the "legacy" Instructor Dashboard. The Legacy Instructor
Dashboard is now disabled by default, and the LMS presents a single version of
the Instructor Dashboard. The **Revert to Legacy Dashboard** option is no
longer available.

Code for the Legacy Instructor Dashboard will be removed entirely in the Open
edX Eucalyptus release.

The **Data Download** page in the Instructor Dashboard now includes an option
to download a report of all learner submissions for a specified problem.
Previously, this report was available only from the Legacy Instructor Dashboard
through a view on a Django app.

============================
XModules and Tools
============================

The following XModules and tools are deprecated in the Dogwood release.

* The FoldIt protein simulator XModule.

* The LTI XModule. This XModule has been replaced by the :ref:`LTI XBlock`.

* Support has ended for the graphical_slider_tool. Code for this tool will
  be removed entirely in the Open edX Eucalyptus release.

============
Django Apps
============

The following Django apps are deprecated in the Dogwood release.

* The Psychometrics Django app.

* The Licenses Django app.

==================
Wiki Notifications
==================

The recent edX platform upgrade to Django 1.8 required edX to deprecate the
wiki notifications feature. The wiki notifications feature was disabled to make
the Django 1.8 upgrade possible, and this feature has not been reimplemented.

********************
Django 1.8 Upgrade
********************

The edX platform was upgraded from Django 1.4 to Django 1.8.7. This section
summarizes the effects of this upgrade. For more information, see the `Django
1.8 Upgrade Release Notes`_ page on the edX wiki or the `Django 1.8 pull
request`_ in GitHub.

==================
Transactions
==================

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

==================
Model Migrations
==================

* All Django Python South schema migrations have been incorporated into each
  initial "0001" Django schema migration.

* Data migrations that seed data are now idempotent. All other data migrations
  have been discarded.

==================
Model Meta Classes
==================

The ``app_label`` attribute has been added to several different models. For
more information, see `app_label`_ on the `Django website`_.

==================
More Information
==================

To view the release notes for Django versions 1.5—1.8, see the following
resources.

* `Django 1.5`_
* `Django 1.6`_
* `Django 1.7`_
* `Django 1.8`_

************************************************
More Information on Dogwood Release Changes
************************************************

The `edX Release Notes`_ contain a summary of changes that are deployed to
edx.org. Those changes are part of the master branch of the edX Platform in
GitHub.

You can also find `release announcements`_ on open.edx.org, which list changes
in each release on edx.org. You can subscribe to have release announcements
sent to your email account.

Changes listed for 16 December 2015 and before are included in the Dogwood
release of Open edX.

**************
Patch Releases
**************

=======================
9 March 2016: Dogwood.1
=======================

* An update to the release packaging was made.

* The help links in Studio now open topics in the correct version of the
  *Building and Running an Open edX Course* guide.


========================
14 April 2016: Dogwood.2
========================

* Django is updated to version 1.8.12.

* You now have the option to allow learners to audit courses without offering
  certificates for the audit track.  Use the ``AUDIT_CERT_CUTOFF_DATE`` setting
  to control when audit certificates are discontinued. For more information,
  see :ref:`installation:Discontinue Audit Certificates` in the *Installing,
  Configuring, and Running the Open edX Platform* guide.

* A number of installation issues are fixed.

* A number of security issues are fixed.


========================
25 April 2016: Dogwood.3
========================

An update to the release packaging was made to fix errors during installations
and upgrades.


.. include:: links.rst
.. include:: ../../links/links.rst
