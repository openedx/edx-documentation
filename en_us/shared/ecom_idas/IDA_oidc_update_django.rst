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

