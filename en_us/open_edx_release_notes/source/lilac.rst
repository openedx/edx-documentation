.. _Open edX Lilac Release:

######################
Open edX Lilac Release
######################

These are the release notes for the Lilac release, the 12th community release of the Open edX Platform, spanning changes from November 12 2020 to April 9 2021.  You can also review details about `earlier releases`_ or learn more about the `Open edX Platform`_.

.. _earlier releases: https://edx.readthedocs.io/projects/edx-developer-docs/en/latest/named_releases.html
.. _Open edX Platform: https://open.edx.org

.. contents::
 :depth: 1
 :local:

===================
Learner Experiences
===================

Open-Response Assessments
-------------------------
- Learners can submit rich text responses
- Grading status message
- Allow viewing ORA steps after peer review
- See the Authoring Experience section below for more ORA enhancements

Account Micro FrontEnd
----------------------
The Account MFE is enabled by default and provides private user settings UIs, including:

- Account settings page
- Demographics collection
- IDV (Identity Verification)

Checkout Micro FrontEnd
-----------------------
The Checkout MFE is enabled by default. Prior checkout UIs may not be PCI compliant.

Learning Micro FrontEnd
-----------------------
The Learning MFE is *not* enabled by default, because theming and internationalizations support is incomplete. However, we expect that this is the last named release to support the Legacy courseware frontend.

If the Learning MFE is installed using the MFE Deployer Ansible role then certain features can be opted in to the Micro-Frontend. These LMS CourseWaffleFlags can be toggled on (globally, per-user, or per-course) to switch certain features over the Learning MFE:

- courseware.courseware_mfe : Enable to host courseware (ie, the learning sequence experience) in the MFE.
- courseware.microfrontend_course_team_preview : Enable to show global and course-level staff members the ability to preview courseware in the MFE. Does not affect learners.
- course_home.course_home_mfe : Enable in conjunction with one or more of the following:

  - course_home.course_home_mfe_dates_tab : Display the “Dates” course tab in the MFE.
  - course_home.course_home_mfe_outline_tab : Display the course outline (the target of the “Course” course tab) in the MFE.
  - course_home.course_home_mfe_progress_tab: Display the “Progress” course tab in the MFE.

Course Dates & Milestones
-------------------------

When a learner reaches the end of the course, they will see a new navigation button directing them to “Complete the course” if they’ve passed or completed an audit course. The new Course Completion page also provides clarity for common learner questions - Did I complete the course? Did I achieve a certificate? Am I still eligible to upgrade?

The 3-day Streak Milestone is live and celebrates learners who engage with their course on 3 consecutive days. It also provides normative insights into how learners’ behavior connects to successful course outcomes. (TBD Image)

See https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/featuretoggles.html#featuretoggle-FEATURES['ENABLE_MILESTONES_APP'] for information on how to turn on and configure these Milestones features.

Mobile Experience
-----------------

- The fonts, text and colors have been updated to match the rebrand, giving users a consistent cross platform experience.
- Mobile learners can now understand the benefits of the upgrade option, especially when they encounter locked content.
- Learners can now complete ORAs in their mobile devices without having to leave the application.
- Learners can now complete Drag and Drop assessments on their mobile devices without having to leave the application. (iOS only)
- When learners open the app, they are asked permission to enable notifications. Using firebase, notifications can be sent to all mobile app learners who have their notifications enabled.
- Learners can now see green checkmarks next to the subsections and components in the course and section outline pages. (iOS only)
- A resume button, similar to the one in web, is now available in the mobile application. When learners click on the resume button, they will be navigated to the component after the last completed one. The state of this resume button syncs across web and mobile. In other words, if a component is completed on web, the user can use the mobile application to resume to the next incomplete component.
- Learners will not see a celebratory modal, similar to web, when they complete their first section.
- Previously, the links to assignments shown in the course dates page  in the app took learners to the mobile browser. Now, they are navigated directly to that component in the mobile application, removing the need to re-login to access the assignment.


Special Exams Experience
------------------------

Proctortrack Onboarding UX Improvements: Based on learner feedback, we’ve added new messaging and entrance locations to the Proctortrack onboarding experience to make the process more clear. (TBD image)



=====================
Authoring Experiences
=====================

Studio
------

- In-Context Unit Naming: Authors can now rename units from the course outline.

Open-Response Assessments
-------------------------

- Toggle rubric visibility for learners: Course staff can now choose to show learners the rubric for an ORA as they complete their ORA submission, more easily allowing learners to understand how they will be evaluated.
- ORA Problems as Component Category: We have elevated Open Response components as a category in the Studio Unit page so that they are easier to drop into a unit page with pre-configured templates. You can quickly add some of the most commonly configured ORA problems
- Allow Viewing ORA Steps After Peer Review: Learners can now proceed to the next assessment step when reaching a peer assessment step. This change makes all peer-related steps non-blocking, though they will still be required to complete the problem. Some problems for example situate self assessment after peer assessment, but previously learners were blocked from completing this step.
- Support Flexible Peer Grading Averaging for Learners delayed / in Peer Grading step: As part of reducing the number of students delayed in the peer grading step, we have introduced a new grading setting for ORA peer reviews called “Enable Flexible Peer Grading Averaging.” When enabled, learners who have received at least 30% of the required “Graded By” peer reviews and who have waited longer than seven days for a peer review will be assigned a peer review grade using available peer reviews. If enabled, the effect is that fewer learners will be waiting for additional peer reviews, requiring less manual staff intervention for this edge case.
- Added username details to ORA report download
- Added problem name and location to ORA report download
- Added ORA zipped file download for submission text + attached files
- Open response assessment problems as a component category
- Separate assessment steps & schedule authoring areas in Studio
- See the Learner Experience section above for more ORA enhancements


LTI 1.3 and LTI Advantage Support
---------------------------------
lti-consumer-xblock (also known as xblock-lti-consumer) has been updated to support LTI 1.3, as well as the Deep Linking (LTI-DL) and Assignments and Grades services (LTI-AGS) features of LTI Advantage. Note that this xBlock is not installed in Lilac by default. Information on configuring lti-consumer-xblock can be found at https://github.com/edx/xblock-lti-consumer/blob/master/README.rst

Gradebook MFE
-------------
The Gradebook MFE is *not* enabled by default because theming and internationalizations support is incomplete. It allows editing of individual learners' grades. Also supports bulk uploads of grades, but requires additional configuration. See https://github.com/edx/frontend-app-gradebook/blob/open-release/lilac.master/README.md for more information.

Special Exams Experience
------------------------

- Proctortrack Onboarding Status Menu: Helps course teams better identify which learners have been onboarded and which have not. See https://partners.edx.org/announcements/proctortrack-onboarding-status-menu for more information. The dashboard can be found under *Instructor Dashboard > Special Exams > Student Onboarding Status*. Requires integration with the `ProctorTrack Service from Verificient`_.
- Reset an Errored Proctortrack Exam Attempt: We added the ability to reset an errored Proctortrack exam attempt to be “Ready to resume” status. Learners will be able to resume the exam immediately once the course team allows it. The exam time will resume from where they last experienced an error.  For example, if the learner errored 45 minutes into the exam, and the allowed duration of the exam is 2 hours, the learner will only have 1 hour and 15 minutes to complete the rest of the exam.

Credentials (for Programs)
--------------------------

Program Completion Emails: Added `ProgramCompletionEmailConfiguration`_ that enables an email to be customized and sent to learners when triggered by the generation of a program certificate. These email messages are especially useful to remind a learner of their accomplishment at the appropriate time if a course in the program has a `certificate availability date`_ set in the future. These messages can be customized on a per program basis.

=========================
Administrator Experiences
=========================

Migrations
----------

An index was added to the ``courseware_studentmodule`` table. This can be a VERY EXPENSIVE MIGRATION which may take hours or days to run depending on size. Depending on your database, it may also lock this table, causing courseware to be non-functional during that time.

If you want to run this migration manually in a more controlled
way (separate from your release pipeline), the SQL needed is::

  CREATE INDEX `courseware_stats` ON `courseware_studentmodule` (`module_id`, `grade`, `student_id`);

You can then `fake the migration`_.

Course Upsell Messaging and Payment
-----------------------------------

- Reduce PCI compliance burden by replacing checkout fields which collect relevant PII data with Cybersource hosted fields. This way we do not collect and sensitive information and do not have to
- Allows setting default currency from environment
- Get and pipe-through the current datetime from the server, so that we don't need to use the browser time in preparation for the redesigned value proposition’s expiration box’s countdown to access expiration.


Settings and Toggles Documentation
----------------------------------
Documentation for settings and toggles is much improved, but still incomplete. See https://edx.readthedocs.io/projects/edx-platform-technical/en/latest/index.html

New settings introduced in Lilac include:

TBD


Dependency updates
------------------

These dependencies were upgraded for the `Open edX Koa Installation`_:

- Mongo was upgraded from 3.0 to 4.0.
- Switched from Elasticsearch 1 to Elasticsearch 7 across Open edX. This may require some syntax changes for custom scripts that used search APIs.
  - Please change queries that used __not to __exclude
  - Please properly URL-encode any plus signs in query URLs (like in course run key parameters) to %2b. Our Elasticsearch 7 implementation is more strict in that regard.
  - Please change queries against course-discovery that used pacing to pacing_type

New Settings
------------

- Use of edx-proctoring with the ProctorTrack vendor now requires a setting PROCTORING_USER_OBFUSCATION_KEY – it should be initially set to the same value as SECRET_KEY, in both LMS and Studio. This allows it to be changed independently, although there is not yet a way to rotate it without breaking integration.

Changes to edx-organizations
----------------------------

  - Uniqueness constraint added to Organization.short_name
    - This was added in edx-organizations 6.0.0. See release notes for details.
    - For instances that did not enable FEATURES['ORGANIZATIONS_APP'], this is a no-op
    - For instances the DID enable FEATURES['ORGANIZATIONS_APP'], any Organizations with conflicting short_names need to be removed (can be done via Django admin), else the migration for edx-organizations 6.0.0 will fail to apply.
  - Organizations feature globally enabled for all LMS and Studio instances.
    - See https://github.com/edx/edx-organizations/blob/master/docs/decisions/0001-phase-in-db-backed-organizations-to-all.rst  for reasoning and details.
    - If you don’t care about this change, then it shouldn’t affect you, although we still recommend running the backfill command (see below).
  - Added ORGANIZATIONS_AUTOCREATE Django setting for Studio.
    - Defaults to True.
    - When True, creating a new course run or content library with an unrecognized org slug (that is, “edX” in course-v1:edX+DemoX+2T2020 will silently auto-create an organization in the background.
    - When False, creating a new course run or content library with an unrecognized org slug will raise an error. This is helpful if you wish to restrict the set of organizations under which course runs and content libraries may be created.
  - The FEATURES['ORGANIZATIONS_APP'] is no longer supported.
    - The Organization and OrganizationCourse model are now available on all instances.
    - If you previously enabled FEATURES['ORGANIZATIONS_APP'], then you should override the Studio setting ORGANIZATIONS_AUTOCREATE to Falsewhen upgrading to Lilac to achieve the same functionality.
  - Added Studio management command: ./manage.py cms backfill_orgs_and_org_courses
    - This back-populates the organizations_organization and organizations_organizationcourse tables, for Open edX instances that did not previously enable FEATURES['ORGANIZATIONS_APP'].
    - It is not critical to run this for the Lilac upgrade, since no features depend on these tables being populated yet.
    - However, future releases may make use of the data in these tables; hence, it is best to run the backfill now.

Certificates
------------

- Various bug fixes and updates around course certificate generation
  - In an effort to be more inclusive, code referencing the course CertificateWhitelist model is being updated to instead refer to a Certificate Allowlist. The model itself has not yet been renamed.
  - Temporary CourseWaffleFlag added to control access to updated behavior of the CertificateWhitelist (aka Certificate Allowlist)
  - Temporary CourseWaffleFlag added to control access to updated behavior of the course certificates
  - The management command named create_fake_cert has been removed. The Certificate Allowlist should be used in its place.
  - The management command named gen_cert_report has been removed. To view the status of generated course certificates, query the certificates_generatedcertificate database table.
  - A user can no longer be added to both the Certificate Allowlist (meaning the user should be granted certificate) and the Certificate Invalidation list (meaning the user should not be granted a certificate) for the same course run.
  - Removal of the allow_certificate field on the UserProfile model has begun

- Added a new export-course-metadata-to-storage feature. In order to use it set COURSE_METADATA_EXPORT_BUCKET and COURSE_METADATA_EXPORT_STORAGE. Useful for external services you might have that want to scrape course data.'

Deprecations
------------

- The sysadmin dashboard is no longer supported.
  - The feature has been deprecated according to DEPR-118, Its ADR can be found at ADR-DEPR-118 and related discussions at Discussion-DEPR-118.
  - The related feature flag FEATURES['ENABLE_SYSADMIN_DASHBOARD'] is also removed.
  - A separate pluggable app named edx-sysadmin has been developed at and can be used as an alternative to sysadmin dashboard.

- CourseTalk integration has been removed.

- Xblock URL token signing can now be migrated to use a new multi-key mechanism rather than being tied to SECRET_KEY. It is recommended that you perform this migration, as it permits easier rotation of SECRET_KEY.

Branding Update
---------------
Open edX logos, colors and fonts have been updated.

=============================
Researcher & Data Experiences
=============================

  - Tracking metrics based on the anonymized session ID will experience a discontinuity or other anomaly at the time of deployment, as the anonymized IDs will change. [PR] This will likely appear as if everyone logged out and back in again, although only from a metrics perspective. In a green-blue deployment scenario, it may briefly appear as if there are twice as many sessions active.

=====================
Developer Experiences
=====================

- Import unqualified packages from lms/djangoapps, cms/djangoapps, or common/djangoapps is no longer supported. Doing so will cause instances of import_shims.warn.DeprecatedEdxPlatformImportError to be raised. See https://github.com/edx/edx-platform/blob/master/docs/decisions/0007-sys-path-modification-removal.rst  for details and context.

- In common.djangoapps.student.models, the save parameter is deprecated for functions anonymous_id_for_user and unique_id_for_user, and these functions will always save generated IDs to the database. This allows future decoupling of ID generation from SECRET_KEY. Including the parameter will result in a DeprecationWarning; after Lilac we plan to remove the parameter (which will be a separate breaking change – DEPR-148).

.. include:: links.rst
.. include:: ../../links/links.rst
