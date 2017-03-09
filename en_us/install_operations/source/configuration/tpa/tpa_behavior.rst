.. _SSO Behavior:

############
SSO Behavior
############

The following behavior applies to all three types of provider (OAuth, SAML, and LTI).

************************
New Learner Registration
************************

* When a user signs in by using single sign on (SSO) for the first time, their
  account is not normally created automatically. Instead, the user information
  sent by the provider is used to pre-fill the registration form. The user can
  then edit any of the information before finalizing the creation of their
  account. The user could also cancel the registration process at this point,
  and no account would be created for them.

* The user information that is passed from the external authentication provider
  to Open edX varies depending on the provider. For example, Google, Facebook,
  a university's SAML provider, and a corporate SAML provider may all provide
  different user information. Some providers may pass the user's full name,
  first name, last name, username, email address, external user ID, and more.
  Other providers may pass only an opaque "user token" that can be used to
  permanently and consistently identify that user, but which is not considered
  personal information and does not correspond to any other public identifier.

* After a user submits the registration form, their user account is created and
  is automatically "linked" to the external provider. For more information, see
  :ref:`Linking Accounts`.

* When a user creates an account by using SSO, the password field on the
  registration form is hidden. User accounts created by using SSO will have a
  `random and highly secure password`_ assigned to their account. The user will
  not know (or need to know) this password. However, the user can always use
  the "reset password" feature to change their password, if they would also
  like to be able to use a traditional password-based sign in method.

.. important::
  No matter which type of sign in method is used, a full and independent Open
  edX user account is always created for the new user, with a copy of the
  user's information. As a result, if the external provider updates the user's
  information (such as name or email address), that information will **not** be
  automatically updated in the user's Open edX account. In other words, the use
  of the external account as a reference that provides user details is a one-
  time event, not an ongoing connection.

.. _Linking Accounts:

*********************
Linking Accounts
*********************

* To be able to sign in by using an external provider such as Google, the
  user's Open edX account must be "linked" to that provider. For example, if a
  user's account is linked to Google, the user can click the **Login with
  Google** button, and will be automatically signed in to their Open edX
  account.

* User accounts can be linked to zero, one, or many external providers.

* Any provider can be linked or unlinked from an account at any time.

* If an external provider is used to register a new account, the newly created
  account will automatically be linked to that provider.

* If a user tries to sign in by using an external provider that is not yet
  linked to any Open edX account, the user will be given the following options.

    * Sign in to an existing account (using a password), which will then link
      the new provider to that existing account.

    * Create a new account.

.. include:: ../../../../links/links.rst
