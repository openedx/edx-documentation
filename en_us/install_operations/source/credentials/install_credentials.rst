.. _Install and Start Credentials:

############################################
Install and Start the Credentials Service
############################################

To install and start the edX Credentials service, you must complete the
following steps.

.. contents::
   :depth: 1
   :local:


.. _Credentials Set Up a Virtual Environment:

******************************
Set Up a Virtual Environment
******************************

.. include:: ../../../shared/ecom_idas/IDA_virtualenv.rst



.. _Credentials Configure Amazon S3 Storage:

************************************
Configure Amazon S3 Storage
************************************

When you deploy the Credentials service on a staging or production server, you
must change the server's settings to use the `Amazon S3 storage backend`_
instead of Django's default file storage backend
(``django.core.files.storage.FileSystemStorage``) so that you do not commit
changes to the repository.

To change the settings, SSH into the system, and then update the
``/edx/etc/credentials.yml`` file. The ``credentials/settings/production.py``
reads the values in this file, but Git ignores them.

The following example shows how to use the Amazon S3 storage backend:

.. code-block:: bash

  AWS_STORAGE_BUCKET_NAME: credentials-s3-bucket-name
  AWS_ACCESS_KEY_ID: AAAAAAAAAAAAAAA
  AWS_SECRET_ACCESS_KEY: BBBBBBBBBBBBBBBBBBBB
  AWS_DEFAULT_ACL: ''


.. _Credentials Configure OIDC:

************************************
Configure edX OpenID Connect (OIDC)
************************************

.. include:: ../../../shared/ecom_idas/IDA_oidc.rst


.. _Credentials Create Register Client:

====================================
Create and Register a Client
====================================

.. include:: ../../../shared/ecom_idas/IDA_oidc_create_client.rst


.. _Credentials Designate the Client as Trusted:

====================================
Designate the Client as Trusted
====================================

.. include:: ../../../shared/ecom_idas/IDA_oidc_designate_trusted.rst


.. _Credentials Update Django Settings:

====================================
Update Django Settings
====================================

.. include:: ../../../shared/ecom_idas/IDA_oidc_update_django.rst


.. _Credentials Verify Service User:

************************************
Verify the Service User Account
************************************

The Open edX Credentials service must communicate with other Open edX services,
such as the LMS or Platform services. Because certificates are publicly
accessible, edX provides a “Credentials service user” account that uses JSON
Web Token (JWT) authentication to communicate between the Credentials service
and other Open edX services. The Credentials service user makes requests on
behalf of the Credentials service to access required APIs and fetch data. The
Credentials service user is only available for internal use in Open edX
services.

By default, the username for the Credentials service user is
``credentials_service_user``. You can change the username of the Credentials
service user in the ``CREDENTIALS_SERVICE_USER`` configuration setting.
However, the Credentials service assumes that a service user named
``credentials_service_user`` is present in all needed services.

The Credentials service user must have the following characteristics.

* The service user must have the Admin role.
* The service user must have a password that is very difficult to guess so that
  the account cannot be accessed from web interfaces.
* The service user must be available in all of the services that the
  Credentials service must communicate with if these services do not require
  real user names.

.. _Credentials Run Migrations and Start the Service:

*************************************
Run Migrations and Start the Service
*************************************

.. include:: ../../../shared/ecom_idas/IDA_start_service.rst

   .. note::
     If you use a different port, make sure you update the OIDC client by using
     the Django administration panel in the LMS. For more information about
     configuring the OIDC client, see :ref:`Credentials Configure OIDC`.


.. include:: ../../../links/links.rst
