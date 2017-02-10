.. _Open edX Ficus Release:

######################
Open edX Ficus Release
######################

This section describes how to install the Open edX Ficus release.

.. contents::
 :local:
 :depth: 1

************************
What's Included in Ficus
************************

The Open edX Ficus release contains several new features for learners,
course teams, and developers. For more information, see
:ref:`openreleasenotes:Open edX Ficus Release`.

**************************
What Is the Ficus Git Tag?
**************************

A git tag identifies the version of Open edX code that is the Ficus release.
You can find the most up-to-date git tag for the current Open edX release on
the `Open edX Releases Wiki page`_.

The following Open edX git repositories have the Ficus git tag:

* edx-platform
* configuration
* cs_comments_service
* xqueue
* ecommerce
* ecommerce-worker
* edx-analytics-configuration
* edx-analytics-dashboard
* edx-analytics-data-api
* edx-analytics-pipeline
* edx-certificates
* edx-custom-a11y-rules
* edx-demo-course
* edx-documentation
* edx-notes-api
* edx-ui-toolkit
* notifier
* programs
* ux-pattern-library

****************************
Installing the Ficus Release
****************************

You can install the Open edX Ficus release using :ref:`Devstack <Installing
the Open edX Developer stack>` or :ref:`Fullstack <Installing Open edX Fullstack>`.

Review the prerequisites and instructions for each option, and then choose the
option that best meets your needs. Ensure that you install the
required software to run the Open edX platform.

Ficus releases have git tag names like ``open-release/ficus.1``.
The available names are detailed on the `Open edX Releases Wiki page`_.

Previous releases ran on Ubuntu 12.04, but Ficus runs on 16.04.  Because of the
change in operating system, edX is not providing an upgrade path.  If you have
an existing Eucalyptus installation, you must install Ficus on a new
machine, and move your data and settings to it.


***************************************
Upgrading to a Subsequent Ficus Release
***************************************

Occasionally, we release updates to Ficus.  For example, the second 
release of Ficus is ``open-release/ficus.2``.
The steps to upgrade differ based on your original installation method.

================================
Upgrading a Vagrant Installation
================================

Devstack and Fullstack are installed using Vagrant.  To upgrade from one Ficus
release to another, follow these steps in the host operating system:

.. code-block:: bash

    $ export OPENEDX_RELEASE=open-release/ficus.2
    $ vagrant provision

===============================
Upgrading a Native Installation
===============================

If you installed Open edX using the `Open edX Native Installation`_, you can
upgrade from one Ficus release to another by re-running those steps using your
desired Ficus tag as the new value for ``OPENEDX_RELEASE``.


.. include:: ../../../links/links.rst
