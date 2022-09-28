.. _Open edX Cypress Release:

########################################
Open edX Cypress Release
########################################

This section describes the Open edX Cypress release. Note that edX no longer
supports the Cypress release.

.. contents::
 :local:
 :depth: 1

******************************
What's Included in Cypress
******************************

The Open edX Cypress release contains several new features for learners, course
teams, and developers. See the Open edX Release Notes for more details.

.. Note::
 There are several new features in the Cypress release that are available, but
 not enabled by default in new installations. For details, see the following
 topics.

 * :ref:`Enable edX Search`
 * :ref:`Enable Badging`
 * :ref:`Enable CCX`
 * :ref:`Enable Licensing`

******************************
What is the Cypress Git Tag?
******************************

The Git tag for the Cypress release is ``named-release/cypress``. You use this
tag to identify the version of Open edX code that is the Cypress release.

The following Open edX Git repositories have the Git tag
``named-release/cypress``.

* edx-platform
* configuration
* cs_comments_service
* notifier
* edx-certificates
* xqueue
* edx-documentation
* edx-ora2
* XBlock

********************************
Upgrading from Birch to Cypress
********************************

You can upgrade an Open edX instance that is running the Birch release to the
Cypress release, by using the ``migrate.sh`` script in the configuration
repository, `available here
<https://github.com/openedx/configuration/blob/master/util/vagrant/migrate.sh>`_.

.. note::
  The upgrade scripts provided are verified only for upgrading instances
  running the Birch release. If you are running any other version of the Open
  edX Platform, the upgrade scripts might not work.

.. caution::
  Before upgrading your Open edX instance, back up all data and configuration
  files. Then verify that you can restore your Open edX instance from the
  backup files.

On the computer or virtual machine that is running the Birch release of Open
edX, run the upgrade script for your type of installation:

* For devstack, run ``./migrate.sh -c devstack``.

* For fullstack, run ``./migrate.sh -c fullstack``.

* You can also run ``./migrate.sh -h`` to see which other options the script
  accepts.

The script creates a temporary directory in which it upgrades Open edX, then
cleans up extra files and directories when it finishes running.

After upgrading Open edX to the Cypress release, start the LMS and Studio and
verify that course content and data was migrated correctly.


.. include:: ../../../links/links.rst
