.. _Open edX Ficus Release:

######################
Open edX Ficus Release
######################

This section describes the Open edX Ficus release. Note that edX no longer 
supports the Ficus relesae. 

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
release to another, run the following commands in the host operating system:

.. code-block:: bash

    $ export OPENEDX_RELEASE=open-release/ficus.2
    $ vagrant provision

===============================
Upgrading a Native Installation
===============================

If you installed Open edX using the `Legacy Open edX Native Installation`_, you can
upgrade from one Ficus release to another by re-running those steps using your
desired Ficus tag as the new value for ``OPENEDX_RELEASE``.


.. include:: ../../../links/links.rst
