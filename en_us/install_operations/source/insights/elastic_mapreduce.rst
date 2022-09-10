.. _Using Elastic MapReduce on AWS:

******************************************
Using Elastic MapReduce on AWS
******************************************

This topic provides an overview of the components and services that you set up
and configure in a deployment that uses Amazon EMR. Work to prepare complete
installation procedures for edX Insights is in progress.

.. contents::
 :local:
 :depth: 1

For more information about AWS, including detailed procedures, see the `AWS
Documentation`_.

.. important::
 The tasks described by this topic rely on the use of third-party services and
 software. Because the services and software are subject to change by their
 owners, the information provided here is intended as a guideline and not as
 exact procedures.

======================
Virtual Private Cloud
======================

Create a Virtual Private Cloud (VPC) with at least one public subnet. A
limitation of EMR running in a VPC is that clusters must be deployed into
public subnets of VPCs. An existing VPC can be used if one is already available
for use.

EdX recommends that you configure the VPC to have at least one private subnet
in addition to the required public subnet. A private subnet is not required.
For more information, see the `example configuration scenario`_
in the *Amazon Virtual Private Cloud User Guide* published by AWS.

An example configuration that includes only `a single public subnet`_
can also be found in the *Amazon Virtual Private Cloud User Guide*.

Other Considerations
*********************

* To take advantage of price fluctuations in the `spot pricing market`_ , you
  can also deploy several public subnets in different availability zones.

* Consider that the clusters deployed using EMR will need network connectivity
  to a read replica of the LMS database. EdX recommends that you use the same
  VPC as the LMS if possible.

* While it is possible to run all of these services outside of a VPC, edX does
  not recommend doing so.

===============================
Identity and Access Management
===============================

For Amazon Identity and Access Management (IAM), create an IAM role for use
by the EMR cluster. Assign all of the Elastic Compute Cloud (EC2) nodes in
the cluster to this role. An option is to consider copying the contents of the
`default IAM roles for Amazon EMR`_ used by AWS. The command
``aws emr create-default-roles`` facilitates this task. For more information,
see `default IAM roles for Amazon EMR`_.

Also, you need to create a role named ``emr`` with the policy
``AmazonElasticMapReduceforEC2Role`` for the EC2 instance profile.

Make sure that an IAM user with administrative privileges is available for use.

=================
SSH Credentials
=================

Generate a secure SSH key that you use to access all AWS resources. For
example, run the following command.

    .. code-block:: bash

        ssh-keygen -t rsa -C "your_email@example.com"

Upload the public key from the SSH key pair to AWS and assign a key pair
name to it.

======================
Elastic Compute Cloud
======================

Ensure that at least one Amazon Elastic Compute Cloud (EC2) instance is
available to host the various services. Depending on the scale of your
deployment, additional instances might be necessary.

Make sure to use the secure key pair name to deploy all of the EC2 instances.

==============================
Relational Database Service
==============================

Deploy a MySQL 5.6 Relational Database Service (RDS) instance. This RDS
instance is the result store.

Connectivity
***************

Ensure that there is connectivity between the EC2 instance that hosts
the edX Analytics API and your RDS instance.

Also, ensure that instances deployed into the public subnet of the VPC
can connect to your RDS instance.

Users
***********

Create at least the following two users on the RDS instance.

* The "pipeline" user must have permission to create databases, tables, and
  indexes, and issue arbitrary Data Manipulation Language (DML) commands.

* The "api" user must have read-only access.

Configure passwords for both of these users.

Other Considerations
*********************

Configure the RDS instance to use "utf8_bin" collation by default for
columns in all databases and tables.

==================================
Scheduler Service
==================================

Establish an SSH connection to the EC2 instance within the VPC that will
run the scheduler service. Then, issue the following commands from a shell
running on that instance.

#. Check out the sources files from `edx-analytics-configuration`_.

    .. code-block:: bash

        git clone https://github.com/openedx/edx-analytics-configuration.git

#. Configure the shell to use the AWS credentials of the administrative AWS
   user.

    .. code-block:: bash

        export AWS_ACCESS_KEY_ID=<access key ID goes here>
        export AWS_SECRET_ACCESS_KEY=<secret access key goes here>

#. Install the `AWS Command Line Interface`_.

    .. code-block:: bash

        pip install awscli

==================================
Simple Storage Solution Buckets
==================================

Create a Simple Storage Solution (S3) bucket to hold all Hadoop logs from
the EMR cluster.

    .. code-block:: bash

        aws s3 mb s3://<your logging bucket name here>

Then, create an S3 bucket to hold secure configuration files and
initialization scripts.

    .. code-block:: bash

        aws s3 mb s3://<your configuration bucket name here>

=========================
MySQL Connector Library
=========================

Download the `MySQL connector library`_ from Oracle. After the download is
complete, you then upload it to S3.

  .. code-block:: bash

    aws s3 cp /tmp/mysql-connector-java-5.1.*.tar.gz s3://<your configuration bucket name here>/

The ``edx-analytics-configuration/batch/bootstrap/install-sqoop`` script
references a specific version of the MySQL connector library. Update this
``install-sqoop`` script to point to the correct version of the library in the
S3 bucket. You must update the script before you continue.

Then, upload the contents of the ``edx-analytics-configuration/batch/bootstrap/`` directory into your configuration bucket.

  .. code-block:: bash

    aws s3 sync edx-analytics-configuration/batch/bootstrap/ s3://<your configuration bucket name here>/

==========================
Cluster Configuration File
==========================

Create a cluster configuration file to specify the parameters for the EMR
cluster. Review the parameters that follow, and change them to specify your
desired configuration. For example, review the ``core`` and ``task`` mappings
and change the values for ``bidprice`` and ``type`` to meet your needs.

Then, save this file to a temporary location such as ``/tmp/cluster.yml``.

    .. code-block:: yaml

        {
            name: <your cluster name here>,
            keypair_name: <your keypair name here>,
            vpc_subnet_id: <your VPC public subnet ID here>,
            log_uri: "s3://<your logging bucket name here>",
            instance_groups: {
                master: {
                    num_instances: 1,
                    type: m3.xlarge,
                    market: ON_DEMAND,
                },
                core: {
                    num_instances: 2,
                    type: m3.xlarge,
                    market: SPOT,
                    bidprice: 0.8
                },
                task: {
                    num_instances: 1,
                    type: m3.xlarge,
                    market: SPOT,
                    bidprice: 0.8
                }
            },
            release_label: emr-4.7.2,
            applications: [ {name: Hadoop}, {name: Hive}, {name: Sqoop-Sandbox}, {name: Ganglia} ],
            steps: [
              {
                type: script,
                name: Install MySQL connector for Sqoop,
                step_args: [ "s3://<your-analytics-packages-bucket>/install-sqoop", "s3://<your-analytics-packages-bucket>" ],
                # You might want to set this to CANCEL_AND_WAIT while debugging step failures.
                action_on_failure: TERMINATE_JOB_FLOW
              }
            ],
            configurations: [
              {
                classification: mapred-site,
                properties:
                {
                  mapreduce.framework.name: 'yarn',
                  mapreduce.jobtracker.retiredjobs.cache.size: '50',
                  mapreduce.reduce.shuffle.input.buffer.percent: '0.20',
                }
              },
              {
                classification: yarn-site,
                properties:
                {
                  yarn.resourcemanager.max-completed-applications: '5'
                }
              }
            ],
            user_info: []
        }


You might find you need to update Hadoop instance types and container
sizes.  In particular, if you encounter jobs that are running out of
physical memory, you might want to choose a larger instance.  If your
instance is a good size but being underutilized, you might want to
explicitly define larger values in the "mapred-site" configuration
than would be provided by default in the instance size you are
using. Here is an example of settings we use with an m3.2xlarge
instance type.

    .. code-block:: yaml

              {
                classification: mapred-site,
                properties:
                {
                  mapreduce.framework.name: 'yarn',
                  mapreduce.jobtracker.retiredjobs.cache.size: '50',
                  mapreduce.reduce.shuffle.input.buffer.percent: '0.20',
                  mapreduce.map.java.opts: '-Xmx2458m',
                  mapreduce.reduce.java.opts: '-Xmx4916m',
                  mapreduce.map.memory.mb: '3072',
                  mapreduce.reduce.memory.mb: '6144'
                }
              }


============
EMR Cluster
============

Deploy the EMR cluster.

    .. code-block:: bash

        EXTRA_VARS="@/tmp/cluster.yml" make provision.emr

Example Output
***************

    ::

        pip install -q -r requirements.txt

        ansible-playbook --connection local -i 'localhost,' batch/provision.yml -e "$EXTRA_VARS"

        PLAY [Provision cluster] ******************************************************

        TASK: [provision EMR cluster] *************************************************
        changed: [localhost]

        TASK: [add master to group] ***************************************************
        ok: [localhost]

        TASK: [display master IP address] *********************************************
        ok: [localhost] => {
            "msg": "10.0.1.236"
        }

        TASK: [display job flow ID] ***************************************************
        ok: [localhost] => {
            "msg": "j-29UUJVM8P1NPY"
        }

        PLAY [Configure SSH access to cluster] ****************************************

        TASK: [user | debug var=user_info] ********************************************
        ok: [10.0.1.236] => {
            "item": "",
            "user_info": []
        }

        TASK: [user | create the edxadmin group] **************************************
        changed: [10.0.1.236]

        TASK: [user | ensure sudoers.d is read] ***************************************
        changed: [10.0.1.236]

        TASK: [user | grant full sudo access to the edxadmin group] *******************
        changed: [10.0.1.236]

        TASK: [user | create the users] ***********************************************
        skipping: [10.0.1.236]

        TASK: [user | create .ssh directory] ******************************************
        skipping: [10.0.1.236]

        TASK: [user | assign admin role to admin users] *******************************
        skipping: [10.0.1.236]

        TASK: [user | copy github key[s] to .ssh/authorized_keys] ********************
        skipping: [10.0.1.236]

        TASK: [user | create bashrc file for normal users] ****************************
        skipping: [10.0.1.236]

        TASK: [user | create .profile for all users] **********************************
        skipping: [10.0.1.236]

        TASK: [user | modify shell for restricted users] ******************************
        skipping: [10.0.1.236]

        TASK: [user | create bashrc file for restricted users] ************************
        skipping: [10.0.1.236]

        TASK: [user | create sudoers file from template] ******************************
        changed: [10.0.1.236]

        TASK: [user | change home directory ownership to root for restricted users] ***
        skipping: [10.0.1.236]

        TASK: [user | create ~/bin directory] *****************************************
        skipping: [10.0.1.236]

        TASK: [user | create allowed command links] ***********************************
        skipping: [10.0.1.236]

        PLAY RECAP ********************************************************************
        10.0.1.236                 : ok=0    changed=4    unreachable=0    failed=0
        localhost                  : ok=4    changed=1    unreachable=0    failed=0

Additional Tasks
=================

To complete the EMR configuration, additional configuration and automation
procedures are required, including scheduling jobs and automating log
duplication. For more information, see the `edX Analytics Installation`_ wiki
page.


.. include:: ../../../links/links.rst

