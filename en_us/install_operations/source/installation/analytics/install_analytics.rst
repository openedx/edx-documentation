.. _Installing the Open edX Analytics Developer Stack:

#################################################
Installing Open edX Analytics Devstack
#################################################

This section describes how to install and run the Open edX Analytics developer
stack.

.. note::
 Before you install analytics developer stack, make sure that you have met
 the :ref:`installation prerequisites<Installation Prerequisites>`.

.. _Install the Analytics Devstack:

******************************
Installing Analytics Devstack
******************************

To install analytics devstack extensions directly from the command line,
follow these steps.

#. Halt any running Open edX devstacks. Navigate to the directory that contains the Vagrantfile for the devstack and run ``vagrant suspend`` or ``vagrant halt``.

   .. code-block:: bash

     $ cd ~/open-edx/devstack/
     $ vagrant suspend

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

#. Clone the edx-analytics-pipeline repository.

   .. code-block:: bash

     $ git clone git@github.com:edx/edx-analytics-pipeline.git ./edx-analytics-pipeline/

#. Prepare the data pipeline inside the virtual machine.

   .. code-block:: bash

     $ vagrant ssh
     $ cd /edx/app/analytics_pipeline/
     $ sudo mkdir venvs
     $ sudo chown vagrant:vagrant venvs
     $ virtualenv venvs/analytics_pipeline/
     $ . venvs/analytics_pipeline/bin/activate
     $ cd analytics_pipeline
     $ make system-requirements
     $ make develop

   .. note::

      The version of edx-analytics-pipeline that you checked out on your host will be mounted at ``/edx/app/analytics_pipeline/analytics_pipeline`` inside the virtual machine. Vagrant directory sharing allows the code to be modified using an editor on the host machine and executed within the virtual machine.

#. Run tests and quality checks.

   .. code-block:: bash

     $ make coverage

#. Run the acceptance tests as the hadoop user.

   .. code-block:: bash

     $ sudo su hadoop
     $ cd /edx/app/analytics_pipeline/
     $ . venvs/analytics_pipeline/bin/activate
     $ cd analytics_pipeline

     # The next step will take hours to run.
     $ make test-acceptance-local

   A subset of acceptance tests can be run using the ``ONLY_TESTS`` parameter.

   .. code-block:: bash

     $ make test-acceptance-local ONLY_TESTS=edx.analytics.tasks.tests.acceptance.test_enrollments

   Acceptance tests usually destroy any existing state before running. This behavior can be disabled by setting the ``DISABLE_RESET_STATE`` environment variable.

   .. code-block:: bash

     $ DISABLE_RESET_STATE=true make test-acceptance-local ONLY_TESTS=edx.analytics.tasks.tests.acceptance.test_enrollments

   .. note::

      Acceptance tests emulate deployment of the code to a remote Hadoop cluster. During this process the tests check out a new copy of the code from the repo. For this reason, all changes must be committed before running the test.

#. Display parameters for a task. You can use the following technique to see the parameters for any task.

   .. code-block:: bash

     $ export LUIGI_CONFIG_PATH="$PWD/config/devstack.cfg"
     $ launch-task ImportEnrollmentsIntoMysql --help

   The `EdX Analytics Pipeline Reference Guide <http://edx-analytics-pipeline-reference.readthedocs.io/en/latest/index.html>`_ contains a more detailed list of available tasks and their parameters.

.. include:: ../../../../links/links.rst
