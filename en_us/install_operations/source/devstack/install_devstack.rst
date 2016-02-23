.. _Installing the Open edX Developer Stack:

########################################
Installing the Open edX Developer Stack
########################################

This section describes how to install the Open edX Developer Stack.

.. contents::
   :local:
   :depth: 1

**********
Overview
**********

The Open edX Developer Stack, known as **devstack**, is a Vagrant instance
designed for local development.

Devstack uses the same system requirements as :ref:`Open edX Fullstack
<Installing Open edX Fullstack>`. This allows you to discover and fix system
configuration issues early in development.

Devstack simplifies certain production settings to make development more
convenient. For example, `nginx`_ and `gunicorn`_ are disabled in devstack;
devstack uses Django's runserver instead.

See the `Vagrant documentation`_ for more information.

********************
Components
********************

Devstack includes the following edX components.

* The Learning Management System (LMS)
* edX Studio
* Discussion Forums
* Open Response Assessments (ORA)
* EdX Search

Devstack also includes a demonstration edX course.

**************************
Knowledge Prerequisites
**************************

To use devstack, you should meet the following knowledge requirements.

* Understand basic terminal usage. If you are using a Mac computer, see
  `Introduction to the Mac OS X Command Line`_. If you are using a Windows
  computer, see `Windows Command Line Reference`_.

* Understand Vagrant commands. See the `Vagrant Getting Started`_ guide for
  more information.

**************************
Software Prerequisites
**************************

To install and run devstack, you must first install the following required
software.

* `VirtualBox`_ 4.3.12 or higher.

* `Vagrant`_ 1.6.5 or higher.

* A Network File System (NFS) client, if your operating system does not include
  one. Devstack uses VirtualBox Guest Editions to share folders through NFS.

.. _Install DevStack:

**************************
Install Devstack
**************************

To install devstack directly from the command line, follow these steps.

.. note::

   The first time you start the devstack virtual machine, Vagrant downloads a
   ``box`` file, which has a file size of approximately four gigabytes. You can
   also install devstack using a torrent file that you download separately. For
   more information, see :ref:`install_devstack_with_torrent_file`.

Before beginning the installation, make sure that you have the administrator
password for your local computer. The administrator password is needed to
configure NFS to allow users to access code directories directly from your
computer.

#. Ensure the ``nfsd`` client is running. Use the ``nfsd status`` command.

   .. code-block:: bash

     sudo nfsd status
     nfsd service is enabled
     nfsd is running (pid 313, 8 threads)

   If the nfsd service is not running, use the ``nfsd start`` command.

   .. code-block:: bash

     sudo nfsd start
     Starting the nfsd service

#. Create a ``devstack`` directory and navigate to it in the command prompt.

   .. code-block:: bash

     mkdir devstack
     cd devstack

#. Download the devstack Vagrant file.

   .. code-block:: bash

     curl -L https://raw.github.com/edx/configuration/master/vagrant/release/devstack/Vagrantfile > Vagrantfile

#.  Set the ``OPENEDX_RELEASE`` environment variable to the Git tag name of the
    named release of the Open edX platform that you are installing. For
    information about the latest Open edX releases and the Git tag names for
    them, see `Open edX Releases Wiki page`_.

    For example, ``named-release/dogwood`` is the Git tag name for the Dogwood
    named release. The following command sets the value of the OPENEDX_RELEASE
    environment variable to ``named-release/dogwood``.

    .. code-block:: bash

      export OPENEDX_RELEASE="named-release/dogwood"

    If you do not set this environment variable, Vagrant will install the
    most recent snapshot version of the Open edX platform. The snapshot version is not a supported release.

#. Create and start the devstack virtual machine.

   .. code-block:: bash

     vagrant up

   The first time you start the devstack virtual machine, Vagrant downloads
   the base box, which has a file size of about 4GB. If you destroy and
   recreate the virtual machine, Vagrant re-uses the box it downloaded. See
   `Vagrant's documentation on boxes`_ for more information.

   When prompted, enter the administrator password for your local computer.

When you have completed these steps, see :ref:`Running the Open edX Developer
Stack` to begin using devstack.

For help with the devstack installation, see :ref:`Troubleshooting the Devstack
Installation`.

.. _install_devstack_with_torrent_file:

*****************************************
Install Devstack Using a Torrent File
*****************************************

You can use a BitTorrent client to download the Vagrant box file. Downloading
the box file and installing it in your Vagrant environment will prevent Vagrant
from downloading the box file directly when you start it for the first time.
This may be useful if you have a limited  or intermittent connection to the
internet and cannot download a large file.

To install devstack using a box file that you download with a BitTorrent
client, follow these steps.

#. Ensure the ``nfsd`` client is running. Use the ``nfsd status`` command.

   .. code-block:: bash

     sudo nfsd status
     nfsd service is enabled
     nfsd is running (pid 313, 8 threads)

   If the nfsd service is not running, use the ``nfsd start`` command.

   .. code-block:: bash

     sudo nfsd start
     Starting the nfsd service

#. Create a ``devstack`` directory and navigate to it in the command prompt.

   .. code-block:: bash

     mkdir devstack
     cd devstack

#. Download the devstack Vagrant file.

   .. code-block:: bash

     curl -O https://raw.github.com/edx/configuration/master/vagrant/release/devstack/Vagrantfile

#. Download the torrent file for the latest Open edX release. For information
   about the latest Open edX releases and to download torrent files for them,
   see `Open edX Releases Wiki page`_.

   .. code-block:: bash

     curl -O https://s3.amazonaws.com/edx-static/vagrant-images/20151221-dogwood-devstack-rc2.box?torrent

#. Use a BitTorrent client to open the torrent file and download the ``.box``
   file. For more information about using a BitTorrent client, see the
   documentation for the client software that you choose.

#.  Set the ``OPENEDX_RELEASE`` environment variable to the Git tag name for
    the Open edX release that you are installing. To find the Git tag name for
    an Open edX release, see `Open edX Releases Wiki page`_.

    For example, the following command sets the value of the OPENEDX_RELEASE
    environment variable to ``named-release/dogwood``.

    .. code-block:: bash

      export OPENEDX_RELEASE="named-release/dogwood"

    .. note::

        If you do not set this environment variable, Vagrant will install the
        most recent snapshot version of the Open edX platform, and will
        download the ``box`` file for it directly. The size of the ``box`` file
        is approximately four gigabytes.  The snapshot version is not a
        supported release.

#. Find the name of the Vagrant ``box`` for the named Open edX release that you
   are installing. To find the Vagrant ``box`` name for an Open edX release,
   see `Open edX Releases Wiki page`_.

#. Create a Vagrant ``box`` using the ``vagrant box add`` command. Specify the
   name of the box and the file path of the box file that you downloaded. The
   name of the box you create must match the box name for the Open edX release
   you are installing.

   For example, the following command creates a box named ``dogwood-devstack-
   rc2``.

   .. code-block:: bash

     vagrant box add dogwood-devstack-rc2 \
     /path/to/vagrant-images_20151221-dogwood-devstack-rc2.box

#. Create and start the devstack virtual machine.

   .. code-block:: bash

     vagrant up

   When prompted, enter the administrator password for your local computer.

When you have completed these steps, see :ref:`Running the Open edX Developer
Stack` to begin using devstack.

For help with the devstack installation, see :ref:`Troubleshooting the Devstack
Installation`.

.. _Troubleshooting the Devstack Installation:

*****************************************
Troubleshooting the Devstack Installation
*****************************************

In some cases, you see an error when you attempt to create the devstack virtual
machine (``vagrant up``). For example:

``mount.nfs: mount to NFS server '192.168.33.1:/path/to/edx-platform' failed: timed out, giving up``

This error situation arises because Vagrant uses a host-only network in
Virtualbox to communicate with your computer. If a network does not exist, one
is created on ``vagrant up``. If this network is created with the VPN up, it
will not work. You must recreate the network with the VPN down.

To resolve the error, follow these steps.

#. Stop the VPN.
#. Type ``vagrant halt``.
#. Open Virtualbox.
#. Navigate to **Preferences > Network > Host-only Networks** and remove the
   most-recently-created host-only network.
#. Type ``vagrant up``.

.. include:: ../../../links/links.rst
