.. _Migrating CSMH:

##########################################################################
Overview of the ``courseware_studentmodulehistory`` Table Migration
##########################################################################

This topic provides background information about why a migration is needed.

.. contents::
   :local:
   :depth: 1

For procedures about how to complete the upgrade for Open edX instances that
are following the master version of the platform, see
:ref:`Migrating CSMH`.

****************************************************************
What Is the ``courseware_studentmodulehistory`` Table?
****************************************************************

The ``courseware_studentmodulehistory`` database table contains a record for
each attempt that learners make to answer ``problem`` type XBlocks correctly.
This database table is a standard ``StudentModuleHistory`` Django model. It has
an ``id`` column with a type of 32-bit signed integer, and therefore has a
maximum capacity of 2,147,483,647 records.

********************************
Why Is a Migration Needed?
********************************

Typically, ``courseware_studentmodulehistory`` is the largest table in the
database. It can be twice as large as the next largest table,
``courseware_studentmodule``.

On the edx.org site, two records are written to this table every second. Before
this table for edx.org reached even half of its maximum capacity, edX began to
strategize a replacement with a higher capacity form.

*************************
What Is the New Table?
*************************

The new database table, ``courseware_studentmodulehistoryextended``, uses a
custom Django field type to give the ``id`` column a type of 64-bit unsigned
integer, which offers an exponentially larger storage capacity than the
``courseware_studentmodulehistory`` table.

********************************
Why Is A New Database Needed?
********************************

The ``courseware_studentmodulehistoryextended`` table must be created in a new
database, ``edxapp_csmh``, which will coexist alongside the existing ``edxapp``
database.

EdX included the new database in the migration design to address several
requirements.

* System performance during the actual data migration process.
*
* The storage capacity of the new ``courseware_studentmodulehistoryextended``
  table.

The software available on the master branch of the edx-platform repository as
of 16 March 2016 writes records to this database and table.

.. ^^ this is really unclear



.. include:: ../../../links/links.rst
