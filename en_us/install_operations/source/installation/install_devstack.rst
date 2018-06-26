.. _Installing and Starting Devstack:

#################################
Installing and Starting Devstack
#################################

This section provides information about how to install and start
the Open edX developer stack (devstack).

.. contents::
   :local:
   :depth: 1

.. _Installing the Open edX Developer stack:

****************************************
Installation Prerequisites for Devstack
****************************************

Before you install devstack, make sure that you have met the
:ref:`installation prerequisites<Installation Prerequisites>`.

You must also ensure that you have the administrator password for your local
computer. The administrator password is needed to configure NFS (network file
system) to allow users to access code directories directly from your computer.

.. _Install Devstack:

****************
Install Devstack
****************

To install devstack, follow these steps.

#. Check out a local copy of the ``edx/devstack`` repository from
   https://github.com/edx/devstack


WHAT ABOUT BRANCHES AND TAGS? What do you check out if you don't want to run master?

#. Create a ``devstack`` directory and navigate to it in the command prompt.

   .. code-block:: bash

     mkdir devstack
     cd devstack



When you have completed these steps, see :ref:`Starting the Open edX Developer
Stack` to begin using devstack.

For help with the devstack installation, see
:ref:`troubleshooting_devstack_installation`.


.. include:: ../../../../links/links.rst

