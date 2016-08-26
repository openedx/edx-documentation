.. _Installing the Open edX Developer stack:

########################################
Installing Open edX Devstack
########################################

This section describes how to install the Open edX developer stack (devstack).

.. contents::
   :local:
   :depth: 1

****************************************
Installation Prerequisites for Devstack
****************************************

Before you install devstack, make sure that you have met the
:ref:`installation prerequisites<Installation Prerequisites>`.

You must also ensure that you have the administrator password for your local
computer. The administrator password is needed to configure NFS (network file
system) to allow users to access code directories directly from your computer.

===========================
Selecting a Download Option
===========================

The Open edX virtual machine box file has a file size of approximately four
gigabytes. To download the box file, you can use one of these methods.

* Install devstack with a direct Vagrant box download. The first time you start
  the devstack virtual machine, the Vagrant virtual machine management tool
  downloads the box file.

* Use a BitTorrent client to download the Vagrant box file before you
  install devstack. The first time you start the devstack virtual machine, the
  Vagrant virtual machine management tool uses the previously downloaded box
  file.

If your internet connection is limited or intermittent, edX recommends that you
torrent the box file. However, this step is optional.


.. _Torrent the Box File:

===============================
Torrent the Box File (Optional)
===============================

#. Download the torrent file for the latest Open edX release. For the URLs and 
   box names of the Open edX releases, see `Open edX Releases Wiki page`_.

   .. code-block:: bash

     curl -OJL https://s3.amazonaws.com/edx-static/vagrant-images/eucalyptus-devstack-2016-08-19.box?torrent

#. Use a BitTorrent client to open the ``.torrent`` file and download the ``.box``
   file. For more information about using a BitTorrent client, see the
   documentation for the client software that you choose.

#. Find the name of the Vagrant box for the Open edX release that you
   are installing. To find the Vagrant box name for an Open edX release,
   see `Open edX Releases Wiki page`_.

#. Create a Vagrant box using the ``vagrant box add`` command. Specify the
   name of the box and the file path of the box file that you downloaded. The
   name of the box you create must match the box name for the Open edX release
   you are installing.

   .. code-block:: bash

     vagrant box add {BOX-NAME} {BOX-FILE}

   Where {BOX-NAME} is the name of the box specified on the Open edX Releases
   Wiki page, and {BOX-FILE} is the path to the box file you downloaded.
   For example, the following command creates a box named
   ``eucalyptus-devstack-2016-08-19``.

   .. code-block:: bash

     vagrant box add eucalyptus-devstack-2016-08-19 /path/to/box/eucalyptus-devstack-2016-08-19.box


.. _Install Devstack:

****************
Install Devstack
****************

To install devstack, follow these steps.

#. Ensure the ``nfsd`` client is running. You can use the ``nfsd status``
   command.

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

#.  Set the ``OPENEDX_RELEASE`` environment variable to the Git tag name of the
    release of the Open edX platform that you are installing. For
    information about the latest Open edX releases and the Git tag names for
    them, see `Open edX Releases Wiki page`_.

    For example, ``open-release/eucalyptus.1`` is the Git tag name for the
    first Eucalyptus release. The following command sets the value of the
    ``OPENEDX_RELEASE`` environment variable to ``open-release/eucalyptus.1``.

    .. code-block:: bash

      export OPENEDX_RELEASE="open-release/eucalyptus.1"

    If you do not set this environment variable, Vagrant will install the most
    recent snapshot version of the Open edX platform. The snapshot version is
    not a supported release.

#. Download the install script.

   .. code-block:: bash

     curl -OL https://raw.github.com/edx/configuration/$OPENEDX_RELEASE/util/install/install_stack.sh

#. Run the install script to create and start the devstack virtual machine.

   .. code-block:: bash

     bash install_stack.sh devstack

   .. note:: This step downloads the box file if you did not already
      :ref:`use Torrent<Torrent the Box File>` to download and add it.

   If you destroy and recreate the virtual machine, Vagrant reuses the box
   file and does not download it again. See `Vagrant's documentation on
   boxes`_ for more information.

   When prompted, enter the administrator password for your local computer.

When you have completed these steps, see :ref:`Starting the Open edX Developer
Stack` to begin using devstack.

For help with the devstack installation, see
:ref:`troubleshooting_devstack_installation`.


.. include:: ../../../../links/links.rst
