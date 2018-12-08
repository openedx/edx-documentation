
* The edX analytics data exporter now includes the following steps to increase
  the quality of data delivered in SQL tables to partner institutions.

  * All embedded tabs, newlines, and carriage returns have been replaced by the
    two-character sequences ``\t``, ``\n``, and ``\r``, respectively.

  * Values in timestamp fields now appear without trailing zeros. For example,
    "2015-10-12 07:51:40.000000" now appear as "2015-10-12 07:51:40". These
    changes apply to all of the .sql files in edX data packages, with the
    exception of data for the ``courseware_studentmodule`` table.

  * Backslash characters (``\``) are now escaped as ``\\``.

  These changes affect data packages available beginning 13 Dec 2015.

* SQL tables of data for open response assessment (ORA) problems are now
  included in an ``ora`` subdirectory in the weekly database
  ``{org}-{date}.zip`` data file. In addition, the ``student_anonymoususerid``
  SQL table, which is necessary for interpreting this data, is also included in
  the weekly database data file.

  These tables are included in data packages available beginning 13 Dec 2015.
  For more information, see the :ref:`data:ORA2 Data` section in the *EdX
  Research Guide*.
