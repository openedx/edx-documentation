.. _Open edX Nutmeg Release:

#######################
Open edX Nutmeg Release
#######################

This section describes how to install the Open edX Nutmeg release.

.. contents::
 :local:
 :depth: 1

*************************
What's Included in Nutmeg
*************************

The Open edX Nutmeg release contains several new features for learners,
course teams, and developers. For more information, see the
`Open edX Platform Release Notes`__.

__ http://edx.readthedocs.io/projects/open-edx-release-notes/en/latest/nutmeg.html


***************************
What Is the Nutmeg Git Tag?
***************************

A git tag identifies the version of Open edX code that is the Nutmeg release.
About three dozen repositories are tagged as part of an Open edX release. Many
other repositories are installed as dependencies of those repositories. You can
find the most up-to-date git tag for Nutmeg on the
`Open edX Named Releases page`_.

*****************************
Installing the Nutmeg Release
*****************************

TODO: Write this for Tutor.

Nutmeg releases have git tag names like ``open-release/nutmeg.1``.
The available names are detailed on the `Open edX Named Releases page`_.

********************************
Upgrading from the Maple Release
********************************

TODO: This needs to be written for Tutor.


****************************************
Upgrading to a Subsequent Nutmeg Release
****************************************

Occasionally, we release updates to Nutmeg.  For example, the second
release of Nutmeg will be ``open-release/nutmeg.2``.
The steps to upgrade differ based on your original installation method.

===============================
Upgrading a Docker Installation
===============================

Devstack is installed using Docker. To upgrade from one Nutmeg
release to another, follow the instructions in `devstack`_.

===============================
Upgrading a Native Installation
===============================

If you installed Open edX using the `Open edX Native Installation`_, you can
upgrade from one Nutmeg release to another by re-running those steps using
your desired Nutmeg tag as the new value for ``OPENEDX_RELEASE``.


.. include:: ../../../links/links.rst
