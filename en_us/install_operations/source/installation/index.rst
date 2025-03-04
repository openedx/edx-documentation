.. _Installing and Starting the Open edX Platform:

#############################################
Installing and Starting the Open edX Platform
#############################################

This section provides information about options for installing and
starting the Open edX platform.

We've tried to simplify the installation by providing a small number of
options, prepackaged to varying degrees. Before installing the Open edX platform, you have
two decisions to make:

* **Version**: What version of the code do you want?
* **Method**: How do you want to install it?

*******************
1. Choose a version
*******************

There are two possibilities for the version to install:

* **Master** is the latest version of the code.

* A **Release** is a version of the code marked and tested for wide use.  These
  are named alphabetically for trees: Sumac, Teak, Ulmo, etc. Look for the most
  recent release if you're beginning a new installation.

You should choose master only if you will be modifying the code and
contributing it back, or if you need a feature or fix that is newer than the
latest Open edX release.  If you aren't planning to contribute changes, and you
don't need the absolute latest code, use the latest official Open edX release.
Details of the releases are on the `Open edX Named Releases page`_.

********************************
2. Choose an installation method
********************************

**`Tutor`_**: is the community-supported Docker-based environment
  suited for both production and development.


Note that Tutor requires some foundational skills:

* Comfort with your chosen operating system.
* Using the command line to perform tasks.
* Some ability to diagnose and solve problems with system software.

You can find more details on each of the methods below:

.. toctree::
   :maxdepth: 2

   tutor

.. include:: ../../../links/links.rst
