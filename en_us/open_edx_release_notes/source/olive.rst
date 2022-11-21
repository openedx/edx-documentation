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


All grades are persisted
------------------------
The Persistent Grades feature was added as an option in Hawthorne. Legacy, non-persistent grades were deprecated in Nutmeg. Now, persistent grades are required. If you have not turned on persistent grades in your installation yet, you will need to follow the instructions in `How to Enable Persistent Grades`_. This process can take a significant amount of time, depending on how many graded problems are in your installation, and how long those grades take to be calculated. It can be run before or after the upgrade.

.. _How to Enable Persistent Grades: https://openedx.atlassian.net/wiki/spaces/AC/pages/755171487/WIP+How+to+Enable+Persistent+Grades+in+Hawthorne

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

.. _Learner Records MFE README: https://github.com/openedx/frontend-app-learner-record/blob/open-release/olive.master/README.rst


Administrators & Operators
==========================

- fixed a performance issue when using multiple themes when running in docker. Now by using LRU cache when searching themes,  the performance was improved.


Deprecations & Removals
=======================

Legacy learner experience
-------------------------
A few pieces of the legacy/deprecated learner experience have been removed entirely in favor of the Learning MFE experience, specifically, the outline, dates, and courseware tabs. Instead, you must run the Learning MFE, and its tabs will be used. Along with the legacy code, a few old waffle flags have been removed: :code:`course_experience.latest_update`, :code:`course_experience.show_upgrade_msg_on_course_home`, :code:`course_experience.upgrade_deadline_message`, :code:`course_home.course_home_use_legacy_frontend`, :code:`courseware.microfrontend_course_team_preview`, and :code:`courseware.use_legacy_frontend`.

Other removals/deprecations
---------------------------

- The `frontend-learner-portal-base repo`_ has been archived. Any MFEs that depend on this library have been updated
- `Removed the last vestiges of the save option from anonymous_id_for_user`_

.. _frontend-learner-portal-base repo: https://github.com/openedx-unsupported/frontend-learner-portal-base
.. _Removed the last vestiges of the save option from anonymous_id_for_user: https://github.com/openedx/public-engineering/issues/35


.. include:: links.rst
.. include:: ../../links/links.rst

