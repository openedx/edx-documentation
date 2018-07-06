.. _Starting Devstack:

######################################
Starting the Open edX Developer Stack
######################################

After you have installed Devstack within Docker, you can start Open edX
services. You start the edX services with the following command. This command 
mounts the repositories under the DEVSTACK_WORKSPACE directory. 

   .. code-block:: bash

    make dev.up

   As an alternative, use :ref:`Docker Sync` with the following command.

   .. code-block:: bash

    make dev.sync.up


**********************
Connecting to Services
**********************

After it starts, each service is accessible at ``localhost`` on a specific 
port. The table below provides links to the homepage of each service. Since 
some services are not meant to be user-facing, the homepage may be the API 
root.

  .. list-table::
   :widths: 20 60
   :header-rows: 1

   * - Service
     - URL
   * - Catalog/Discovery
     - http://localhost:18381/api-docs/
   * - Credentials
     - http://localhost:18150/api/v2/
   * - E-Commerce/Otto
     - http://localhost:18130/dashboard/
   * - LMS
     - http://localhost:18000/
   * - Notes/edx-notes-api
     - http://localhost:18120/api/v1/
   * - Studio/CMS
     - http://localhost:18010/

After the services have started, you can get shell access to one of the 
services with a  ``make <service>-shell`` command. For example, to access the 
Catalog/Course Discovery Service, run this command.

  .. code-block:: bash
 
   make discovery-shell

************
Viewing Logs
************ 

To see logs from containers running in detached mode, run the following 
command.

  .. code-block:: bash
   
   make logs

As an alternative, you can use Docker's Kitematic feature, which is available from the **Docker for Mac** menu.

To view the logs of a specific service container, run a 
``make <service>-logs`` command. For example, to access the logs for the 
Ecommerce service, run this command.

  .. code-block:: bash
   
   make ecommerce-logs

*******************
Restarting Services
*******************

To restart a particular service, run a ``docker-compose restart <service>`` 
command. For example, to restart the Studio service, run the following 
command. 

  .. code-block:: bash
   
   docker-compose restart studio

********************
Restarting Devstack
********************

To reset your environment and start provisioning from scratch, run the 
following command.

  .. code-block:: bash
   
   make destroy

For information on all the available make commands, run the following 
command.

  .. code-block:: bash
   
   make help

.. _Default Accounts:

****************
Default Accounts
****************

When you install an Open edX system, the following user accounts are created by
default.

  .. list-table::
   :widths: 20 60
   :header-rows: 1

   * - Account
     - Description
   * - ``staff@example.com``
     - An LMS and Studio user with course creation and editing permissions.
       This user is a course team member with the Admin role, which gives
       rights to work with the demonstration course in Studio, the LMS, and
       Insights.
   * - ``verified@example.com``
     - A student account that you can use to access the LMS for testing
       verified certificates.
   * - ``audit@example.com``
     - A student account that you can use to access the LMS for testing course
       auditing.
   * - ``honor@example.com``
     - A student account that you can use to access the LMS for testing honor
       code certificates.

The default password for all of these accounts is ``edx``.

.. _Docker Sync:

*******************************************
Improve Mac OS Performance with Docker Sync
*******************************************

Docker for Mac has known filesystem issues that significantly decrease
performance for certain use cases, such as running tests in ``edx-platform``.
To improve performance, you can use Docker Sync to synchronize file data from
the host machine to the containers.

Using Docker Sync has the disadvantages of adding complexity and sometimes leading to issues with the filesystem getting out of sync.

You can switch between using Docker Sync and native volumes at any time, by
using the `make` targets with or without `sync`. However, if you want to
switch inside the PyCharm IDE, this is harder to do quickly due to its need to
rebuild its cache of the containers' virtual environments.

If you are using Mac OS, follow the `Docker sync installation`_
instructions before provisioning.

================================
Docker Sync Troubleshooting tips
================================

Check your version and make sure you are running Docker Sync 0.4.6 or above:

  .. code-block:: bash

   docker-sync --version

If not, upgrade to the latest version:

  .. code-block:: bash

   gem update docker-sync

If you are having issues with Docker Sync, try the following:

  .. code-block:: bash

   make stop
   docker-sync stop
   docker-sync clean

.. include:: ../../../links/links.rst

