.. _Options for Updating Your Open edX Instances:

##############################################
Options for Updating Your Open edX Instances
##############################################

This topic outlines the options for updating to the new database and
table configuration required by the ``courseware_studentmodulehistory`` change.

.. contents::
   :local:
   :depth: 1

Because each Open edX installation has a unique set of constraints
and requirements, edX recommends that you review all of these options before
selecting one for your instance or instances.

******************************
Migrate All Data to One Table
******************************

.. note:: This option is suitable for instances with large databases,
  such as a large production instance.

For instances with relatively large databases, you set up the new database and
table and then migrate all existing data to the new table. When the process is
complete, the system uses only the new table. An outline of the steps you
complete follows.

#. Create the ``edxapp_csmh`` database.

#. Update ``lms.auth.json`` with a new entry in the DATABASES section.

#. Update ``lms.env.json`` to set ``"ENABLE_CSMH_EXTENDED": true``.

#. Update ``edxapp/defaults/main.yml`` with a new entry in the edxapp_databases
   section.

#. Migrate all data from ``courseware_studentmodulehistory`` to
   ``courseware_studentmodulehistoryextended``.

#. Update ``lms.env.json`` to set
   ``"ENABLE_READING_FROM_MULTIPLE_HISTORY_TABLES": false``.

#. Truncate ``courseware_studentmodulehistory``.

As soon as you set ``"ENABLE_CSMH_EXTENDED": true``, the system writes only to
the ``courseware_studentmodulehistoryextended`` table, but it reads from both
that table and the ``courseware_studentmodulehistory`` table. To reduce the
overhead of querying two tables in two databases, you migrate data and then
set ``"ENABLE_READING_FROM_MULTIPLE_HISTORY_TABLES": false``.

This option is suitable for installations that have a large number of records
in the ``courseware_studentmodulehistoryextended`` table.

For more information, see :ref:`CSMHE Procedures`.

*******************************
Keep, and Query, Both Tables
*******************************

.. note:: This option is suitable for instances with small databases,
  such as a fullstack or small production instance.

For instances with relatively small databases, you set up the new database and
table and then configure the system to read from both tables, without migrating
data. An outline of the steps you need to complete follows.

#. Create the ``edxapp_csmh`` database.

#. Update ``lms.auth.json`` with a new entry in the DATABASES section.

#. Update ``lms.env.json`` to set ``"ENABLE_CSMH_EXTENDED": true``. Leave
   ``"ENABLE_READING_FROM_MULTIPLE_HISTORY_TABLES": true``.

A system with this configuration writes only to the new
``courseware_studentmodulehistoryextended`` table, but it reads from both that
table and the ``courseware_studentmodulehistory`` table in the ``edxapp``
database.

This option is suitable when the performance overhead of querying two databases
is not a significant consideration.

For more information, see :ref:`CSMHE Procedures`.

**************
Reinstall
**************

.. note:: This option is suitable for Devstacks only.

To set up Devstack with the new database and SQL table, you can reprovision.
If you choose this option for updating Devstack, no further configuration
or migration procedures are required.

   .. code-block:: bash

     vagrant provision

Reprovisioning adds the ``edxapp_csmh`` database and its
``courseware_studentmodulehistoryextended`` table. The ``lms.env.json`` feature
flags that control ``courseware_studentmodulehistoryextended`` use have the
following settings.

   .. code-block:: bash

     "ENABLE_CSMH_EXTENDED": true
     "ENABLE_READING_FROM_MULTIPLE_HISTORY_TABLES": true

A system with this configuration writes to the new
``courseware_studentmodulehistoryextended`` table only, but queries both
tables.


.. include:: ../../../links/links.rst
