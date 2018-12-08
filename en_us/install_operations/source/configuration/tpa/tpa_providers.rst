.. _Supported Identity Providers:

#######################################
Supported Identity Providers
#######################################

In an exchange of authentication and authorization data, an identity provider
securely asserts the identity and access rights of a set of users. Your
implementation of the Open edX platform is the service provider that allows
the users access on the basis of credentials sent by an identity provider.

For example, your Open edX installation hosts the courses of three different
institutions. When you configure the open edX installation to be a service
provider, and configure each of the three institutions to be identity
providers, you permit learners who have valid user credentials at any of
those institutions to access the Open edX site. 

.. You can enable third party authentication between your Open edX system and identity providers that use the SAML 2.0 (Security Assertion Markup Language, version 2.0) or OAuth2 standards for authentication. 

.. replace the first following sentence with the above when ready to add OAuth2 
.. - Alison 5 Aug 15

You can enable third party authentication between your Open edX system and
identity providers that use the SAML 2.0 (Security Assertion Markup Language,
version 2.0) standard for authentication. For more information, see
:ref:`Integrating with a SAML Identity Provider`.

.. Regardless of the standard that the identity provider you want to integrate with uses, you begin by :ref:`enabling the third party authentication feature<Enable the Third Party Authentication Feature>` for your installation.

.. replace the following para with the above para when ready to add OAuth2 
.. - Alison 5 Aug 15

At an Open edX installation, you begin by :ref:`enabling the third party
authentication feature<Enable the Third Party Authentication Feature>` for your
installation.

At an institution that has a partner membership with edX, you can :ref:`enable
third party authentication<Enabling Third Party Authentication Edge>` between
your institutional authentication systems and the edX Edge site.

If you are using :ref:`edX as an LTI tool provider<Configuring an edX Instance
as an LTI Tool Provider>` to a external learning management system or
application, you can set up an authentication workflow between your Open edX
system and the system that is the LTI tool consumer. For more information, see
:ref:`Options for LTI Authentication and User Provisioning` and
:ref:`Configuring Open edX for LTI Authentication`.
