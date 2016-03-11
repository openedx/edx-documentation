.. _Migrating CSMH:

########################################################
Migrating the ``courseware_studentmodulehistory`` Table
########################################################

This section describes a change to the ``courseware_studentmodulehistory``
database table that requires a new database configuration and a migration.
These changes took place for the edx.org and edX Edge sites during the first
two weeks of March 2016.

.. important::  All Open edX installations that use **the latest version**
  available on the master branch of the edx-platform repository, including
  devstack installations, must also perform these changes.

.. contents::
   :local:
   :depth: 1

.. note:: No changes are required or supported at this time for Open edX
  installations that use the **Dogwood release**. The changes needed for the
  ``courseware_studentmodulehistory`` table will be required during the upgrade
  to the Open edX Eucalyptus release.

****************************
Why Is a Migration Needed?
****************************

The ``courseware_studentmodulehistory`` database table contains a record for
each attempt that learners make to answer ``problem`` type XBlocks correctly.
This database table is a standard ``StudentModuleHistory`` Django model. It has
an ``id`` column with a type of 32-bit signed integer, and therefore has a
maximum capacity of 2,147,483,647 records.

Typically, ``courseware_studentmodulehistory`` is the largest table in the
database. On the edx.org site, 20,000 to 80,000 records are written to this
table every hour. A migration to replace the current form of the
``courseware_studentmodulehistory`` table with a higher capacity form is
required to assure that no data is lost for the edx.org site.

A new database table, ``courseware_studentmodulehistoryextended``, replaces the
``courseware_studentmodulehistory`` table. The
``courseware_studentmodulehistoryextended`` table uses a custom Django field
type to give the ``id`` column a type of 64-bit unsigned integer, which offers
an exponentially larger storage capacity.

********************************
Database Configuration Strategy
********************************

Due to the number of records involved, the edX DevOps team estimated a duration
of several days for the migration of the edx.org
``courseware_studentmodulehistory`` table. Downtime of that duration for the
edx.org site is not acceptable, so the team developed a two-part strategy for
this procedure.

.. contents::
   :local:
   :depth: 1

=============================
Creating a Separate Database
=============================

To avoid site downtime, you create the
``courseware_studentmodulehistoryextended`` table in a separate database
named ``student_module_history``. The software available on the master branch
of the edx-platform repository as of 16 March 2016 writes records to this
database and table.

To avoid data loss, the system continues to read the records in both tables,
the original in the default database and the extended table in the
``student_module_history`` database.

=======================
Migrating Table Data
=======================

To migrate the data from the original table to the extended table, you enable a
feature flag, ``ENABLE_CSMH_EXTENDED``. This change starts the migration
script.

When the migration is complete, you enable another feature flag,
``READ_ONLY_FROM_CSMHE``, so that new records are written only to the extended
table. In addition, the script iterates back to migrate any records written to
the original table after the script started to the extended table.

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

.. how to info to come

.. include:: ../../links/links.rst
