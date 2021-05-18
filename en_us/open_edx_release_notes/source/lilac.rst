.. _Open edX Lilac Release:

######################
Open edX Lilac Release
######################

These are the release notes for the Lilac release, the 12th community release of the Open edX Platform, spanning changes from November 12 2020 to April 9 2021.  You can also review details about `earlier releases`_ or learn more about the `Open edX Platform`_ if you are new to Open edX.

.. _earlier releases: https://edx.readthedocs.io/projects/edx-developer-docs/en/latest/named_releases.html
.. _Open edX Platform: https://open.edx.org

.. contents::
 :depth: 1
 :local:

===================
Learner Experiences
===================

Account Micro FrontEnd
-----------
The Account MFE is enabled by default and provides private user settings UIs, including:

- Account settings page
- Demographics collection
- IDV (Identity Verification)

Checkout Micro FrontEnd
------------
The Checkout MFE is enabled by default. Prior checkout UIs are not PCI compliant.

Learning Micro FrontEnd
------------
The Learning MFE is *not* enabled by default, because theming and internationalizations support is incomplete. However, we expect that this is the last named release to support the Legacy courseware frontend.

If the Learning MFE is installed using the MFE Deployer Ansible role then certain features can be opted in to the Micro-Frontend. These LMS CourseWaffleFlags can be toggled on (globally, per-user, or per-course) to switch certain features over the Learning MFE:

- courseware.courseware_mfe : Enable to host courseware (ie, the learning sequence experience) in the MFE.
- courseware.microfrontend_course_team_preview : Enable to show global and course-level staff members the ability to preview courseware in the MFE. Does not affect learners.
- course_home.course_home_mfe : Enable in conjunction with one or more of the following:

  - course_home.course_home_mfe_dates_tab : Display the “Dates” course tab in the MFE.
  - course_home.course_home_mfe_outline_tab : Display the course outline (the target of the “Course” course tab) in the MFE.
  - course_home.course_home_mfe_progress_tab: Display the “Progress” course tab in the MFE.

Course Completion Milestone
---------------------------

Mobile Experience
-----------------

- Improved mobile support for Open Response Assessment (ORA)
- Mobile support for drag-and-drop xBlock


=====================
Authoring Experiences
=====================

Proctortrack Onboarding Status Menu
-----------------------------------

Gradebook MFE
-------------
The Gradebook MFE is *not* enabled by default because theming and internationalizations support is incomplete. It allows editing of individual learners' grades. Also supports bulk uploads of grades, but requires additional configuration. See https://github.com/edx/frontend-app-gradebook/blob/open-release/lilac.master/README.md for more information.


=========================
Administrator Experiences
=========================

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

Changes to certificates
-----------------------

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
