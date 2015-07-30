.. include:: ../links.rst

.. _Installing the Open edX Analytics Developer Stack:

#################################################
Installing the Open edX Analytics Developer Stack
#################################################

This chapter is intended for those who are installing and running the Open edX
Analytics Developer Stack.

.. contents:: Chapter Contents:


**********
Overview
**********

The Open edX Analytics Developer stack is an extension to the :ref:`Open edX
Developer Stack <Installing the Open edX Developer Stack>`.

It provides all of the services and tools needed to extend the Open edX
Analytics Pipeline, Data API and Insights projects.

********************
Components
********************

The Analytics Devstack includes the following additional components:

* edX Analytics Data API
* edX Insights

Analytics Devstack also includes all components needed to run the edX
Analytics Pipeline, the primary Extract Transform and Load (ETL) tool used to
exctract and analyze data from the other Open edX services.

**************************
Software Prerequisites
**************************

To install and run the Analytics Devstack, you must first install the base
:ref:`Open edX Developer Stack <Installing the Open edX Developer Stack>`.

Open edX Analytics Pipeline includes a tool that is used to deploy itself.
In order to make use of these tools, follow the instructions below.


1. Clone the repository.

  .. code-block:: bash

     git clone https://github.com/edx/edx-analytics-pipeline


2. Install the project dependencies.

  .. code-block:: bash

     make bootstrap

The system is now ready to start running tasks on the Analytics Devstack
using the `remote-task` tool.

  
.. _Install the Analytics Devstack:  

******************************
Install the Analytics Devstack
******************************

To install the Analytics Devstack extensions directly from the command line,
follow the instructions below.

1. Navigate to the directory where you installed the base Open edX Devstack.

  .. code-block:: bash

     cd devstack

#. Login to the base Open edX Devstack.
   
   .. code-block:: bash

     vagrant ssh

#. Install the Analytics Devstack extensions.
   
   .. code-block:: bash

     cd /edx/app/edx_ansible/edx_ansible/playbooks/edx-east
     /edx/app/edx_ansible/venvs/edx_ansible/bin/ansible-playbook -i localhost, -c local analytics_single.yml


****************************
Using the Analytics Devstack
****************************

====================
Run the Open edX LMS
====================

#. Login to the base Open edX Devstack.
   
   .. code-block:: bash

     vagrant ssh

#. Switch to the edxapp user.
   
   .. code-block:: bash

     sudo su edxapp

#. Start the LMS.
   
   .. code-block:: bash
     
     paver devstack lms

===================================
Run the Open edX Analytics Data API
===================================

#. Login to the base Open edX Devstack.
   
   .. code-block:: bash

     vagrant ssh

#. Switch to the analytics_api user.
   
   .. code-block:: bash

     sudo usermod analytics_api -s /bin/bash
     sudo su analytics_api

#. Start the Data API.
   
   .. code-block:: bash

     cd /edx/app/analytics_api
     . analytics_api_env
     venvs/analytics_api/bin/python analytics_api/manage.py runserver 0.0.0.0:8100 --insecure

=====================
Run Open edX Insights
=====================

#. Login to the base Open edX Devstack.
   
   .. code-block:: bash

     vagrant ssh

#. Switch to the insights user.
   
   .. code-block:: bash

     sudo usermod insights -s /bin/bash
     sudo su insights

#. Enable features that are disabled by default.

   .. code-block:: bash

    venvs/insights/bin/python edx_analytics_dashboard/manage.py switch display_verified_enrollment on --create
    venvs/insights/bin/python edx_analytics_dashboard/manage.py switch enable_course_api on --create

#. Start Insights.
   
   .. code-block:: bash

     cd /edx/app/insights
     . insights_env
     venvs/insights/bin/python edx_analytics_dashboard/manage.py runserver 0.0.0.0:8110 --insecure

#. Open the URL `http://127.0.0.1:8110` in a browser on the host. It is important to use the IP address `127.0.0.1` instead of `localhost`, using `localhost` will prevent you from being able to login.

===================================
Run the Open edX Analytics Pipeline
===================================

#. Create a new user in the LMS and enroll in the demo course.

#. Navigate to the courseware and submit answers to a few problems.

#. Navigate to the location where edx-analytics-pipeline project was cloned on the host.
   
   .. code-block:: bash

     cd edx-analytics-pipeline

#. Run the enrollment task.
   
   .. code-block:: bash

     remote-task --vagrant-path <path to `devstack`> --remote-name devstack --override-config ${PWD}/config/devstack.cfg --wait \
        ImportEnrollmentsIntoMysql --local-scheduler --interval-end $(date +%Y-%m-%d -d "tomorrow") --n-reduce-tasks 1

#. Run the answer distribution task.

   .. code-block:: bash

    remote-task --vagrant-path <path to `devstack`> --remote-name devstack --override-config ${PWD}/config/devstack.cfg --wait \
        AnswerDistributionWorkflow --local-scheduler \
          --src hdfs://localhost:9000/data/ \
          --include '*tracking.log*' \
          --dest hdfs://localhost:9000/edx-analytics-pipeline/output/answer_distribution_raw/dt=$(date +%Y-%m-%d -d "today")/data \
          --name devstack_$(date +%Y-%m-%d -d "today") \
          --output-root hdfs://localhost:9000/edx-analytics-pipeline/output/answer_distribution/ \
          --marker hdfs://localhost:9000/edx-analytics-pipeline/output/answer_distribution_raw/dt=$(date +%Y-%m-%d -d "today")/marker \
          --n-reduce-tasks 1
