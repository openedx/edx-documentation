.. _Configure Amazon S3 Storage:

************************************
Configure Amazon S3 Storage
************************************

When you deploy the credentials on a staging or production server, you must change the settings to use the Amazon S3 storage backend instead of Django's default file storage backend (``django.core.files.storage.FileSystemStorage``) so that you do not commit changes to the repository.

To change the settings, SSH into the system, and then update the :file:`/edx/etc/credentials.yml` file. This file's values are read by :file:`credentials/settings/production.py`, but ignored by Git.

The following example shows how to use the Amazon S3 storage backend:

::

  AWS_STORAGE_BUCKET_NAME: credentials-s3-bucket-name
  AWS_ACCESS_KEY_ID: AAAAAAAAAAAAAAA
  AWS_SECRET_ACCESS_KEY: BBBBBBBBBBBBBBBBBBBB
  AWS_DEFAULT_ACL: ''

Amazon S3 storage backend: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html
