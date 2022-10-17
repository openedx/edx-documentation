.. _Open edX Olive Release:

######################
Open edX Olive Release
######################

This section describes how to install the Open edX Olive release.

.. contents::
 :local:
 :depth: 1

*************************
What's Included in Olive
*************************

The Open edX Olive release contains several new features for learners,
course teams, and developers. For more information, see the
`Open edX Platform Release Notes`__.

__ http://edx.readthedocs.io/projects/open-edx-release-notes/en/latest/olive.html

**************************
What Is the Olive Git Tag?
**************************

A git tag identifies the version of Open edX code that is the Olive release.
Over fourty repositories are tagged as part of an Open edX release. Many
other repositories are installed as dependencies of those repositories. You can
find the most up-to-date git tag for Olive on the
`Open edX Named Releases page`_.

****************************
Installing the Olive Release
****************************

TODO: Write this for Tutor.

Olive releases have git tag names like ``open-release/olive.1``.
The available names are detailed on the `Open edX Named Releases page`_.

*********************************
Upgrading from the Nutmeg Release
*********************************

TODO: This needs to be written for Tutor.

***************************************
Upgrading to a Subsequent Olive Release
***************************************

Occasionally, we release updates to Olive.  For example, the second
release of Olive will be ``open-release/olive.2``.
The steps to upgrade differ based on your original installation method.

===============================
Upgrading a Docker Installation
===============================

Devstack is installed using Docker. To upgrade from one Olive
release to another, follow the instructions in `devstack`_.


.. include:: ../../../links/links.rst
