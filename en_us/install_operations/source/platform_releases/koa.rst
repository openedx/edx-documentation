.. _Open edX Koa Release:

####################
Open edX Koa Release
####################

.. warning::

    This release is unsupported.

    The `Open edX Named Releases page`_ and the `Open edX Releases Homepage`_ are the
    authoratative sources of information on all Open edX releases. It is *strongly*
    recommended to operate off the latest Open edX release at all points in time, as
    only the most recent release is community-supported.

    See the `Open edX Release Schedule`_ for information on release dates and end-of-life
    support.

This section describes how to install the Open edX Koa release.

.. contents::
 :local:
 :depth: 1

**********************
What's Included in Koa
**********************

The Open edX Koa release contains several new features for learners,
course teams, and developers. For more information, see the 
`Open edX Platform Release Notes`__.

__ https://docs.openedx.org/en/latest/community/release_notes/koa.html


************************
What Is the Koa Git Tag?
************************

A git tag identifies the version of Open edX code that is the Koa release.
About three dozen repositories are tagged as part of an Open edX release. Many 
other repositories are installed as dependencies of those repositories. You can 
find the most up-to-date git tag for Koa on the
`Open edX Named Releases page`_.

**************************
Installing the Koa Release
**************************

.. warning::

    This release is unsupported.

See `Tutor installation instructions <https://docs.tutor.edly.io/gettingstarted.html>`_.

You can install the Open edX Koa release using either
`devstack`_ or the Open edX Native Installation.

Koa releases have git tag names like ``open-release/koa.1``.
The available names are detailed on the `Open edX Named Releases page`_.

**********************************
Upgrading from the Juniper Release
**********************************

The recommended approach to upgrading an existing installation of the Open edX
Juniper release to the Koa release is to make a fresh installation of the
Koa release on a new machine, and move your data and settings to it.

To move and upgrade your Juniper data onto a Koa installation, follow these
steps.

#. Be sure that your Juniper installation is on the latest commit from
   ``open-release/juniper.master``. This ensures that your database is fully 
   migrated and ready for upgrade to Koa.

#. Stop all services on the Juniper machine.

#. Dump the data on the Juniper machine. Here's an example script that will dump
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

#. Copy the ``.tgz`` data file to the Koa machine.

#. Stop all services on the Koa machine.

#. Restore the Juniper data into the Koa machine. As an example, you might
   use the following commands.

    .. code-block:: bash

        $ tar -xvf openedx-data-20200411T154750.tgz
        $ mysql -uroot -p < mysql-data-20200411T154750.sql
        $ mongorestore -u admin -p -h localhost --authenticationDatabase admin --drop -d edxapp mongo-dump-20200411T154750/edxapp
        $ mongorestore -u admin -p -h localhost --authenticationDatabase admin --drop -d cs_comment_service mongo-dump-20200411T154750/cs_comment_service_development

#. Run the Koa migrations, which will update your Juniper data to be
   valid for Koa:

    .. code-block:: bash

        $ /edx/app/edx_ansible/edx_ansible/util/install/native.sh --tags migrate

#. Copy your configuration files from the Juniper machine to the Koa machine.

#. Restart all services.

*************************************
Upgrading to a Subsequent Koa Release
*************************************

Occasionally, we release updates to Koa.  For example, the second
release of Koa will be ``open-release/koa.2``.
The steps to upgrade differ based on your original installation method.

===============================
Upgrading a Docker Installation
===============================

Devstack is installed using Docker. To upgrade from one Koa
release to another, follow the instructions in `devstack`_.

===============================
Upgrading a Native Installation
===============================

If you installed Open edX using the Open edX Native Installation, please
migrate to Tutor. This `Native Installation to Tutor forum post`_ may be helpful,
as may be `this second Native to Tutor post`_. If not, post on the `Open edX Forums`_.

If you installed Open edX using the Open edX Native Installation, you can
upgrade from one Koa release to another by re-running those steps using
your desired Koa tag as the new value for ``OPENEDX_RELEASE``.


.. include:: ../../../links/links.rst
