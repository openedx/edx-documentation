.. _Installing the Open edX Developer Stack:

########################################
Installing the Open edX Developer Stack
########################################

This section describes how to install the Open edX developer stack (Devstack).

.. contents::
   :local:
   :depth: 1

.. note::
 Before you install Devstack, make sure that you have met the
 :ref:`installation prerequisites<Installation Prerequisites>`.

.. _Install DevStack:

**************************
Install Devstack
**************************

To install Devstack directly from the command line, follow the instructions
below. You can also install DevStack using a Torrent file, as explained in the
next section.

Before beginning the installation, ensure that you have the administrator
password for your local computer. The administrator password is needed so that
NFS can be set up to allow users to access code directories directly from your
computer.

#. Ensure the ``nfsd`` client is running.

#. Create the ``devstack`` directory and navigate to it in the command prompt.

   .. code-block:: bash

     mkdir devstack
     cd devstack

#. Download the Devstack Vagrant file.

   .. code-block:: bash

     curl -L https://raw.github.com/edx/configuration/master/vagrant/release/devstack/Vagrantfile > Vagrantfile

#. Install the Vagrant ``vbguest`` plugin.

   .. code-block:: bash

     vagrant plugin install vagrant-vbguest

#. Create the Devstack virtual machine.

   .. code-block:: bash

     vagrant up

   The first time you create the Devstack virtual machine, Vagrant downloads
   the base box, which has a file size of about 4GB. If you destroy and
   recreate the virtual machine, Vagrant re-uses the box it downloaded. See
   `Vagrant's documentation on boxes`_ for more information.

#. When prompted, enter the administrator password for your local computer.

When you have completed these steps, see :ref:`Running the Open edX Developer
Stack` to begin using Devstack.

For help with the Devstack installation, see :ref:`Troubleshooting the Devstack
Installation`.

*****************************************
Install Devstack using the Torrent file
*****************************************

You can use BitTorrent to download the box file.  Follow all of the
instructions in :ref:`Install DevStack`, but instead of downloading
the Vagrant file with curl, do this:

#. Download the Torrent file for the latest Open edX release.
   See the `Open edX Releases Wiki page`_ to find out what the latest Open edX
   release is, and where to download the Torrent file.

#. When you have the file on your computer, add the virtual machine using the
   following command.

    .. code-block:: bash

     vagrant box add box-name path-to-box-file

*************************
Installation Options
*************************

When you install Devstack, you can customize the environment.

================================================
Set Up Ability to Preview Units (Mac/Linux Only)
================================================

If you are installing Devstack on a Linux or Macintosh computer, you must
configure your installation to use the preview feature in edX Studio.

#. :ref:`Connect to the Devstack virtual machine<Connect to Devstack VM>`.

#. In the ``etc/hosts`` file, add the following line.

  .. code-block:: bash

    192.168.33.10 preview.localhost



===================================
Customize the Source Code Location
===================================

You can customize the location of the edX source code that gets cloned when you
provision Devstack. You may want to do this to have Devstack work with source
code that already exists on your computer.

By default, the source code location is the directory in which you run
``vagrant up``. To change this location, follow these steps.

#. :ref:`Connect to the Devstack virtual machine<Connect to Devstack VM>`.

#. Set the ``VAGRANT_MOUNT_BASE`` environment variable to set the base
   directory for the ``edx-platform`` and ``cs_comments_service`` source code
   directories.

.. _Troubleshooting the Devstack Installation:

*****************************************
Troubleshooting the Devstack Installation
*****************************************

In some cases, you see an error when you attempt to create the Devstack virtual
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

.. include:: ../../../../links/links.rst
