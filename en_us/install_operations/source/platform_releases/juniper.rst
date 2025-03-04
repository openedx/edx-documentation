.. _Open edX Juniper Release:

#########################
Open edX Juniper Release
#########################

.. warning::

    This release is unsupported.

    The `Open edX Named Releases page`_ and the `Open edX Releases Homepage`_ are the
    authoratative sources of information on all Open edX releases. It is *strongly*
    recommended to operate off the latest Open edX release at all points in time, as
    only the most recent release is community-supported.

    See the `Open edX Release Schedule`_ for information on release dates and end-of-life
    support.

This section describes how to install the Open edX Juniper release.

.. contents::
 :local:
 :depth: 1

****************************
What's Included in Juniper
****************************

The Open edX Juniper release contains several new features for learners,
course teams, and developers. For more information, see the 
`Open edX Release Notes`__.

__ https://docs.openedx.org/en/latest/community/release_notes/juniper.html


******************************
What Is the Juniper Git Tag?
******************************

A git tag identifies the version of Open edX code that is the Juniper release.
About three dozen repositories are tagged as part of an Open edX release. Many 
other repositories are installed as dependencies of those repositories. You can 
find the most up-to-date git tag for Juniper on the
`Open edX Named Releases page`_.

*******************************
Installing the Juniper Release
*******************************

You can install the Open edX Juniper release using either
`devstack`_ or the `Legacy Open edX Native Installation`_ instructions.

Juniper releases have git tag names like ``open-release/juniper.1``.
The available names are detailed on the `Open edX Named Releases page`_.

***********************************
Upgrading from the Ironwood Release
***********************************

The recommended approach to upgrading an existing installation of the Open edX
Ironwood release to the Juniper release is to make a fresh installation of the
Juniper release on a new machine, and move your data and settings to it.

To move and upgrade your Ironwood data onto a Juniper installation, follow these
steps.

#. Be sure that your Ironwood installation is on the latest commit from
   ``open-release/ironwood.master``. This ensures that your database is fully 
   migrated and ready for upgrade to Juniper.

#. Stop all services on the Ironwood machine.

#. Dump the data on the Ironwood machine. Here's an example script that will dump
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

#. Copy the ``.tgz`` data file to the Juniper machine.

#. Stop all services on the Juniper machine.

#. Restore the Ironwood data into the Juniper machine. As an example, you might
   use the following commands.

    .. code-block:: bash

        $ tar -xvf openedx-data-20200411T154750.tgz
        $ mysql -uroot -p < mysql-data-20200411T154750.sql
        $ mongorestore -u admin -p -h localhost --authenticationDatabase admin --drop -d edxapp mongo-dump-20200411T154750/edxapp
        $ mongorestore -u admin -p -h localhost --authenticationDatabase admin --drop -d cs_comment_service mongo-dump-20200411T154750/cs_comment_service_development

#. Run the Juniper migrations, which will update your Ironwood data to be
   valid for Juniper:

    .. code-block:: bash

        $ /edx/app/edx_ansible/edx_ansible/util/install/native.sh --tags migrate

#. Copy your configuration files from the Ironwood machine to the Juniper machine.

#. Restart all services.

******************************************
Upgrading to a Subsequent Juniper Release
******************************************

Occasionally, we release updates to Juniper.  For example, the second
release of Juniper will be ``open-release/juniper.2``.
The steps to upgrade differ based on your original installation method.

================================
Upgrading a Docker Installation
================================

Devstack is installed using Docker. To upgrade from one Juniper
release to another, follow the instructions in `devstack`_.

===============================
Upgrading a Native Installation
===============================

If you installed Open edX using the `Legacy Open edX Native Installation`_, you can
upgrade from one Juniper release to another by re-running those steps using
your desired Juniper tag as the new value for ``OPENEDX_RELEASE``.


.. include:: ../../../links/links.rst
