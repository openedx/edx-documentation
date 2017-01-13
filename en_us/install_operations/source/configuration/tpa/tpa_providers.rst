.. _Supported Identity Providers:

#######################################
Supported Identity Providers
#######################################

In an exchange of authentication and authorization data, an identity provider
securely asserts the identity and access rights of a set of users. Your Open
edX site is the service provider that allows the users access on the basis of credentials sent by an identity provider.

For example, your Open edX site hosts the courses of three different
organizations. When you configure the Open edX site to be a service provider,
and configure each of the three organizations to be identity providers, you
permit learners who have valid user credentials at any of those organizations
to access the Open edX site.

You can enable third party authentication between your Open edX site and many
types of identity providers. The Open edX platform provides support for
three types of identity providers.

****************************
Supported Identity Providers
****************************

The Open edX platform has integrated support for the following providers.

* **OAuth** based providers (OAuth2 and the older OAuth v1). Google, Facebook,
  LinkedIn, and Azure Active Directory are available by default. Any other
  `OAuth backends supported by python-social-auth v0.2.12`_ can be enabled by
  changing a configuration setting. People in the Open edX community sometimes
  use “third party auth” to refer to Google or Facebook integration. Single
  sign on, or “SSO”, and “third party auth” are largely interchangeable terms
  for the purposes of this document.

* **Security Assertion Markup Language (SAML) version 2.0**, or Shibboleth.
  SAML is an SSO standard mostly used by universities and corporations.
  Shibboleth is the name of a particular implementation of SAML, commonly used
  by higher education institutions. People in the Open edX community sometimes
  use “SSO” to refer to SAML or Shibboleth. “SSO” and “Third Party Auth” are
  largely interchangeable terms for the purposes of this doc. For more
  information, see :ref:`Integrating with a SAML Identity Provider`.

* **LTI**. Users can use Learning Tools Interoperability® (LTI®) to
  authenticate.

******************************************
Provisionally Supported Identity Providers
******************************************

The Open edX platform also includes limited support for the following SSO
providers.

* OpenID
* Apache-hosted Shibboleth
* SSL client certificates
* Central Authentication Service (CAS)

These providers are part of the external_auth app, tend to be older and less
robustly tested, and have a much more limited feature set. These providers are
included in the source code but are not officially supported.

******************************
Integrating Identity Providers
******************************

Regardless of the standard that the identity provider you want to integrate
with uses, you begin by :ref:`enabling the third party authentication
feature<Enable the Third Party Authentication Feature>` for your site.

For example, your Open edX site hosts the courses of three different
organizations. When you configure the Open edX site to be a service provider,
and configure each of the three organizations to be identity providers, you
permit learners who have valid user credentials at any of those organizations
to access the Open edX site.

If you are using :ref:`edX as an LTI tool provider<Configuring an edX
Instance as an LTI Tool Provider>` to a external learning management system
or application, you can set up an authentication workflow between your Open
edX site and the system that is the LTI tool consumer. For more information,
see :ref:`Options for LTI Authentication and User Provisioning` and
:ref:`Configuring Open edX for LTI Authentication`.

.. include:: ../../../../links/links.rst
