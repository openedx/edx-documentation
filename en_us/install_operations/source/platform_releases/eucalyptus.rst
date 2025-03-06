.. _Open edX Eucalyptus Release:

########################################
Open edX Eucalyptus Release
########################################

.. warning::

    This release is unsupported.

    The `Open edX Named Releases page`_ and the `Open edX Releases Homepage`_ are the
    authoratative sources of information on all Open edX releases. It is *strongly*
    recommended to operate off the latest Open edX release at all points in time, as
    only the most recent release is community-supported.

    See the `Open edX Release Schedule`_ for information on release dates and end-of-life
    support.

This section describes the Open edX Eucalyptus release. Note that edX no longer 
supports the Eucalyptus relesae. 

.. contents::
 :local:
 :depth: 1

******************************
What's Included in Eucalyptus
******************************

The Open edX Eucalyptus release contains several new features for learners,
course teams, and developers. For more information, see
`Open edX Eucalyptus Release <https://docs.openedx.org/en/latest/community/release_notes/eucalyptus.html>`.

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


************************************
Upgrading from Dogwood to Eucalyptus
************************************

You can upgrade an Open edX instance that is running the Dogwood release to the
Eucalyptus release.  EdX provides the ``upgrade.sh`` script if you have a simple
Dogwood installation and want to upgrade it automatically. If you have a more
complex or customized installation, you may need to upgrade manually.

`The upgrade.sh script`_ is in the edX configuration repository on GitHub.

.. note::
  The upgrade script is only for upgrading instances running the Dogwood
  release.  If your instance is running a release prior to the Dogwood release,
  follow the instructions to upgrade it to each intervening release, and then
  upgrade from Dogwood to Eucalyptus.

.. caution::
  Before upgrading your Open edX instance, back up all data and configuration
  files. Then verify that you can restore your Open edX instance from the
  backup files.

On the computer or virtual machine that is running the Dogwood release of Open
edX, run the upgrade script for your type of installation.

#.  Download the script.

    .. code-block:: bash

        $ export OPENEDX_RELEASE=open-release/eucalyptus.1
        $ curl -OL https://raw.github.com/openedx/configuration/$OPENEDX_RELEASE/util/vagrant/upgrade.sh

#.  Run the script.

    * For devstack, run ``bash upgrade.sh -c devstack``.

    * For fullstack, run ``bash upgrade.sh -c fullstack``.

You can find the most up-to-date Git tag for the current Open edX release on
the `Open edX Releases Wiki page`_.

You can also run ``bash upgrade.sh -h`` to see which other options the script
accepts.

The script creates a temporary directory in which it upgrades Open edX, then
cleans up extra files and directories when it finishes running.

After upgrading Open edX to the Eucalyptus release, start the LMS and Studio and
verify that course content and data was migrated correctly.


********************************************
Upgrading to a Subsequent Eucalyptus Release
********************************************

Occasionally, we release updates to Eucalyptus.  For example, the second 
release of Eucalyptus is ``open-release/eucalyptus.2``.
The steps to upgrade differ based on your original installation method.

================================
Upgrading a Vagrant Installation
================================

Devstack and Fullstack for Eucalyptus are installed using Vagrant.  To upgrade 
to a Eucalyptus point release, follow these steps in the host operating system.

.. code-block:: bash

    $ export OPENEDX_RELEASE=open-release/eucalyptus.2
    $ vagrant provision

===============================
Upgrading a Native Installation
===============================

If you installed Open edX using the `Open edX Native 12.04 Installation`_, re-run
those steps using your desired Eucalyptus tag as the new value for
``OPENEDX_RELEASE``.


.. include:: ../../../links/links.rst

