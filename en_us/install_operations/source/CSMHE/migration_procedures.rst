.. _CSMHE Migration Procedures:

##############################################
Procedures for Migrating Open edX Instances
##############################################


.. contents::
   :local:
   :depth: 1



****************
Migrate Devstack
****************

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

****************************************************
Migrate Fullstack or a Small Production Installation
****************************************************



******************************************
Migrate a Large Production Installation
******************************************



Create the ``edxapp_csmh`` Database



Verify the Starting ID Offset



Run the migration


Deploy edxapp with ENABLE_CSMH_EXTENDED = True



Configuration




.. include:: ../../../links/links.rst
