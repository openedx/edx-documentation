.. _Open edX Eucalyptus Release:

########################################
Open edX Eucalyptus Release
########################################

This section describes how to install the Open edX Eucalyptus release.

.. contents::
 :local:
 :depth: 1

******************************
What's Included in Eucalyptus
******************************

The Open edX Eucalyptus release contains several new features for learners, course
teams, and developers. See the release notes for the
:ref:`openreleasenotes:Open edX Eucalyptus Release` for more details.

*******************************
What Is the Eucalyptus Git Tag?
*******************************

A Git tag identifies the version of Open edX code that is the Eucalyptus release.
You can find the most up-to-date Git tag for the current Open edX release on
the `Open edX Releases Wiki page`_.

The following Open edX Git repositories have the Eucalyptus Git tag.

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
Installing the Eucalyptus Release
*********************************

You can install the Open edX Eucalyptus release using :ref:`Devstack <Installing
the Open edX Developer stack>` or :ref:`Fullstack <Installing Open edX Fullstack>`.

Review the prerequisites and instructions for each option, and then choose the
option that best meets your needs. Ensure that you install the
required software to run the edX platform.

If you are upgrading from the Dogwood release, see `Upgrading from Dogwood to
Eucalyptus`_.

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
``OPENEDX_RELEASE`` environment variable to the Git tag for the Eucalyptus
release. To do so, use the Linux ``export`` command.

.. code-block:: bash

  export OPENEDX_RELEASE="{Git tag}"

=========================
Install the Vagrant Box
=========================

When you have completed the previous steps, install the Eucalyptus release by
following the installation instructions for :ref:`Devstack <Installing the Open
edX Developer Stack>` or :ref:`Fullstack <Installing Open edX Fullstack>`.

************************************
Upgrading from Dogwood to Eucalyptus
************************************

You can upgrade an Open edX instance that is running the Dogwood release to the
Eucalyptus release.  EdX provides the ``upgrade.sh`` script if you have a simple
Dogwood installation and want to upgrade it automatically. If you have a more
complex or customized installation, you may need to upgrade manually.

===================
Automatic Upgrading
===================

`The upgrade.sh script`_ is in the edX configuration repository on GitHub.

.. note::
  The upgrade scripts provided are verified only for upgrading instances
  running the Dogwood release. If you are running any other version of the Open
  edX Platform, the upgrade scripts might not work.

.. caution::
  Before upgrading your Open edX instance, back up all data and configuration
  files. Then verify that you can restore your Open edX instance from the
  backup files.

On the computer or virtual machine that is running the Dogwood release of Open
edX, run the upgrade script for your type of installation.

* For devstack, run
  ``./upgrade.sh -c devstack -t open-release/eucalyptus/latest``.

* For fullstack, run
  ``./upgrade.sh -c fullstack -t open-release/eucalyptus/latest``.

You can find the most up-to-date Git tag for the current Open edX release on
the `Open edX Releases Wiki page`_.

You can also run ``./upgrade.sh -h`` to see which other options the script
accepts.

The script creates a temporary directory in which it upgrades Open edX, then
cleans up extra files and directories when it finishes running.

After upgrading Open edX to the Eucalyptus release, start the LMS and Studio and
verify that course content and data was migrated correctly.

========================
Upgrade Process Overview
========================

This is an overview of what happens during an upgrade from Dogwood to Eucalyptus.
The ``upgrade.sh`` script implements this process.  You may need to understand
this process if your installation is customized in some way, or if you need to
diagnose problems during the upgrade.

TBD

***************************************
Upgrading to a Eucalyptus Point Release
***************************************

Occasionally, we release updates to Eucalyptus.  The
``open-release/eucalyptus/latest`` branch always refers to the latest release
of Eucalyptus.    The steps differ based on your original installation method.  

================================
Upgrading a Vagrant Installation
================================

Devstack and Fullstack are installed using Vagrant.  To upgrade to a Eucalyptus
point release, follow these steps in the host operating system.

.. code-block:: bash

    $ export OPENEDX_RELEASE=open-release/eucalyptus/latest
    $ vagrant provision

===============================
Upgrading a Native Installation
===============================

If you installed Open edX using the `Open edX Native Installation`_, re-run
those steps using your desired Eucalyptus tag as the new value for
``OPENEDX_RELEASE``.


.. include:: ../../../links/links.rst

