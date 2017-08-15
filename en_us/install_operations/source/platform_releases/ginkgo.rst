.. _Open edX Ginkgo Release:

########################
Open edX Ginkgo Release
########################

This section describes how to install the Open edX Ginkgo release.

.. contents::
 :local:
 :depth: 1

**************************
What's Included in Ginkgo
**************************

The Open edX Ginkgo release contains several new features for learners,
course teams, and developers. For more information, see
:ref:`openreleasenotes:Open edX Ginkgo Release`.

****************************
What Is the Ginkgo Git Tag?
****************************

A git tag identifies the version of Open edX code that is the Ginkgo release.
You can find the most up-to-date git tag for the current Open edX release on
the `Open edX Releases Wiki page`_.

The following Open edX git repositories have the Ginkgo git tag:

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

******************************
Installing the Ginkgo Release
******************************

You can install the Open edX Ginkgo release using :ref:`Devstack <Installing
the Open edX Developer stack>` or :ref:`Fullstack <Installing Open edX Fullstack>`.

Review the prerequisites and instructions for each option, and then choose the
option that best meets your needs. Ensure that you install the
required software to run the Open edX platform.

Ginkgo releases have git tag names like ``open-release/ginkgo.1``.
The available names are detailed on the `Open edX Releases Wiki page`_.

.. _upgrade_ficus:

**********************************
Upgrading from the Ficus Release
**********************************

One approach to upgrading an existing installation of the Open edX Ficus
release to the Ginkgo release is to make a fresh installation of the Ginkgo
release on a new machine, and move your data and settings to it.

To move and upgrade your Ficus data onto a Ginkgo installation, follow these
steps.

#. Be sure that your Ficus installation is on Ficus.4.  The Ficus.4 release
   provided required database migrations beyond what was in Ficus.3.  The only
   version of Ficus that will upgrade to Ginkgo successfully is Ficus.4.

#. Stop all services on the Ficus machine.

#. Dump the data on the Ficus machine. Here's an example script that will dump
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

#. Copy the ``.tgz`` data file to the Ginkgo machine.

#. Stop all services on the Ginkgo machine.

#. Restore the Ficus data into the Ginkgo machine. As an example, you might use
   the following commands.

    .. code-block:: bash

        $ tar -xvf openedx-data-20170811T154750.tgz
        $ mysql -uroot -p < mysql-data-20170811T154750.sql
        $ mongorestore -u admin -p -h localhost --authenticationDatabase admin --drop -d edxapp mongo-dump-20170811T154750/edxapp
        $ mongorestore -u admin -p -h localhost --authenticationDatabase admin --drop -d cs_comment_service mongo-dump-20170811T154750/cs_comment_service_development

#. To migrate data from Ficus to Ginkgo, you need to drop the database tables
   used by djcelery. These tables should be empty in your Ficus data, so it is
   safe to drop them. The edx-platform application has a management command to
   check that they are empty and drop them:

    .. code-block:: bash

        $ sudo su - -s /bin/bash edxapp
        edxapp@xyz:~$ . edxapp_env
        edxapp@xyz:~$ cd edx-platform/
        edxapp@xyz:~/edx-platform$ python manage.py lms drop_djcelery_tables --settings=aws

#. Run the Ginkgo migration script, which will update your Ficus data to be valid
   for Ginkgo:

    .. code-block:: bash

        $ /edx/app/edx_ansible/edx_ansible/util/install/sandbox.sh --tags migrate

#. Copy your configuration files from the Ficus machine to the Ginkgo machine.

#. Restart all services.

.. _oscar_ginkgo:

=========================
Upgrading Django Oscar
=========================

The Ginkgo release of Open edX upgrades Django Oscar to version 1.4. If you have
an existing installation of Open edX with the E-Commerce service, and your
``orders`` table is larger than a million rows, there is an additional step to
upgrade your Django Oscar installation.

The migration includes a change to the ``guest_email`` column in the ``orders``
table. This change is applied automatically.  If your ``orders`` table is larger
than a million rows, this migration may lock the table for an extended amount of
time. The E-Commerce service does not normally use the ``guest_email`` column.
If your installation does not use this column, you can avoid the table lock by
using the ``--fake`` argument in migrating the ``orders`` table, running the
``migrate`` command in the following form.

.. code-block:: bash

   ./manage.py migrate orders 0013 --fake


****************************************
Upgrading to a Subsequent Ginkgo Release
****************************************

Occasionally, we release updates to Ginkgo.  For example, the second
release of Ginkgo will be ``open-release/ginkgo.2``.
The steps to upgrade differ based on your original installation method.

================================
Upgrading a Vagrant Installation
================================

Devstack and Fullstack are installed using Vagrant.  To upgrade from one Ginkgo
release to another, run the following commands in the host operating system:

.. code-block:: bash

    $ export OPENEDX_RELEASE=open-release/ginkgo.2
    $ vagrant provision

===============================
Upgrading a Native Installation
===============================

If you installed Open edX using the `Open edX Native Installation`_, you can
upgrade from one Ginkgo release to another by re-running those steps using your
desired Ginkgo tag as the new value for ``OPENEDX_RELEASE``.


.. include:: ../../../links/links.rst
