.. _Open edX Platform Installation Options:

########################################
Open edX Platform Installation Options
########################################

This section describes Open edX installation options and the components that
each option includes. More details about the various options are at the
`Open edX Installation Options`_ page on the edX wiki.

There are a three virtual machine options, which install the Open edX
software in a virtual Ubuntu machine.  If you prefer, you can install into an
Ubuntu machine of your own using the Native installation.

.. contents::
 :local:
 :depth: 1

**********************************
Open edX Platform Virtual Machines
**********************************

You can install the Open edX developer stack (**devstack**), the Open edX full
stack (**fullstack**), or the Open edX analytics developer stack (**analytics
devstack**).

* Devstack is a Vagrant virtual machine instance designed for local
  development. For more information, see :ref:`Info Devstack`.

* Fullstack is a Vagrant virtual machine instance designed for installing all
  Open edX services on a single server in a production-like configuration. For
  more information, see :ref:`Info Fullstack`.

* Analytics devstack is a modified version of the devstack virtual machine that
  allows you to run Open edX Analytics. For more information, see
  :ref:`Info Analytics Devstack`.

.. _Info Devstack:

=================
Open edX Devstack
=================

Devstack is a Vagrant instance designed for local development. Devstack has
the same system requirements as :ref:`Fullstack <Installing Open edX
Fullstack>`. This allows you to discover and fix system configuration issues
early in development.

Devstack simplifies certain production settings to make development more
convenient. For example, `nginx`_ and `gunicorn`_ are disabled in devstack;
devstack uses Django's runserver instead.

For information about devstack and other installation and configuration options
from edX and the Open edX community, see the `Open edX Installation Options`_
page on the edX wiki.

.. note::
  Because of the large number of dependencies needed to develop extensions to
  Open edX Insights, a separate development environment is available to support
  Analytics development. For more information, see :ref:`Installing and
  Starting Analytics Devstack`.

For more information about Vagrant, see the `Vagrant documentation`_.

.. _Info Fullstack:

==================
Open edX Fullstack
==================

Fullstack is a Vagrant instance designed for installing all Open edX services
on a single server in a production-like configuration.  Fullstack is a
pre-packaged Native installation running in a Vagrant virtual machine.

For information about fullstack and other installation and configuration
options from edX and the Open edX community, see the `Open edX Installation
Options`_ page on the edX wiki.

For more information about Vagrant, see the `Vagrant documentation`_.


.. _Info Analytics Devstack:

===========================
Open edX Analytics Devstack
===========================

Some users might want to develop Analytics features on their instance of the
Open edX platform. Because of the large number of dependencies needed to
develop extensions to Analytics, edX has created a separate developer stack,
known as analytics devstack. We strongly recommend that you install the
analytics devstack instead of adding Analytics extensions to an instance of
devstack.

Analytics devstack is a modified version of the :ref:`Open edX developer
stack<Info Devstack>`. This development environment provides all of the
services and tools needed to modify the Open edX Analytics Pipeline, Data API,
and Insights projects.


*******************
Native Installation
*******************

The Native installation installs the Open edX software on your own Ubuntu 16.04
machine in a production-like configuration.  Details are at the `Open edX
Native Installation`_ page on the edX wiki.


*******************
Software Components
*******************

All installations include the following Open edX components:

* The Learning Management System (LMS).
* Open edX Studio.
* Discussion Forums.
* Open Response Assessments (ORA).

Devstack, fullstack and native installation also include:

* E-Commerce
* Programs
* A demonstration Open edX course.
* Open edX Search.

Fullstack and native also include the following Open edX components:

* Open edX Analytics Data API.
* Open edX Insights.
* Certificates
* XQueue, the queuing server that uses `RabbitMQ`_ for external graders.

Analytics devstack also includes the following Open edX components:

* Open edX Analytics Data API.
* Open edX Insights.
* The components needed to run the Open edX Analytics Pipeline. This is the
  primary extract, transform, and load (ETL) tool that extracts and analyzes
  data from the other Open edX services.

.. _Default Accounts:

================
Default Accounts
================

When you install an Open edX system, the following user accounts are created by
default.

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

.. _vm_installation_options:

*************************************
Virtual Machine Configuration Options
*************************************

When you install devstack, fullstack, or analytics devstack you can customize
the environment. This section provides information about configuration options
for Open edX virtual machines.

================================================
Set Up Ability to Preview Units (Mac/Linux Only)
================================================

If you are installing an Open edX virtual machine on a Linux or Mac computer, you
must configure your installation to use the preview feature in Open edX Studio.

#. :ref:`Connect to the Devstack virtual machine<Connect to Devstack VM>`.

#. In the ``/etc/hosts`` file, add the following line.

  .. code-block:: bash

    192.168.33.10 preview.localhost

===================================
Customize the Source Code Location
===================================

You can customize the location of the Open edX source code that gets cloned
when you provision a devstack. You may want to do this to have the Open edX
virtual machine work with source code that already exists on your computer.

By default, the source code location is the directory in which you run
``vagrant up``. To change this location, follow these steps.

#. :ref:`Connect to the Devstack virtual machine<Connect to Devstack VM>`.

#. Set the ``VAGRANT_MOUNT_BASE`` environment variable to set the base
   directory for the ``edx-platform`` and ``cs_comments_service`` source code
   directories.

.. include:: ../../../links/links.rst
