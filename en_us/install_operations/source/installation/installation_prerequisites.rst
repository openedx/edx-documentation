.. _Installation Prerequisites:

######################################################
Installation Prerequisites
######################################################

To use devstack or analytics devstack successfully, you must meet the
following knowledge and software requirements.

**************************
Knowledge Prerequisites
**************************

Devstack and analytics devstack require an understanding of the
following items.

* Basic terminal usage. If you are using a Mac computer, see
  `Introduction to the Mac OS X Command Line`_. If you are using a Windows
  computer, see `Windows Command Line Reference`_.

>>>> WHAT is DOCKER EQUIVALENT?
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

Devstack and analytics devstack require the following software.

* `Docker`_ 17.06 CE or later. We recommend Docker Stable, but Docker Edge
  should work as well.

* make >>> XREF

* An NFS (network file system) client, if your operating system does not
  include one. NFS allows devstack and fullstack virtual machines to share a
  common file system with host computers.

.. include:: ../../../links/links.rst
