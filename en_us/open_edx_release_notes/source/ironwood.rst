.. _Open edX Ironwood Release:

#########################
Open edX Ironwood Release
#########################

This page lists the highlights of the Ironwood release of the Open edX platform.

.. this doesn't seem relevant any more:

    The `edX Release Notes`_ contain a summary of changes that are deployed to
    edx.org. Those changes are part of the master branch of the edX Platform in
    GitHub. You can also find `release announcements`_ on the open.edx.org
    website.

    Changes listed for July 6, 2018 and before are included in the Ironwood release
    of Open edX. Changes after that point will be in future Open edX releases.

.. contents::
 :depth: 1
 :local:

============================
Authoring Experience Updates
============================

Studio Login via the LMS
------------------------

Now logging in to Studio is done by redirecting the user to the LMS to log in,
and then redirecting back to Studio.  This can be disabled by site operators
using the new DISABLE_STUDIO_SSO_OVER_LMS feature flag.

Course Launch & Best Practices Checklist
----------------------------------------

We have reintroduced the Studio checklist feature from 2014 to help
automatically track important course launch steps. Previously this was a manual
checklist feature that we stopped using in 2015, but with this update the
feature is live once again and it automatically detects completion status for
authors. In addition to basic launch requirements such as ensuring a
certificate is enabled for a course and course dates have been set, we have
also included a best practices checklist. These checklists are summarized on
the course outline showing the current number of items successfully completed
out of the total remaining. In addition to this, certain checklist items such
as the assignment deadline validator will list out the instances in the course
where the checklist rule is not met. Assignments with deadlines that do not
fall between the course start and end date are automatically flagged and
listed.


Video Status Indicators
-----------------------

For Open edX instances using the video uploads page, this view now conveys the
status of each video as it relates to its transcoding (through edx-VEDA) and
transcription (3rd party configuration). The status column is listed in the
Previous Uploads table. More details around the status messages are `available
in our documentation`__.

.. __: https://edx.readthedocs.io/projects/edx-partner-course-staff/en/latest/video/upload_video.html#video-processing-statuses

Gradebook Application
---------------------

The gradebook will give you a central location where you can view and manage
grades for all learners in a course. It will provide you with improved search
which you can use to find specific learners and override assignment-specific
grades. In addition, you can filter by cohort, track, or assignment type.

You can read more about this in the documentation for the `Gradebook Application`__.

.. __: https://edx.readthedocs.io/projects/open-edx-building-and-running-a-course/en/latest/student_progress/course_grades.html#review-learner-grades-on-the-instructor-dashboard

.. note:: This application is available in devstack, but is not yet supported
          in production installations.


Learner Data for a Specific Problem
-----------------------------------

Thanks to the Open edX community, the downloadable Student State report
received readability enhancements and now contains new columns for single
problems or for all problems in a unit, subsection, or section, as well as for
all problems in the course.


==========================
Learner Experience Updates
==========================

Transferrable Learner Records
-----------------------------

The credentials service which previously powered program certificates now also
supports learner program records. Where certificates function as a sharable
digital credential analogous to a wall display of a diploma, the learner record
is a credential representation that is digitally similar to a transcript.
Program record views include grading details and other information which can
then be shared or sent to specific institutions. The learner record sending
feature is configured with the help of the discovery service, by adding
pathways that are associated with one or more programs. An example of a credit
pathway is a full degree program that is associated with a program (ex: By
completing the MIT Supply Chain MicroMasters Program, you can apply and
transfer credit into MIT’s campus Supply Chain Masters Degree program if
admitted.) While we do not yet have course records or full learner history
records, we are excited about the potential this work opens up for learners
looking to transfer or share their valuable credentials to employer and credit
pathways.

Password Complexity Requirements
--------------------------------

We have updated the syntax for setting password complexity of your instance. We
also added some default checks to ensure that your password isn't trivial. You
can now also provide your own password validator plugin if you have custom
rules or logic for password complexity.


Expanded Language Support for course experience
-----------------------------------------------

We have added support for beta languages on the platform. These languages
become a selectable option in the account settings dropdown alongside fully
supported languages. If a learner selects a beta language, they are shown a
message letting them know support for this language is partial and makes it
easy to revert their language or head over to transifex to help translate the
platform into that language as a member of that language team.


Anonymous Course Content Access
-------------------------------

This feature enables learners to preview course content without necessarily
being logged into a given learning environment. It was implemented by adding a
setting to the platform that lets course authors adjust the visibility of
course content in the LMS.  Three different options are supported: private,
public outline, or public.

* Private (default, same as today)
* Public Outline (redirects learners to the course outline page and shows the outline only)
* Public (lets learners view HTML & Video content in the course, but hides unsupported XBlocks - such as problems and inline discussions)

Feature Based Enrollments
-------------------------

Feature Based Enrollments, the basis of edX.org’s new revenue model, is
available in Ironwood. FBE allows you to differentiate what features are
available to audit learners (free track). With this enabled, audit learners
will have access to core course content – videos, reading, discussion forums,
supplemental resources, and practice problems for the expected duration of the
course. You can configure it such that only verified learners will have access
to graded problems and/or have unlimited access to course content after course
end. This functionality is defaulted to off at the platform level, and can
additionally be configured by course run or organization.


===============================
Mobile Application Improvements
===============================

Between Hawthorn and Ironwood, the Mobile application releases spanned 2.15 →
2.17.1 The details of these releases are captured in our release documentation
for the mobile applications. Included below is a summary of the learner facing
and operator facing changes to mobile.

Learner Facing Mobile Changes
-----------------------------

A major experience improvement to landscape and rotation support arrived in
version 2.15. This was a key driver of lower ratings and reviews for our
applications as many of our mobile learners use tablets, in particular iPad
devices. For mobile applications using web course discovery, we have added a
way to add native cards that let users jump to a specific course discovery
view. On edX.org’s mobile applications we used this to expose popular subjects
in the mobile course discovery experience.

Another improvement, delivered in version 2.16, was the introduction of
programs through new program fragment views of the web edX platform pages. This
new area enables learners to view their program dashboard and program progress
pages, just as they do on the web browser experience.

With version 2.17 we delivered many accessibility improvements into the mobile
applications, including initial support for iOS 11’s recently introduced
Dynamic Text Type sizing and scaling. This change means learners who have set
their device text size to being larger now have that setting expressed within
the open edX mobile application. Additionally, the mobile application now
provides clarity into when learners will lose access to a course. More details
around this are included in the `Feature Based Enrollments`_ update.

Developer Facing Mobile Changes
-------------------------------

For the iOS code base, we upgraded to support Xcode 10.1, we have updated our
Firebase configuration now that Fabric has been deprecated as a service, and we
removed the deprecated Parse code that was still in the code base.
Additionally, we have mostly completed our deep linking integration with Branch
with the v2.17.1 release, though other follow on improvements have merged since
Ironwood was released.

For the Android code base, we removed unnecessary permissions that were being
requested from the earliest version of our application and implemented run time
permissions instead to request permissions such as file storage access when
learner’s trigger actions such as uploading a new profile photo. In terms of
library upgrades, we updated the Facebook SDK to 4.36.0, upgraded minSdkVersion
to KitKat (API Level 19), upgraded gradle and other libraries, updated Fabric
and Firebase configurations,  and implemented pull to refresh functionality on
the course outline page.

=========================
Platform Operator Updates
=========================

Starting in Ironwood, the configuration repo will no longer ship with a default
Django secret key for edx-platform.  This means that if you have been deploying
with the default insecure secret key, your builds will break.  The change was
made so that deployers are forced to make actual secret keys that are not
predictable.  If you wish to use the old key still, you can add the following
line to your config overrides::

    EDXAPP_EDXAPP_SECRET_KEY: "DUMMY KEY CHANGE BEFORE GOING TO PRODUCTION"

As part of the work on :jira:`LEARNER-4674`, edX switched from using a custom-built
password validator to Django's framework of password validation. This involved
creating a new configuration value, ``AUTH_PASSWORD_VALIDATORS``, a list of
Django and edX-created validators.  To facilitate code cleanliness, we have
removed unnecessary configuration values preferring to specify the values in
``AUTH_PASSWORD_VALIDATORS``. The removed variables are
``PASSWORD_MIN_LENGTH``, ``PASSWORD_MAX_LENGTH``, and ``PASSWORD_COMPLEXITY``.
The new values were added in `pull request #4810`_ and the unnecessary values
were removed in `#4811`_.

.. _LEARNER-4674: https://openedx.atlassian.net/browse/LEARNER-4674
.. _pull request #4810: https://github.com/edx/configuration/pull/4810
.. _#4811: https://github.com/edx/configuration/pull/4811

Two new settings files were added to edx-platform with this release, at
``lms/envs/production.py`` and ``cms/envs/production.py``.  These new files
replace the existing aws.py settings files.  The aws.py settings files remain,
but are deprecated as of Ironwood and will be removed in the next release.  If
you are using the configuration repo to set up your environment, it will
automatically start using the production.py file with this release without you
needing to make any changes.

With the changes in Studio to use LMS for login authentication, LMS and Studio
have to be served from cookie-compatible domains. If the Studio domain name is
a sub-domain of the LMS domain name, then the ``EDXAPP_SESSION_COOKIE_DOMAIN``
Ansible variable (translates to ``SESSION_COOKIE_DOMAIN`` in lms.env.json) has to
be set to '.<LMS domain>'. The Studio domain has to be added to the
``EDXAPP_LOGIN_REDIRECT_WHITELIST`` Ansible variable (``LOGIN_REDIRECT_WHITELIST``
variable in lms.env.json) for the redirect from LMS to Studio after login to
work.

We added some new tooling to help us better monitor celery queues.  There is a
`new python script`__ that will monitor redis queues and alert if a task has
been sitting in the queue for too long.

.. __: https://github.com/edx/configuration/tree/36ed093d6db6a719d12a65057bcd19aae1588a84/util/jenkins/check_celery_progress

Abbey.py tooling to build AMIs from Ansible runs of the configuration repo has
been removed.  If you wish to run Ansible and then create AMIs from those
machines, use the Ansible scripts under the `continuous_delivery`__ folder.

.. __: https://github.com/edx/configuration/tree/36ed093d6db6a719d12a65057bcd19aae1588a84/playbooks/continuous_delivery

The e-commerce dependencies have been updated to django-oscar 1.5.4. The 1.5.3
release of django-oscar contains a security fix. If you use anonymous checkout,
please see the `django-oscar 1.5.3 release notes`__ as you may need to rotate your
keys.

.. __: https://django-oscar.readthedocs.io/en/latest/releases/v1.5.3.html


.. include:: links.rst
.. include:: ../../links/links.rst
