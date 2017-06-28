.. _Open edX Gingko Release:

#########################
Open edX Gingko Release
#########################

This page lists the highlights of the Gingko release.

.. contents::
 :depth: 1
 :local:

************
New Features
************

The Open edX Gingko release includes the following updates.

.. contents::
 :depth: 1
 :local:


===
LMS
===

*

===========
Discussions
===========

*

============================
Studio & Course Author Tools
============================

*

*


***************************************************
Updates to Analytics Events and Database Tables
***************************************************

*


***********************
Accessibility Updates
***********************

In keeping with edX's commitment to creating accessible content for everyone,
everywhere, the Open edX Gingko release contains numerous accessibility
enhancements and improvements to readability and navigability.

.. contents::
 :depth: 1
 :local:

*



*******************************
System Upgrades and Updates
*******************************

Something about the upgrade path


.. list-table::
   :widths: 60 40
   :header-rows: 1

   * - System
     - Upgraded Version
   * - Catalog Service
     - Django 1.11.x
   * - Credentials Service
     - Django 1.11.x
   * - E-Commerce Service
     - Django 1.10.x
   * - Search
     - ElasticSearch 1.5
   * - Node
     - Node 6.9

* Webpack is now supported. [link to something about Webpack]
* ESLink is now used for JavaScript linting. The edX rules are defined in
   https://github.com/edx/eslint-config-edx . Packages are provided for ES5 and
   ES2015+. See [ESLint|https://openedx.atlassian.net/wiki/display/FEDX/ESLint]
   for more details


***********************
Deprecated Features
***********************

Several features are deprecated, or deleted, by the Open edX Gingko release.

* The Programs was deprecated in Ficus. It has been replaced by the Catalog
  service in Ginkgo.
* The Credentials API V2 has replaced the Credentials API V1, which has been
  removed.
* The waffle flag ``unified_course_view``, which can be used for the new view
  of the course outline on a separate page, is deprecated in Ginkgo.  The old
  sidebar navigation and this waffle flag will be fully removed in the next
  release. This is currently defaulted off, but we'd like to get it defaulted
  on for Ginkgo.


************************************************
More Information on Gingko Release Changes
************************************************

The `edX Release Notes`_ contain a summary of changes that are deployed to
edx.org. Those changes are part of the master branch of the edX Platform in
GitHub.  You can also find `release announcements`_ on the open.edx.org
website.

Changes listed for [DATE] 2017 and before are included in the Gingko release
of Open edX.  Changes after that point will be in future Open edX releases.

.. include:: links.rst
.. include:: ../../links/links.rst
