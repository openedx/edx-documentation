.. _Package:

######################################
Data Delivered in Data Packages
######################################

For partners who are running courses on edx.org and edge.edx.org, edX regularly
makes research data available for download from the Amazon S3 storage service.
The *data package* that data czars download from Amazon S3 consists of a set of
compressed and encrypted files that contain event logs and database snapshots
for all of their organizations' edx.org and edge.edx.org courses.

.. contents::
   :local:
   :depth: 1

Course-specific data is also available to the members of individual course
teams. Users who are assigned the Admin or Staff role for the course can view
and download data from the Instructor Dashboard in their live courses and from
edX Insights. The data available to course teams from these applications is a
subset of the data available in the data packages. For more information, see
:ref:`partnercoursestaff:document index` and :ref:`insights:Overview`.

.. _Data Package Files:

**********************
Data Package Files
**********************

A data package consists of different files that contain event data and database
data. 

.. note:: In all file names, the date is in {YYYY}-{MM}-{DD} format.

You download these files from different Amazon S3 "buckets" and folders. See
:ref:`Amazon S3 Buckets and Directories`.

============
Event Data
============

The ``{org}-{site}-events-{date}.log.gz.gpg`` file contains a daily log of
course events. A separate file is available for courses running on edge.edx.org
(with "edge" for {site} in the file name) and on edx.org (with "prod" for
{site}).

For a partner organization named UniversityX, these daily files are identified
by the organization name, the edX site name, and the date. For example,
``universityx-edge-events-2014-07-25.log.gz.gpg``.

Each of these compressed files can range in size from hundreds of kilobytes to
tens of megabytes. When you extract a compressed file, it is approximately 20
times larger. As a result, multiple gigabytes of space might be needed to store
the tracking logs for a year.

For information about the contents of these files, see :ref:`Data Package
Contents`.

==================
Database Data
==================

The ``{org}-{date}.zip`` file contains views on database tables. This file
includes data as of the time of the export, for all of an organization's
courses on both the edx.org and edge.edx.org. sites. A new file is available
every week, representing the database at that point in time.

For a partner organization named UniversityX, each weekly file is identified by
the organization name and its extraction date: for example,
``universityx-2013-10-27.zip``.

Compressed, these files can range in size from hundreds of megabytes to tens of
gigabytes in size. When you extract a compressed file, it is approximately 20
times larger. As a result, institutions that receive data for several courses
for several years might require from tens to hundreds of gigabytes of space for
data storage.

For information about the contents of this file, see :ref:`Data Package
Contents`.

.. _Amazon S3 Buckets and Directories:

********************************************
Amazon S3 Buckets and Folders
********************************************

Data package files are located at the following Amazon S3 destinations:

* The **s3://edx-course-data/{org}** folder contains the daily
  ``{org}-{site}-events-{date}.log.gz.gpg`` files of course event data.
  
* The **s3://course-data** bucket contains the weekly ``{org}-{date}.zip``
  database snapshot.

For information about accessing Amazon S3, see :ref:`Access Amazon S3`.

.. _Download Data Packages from Amazon S3:

****************************************************************
Download Data Packages from Amazon S3
****************************************************************

You download the files in your data package from the Amazon S3 storage
service.

==========================
Download Daily Event Files
==========================

#. To download daily event files, use the AWS Command Line Interface or a
   third-party tool to connect to the **s3://edx-course-data/{org}** folder on
   Amazon S3.

   For information about providing your credentials to connect to Amazon S3,
   see :ref:`Access Amazon S3`.

#. Navigate within **s3://edx-course-data/{org}** to locate the files that you
   want:

   ``{org}/{site}/events/{year}``

   The event logs in the ``{year}`` folder are in compressed, encrypted
   files named ``{org}-{site}-events-{date}.log.gz.gpg``.

3. Download the ``{org}-{site}-events-{date}.log.gz.gpg`` file.

   If your organization has courses running on both edx.org and edge.edx.org,
   separate log files are available for the "prod" site and the "edge" site.
   Repeat this step to download the file for the other site.

==============================
Download Weekly Database Files
==============================

.. note:: If you are using a third-party tool to connect to Amazon S3, you
    might not be able to navigate directly between the **s3://course-data**
    bucket and the **s3://edx-course-data/{org}** folder. You might need to
    disconnect from Amazon S3 and then reconnect to the other destination.

#. To download a weekly database data file, connect to the edX 
   **s3://course-data** bucket on Amazon S3 using the AWS Command Line 
   Interface or a third-party tool.

   For information about providing your credentials to connect to Amazon S3,
   see :ref:`Access Amazon S3`.

2. Download the ``{org}-{date}.zip`` database data file from the 
   **s3://course-data** bucket.


.. _Data Package Contents:

**********************
Data Package Contents
**********************

Each of the files you download contains one or more files of research data.

================================================================
Extracted Contents of ``{org}-{site}-events-{date}.log.gz.gpg``
================================================================

The ``{org}-{site}-events-{date}.log.gz.gpg`` file contains all event data for
courses on a single edX site for one 24-hour period. After you download a
``{org}-{site}-events-{date}.log.gz.gpg`` file for your institution, you:

#. Use your private key to decrypt the file. See :ref:`Decrypt an Encrypted
   File`.

#. Extract the log file from the compressed .gz file. The result is a single
   file named ``{org}-{site}-events-{date}.log``. (Alternatively, the data can
   be decompressed in stream using a tool such as gzip.)

For more information about the events in this file, see :ref:`Tracking Logs`.

============================================
Extracted Contents of ``{org}-{date}.zip``
============================================

After you download the ``{org}-{date}.zip`` file for your
institution, you:

#. Extract the contents of the file. When you extract (or unzip) this file, all
   of the files that it contains are placed in the same directory. All of the
   extracted files end in ``.gpg``, which indicates that they are encrypted.

#. Use your private key to decrypt the extracted files. See
   :ref:`Decrypt an Encrypted File`.

The result of extracting and decrypting the ``{org}-{date}.zip`` file is the
following set of .sql, .csv, and .mongo files. Note that the .sql files are
tab separated.

``{org}-{course}-{date}-auth_user-{site}-analytics.sql``

  Information about the users who are authorized to access the course. See
  :ref:`auth_user`.

``{org}-{course}-{date}-auth_userprofile-{site}-analytics.sql``

  Demographic data provided by users during site registration. See
  :ref:`auth_userprofile`.

``{org}-{course}-{date}-certificates_generatedcertificate-{site}-analytics.sql``

  The final grade and certificate status for students (populated after course
  completion). See :ref:`certificates_generatedcertificate`.

``{org}-{course}-{date}-course_structure-{site}-analytics.json``

  This file documents the structure of a course at a point in time. The file
  includes data for the course, including important dates, pages, and course-
  wide discussion topics. It also identifies each item of course content
  defined in the course outline. A separate file is included for each course
  on the site. For more information, see :ref:`course_structure`.

``{org}-{course}-{date}-courseware_studentmodule-{site}-analytics.sql``

  The courseware state for each student, with a separate row for each item in
  the course content that the student accesses. No file is produced for courses
  that do not have any records in this table (for example, recently created
  courses). See :ref:`courseware_studentmodule`.

``{org}-email_opt_in-{site}-analytics.csv``

  This file reports the email preference selected by students who are enrolled
  in any of your institution's courses. See :ref:`Institution_Data`.

``{org}-{course}-{date}-student_courseenrollment-{site}-analytics.sql``

  The enrollment status and type of enrollment selected by each student in the
  course. See :ref:`student_courseenrollment`.

``{org}-{course}-{date}-user_api_usercoursetag-{site}-analytics.sql``

  Metadata that describes different types of student participation in the
  course. See :ref:`user_api_usercoursetag`.

``{org}-{course}-{date}-user_id_map-{site}-analytics.sql``

   A mapping of user IDs to site-wide obfuscated IDs. See :ref:`user_id_map`.

``{org}-{course}-{date}-{site}.mongo``

  The content and characteristics of course discussion interactions. See
  :ref:`Discussion Forums Data`.

``{org}-{course}-{date}-wiki_article-{site}-analytics.sql``

  Information about the articles added to the course wiki. See
  :ref:`wiki_article`.

``{org}-{course}-{date}-wiki_articlerevision-{site}-analytics.sql``

  Changes and deletions affecting course wiki articles. See
  :ref:`wiki_articlerevision`.


.. include:: ../../../links/links.rst
