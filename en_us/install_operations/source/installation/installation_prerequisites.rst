.. _Installation Prerequisites:

######################################################
Installation Prerequisites
######################################################

To use devstack, fullstack, or analytics devstack, you must meet the
following knowledge and software requirements.

**************************
Knowledge Prerequisites
**************************

Devstack, fullstack, and analytics devstack require an understanding of the
following items.

* Basic terminal usage. If you are using a Mac computer, see
  `Introduction to the Mac OS X Command Line`_. If you are using a Windows
  computer, see `Windows Command Line Reference`_.

* Vagrant commands. See the `Vagrant Getting Started`_ guide for
  more information.

* Diagnosing and fixing failures may involve many different technologies and
  skills. It will help to know these things.

  - The basics of how Python web applications are built, installed, and
    deployed.

  - How to manage a Linux system, including supervisor.

  - The basics of configuration management and automation.  We use `Ansible`_
    to automate the installation process.


.. _Software Prerequisites:

**************************
Software Prerequisites
**************************

Devstack, fullstack, and analytics devstack require the following software.

* `VirtualBox`_ 4.3.12 or later.

* `Vagrant`_ 1.6.5 or later.

* An NFS (network file system) client, if your operating system does not
  include one. NFS allows devstack and fullstack virtual machines to share a
  common file system with host computers.

.. include:: ../../../links/links.rst
