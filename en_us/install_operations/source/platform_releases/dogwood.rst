.. _Open edX Dogwood Release:

########################################
Open edX Dogwood Release
########################################

This section describes the Open edX Dogwood release. Note that edX no longer 
supports the Dogwood relesae. 

.. contents::
 :local:
 :depth: 1

.. note::
  Now that the Open edX Eucalyptus release is available, edX no longer
  supports the Dogwood release.

******************************
What's Included in Dogwood
******************************

The Open edX Dogwood release contains several new features for learners, course
teams, and developers. See the release notes for the
:ref:`Open edX Dogwood Release` for more details.

******************************
What Is the Dogwood Git Tag?
******************************

A Git tag identifies the version of Open edX code that is the Dogwood release.
You can find the most up-to-date Git tag for the current Open edX release on
the `Open edX Releases Wiki page`_.

The following Open edX Git repositories have the Dogwood Git tag.

* edx-platform
* configuration
* cs_comments_service
* xqueue
* XBlock
* notifier
* edx-ora2
* edx-documentation
* edx-certificates
* edx-analytics-data-api-client
* edx-analytics-configuration
* edx-analytics-dashboard
* edx-analytics-data-api
* edx-analytics-pipeline

*********************************
Upgrading from Cypress to Dogwood
*********************************

You can upgrade an Open edX instance that is running the Cypress release to the
Dogwood release.  EdX provides the ``migrate.sh`` script if you have a simple
Cypress installation and want to upgrade it automatically. If you have a more
complex or customized installation, you may need to upgrade manually.

===================
Automatic Upgrading
===================

`The migrate.sh script`_ is in the edX configuration repository on GitHub.

.. note::
  The upgrade scripts provided are verified only for upgrading instances
  running the Cypress release. If you are running any other version of the Open
  edX Platform, the upgrade scripts might not work.

.. caution::
  Before upgrading your Open edX instance, back up all data and configuration
  files. Then verify that you can restore your Open edX instance from the
  backup files.

On the computer or virtual machine that is running the Cypress release of Open
edX, run the upgrade script for your type of installation.

* For devstack, run ``./migrate.sh -c devstack -t named-release/dogwood``.

* For fullstack, run
  ``./migrate.sh -c fullstack -t named-release/dogwood``.

You can find the most up-to-date Git tag for the current Open edX release on
the `Open edX Releases Wiki page`_.

You can also run ``./migrate.sh -h`` to see which other options the script
accepts.

The script creates a temporary directory in which it upgrades Open edX, then
cleans up extra files and directories when it finishes running.

After upgrading Open edX to the Dogwood release, start the LMS and Studio and
verify that course content and data was migrated correctly.

========================
Upgrade Process Overview
========================

This is an overview of what happens during an upgrade from Cypress to Dogwood.
The ``migrate.sh`` script implements this process.  You may need to understand
this process if your installation is customized in some way, or if you need to
diagnose problems during the upgrade.

Upgrading Cypress to Dogwood is more involved than most Open edX release
upgrades.

* Dogwood upgrades the Django framework from version 1.4 to 1.8, which changed
  the database migration tool from South to Django. When you upgrade from
  Cypress to Dogwood, it is important to take special care with the database
  migrations.

* Dogwood upgrades Python from 2.7.3 to 2.7.10. This means virtualenvs have to
  be recreated.

The upgrade from Cypress to Dogwood includes these steps.

#. Applies a `forum migration described on the Open edX wiki`_ to support teams
   discussion filtering.

#. Updates edx-platform to the ``release-2015-11-09`` tag.  This is the last
   released version that used Django 1.4.

#. Recreates the virtualenvs to use Python 2.7.10 instead of 2.7.3.

#. Migrates the database. This makes the database current with the last 1.4
   code.

#. Uninstalls South so that it does not interfere with the new Django
   migrations.

#. Updates edx-platform to the ``dogwood-first-18`` tag. This is the first
   version of the code that used Django 1.8.

#. Applies all the initial Django migrations. This gets your database ready to
   use the new Django 1.8 migration mechanism.

#. Updates edx-platform to Dogwood.

#. Runs Django database migrations.

#. Runs two management commands to update records in the database:
   ``generate_course_overview`` and ``post_cohort_membership_fix``.

#. Runs the forum migration again. This step processes any discussion topics
   created during the running of the script.

Similar steps are followed to upgrade other repositories such as xqueue.


************************************
Upgrading to a Dogwood Point Release
************************************

Occasionally, we release updates to Dogwood.  The first of these is named
Dogwood.1, then Dogwood.2, and so on.  The steps differ based on your original
installation method.  You will need to know the name of the Dogwood tag you
want to install, for example ``named-release/dogwood.2``.

================================
Upgrading a Vagrant Installation
================================

Devstack and Fullstack are installed using Vagrant.  To upgrade to a Dogwood
point release, follow these steps in the host operating system.

.. code-block:: bash

    $ export OPENEDX_RELEASE={desired-dogwood-tag}
    $ vagrant provision

===============================
Upgrading a Native Installation
===============================

If you installed Open edX using the `Open edX Native 12.04 Installation`_, re-run
those steps using your desired Dogwood tag as the new value for
``OPENEDX_RELEASE``.


.. include:: ../../../links/links.rst
