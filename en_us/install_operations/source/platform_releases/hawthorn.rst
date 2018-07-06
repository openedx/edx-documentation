.. _Open edX Hawthorn Release:

########################
Open edX Hawthorn Release
########################

This section describes how to install the Open edX Hawthorn release.

.. contents::
 :local:
 :depth: 1

****************************
What's Included in Hawthorn
****************************

The Open edX Hawthorn release contains several new features for learners,
course teams, and developers. For more information, see
:ref:`openreleasenotes:Open edX Hawthorn Release`.

******************************
What Is the Hawthorn Git Tag?
******************************

A git tag identifies the version of Open edX code that is the Hawthorn release.
You can find the most up-to-date git tag for the current Open edX release on
the `Open edX Releases Wiki page`_.

The following Open edX git repositories have the Hawthorn git tag:

* edx-platform
* configuration
* course_discovery
* cs_comments_service
* xqueue
* ecommerce
* ecommerce-worker
* edx-analytics-configuration
* edx-analytics-dashboard
* edx-analytics-data-api
* edx-analytics-pipeline
* edx-certificates
* edx-custom-a11y-rules
* edx-demo-course
* edx-documentation
* edx-notes-api
* edx-ui-toolkit
* notifier
* ux-pattern-library

*******************************
Installing the Hawthorn Release
*******************************

You can install the Open edX Hawthorn release using :ref:`Devstack <Installing
the Open edX Developer stack>`.

Hawthorn releases have git tag names like ``open-release/hawthorn.1``.
The available names are detailed on the `Open edX Releases Wiki page`_.

.. _upgrade_ginkgo:

**********************************
Upgrading from the Ginkgo Release
**********************************

The recommended approach to upgrading an existing installation of the Open edX
Ginkgo release to the Hawthorn release is to make a fresh installation of the
Hawthorn release on a new machine, and move your data and settings to it.

To move and upgrade your Ginkgo data onto a Hawthorn installation, follow these
steps.

>>>> IS THIS TRUE?
#. Be sure that your Ginkgo installation is on Ginkgo.2.  The Ginkgo.2 release
   provided required database migrations beyond what was in Ginkgo.2.  The only
   version of Ginkgo that will upgrade to Hawthorn successfully is Ginkgo.2.

#. Stop all services on the Ginkgo machine.

#. Dump the data on the Ginkgo machine. Here's an example script that will dump
   the MySQL and Mongo databases into a single ``.tgz`` file.  The script will
   prompt for the MySQL and Mongo passwords as needed.

    .. code-block:: bash

        #!/bin/bash
        MYSQL_CONN="-uroot -p"
        echo "Reading MySQL database names..."
        mysql ${MYSQL_CONN} -ANe "SELECT schema_name FROM information_schema.schemata WHERE schema_name NOT IN ('mysql','information_schema','performance_schema')" > /tmp/db.txt
        DBS="--databases $(cat /tmp/db.txt)"
        NOW="$(date +%Y%m%dT%H%M%S)"
        SQL_FILE="mysql-data-${NOW}.sql"
        echo "Dumping MySQL structures..."
        mysqldump ${MYSQL_CONN} --add-drop-database --no-data ${DBS} > ${SQL_FILE}
        echo "Dumping MySQL data..."
        # If there is table data you don't need, add --ignore-table=tablename
        mysqldump ${MYSQL_CONN} --no-create-info ${DBS} >> ${SQL_FILE}

        for db in edxapp cs_comment_service_development; do
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

#. Run the Hawthorn migration script, which will update your Ginkgo data to be
   valid for Ginkgo:

    .. code-block:: bash

        $ /edx/app/edx_ansible/edx_ansible/util/install/sandbox.sh --tags migrate

#. Copy your configuration files from the Ginkgo machine to the Hawthorn
    machine.

#. Restart all services.

.. _oscar_hawthorn:

=========================
Upgrading Django Oscar
=========================

>> ANYTHING ABOUT DJANGO 1.11? The following is leftover from Ginkgo and prob. no longer applies

The Hawthorn release of Open edX upgrades Django Oscar to version 1.5. If you
have an existing installation of Open edX with the E-Commerce service, and your
``orders`` table is larger than a million rows, there is an additional step to
upgrade your Django Oscar installation.

The migration includes a change to the ``guest_email`` column in the ``orders``
table. This change is applied automatically.  If your ``orders`` table is
larger than a million rows, this migration may lock the table for an extended
amount of time. The E-Commerce service does not normally use the
``guest_email`` column. If your installation does not use this column, you can
avoid the table lock by using the ``--fake`` argument in migrating the
``orders`` table, running the ``migrate`` command in the following form.

.. code-block:: bash

   ./manage.py migrate orders 0013 --fake


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
release to another, follow the instructions in :ref:`Updating Docker`.

.. code-block:: bash

    $ export OPENEDX_RELEASE=open-release/hawthorn.2
    $ vagrant provision

===============================
Upgrading a Native Installation
===============================

If you installed Open edX using the `Open edX Native Installation`_, you can
upgrade from one Hawthorn release to another by re-running those steps using
your desired Hawthorn tag as the new value for ``OPENEDX_RELEASE``.


.. include:: ../../../links/links.rst
