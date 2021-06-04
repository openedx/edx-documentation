.. _Open edX Ironwood Release:

#########################
Open edX Ironwood Release
#########################

This section describes how to install the Open edX Ironwood release.

.. contents::
 :local:
 :depth: 1

****************************
What's Included in Ironwood
****************************

The Open edX Ironwood release contains several new features for learners,
course teams, and developers. For more information, see the 
`Open edX Release Notes`__.

__ http://edx.readthedocs.io/projects/open-edx-release-notes/en/latest/ironwoood.html


******************************
What Is the Ironwood Git Tag?
******************************

A git tag identifies the version of Open edX code that is the Ironwood release.
About two dozen repositories are tagged as part of an Open edX release. Many 
other repositories are installed as dependencies of those repositories. You can 
find the most up-to-date git tag for Ironwood on the
`Open edX Named Releases page`_.

*******************************
Installing the Ironwood Release
*******************************

You can install the Open edX Ironwood release using either 
`devstack`_ or the `Legacy Open edX 
Native Installation`_ instructions.

Ironwood releases have git tag names like ``open-release/ironwood.1``.
The available names are detailed on the `Open edX Named Releases page`_.

.. _upgrade_hawthorn:

***********************************
Upgrading from the Hawthorn Release
***********************************

The recommended approach to upgrading an existing installation of the Open edX
Hawthorn release to the Ironwood release is to make a fresh installation of the
Ironwood release on a new machine, and move your data and settings to it.

To move and upgrade your Hawthorn data onto a Ironwood installation, follow these
steps.

#. Be sure that your Hawthorn installation is on the latest 
   ``open-release/hawthorn.master``. This ensures that your database is fully 
   migrated and ready for upgrade to Ironwood.

#. Stop all services on the Hawthorn machine.

#. Dump the data on the Hawthorn machine. Here's an example script that will dump
   the MySQL and Mongo databases into a single ``.tgz`` file.  The script will
   prompt for the MySQL and Mongo passwords as needed.

    .. code-block:: bash

        #!/bin/bash
        MYSQL_CONN="-uroot -p"
        echo "Reading MySQL database names..."
        mysql ${MYSQL_CONN} -ANe "SELECT schema_name FROM information_schema.schemata WHERE schema_name NOT IN ('mysql','information_schema','performance_schema', 'sys')" > /tmp/db.txt
        DBS="--databases $(cat /tmp/db.txt)"
        NOW="$(date +%Y%m%dT%H%M%S)"
        SQL_FILE="mysql-data-${NOW}.sql"
        echo "Dumping MySQL structures..."
        mysqldump ${MYSQL_CONN} --add-drop-database --skip-add-drop-table --no-data ${DBS} > ${SQL_FILE}
        echo "Dumping MySQL data..."
        # If there is table data you don't need, add --ignore-table=tablename
        mysqldump ${MYSQL_CONN} --no-create-info ${DBS} >> ${SQL_FILE}

        for db in edxapp cs_comments_service; do
            echo "Dumping Mongo db ${db}..."
            mongodump -u admin -p -h localhost --authenticationDatabase admin -d ${db} --out mongo-dump-${NOW}
        done

        tar -czf openedx-data-${NOW}.tgz ${SQL_FILE} mongo-dump-${NOW}

#. Copy the ``.tgz`` data file to the Ironwood machine.

#. Stop all services on the Ironwood machine.

#. Restore the Hawthorn data into the Ironwood machine. As an example, you might
   use the following commands.

    .. code-block:: bash

        $ tar -xvf openedx-data-20170811T154750.tgz
        $ mysql -uroot -p < mysql-data-20170811T154750.sql
        $ mongorestore -u admin -p -h localhost --authenticationDatabase admin --drop -d edxapp mongo-dump-20170811T154750/edxapp
        $ mongorestore -u admin -p -h localhost --authenticationDatabase admin --drop -d cs_comment_service mongo-dump-20170811T154750/cs_comment_service_development

#. To migrate data from Hawthorn to Ironwood, you need to drop the database
   tables used by djcelery. These tables should be empty in your Hawthorn data,
   so it is safe to drop them. The edx-platform application has a management
   command to check that they are empty and drop them:

    .. code-block:: bash

        $ sudo su - -s /bin/bash edxapp
        edxapp@xyz:~$ . edxapp_env
        edxapp@xyz:~$ cd edx-platform/
        edxapp@xyz:~/edx-platform$ python manage.py lms drop_djcelery_tables --settings=aws

#. Run the Ironwood migrations, which will update your Hawthorn data to be
   valid for Ironwood:

    .. code-block:: bash

        $ /edx/app/edx_ansible/edx_ansible/util/install/native.sh --tags migrate

#. Copy your configuration files from the Hawthorn machine to the Ironwood
    machine.

#. Restart all services.

******************************************
Upgrading to a Subsequent Ironwood Release
******************************************

Occasionally, we release updates to Ironwood.  For example, the second
release of Ironwood will be ``open-release/ironwood.2``.
The steps to upgrade differ based on your original installation method.

================================
Upgrading a Docker Installation
================================

Devstack is installed using Docker. To upgrade from one Ironwood
release to another, follow the instructions in `devstack`_.

===============================
Upgrading a Native Installation
===============================

If you installed Open edX using the `Legacy Open edX Native Installation`_, you can
upgrade from one Ironwood release to another by re-running those steps using
your desired Ironwood tag as the new value for ``OPENEDX_RELEASE``.


.. include:: ../../../links/links.rst
