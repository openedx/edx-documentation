.. _CSMHE Procedures:

############################################################
Procedures for Updating ``courseware_studentmodulehistory``
############################################################

This topic provides procedures for updating to the new database and table
configuration required by the ``courseware_studentmodulehistory`` change. It
also includes the optional procedure for for migrating all data from
``courseware_studentmodulehistory`` to
``courseware_studentmodulehistoryextended``.

.. contents::
   :local:
   :depth: 1

Before you follow these procedures for your Open edX instance, be sure to
review the different :ref:`options for updating
``courseware_studentmodulehistory``<Options for Updating Your Open edX
Instances>`.

***************************************
Configure the New Database and Table
***************************************

.. note:: This procedure applies to all Fullstack and production instances.

#. Create a mysql database. For the edx.org and edX Edge instances, edX named
   this database ``edxapp_csmh``.

   .. code-block:: bash

     $ mysql -uroot
     mysql> create database  edxapp_csmh DEFAULT CHARACTER SET utf8
     mysql> grant edxapp migrate permissions

   Alternatively, you can use an `ansible playbook`_ to create a database and
   users.

#. Edit the ``lms.auth.json`` file to add the new database. In the DATABASES
   section of this file, add the following configuration information.

   .. code-block:: bash

     "student_module_history": {
            "ENGINE": "django.db.backends.mysql",
            "HOST": "localhost",
            "NAME": "edxapp_csmh",
            "PASSWORD": "password",
            "PORT": "3306",
            "USER": "edxapp001"
        },


#. Edit the ``lms.env.json`` file to set the ``ENABLE_CSMH_EXTENDED`` feature
   flag.

   .. code-block:: bash

    ``"ENABLE_CSMH_EXTENDED": true``

When you bring your servers back online with this configuration, the system
only writes records for interactions with problems to
``courseware_studentmodulehistoryextended``.

Optionally, you can now migrate all data from
``courseware_studentmodulehistory`` to
``courseware_studentmodulehistoryextended``.

*************************************************************
Migrate Data to ``courseware_studentmodulehistoryextended``
*************************************************************

.. note:: This procedure is most likely to apply to large production instances.

#. Edit the ``edxapp/defaults/main.yml`` file to add the new database. In the
   edxapp_databases section of this file, add the following configuration
   information.

   .. code-block:: bash

     STUDENT_MODULE_HISTORY:
       EDXAPP_MYSQL_CSMH_DB_NAME: "{{ EDXAPP_MYSQL_DB_NAME }}"
       EDXAPP_MYSQL_CSMH_USER: "{{ EDXAPP_MYSQL_USER }}"
       EDXAPP_MYSQL_CSMH_PASSWORD: "{{ EDXAPP_MYSQL_PASSWORD }}"
       EDXAPP_MYSQL_CSMH_HOST: "{{ EDXAPP_MYSQL_DB_HOST }}"
       EDXAPP_MYSQL_CSMH_PORT: "{{ EDXAPP_MYSQL_PORT }}"

#. Run the migration script.

   .. code-block:: bash

     $ ./manage.py lms migrate --database=student_module_history --settings=devstack

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

#. If you need to restart the migration, you can use the following command to
   find the largest ID value that was successfully inserted into the new table.

   .. code-block:: bash

     select max(id) from wwc.courseware_studentmodulehistory where id < MAXID

   You can then rerun with i > 0.

#. Edit the ``lms.env.json`` file to set the
   ``ENABLE_READING_FROM_MULTIPLE_HISTORY_TABLES`` feature flag.

   .. code-block:: bash

    ``"ENABLE_READING_FROM_MULTIPLE_HISTORY_TABLES": false``

When you bring your servers back online with this configuration, the system
only writes to and queries ``courseware_studentmodulehistoryextended``.



.. _ansible playbook:  https://github.com/edx/configuration/blob/master/playbooks/edx-east/create_db_and_users.yml
