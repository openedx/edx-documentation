.. _Installing the Open edX Analytics Stack on a Single Instance:

############################################################
Installing Open edX Analytics on a Single Instance
############################################################

This page describes how to set up the analytics stack in a small scale production-like setup,
all on one box, with no use of AWS-specific features. The setup is mostly automated using ansible,
but still has a few pieces that are manual.

.. note::

   This is a "production-like" setup, but requires some tweaking to be truly production quality.
   For example: we strongly recommend you use HTTPS instead of HTTP for both insights and
   the LMS in production environments. These instructions do not yet contain complete instructions
   for setting up the system using HTTPS, but there is some stuff in here to help get you started.

.. note::

     Installation advice: Don't run it on an existing edx platform. Yarn nodemanager will collide with xqueue service
     on port 8040. Tasks will be submitted but they will never be processed.

     For reference see:

     - ``yarn nodemanager default port`` -> https://goo.gl/1uy6kx 
     - ``xqueue default port`` -> https://goo.gl/Ra5g3R.
     
.. _Installation Overview:

******************************
Installation Overview
******************************

#. Set up a new box and ensure it can connect to the LMS and the LMS mysql DB
#. Run ansible to install all the things and do most of the configuration
#. Manually finish a few bits of configuration (in particular, OAuth config on the LMS side)
#. Copy over tracking logs and run some test jobs
#. Automate loading of tracking logs and schedule jobs to run regularly


.. _Installation Script:

*****************************
Installation Script
*****************************

Below is a script to install all the things.

.. note::

   #. It expects to find a tracking.log file in the home directory – put an LMS log there before you run this.
   #. You'll need to manually run the OAuth management command on your LMS system – see below.
   #. You may need to do some network config to make sure your machines have the right ports open. See below.

Run the following on a new Ubuntu 16.04 box as a user that has sudo privileges.

   .. code-block:: bash

      #!/bin/bash
      LMS_HOSTNAME="https://lms.mysite.org"
      INSIGHTS_HOSTNAME="http://127.0.0.1:8110"  # Change this to the externally visible domain and scheme for your Insights install, ideally HTTPS
      DB_USERNAME="read_only"
      DB_HOST="localhost"
      DB_PASSWORD="password"
      DB_PORT="3306"
      # Run this script to set up the analytics pipeline
      echo "Assumes that there's a tracking.log file in \$HOME"
      sleep 2
      
      echo "Create ssh key"
      ssh-keygen -t rsa -f ~/.ssh/id_rsa -P ''
      echo >> ~/.ssh/authorized_keys # Make sure there's a newline at the end
      cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
      # check: ssh localhost "echo It worked!" -- make sure it works.
      echo "Install needed packages"
      sudo apt-get update
      sudo apt-get install -y git python-pip python-dev libmysqlclient-dev
      sudo pip install virtualenv
      echo 'create an "ansible" virtualenv and activate it'
      virtualenv ansible
      . ansible/bin/activate
      git clone https://github.com/edx/configuration.git
      
      cd configuration/
      pip install -r requirements.txt
      cd playbooks/edx-east/
      echo "running ansible -- it's going to take a while"
      ansible-playbook -i localhost, -c local analytics_single.yml --extra-vars "INSIGHTS_LMS_BASE=$LMS_HOSTNAME INSIGHTS_BASE_URL=$INSIGHTS_HOSTNAME"
      
      echo "-- Set up pipeline"
      cd $HOME
      sudo mkdir -p /edx/var/log/tracking
      sudo cp ~/tracking.log /edx/var/log/tracking
      sudo chown hadoop /edx/var/log/tracking/tracking.log
      
      echo "Waiting 70 seconds to make sure the logs get loaded into HDFS"
      # Hack hackity hack hack -- cron runs every minute and loads data from /edx/var/log/tracking
      sleep 70
      
      # Make a new virtualenv -- otherwise will have conflicts
      echo "Make pipeline virtualenv"
      virtualenv pipeline
      . pipeline/bin/activate
      
      echo "Check out pipeline"
      git clone https://github.com/edx/edx-analytics-pipeline
      cd edx-analytics-pipeline
      make bootstrap
      # HACK: make ansible do this
      cat <<EOF > /edx/etc/edx-analytics-pipeline/input.json
      {"username": $DB_USERNAME, "host": $DB_HOST, "password": $DB_PASSWORD, "port": $DB_PORT}
      EOF
      
      echo "Run the pipeline"
      # Ensure you're in the pipeline virtualenv
      remote-task --host localhost --repo https://github.com/edx/edx-analytics-pipeline --user ubuntu \
        --override-config $HOME/edx-analytics-pipeline/config/devstack.cfg --remote-name analyticstack \
	--wait TotalEventsDailyTask --interval 2016 --output-root hdfs://localhost:9000/output/ --local-scheduler
      
      echo "If you got this far without error, you should try running the real pipeline tasks listed/linked below"

.. _Installation Details:

***********************
Installation Details
***********************

#. Gather information:
   
    a. url to your LMS. e.g. lms.mysite.org
       
    b. url and credentials to your LMS DB. e.g. mysql.mysite.org
       
#. Create a box to use for the analytics stack (e.g. analytics.mysite.org).
   
    a. We started with a blank ubuntu 16.04 AMI on AWS
	
    b. Ensure that this box can talk to the LMS via HTTP ::

        curl lms.mysite.org

    c. Ensure that this box can connect to the DB ::

        telnet mysql.mysite.org 3306

    d. Ensure that the box has the following ports open ::

        80 -- for insights (actually 18110 at the moment -- should be changed)

    e. Install git and python tools ::

        sudo apt-get update
        sudo apt-get install git
        sudo apt-get install python-pip
        sudo apt-get install python-dev
        sudo pip install virtualenv

    f. Create a new virtual environment ::

        virtualenv ansible
        . ansible/bin/activate

#. Run ansible to set up most of the services. This script will do the following:

   a. Install and configure hadoop, hive and sqoop
      
   b. Configure SSH daemon on the hadoop master node
      
   c. Configure the result store database
      
    1. Setup databases
    2. Setup Users
       
   d. Configure data API
      
    1. Shared secret
    2. Database connection
       
   e. Configure Insights
      
    1. API shared secret
    2. Tell insights where the LMS is
       
   The script: ::

    git clone https://github.com/edx/configuration.git
    cd configuration/
    pip install -r requirements.txt
    cd playbooks/edx-east/
    ansible-playbook -i localhost, -c local analytics_single.yml --extra-vars "INSIGHTS_LMS_BASE=mysite.org"
    # (If your site uses https, change the scheme and set the oauth flag to true. Enforce_secure means "insist on https".)
    # wait for a while
#. Sanity Checks

   a. Run the built-in "compute pi" hadoop job ::

       sudo su - hadoop
       cd /edx/app/hadoop
       hadoop jar hadoop*/share/hadoop/mapreduce/hadoop-mapreduce-examples*.jar pi 2 100
       # it should compute something approximating pi

   b. Make sure you can run hive ::

       /edx/app/hadoop/hive/bin/hive
       # hive should start,
       # use ^D to get back to your regular user

   c. The Insights application should be up - go to insights.mysite.org and make sure the home page is there. You won't
      be able to login yet. ::

       # Insights gunicorn is on port 8110
       curl localhost:8110
       
       # Insights nginx (the externally-facing view) should be on port 18110
       curl mybox.org:18110

#. Place some test logs into HDFS

   a. copy some log files into the hdfs system ::

       # scp tracking.log onto the machine from your LMS. Then do the following:
       sudo mkdir /edx/var/log/tracking
       sudo cp /path/to/tracking.log /edx/var/log/tracking
       sudo chown hadoop /edx/var/log/tracking/tracking.log
       # wait 60 seconds - ansible creates a cron job to load files in that directory every minute

       # check that it exists
       hdfs dfs -ls /data
        
       # should find this:
       Found 1 items
       -rw-r--r--   1 hadoop supergroup     308814 2015-10-15 14:31 /data/tracking.log

   b. Setup the pipeline ::

       ssh-keygen -t rsa -f ~/.ssh/id_rsa -P ''
       echo >> ~/.ssh/authorized_keys # Make sure there's a newline at the end
       cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
       # check: ssh localhost "echo It worked!" -- make sure it works.
         
       # Make a new virtualenv -- otherwise will have conflicts
       virtualenv pipeline
       . pipeline/bin/activate
           
       git clone https://github.com/edx/edx-analytics-pipeline
       cd edx-analytics-pipeline
         
       make bootstrap

   c. Check the pipeline installation by running a simple job to count events per day. There are many parameters to
      setup the pipeline before running the job. We'll be able to use `--skip-setup` below. The user should be set to the
      current user (that has the ssh self-login setup). ::

       # Ensure you're in the pipeline virtualenv 
       remote-task --host localhost \
         --repo https://github.com/edx/edx-analytics-pipeline \
         --user ubuntu \
         --override-config $HOME/edx-analytics-pipeline/config/devstack.cfg \
         --remote-name analyticstack \
         --wait TotalEventsDailyTask \
         --interval 2015 \
         --output-root hdfs://localhost:9000/output/ \
         --local-scheduler

#. Finish the rest of the pipeline configuration

   a. Write config files for the pipeline so that it knows where the LMS database is: ::

       sudo vim /edx/etc/edx-analytics-pipeline/input.json
       # put in the right url and credentials for your LMS database

   b. Test it (Note the ``--skip-setup`` option can be added to subsequent calls to ``remote-task`` in cases where the "setup" does  not need to be repeated). ::

	 remote-task --host localhost \
           --user ubuntu \
           --remote-name analyticstack \
           --skip-setup \
           --wait CourseEnrollmentEventsTask \
           --interval 2016 \
           --local-scheduler

   c. Confirm the test succeeded ::

       sudo mysql
       SELECT * FROM reports.course_enrollment_daily;
       # This should show you enrollments over time. Note that this only counts enrollment in the event logs -
       if you manually created users or enrollments in the database, they won't be counted here.

#. Finish the LMS -> Insights SSO configuration via LMS OAuth Trusted Client Registration. You'll be setting up the
   connection between Insights and the LMS, so single sign on will work.

   a. Run the following Django Management command *on the LMS machine* ::

       sudo su edxapp
       /edx/bin/python.edxapp /edx/bin/manage.edxapp lms --setting=aws create_oauth2_client \
         http://107.21.156.121:18110 \
	 http://107.21.156.121:18110/complete/edx-oidc/ \
	 confidential \
	 --client_name insights \
	 --client_id YOUR_OAUTH2_KEY \
	 --client_secret secret \
	 --trusted
         
       # Replace "secret", "YOUR_OAUTH2_KEY", and the url of your Insights box.
       # INSIGHTS_BASE_URL
       # INSIGHTS_OAUTH2_KEY
       # INSIGHTS_OAUTH2_SECRET
       # Also set other secrets to more secret values.
         
       # Ensure that JWT_ISSUER and OAUTH_OIDC_ISSUER on the LMS in /edx/app/edxapp/lms.env.json match the url root in
       # /edx/etc/insights.yml (SOCIAL_AUTH_EDX_OIDC_URL_ROOT). This should be the case unless your environment is weird
       (ala edx sandboxes are really username.sandbox.edx.org but the setting is "int.sandbox.edx.org")

   b. Check it by logging into LMS as a staff user, then ensure that you can log into Insights and see all the courses
      you have staff access to.

#. Automate copying of logs. You probably don't want to do it manually every time. Some options:

   a. Create a cron job that copies all of the logs from the LMS servers regularly.

   b. Create a job to copy logs to S3 and use S3 as your HDFS store (and update your config accordingly).

#. Schedule `launch-task` jobs to actually run all the pipeline tasks regularly.

   a. Here is the list of tasks: https://github.com/edx/edx-analytics-pipeline/wiki/Tasks-to-Run-to-Update-Insights ::

       # Ensure you're in the pipeline virtualenv
       remote-task --host localhost \
         --user ubuntu \
         --remote-name analyticstack \
         --skip-setup \
         --wait CourseActivityWeeklyTask \
         --local-scheduler \
         --end-date $(date +%Y-%m-%d -d "today") \
         --weeks 24 \
         --n-reduce-tasks 1	  # number of reduce slots in your cluster -- we only have 1


************
Resources
************
- `The ansible playbook we use <https://github.com/edx/configuration/blob/master/playbooks/edx-east/analytics_single.yml>`_
- `Analytics devstack docs <http://edx.readthedocs.io/projects/edx-installing-configuring-and-running/en/latest/installation/analytics/index.html>`_
- `Analytics configuration <https://github.com/edx/edx-analytics-configuration>`_
- `Updating insights <https://github.com/edx/edx-analytics-pipeline/wiki/Tasks-to-Run-to-Update-Insights>`_
- `Mailing list <https://groups.google.com/forum/#!forum/openedx-ops>`_
