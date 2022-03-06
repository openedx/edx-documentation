.. _Integrating with an OAuth2 Identity Provider:

###############################################
Integrating with an OAuth2 Identity Provider
###############################################

Open edX has specific instructions for Google, Facebook, LinkedIn, and Azure
Active Directory. For more information about how to set up one or more of these
integrations, see :ref:`Common OAuth2 Providers`.

The system also supports integrations with alternative OAuth2 providers. For
more information, see :ref:`Additional Providers`.

.. _Common OAuth2 Providers:

****************************
Common OAuth2 Providers
****************************

Integrating with the most common OAuth2 IdPs has several steps.

#. :ref:`Register the Open edX instance with the provider<Register the Open edX
   Instance>`.
#. :ref:`Configure Open edX<OAuth2 Configure Open edX>`.
#. :ref:`Add the provider configuration<Add the Provider Configuration>`.


.. _Register the Open edX Instance:

==============================
Register the Open edX Instance
==============================

The most common OAuth2 providers are Google, Facebook, LinkedIn, and Azure
Active Directory.

.. contents::
   :local:
   :depth: 1

Register the Open edX Instance with Google
******************************************

The following instructions describe how to configure Google as a third party
authentication provider so that users can use Google accounts (which includes
Google Apps accounts) to sign in. These are based on the official Google
instructions.

#. Obtain credentials to access the Google API. To do this, follow the
   `official Google instructions`_ to go to the `Google Developers Console`_,
   create a new project, and enable the Google+ API service.

#. In the Google Developers Console, select **API Manager**, and then select
   **OAuth Consent Screen**.

#. For **Product name shown to users** enter the name of your Open edX instance
   (for example, "Example Academy Online").

#. Select **Save**.

#. Select the **Credentials** tab, select **Create credentials**, and then
   select **OAuth client ID**.

   * For **Application type**, select **Web application**.
   * Leave the **Authorized JavaScript origins** field blank.
   * For **Authorized redirect URIs**, enter ``<Open edX instance
     domain>/auth/complete/google-oauth2/``. For example, for devstack, enter
     ``http://localhost:8000/auth/complete/google-oauth2/``.
   * Select **Create** to finish creating the credentials.

#. After you obtain the credentials, note the client ID and the client secret.

Register the Open edX Instance with Facebook
********************************************

To create the app in the Facebook developer portal, follow these steps.

#. Sign in to Facebook, then go to the `Facebook for Developers`_ page.

#. Select **Add a New App**, and then select **Website**.

#. Enter a name for the app, and then select **Create New Facebook App ID**.

#. Enter your information in the rest of the fields in the app creation
   process.

#. Under **Quick Start for Website**, select **Skip Quick Start**.

   You are now at the developer console page for the new Facebook app.

#. Select **Settings**, and note the **App ID** and **App Secret**.

#. On the **Settings** page, select **Add Platform**, and then select
   **Website**.

#. For **Site URL**, enter the URL of your Open edX instance (for example,
   ``<http://localhost:8000/>`` for devstack).

#. In the **App Domains** field, enter the domain name from this URL (for
   example, ``localhost``).

#. Select **Save Changes**.

#. Under **Products** -> **Facebook Login** -> **Settings** ->
   **Authorized redirect URIs**, enter ``<Open edX instance
   domain>/auth/complete/facebook/``. For example, for devstack, enter
   ``http://localhost:8000/auth/complete/facebook/``.

#. Select **Save Changes**.

Register the Open edX Instance with LinkedIn
********************************************

To create the LinkedIn app, follow these steps.

#. Go to the `LinkedIn Developers`_ page.

#. Click **Create Application**, enter your information in the form, and then
   submit the form.

#. On the page that opens with information about the app, note the **Client
   ID** and **Client Secret**.

#. In the **OAuth 2.0** section, for **Authorized Redirect URL**, enter ``<Open
   edX instance domain>/auth/complete/linkedin-oauth2/``. For example, for
   devstack, enter ``http://localhost:8000/auth/complete/linkedin-oauth2/``.

#. Select **Update** to save your information.

Register the Open edX Instance with Azure Active Directory
**********************************************************

You can use Azure Active Directory to allow users with Microsoft Office 365
Business accounts to sign in to Open edX. Note that this feature currently does
not work with other types of Microsoft accounts (such as "@live.com" or
"@hotmail.com" accounts).

#. If you do not have a Microsoft account, create one on the `Microsoft sign in`_ page.

#. If you do not have an Azure subscription, create one on the `Azure account
   creation`_ page.

   .. note::
    You must enter a credit card on this page, but if you do not create any
    virtual machines or other services besides Azure AD, you will not be
    charged.

#. Go to the `Azure sign in`_ page.

#. Click **New**, locate **Active Directory**, and then select **Create**.

#. Enter a name, domain name, and country.

#. Create a new application.

   #. Find the new Active Directory in the portal, select **Applications**,
      select **Add**, and then select **Add an application my organization is
      developing**.

   #. Enter a name for the app, and then select **Web Application**.

   #. For **Sign-on URL**, enter ``<LMS URI>/auth/complete/azuread-oauth2/``.
      For example, you might enter
      ``http://localhost:8000/auth/complete/azuread-oauth2/``.

   #. For **App ID URL**, enter ``<LMS URI>/sign in``. For example, you might
      enter ``http://localhost:8000/sign in``.

   #. Finish creating the new app.

#. In the portal, locate your Azure AD application, click **Configure**, and
   then locate and make a note of the client ID. For example, the client ID may
   be ``fe3c3868-0faa-44ee-a1bf-1110aeab1a65``.

#. In the **Keys** section, select a two-year duration, and then select
   **Save** to create a secret key. Note the value of the key. For example, the
   key-value may be ``abcdef12341yHlmOrR8D3vlV1cD2VtL7k9xk9DSB8vw=``.

#. In the **Permissions to other applications** section, locate the **Delegated
   Permissions** option for Windows Azure Active Directory, and then select
   **Sign in and read user profile**.

#. Verify the Azure AD domain name. To do this, follow these steps.

   #. In the portal, locate the new Active Directory.

   #. Select **Domains**, select **Add**, and then add the root domain you want
      to use (for example, ``edx.org``). Make sure that you add the root domain
      first, and then follow the TXT record verification process.

   #. (optional) After the domain has been verified, add subdomains (for
      example, ``courses.edx.org``). Subdomains also request verification, but
      do not need it.

#. In the Active Directory, select **Applications**, and then select the
   application that you created.

#. Enable **multi-tenant** support.


.. _OAuth2 Configure Open edX:

======================
Configure Open edX
======================

Configuring Open edX is very similar for Google, Facebook, LinkedIn, and Azure.

#. In the ``lms.yml`` file, change the value of ``FEATURES`` >
   ``ENABLE_THIRD_PARTY_AUTH`` to ``true`` (it is ``false`` by default).

#. If necessary, make sure that the correct backend is specified.

   * If you are using Google, Facebook, LinkedIn, or Active Directory, open the
     ``lms.yml`` file and look for the ``THIRD_PARTY_AUTH_BACKENDS`` list.
     By default, the file does not contain this list.

     If the ``lms.yml`` file does not contain the
     ``THIRD_PARTY_AUTH_BACKENDS`` list, you do not have to complete any
     additional steps.

     If the ``lms.yml`` file contains the ``THIRD_PARTY_AUTH_BACKENDS``
     list, add the backend for the applicable IdP to the list.

       * For Google, add ``"social_core.backends.google.GoogleOAuth2"``.

       * For Facebook, add ``"social_core.backends.facebook.FacebookOAuth2"``.

       * For LinkedIn, add ``"social_core.backends.linkedin.LinkedinOAuth2"``.

       * For Azure Active Directory, add
          ``"social_core.backends.azuread.AzureADOAuth2"``.

   * If you are using a custom backend, add the applicable OAuth2 provider to
     the ``THIRD_PARTY_AUTH_BACKENDS`` list in the ``lms.yml`` file. If
     the file does not contain the ``THIRD_PARTY_AUTH_BACKENDS`` list, create
     the list, and then add the OAuth2 provider.

   For more information, see the `AWS template file`_ file in GitHub.

#. In the ``lms.yml`` file, add the client secret. To do this, create the
   ``SOCIAL_AUTH_OAUTH_SECRETS`` key if the key does not already exist, and
   then add the appropriate value for your IdP.

   .. note::
      If you are using Ansible, set the ``EDXAPP_SOCIAL_AUTH_OAUTH_SECRETS``
      variable.

   * For Google, add the following value.

     .. code-block:: none

        "SOCIAL_AUTH_OAUTH_SECRETS": { "google-oauth2":
           "abcdef123456789101112131" }

   * For Facebook, add the following value.

     .. code-block:: none

        "SOCIAL_AUTH_OAUTH_SECRETS": {
           "facebook": "98765432181bbe3a2596efa8ba7abcde"
        }

   * For LinkedIn, add the following value.

     .. code-block:: none

      "SOCIAL_AUTH_OAUTH_SECRETS": { "linkedin-oauth2": "4D3Cb2aB1C0dEFGH" }

   * For Azure, add the following value.

     .. code-block:: none

      "SOCIAL_AUTH_OAUTH_SECRETS": { "azuread-oauth2":
          "abcdef12341yHlmOrR8D3vlV1cD2VtL7k9xk9DSB8vw=" }

#. Restart the LMS server so that it will use the new settings.

.. _Add the Provider Configuration:

==============================
Add the Provider Configuration
==============================

#. Go to ``<LMS URI>/admin/third_party_auth/oauth2providerconfig/``. For
   example, on devstack, go to
   ``http://localhost:8000/admin/third_party_auth/oauth2providerconfig/``.

#. Select **Add Provider Configuration (OAuth)**.

#. Make sure that **Enabled** is selected.

#. Make sure that **Visible** is selected.

#. For **Icon Class**, enter the appropriate value.

   * For Google, enter ``fa-google-plus``.

   * For Facebook, enter ``fa-facebook``.

   * For LinkedIn, enter ``fa-linkedin``.

   * For Azure, leave the field blank.

#. For **Name**, enter the appropriate value.

   * For Google, enter ``Google``.

   * For Facebook, enter ``Facebook``.

   * For LinkedIn, enter ``LinkedIn``.

   * For Azure, enter ``Microsoft``.

#. For **Backend Name**, select the appropriate value.

   * For Google, select **google-oauth2**.

   * For Facebook, select **facebook**.

   * For LinkedIn, select **linkedin-oauth2**.

   * For Azure, select **azuread-oauth2**.

   .. note::
     If the value does not appear in the list, either the
     ``ENABLE_THIRD_PARTY_AUTH`` setting or the ``THIRD_PARTY_AUTH_BACKENDS``
     setting is not configured correctly.

#. For **Client ID**, enter the client ID that you noted earlier.

#. Leave **Client Secret** blank. Open edX sets the secret through
   ``lms.yml``, which is more secure.

#. (Optional) If you want Facebook or LinkedIn to provide the user's email
   address during registration, enter the following code into **Other
   settings**.

   For Facebook, use this code.

    .. code-block:: none

        {
            "SCOPE": ["email"],
            "PROFILE_EXTRA_PARAMS": {
                "fields": "id, name, email"
            }
        }

   For LinkedIn, use this code.

    .. code-block:: none

        { "SCOPE": ["r_basicprofile", "r_emailaddress"], "FIELD_SELECTORS":
         ["email-address"] }


#. Select **Save**.

Users who have an account with the IdP that you have configured can now sign
in.

.. note::

  For Google only, if you see the following error message, the
  ``SOCIAL_AUTH_OAUTH_SECRETS`` setting is not correct.

   ``'unicode' object has no attribute 'get'``

  To resolve this problem, make sure that this setting does not appear multiple
  times in the ``lms.yml`` file.

.. _Additional Providers:

**************************************
Additional OAuth2 Providers (Advanced)
**************************************

You can add any other third party authentication provider that supports the
OAuth2 standard to the Open edX platform. To do this, follow these steps.

.. note::
 OAuth1 providers are also supported and can be configured using these same
 steps. However, OAuth2 is preferred over OAuth1 wherever possible.

#. In ``lms.yml``, change the value of ``FEATURES`` >
   ``ENABLE_THIRD_PARTY_AUTH`` to ``true`` (it is ``false`` by default).

#. Install the python-social-auth authentication backend specific to
   that provider, and determine the python module path of the backend.

   * If the provider is a `python-social-auth supported backend`_, the backend
     is already installed.

     To determine the python module path of the backend, locate the backend in
     the `list of python-social-auth backends`_, open the file for the backend,
     and locate the name of the class. The python module path is of the format
     ``social_core.backends.<file name>.<class name>``.

     For example, for GitHub, the file is ``github.py`` and the class in that
     file is ``GithubOAuth2``. The backend module path is therefore
     ``social_core.backends.github.GithubOAuth2``.

   * If the provider is not a python-social-auth supported backend, you must
     create a new Python package that includes the code required to implement
     the backend. Your python package must contain a module with a class that
     subclasses ``social_core.backends.oauth.BaseOAuth2``. For more information, see
     the `python-social-auth documentation`_, or see the code of the fully
     supported backends (such as Google or Facebook) for examples.

#. Enable the python-social-auth authentication backend specific to that
   provider:

   #. In the ``THIRD_PARTY_AUTH_BACKENDS`` setting in ``lms.yml``, add the
      full path of the module to the list.

   #. (optional) Set the value of ``THIRD_PARTY_AUTH_BACKENDS`` to match `the
      default value in the aws.py file`_, and then add any additional backends
      you need.

#. Obtain a client ID and client secret from the provider.

#. Add the client secret to ``lms.yml``. To do this, create a new key
   called ``SOCIAL_AUTH_OAUTH_SECRETS`` if it doesn't already exist, and then
   add the backend name to that key as follows.

    .. code-block:: none

        "SOCIAL_AUTH_OAUTH_SECRETS": { "backend-name": "secret" }

   If you are using Ansible, the variable to set is called
   ``EDXAPP_SOCIAL_AUTH_OAUTH_SECRETS``.

#. Restart the LMS server so that it will use the new settings.

#. Go to ``<LMS URI>/admin/third_party_auth/oauth2providerconfig/``. For
   example, on devstack, go to
   ``http://localhost:8000/admin/third_party_auth/oauth2providerconfig/``.

#. Select **Add Provider Configuration (OAuth)**.

#. Make sure that **Enabled** is selected.

#. Make sure that **Visible** is selected.

#. For **Icon Class**, select one of the following options.

   * Use a generic icon by entering ``fa-sign-in``.

   * Use a relevant Font Awesome icon.

   * Upload an SVG icon using the **Icon Image** field.

#. For **Name**, enter the name of the provider.

#. For **Backend Name**, select the backend name from the list. (If it does not
   appear in the list, either the ``ENABLE_THIRD_PARTY_AUTH`` setting or the
   ``THIRD_PARTY_AUTH_BACKENDS`` setting is not configured correctly.)

#. For **Client ID**, enter the client ID that you noted earlier.

#. Leave **Client Secret** blank. Open edX sets the secret through
   ``lms.yml``, which is more secure.

#. Select **Save**.

Users can now sign in using this OAuth2 provider.



.. include:: ../../../../../links/links.rst
