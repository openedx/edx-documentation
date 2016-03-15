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

.. _Designate the Client as Trusted:

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

.. include:: ../../../links/links.rst
