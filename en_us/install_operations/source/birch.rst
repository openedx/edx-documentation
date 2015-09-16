.. _Open edX Birch Release:

########################################
Open edX Birch Release
########################################

This section describes how to install the Open edX Birch release.

.. contents::
 :local:
 :depth: 1

.. note:: 
  Now that the Open edX Cypress release is available, edX no longer
  supports the Birch release.

******************************
What's Included in Birch
******************************

The Open edX Birch release contains several new features for students, course
teams, and developers.  See the Open edX Release Notes for more details.

.. Note::
 There are several new features in the Birch release that are available, but
 not configured in new installations.  For details, see the following topics.

 * :ref:`Add the Google Drive and Google Calendar XBlock`.
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

.. confirm

******************************
Installing the Birch Release
******************************

You can install the Open edX Birch release using :ref:`Devstack <Install DevStack>` or :ref:`Fullstack <Install Open edX Fullstack>`.

Review the prerequisites and instructions for each option, then choose the
option that best meets your needs. Ensure you install the required software to
run the edX Platform.

If you are upgrading from the Aspen release, see `Upgrading from Aspen to
Birch`_.

For new installations, follow the steps below.

#. `Download the Vagrant Box`_ or `Download the BitTorrent File`_.

   .. caution::
     The Vagrant boxes have a large file size (about 2.5GB). If you have a slow
     or unreliable Internet connection, use BitTorrent to download the
     Vagrant box you need.

#. `Set the OPENEDX_RELEASE Environment Variable`_.
#. `Install the Vagrant Box`_.

=========================
Download the Vagrant Box
=========================

If you have a fast and reliable Internet connection, you can download the
Vagrant box directly or by running ``vagrant up`` when installing
:ref:`Devstack <Installing the Open edX Developer Stack>` or
:ref:`Fullstack <Installing Open edX Fullstack>`.

See the `Open edX Releases Wiki page`_ to access the latest Vagrant
boxes.

See `Vagrant's documentation on boxes`_ for more information.


=============================
Download the BitTorrent File
=============================

You can also download the BitTorrent file for the option you selected.
BitTorrent is recommended if you have a slow or unreliable data connection.
You then use the BitTorrent file to download the Vagrant box. If the Internet
connection is temporarily lost while you are downloading the Vagrant box
through BitTorrent, you can later continue the download without data loss or
corruption.

See the `Open edX Releases Wiki page`_ to access the latest Vagrant
boxes.

See `BitTorrent`_ for more information.

If you download the Vagrant box through BitTorrent, you must add the box to
Vagrant before continuing with the installation process.

* For Devstack installations, run the following command.

   .. code-block:: bash

     $ vagrant box add /path-to-downloaded-box/vagrant-images-birch-2-devstack.box --name birch-devstack-2

* For Fullstack installations, run the following command.

   .. code-block:: bash

     $ vagrant box add /path-to-downloaded-box/vagrant-images-birch-2-fullstack.box --name birch-fullstack-2

============================================
Set the OPENEDX_RELEASE Environment Variable
============================================

Before installing the Vagrant box, you must set the value of the
`OPENEDX_RELEASE` environment variable to the Git tag for the Birch release:

.. code-block:: bash

  export OPENEDX_RELEASE="named-release/birch.2"


=========================
Install the Vagrant Box
=========================

When you have completed the previous steps, install the Birch release by
following the installation instructions for :ref:`Devstack <Installing the Open
edX Developer Stack>` or
:ref:`Fullstack <Installing Open edX Fullstack>`.


******************************
Upgrading from Aspen to Birch
******************************

You can upgrade your Open edX instance that is running the Aspen release to the
Birch release, using the ``migrate.sh`` script in the configuration repository,
`available here <https://github.com/edx/configuration/blob/master/util/vagrant/migrate.sh>`_.

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

* For Devstack, run ``./migrate.sh -t named-release/birch.2 -c devstack``.

* For Fullstack, run ``./migrate.sh -t named-release/birch.2 -c fullstack``.

* You can also run ``./migrate.sh -h`` to see which other options the script accepts.

The script creates a temporary directory in which it upgrades Open edX, then
cleans up extra files and directories when it finishes running.

After upgrading Open edX to the Birch release, run the edX Platform and verify
that course content and data was migrated correctly.

.. include:: ../../links/links.rst