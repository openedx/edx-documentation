.. _Install and Start ECommerce:

############################################
Install and Start the E-Commerce Service
############################################

To install and start the edX E-Commerce service, you must complete the
following steps.

.. contents::
   :depth: 1
   :local:

.. note::
 These steps assume that you are running Open edX `devstack`_. If you prefer to
 run the E-Commerce service locally on your computer instead of on the virtual
 machine (VM) that devstack uses, see :ref:`Development Outside Devstack`.

.. _Set Up a Virtual Environment:

******************************
Set Up a Virtual Environment
******************************

#. Create or activate a Python virtual environment. You execute all of the
   commands described in this section within the virtualenv (unless otherwise
   noted).

   For more information, see `Virtual Environments`_.

#. Run the following command to install dependencies.

   .. code-block:: bash

    $ make requirements

#. (Optional) Create settings overrides that you do not commit to the
   repository. To do this, create a file named
   ``ecommerce/settings/private.py``. The ``ecommerce/settings/local.py`` file
   reads the values in this file, but Git ignores the file.

.. _Configure OIDC:

************************************************
Configure edX OpenID Connect (OIDC)
************************************************

The E-Commerce service relies on the edX `OpenID Connect`_ (OIDC)
authentication provider for login. OIDC is built on top of OAuth 2.0.
Currently, the LMS serves as the authentication provider.

To configure the E-Commerce service to work with OIDC, complete the following
procedures.

.. contents::
   :depth: 1
   :local:

.. _Create Register Client:

====================================
Create and Register a Client
====================================

To create and register a new OIDC client, follow these steps.

#. Start the LMS.
#. In your browser, go to ``http://127.0.0.1:8000/admin/oauth2/client/``.
#. Select **Add client**.
#. Leave the **User** field blank.
#. For **Client Name**, enter ``E-Commerce Service``.
#. For **URL**, enter ``http://localhost:8002/``.
#. For **Redirect URL**, enter ``https://localhost:8002/complete/edx-oidc/``.
   This is the OIDC client endpoint.

   The system automatically generates values in the **Client ID** and **Client
   Secret** fields. You use these values when you :ref:`update Django
   settings<Update Django Settings>`.

#. For **Client Type**, select **Confidential (Web applications)**.
#. Select **Save**.

====================================
Designate the Client as Trusted
====================================

After you create your client, designate it as trusted. Trusted clients
bypass the user consent form that usually appears after the system validates
the user's credentials.

To designate your client as trusted, follow these steps.

#. In your browser, go to
   ``http://127.0.0.1:8000/admin/oauth2_provider/trustedclient/add/``.
#. In the **OAuth 2.0 clients** list, select the redirect URL for the client
   that you just created.
#. Select **Save**.

.. _Update Django Settings:

====================================
Update Django Settings
====================================

To finish creating and configuring your OIDC client, add the client credentials
to the Django settings for your project.

In the ``ecommerce/settings/local.py`` file, update the following settings.

.. list-table::
   :widths: 25 60 20
   :header-rows: 1

   * - Setting
     - Description
     - Value
   * - ``SOCIAL_AUTH_EDX_OIDC_KEY``
     - OAuth 2.0 client key
     - Enter the value from the **Client ID** field in the :ref:`Create
       Register Client` section.
   * - ``SOCIAL_AUTH_EDX_OIDC_SECRET``
     - OAuth 2.0 client secret
     - Enter the value from the **Client Secret** field in the :ref:`Create
       Register Client` section.
   * - ``SOCIAL_AUTH_EDX_OIDC_URL_ROOT``
     - OAuth 2.0 authentication URL
     - Enter ``http://127.0.0.1:8000/oauth2``.
   * - ``SOCIAL_AUTH_EDX_OIDC_ID_TOKEN_DECRYPTION_KEY``
     - OIDC ID token decryption key, used to validate the ID
       token
     - Set this to the same value as ``SOCIAL_AUTH_EDX_OIDC_SECRET``.


************************************
Run Migrations and Start the Server
************************************

To complete the installation and start the E-Commerce service, follow these
steps.

.. note::
    Local installations use SQLite by default. If you use another database
    backend, make sure you update your settings and create the database, if
    necessary, before you run migrations.

#. (Devstack only) If you are using devstack, switch to the ``ecommerce`` user
   and use the ``ecommerce.settings.devstack`` settings module to run the
   following commands.

    .. code-block:: bash

      $ sudo su ecommerce
      $ make devserve

#. To run migrations, execute the following command.

   .. code-block:: bash

      $ make migrate

#. To run the server, execute the following command.

   .. code-block:: bash

     $ python manage.py runserver 8002

   .. note::
     If you use a different port, make sure you update the OIDC client by using
     the Django administration panel in the LMS. For more information about
     configuring the OIDC client, see :ref:`Configure OIDC`.



.. _Development Outside Devstack:

*******************************
Development Outside Devstack
*******************************

If you are running the LMS in `devstack`_ but would prefer to run the
E-Commerce service on your host, set up a reverse port-forward. This reverse
port-forward allows the LMS process inside your devstack to use
``127.0.0.1:8002`` to make calls to the E-Commerce service running on your
host. This simplifies LMS URL configuration.

To set up a reverse port-forward, execute the following command when you SSH
into your devstack. Make sure that you run this command on the VM host, not the
guest.

.. code-block:: bash

    $ vagrant ssh -- -R 8002:127.0.0.1:8002




.. include:: ../../../links/links.rst
