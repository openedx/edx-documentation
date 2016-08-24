.. _Replacing CSMH:

########################################################
Replacing the ``courseware_studentmodulehistory`` Table
########################################################

This section describes a change to the ``courseware_studentmodulehistory``
database table.

.. note:: The changes described in this section are a part of the upgrade to
 the Open edX Eucalyptus release.

The change to the ``courseware_studentmodulehistory`` database table requires a
new database configuration, and offers an optional data migration. This change
will be released to the edx-platform repository on 5 May 2016, and will affect
all Open edX installations that follow master on that date.

.. important:: If you are responsible for maintaining an Open edX instance,
 including a devstack, fullstack, or production installation, you must prepare
 for this change before you upgrade to the 5 May 2016 version of master.

This section presents an overview of the change followed by options for
completing the required and optional procedures. EdX recommends that you review
all of the topics in this section before you choose an option for your Open edX
installation.

.. toctree::
   :maxdepth: 2

   CSMHE_overview
   migration_options
   migration_procedures

.. include:: ../../../links/links.rst
