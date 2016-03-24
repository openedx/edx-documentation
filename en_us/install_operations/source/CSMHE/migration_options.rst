.. _Options for Migrating Your Open edX Instances:

##############################################
Options for Migrating Your Open edX Instances
##############################################


.. contents::
   :local:
   :depth: 1



================
Migrate Devstack
================

To migrate a devstack that is used for development and that has a small
database, you replace your devstack with an up to date devstack.

   .. code-block:: bash

     vagrant provision

This procedure adds a devstack with the new ``edxapp_csmh`` database and its
``courseware_studentmodulehistoryextended`` table. The feature flags relevant
to the migration have the following settings.

``ENABLE_CSMH_EXTENDED``: true
``READ_ONLY_FROM_CSMHE``: false

After you provision the new devstack instance, no further migration or
configuration procedures are required. With these settings, the system writes
only to the new ``courseware_studentmodulehistoryextended`` table, but it reads
from both the new table and the ``courseware_studentmodulehistory`` table in
the ``edxapp`` database.

Due to the performance overhead of doing lookups in two databases, this option
is most suitable for development environments with small databases.

For more information, see TBD

====================================================
Migrate Fullstack or a Small Production Installation
====================================================



==========================================
Migrate a Large Production Installation
==========================================



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
