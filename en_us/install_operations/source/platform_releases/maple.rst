.. _Open edX Maple Release:

######################
Open edX Maple Release
######################

.. warning::

    This release is unsupported.

    The `Open edX Named Releases page`_ and the `Open edX Releases Homepage`_ are the
    authoratative sources of information on all Open edX releases. It is *strongly*
    recommended to operate off the latest Open edX release at all points in time, as
    only the most recent release is community-supported.

    See the `Open edX Release Schedule`_ for information on release dates and end-of-life
    support.

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

__ https://docs.openedx.org/en/latest/community/release_notes/maple.html


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

.. warning::

    This release is unsupported.

See `Tutor installation instructions <https://docs.tutor.edly.io/gettingstarted.html>`_.

Maple releases have git tag names like ``open-release/maple.1``.
The available names are detailed on the `Open edX Named Releases page`_.

*********************************
Upgrading from the Lilac Release
*********************************

See `Tutor upgrade instructions <https://docs.tutor.edly.io/tutorials/oldreleases.html>`_.


***************************************
Upgrading to a Subsequent Maple Release
***************************************

Occasionally, we release updates to Maple.  For example, the second
release of Maple will be ``open-release/maple.2``.
The steps to upgrade differ based on your original installation method.

===============================
Upgrading a Docker Installation
===============================

The `devstack`_ installation method is deprecated. It is recommended
to migrate to Tutor. See `Tutor installation instructions <https://docs.tutor.edly.io/gettingstarted.html>`_.

===============================
Upgrading a Native Installation
===============================

If you installed Open edX using the Open edX Native Installation, please
migrate to Tutor. This `Native Installation to Tutor forum post`_ may be helpful,
as may be `this second Native to Tutor post`_. If not, post on the `Open edX Forums`_.

If you installed Open edX using the Open edX Native Installation, you can
upgrade from one Maple release to another by re-running those steps using
your desired Maple tag as the new value for ``OPENEDX_RELEASE``.


.. include:: ../../../links/links.rst
