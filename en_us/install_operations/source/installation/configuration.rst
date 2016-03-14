.. _vm_installation_options:

****************************************
Virtual Machine Installation Options
****************************************

When you install devstack, fullstack, or analytics devstack you can customize
the environment. This section provides information about configuration options
for edX virtual machines.

================================================
Set Up Ability to Preview Units (Mac/Linux Only)
================================================

If you are installing an edX virtual machine on a Linux or Macintosh computer,
you must configure your installation to use the preview feature in edX Studio.

#. :ref:`Connect to the Devstack virtual machine<Connect to Devstack VM>`.

#. In the ``etc/hosts`` file, add the following line.

  .. code-block:: bash

    192.168.33.10 preview.localhost

===================================
Customize the Source Code Location
===================================

You can customize the location of the edX source code that gets cloned when you
provision an edX virtual machine. You may want to do this to have the edX
virtual machine work with source code that already exists on your computer.

By default, the source code location is the directory in which you run
``vagrant up``. To change this location, follow these steps.

#. :ref:`Connect to the Devstack virtual machine<Connect to Devstack VM>`.

#. Set the ``VAGRANT_MOUNT_BASE`` environment variable to set the base
   directory for the ``edx-platform`` and ``cs_comments_service`` source code
   directories.

.. include:: ../../../links/links.rst
