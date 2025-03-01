.. _Open edX Hawthorn Release:

#########################
Open edX Hawthorn Release
#########################

.. warning::

    This release is unsupported.

    The `Open edX Named Releases page`_ and the `Open edX Releases Homepage`_ are the
    authoratative sources of information on all Open edX releases. It is *strongly*
    recommended to operate off the latest Open edX release at all points in time, as
    only the most recent release is community-supported.

    See the `Open edX Release Schedule`_ for information on release dates and end-of-life
    support.

This section describes how to install the Open edX Hawthorn release.

.. contents::
 :local:
 :depth: 1

****************************
What's Included in Hawthorn
****************************

The Open edX Hawthorn release contains several new features for learners,
course teams, and developers. For more information, see the 
`Open edX Release Notes`__.

__ https://docs.openedx.org/en/latest/community/release_notes/hawthorn.html

=======================
User Retirement Feature
=======================

The Hawthorn release also includes the new user retirement feature, which is a 
set of APIs and tooling that enables Open edX instances to retire registered 
users. There have been many changes to privacy laws (for example, GDPR or the 
European Union General Data Protection Regulation) intended to change the way 
that businesses think about and handle Personally Identifiable Information 
(PII) data. The user retirement feature is a step toward enabling Open edX to 
support some of the key updates in privacy laws. For more information, see 
`retirement`_.

******************************
What Is the Hawthorn Git Tag?
******************************

A git tag identifies the version of Open edX code that is the Hawthorn release.
About two dozen repositories are tagged as part of an Open edX release. Many 
other repositories are installed as dependencies of those repositories. You can 
find the most up-to-date git tag for Hawthorn on the
`Open edX Named Releases page`_.

*******************************
Installing the Hawthorn Release
*******************************

You can install the Open edX Hawthorn release using either 
`devstack`_ or the `Legacy Open edX 
Native Installation`_ instructions.

Hawthorn releases have git tag names like ``open-release/hawthorn.1``.
The available names are detailed on the `Open edX Named Releases page`_.

.. _upgrade_ginkgo:

**********************************
Upgrading from the Ginkgo Release
**********************************

The recommended approach to upgrading an existing installation of the Open edX
Ginkgo release to the Hawthorn release is to make a fresh installation of the
Hawthorn release on a new machine, and move your data and settings to it.

To move and upgrade your Ginkgo data onto a Hawthorn installation, follow these
steps.

#. Be sure that your Ginkgo installation is on the latest 
   ``open-release/ginkgo.master``. This ensures that your database is fully 
   migrated and ready for upgrade to Hawthorn.

#. Stop all services on the Ginkgo machine.

#. Dump the data on the Ginkgo machine. Here's an example script that will dump
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

#. Copy the ``.tgz`` data file to the Hawthorn machine.

#. Stop all services on the Hawthorn machine.

#. Restore the Ginkgo data into the Hawthorn machine. As an example, you might
   use the following commands.

    .. code-block:: bash

        $ tar -xvf openedx-data-20170811T154750.tgz
        $ mysql -uroot -p < mysql-data-20170811T154750.sql
        $ mongorestore -u admin -p -h localhost --authenticationDatabase admin --drop -d edxapp mongo-dump-20170811T154750/edxapp
        $ mongorestore -u admin -p -h localhost --authenticationDatabase admin --drop -d cs_comment_service mongo-dump-20170811T154750/cs_comment_service_development

#. To migrate data from Ginkgo to Hawthorn, you need to drop the database
   tables used by djcelery. These tables should be empty in your Ginkgo data,
   so it is safe to drop them. The edx-platform application has a management
   command to check that they are empty and drop them:

    .. code-block:: bash

        $ sudo su - -s /bin/bash edxapp
        edxapp@xyz:~$ . edxapp_env
        edxapp@xyz:~$ cd edx-platform/
        edxapp@xyz:~/edx-platform$ python manage.py lms drop_djcelery_tables --settings=aws

#. Run the Hawthorn migrations, which will update your Ginkgo data to be
   valid for Hawthorn:

    .. code-block:: bash

        $ /edx/app/edx_ansible/edx_ansible/util/install/native.sh --tags migrate

#. Copy your configuration files from the Ginkgo machine to the Hawthorn
    machine.

#. Restart all services.


******************************************
Upgrading to a Subsequent Hawthorn Release
******************************************

Occasionally, we release updates to Hawthorn.  For example, the second
release of Hawthorn will be ``open-release/hawthorn.2``.
The steps to upgrade differ based on your original installation method.

================================
Upgrading a Docker Installation
================================

Devstack is installed using Docker. To upgrade from one Hawthorn
release to another, follow the instructions in `devstack`_.

===============================
Upgrading a Native Installation
===============================

If you installed Open edX using the `Legacy Open edX Native Installation`_, you can
upgrade from one Hawthorn release to another by re-running those steps using
your desired Hawthorn tag as the new value for ``OPENEDX_RELEASE``.


.. include:: ../../../links/links.rst
