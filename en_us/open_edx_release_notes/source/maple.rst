.. _Open edX Maple Release:

######################
Open edX Maple Release
######################

These are the release notes for the Maple release, the 13th community release of the Open edX Platform, spanning changes from April 9 2021 to October 15 2021.  You can also review details about `earlier releases`_ or learn more about the `Open edX Platform`_.

.. _earlier releases: https://edx.readthedocs.io/projects/edx-developer-docs/en/latest/named_releases.html
.. _Open edX Platform: https://open.edx.org

.. contents::
 :depth: 1
 :local:

================
Breaking Changes
================

Tutor is the supported distribution
-----------------------------------

`Tutor`_ is now the official, community-supported distribution of open edX for production. It replaces `edX configuration`_. The Tutor changelog for the Maple release is at https://github.com/overhangio/tutor/blob/master/CHANGELOG.md#v1300

Learning Micro-Frontend (MFE) becomes the default courseware experience
-----------------------------------------------------------------------

Warning: Entrance exams, non-standard XML and HTML tags, and non-standard course hierarchies are not supported. See below for more details.


Studio login changed to OAuth
-----------------------------

In versions prior to Maple, Studio (CMS) shared a session cookie with the LMS, and redirected to the LMS for login.
Studio is changing to become an OAuth client of the LMS, using the same SSO configuration that other IDAs use. (See
:jira:`ARCHBOM-1860`; `OEP-42`_) This is a breaking change. Follow the `Studio OAuth migration runbook`_ as part of
upgrading to Maple. For devstack, run::

    ./provision-ida-user.sh studio studio 18010


django-cors-headers version updgraded
-------------------------------------

django-cors-headers is upgraded to version 3.2.0. The setting :code:`CORS_ORIGIN_WHITELIST` now requires URI schemes.
You will need to update your whitelist to include schemes, for example from this::

    CORS_ORIGIN_WHITELIST = ["foo.com"]

to this::

    CORS_ORIGIN_WHITELIST = ["https://foo.com"]


===================
Learner Experiences
===================

Learning Micro-Frontend (MFE)
-----------------------------

The Learning MFE (including both "courseware" and the "course home") is the default course experience in Maple. With the new experience, learners will notice a reduction in load times and better site performance. The Nutmeg release will drop support for the legacy (that is, LMS-rendered) course experience entirely.

Configuration
^^^^^^^^^^^^^
- MFE branding elements can be set in the Tutor MFE plugin. See the `tutor mfe plugin README`_ for more details.
- The :code:`courseware.use_legacy_frontend` and :code:`course_home.course_home_use_legacy_frontend` Waffle flags can be toggled on (either globally or per-course-run) in order to revert to the legacy (LMS Django-rendered) courseware experience.
- The domain name for your learning MFE should be added to the :code:`CORS_ORIGIN_WHITELIST` for ecommerce, discovery, lms, and studio.

Removed Features
^^^^^^^^^^^^^^^^
- Entrance Exams are slated to be deprecated and are never enabled on the MFE. Attempting to start a course with an entrance exam on the MFE results in an error. Using the waffle flags to enable the legacy experience should enable their usage for the time being, but their deprecation is forthcoming.
- Problemsets and videosequences, which are deprecated variations of the Sequence block will not render in the MFE. Note, these could have only been added in raw OLX. This cannot affect courses authored entirely in Studio.
- **Non-standard course hierarchies** Legacy courseware was willing to render some content that didn’t strictly follow that hierarchy, and that content will break in the MFE. This should only affect courses authored directly in OLX. Studio-authored courses already follow these hierarchy requirements. Essentially, courses must follow a stricter hierarchy in order to work in the MFE:

  * The direct children of the root Course block should be Section (aka Chapter) blocks.
  * The children of the Sections must be Subsections (aka Sequence) blocks. Each Subsection must be part of at most one Section.
  * Children of the Subsections should be "Unit-like" blocks (most commonly Verticals, but HTML/Problem/etc are okay too)

Altered Features
^^^^^^^^^^^^^^^^
- The ability for course authors to preview units in the learner experience before they are published will preview in the legacy experience, not the MFE. Work enabling preview using the MFE is anticipated.
- According to the HTML standard, <script> and <iframe> tags are not self-closing; they must be closed with </script> and </iframe> tags. Legacy courseware incidentally corrected this error when it occurred in course content. MFE courseware does not do that correction. Course authors should update their courses to use well-formed HTML if they happened to rely on self-closing <script> or <iframe> tags.
- Courses which use the  course key pattern ORG/COURSE/RUN instead of the new pattern, course-v1:ORG+COURSE+RUN,  are stored in our legacy storage service, Old Mongo, and will not be served by the new MFE. Instead they default to the legacy experience. But this pattern has been deprecated and will be removed.
- Author-written JS inside a Custom Javascript Problem block which acts outside the boundary of a unit will fail. Problem blocks will no longer be able to modify other problem blocks or access any parent elements using javascript. The main use case is pulling in content from a students’ previous answers or state. This is still possible with the get_statefn attribute all within the iframe. Although this may remove some small pieces of custom functionality, it is in the interests of adhering to security protocols.
- Course Navigation on the MFE and legacy experience will have minor differences.

  * The breadcrumbs displayed at the top of a page in the legacy experience were organized by Course -> Sequence -> Unit -> Content Block Title, but in the new MFE breadcrumbs only include Course -> Sequence -> Unit. This removes visual clutter of having the same title repeated in a small space on the page.
  * the MFE changes the URL scheme from::

      LMS_BASE/courses/COURSE_KEY/courseware/SECTION_URLNAME/SEQUENCE_URLNAME/UNIT_INDEX?activate_block_id=COMPONENT_KEY

    to::

      LEARNING_MFE_BASE/course/COURSE_KEY/SEQUENCE_KEY/UNIT_KEY

- If all content inside a unit should be invisible to a cohort, but the sequence or the unit is not hidden, learners may be able to still see the titles of the content on the course outline, as well as the title of the sequence which contains only what should be hidden content to that learner. This issue can be removed by setting the :code:`learning_sequences.use_for_outlines` waffle flag to :code:`true`.

Maintained Features
^^^^^^^^^^^^^^^^^^^
- Features which remain functional within MFE courses, but still will be served by the legacy experience in Maple are:

  * The XBlock student view, as exposed via the unit iframe in MFE courseware
  * Static tabs (aka Custom Pages)
  * Discussions tab
  * Wiki tab
  * Teams tab
  * Notes tab
  * Instructor dashboard.
- Special exams (timed and proctored) will be functional within the Learning MFE for MFE enabled courses.

Added Features
^^^^^^^^^^^^^^
- To enable faster movement through course content, staff users will now see jump navigation selectors to augment the existing course breadcrumb in the learning sequence experience (Learning MFE). With this deployment, a staff user can select a section or subsection, a menu will appear, and the user can jump to a particular unit within a course.
- Course outlines will now feature automatic effort estimates for subsections. Courses have to be republished before they show estimates, and all videos in the course must also have durations in `edx-val`_, the Open edX video abstraction layer.
- There are some in-course celebrations of progress. A modal popup when a learner finishes their first section. And a 3-day streak celebration modal popup. This is configurable using the waffle toggles :code:`mfe_progress_milestones` and :code:`mfe_progress_milestones_streak_celebration`
- The end of a course now has its own landing page, which can be enabled by setting the waffle toggle :code:`microfrontend_course_exit_page` to :code:`true`.


Certificates
------------

Various bug fixes and updates around course certificate generation

- Removal of the :code:`allow_certificate` field on the :code:`UserProfile` model has been completed, and the column has been dropped (Note: if your UserProfile table has a lot of rows, the migration to drop the column could lock the table and necessitate a status page/downtime.)
- The temporary waffle flag :code:`certificates_revamp.use_allowlist` has been removed, as testing during the rollout of this feature has been completed. All course runs now use the new allowlist behavior, which is described in the `Allowlist ADR`_
- Code to generate a new or update an existing course certificate has been consolidated:

  * The temporary waffle flag :code:`certificates_revamp.use_updated` has been removed, as testing during the rollout of this feature has been completed. All course runs now use the new consolidated course certificate behavior, which is described here.
  * Code to generate (create or update) PDF course certificates has been removed from edx-platform.
  * The :code:`fix_ungraded_certs`, :code:`regenerate_user`, :code:`resubmit_error_certificates`, and :code:`ungenerated_certs` management commands have been removed. In their place, please use the `cert_generation command`_.
- In an effort to be more inclusive, code referencing a Certificate Whitelist has been updated to instead refer to a Certificate Allowlist. The CertificateWhitelistmodel has been replaced by the CertificateAllowlistmodel (data is automatically copied over to the new model by a data migration).
- The management command named :code:`cert_whitelist` has been removed. In its place, please use the Certificate Allowlist, which can be accessed from the Instructor tab on the course page in the LMS. (:jira:`DEPR-156`)
- The Segment event :code:`edx.bi.user.certificate.generate` will no longer emit from the courseware when self-generated certificate generation is attempted by a user. There was some overlap in this Certificate event with the :code:`edx.certificate.createdevent` sent during certificate generation. A self-generated certificate event will have a generation_mode of self (versus batch for certificates generated automatically).
- Removed use of the modulestore wherever possible in the certificates Django app of edx-platform. Changes include:
  * Using a course’s CourseOverview over retrieving course data from the modulestore
  * Supporting change: Update the :code:`list_with_level` function in the Instructor Dashboard to accept a course-id over the entire course object (`PR 27646`_)
- Removed the :code:`AUDIT_CERT_CUTOFF_DATE` setting. Awarding Audit certificates will not be supported in V2 of Course Certificates (:jira:`DEPR-159`)
- Removed the :code:`openedx/core/djangoapps/certificates` app by merging the single :code:`api.py` file into :code:`lms/djangoapps/certificates`. All APIs functions have been been moved as is, so if you have any code in a third party repository that used this API, please point them to the new path. openedx/core/djangoapps/certificates/api.py → lms/djangoapps/certificates/api.py
- Removed :code:`backpopulate_program_credentials` management command in place of an updated :code:`notify_credentials` command.


Open-Response Assessments
-------------------------
- extend frontend feedback limit to 1k chars
- Make submission feedback full-width


Account Micro-frontend
----------------------

- removed hard-coded edX string

Payment Micro-frontend
-----------------------

The Payment MFE is the only supported UI for ecommerce in this release. Cybersource and PayPal backends have been tested. See the Tutor Ecommerce plugin for configuration details: https://overhang.io/tutor/plugin/ecommerce

Mobile Experience
-----------------

Android
^^^^^^^
- Allow word_cloud as supported xBlock
- allow specialExam xBlock to open through View on Web
- open rendered HTML block having iframe in mobile browser
- add self-paced course dates events in calendar
- add support of lti_consumer xblocks
- add alerts prior to course due dates

iOS
^^^
- Open rendered HTML block that contains an iframe in the mobile browser
- add word cloud to acceptable list of xblocks
- add course events to calendar
- Add support of lti_consumer xblocks

Special Exams Experience
------------------------

- Created a new page in the account frontend to host proctoring instructions and requirements. This content can be dynamic to the need of each proctoring provider and potentially each course.
- Allow learners to resume an exam after hitting a proctoring error, without forcing them to restart the exam, or to use an exam attempt.


======================
Instructor Experiences
======================

Studio
------

- Course and library creation rights can now be granted on a per-organization basis.
  * Controlled content creation rights feature must be enabled via the FEATURES['ENABLE_CREATOR_GROUP'] flag.
  * Creation rights are requested by new users on the Studio page.
  * Administrators handle requests by modifying records in the course_creators admin app: <STUDIO_ROOT>/admin/course_creators/coursecreator/
- Administrators will now have a new capability when granting access:
  * Admins may now uncheck “All Organizations”, and instead select one or more particular organizations from the list.
  * Users granted creation access in this manner will only be able to create courses or libraries under the specified organizations.
  * This change is backwards-compatible: existing creation right grants will continue to apply to all organizations, and “All Organizations” remains the default option when granting new rights.
  * However, administrators can safely modify the organization settings on existing creation right grants if they would like to retroactively use this feature.

Course Authoring Import Messaging & Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

While many course teams do not commonly use this course import, educators cannot continue course authoring when it does fail. Previously, course teams would occasionally encounter issues importing a new version of their course through Studio. Existing error messaging made the root cause hard to discern, requiring course teams to reach out to an admin for assistance. Educators blocked by the import tool were not unable to update or launch their course without admin intervention, delaying authoring and publishing timelines for courses.

Now educators will see specific error messages in the course import area of Studio. For developers, these errors are logged and can exported to a New Relic, Splunk, etc.


Uploading Errors
================

- **File Chunk Missed During Upload** - The most common error that was captured, “Chunk Missed Error”. When a Course Import file (tar.gz) is larger than 20MB, it is divided into equal chunks and uploaded to the server. Due to our server configuration, it is possible to lose a chunk that could fail the course import while combing on the server

- **File Chunk Failed To Upload Error** - This error is raised when a file chunk has been lost during the upload process. Due to this the file is corrupted and can not be processed.

- **Incompatible File** - This error is raised for the sanity check if a user accidentally tries to upload an incompatible file. This check exists in the frontend as well.

Unpacking Errors
================

There are a few validation checks before the unpacking of the tar file begins. These validation checks look redundant and similar to file upload but these errors are in place because this is an asynchronous task and can be triggered from the API. Currently, this work was out of scope so this is added in the “What’s Next” section.

- **Invalid User** - In case the user_id provided does not exist. This is highly unlikely to occur from the front end, but this check is in place for the sanity check.

- **Permission Denied** - This error occurs if the user does not have the required permissions to perform the course import. Once that case occurs, the system throws the error to the user.

- **Incompatble File** - This error is raised if the file to unpack is not in tar.gz format. This check verifies that the process of unpacking does not execute if the file is not in a valid format.

- **File Not Found** - This error occurs if the uploaded file is not available in the storage or has been deleted.

- **Unsafe Tar File** - This is a system-level error that occurs when the tar file tries to unpack itself at the root where it does not have permissions.

- **Unknown Exception** - There can still be unknown events that may occur during the course import, for those further information will be logged in the system logs but there is not a clear and useful user facing error.

Verifying Stage
===============

- **Verify Root Name** - The root name for a course import is ``course.xml`` and for a library it's ``library.xml``. If that file does not exist then this error is thrown.

Updating Errors
===============

The errors can occur after the XML validation and during the data update in the course.

- **Error while parsing asset XML** - Error while reading ``assets.xml`` file when it has syntax or other errors.

- **Duplicate CourseID** - Aborting import because a course with this id already exists

- **Module Import Error** - A module in the coures failed to import correctly.

- **Proctoring Provider Error** - This error is raised when a ``courserun.xml`` file contains an attribute ``proctoring_provider`` e.g. ``proctoring_provider="proctortrack"`` and that provider is not available/enabled on the server.

- **Unknown Error** - An unknown error occured whyl updating the course.

.. note::

   More information about the development process can be found in this `documented in Confluence`_.  However that is not a public document and only left here for admins and future reference. The error details above have been extracted from that document.

Open-Response Assessments
-------------------------

Reusable Rubrics
^^^^^^^^^^^^^^^^

Course staff can now reuse a rubric from an existing Open Response Assessment (ORA) in a course when creating a new ORA in the same course. Using a Block ID, course staff can now specify which ORA’s rubric they want to clone into another ORA within the same course.

In Studio, course staff navigates to the “Rubric” section of the editing modal for the published or unpublished ORA whose rubric they want to clone. After expanding the “Clone Rubric” section, they can copy the Block ID for that ORA.

Next, they can either create a new ORA or navigate to an existing ORA, and open the “Rubric” section of the editing modal. Here, they can either paste the full Block ID of the ORA whose rubric they want to clone or type in a few characters of that Block ID and select it from the dropdown.

Once the correct Block ID is selected, they can select “Clone” and all of the existing rubric values will be replaced with the rubric values from the original ORA.


Other ORA features
^^^^^^^^^^^^^^^^^^

- Learners can now provide feedback with an expanded character limit of 1k
- Add a new button to edit an ORA in Studio
- Make submission feedback full-width
- UI Changes for Rubric Reuse


LTI 1.3 and LTI Advantage Support
---------------------------------

lti-consumer-xblock (also known as xblock-lti-consumer) has been updated to support LTI 1.3, as well as the Deep Linking (LTI-DL) and Assignments and Grades services (LTI-AGS) features of LTI Advantage. Information on configuring lti-consumer-xblock can be found at https://github.com/edx/xblock-lti-consumer/blob/master/README.rst

- LTI 1.3 and LTI Advantage features are now enabled by default.
- LTI 1.3 settings were simplified to reduce confusion when setting up a LTI tool.
- The URL of the LTI Config Model has been updated. This configuration is used to enable LTI PII sharing per course.  The impact of this update is that anyone who has bookmarked the LTI Django Admin model will need to update their pointer.  The new model admin is available in studio admin at : “admin/lti_consumer/courseallowpiisharinginltiflag/”.
- Move CourseEditLTIFieldsEnabledFlag from edx-platform to this repo while retaining data from existing model.
- Use CourseAllowPIISharingInLTIFlag for LTI 1.3 in lieu of the current CourseWaffleFlag.
- Rename CourseEditLTIFieldsEnabledFlag to CourseAllowPIISharingInLTIFlag to highlight its increased scope.
- The modal to confirm information transfer on open of lti in new tab/window has been updated because of a change in how browsers handle iframe permissions.
- Long-term fix for cross-origin iFrames


Gradebook Micro-FrontEnd
------------------------

Gradebook allows course staff to view, filter, and override subsection grades for a course. For configuration details, see https://github.com/edx/frontend-app-gradebook

There are some limitations to the version in Maple:

- The MFE makes calls to New Relic even when it is not configured, cluttering the user's browser console log.
- the header is not translated, but it can be overridden. To override the header, use the frontend-component-header in version 2.2.5 as a base (newer versions could break the MFE)


Special Exams Experience
------------------------

- We added a view to the Instructor Dashboard for seeing onboarding progress for Proctored Exams. This tab includes all students enrolled in the course and their onboarding state, even if they have never attempted the exam. This list should be filterable to quickly identify the list of learners where action may be needed to encourage onboarding soon.
- Instructors can give learners permission to resume an exam after encountering a proctoring error. Grades/certificates will not be released until all active attempts have been reviewed and marked as passing.


=========================
Administrator Experiences
=========================


Password Complexity
-------------------

Implemented and rolled out new password complexity requirements to meet PCI compliance. For more detail, see https://github.com/edx/edx-platform/blob/open-release/maple.master/common/djangoapps/util/password_policy_validators.py


Migrations
----------

See the sections above on OAuth and Certificates.


Settings and Toggles
--------------------
Documentation for settings and toggles is much improved, but still incomplete. See https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/index.html


Dependency updates
------------------

- **Django 3.2** We upgraded Django to version 3.2, the next LTS (long term support) release. More details available at https://openedx.atlassian.net/wiki/spaces/AC/pages/2844426436/Django+3.2+Upgrade
- **ElasticSearch 7.10** We upgraded all IDAs, using ElasticSearch (edx-platform, Blockstore, discovery, notes, analytics-api, cs-c comments-service) to ElasticSearch 7.10.
- **Mongo 4.2** MongoDB version 4.0 is end of life in April 2022. We upgraded all IDAs, using Mongo 4.0 (edx-platform, cs-comments) to Mongo version 4.2. More details at https://openedx.atlassian.net/wiki/spaces/AC/pages/2922316338/Mongo+4.2+Upgrade


Deprecations
------------

- The sysadmin dashboard has been removed. Similar functionality is available via the (unsupported) edx-sysadmin plugin from https://github.com/mitodl/edx-sysadmin/
- The :code:`AUDIT_CERT_CUTOFF_DATE` setting was removed. This setting allowed organizations that previously offered course certificates to audit track learners to discontinue generation of this type of certificate. Instead, the logic of :code:`CourseMode.is_eligible_for_certificate()` will be used. In this logic, the audit mode is not eligible for a course certificate. The honor mode may or may not be eligible, depending on whether the :code:`DISABLE_HONOR_CERTIFICATES` feature is enabled. Other modes are eligible for certificates.
- The management command named :code:`cert_whitelist` has been removed. In its place, please use the Certificate Allowlist, which can be accessed from the Instructor tab on the course page in the LMS. (:jira:`DEPR-156`)


=============================
Researcher & Data Experiences
=============================

- Tracking metrics based on the anonymized session ID will experience a discontinuity or other anomaly at the time of deployment, as the anonymized IDs will change. This will likely appear as if everyone logged out and back in again, although only from a metrics perspective. In a green-blue deployment scenario, it may briefly appear as if there are twice as many sessions active.
- Removed certificate generation segment event. We will continue to track certificate creation/generation using the existing :code:`edx.certificate.created` event.

=====================
Developer Experiences
=====================

Hooks Extension Framework
-------------------------

Hooks are predefined places in the edx-platform core where externally defined functions can take place. In some cases, those functions can alter what the user sees or experiences in the platform. Other cases are informative only. All cases are meant to be extended using Open edX plugins and configuration. For documentation, see https://github.com/eduNEXT/edx-platform/blob/open-release/maple.master/docs/guides/hooks/index.rst You can find code for a sample hook at https://github.com/eduNEXT/openedx-events-2-zapier

Course Certificate Generation Logic Improvement
-----------------------------------------------

We have replaced the back-end code (no UX changes) that generates course certificates with a new version to condense the number of conflicting generation logic patterns, make it easier to troubleshoot/support, and to better defend generated certificates against errant revocation.

By creating this new, unified course certificate generation logic we have improved certificate generation, revocation, allow-listing, program record synchronization, and issue resolution times.

Learners and partners should not notice any change. The only effect is that they should see a reduced time to resolution if they ever encounter a problem related to certificates or credentials.

Learning Micro-Frontend (MFE)
-----------------------------
To increase development speed and site performance, we've made improvements to the learning sequence experience (Learning MFE) on edX-platform, to use a React-based frontend that emulates the legacy experience. The Learning MFE code repository is at https://github.com/edx/frontend-app-learning

After a year of diligently working to overhaul the learning sequence experience to use a React-based micro-frontend, it is now live for learners. This update to the underlying infrastructure of the learning sequence experience aims to drive innovation and experimentation that will ultimately foster greater learner engagement. With the new experience, learners will notice a reduction in load times and better site performance. However, the true beneficiaries of this work are internal development teams who will be able to quickly and efficiently build in this area of the system.

Using the React MFE allows for a richer learner experience by reducing course load-time and vastly improving the mobile-web experience. Additionally, the new experience supports learners by increasing internal development speeds which allows for greater feature development. By breaking down the courseware and reducing dependency, developers can more easily iterate in this area of the platform. Today, we see the benefits of this infrastructure change to the learning sequence experience contribute to the release of several projects and experiments.



.. include:: links.rst
.. include:: ../../links/links.rst

