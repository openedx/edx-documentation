.. _Use Amazon S3 for Data Storage:

####################################
Use Amazon S3 for Data Storage
####################################

By default, the Open edX platform uses Amazon S3 (Simple Storage Service) for
data storage. If you need to reconfigure an instance of Open edX to use S3, you
update the ``server-vars.yml`` file in the edX platform.

.. Note::
  Before proceeding, review :ref:`Guidelines for Updating the Open edX
  Platform`.

To change your data storage configuration, you must determine the values to
use for settings the ``server-vars.yml`` file, including your storage domain
and bucket. Then, follow these steps.

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
       custom_domain:
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
       custom_domain: ""
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

#. Repeat this procedure for each instance that you want to store data on
   Amazon S3.

.. include:: ../../../links/links.rst
