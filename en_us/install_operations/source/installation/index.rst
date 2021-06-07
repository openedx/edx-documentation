.. _Installing and Starting the Open edX Platform:

#############################################
Installing and Starting the Open edX Platform
#############################################

This section provides information about options for installing and
starting the Open edX platform.

We've tried to simplify the installation by providing a small number of
options, prepackaged to varying degrees. Before installing Open edX, you have
two decisions to make:

* **Version**: What version of the code do you want?
* **Method**: How do you want to install it?

*******************
1. Choose a version
*******************

There are two possibilities for the version to install:

* **Master** is the latest version of the code, newer even than what is running
  on edx.org.
* A **Release** is a version of the code marked and tested for wide use.  These
  are named alphabetically for trees: Juniper, Koa, Lilac, etc.

You should choose master only if you will be modifying the code and
contributing it back, or if you need a feature or fix that is newer than the
latest Open edX release.  If you aren't planning to contribute changes, and you
don't need the absolute latest code, use the latest official Open edX release.
Details of the releases are at the `Open edX Releases Wiki Page`_.

********************************
2. Choose an installation method
********************************

The currently supported installation methods are:

* **Tutor**: (New for Lilac) A community-supported Docker-based environment
  suited for both production and development.
* **Native**: (Deprecated in Lilac, to be removed in Maple) Provides a
  production-ready installation on an Ubuntu machine of your own, using an
  Ansible playbook.
* **Devstack**: A development environment based on Docker; useful if you want
  to modify Open edX code locally.

Broadly speaking, the different methods all install the same collection of
software.  Which method you choose depends on what you'll be doing with your
installation:

* If you will be running a production installation on a **Release**, use
  **Tutor** or **Native**.
* If you want a production-like installation for testing a **Release**, you
  should also use either **Tutor** or **Native**.
* If you want a production-like installation for testing **Master**, you
  should use **Native**.
* If you will be modifying code on **Master**, use **Devstack**.

Note that all of them require some foundational skills:

* Comfort with your chosen operating system.
* Using the command line to perform tasks.
* Some ability to diagnose and solve problems with system software.

You can find more details on each of the methods below:

.. toctree::
   :maxdepth: 2

   tutor
   native_installation
   devstack

.. include:: ../../../links/links.rst
