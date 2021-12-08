.. _Open edX Maple Release:

######################
Open edX Maple Release
######################

This section describes how to install the Open edX Maple release.

.. contents::
 :local:
 :depth: 1

************************
What's Included in Maple
************************

The Open edX Maple release contains several new features for learners,
course teams, and developers. For more information, see the
`Open edX Platform Release Notes`__.

__ http://edx.readthedocs.io/projects/open-edx-release-notes/en/latest/maple.html


**************************
What Is the Maple Git Tag?
**************************

A git tag identifies the version of Open edX code that is the Maple release.
About three dozen repositories are tagged as part of an Open edX release. Many
other repositories are installed as dependencies of those repositories. You can
find the most up-to-date git tag for Maple on the
`Open edX Named Releases page`_.

****************************
Installing the Maple Release
****************************

TODO: Write this for Tutor.

Maple releases have git tag names like ``open-release/maple.1``.
The available names are detailed on the `Open edX Named Releases page`_.

******************************
Upgrading from the Koa Release
******************************

TODO: This needs to be written for Tutor.


***************************************
Upgrading to a Subsequent Maple Release
***************************************

Occasionally, we release updates to Maple.  For example, the second
release of Maple will be ``open-release/maple.2``.
The steps to upgrade differ based on your original installation method.

===============================
Upgrading a Docker Installation
===============================

Devstack is installed using Docker. To upgrade from one Maple
release to another, follow the instructions in `devstack`_.

===============================
Upgrading a Native Installation
===============================

If you installed Open edX using the `Open edX Native Installation`_, you can
upgrade from one Maple release to another by re-running those steps using
your desired Maple tag as the new value for ``OPENEDX_RELEASE``.


.. include:: ../../../links/links.rst
