.. _Installing the Open edX Analytics Developer Stack:

#################################################
Installing the Open edX Analytics Developer Stack
#################################################

This section describes how to install and run the Open edX Analytics Developer
Stack.

.. contents::
   :local:
   :depth: 1

**********
Overview
**********

The Open edX Analytics Developer stack, known as the Analytics Devstack, is a
modified version of the :ref:`Open edX Developer Stack<Installing the Open edX
Developer Stack>`.

It provides all of the services and tools needed to modify the Open
edX Analytics Pipeline, Data API, and Insights projects.

********************
Components
********************

The Analytics Devstack includes the following additional components.

* edX Analytics Data API
* edX Insights

The Analytics Devstack also includes all of the components needed to run the
Open edX Analytics Pipeline, which is the primary ETL (extract, transform, and
load) tool that extracts and analyzes data from the other Open edX services.

***********************************
Install the Software Prerequisites
***********************************

To install and run the Analytics Devstack, you must first install the following
required software.

* `VirtualBox`_ 4.3.12 or higher

* `Vagrant`_ 1.6.5 or higher

* A Network File System (NFS) client, if your operating system does not already
  include one. Devstack uses VirtualBox Guest Editions to share folders through NFS.

Additionally, the Open edX Analytics Pipeline includes a tool that is used to
deploy itself. To make use of these tools, follow these steps.

#. Clone the repository on your host, not on the Virtual Machine.

  .. code-block:: bash

     $ git clone https://github.com/edx/edx-analytics-pipeline


2. Install the project dependencies into a virtualenv on your host.

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

2. Download the Analytics Devstack Vagrant file.
   
   .. code-block:: bash

     $ curl -L https://raw.github.com/edx/configuration/master/vagrant/release/analyticstack/Vagrantfile > Vagrantfile

3. Create the Analytics Devstack virtual machine.

   .. code-block:: bash

     $ vagrant up


****************************
Using the Analytics Devstack
****************************

====================
Run the Open edX LMS
====================

#. Log in to the Analytics Devstack.
   
   .. code-block:: bash

     $ vagrant ssh

2. Switch to the ``edxapp`` user.
   
   .. code-block:: bash

     $ sudo su edxapp

3. Start the LMS.
   
   .. code-block:: bash
     
     $ paver devstack lms

===================================
Run the Open edX Analytics Data API
===================================

#. Log in to the Analytics Devstack.
   
   .. code-block:: bash

     $ vagrant ssh

2. Switch to the ``analytics_api`` user.
   
   .. code-block:: bash

     $ sudo su analytics_api

3. Start the Data API.
   
   .. code-block:: bash

     $ ~/venvs/analytics_api/bin/python ~/analytics_api/manage.py runserver 0.0.0.0:8100 --insecure

=====================
Run Open edX Insights
=====================

#. Log in to the Analytics Devstack.
   
   .. code-block:: bash

     $ vagrant ssh

2. Switch to the ``insights`` user.
   
   .. code-block:: bash

     $ sudo su insights

3. Enable features that are disabled by default.

   .. code-block:: bash

     $ ~/venvs/insights/bin/python ~/edx_analytics_dashboard/manage.py switch display_verified_enrollment on --create
     $ ~/venvs/insights/bin/python ~/edx_analytics_dashboard/manage.py switch enable_course_api on --create

4. Start Insights.
   
   .. code-block:: bash

     $ ~/venvs/insights/bin/python ~/edx_analytics_dashboard/manage.py runserver 0.0.0.0:8110 --insecure

5. Open the URL ``http://127.0.0.1:8110`` in a browser on the host. 

   .. important:: Be sure to use the IP address ``127.0.0.1`` instead of 
     ``localhost``. Using ``localhost`` will prevent you from logging in.

===================================
Run the Open edX Analytics Pipeline
===================================

#. In the Devstack LMS, register a new user and enroll in the demo course.

#. Navigate to the courseware and submit answers to a few problems.

#. Navigate to the location where edx-analytics-pipeline project was cloned on
   the host.
   
   .. code-block:: bash

     $ cd edx-analytics-pipeline

4. Run the enrollment task.
   
   .. code-block:: bash

     $ export WHEEL_URL=http://edx-wheelhouse.s3-website-us-east-1.amazonaws.com/Ubuntu/precise
     # On Mac OS X replace the date command below with $(date -v+1d +%Y-%m-%d)
     $ remote-task --vagrant-path <path to `analyticstack`> --remote-name devstack --override-config ${PWD}/config/devstack.cfg --wheel-url $WHEEL_URL --wait \
        ImportEnrollmentsIntoMysql --local-scheduler --interval-end $(date +%Y-%m-%d -d "tomorrow") --n-reduce-tasks 1

5. Run the answer distribution task.

   .. code-block:: bash

    $ export WHEEL_URL=http://edx-wheelhouse.s3-website-us-east-1.amazonaws.com/Ubuntu/precise
    $ export UNIQUE_NAME=$(date +%Y-%m-%dT%H_%M_%SZ)
    $ remote-task --vagrant-path <path to `analyticstack`> --remote-name devstack --override-config ${PWD}/config/devstack.cfg --wheel-url $WHEEL_URL --wait \
        AnswerDistributionWorkflow --local-scheduler \
          --src hdfs://localhost:9000/data/ \
          --include '*tracking.log*' \
          --dest hdfs://localhost:9000/edx-analytics-pipeline/output/answer_distribution_raw/$UNIQUE_NAME/data \
          --name $UNIQUE_NAME \
          --output-root hdfs://localhost:9000/edx-analytics-pipeline/output/answer_distribution/ \
          --marker hdfs://localhost:9000/edx-analytics-pipeline/output/answer_distribution_raw/$UNIQUE_NAME/marker \
          --n-reduce-tasks 1

.. include:: ../../../links/links.rst
