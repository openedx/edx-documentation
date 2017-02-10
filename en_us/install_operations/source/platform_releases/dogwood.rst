.. _Open edX Dogwood Release:

########################################
Open edX Dogwood Release
########################################

This section describes how to install the Open edX Dogwood release.

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
:ref:`openreleasenotes:Open edX Dogwood Release` for more details.

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

******************************
Installing the Dogwood Release
******************************

You can install the Open edX Dogwood release using :ref:`Devstack <Installing
the Open edX Developer stack>` or :ref:`Fullstack <Installing Open edX Fullstack>`.

Review the prerequisites and instructions for each option, and then choose the
option that best meets your needs. Ensure that you install the
required software to run the edX platform.

If you are upgrading from the Cypress release, see `Upgrading from Cypress to
Dogwood`_.

For new installations, follow these steps.

#. `Download the Vagrant Box`_ or `Download the BitTorrent File`_.

   .. caution::
     The Vagrant boxes have a large file size (between 4 and 5 GB). If you have
     a slow or unreliable Internet connection, use BitTorrent to download the
     Vagrant box you need.

#. `Set the OPENEDX_RELEASE Environment Variable`_.

#. `Install the Vagrant Box`_.

=========================
Download the Vagrant Box
=========================

If you have a fast and reliable Internet connection, you can download the
Vagrant box directly or by running ``vagrant up`` when you install
:ref:`Devstack <Installing the Open edX Developer Stack>` or
:ref:`Fullstack <Installing Open edX Fullstack>`.

To access the latest Vagrant boxes, see the `Open edX Releases Wiki
page`_.

For more information about working with vagrant boxes, see `Vagrant's
documentation on boxes`_.

=============================
Download the BitTorrent File
=============================

You can also download the BitTorrent file for the option you selected.
BitTorrent is recommended if you have a slow or unreliable data connection.
You then use the BitTorrent file to download the Vagrant box. If the Internet
connection is temporarily lost while you are downloading the Vagrant box
through BitTorrent, you can later continue the download without data loss or
corruption.

To access the latest Vagrant box torrents, see the `Open edX Releases Wiki
page`_.

For more information about downloading BitTorrent files, see `BitTorrent`_.

If you download the Vagrant box through BitTorrent, you must add the box to
Vagrant before continuing with the installation process.

Be sure to verify that you have the most up-to-date Git tag for the Open edX
releases on the `Open edX Releases Wiki page`_.

* For devstack installations, run the following command.

   .. code-block:: bash

     $ vagrant box add /{path-to-downloaded-box}/{vagrant-box-name} --name {Git-tag}

* For fullstack installations, run the following command.

   .. code-block:: bash

     $ vagrant box add /{path-to-downloaded-box}/{vagrant-box-name} --name {Git-tag}

============================================
Set the OPENEDX_RELEASE Environment Variable
============================================

Before installing the Vagrant box, you must set the value of the
``OPENEDX_RELEASE`` environment variable to the Git tag for the Dogwood
release. To do so, use the Linux ``export`` command.

.. code-block:: bash

  export OPENEDX_RELEASE="{Git tag}"

=========================
Install the Vagrant Box
=========================

When you have completed the previous steps, install the Dogwood release by
following the installation instructions for :ref:`Devstack <Installing the Open
edX Developer Stack>` or :ref:`Fullstack <Installing Open edX Fullstack>`.

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
