.. _Open edX Ginkgo Release:

########################
Open edX Ginkgo Release
########################

This section describes how to install the Open edX Ginkgo release.

.. contents::
 :local:
 :depth: 1

**************************
What's Included in Ginkgo
**************************

The Open edX Ginkgo release contains several new features for learners,
course teams, and developers. For more information, see
:ref:`openreleasenotes:Open edX Ginkgo Release`.

****************************
What Is the Ginkgo Git Tag?
****************************

A git tag identifies the version of Open edX code that is the Ginkgo release.
You can find the most up-to-date git tag for the current Open edX release on
the `Open edX Releases Wiki page`_.

The following Open edX git repositories have the Ginkgo git tag:

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

******************************
Installing the Ginkgo Release
******************************

You can install the Open edX Ginkgo release using :ref:`Devstack <Installing
the Open edX Developer stack>` or :ref:`Fullstack <Installing Open edX Fullstack>`.

Review the prerequisites and instructions for each option, and then choose the
option that best meets your needs. Ensure that you install the
required software to run the Open edX platform.

Ginkgo releases have git tag names like ``open-release/ginkgo.1``.
The available names are detailed on the `Open edX Releases Wiki page`_.

**********************************
Upgrading from the Ficus Release
**********************************

The best approach to upgrading an existing installation of the Open edX Ficus
release to the Ginkgo release is to make a fresh installation of the Ginkgo
release on a new machine, and move your data and settings to it. For more
information, see TBD.

***************************************
Upgrading to a Subsequent Ginkgo Release
***************************************

Occasionally, we release updates to Ginkgo.  For example, the second
release of Ginkgo will be ``open-release/ginkgo.2``.
The steps to upgrade differ based on your original installation method.

================================
Upgrading a Vagrant Installation
================================

Devstack and Fullstack are installed using Vagrant.  To upgrade from one Ginkgo
release to another, run the following commands in the host operating system:

.. code-block:: bash

    $ export OPENEDX_RELEASE=open-release/ginkgo.2
    $ vagrant provision

===============================
Upgrading a Native Installation
===============================

If you installed Open edX using the `Open edX Native Installation`_, you can
upgrade from one Ginkgo release to another by re-running those steps using your
desired Ginkgo tag as the new value for ``OPENEDX_RELEASE``.


.. include:: ../../../links/links.rst
