.. _Open edX Birch Release:

########################################
Open edX Birch Release
########################################

.. warning::

    This release is unsupported.

    The `Open edX Named Releases page`_ and the `Open edX Releases Homepage`_ are the
    authoratative sources of information on all Open edX releases. It is *strongly*
    recommended to operate off the latest Open edX release at all points in time, as
    only the most recent release is community-supported.

    See the `Open edX Release Schedule`_ for information on release dates and end-of-life
    support.

This section describes how to install the Open edX Birch release.

.. contents::
 :local:
 :depth: 1

.. note::
  edX no longer supports the Birch release.

******************************
What's Included in Birch
******************************

The Open edX Birch release contains several new features for students, course
teams, and developers.  See the Open edX Release Notes for more details.

.. Note::
 There are several new features in the Birch release that are available, but
 not configured in new installations.  For details, see the following topics.

 * :ref:`Enable Course Prerequisites`
 * :ref:`Enable Entrance Exams`

******************************
What is the Birch Git Tag?
******************************

The Git tag for the Birch release is **named-release/birch.2**. You use this tag
to identify the version of Open edX code that is the Birch release.

The following Open edX Git repositories have the Git tag **named-release/birch.2**:

* edx-platform
* configuration
* cs_comments_service
* notifier
* edx-certificates
* xqueue
* edx-documentation
* edx-ora2
* XBlock

******************************
Upgrading from Aspen to Birch
******************************

You can upgrade your Open edX instance that is running the Aspen release to the
Birch release, using the ``migrate.sh`` script in the configuration repository,
`available here <https://github.com/openedx/configuration/blob/master/util/vagrant/migrate.sh>`_.

.. note::
  The upgrade scripts provided are verified only for upgrading instances
  running the Aspen release. If you are running any other version of the Open
  edX Platform, the upgrade scripts might not work.

.. caution::
  Before upgrading your Open edX instance, back up all data and configuration
  files. Then verify that you can restore your Open edX instance from the
  backup files.

On the computer or virtual machine running the Aspen release of Open edX, run
the upgrade script for your type of installation:

* For devstack, run ``./migrate.sh -t named-release/birch.2 -c devstack``.

* For fullstack, run ``./migrate.sh -t named-release/birch.2 -c fullstack``.

* You can also run ``./migrate.sh -h`` to see which other options the script accepts.

The script creates a temporary directory in which it upgrades Open edX, then
cleans up extra files and directories when it finishes running.

After upgrading Open edX to the Birch release, run the edX Platform and verify
that course content and data was migrated correctly.

.. include:: ../../../links/links.rst
