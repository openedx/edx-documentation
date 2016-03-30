.. _CSMH Overview:

##########################################################################
Overview of the ``courseware_studentmodulehistory`` Migration
##########################################################################

This topic provides background information about the
``courseware_studentmodulehistory`` table and why a new database configuration
is needed.

.. contents::
   :local:
   :depth: 1

For procedures about how to upgrade all Open edX instances that follow master,
see :ref:`CSMHE Migration Procedures`.

****************************************************************
What Is the ``courseware_studentmodulehistory`` Table?
****************************************************************

The ``courseware_studentmodulehistory`` database table contains a record for
each attempt that learners make to answer ``problem`` XBlocks correctly.
This database table is a standard ``StudentModuleHistory`` Django model. It has
an ``id`` column with a type of 32-bit signed integer, and therefore has a
maximum capacity of 2,147,483,647 records.

************************
What Is the Issue?
************************

Typically, ``courseware_studentmodulehistory`` is the largest table in the
database. It can be twice as large as the next largest table,
``courseware_studentmodule``.

On the edx.org site, two records are written to this table every second. Before
this table for edx.org reached even half of its maximum capacity, edX began to
strategize a replacement with a higher capacity form.

*******************************
What Is the Replacement Table?
*******************************

The new database table, ``courseware_studentmodulehistoryextended``, uses a
custom Django field type to give the ``id`` column a type of 64-bit unsigned
integer, which offers an exponentially larger storage capacity than the
``courseware_studentmodulehistory`` table.

********************************
Why Is A New Database Needed?
********************************

By design, the ``courseware_studentmodulehistoryextended`` table must be
created in a new database, ``edxapp_csmh``. The new database will coexist
alongside the existing ``edxapp`` database.

EdX chose to set up a new database to address several requirements.

* System performance during the actual data migration process.
* Load balancing between the databases on AWS.
* The storage capacity of the new ``courseware_studentmodulehistoryextended``
  table.

.. ^^ guessing. Useful?

The edx-platform repository master branch writes records to this database and
table as of TBD.


.. include:: ../../../links/links.rst
