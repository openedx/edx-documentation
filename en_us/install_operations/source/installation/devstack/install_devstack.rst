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

.. _Install DevStack:

******************************************************
Install Devstack with a Direct Vagrant Box Download
******************************************************

During an installation of this type, the Vagrant virtual machine management
tool downloads an Open edX virtual maching ``box`` file.

.. note::

   The first time you start the devstack virtual machine, Vagrant downloads a
   ``box`` file, which has a file size of approximately four gigabytes. This
   installation method might not be suitable if your internet connection is
   limited or intermittent.

   You can also install devstack using a torrent file that you download
   separately. For more information, see
   :ref:`install_devstack_with_torrent_file`.

To install devstack with a direct Vagrant box download, follow these steps.

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

    If you do not set this environment variable, Vagrant will install the most
    recent snapshot version of the Open edX platform. The snapshot version is
    not a supported release.

#. Create and start the devstack virtual machine.

   .. code-block:: bash

     vagrant up

   The first time you start the devstack virtual machine, Vagrant downloads
   the base box, which has a file size of about 4GB. If you destroy and
   recreate the virtual machine, Vagrant re-uses the box it downloaded. See
   `Vagrant's documentation on boxes`_ for more information.

   When prompted, enter the administrator password for your local computer.

When you have completed these steps, see :ref:`Starting the Open edX Developer
Stack` to begin using devstack.

For help with the devstack installation, see
:ref:`troubleshooting_devstack_installation`.

.. _install_devstack_with_torrent_file:

*******************************************************
Install Devstack with a Torrent Vagrant Box Download
*******************************************************

You can use a BitTorrent client to download the Vagrant box file. Downloading
the box file and installing it in your Vagrant environment will prevent Vagrant
from downloading the box file directly when you start it for the first time.
This may be useful if you have a limited or intermittent connection to the
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

When you have completed these steps, see :ref:`Starting the Open edX Developer
Stack` to begin using devstack.

For help with the devstack installation, see
:ref:`troubleshooting_devstack_installation`.

.. include:: ../../../../links/links.rst
