.. _Open edX Platform Installation Options:

########################################
Open edX Platform Installation Options
########################################

This section describes Open edX installation options and the components that
each option includes. There are two virtual machine options, which install
the Open edX software in a virtual Ubuntu machine. If you prefer, you can
install into an Ubuntu machine of your own using the Native installation.


.. contents::
 :local:
 :depth: 1

**********************************
Open edX Platform Virtual Machines
**********************************

You can install the Open edX developer stack (**devstack**) or the Open edX
analytics developer stack (**analytics devstack**).

* Devstack is a Docker virtual machine instance designed for local
  development. For more information, see :ref:`Info Devstack`.

* Analytics devstack is a modified version of the devstack virtual machine that
  allows you to run Open edX Analytics. For more information, see
  :ref:`Info Analytics Devstack`.

You can run Devstack or Analytics Devstack on Linux or Mac OS. See the
`Docker`_ downloads page for information about the operating systems and
architectures on which you can run Docker.

.. _Info Devstack:

=================
Open edX Devstack
=================

Devstack is a deployment of the Open edX platform within a Docker instance
designed for local development. Running the Open edX platform locally allows
you to discover and fix system configuration issues early in development.

Devstack simplifies certain production settings to make development more
convenient. For example, `nginx`_ and `gunicorn`_ are disabled in devstack;
devstack uses Django's ``runserver`` instead.

.. note::
  Because of the large number of dependencies needed to develop extensions to
  Open edX Insights, a separate development environment is available to support
  Analytics development. For more information, see :ref:`Installing and
  Starting Analytics Devstack`.

For more information about Docker, see the `Docker documentation`_.

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

.. How has this changed, if at all?

A devstack installation includes the following Open edX components:

* The Learning Management System (LMS)
* Open edX Studio
* Discussion Forums
* Open Response Assessments (ORA)
* E-Commerce
* Programs
* A demonstration Open edX course
* Open edX Search

Analytics devstack also includes the following Open edX components:

* Open edX Analytics Data API
* Open edX Insights
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

The default password for all of these accounts is ``edx``.

.. _vm_installation_options:

*************************************
Virtual Machine Configuration Options
*************************************

When you install devstack or analytics devstack you can customize
the environment. This section provides information about configuration options
for Open edX virtual machines.

================================================
Set Up Ability to Preview Units (Mac/Linux Only)
================================================

If you are installing an Open edX virtual machine on a Linux or Mac computer,
you must configure your installation to use the preview feature in Open edX
Studio.

#. :ref:`Connect to the devstack virtual machine<Connect to Devstack VM>`.

#. In the ``/etc/hosts`` file, add the following line.

  .. code-block:: bash

    192.168.33.10 preview.localhost

===================================
Customize the Source Code Location
===================================

>>> WHAT IS THE DOCKER EQUIVALENT?

You can customize the location of the Open edX source code that gets cloned
when you provision a devstack instance. You may want to do this to have the
Open edX virtual machine work with source code that already exists on your
computer.

By default, the source code location is the directory in which you run
``vagrant up``. To change this location, follow these steps.

#. :ref:`Connect to the Devstack virtual machine<Connect to Devstack VM>`.

#. Set the ``VAGRANT_MOUNT_BASE`` environment variable to set the base
   directory for the ``edx-platform`` and ``cs_comments_service`` source code
   directories.

.. include:: ../../../links/links.rst
