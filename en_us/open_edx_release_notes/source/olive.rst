.. _Open edX Olive Release:

######################
Open edX Olive Release
######################

These are the release notes for the Olive release, the 15th community release of the Open edX Platform, spanning changes from April 11 2022 to October 11 2022.  You can also review details about `earlier releases`_ or learn more about the `Open edX Platform`_.

.. _earlier releases: https://edx.readthedocs.io/projects/edx-developer-docs/en/latest/named_releases.html
.. _Open edX Platform: https://openedx.org

.. contents::
 :depth: 1
 :local:

Breaking Changes
================


Learning MFE is now required
----------------------------
The Learning Micro Frontend (MFE) is no longer optional, and must be run as part of your installation now. It has been the default since the Maple release, with a setting that allowed for opting out. The setting :code:`courseware.use_legacy_frontend` has been removed. (See Deprecations & Removals below for more).


Learner Experiences
===================


Learner Records Micro-frontend (MFE)
------------------------------------

- The Learner records MFE is now available as an optional frontend for the Credentials application (or is it a plugin?). See the `Learner Records MFE README`_ for configuration information.
- Even if the the Learner Records MFE is turned on, the old UI is still used for public links to records. This will be changed in the Palm release. (this may have been backported already)
- Masquerading is not supported, as it is in the legacy UI. Use the "Records" tab in support tools as an alternative.

.. _Learner Records MFE README : https://github.com/openedx/frontend-app-learner-record/blob/open-release/olive.master/README.rst

Deprecations & Removals
=======================

Legacy learner experience
-------------------------
A few pieces of the legacy/deprecated learner experience have been removed entirely in favor of the Learning MFE experience, specifically, the outline, dates, and courseware tabs. Instead, you must run the Learning MFE, and its tabs will be used. Along with the legacy code, a few old waffle flags have been removed: course_experience.latest_update, course_experience.show_upgrade_msg_on_course_home, course_experience.upgrade_deadline_message, course_home.course_home_use_legacy_frontend, courseware.microfrontend_course_team_preview, and  @Michael Terry (Deactivated)


.. include:: links.rst
.. include:: ../../links/links.rst

