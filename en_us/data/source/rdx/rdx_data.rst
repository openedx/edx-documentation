.. _Data Obfuscation Procedures for RDX:

########################################
Data Obfuscation Procedures for RDX
########################################

To receive RDX data, researchers who are approved for a research project must
work with their institution's data czar. Before delivering data through this
program, edX works to obscure personally identifying information (PII) by
obfuscating obvious identifiers. EdX executes the obfuscation process on every
XBlock in the course, including the course itself.

The following topics describe the data obfuscation procedures.

.. contents::
   :local:
   :depth: 1

.. _Data Obfuscation Methods:

**************************
Data Obfuscation Methods
**************************

To obfuscate PII and other sensitive information in RDX data packages, edX
uses these methods to modify data.

.. contents::
   :local:
   :depth: 1

=================
Remapping
=================

EdX remaps SQL table column values that are foreign keys, such as the
``user_id`` and ``username`` values in the ``auth_userprofile`` table. This
process applies a format-preserving algorithm to the affected data values
across all table columns and event member fields. As a result, scripts and
software designed to process these values in institution-specific data packages
should continue to function as expected for an RDX data package.

==========
Removal
==========

Data removal effectively deletes a data value. This process replaces a value
with NULL, a zero-length string, or zeros, based on the data type of the column
or field.

EdX applies this method to files and columns that contain sensitive data or PII
that cannot be remapped to a usable value. Examples include the ``first_name``
and ``last_name`` columns in the ``auth_userprofile`` table and
``wiki_articlerevision.ip_address``.

=================
Replacement
=================

The replacement method identifies text strings that have characteristics of
PII. Identified values are replaced by token values. EdX typically applies this
method to free text, including discussion posts and wiki articles.

The replacement method identifies and replaces the following values.

* Email addresses in ``{name}@{destination}.{domain}`` format. All of the
  characters in this format must be ASCII.

* Telephone numbers in common European and U.S. formats.

* Usernames that match the value in ``auth_user.username``, with the exception
  of usernames that begin or end with a punctuation mark such as an underscore
  or hyphen.

  The system identifies and replaces only the username of the person who is
  associated with the event or row. For example, if a learner identifies a wiki
  contribution with her username, the system replaces that username if it
  matches the value in ``auth_user.username``.

* Names that, after punctuation is removed, match any whitespace delimited
  words of three or more characters in ``auth_userprofile.name``.

  The system identifies and replaces only the name of the person who is
  associated with the event or row. For example, if a learner introduces
  himself on a course discussion page, the system replaces the name if it
  matches a word in ``auth_userprofile.name``.

EdX uses tokens that identify the category of the information that was
replaced, including ``<<EMAIL>>`` and ``<<PHONE_NUMBER>>``. As a result, the
general meaning of the original text can be inferred from the token.

Replacement Example
********************

For example, a learner adds this post to a course discussion.

.. code-block:: none

  Hi all,
    My name is Jonathan M. Doe (johndoe), and I'm excited to be in this
    class. Looking forward to connecting with everyone.
    My email is johndoe@gmail.com, or you can call me at (123)321-1234.
  Thanks,
  -Jonathan

Assuming that the learner has values of "johndoe" in ``auth_user.username`` and
"Jonathan Doe" in ``auth_userprofile.name``, the ``CommentThread.body`` in
the RDX package appears as follows.

.. code-block:: none

  Hi all,
    My name is <<FULLNAME>> M. <<FULLNAME>> (<<USERNAME>>), and I'm excited to
    be in this class. Looking forward to connecting with everyone.
    My email is <<EMAIL>>, or you can call me at <<PHONE_NUMBER>>.
  Thanks,
  -<<FULLNAME>>

Another example follows, in which the learner's post does not include any
values that the replacement method identifies or replaces. In this case, the
``CommentThread.body`` in the RDX package is identical to the original post.

.. code-block:: none

  Hi everyone! My name is John, here's my info if you want to contact me!
    Email: johnmdoe (AT) gmail (DOT) com
    Twitter: @jmdoe
    Mobile: 1233211234

**********************************************
Obfuscated Data in Course Content Data Files
**********************************************

.. contents::
   :local:
   :depth: 1

.. _Obfuscated Data in the course_structure File:

==================================================
Obfuscated Data in the ``course_structure`` File
==================================================

An ``{org}-{course}-{date}-course_structure-{site}-analytics.json`` file is
provided for each course. Its ``metadata`` member field stores course settings
that can contain sensitive data such as the password used to authenticate a
third party service for the course.

Before packaging this file for an RDX research project, edX obfuscates data as
follows.

* EdX only includes an approved subset of the settings that can be defined in
  the ``metadata`` object.

* EdX removes all of the other fields found in this object.

* A new field, ``redacted_metadata``, is added to the file. This JSON array
  lists all of the fields that edX removed.

  An example follows.

  ::

    {
      "category": "course",
      "metadata": {...},
      "redacted_metadata": ["field_name"]
    }

For more information about this file, see :ref:`course_structure`.

=======================================
Obfuscated Data in the ``course`` File
=======================================

An ``{org}-{course}-course-{site}-analytics.xml.tar.gz`` file is provided for
each course. This compressed file contains exports of all of a course's content
in a set of JSON and XML files.

.. note:: EdX does not support imports of ``course`` files that contain
 obfuscated data.

Obfuscated Data in the ``policy.json`` File
********************************************

Like the ``course_structure`` file, the ``policy.json`` file found in the
``course`` file stores course-level settings. To remove data from this file,
edX uses the same procedure described for :ref:`Obfuscated Data in the
course_structure File`.

Before processing, the ``course_structure`` file lists settings by name with their specified values.

::

  {
      "course/course_name": {
          "setting_name": "some_value",
      }
  }


After processing, the ``redacted_attributes`` array is added to list any field
names removed by the obfuscation process.

::

 {
    "course/course_name": {
        "redacted_attributes": ["setting_name"]
    }
 }

For more information about this file, see :ref:`Course Policies`.

Obfuscated Data in the XML Files
*********************************

The XML files found in the ``course`` file store data for course content. The
files for course components can contain sensitive data that is defined at the
component level, such as passwords for third party services.

Before packaging the XML files for an RDX research project, edX obfuscates data
as follows.

* EdX only includes an approved subset of the settings that can be defined for
  components.

* EdX removes all of the other attributes that define component settings.

* The new ``redacted_attributes`` attribute lists all of the attributes that
  edX removed.

* The new ``redacted_children`` attribute lists all of the child nodes that edX
  removed.

For more information about this file, see :ref:`OLX TOC`.

*****************************
Obfuscated Data in SQL Tables
*****************************

.. contents::
   :local:
   :depth: 1

==============================================
Obfuscated Columns in the ``auth_user`` Table
==============================================

The following table lists the columns in the ``auth_user`` table that can
contain PII and the obfuscation method that edX applies before the data is
included in an RDX package. For more information about this table, see
:ref:`auth_user`.

  .. list-table::
     :widths: 25 65
     :header-rows: 1

     * - Column
       - Method
     * - ``id``
       - Remap
     * - ``username``
       - Remap. The result is in the format "username_{remapped ``id`` value}".
     * - ``first_name``
       - Remove
     * - ``last_name``
       - Remove
     * - ``email``
       - Remove
     * - ``password``
       - Remove
     * - ``status``
       - Remove
     * - ``email_key``
       - Remove
     * - ``avatar_type``
       - Remove
     * - ``country``
       - Remove
     * - ``show_country``
       - Remove
     * - ``date_of_birth``
       - Remove
     * - ``interesting_tags``
       - Remove
     * - ``ignored_tags``
       - Remove
     * - ``email_tag_filter_strategy``
       - Remove
     * - ``display_tag_filter_strategy``
       - Remove
     * - ``consecutive_days_visit_count``
       - Remove

For more information about how edX changes the data in these fields, see
:ref:`Data Obfuscation Methods`.

=====================================================
Obfuscated Columns in the ``auth_userprofile`` Table
=====================================================

The following table lists the columns in the ``auth_userprofile`` table that
can contain PII and the obfuscation method that edX applies before the data is
included in an RDX package. For more information about this table, see
:ref:`auth_userprofile`.

  .. list-table::
     :widths: 25 65
     :header-rows: 1

     * - Column
       - Method
     * - ``user_id``
       - Remap (same as ``auth_user.id``)
     * - ``name``
       - Remove
     * - ``language``
       - Remove
     * - ``location``
       - Remove
     * - ``meta``
       - Remove
     * - ``courseware``
       - Remove
     * - ``mailing_address``
       - Remove
     * - ``city``
       - Remove
     * - ``bio``
       - Remove

The self reported, optional values for ``gender``, ``year_of_birth``,
``level_of_education``, ``goals``, and ``country`` are not obfuscated.

For more information about how edX changes the data in these fields, see
:ref:`Data Obfuscation Methods`.

=============================================================
Obfuscated Columns in the ``student_courseenrollment`` Table
=============================================================

The following table lists the columns in the ``student_courseenrollment`` table
that can contain PII and the obfuscation method that edX applies before the data
is included in an RDX package. For more information about this table, see
:ref:`student_courseenrollment`.

  .. list-table::
     :widths: 25 65
     :header-rows: 1

     * - Column
       - Method
     * - ``user_id``
       - Remap (same as ``auth_user.id``)

For more information about how edX changes the data in these fields, see
:ref:`Data Obfuscation Methods`.

=============================================================
Obfuscated Columns in the ``user_api_usercoursetag`` Table
=============================================================

The following table lists the columns in the ``user_api_usercoursetag`` table
that can contain PII and the obfuscation method that edX applies before the data
is included in an RDX package. For more information about this table, see
:ref:`user_api_usercoursetag`.

  .. list-table::
     :widths: 25 65
     :header-rows: 1

     * - Column
       - Method
     * - ``user_id``
       - Remap (same as ``auth_user.id``)

For more information about how edX changes the data in these fields, see
:ref:`Data Obfuscation Methods`.

===============================================================
Obfuscated Columns in the ``teams_courseteammembership`` Table
===============================================================

The following table lists the columns in the ``teams_courseteammembership``
table that can contain PII and the obfuscation method that edX applies before
the data is included in an RDX package. For more information about this table,
see :ref:`teams_courseteammembership`.

  .. list-table::
     :widths: 25 65
     :header-rows: 1

     * - Column
       - Method
     * - ``user_id``
       - Remap (same as ``auth_user.id``)

For more information about how edX changes the data in these fields, see
:ref:`Data Obfuscation Methods`.

===============================================================
Obfuscated Columns in the ``courseware_studentmodule`` Table
===============================================================

The following table lists the columns in the ``courseware_studentmodule`` table
that can contain PII and the obfuscation method that edX applies before the
data is included in an RDX package. For more information about this table, see
:ref:`courseware_studentmodule`.

  .. list-table::
     :widths: 25 65
     :header-rows: 1

     * - Column
       - Method
     * - ``student_id``
       - Remap (same as ``auth_user.id``)
     * - ``state``
       - Replace

For more information about how edX changes the data in these fields, see
:ref:`Data Obfuscation Methods`.

======================================================================
Obfuscated Columns in the ``certificates_generatedcertificate`` Table
======================================================================

The following table lists the columns in the
``certificates_generatedcertificate`` table that can contain PII and the
obfuscation method that edX applies before the data is included in an RDX
package. For more information about this table, see
:ref:`certificates_generatedcertificate`.

  .. list-table::
     :widths: 25 65
     :header-rows: 1

     * - Column
       - Method
     * - ``user_id``
       - Remap (same as ``auth_user.id``)
     * - ``download_url``
       - Remove
     * - ``verify_uuid``
       - Remove
     * - ``download_uuid``
       - Remove
     * - ``name``
       - Remove
     * - ``error_reason``
       - Remove
     * - ``key``
       - Remove

For more information about how edX changes the data in these fields, see
:ref:`Data Obfuscation Methods`.

======================================================================
Obfuscated Columns in the ``verify_student_verificationstatus`` Table
======================================================================

The following table lists the columns in the
``verify_student_verificationstatus`` table that can contain PII and the
obfuscation method that edX applies before the data is included in an RDX
package. For more information about this table, see
:ref:`verify_student_verificationstatus`.

  .. list-table::
     :widths: 25 65
     :header-rows: 1

     * - Column
       - Method
     * - ``user_id``
       - Remap (same as ``auth_user.id``)

For more information about how edX changes the data in these fields, see
:ref:`Data Obfuscation Methods`.

============================================================
Obfuscated Columns in the ``wiki_article`` Table
============================================================

The following table lists the columns in the ``wiki_article`` table that can
contain PII and the obfuscation method that edX applies before the data is
included in an RDX package. For more information about this table, see
:ref:`wiki_article`.

  .. list-table::
     :widths: 25 65
     :header-rows: 1

     * - Column
       - Method
     * - ``owner_id``
       - Remove
     * - ``group_id``
       - Remove

For more information about how edX changes the data in these fields, see
:ref:`Data Obfuscation Methods`.

============================================================
Obfuscated Columns in the ``wiki_articlerevision`` Table
============================================================

The following table lists the columns in the ``wiki_articlerevision`` table
that can contain PII and the obfuscation method that edX applies before the data
is included in an RDX package. For more information about this table, see
:ref:`wiki_articlerevision`.

  .. list-table::
     :widths: 25 65
     :header-rows: 1

     * - Column
       - Method
     * - ``automatic_log``
       - Remove
     * - ``content``
       - Replace
     * - ``ip_address``
       - Remove
     * - ``user_id``
       - Remap (same as ``auth_user.id``)
     * - ``user_message``
       - Remove

For more information about how edX changes the data in these fields, see
:ref:`Data Obfuscation Methods`.

******************************************
Unchanged ``teams_courseteam``  SQL Table
******************************************

The obfuscation process does not change any of the values in the
``teams_courseteam`` table. For more information about this table, see
:ref:`teams_courseteam`.

********************************
Data Omitted from RDX Packages
********************************

The following data is not included in RDX packages.

*  The email opt in report in the ``{org}-email_opt_in-{site}-analytics.csv``
   file. For more information about this report, see :ref:`Institution_Data`.

* The SQL tables in the data schema for the edX open response assessment (ORA)
  system. For more information about this data schema, see :ref:`ORA2 Data`.

* The ``user_id_map`` SQL table. For more information about this table, see
  :ref:`user_id_map`.

******************************
Obfuscated Discussion Data
******************************

The following table lists fields in the ``CommentThread`` and ``Comment`` JSON
documents that can contain PII and the obfuscation method that edX applies
before the data is included in an RDX package. For more information about these
documents, see :ref:`Discussion Forums Data`.

  .. list-table::
     :widths: 30 30 35
     :header-rows: 1

     * - Field
       - Method
       - Found in
     * - ``author_id``
       - Remap (same as ``auth_user.id``)
       - ``CommentThread`` and ``Comment``
     * - ``title``
       - Replace
       - ``CommentThread`` only
     * - ``author_username``
       - Remap (same as ``auth_user.username``)
       - ``CommentThread`` and ``Comment``
     * - ``body``
       - Replace
       - ``CommentThread`` and ``Comment``
     * - ``votes``
       - Remap (same as ``auth_user.id``)
       - ``CommentThread`` and ``Comment``
     * - ``endorsement`` (same as ``auth_user.id``)
       - Remap
       - ``CommentThread`` only
     * - ``abuse_flaggers`` (same as ``auth_user.id``)
       - Remap
       - ``CommentThread`` only
     * - ``historical_abuse_flaggers``
       - Remap (same as ``auth_user.id``)
       - ``CommentThread`` only

For more information about how edX changes the data in these fields, see
:ref:`Data Obfuscation Methods`.

************************************
Types of Event Data in RDX Packages
************************************

RDX data packages include both explicit events and implicit events.

* Explicit events are designed to capture specific server actions and browser
  interactions. All of the events documented in the :ref:`Tracking Logs`
  section of this guide are included in RDX data packages.

* Implicit events are automatically generated. To provide information that can
  help researchers understand learner navigation sequences, RDX packages
  include implicit events that record actions in areas of the LMS that are not
  currently instrumented to generate explicit events. This section lists the
  implicit events that are included in the RDX package.

The following topics list the implicit events that are included in RDX data
packages.

.. contents::
   :local:
   :depth: 1

.. note:: Implicit events are not instrumented by edX and are subject to
 change at any time.

=====================================
Implicit Events for Course Navigation
=====================================

RDX data packages include implicit events for course navigation that begin with
these prefixes.

* ``/courses/{course_id}/jump_to_id/``
* ``/courses/{course_id}/courseware/``

Events that indicate navigation to a specific page in the LMS are also
included. These events are identified as follows, without additional trailing
characters other than a slash.

* ``/courses/{course_id}``
* ``/courses/{course_id}/info``
* ``/courses/{course_id}/progress``
* ``/courses/{course_id}/course_wiki``
* ``/courses/{course_id}/about``
* ``/courses/{course_id}/teams``
* ``/courses/{course_id}/{hex32}``, where the hex32 value is a 32-character
  (0-9, A-F) hexadecimal code.

In addition, the following events that indicate specific navigation choices in
the LMS are included.

* ``/courses/{course_id}/pdfbook/(intX)[/chapter/(intX)/[intX]]``
* ``/courses/{course_id}/wiki/`` All paths for wiki events are included with
  the exception of those that indicate actions, such as ``_preview``,
  ``_edit``, ``_create``, and ``_delete``.

=========================================
Implicit Events for Discussion Navigation
=========================================

RDX data packages include implicit events that indicate specific navigation
choices in the course discussions.

* ``/courses/{course_id}/discussion/threads/``
* ``/courses/{course_id}/discussion/comments/``
* ``/courses/{course_id}/discussion/upload``
* ``/courses/{course_id}/discussion/users``
* ``/courses/{course_id}/discussion/forum``
* ``/courses/{course_id}/discussion/{commentable_id}/threads/create``
* ``/courses/{course_id}/discussion/forum/{forum_id}/inline``
* ``/courses/{course_id}/discussion/forum/{forum_id}/search``
* ``/courses/{course_id}/discussion/forum/{forum_id}/threads``
* ``/courses/{course_id}/discussion/forum/{forum_id}/threads/{thread-id}``

Where ``commentable_id`` is ``(\w\-.)+``, ``forum_id`` is ``(\w\-.)+``,
and ``thread-id`` is ``\w+``.

*****************************
Obfuscated Data in Events
*****************************

.. contents::
   :local:
   :depth: 1

==================================
Obfuscated Data in Common Fields
==================================

The following table lists fields that can contain PII and that are common to
all events, with the obfuscation method that edX applies before the data is
included in an RDX package.

The common ``context`` field, which can contain event-specific member fields,
is described in the :ref:`context member fields<Obfuscated Data in context
Member Fields>` topic. For more information about the fields that are common to
all events, see :ref:`common`.

  .. list-table::
     :widths: 25 65
     :header-rows: 1

     * - Common Field
       - Method
     * - ``host``
       - Remove
     * - ``ip``
       - Remove
     * - ``page``
       - Remove
     * - ``referer``
       - Remove
     * - ``username``
       - Remap

For more information about how edX changes the data in these fields, see
:ref:`Data Obfuscation Methods`.

.. _Obfuscated Data in context Member Fields:

============================================
Obfuscated Data in ``context`` Member Fields
============================================

The following table lists member fields of the ``context`` field that are
obfuscated when present for any event.

  .. list-table::
     :widths: 25 65
     :header-rows: 1

     * - ``context`` Member Field
       - Method
     * - ``client``
       - Remove ``device`` or ``ip`` if present
     * - ``host``
       - Remove
     * - ``ip``
       - Remove
     * - ``path``
       - Remove
     * - ``user_id``
       - Remap
     * - ``username``
       - Remap (same as ``auth_user.username``)

For more information about how edX changes the data in these fields, see
:ref:`Data Obfuscation Methods`.

===========================================
Obfuscated Data in ``event`` Member Fields
===========================================

The following table lists member fields of the ``event`` field that are
obfuscated when present for any event.

.. note:: To search for string values to replace, the obfuscation process
  recursively traverses the entire event data structure. This table lists
  event member fields that typically include data that is removed or remapped.
  Additional event member fields can also include data that is replaced.

.. list-table::
     :widths: 25 65
     :header-rows: 1

     * - ``event`` Member Field
       - Method
     * - ``answer.file_upload_key``
       - Remove
     * - ``certificate_id``
       - Remove
     * - ``certificate_url``
       - Remove
     * - ``fileName``
       - Remove
     * - ``GET``
       - Remove
     * - ``instructor``
       - Remap (same as ``auth_user.username``)
     * - ``POST``
       - Remove
     * - ``report_url``
       - Remove
     * - ``requesting_student_id``
       - Remove
     * - ``saved_response.file_upload_key``
       - Remove
     * - ``student``
       - Remap (same as ``auth_user.username``)
     * - ``source_url``
       - Remove
     * - ``url``
       - Remove
     * - ``url_name``
       - Remove
     * - ``user``
       - Remap (same as ``auth_user.username``)
     * - ``user_id``
       - Remap (same as ``auth_user.id``)
     * - ``username``
       - Remap (same as ``auth_user.username``)

For more information about how edX changes the data in these fields, see
:ref:`Data Obfuscation Methods`.

.. include:: ../../../links/links.rst
