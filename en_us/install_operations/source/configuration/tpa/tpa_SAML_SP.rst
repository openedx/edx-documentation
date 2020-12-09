.. _Configuring your Installation as a SAML Service Provider:

###############################################################
Configuring your Open edX Site as a SAML Service Provider
###############################################################

The first step in configuring your Open edX site to act as a SAML SP is
to create a credential key pair to ensure secure data transfers with identity
providers. To complete the configuration procedure, you configure your Open edX
site as a SAML SP, which creates your metadata XML file.

.. contents::
   :local:
   :depth: 1

After you complete this configuration, you can share your metadata file with
SAML identity providers, and configure them to assert identity and access
rights for users to your installation. For more information, see
:ref:`Integrating with a SAML Identity Provider`.

**********************************************
Generate Public and Private Keys
**********************************************

To generate the keys for your Open edX installation, follow these steps.

#. On your local computer or on the server, open Terminal or a Command Prompt
   and run the following command.

   ``openssl req -new -x509 -days 3652 -nodes -out saml.crt -keyout saml.key``

#. Provide information at each prompt.

Two files, ``saml.crt`` and ``saml.key``, are created in the directory where
you ran the command.

.. _Add Keys to the LMS Configuration File:

**************************************************
Add Keys to the LMS Configuration File
**************************************************

.. note:: Configuration settings added to the ``lms.yml`` file are reset
 to their default values when you use Ansible to update edx-platform.

To configure an Open edX site with your public and private SAML keys, follow
these steps.

#. Open the ``edx/app/edxapp/lms.yml`` file in your text editor.

#. In the root of the JSON, add the ``SOCIAL_AUTH_SAML_SP_PUBLIC_CERT`` key
   followed by a colon (:), a space, and an empty string where you'll paste the
   escaped certificate.

   .. code:: json

    "SOCIAL_AUTH_SAML_SP_PUBLIC_CERT": "",

#. Open the ``saml.crt`` file, copy its entire contents, and then paste them
   inside the quotes after the ``SOCIAL_AUTH_SAML_SP_PUBLIC_CERT`` parameter.
   Replace all newlines with `\n`.

   .. code:: json

    "SOCIAL_AUTH_SAML_SP_PUBLIC_CERT": "-----BEGIN CERTIFICATE-----\nSWP6P/C1ypaYkmS...j9+hjvbBf3szk=\n-----END CERTIFICATE-----\n"

#. Add the ``SOCIAL_AUTH_SAML_SP_PRIVATE_KEY`` key followed by a colon
   (:), a space, and an empty string where you'll paste the escaped key.

   .. code:: json

    "SOCIAL_AUTH_SAML_SP_PUBLIC_CERT": "-----BEGIN CERTIFICATE-----\nSWP6P/C1ypaYkmS...j9+hjvbBf3szk=\n-----END CERTIFICATE-----\n"
    "SOCIAL_AUTH_SAML_SP_PRIVATE_KEY": ""

#. Open the ``saml.key`` file, copy its entire contents, and then paste them
   inside the quotes after the ``SOCIAL_AUTH_SAML_SP_PRIVATE_KEY`` key.
   Replace all newlines with `\n`.

   .. code:: json

    "SOCIAL_AUTH_SAML_SP_PUBLIC_CERT": "-----BEGIN CERTIFICATE-----\nSWP6P/C1ypaYkmS...j9+hjvbBf3szk=\n-----END CERTIFICATE-----\n"
    "SOCIAL_AUTH_SAML_SP_PRIVATE_KEY": "-----BEGIN RSA PRIVATE KEY-----\nW1icmlkZN+FtM5h...s/psgLDn38Q==\n-----END RSA PRIVATE KEY-----\n"

#. Save and close the ``lms.yml`` file.


**************************************************
Configure your Open edX Site as a Service Provider
**************************************************

To configure your Open edX site as a SAML service provider, follow
these steps.

#. Sign in to the Django administration console for your base URL. For example,
   ``http://{your_URL}/admin``.

#. In the **Third_Party_Auth** section, next to **SAML Configuration** select
   **Add**.

   .. note:: If you want to change the configuration of an existing service
    provider, next to **SAML Configuration** select **Change**, and then
    select **Update** for the provider that you want to configure.

#. Select **Enabled**.

#. Enter the following information.

  - **Entity ID**: Enter a URI for the server. To ensure that this value
    uniquely identifies your site, the naming convention that edX recommends is
    to include the server's domain name. For example,
    ``http://saml.mydomain.com/``.

  - **Site**: Specify the site that you are configuring to be a SAML service
    provider. There can only be one SAML Service Provider per site. For more
    information about Sites in Open edX, see :ref:`Configuring Open edX sites`.

  - **Organization Info**: Use the format in the example that follows to
    specify a language and locale code and identifying information for your
    installation.

    .. code:: json

     {
        "en-US": {
            "url": "http://www.mydomain.com",
            "displayname": "{Complete Name}",
            "name": "{Short Name}"
        }
     }

  - **Other config str**: Define the security settings for the IdP metadata
    files. For more information about the security settings, see the
    `Python SAML Toolkit`_. An example follows.

    .. code:: json

     {
        "SECURITY_CONFIG": {
          "signMetadata": false,
          "metadataCacheDuration": ""
        }
     }

#. Optionally, you can save your public and private keys in the Django
   administration console. Because this procedure saves your credentials in the
   database, edX recommends that you use the ``lms.yml`` file instead.
   For more information, see :ref:`Add Keys to the LMS Configuration File`.

#. Select **Save**. You can direct identity providers to
   ``{your LMS URL}/auth/saml/metadata.xml`` for your metadata file.

*******************************************************
Ensure that the SAML Authentication Backend is Loaded
*******************************************************

By default, SAML is included as an approved data format for identity providers.
The default configuration of the ``/edx/app/edxapp/lms.yml`` file does not
explicitly include the ``THIRD_PARTY_AUTH_BACKENDS`` setting.

If you have customized this file and added the ``THIRD_PARTY_AUTH_BACKENDS``
setting to it, you might need to verify that the
``common.djangoapps.third_party_auth.saml.SAMLAuthBackend`` python-social-auth backend class is
specified for it. That backend is required before you can add SAML IdPs.

To verify that the SAML authentication backend is loaded on a devstack or
fullstack installation, review the ``/edx/app/edxapp/lms.yml`` file.

.. include:: ../../../../links/links.rst
