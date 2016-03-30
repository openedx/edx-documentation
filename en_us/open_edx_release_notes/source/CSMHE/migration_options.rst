.. _Options for Updating Your Open edX Instances:

##############################################
Options for Updating Your Open edX Instances
##############################################

Because Open edX installations really do come in all shapes and sizes, this
topic outlines different options for updating your Open edX instances to use
the new database and table configuration.

.. contents::
   :local:
   :depth: 1



**************
Reprovision
**************

.. note:: This option is only suitable for devstacks. You can use this option,
 or either of the other options, to update a devstack.

To update devstack with the new database and SQL table, you can replace
your devstack with an up to date version.

   .. code-block:: bash

     vagrant provision

No further migration or configuration procedures are required.

Reprovisioning updates your devstack with the new ``edxapp_csmh`` database and
its ``courseware_studentmodulehistoryextended`` table.

The feature flags that are added to ``lms.env.json`` to control system use of
the ``courseware_studentmodulehistoryextended`` table have the following
settings.

   .. code-block:: bash

     "ENABLE_CSMH_EXTENDED": true
     "ENABLE_READING_FROM_MULTIPLE_HISTORY_TABLES": false

With this configuration, the system writes only to the new
``courseware_studentmodulehistoryextended`` table, but it reads from both the
new table and the ``courseware_studentmodulehistory`` table in the ``edxapp``
database. For most devstacks, the performance overhead of querying two
databases is not a significant consideration.

********************************************
Keep and Query Both Tables
********************************************

.. note:: This option is only suitable for instances with small databases,
 such as a fullstack or small production instance.



Due to the performance overhead of doing lookups in two databases, this option
is most suitable for development environments with small databases.

**********************************************
Keep One Table, Truncate the Other
**********************************************

Large production instances


Create the ``edxapp_csmh`` Database



Verify the Starting ID Offset



Run the migration


Deploy edxapp with ENABLE_CSMH_EXTENDED = True



Configuration



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
 nn
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




****************************

****************************


************************************
Options for Updating Your Instances
************************************

Devstack Instance: provision a new Vagrant instance.

Fullstack or Small Production Instance:

Larger Production Instance:


.. include:: ../../../links/links.rst
