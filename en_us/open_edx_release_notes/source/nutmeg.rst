.. _Open edX Nutmeg Release:

#######################
Open edX Nutmeg Release
#######################

These are the release notes for the Nutmeg release, the 14th community release of the Open edX Platform, spanning changes from October 15 2021 to April 11 2022.  You can also review details about `earlier releases`_ or learn more about the `Open edX Platform`_.

.. _earlier releases: https://edx.readthedocs.io/projects/edx-developer-docs/en/latest/named_releases.html
.. _Open edX Platform: https://openedx.org

.. contents::
 :depth: 1
 :local:

================
Breaking Changes
================

SafeSessionMiddleware
---------------------
Before upgrade: Check that your logs do not contain warnings starting with "SafeCookieData user at request", or that these warnings are very rare. If they are common, see the SafeSessionMiddleware section below in the Administrators and Operators Section.

Django Admin login disabled by default
--------------------------------------
Default Django admin login window is disabled and now one has to login from the LMS.

===================
Learner Experiences
===================

* Bug fix: facebook share links now work on the course about page.

User Tours
----------
User Tours are walkthroughs that can be presented to users in micro-frontends (MFEs). The default tours that exist are: "Course Home New User Tour" (`screencast`_), "Course Home Existing User Tour", and "Courseware New User Tour".
In order for User Tours to properly work, the backpopulate user tours management command should be run.

.. _screencast: https://user-images.githubusercontent.com/25124041/143145608-6886237d-ea83-42a4-ac2c-555b07392723.mov

.. code-block:: shell

    $ python ./manage.py lms backpopulate_user_tours


Dates Tab
---------
The Dates Tab has been added as a default static tab on all courses. All new courses will automatically include the Dates Tab. In order to properly have the Dates Tab show up for all your existing courses, a backfill course tabs management command has been created.

.. code-block:: shell

    $ python manage.py cms backfill_course_tabs

The Dates Tab has also been removed from the legacy learner experience. It is only available in the Learner MFE. This is the first step in remove the legacy learner experience altogether, which will be completed in the Olive release.


Weekly Course Goals
-------------------
The old course goals feature has been replaced with a new weekly learning goals feature. Users set a goal for how frequently they want to learn per course and get reminder emails about their goals. See `4.30. Enabling the Weekly Learning Goals Feature in "Installing, Configuring, and Running the Open edX Platform"`_ for instructions on how to configure this feature and more details on how the feature works. The new weekly learning goals feature is controlled with the same flag as the previous course goals feature.


Learning Micro-Frontend (MFE)
-----------------------------

* When an XBlock fails to render, the user will now see an error message "An unexpected error occurred. Please click the button below to refresh the page."
* RTL languages are now supported
* Support for the pre-alpha Discussions MFE was added


Account Micro-frontend (MFE)
----------------------------

The `Account Micro-frontend (MFE)`_ is now enabled by default. The legacy account pages will be removed in the next release, Olive.

.. _Account Micro-frontend (MFE): https://github.com/openedx/frontend-app-account


Mobile Experience
-----------------

* Added support for notices in apps.
* Added an activation opt in checkbox (default checked) so user can agree to receive marketing messages. See `LEARNER-8652`_ for a screenshot.
* Mobile apps can now support LTI by opening it in a browser

.. _LEARNER-8652: https://openedx.atlassian.net/browse/LEARNER-8652

Special Exams Experience
------------------------

To take a proctored exam, the learner must now be enrolled in a :code:`verified` course track. Previously, a learner enrolled in any track could take a proctored exam. Note that ID verification (IDV) is not required.


======================
Instructor Experiences
======================

* Default course tabs have a new, standard order. Course authors may still change the order of their custom static tabs, but the ordering of the default tabs cannot be changed. This ensures a more uniform location across courses.
* When setting grading policies, course authors can now set the minimum grade cutoff to 99. Previously it could not be higher than 97.
* When downloading the team membership csv from the **Teams > Manage** page, username and external key are now separate columns (previously, an external key would override the username, leading to ambiguity when importing teams csv)


LTI Support
-----------

* Course authors can now define static and dynamic custom parameters that will be sent to the LTI Tool Provider at launch. See the `Custom LTI Parameter section of the LTI Consumer XBlock Readme`_ for more details.
* Mobile apps can now support LTI by opening it in a browser

.. _Custom LTI Parameter section of the LTI Consumer XBlock Readme: https://github.com/openedx/xblock-lti-consumer/blob/master/README.rst#custom-lti-parameters

Gradebook Micro-frontend (MFE)
------------------------------

* Added support for transifex translations.
* Added support for custom theming.


==========================
Administrators & Operators
==========================

* Various improvements and bugfixes have been applied to `Tutor`_, the officialy-supported Open edX distribution and installation method. Notable features include an overhauled Tutor Plugin API and a new CLI for mounting repositories during development. You can see the full list by viewing `Tutor's changelog, starting at v13.0.1`_ (the first Tutor release after Maple) and reading upwards until v14.0.0 (the first Tutor release supporting Nutmeg).

.. _Tutor's changelog, starting at v13.0.1: https://github.com/overhangio/tutor/blob/master/CHANGELOG.md#v1301-2021-12-20


* An internal performance improvement called `learning sequences`_ has been opt-in for a few releases, but is now always-on for Nutmeg. If you have any courses that have not been re-published on Koa or later, run the :code:`simulate_publish` cms django command on your courses before upgrading, to populate the learning sequence data.

.. _learning sequences: https://github.com/openedx/edx-platform/blob/db32ff2cdf678fa8edd12c9da76a76eef0478614/openedx/core/djangoapps/content/learning_sequences/README.rst
.. code-block:: shell

    $ python manage.py cms simulate_publish

* By setting the :code:`ENABLE_NEW_RELIC` to false, the new relic logging integration will be disabled across all MFEs.

* It's now possible to add optional fields to the registations form that are always visible, and do not require the user to click the checkbox "Support education research by providing additional information." Use the new :code:`optional-exposed` setting in the `REGISTRATION_EXTRA_FIELDS`_ setting.

.. _REGISTRATION_EXTRA_FIELDS: https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/settings.html#setting-REGISTRATION_EXTRA_FIELDS

* Added an activation opt in checkbox to the registration form (default checked) so user can agree to receive marketing messages. The field :code:`marketing_emails_opt_in` is now enabled by default in the `REGISTRATION_EXTRA_FIELDS`_ setting.

* Waffle overrides can be set at the org level now (in between course level and global).

* To customize the template for course emails, set :code:`BULK_EMAIL_SEND_USING_EDX_ACE` to true.

* Course Discovery API now supports Learner Pathways and Course Recommendations

* Bug fix: When using GMSTP (Gmail) for sending bulk email, retriable SMTP exceptions were not caught and bulk sending failed. This has been fixed.

Bulk Course Email Tool
----------------------

* Added the ability to filter recipients of bulk course emails based on the last_login date of Users enrolled in a course run. This feature can be enabled by setting a value for the :code:`BULK_COURSE_EMAIL_LAST_LOGIN_ELIGIBILITY_PERIOD` setting. Its value should be an integer (representing months) that represents the eligibility period from the current date to receive a message. The new setting defaults to None which keeps this new feature disabled (and there will be no change in behavior in how recipients are filtered/selected for a message).

* Added a simple :code:`bulk_email_disabledcourse` table that allows for the bulk email tool to be disabled for specific course runs, even if the bulk email flag is on and the course is enabled in the :code:`bulk_email_courseauthorization` table. A course team will not be able to see the bulk email tab on the instructor dashboard for whatever course runs are in this table.

* the setting :code:`EMAIL_USE_DEFAULT_FROM_FOR_BULK` was changed to :code:`EMAIL_USE_COURSE_ID_FROM_FOR_BULK`. Additionally, the behavior was changed.  Previously, it was possible for a "from" address constructed out of a course id to be non existent, and thus fail in email servers. Now, those who wish to use their course id  in the "from" address for bulk email must enable the flag to true.


SafeSessionMiddleware rejects mismatching requests and sessions
---------------------------------------------------------------

Background: :code:`SafeSessionMiddleware` is an existing middleware that provides several protections against vulnerabilities that could result from cache misconfigurations or other bugs resulting in one user getting a different user's session.

Changed: Previously if a user mismatch was detected between request or session and response, the middleware would log warnings; now, it will invalidate the session and send an error response. The toggle :code:`ENFORCE_SAFE_SESSIONS` is enabled by default, but can be disabled to return to just log warnings.

Before upgrade: Check that your logs do not contain warnings starting with "SafeCookieData user at request", or that these warnings are very rare. If they are common, there is likely a false positive caused by some custom login, masquerading, or registration code. You will need to update your custom code to call :code:`mark_user_change_as_expected``. Otherwise, valid requests may be rejected.


Migrations
----------

There are no known migrations that will cause compatibility issues when deployed. As always migrations should be run before the new code is deployed.


Pre-Alpha Features
-------------------

The following Micro-frontends (MFEs) are in a "pre-alpha" state. They exist on GitHub but are not yet supported in Tutor. Additionally, they may lack key features such as support for theming, internationalization, and path-based deployments. We include mention of them because we expect all of them to be supported in the next release, Olive.

* `Authentication Micro-Frontend (MFE)`_
* `Discussions Micro-Frontend (MFE)`_
* `Course Authoring Micro-frontend (MFE)`_
* `Open-Response Assessments (ORA) Grading Micro-frontend (MFE)`_

.. _Authentication Micro-Frontend (MFE): https://github.com/openedx/frontend-app-authn
.. _Discussions Micro-Frontend (MFE): https://github.com/openedx/frontend-app-discussions
.. _Course Authoring Micro-frontend (MFE): https://github.com/openedx/frontend-app-course-authoring
.. _Open-Response Assessments (ORA) Grading Micro-frontend (MFE): https://github.com/edx/frontend-app-ora-grading

Settings and Toggles
--------------------

New settings and toggles added since the Maple release:

* `CELERY_EXTRA_IMPORTS <https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/settings.html#setting-CELERY_EXTRA_IMPORTS>`_
* `DISCUSSIONS_MFE_FEEDBACK_URL <https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/settings.html#setting-DISCUSSIONS_MFE_FEEDBACK_URL%20=%20None>`_
* `ORA_GRADING_MICROFRONTEND_URL <https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/settings.html#setting-ORA_GRADING_MICROFRONTEND_URL>`_

* `RATELIMIT_RATE <https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/settings.html#setting-RATELIMIT_RATE>`_
* `REGISTRATION_RATELIMIT <https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/settings.html#setting-REGISTRATION_RATELIMIT>`_
* `COURSEGRAPH_CONNECTION <https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/settings.html#setting-COURSEGRAPH_CONNECTION>`_
* `COURSEGRAPH_JOB_QUEUE <https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/settings.html#setting-COURSEGRAPH_JOB_QUEUE>`_
* `PREPEND_LOCALE_PATHS <https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/settings.html#setting-PREPEND_LOCALE_PATHS>`_
* `BULK_EMAIL_SEND_USING_EDX_ACE <https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/featuretoggles.html#featuretoggle-BULK_EMAIL_SEND_USING_EDX_ACE>`_
* `COURSEGRAPH_DUMP_COURSE_ON_PUBLISH <https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/featuretoggles.html#featuretoggle-COURSEGRAPH_DUMP_COURSE_ON_PUBLISH>`_
* `ENABLE_AUTHN_LOGIN_BLOCK_HIBP_POLICY <https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/featuretoggles.html#featuretoggle-ENABLE_AUTHN_LOGIN_BLOCK_HIBP_POLICY>`_
* `ENABLE_AUTHN_LOGIN_NUDGE_HIBP_POLICY <https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/featuretoggles.html#featuretoggle-ENABLE_AUTHN_LOGIN_NUDGE_HIBP_POLICY>`_
* `ENABLE_AUTHN_REGISTER_HIBP_POLICY <https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/featuretoggles.html#featuretoggle-ENABLE_AUTHN_REGISTER_HIBP_POLICY>`_
* `ENABLE_COPPA_COMPLIANCE <https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/featuretoggles.html#featuretoggle-ENABLE_COPPA_COMPLIANCE>`_
* `ENFORCE_SAFE_SESSIONS <https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/featuretoggles.html#featuretoggle-ENFORCE_SAFE_SESSIONS>`_
* `FEATURES['ENABLE_AUTOMATED_SIGNUPS_EXTRA_FIELDS'] <https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/featuretoggles.html#featuretoggle-FEATURES['ENABLE_AUTOMATED_SIGNUPS_EXTRA_FIELDS']>`_
* `FEATURES['ENABLE_INTEGRITY_SIGNATURE'] <https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/featuretoggles.html#featuretoggle-FEATURES['ENABLE_INTEGRITY_SIGNATURE']>`_
* `FEATURES['ENABLE_NEW_BULK_EMAIL_EXPERIENCE'] <https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/featuretoggles.html#featuretoggle-FEATURES['ENABLE_NEW_BULK_EMAIL_EXPERIENCE']>`_
* `FEATURES['ENABLE_PASSWORD_RESET_FAILURE_EMAIL'] <https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/featuretoggles.html#featuretoggle-FEATURES['ENABLE_PASSWORD_RESET_FAILURE_EMAIL']>`_
* `FEATURES['SHOW_PROGRESS_BAR'] <https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/featuretoggles.html#featuretoggle-FEATURES['SHOW_PROGRESS_BAR']>`_
* `LOG_REQUEST_USER_CHANGE_HEADERS <https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/featuretoggles.html#featuretoggle-LOG_REQUEST_USER_CHANGE_HEADERS>`_
* `MARK_LIBRARY_CONTENT_BLOCK_COMPLETE_ON_VIEW <https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/featuretoggles.html#featuretoggle-MARK_LIBRARY_CONTENT_BLOCK_COMPLETE_ON_VIEW>`_
* `RATELIMIT_ENABLE <https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/featuretoggles.html#featuretoggle-RATELIMIT_ENABLE>`_
* `SEARCH_SKIP_SHOW_IN_CATALOG_FILTERING <https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/featuretoggles.html#featuretoggle-SEARCH_SKIP_SHOW_IN_CATALOG_FILTERING>`_
* `course_live.enable_course_live <https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/featuretoggles.html#featuretoggle-course_live.enable_course_live>`_
* `courseware.enable_new_financial_assistance_flow <https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/featuretoggles.html#featuretoggle-courseware.enable_new_financial_assistance_flow>`_
* `discussions.enable_discussions_mfe <https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/featuretoggles.html#featuretoggle-discussions.enable_discussions_mfe>`_
* `discussions.enable_learners_tab_in_discussions_mfe <https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/featuretoggles.html#featuretoggle-discussions.enable_learners_tab_in_discussions_mfe>`_
* `discussions.enable_moderation_reason_codes <https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/featuretoggles.html#featuretoggle-discussions.enable_moderation_reason_codes>`_
* `discussions.enable_new_structure_discussions <https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/featuretoggles.html#featuretoggle-discussions.enable_new_structure_discussions>`_
* `discussions.enable_reported_content_email_notifications <https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/featuretoggles.html#featuretoggle-discussions.enable_reported_content_email_notifications>`_
* `learner_dashboard.enable_masters_program_tab_view <https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/featuretoggles.html#featuretoggle-learner_dashboard.enable_masters_program_tab_view>`_
* `learner_dashboard.enable_program_tab_view <https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/featuretoggles.html#featuretoggle-learner_dashboard.enable_program_tab_view>`_
* `learner_dashboard.enable_program_tab_view <https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/featuretoggles.html#featuretoggle-learner_dashboard.enable_program_tab_view>`_
* `new_core_editors.use_new_problem_editor <https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/featuretoggles.html#featuretoggle-new_core_editors.use_new_problem_editor>`_
* `new_core_editors.use_new_text_editor <https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/featuretoggles.html#featuretoggle-new_core_editors.use_new_text_editor>`_
* `new_core_editors.use_new_video_editor <https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/featuretoggles.html#featuretoggle-new_core_editors.use_new_video_editor>`_



the following settings were removed:

* agreements.enable_integrity_signature

* course_experience.latest_update

* course_goals.number_of_days_goals

* course_home.course_home_use_legacy_frontend

* learner_dashboard.enable_program_discussions

* learning_sequences.use_for_outlines

* request_utils.capture_cookie_sizes

* user_authn.redirect_to_microfrontend



Dependency updates
------------------

There are no notable dependency updates in nutmeg.

============
Deprecations
============

Removed in Nutmeg
-----------------
- django-ratelimit-backend has been removed from edx-platform. Now the django-ratelimit library will be used for rate limiting. See :jira:`DEPR-150` for more details. Related to this, the default Django admin login window is disabled and now one has to login from LMS.
- The `edx-certificates repo`_ has been archived. See `DEPR-160` for more details.
- “Old Mongo” course access has finally been fully removed. This means course runs that have keys like :code:`Org/Course/Run` rather than :code:`course-v1:Org+Course+run`  cannot be accessed by learners. New runs of this type haven’t been able to be created since 2015, but now learner access has also been removed. See `[DEPR] Issue #62`_ for more information on the continuing removal of Old Mongo technology.
- :code:`problemset` and :code:`videosequence` are old-but-not-entirely-unused aliases to the sequential (in Studio-speak, "Subsection") block type. Support for them in the Learning MFE ended in the maple release. Now all support has been removed.

Deprecated in Nutmeg (or earlier) and scheduled to be removed in the Olive release
----------------------------------------------------------------------------------

* `bokchoy test suites`_
* the `frontend-learner-portal-base`_ library
* The `xblock.fragment module`_ and deprecated :code:`id_generator` method parameters in :code:`xblock.runtime`
* The legacy courseware experience (rendered server-side by Django) will be removed. The Learner MFE will be required.
* The legacy account pages will be removed. The Account MFE will be required.
* EdxRestApiClient is no longer supported, as you may have been able to tell from the many, many deprecation warnings.
* DraftModuleStore (also know as Old Mongo Modulestore) will be removed. "Old Mongo" course access was already removed in nutmeg.
* microsites djangoapp
* the ability to import legacy OLX attributes :code:`slug`, :code:`name`, :code:`id` (discussion block), :code:`for`, and :code:`attempts`

.. _bokchoy test suites: https://github.com/gedx/public-engineering/issues/13
.. _frontend-learner-portal-base: https://github.com/openedx/frontend-learner-portal-base/issues/31
.. _xblock.fragment module: https://github.com/openedx/public-engineering/issues/15
.. _microsites djangoapp: https://github.com/openedx/public-engineering/issues/69
.. _import legacy OLX attributes: https://github.com/openedx/public-engineering/issues/74

Future deprecations and removals
--------------------------------

.. note:: Major deprecation work is being funded between now and the Olive release, scheduled for December 2022. Please review the `DEPR: Deprecation & Removal`_ board on Github to be sure you have stopped using deprecated technologies.

.. _DEPR\: Deprecation & Removal: https://github.com/orgs/openedx/projects/9/views/4

=============================
Researcher & Data Experiences
=============================

* added a :code:`complete_video` event that fires when a user has watched a video to the end. Requires the waffle switch :code:`completion.enable_completion_tracking`


=====================
Developer Experiences
=====================

* Added support for custom xBlock editors in Studio. Read the `pluggable_override docstring`_ to learn more.
* Added an API for updating user's email opt-in setting.
* django plugins can now return context for the Instructor Dashboard template, by adding it to the constant :code:`INSTRUCTOR_DASHBOARD_PLUGIN_VIEW_NAME`. See `PR 29376`_ for more details.

.. _pluggable_override docstring: https://github.com/openedx/edx-django-utils/blob/master/edx_django_utils/plugins/pluggable_override.py#L11-L58
.. _django plugins: https://github.com/edx/edx-platform/blob/master/openedx/core/djangoapps/plugins/README.rst
.. _PR 29376: https://github.com/openedx/edx-platform/pull/29376

Events and Filters Extension Framework
--------------------------------------
Core extensibility: We have added a new way of extending the core through `Open edX Events & Filters`_ (part of `OEP-50: Hooks Extension Framework`_)

Open edX Events: this standardized version of Django Signals allows extension developers to extend functionality just by listening to the event that’s sent after a key process finishes, e.g after enrollment, login, register, etc.

Open edX Filters: through configuration only, extension developers can set a list of functions to be executed before a key process starts, e.g before enrollment, login, register, etc.


.. include:: links.rst
.. include:: ../../links/links.rst

