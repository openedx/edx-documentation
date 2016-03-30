.. _CSMHE Migration Procedures:

##############################################
Procedures for Migrating Open edX Instances
##############################################


.. contents::
   :local:
   :depth: 1



****************
Migrate Devstack
****************

To migrate a devstack that is used for development and that has a small
database, you replace your devstack with an up to date devstack.

   .. code-block:: bash

     vagrant provision

This procedure adds a devstack with the new ``edxapp_csmh`` database and its
``courseware_studentmodulehistoryextended`` table. The feature flags relevant
to the migration have the following settings.

``ENABLE_CSMH_EXTENDED``: true
``READ_ONLY_FROM_CSMHE``: false

After you provision the new devstack instance, no further migration or
configuration procedures are required. With these settings, the system writes
only to the new ``courseware_studentmodulehistoryextended`` table, but it reads
from both the new table and the ``courseware_studentmodulehistory`` table in
the ``edxapp`` database.

Due to the performance overhead of doing lookups in two databases, this option
is most suitable for development environments with small databases.

For more information, see TBD

****************************************************
Migrate Fullstack or a Small Production Installation
****************************************************



******************************************
Migrate a Large Production Installation
******************************************



Create the ``edxapp_csmh`` Database



Verify the Starting ID Offset



Run the migration


Deploy edxapp with ENABLE_CSMH_EXTENDED = True



Configuration





.. _Migrating CSMH:

########################################################
Migrating the ``courseware_studentmodulehistory`` Table
########################################################

This section describes a change to the ``courseware_studentmodulehistory``
database table that requires a new database configuration and a migration.
These changes took place for the edx.org and edX Edge sites during the first
two weeks of March 2016.

.. important::  All Open edX installations that use **the latest version**
  available on the master branch of the edx-platform repository, including
  devstack installations, must also perform these changes.

.. contents::
   :local:
   :depth: 1

.. note:: No changes are required or supported at this time for Open edX
  installations that use the **Dogwood release**. The changes needed for the
  ``courseware_studentmodulehistory`` table will be required during the upgrade
  to the Open edX Eucalyptus release.

****************************
Why Is a Migration Needed?
****************************

The ``courseware_studentmodulehistory`` database table contains a record for
each attempt that learners make to answer ``problem`` type XBlocks correctly.
This database table is a standard ``StudentModuleHistory`` Django model. It has
an ``id`` column with a type of 32-bit signed integer, and therefore has a
maximum capacity of 2,147,483,647 records.

Typically, ``courseware_studentmodulehistory`` is the largest table in the
database. On the edx.org site, 20,000 to 80,000 records are written to this
table every hour. A migration to replace the current form of the
``courseware_studentmodulehistory`` table with a higher capacity form is
required to assure that no data is lost for the edx.org site.

A new database table, ``courseware_studentmodulehistoryextended``, replaces the
``courseware_studentmodulehistory`` table. The
``courseware_studentmodulehistoryextended`` table uses a custom Django field
type to give the ``id`` column a type of 64-bit unsigned integer, which offers
an exponentially larger storage capacity.

********************************
Database Configuration Strategy
********************************

Due to the number of records involved, the edX DevOps team estimated a duration
of several days for the migration of the edx.org
``courseware_studentmodulehistory`` table. Downtime of that duration for the
edx.org site is not acceptable, so the team developed a two-part strategy for
this procedure.

.. contents::
   :local:
   :depth: 1

=============================
Creating a Separate Database
=============================

To avoid site downtime, you create the
``courseware_studentmodulehistoryextended`` table in a separate database
named ``student_module_history``. The software available on the master branch
of the edx-platform repository as of 16 March 2016 writes records to this
database and table.

=======================
Migrating Table Data
=======================

To migrate the data from the original table to the extended table, you enable a
feature flag, ``ENABLE_CSMH_EXTENDED``. This change starts the migration
script.

To avoid data loss during the migration, the system reads the records in both
the original table in the default database and the extended table in the
``student_module_history`` database.

When the migration is complete, you enable another feature flag,
``READ_ONLY_FROM_CSMHE``, so that new records are written only to the extended
table. In addition, the script iterates back to migrate any records written to
the original table after the script started to the extended table.

.. ^ really not sure of this section even as a general overview

==========================
Post-Migration Options
==========================

After the data migration is complete, you have several options.

* You can configure your system to read only from the new
  ``courseware_studentmodulehistoryextended`` table, and then truncate the old
  table. This option is suitable for installations that have a large number of
  records in the ``courseware_studentmodulehistoryextended`` table.

* You can leave both tables in place, and allow the system to continue to read
  from both tables. Due to the overhead of doing lookups in two databases, this
  option is only suitable for development environments with small databases.










**************************************************************
Create the ``courseware_studentmodulehistoryextended`` Table
**************************************************************

#. Create a database named ``student_module_history``.

#. Define new databases hash.

   .. code-block:: bash

       STUDENT_MODULE_HISTORY:

       EDXAPP_MYSQL_CSMH_DB_NAME: "{{ EDXAPP_MYSQL_DB_NAME }}"
       EDXAPP_MYSQL_CSMH_USER: "{{ EDXAPP_MYSQL_USER }}"
       EDXAPP_MYSQL_CSMH_PASSWORD: "{{ EDXAPP_MYSQL_PASSWORD }}"
       EDXAPP_MYSQL_CSMH_HOST: "{{ EDXAPP_MYSQL_DB_HOST }}"
       EDXAPP_MYSQL_CSMH_PORT: "{{ EDXAPP_MYSQL_PORT }}"

.. not sure I got this right.

#. Sign in to the Django administration console for your base URL. For example,
   ``http://{your_URL}/admin``.

#. In the **TBD** section, next to **DATABASES** select **Add**.

#. In the **TBD** field, enter "student_module_history".

  .. with or without the quotes?

#. Use South migrations to create the
   ``courseware_studentmodulehistoryextended`` table in the
   ``student_module_history`` database.

   .. didn't we get rid of South migrations in the Django framework upgrade?

#. Installations that have a large number of records, such as the edx.org site,
   can optionally drop all of the tables created in the
   ``student_module_history`` database with the exception of the new
   ``courseware_studentmodulehistoryextended`` table.

*****************
Migrate Data
*****************

#. Set ``ENABLE_CSMH_EXTENDED: true``

   .. where?

#. Save the file.

   The migration script begins to copy records from the original table in the
   default database and insert them into the new
   ``courseware_studentmodulehistoryextended`` table in the
   ``student_module_history`` database.

#.


   .. code-block:: bash

      mysqldump --skip-add-drop-table --no-create-info -u migrate -p -h rdshost.us-east-1.rds.amazonaws.com wwc courseware_studentmodulehistory --where='id > LAST_ID' --result-file=catchup.sql



   .. code-block:: bash

     MINID=2460000
     MAXID=1003426362
     STEP=10000
     MIGRATE_USER=migrate
     PASSWORD='migrate-password-from-settings'
     HOST='loadtest-edx-csmh.ciqreuddjk02.us-east-1.rds.amazonaws.com'


     for ((i=$MINID-1; i<=$MAXID; i+=$STEP)); do
     echo -n "$i";
     mysql -u $MIGRATE_USER -p$PASSWORD -h $HOST wwc <<EOF
     INSERT INTO wwc.coursewarehistoryextended_studentmodulehistoryextended (id, version, created, state, grade, max_grade, student_module_id)
       SELECT id, version, created, state, grade, max_grade, student_module_id
       FROM wwc.courseware_studentmodulehistory
       WHERE id BETWEEN $i AND $(($i+$STEP-1));
     EOF
     echo '.';
     sleep 2;
     done


  .. code-block:: bash

    MAXID=
    STEP=20000
    MIGRATE_USER=
    PASSWORD=
    HOST=


    for ((i=0; i<=$MAXID; i+=$STEP)); do
    mysql -u $MIGRATE_USER -p$PASSWORD -h $HOST wwc <<EOF
    INSERT INTO edxapp_csmh.coursewarehistoryextended_studentmodulehistoryextended (id, version, created, state, grade, max_grade, student_module_id)
      SELECT id, version, created, state, grade, max_grade, student_module_id
      FROM wwc.courseware_studentmodulehistory
      WHERE id BETWEEN $i AND $(($i+$STEP-1));
    EOF
    sleep 2
    done


#. If you need to restart, use the following command to find the largest ID value that was successfully inserted.

   .. code-block:: bash

     select max(id) from wwc.courseware_studentmodulehistory where id < MAXID

  Then re-run with i > 0.

  This gets you the largest id that successfully inserted if you need to restart


.. include:: ../../links/links.rst








As of a certain date, you will need to know how master is set up so that if you are following master, you can make the changes you need to to enable the feature flag.

As of that date, people with devstacks will need to provision a new devstack.




Devstack: vagrant provision and that's it





1. create database ``edxapp_csmh``

   #. Create a mysql database named WHATEVER YOU WANT. EdX uses edxapp_csmh.
   #. $ mysql -uroot
   #. mysql> create database  ``edxapp_csmh`` DEFAULT CHARACTER SET utf8
   #. mysql> grant edxapp migrate permissions

   Alternatively, you can use an ansible playbook: https://github.com/edx/configuration/blob/master/playbooks/edx-east/create_db_and_users.yml

2. tell Django by updating ``lms.auth.json``
  #. in the DATABASES section, add

     "student_module_history": {
            "ENGINE": "django.db.backends.mysql",
            "HOST": "localhost",
            "NAME": "edxapp_csmh",
            "PASSWORD": "password",
            "PORT": "3306",
            "USER": "edxapp001"
        },

3. feature flag on: in lms.env.json (or however you normally turn it on) "ENABLE_CSHM_EXTENDED": TRUE


- allows the migration to run
- when you bring the servers back on with this flag on, interactions write to the new db and table


   # edit https://github.com/edx/configuration/blob/master/playbooks/roles/edxapp/defaults/main.yml#L635

   under edxapp_databases, add lines for

       STUDENT_MODULE_HISTORY:

       EDXAPP_MYSQL_CSMH_DB_NAME: "{{ EDXAPP_MYSQL_DB_NAME }}"
       EDXAPP_MYSQL_CSMH_USER: "{{ EDXAPP_MYSQL_USER }}"
       EDXAPP_MYSQL_CSMH_PASSWORD: "{{ EDXAPP_MYSQL_PASSWORD }}"
       EDXAPP_MYSQL_CSMH_HOST: "{{ EDXAPP_MYSQL_DB_HOST }}"
       EDXAPP_MYSQL_CSMH_PORT: "{{ EDXAPP_MYSQL_PORT }}"


   $ ./manage.py lms migrate --database=student_module_history --settings=devstack


4. migrate



   .. code-block:: bash

     MINID=2460000
     MAXID=1003426362
     STEP=10000
     MIGRATE_USER=migrate
     PASSWORD='migrate-password-from-settings'
     HOST='loadtest-edx-csmh.ciqreuddjk02.us-east-1.rds.amazonaws.com'


     for ((i=$MINID-1; i<=$MAXID; i+=$STEP)); do
     echo -n "$i";
     mysql -u $MIGRATE_USER -p$PASSWORD -h $HOST wwc <<EOF
     INSERT INTO wwc.coursewarehistoryextended_studentmodulehistoryextended (id, version, created, state, grade, max_grade, student_module_id)
       SELECT id, version, created, state, grade, max_grade, student_module_id
       FROM wwc.courseware_studentmodulehistory
       WHERE id BETWEEN $i AND $(($i+$STEP-1));
     EOF
     echo '.';
     sleep 2;
     done



#. If you need to restart, use the following command to find the largest ID value that was successfully inserted.

   .. code-block:: bash

     select max(id) from wwc.courseware_studentmodulehistory where id < MAXID


  This gets you the largest id that successfully inserted if you need to restart

  Then re-run with i > 0.





System is now fine. Data remains in both places, query is to both tables


ENABLE_READING_FROM_MULTIPLE_HISTORY_TABLES defaults to true, you have the optio to turn it to false when your migration is over.








