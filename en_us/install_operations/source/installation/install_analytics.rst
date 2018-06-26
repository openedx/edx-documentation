.. _Installing and Starting Analytics devstack:

##########################################
Installing and Starting Analytics Devstack
##########################################

This section provides information about how to install and start
the Open edX analytics developer stack (analytics devstack).

.. contents::
   :local:
   :depth: 1

.. _Installing the Open edX Analytics devstack:

*************************************************
Installation Prerequisites for Analytics Devstack
*************************************************

Before you install analytics devstack, make sure that you have met the
:ref:`installation prerequisites<Installation Prerequisites>`.

You must also ensure that you have the administrator password for your local
computer. The administrator password is needed to configure NFS (network file
system) to allow users to access code directories directly from your computer.

.. _Install Analytics Devstack:

**************************
Install Analytics Devstack
**************************

To install analytics devstack, follow these steps.

#. Follow steps x y z in :ref:`Install Devstack`.

#. Pull the relevant docker images by running the following commands.
   .. code-block:: bash

     make pull
     make pull.analytics_pipeline

#. Configure the analytics devstack by running the following provision
   command.
   .. code-block:: bash
    make dev.provision.analytics_pipeline


When you have completed these steps, see :ref:`Starting the Open edX Developer
Stack` to begin using devstack.

For help with the devstack installation, see
:ref:`troubleshooting_devstack_installation`.


.. include:: ../../../../links/links.rst

