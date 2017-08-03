.. _Open edX Ginkgo Release:

#########################
Open edX Ginkgo Release
#########################

This page lists the highlights of the Ginkgo release.

.. contents::
 :depth: 1
 :local:

************
New Features
************

The Open edX Ginkgo release includes the following updates.

.. contents::
 :depth: 1
 :local:


===
LMS
===

*  The Course page now opens to a course outline that serves as the basis for a
   new course home experience. This course outline replaces the course outline
   sidebar on course content pages that listed sections and subsections. It
   allows learners to focus on content consumption and progression through the
   course. For more information, see `Course Navigation Changes`_ on the Open
   edX portal.
*  Search functionality is available on the **Outline** page.
*  Course staff can now send emails to learners based on their enrollment track.
*  Drag and drop problems can be rescored.


============================
Studio & Course Author Tools
============================

* The default permissions have been changed so that new Studio users cannot
  author courses unless an admin has added them to the course creator group.

=======================
Catalog Service
=======================

The Catalog service has been upgraded to RabbitMQ 3.6.9.

=======================
Credentials Service
=======================

The Credentials service now requires Python 3.5.

======================
E-Commerce Service
======================

* Receipt page - The receipt page integrated into Otto is the only receipt page
  that is supoorted. Redirecting to the ``LMS/shopping_cart`` receipt page is no
  longer enabled.

* CyberSource - Secure Acceptance Silent Order POST is the only supported
  CyberSource integration. Using this integration requires creating a new profile
  in the business center. >> What is the business center?

* The merchant notifications endpoint has been removed.

* Django Oscar has been upgraded to version 1.4. See Upgrading Django Oscar for
  information about migrating an existing installation to the new version.

* The Course Administration Tool has been updated to use the user account
  associated with the OAuth credentials rather than individual users' accounts.
  The user associated with the OAuth credentials (at edx.org, we use the
  username ``ecommerce_worker``) needs to have full CRUD permissions for the
  following models on LMS:
     * ``commerce.CommerceConfiguration``
     * ``course_modes.CourseMode``
     * ``credit.CreditCourse``
     * ``credit.CreditRequest``
  In addition, if you are using SDN verification, this user nneds to have the
  ``student:userprofile:can_deactivate_users`` permission.

=======================
Insights and Analytics
=======================

*  A new **Courses** page in Insights provides a dashboard view of all of your
   courses.

*  Updates to Insights requires a series of migration steps to account for changes
   to ``social-auth``. For information, see >>Migration doc.

*******************************
System Upgrades and Updates
*******************************

>> Something about the upgrade path


.. list-table::
   :widths: 60 40
   :header-rows: 1

   * - System
     - Upgraded Version
   * - Catalog Service
     - Django 1.11.x
   * - Credentials Service
     - Django 1.11.x
   * - Django Waffle
     - 0.12.0
   * - E-Commerce Service
     - Django 1.10.x
   * - Search
     - ElasticSearch 1.5
   * - Node
     - Node 6.9
   * - xblock-lti-consumer
     - 1.1.5

* Webpack, a JavaScript module bundler, is now supported in Studio and the LMS.
  See `Webpack`_ for more information.

* ESLint is now used for JavaScript linting. The edX rules are defined in
  https://github.com/edx/eslint-config-edx . Packages are provided for ES5 and
  ES2015+. See `ESLint`_ for more details.


***********************
Deprecated Features
***********************

Several features are deprecated or deleted, by the Open edX Ginkgo release.

* The Programs service was deprecated in Ficus. It has been replaced by the Catalog
  service in Ginkgo.
* The Credentials API V2 has replaced the Credentials API V1, which has been
  removed.
* The waffle flag ``unified_course_view``, which can be used for the new view
  of the course outline on a separate page, is deprecated in Ginkgo.  The old
  sidebar navigation and this waffle flag will be fully removed in the next
  release. >> This is currently defaulted off, but we'd like to get it defaulted
  on for Ginkgo.


************************************************
More Information on Ginkgo Release Changes
************************************************

The `edX Release Notes`_ contain a summary of changes that are deployed to
edx.org. Those changes are part of the master branch of the edX Platform in
GitHub. You can also find `release announcements`_ on the open.edx.org
website.

Changes listed for July 7, 2017 and before are included in the Ginkgo release
of Open edX. Changes after that point will be in future Open edX releases.

.. include:: links.rst
.. include:: ../../links/links.rst
