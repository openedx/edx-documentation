.. _Migrating CSMH:

########################################################
Migrating the ``courseware_studentmodulehistory`` Table
########################################################

This section describes a change to the ``courseware_studentmodulehistory``
database table that requires a new database configuration and how you update
your Open edX instances. This change will be released to the edx-platform
repository on TBD, and will affects all Open edX installations that follow
master as of that date.

.. important:: If you are responsible for maintaining an Open edX instance,
 including devstack, fullstack, or production installations, you must prepare
 for this change before you upgrade to the TBD version of master.

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
that use the **Dogwood** release. For those installations, the changes
described in this section will be a part of the upgrade to the Open edX
Eucalyptus release.

.. include:: ../../../links/links.rst
