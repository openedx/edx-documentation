.. _Installing the Open edX Analytics Developer Stack:

#################################################
Installing Open edX Analytics Devstack
#################################################

This section describes how to install and run the Open edX Analytics developer
stack.

.. note::
 Before you install analytics developer stack, make sure that you have met
 the :ref:`installation prerequisites<Installation Prerequisites>`.

.. contents::
   :local:
   :depth: 1


*************************************
Installing the Software Prerequisites
*************************************

In addition to the :ref:`software prerequisites<Software Prerequisites>` that
fullstack and devstack require, for analytics devstack, you must install a
tool that the Open edX Analytics Pipeline uses to deploy itself. To install
this tool, follow these steps.

#. Clone the repository on your host, not on the virtual machine.

   .. code-block:: bash

      $ git clone https://github.com/edx/edx-analytics-pipeline


#. Install the project dependencies into a virtualenv on your host.

   .. code-block:: bash

      $ cd edx-analytics-pipeline
      $ virtualenv venv
      $ source venv/bin/activate
      $ make bootstrap

The system is now ready to start running tasks on analytics devstack
using the ``remote-task`` tool.


.. _Install the Analytics Devstack:

******************************
Installing Analytics Devstack
******************************

To install analytics devstack extensions directly from the command line,
follow these steps.

#. Create the ``analyticstack`` directory and navigate to it in the command
   prompt.

   .. code-block:: bash

     $ mkdir analyticstack
     $ cd analyticstack

#. Download the analytics devstack Vagrant file.

   .. code-block:: bash

     $ curl -L https://raw.github.com/edx/configuration/master/vagrant/release/analyticstack/Vagrantfile > Vagrantfile

#. Create the analytics devstack virtual machine.

   .. code-block:: bash

     $ vagrant up


.. include:: ../../../../links/links.rst
