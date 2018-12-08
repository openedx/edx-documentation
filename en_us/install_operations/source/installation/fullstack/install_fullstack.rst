.. _Installing Open edX Fullstack:

##############################################
Installing Open edX Fullstack
##############################################

This section describes how to install the Open edX full stack (fullstack).

.. contents::
   :local:
   :depth: 1

****************************************
Installation Prerequisites for Fullstack
****************************************

Before you install Open edX fullstack, make sure that you have met the
:ref:`installation prerequisites<Installation Prerequisites>`.


===========================
Selecting a Download Option
===========================

The Open edX virtual machine box file has a file size of approximately four
gigabytes. To download the box file, you can use one of these methods.

* Install fullstack with a direct Vagrant box download. The first time you start
  the fullstack virtual machine, the Vagrant virtual machine management tool
  downloads the box file.

* Use a BitTorrent client to download the Vagrant box file before you
  install fullstack. The first time you start the fullstack virtual machine, the
  Vagrant virtual machine management tool uses the previously downloaded box
  file.

If your internet connection is limited or intermittent, edX recommends that you
torrent the box file by following the instructions in :ref:`Torrent the Box File`.
However, this step is optional.


******************
Install Fullstack
******************

To install fullstack follow these steps.

#. Create the ``fullstack`` directory and navigate to it in the command prompt.

   .. code-block:: bash

     mkdir fullstack
     cd fullstack

#.  Set the ``OPENEDX_RELEASE`` environment variable to the Git tag name of the
    release of the Open edX platform that you are installing. For
    information about the latest Open edX releases and the Git tag names for
    them, see the `Open edX Releases Wiki page`_.

    For example, ``open-release/eucalyptus.1`` is the Git tag name for the
    first Eucalyptus release. The following command sets the value of the
    ``OPENEDX_RELEASE`` environment variable to ``open-release/eucalyptus.1``.

    .. code-block:: bash

      export OPENEDX_RELEASE="open-release/eucalyptus.1"

#. Download the install script.

   .. code-block:: bash

     curl -OL https://raw.github.com/edx/configuration/$OPENEDX_RELEASE/util/install/install_stack.sh

#. Run the install script to create and start the fullstack virtual machine.

   .. code-block:: bash

     bash install_stack.sh fullstack

   .. note:: This step downloads the box file if you did not already
      :ref:`use Torrent<Torrent the Box File>` to download and add it.

   If you destroy and recreate the virtual machine, Vagrant reuses the box
   file and does not download it again. See `Vagrant's documentation on
   boxes`_ for more information.

When you have completed these steps, see :ref:`Starting Open edX Fullstack`
to begin using fullstack.

.. include:: ../../../../links/links.rst
