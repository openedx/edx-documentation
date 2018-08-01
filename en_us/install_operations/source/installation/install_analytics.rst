.. _Installing and Starting Analytics devstack:

##########################################
Installing and Starting Analytics Devstack
##########################################

This section provides information about how to install and start
the Open edX analytics developer stack (Analytics Devstack).

.. contents::
   :local:
   :depth: 1

.. _Installing the Open edX Analytics devstack:

*************************************************
Installation Prerequisites for Analytics Devstack
*************************************************

Before you install Analytics Devstack, make sure that you have met the
:ref:`installation prerequisites<Installation Prerequisites>`.

.. _Install Analytics Devstack:

**************************
Install Analytics Devstack
**************************

To install Analytics Devstack, follow these steps.

#. Follow steps 1 through 6 in :ref:`Install Devstack`.

#. Pull the relevant Docker images by running the following commands.
   
   .. code-block:: bash

     make pull
     make pull.analytics_pipeline

#. Configure the Analytics Devstack by running the following provision
   command.

   .. code-block:: bash
    
    make dev.provision.analytics_pipeline

#. Start the analytics service by running the following command.

   .. code-block:: bash
    
    make dev.up.analytics_pipeline

   This command mounts the respositories under the ``DEVSTACK_WORKSPACE`` 
   directory. Note that it may take up to 60 seconds for Hadoop services to 
   start.

 #. Access the analytics pipeline shell by running the following command.  

   .. code-block:: bash
    
    make analytics-pipeline-shell

=================
Viewing Logs
=================

To see logs from containers running in detached mode, run the following 
command.

  .. code-block:: bash
   
   make logs

As an alternative, you can use Docker's Kitematic feature, which is available from the **Docker for Mac** menu.

To view the logs of a specific service container, run a 
``make <service>-logs`` command. For example, to access the logs for Hadoop's 
namenode, run this command.

  .. code-block:: bash
   
   make namenode-logs

For additional information, see :ref:`Starting Devstack`.

For help with running the Analytics Devstack, see
:ref:`Troubleshooting Devstack`.


.. include:: ../../../links/links.rst

