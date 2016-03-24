.. _Migrating CSMH:

########################################################
Migrating the ``courseware_studentmodulehistory`` Table
########################################################

This section describes a change to the ``courseware_studentmodulehistory``
database table that requires a new database configuration and a migration.
This change took place for the edx.org and edX Edge sites during March 2016.

.. important:: All Open edX installations that use the **latest** version
  available on the master branch of the edx-platform repository, including
  devstack and fullstack installations, are affected by this change.

After an overview of the change, this section presents different options for
completing the required procedures. EdX recommends that you review all of these
options before you select and complete the migration for your Open edX
installation.

.. toctree::
   :maxdepth: 2

   CSMHE_overview
   migration_options
   migration_procedures

No changes are required or supported at this time for Open edX installations
that use the **Dogwood** release. The changes described here will be a part
of the upgrade to the Open edX Eucalyptus release.

.. include:: ../../../links/links.rst
