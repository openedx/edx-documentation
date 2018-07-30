.. _Installation Prerequisites:

######################################################
Installation Prerequisites
######################################################

To use Devstack or Analytics Devstack successfully, you must meet the
following knowledge and software requirements.

**************************
Knowledge Prerequisites
**************************

Devstack and Analytics Devstack require an understanding of the
following items.

* Basic terminal usage. If you are using a Mac computer, see
  `Introduction to the Mac OS X Command Line`_.
* Diagnosing and fixing failures may involve many different technologies and
  skills. It will help to know these things.

  - The basics of how Python web applications are built, installed, and
    deployed.

  - How to manage a Linux system, including supervisor.

  - The basics of configuration management and automation.  We use `Ansible`_
    to automate the installation process.

.. _Software Prerequisites:

************************
Software Prerequisites
************************

Devstack and Analytics Devstack require the following software.

* `make`_
* `Docker`_ 17.06 CE or later. We recommend Docker Stable, but Docker Edge
  should work as well.

You must have ``docker-compose`` in your path. On macOS, installing Docker for 
Mac takes care of this requirement.

=======================================
Allocate Sufficient Resources to Docker
=======================================

Since a Docker-based Devstack runs many containers, you should configure Docker with a sufficient amount of resources. We find that configuring Docker for Mac with a minimum of 2 CPUs and 6GB of memory works well. For more information, see the `Docker documentation`_.

======================
Use overlay2 on Linux
======================

If you are using Linux, use the ``overlay2`` storage driver, kernel version
4.0+ and *not* ``overlay``. To check which storage driver your
``docker-daemon`` uses, run the following command.

  .. code-block:: bash

   docker info | grep -i 'storage driver'


.. include:: ../../../links/links.rst
