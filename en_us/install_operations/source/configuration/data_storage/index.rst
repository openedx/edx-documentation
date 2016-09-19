.. _Configuring Data Storage:

===========================
Configuring Data Storage
===========================

The Open edX platform uses cloud storage to store and retrieve data for the
following system features and requirements.

* The default django-storages location.

* :ref:`opencoursestaff:Grade reports<Access_grades>` generated from the LMS
  instructor dashboard.

* Identity verification for a proctoring vendor.

  .. note:: Open edX sites can enable the proctoring feature as designed for
   use on the edx.org website, but its use is not supported.

By default, the Open edX platform is configured to use Amazon S3 (Simple
Storage Service) for data storage. You can change the configuration of your
Open edX instances to use Swift (the OpenStack Object Store project) instead of
S3 for data storage.

.. toctree::
   :maxdepth: 1

   data_storage_swift
   data_storage_s3

