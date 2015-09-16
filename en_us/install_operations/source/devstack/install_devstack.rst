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

The Open edX Developer Stack, known as **Devstack**, is a Vagrant instance
designed for local development.

Devstack uses the same system requirements as :ref:`Open edX Fullstack
<Installing Open edX Fullstack>`. This allows you to discover and fix system
configuration issues early in development.

Devstack simplifies certain production settings to make development more
convenient. For example, `nginx`_ and `gunicorn`_ are disabled in Devstack;
Devstack uses Django's runserver instead.

See the `Vagrant documentation`_ for more information.

********************
Components
********************

Devstack includes the following edX components:

* The Learning Management System (LMS)
* edX Studio
* Discussion Forums
* Open Response Assessments (ORA)
  
Devstack also includes a demo edX course.

**************************
Knowledge Prerequisites
**************************

To use Devstack, you should meet the following knowledge requirements.

* Understand basic terminal usage. If you are using a Mac computer, see
  `Introduction to the Mac OS X Command Line`_. If you are using a Windows
  computer, see `Windows Command Line Reference`_.

* Understand Vagrant commands. See the `Vagrant Getting Started`_ guide for
  more information.


**************************
Software Prerequisites
**************************

To install and run Devstack, you must first install the following required
software.

* `VirtualBox`_ 4.3.12 or higher

* `Vagrant`_ 1.6.5 or higher

* A Network File System (NFS) client, if your operating system does not include
  one. Devstack uses VirtualBox Guest Editions to share folders through NFS.
  
.. _Install DevStack:  

**************************
Install DevStack
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

#. Download the Devstack `Torrent`_ file.

#. When you have the file on your computer, add the virtual machine using the
   following command.

    .. code-block:: bash

     vagrant box add box-name path-to-box-file


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

.. include:: ../../../links/links.rst
