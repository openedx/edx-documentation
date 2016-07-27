.. _Use Amazon S3 for Data Storage:

####################################
Using Amazon S3 for Data Storage
####################################

By default, the Open edX platform uses Amazon S3 (Simple Storage Service) for
data storage. If you need to reconfigure an instance of Open edX to use S3, you
update the ``/edx/app/edx_ansible/server-vars.yml`` file.

.. note:: Before proceeding, review :ref:`Guidelines for Updating the Open edX
  Platform`.

**************************************************
Preparing to Configure Amazon S3 for Data Storage
**************************************************

Before you change your data storage configuration, be sure to determine the
values that apply to your S3 data storage service, including the name of your
bucket.

If you want to ensure that the data you store on S3 is secure, and you plan to
use signed URLs that are valid for only a short time, be sure to set
``querystring_auth: true`` and ``default_acl: 'private'``, as shown in the
topic that follows. In addition, be sure to verify the following third-party
configuration settings.

* Files in S3 should be private.

* The signed URLs should have temporary authentication that allows private
  files to be accessed.

********************************
Use Amazon S3 for Data Storage
********************************

To configure S3 data storage, follow these steps.

#. Stop the LMS server.

#. Create or edit the ``/edx/app/edx_ansible/server-vars.yml`` file to define
   the following settings.

   Be sure to replace the example values for the settings that follow with
   values that apply to your instance.

   .. code-block:: yaml

     COMMON_OBJECT_STORE_LOG_SYNC: true
     .
     .
     .
     EDXAPP_GRADE_STORAGE_CLASS: 'storages.backends.s3boto.S3BotoStorage'
     EDXAPP_GRADE_STORAGE_KWARGS:
       bucket: 'example-student-grades'
       custom_domain: null
       locations:  '{{ COMMON_ENVIRONMENT }}-{{ COMMON_DEPLOYMENT }}'
       querystring_expire: 300
       gzip: true
       querystring_auth: true
       default_acl: 'private'
     .
     .
     .
     EDXAPP_VERIFY_STUDENT:
       DAYS_GOOD_FOR: 365
       SOFTWARE_SECURE:
         STORAGE_CLASS: "storages.example.s3.S3Storage"
         STORAGE_KWARGS:
           bucket: "example-certs-test"
           custom_domain: null
           querystring_expire: 432000
           querystring_auth: true
           default_acl: 'private'
     .
     .
     .
     ENABLE_GRADE_DOWNLOADS: true

#. Run the ``/edx/bin/update`` command.

   .. code-block:: bash

      sudo /edx/bin/update edx-platform <your-branch-name>

#. Restart the LMS server.

#. Repeat this procedure for each instance that has data that you want to store
   on Amazon S3.

.. include:: ../../../links/links.rst
