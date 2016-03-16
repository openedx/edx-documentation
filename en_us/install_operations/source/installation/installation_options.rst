.. _Open edX Platform Installation Options:

########################################
Open edX Platform Installation Options
########################################

This section describes Open edX installation options and the components that
each option includes.

.. contents::
 :local:
 :depth: 1

********************
Platform Options
********************

You can install the Open edX developer stack (**devstack**), the Open edX full
stack (**fullstack**), or the Open edX analytics developer stack (**analytics
devstack**).

* Devstack is a Vagrant instance designed for local development. For more
  information, see :ref:`Info Devstack`.

* Fullstack is a Vagrant instance designed for deploying all edX services on a
  single server. For more information, see :ref:`Info Fullstack`.

* Analytics devstack is a modified version of the Open edX developer stack
  (devstack) that allows you to run edX Analytics. For more information, see
  :ref:`Info Analytics Devstack`.

.. _Info Devstack:

==============================
Open edX Devstack
==============================

Devstack is a Vagrant instance designed for local development. Devstack has
the same system requirements as :ref:`Fullstack <Installing Open edX
Fullstack>`. This allows you to discover and fix system configuration issues
early in development.

Devstack simplifies certain production settings to make development more
convenient. For example, `nginx`_ and `gunicorn`_ are disabled in devstack;
devstack uses Django's runserver instead.

Devstack is in the `edx configuration repository`_ on GitHub.

For information about devstack and other installation and configuration options
from edX and the Open edX community, see the `edx configuration repository
wiki`_. Specifically, the following pages have more information about devstack.

* `Devstack wiki`_
* `Developing on Devstack`_

.. note::
  Because of the large number of dependencies needed to develop extensions to
  Open edX Insights, a separate development environment is available to support
  Analytics development. For more information, see * :ref:`Installing and
  Starting Analytics Devstack`.

For more information about Vagrant, see the `Vagrant documentation`_.

.. _Info Fullstack:

====================
Open edX Fullstack
====================

Fullstack is a Vagrant instance designed for deploying all edX services on a
single server. Fullstack is in the `edx configuration repository`_ on GitHub.

For information about fullstack and other installation and configuration
options from edX and the Open edX community, see the
`edx configuration repository wiki`_.

For more information about Vagrant, see the `Vagrant documentation`_.

Ubuntu 12.04 64
*********************

You can install fullstack on a single Ubuntu 12.04 64-bit server. More Ubuntu
information is planned for future versions of this guide.

For information about Ubuntu and other installation and configuration
optionsfrom edX and the Open edX community, see the
`edx configuration repository wiki`_.

.. _Info Analytics Devstack:

========================================
Open edX Analytics Devstack
========================================

Some users might want to develop Analytics features on their instance of the
Open edX platform. Because of the large number of dependencies needed to
develop extensions to Analytics, edX has created a separate developer stack,
known as analytics devstack. We strongly recommend that you install the
Analytics Devstack instead of adding Analytics extensions to an instance of
devstack.

Analytics devstack is a modified version of the :ref:`Open edX developer
stack<Info Devstack>`. This development environment provides all of the
services and tools needed to modify the Open edX Analytics Pipeline, Data API,
and Insights projects.

********************
Components
********************

Fullstack, devstack, and analytics devstack all include the following edX
components.

* The Learning Management System (LMS).
* edX Studio.
* Discussion Forums.
* Open Response Assessments (ORA).

Devstack also includes the following edX components.

* A demonstration edX course.
* EdX Search.

Fullstack also includes the following edX components.

* XQueue, the queuing server that uses `RabbitMQ`_ for external graders.
* `Discern`_, the machine-learning-based automated textual classification API
  service.
* `Ease`_, a library for the classification of textual content.

Analytics devstack also includes the following edX components.

* edX Analytics Data API.
* edX Insights.
* The components needed to run the Open edX Analytics Pipeline. This is the
  primary extract, transform, and load (ETL) tool that extracts and analyzes
  data from the other Open edX services.

.. _Default Accounts:

=========================
Default Accounts
=========================

When you install devstack, fullstack, or analytics devstack, the following
user accounts are created by default.

  .. list-table::
   :widths: 20 60
   :header-rows: 1

   * - Account
     - Description
   * - ``staff@example.com``
     - An LMS and Studio user with course creation and editing permissions.
       This user is a course team member with the Admin role, which gives
       rights to work with the demonstration course in Studio, the LMS, and
       Insights.
   * - ``verified@example.com``
     - A student account that you can use to access the LMS for testing
       verified certificates.
   * - ``audit@example.com``
     - A student account that you can use to access the LMS for testing course
       auditing.
   * - ``honor@example.com``
     - A student account that you can use to access the LMS for testing honor
       code certificates.

The password for all of these accounts is ``edx``.

.. include:: ../../../links/links.rst
