.. _CSMHE Procedures:

############################################################
Procedures for Replacing ``courseware_studentmodulehistory``
############################################################

This topic provides procedures for updating to the new database and table
configuration required by the ``courseware_studentmodulehistory`` change. It
also includes the optional procedure for migrating all data from
``courseware_studentmodulehistory`` to
``coursewarehistoryextended_studentmodulehistoryextended``.

.. contents::
   :local:
   :depth: 1

Before you follow these procedures for your Open edX instance, be sure to
review the different :ref:`options<Options for Updating Your Open edX
Instances>` for updating ``courseware_studentmodulehistory``.

*************************************
Step 1: Create the Database
*************************************

.. contents::
   :local:
   :depth: 2

========================================
Options for Creating the Database
========================================

For all fullstack and production instances that follow master, you must create
a MySQL database and set users up. To do so, you can use one of
these options.

* Use the `create_db_and_users.yml playbook`_ to create the database and user
  automatically. For more information, see :ref:`Use the Playbook to Create the
  Database`.

* Create the database and users manually. If you select this option, you must
  also complete other configuration steps manually. For more information, see
  :ref:`Create the Database Manually`.

.. note:: You must follow one of these procedures for all of your fullstack
  and production instances.

.. _Use the Playbook to Create the Database:

Use the Playbook to Create the Database
****************************************

Follow the `create_db_and_users.yml playbook`_ to create the ``edxapp_csmh``
database and its users automatically.

You then choose an option for :ref:`configuring<Options for Configuring the
Database>` the ``edxapp_csmh`` database.

.. _Create the Database Manually:

Create the Database Manually
*******************************

Create the MySQL database. For the edx.org and edX Edge instances, edX named
this database ``edxapp_csmh``.

Modify the following example command for your database users and naming
schemes.

.. code-block:: sql

     mysql> create database edxapp_csmh DEFAULT CHARACTER SET utf8;
     mysql> grant SELECT,INSERT,UPDATE,DELETE on edxapp_csmh.* to 'edxapp001@hosts'
     mysql> grant SELECT,INSERT,UPDATE,DELETE,ALTER,CREATE,DROP,INDEX on edxapp_csmh.* to 'migrate@hosts'

You then choose an option for :ref:`configuring<Options for Configuring the
Database>` your new database.

*************************************
Step 2: Configure the Database
*************************************

.. contents::
   :local:
   :depth: 2

.. _Options for Configuring the Database:

=====================================
Options for Configuring the Database
=====================================

After you create the MySQL database and set users up, you update
``lms.yml`` to add configuration settings to the DATABASES section. To do
so, you can use one of these options.

* Use the `edxapp.yml playbook`_ to update your edxapp instances. If you
  choose to use this playbook, then master after 5 May 2016 will update
  ``lms.yml`` to set ``edxapp_databases`` in the DATABASES section for
  you.

  The playbook requires ``EDXAPP_MYSQL_CSMH_DB_NAME``,
  ``EDXAPP_MYSQL_CSMH_USER``, ``EDXAPP_MYSQL_CSMH_PASSWORD``,
  ``EDXAPP_MYSQL_CSMH_HOST``, ``EDXAPP_MYSQL_CSMH_PORT`` to be populated in the
  same way that the ``EDXAPP_MYSQL_...`` variables are populated in your
  Ansible overrides.

* Update the DATABASES section in ``lms.yml`` manually. If you create the
  MySQL database yourself, you must use this option. For more information, see
  :ref:`Update DATABASES Manually`.

.. _Update DATABASES Manually:

Update DATABASES Manually
**************************

If you create the MySQL database yourself, you configure the database by adding
a clause to the ``lms.yml`` file.

#. Open the ``edx/app/edxapp/lms.yml`` file in your text editor.

#. In the DATABASES section, add configuration details for your new database.
   An example follows.

   .. code-block:: bash

     "student_module_history": {
            "ENGINE": "django.db.backends.mysql",
            "HOST": "localhost",
            "NAME": "edxapp_csmh",
            "PASSWORD": "password",
            "PORT": "3306",
            "USER": "edxapp001"
        },

*****************************************
Step 3: Enable Writes to the New Table
*****************************************

Edit the ``lms.yml`` file to set the ``ENABLE_CSMH_EXTENDED`` feature
flag.

   .. code-block:: bash

    ``"ENABLE_CSMH_EXTENDED": true``

Alternatively, you can use your current Ansible overrides for updating feature
flags to make this change.

*************************************
Step 4: Create the Table
*************************************

.. contents::
   :local:
   :depth: 2

.. _Options for Creating the Table:

=====================================
Options for Creating the Table
=====================================

After you create and configure the MySQL database and enable the new table, you
create the new table. To do so, you can use one of these options.

* Run Django migrations to create the
  ``coursewarehistoryextended_studentmodulehistoryextended`` table. The
  `edxapp.yml playbook`_ uses these scripts to run migrations.
  * ``/edx/bin/edxapp-migrate-lms``
  * ``/edx/bin/edxapp-migrate-cms``

* Run migrations manually. For more information, see :ref:`Run Migrations
  Manually`.

After you bring your servers back online with this configuration, the system
only writes records for interactions with CAPA problems to the
``coursewarehistoryextended_studentmodulehistoryextended`` table.

.. _Run Migrations Manually:

Run Migrations Manually
**************************

A summary of the manual steps for running migrations follows.

#. Run cms migrations against the default database.
#. Run lms migrations against the default database.
#. Run cms migrations against the ``student_module_history`` database.
#. Run lms migrations against the ``student_module_history`` database.

If you choose to run migrations manually, refer to the last few lines of the
``/edx/bin/edxapp-migrate-lms`` and ``/edx/bin/edxapp-migrate-cms`` scripts
for the commands that you must run.


*************************************************************
Optional Step 5: Migrate All Data to the New Table
*************************************************************

After you complete all of the deployment steps (1-4) described above, you have
the option to migrate all data from ``courseware_studentmodulehistory`` to
``coursewarehistoryextended_studentmodulehistoryextended``. For more
information about this optional procedure, see :ref:`Migrate All Data to One
Table`.

.. contents::
   :local:
   :depth: 2

.. note:: This procedure is suitable only for large production instances that
 require the operational benefits described in the :ref:`Why Is A New Database
 Needed` topic.

.. _Script Options for Migrating Data:

=====================================
Script Options for Migrating Data
=====================================

EdX provides the following `migration scripts`_. You select the one that
applies to your database architecture.

*  ``migrate-separate-database-instances.sh`` applies to installations that
   set up the new database on a different database server than the default
   database.

* ``migrate-same-database-instance.sh`` applies to installations that set up
  the new database on the same database server as the default database.

  Implementing this database architecture is simpler than setting up a separate
  database server, but it offers different operational benefits.

Both options require your installation to be running a deploy of Open edX that
writes only to ``coursewarehistoryextended_studentmodulehistoryextended``. You
can :ref:`restart<Restart a Migration>` either of the migrations if necessary.

Run the Script for Separate Database Servers
*********************************************

EdX selected the database architecture with separate database servers, and
implemented it by creating a read replica and then severing it from production.
This process ensures that you have a mostly up to date
``courseware_studentmodulehistory`` table, which is then copied to
``coursewarehistoryextended_studentmodulehistoryextended``.

#. Do a final mysqldump from the first (default) database server to the second
   (new) database server.

   .. code-block:: bash

     mysqldump --skip-add-drop-table --no-create-info -u migrate -p -h dbhost db courseware_studentmodulehistory --where='id > LAST_ID' --result-file=catchup.sql

   Allow the mysqldump to run to completion, so that
   ``courseware_studentmodulehistory`` is caught up.

#. Run ``migrate-separate-database-instances.sh`` to copy data slowly.

   .. code-block:: bash

     mysql -u migrate -p -h newdbhost db2 < catchup.sql

   Be sure to monitor your progress to ensure that the process runs slowly, and
   does not cause disk contention or other performance issues on the new
   database instance.

Run the Script for A Single Database Server
*******************************************

Run ``migrate-same-database-instance.sh``.

.. _Restart a Migration:

======================
Restart a Migration
======================

If you need to restart either migration, you can use the following command to
find the largest ID value that was successfully inserted into the new table.

.. code-block:: bash

   select max(id) from wwc.courseware_studentmodulehistory where id < MAXID

You can then rerun with MINID set to the result of this query.

====================================
Disable Reads from the Old Table
====================================

Edit the ``lms.yml`` file to set the
``ENABLE_READING_FROM_MULTIPLE_HISTORY_TABLES`` feature flag.

   .. code-block:: bash

    "ENABLE_READING_FROM_MULTIPLE_HISTORY_TABLES": false

After you bring your servers back online with this configuration, the system
only writes to and queries from the
``coursewarehistoryextended_studentmodulehistoryextended`` table.

====================================
Truncate the Old Table
====================================

Select one of the available MySQL techniques for slowly draining the
``courseware_studentmodulehistory`` table.

* The preferred technique for installations with small or moderately sized
  databases is the ``TRUNCATE TABLE courseware_studentmodulehistory`` command.
  However, this command can cause a lot of disk activity.

* If your table is very large, you can choose to use the ``slow-delete.sh``
  script instead. EdX prepared and used this script to truncate
  ``courseware_studentmodulehistory``.



.. _migration scripts: https://github.com/openedx/configuration/blob/master/util/csmh-extended

.. _edxapp.yml playbook: https://github.com/openedx/configuration/blob/master/playbooks/edx-east/edxapp.yml

.. _create_db_and_users.yml playbook:   https://github.com/openedx/configuration/blob/master/playbooks/edx-east/create_db_and_users.yml
