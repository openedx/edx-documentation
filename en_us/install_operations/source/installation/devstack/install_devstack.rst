.. _Installing the Open edX Developer Stack:

########################################
Installing the Open edX Developer Stack
########################################

This section describes how to install the Open edX developer stack (devstack).

.. contents::
   :local:
   :depth: 1

.. note::
 Before you install devstack, make sure that you have met the
 :ref:`installation prerequisites<Installation Prerequisites>`.

.. _Install DevStack:

**************************
Install Devstack
**************************

To install devstack directly from the command line, follow the instructions
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

#. Download the devstack Vagrant file.

   .. code-block:: bash

     curl -L https://raw.github.com/edx/configuration/master/vagrant/release/devstack/Vagrantfile > Vagrantfile

#. Install the Vagrant ``vbguest`` plugin.

   .. code-block:: bash

     vagrant plugin install vagrant-vbguest

#. Create the devstack virtual machine.

   .. code-block:: bash

     vagrant up

   The first time you create the devstack virtual machine, Vagrant downloads
   the base box, which has a file size of about 4GB. If you destroy and
   recreate the virtual machine, Vagrant re-uses the box it downloaded. See
   `Vagrant's documentation on boxes`_ for more information.

#. When prompted, enter the administrator password for your local computer.

When you have completed these steps, see :ref:`Running the Open edX Developer
Stack` to begin using devstack.

For help with the devstack installation, see :ref:`Troubleshooting the Devstack
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

.. include:: ../../../../links/links.rst
