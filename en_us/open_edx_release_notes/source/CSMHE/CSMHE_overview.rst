.. _CSMH Overview:

##########################################################################
Overview of the ``courseware_studentmodulehistory`` Changes
##########################################################################

This topic provides background information about the
``courseware_studentmodulehistory`` table and why a new database configuration
is needed.

.. contents::
   :local:
   :depth: 1

For procedures about how to upgrade all Open edX instances that follow master,
see :ref:`CSMHE Procedures`.

.. note:: The changes described in this section are a part of the upgrade to
 the Open edX Eucalyptus release.

****************************************************************
What Is the ``courseware_studentmodulehistory`` Table?
****************************************************************

The ``courseware_studentmodulehistory`` database table contains a record for
each attempt that learners make to answer problem types that are implemented in
the edX platform by the ``capa_module`` XBlock correctly. This database table
is a standard Django model. It has an ``id`` column with a type of 32-bit
signed integer, and therefore has a maximum capacity of 2,147,483,647 records.

.. _What Is the Issue:

************************
What Is the Issue?
************************

Typically, ``courseware_studentmodulehistory`` is the largest table in the
database. It can be twice as large as the next largest table,
``courseware_studentmodule``.

On the edx.org site, two records are written to this table every second. Before
this table for edx.org reached even half of its maximum capacity, edX began to
design a replacement with a higher capacity form.

*******************************
What Is the Replacement Table?
*******************************

The new database table,
``coursewarehistoryextended_studentmodulehistoryextended``, uses a custom
Django field type to give the ``id`` column a type of 64-bit unsigned integer,
which offers an exponentially larger storage capacity than the
``courseware_studentmodulehistory`` table.

.. _Why Is A New Database Needed:

********************************
Why Is A New Database Needed?
********************************

By design, the ``coursewarehistoryextended_studentmodulehistoryextended`` table
must be created in a new database, ``edxapp_csmh``. The new database will
coexist alongside the existing ``edxapp`` database.

Depending on your operational needs, you can either create this database in
your existing database infrastructure or stand a new database server up.

EdX chose to set up a new database to address several requirements.

* Distribute write load across different backends.
* Reclaim storage on our main database instance, shifting that storage to a
  less powerful and less expensive system.
* Enable smaller, faster, and less disruptive backups.
* Ensure faster disaster recovery by having smaller backups.

The edx-platform repository master branch writes records to this database and
table as of 5 May 2016.


.. include:: ../../../links/links.rst
