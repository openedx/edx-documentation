.. _Use Swift for Data Storage:

####################################
Use Swift for Data Storage
####################################

To change the default configuration of an Open edX instance to use Swift (the
OpenStack Object Store project) for data storage, you update the
``/edx/app/edx_ansible/server-vars.yml`` file.

.. Note::
  Before proceeding, review :ref:`Guidelines for Updating the Open edX
  Platform`.

Before you change your data storage configuration, be sure to determine the
values that apply to your Swift data storage service, including the name of
your bucket. Then, follow these steps.

.. if bucket applies ^^

#. Stop the LMS server.

#. Create or edit the ``/edx/app/edx_ansible/server-vars.yml`` file to define
   the following settings.

   Be sure to replace the example values for the settings that follow with
   values that apply to your instance.

.. Braden or other OpenCraft SME, please let me know what the actual KWARGS for Swift are (below I've included the S3 ones as placeholders).

   .. code-block:: yaml

     COMMON_OBJECT_STORE_LOG_SYNC: true
     .
     .
     .
     EDXAPP_GRADE_STORAGE_CLASS: 'swift.storage.SwiftStorage'
     EDXAPP_GRADE_STORAGE_KWARGS:
       bucket: 'example-student-grades'
       custom_domain: null
       locations:  '{{ COMMON_ENVIRONMENT }}-{{ COMMON_DEPLOYMENT }}'
       querystring_expire: 300
       gzip: true
     .
     .
     .
     EDXAPP_VERIFY_STUDENT:
       DAYS_GOOD_FOR: 365
       SOFTWARE_SECURE:
     STORAGE_CLASS: "swift.storage.SwiftStorage"
     STORAGE_KWARGS:
       bucket: "example-certs-test"
       custom_domain: null
       querystring_expire: 432000
     .
     .
     .
     ENABLE_GRADE_DOWNLOADS: true

#. Run the ``/edx/bin/update`` command.

   .. code-block:: bash

      sudo /edx/bin/update edx-platform <your-branch-name>

#. Restart the LMS server.

#. Repeat this procedure for each instance that has data that you want to store
   on Swift.

.. include:: ../../../links/links.rst
