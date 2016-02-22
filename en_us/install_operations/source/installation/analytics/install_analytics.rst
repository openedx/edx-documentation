.. _Installing the Open edX Analytics Developer Stack:

#################################################
Installing the Open edX Analytics Developer Stack
#################################################

This section describes how to install and run the Open edX Analytics Developer
Stack.

.. note::
 Before you install Open edX Fullstack, make sure that you have met
 the :ref:`installation prerequisites<Installation Prerequisites>`.

.. contents::
   :local:
   :depth: 1


***********************************
Install the Software Prerequisites
***********************************

In addition to the :ref:`software prerequisites<Software Prerequisites>` that Fullstack and Devstack require,
for the Analytics Devstack, you must install a tool that the Open edX Analytics
Pipeline uses to deploy itself. To install this tool, follow these steps.

#. Clone the repository on your host, not on the virtual machine.

   .. code-block:: bash

      $ git clone https://github.com/edx/edx-analytics-pipeline


#. Install the project dependencies into a virtualenv on your host.

   .. code-block:: bash

      $ cd edx-analytics-pipeline
      $ virtualenv venv
      $ source venv/bin/activate
      $ make bootstrap

The system is now ready to start running tasks on the Analytics Devstack
using the ``remote-task`` tool.


.. _Install the Analytics Devstack:

******************************
Install the Analytics Devstack
******************************

To install the Analytics Devstack extensions directly from the command line,
follow these steps.

#. Create the ``analyticstack`` directory and navigate to it in the command
   prompt.

   .. code-block:: bash

     $ mkdir analyticstack
     $ cd analyticstack

#. Download the Analytics Devstack Vagrant file.

   .. code-block:: bash

     $ curl -L https://raw.github.com/edx/configuration/master/vagrant/release/analyticstack/Vagrantfile > Vagrantfile

#. Create the Analytics Devstack virtual machine.

   .. code-block:: bash

     $ vagrant up


.. include:: ../../../../links/links.rst
