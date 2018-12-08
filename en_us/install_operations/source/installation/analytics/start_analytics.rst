.. _Starting the Open edX Analytics Developer Stack:

#################################################
Starting Open edX Analytics Devstack
#################################################

This section describes how to start the Open edX Analytics developer
stack (analytics devstack).

.. contents::
   :local:
   :depth: 1

****************************
Starting the Open edX LMS
****************************

#. Log in to analytics devstack.

   .. code-block:: bash

     $ vagrant ssh

#. Switch to the ``edxapp`` user.

   .. code-block:: bash

     $ sudo su edxapp

#. Start the LMS.

   .. code-block:: bash

     $ paver devstack lms

****************************************
Starting the Open edX Analytics Data API
****************************************

#. Log in to analytics devstack.

   .. code-block:: bash

     $ vagrant ssh

#. Switch to the ``analytics_api`` user.

   .. code-block:: bash

     $ sudo su analytics_api

#. Start the Data API.

   .. code-block:: bash

     $ ~/venvs/analytics_api/bin/python ~/analytics_api/manage.py runserver 0.0.0.0:8100 --insecure

**************************
Starting Open edX Insights
**************************

#. Log in to analytics devstack.

   .. code-block:: bash

     $ vagrant ssh

#. Switch to the ``insights`` user.

   .. code-block:: bash

     $ sudo su insights

#. Enable features that are disabled by default.

   .. code-block:: bash

     $ ./manage.py waffle_switch display_verified_enrollment on --create
     $ ./manage.py waffle_switch enable_course_api on --create

   For a complete list of the waffle switches that are available, see
   `Feature Gating`_.

#. Start Insights.

   .. code-block:: bash

     $ ~/venvs/insights/bin/python ~/edx_analytics_dashboard/manage.py runserver 0.0.0.0:8110 --insecure

#. Open the URL ``http://127.0.0.1:8110`` in a browser on the host.

   .. important:: Be sure to use the IP address ``127.0.0.1`` instead of
     ``localhost``. Using ``localhost`` will prevent you from logging in.

************************************************
Starting the Open edX Analytics Pipeline
************************************************

#. In the Devstack LMS, register a new user and enroll in the demo course.

#. Navigate to the course body and submit answers to a few problems.

#. Activate the data pipeline virtual environment as the ``hadoop`` user.

   .. code-block:: bash

     $ sudo su hadoop
     $ cd /edx/app/analytics_pipeline/
     $ . venvs/analytics_pipeline/bin/activate
     $ cd analytics_pipeline/
     $ export LUIGI_CONFIG_PATH="$PWD/config/devstack.cfg"

#. Run the enrollment task.

   .. code-block:: bash

     $ launch-task ImportEnrollmentsIntoMysql --local-scheduler --interval-end $(date +%Y-%m-%d -d "tomorrow") --n-reduce-tasks 1

#. Run the answer distribution task.

   .. code-block:: bash

     $ export UNIQUE_NAME=$(date +%Y-%m-%dT%H_%M_%SZ)
     $ launch-task AnswerDistributionWorkflow --local-scheduler \
           --src hdfs://localhost:9000/data/ \
           --include '*tracking.log*' \
           --dest hdfs://localhost:9000/edx-analytics-pipeline/output/answer_distribution_raw/$UNIQUE_NAME/data \
           --name $UNIQUE_NAME \
           --output-root hdfs://localhost:9000/edx-analytics-pipeline/output/answer_distribution/ \
           --marker hdfs://localhost:9000/edx-analytics-pipeline/output/answer_distribution_raw/$UNIQUE_NAME/marker \
           --n-reduce-tasks 1

.. include:: ../../../../links/links.rst

.. _Feature Gating: https://github.com/edx/edx-analytics-dashboard#feature-gating
