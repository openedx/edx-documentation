.. _Retrieving RDX Packages:

########################
Retrieving RDX Packages
########################

Data czars retrieve RDX packages from AWS. The procedures for downloading RDX
data packages and extracting their contents is similar to the procedures you
follow for your organization's data packages.

The topics in this section describe the differences between RDX packages and
organizational data packages.

.. contents::
   :local:
   :depth: 2

For more information about downloading and extracting your organizational data
packages, see :ref:`Package`.

.. _RDX Package Identifiers:

***************************
Identifying an RDX Package
***************************

When researchers propose projects that require RDX data, they request data
either for specific courses or for courses that meet specified criteria. EdX
identifies courses that meet these specifications and, on approval, assigns an
RDX request ID to the project.

EdX provides a single RDX data package for each approved project. The RDX
package contains all of the data files, after the :ref:`data obfuscation
procedures<Data Obfuscation Procedures for RDX>` are applied, for all of the
courses in the project. On AWS, data czars can identify the RDX packages by
request ID.

.. _Amazon S3 Buckets and Directories for RDX Data:

********************************************
Locating RDX Data on Amazon S3
********************************************

EdX uploads RDX data packages to an Amazon S3
``s3://edx-course-data/{org}/rdx/{requestID}`` folder. This folder contains
one ``{org}_{course}_{run}.tar.gz.gpg`` file for each of the requested courses.

The ``{org}_{course}_{run}.tar.gz.gpg`` file contains data and event files for
the requested time period in the course's history.

.. _Download an RDX Package from Amazon S3:

*******************************************
Download an RDX Package from Amazon S3
*******************************************

Only the data czar at a participating partner institution can download an RDX
data package.

To download an RDX data package from the Amazon S3 storage service, follow
these steps.

.. note:: If you are using a third party tool to connect to Amazon S3, you
    might not be able to navigate directly from the bucket that contains your
    own organization's data to the bucket for RDX data. You might need to
    disconnect from Amazon S3 and then reconnect to the RDX destination.

#. Use the AWS Command Line Interface or a third party tool to connect to the
   ``s3://edx-course-data/`` folder on Amazon S3.

   For information about providing your credentials to connect to Amazon S3,
   see :ref:`Access Amazon S3`.

#. Navigate to the RDX folder for a specific research project. The RDX data
   package is located in the ``s3://edx-course-data/{org}/rdx/{requestID}``
   folder.

#. Download the compressed, encrypted ``{org}_{course}_{run}.tar.gz.gpg`` file
   for each of the courses in the project.


*********************************************************
Extract the ``{org}_{course}_{run}.tar.gz.gpg`` File
*********************************************************

After you download each of the ``{org}_{course}_{run}.tar.gz.gpg`` files for an
RDX research project, you complete these tasks. You repeat this process for
each ``{org}_{course}_{run}.tar.gz.gpg`` file in the RDX package.

#. Use your private key to decrypt the file. The result is a file named
   ``{org}_{course}_{run}.tar.gz``. See :ref:`Decrypt an Encrypted File`.

#. Use the gunzip command to expand the .gz file. The result is a file named
   ``{org}_{course}_{run}.tar``.

#. Extract the .tar file. The result of this decryption and extraction process
   is a ``metadata_file.json`` file and a set of folders that contain the event
   and state data for the requested time period. The file and folder hierarchy
   follows this pattern.

   ::

      metadata_file.json
        /events
          {org}_{course}_{run}-events-CCYY-MM-dd.log.gz
          ...
        /state
          /CCYY-MM-dd
            {org}_{course}_{run}-{suffix}
            ...

   The ``metadata_file.json`` file provides information about the version of
   the edX analytics pipeline that was in use when edX obfuscated PII and other
   sensitive values in the package.
