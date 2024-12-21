.. _Configure Password Policy:

#############################
Configuring a Password Policy
#############################

This topic describes how to configure a password policy in your
instance of Open edX.

.. contents::
   :local:
   :depth: 1

*********
Overview
*********

By default, Open edX imposes a minimal password complexity policy for all
users who log  in to the LMS or Studio. Under the default password complexity
policy, passwords must contain 2 to 75 characters and cannot be similar to the
user's username or email address.

.. note:: Open edX does not store plain-text passwords, only
   hashes. Since the length of a hash is independent of the length of
   the original password, passwords can effectively be of unlimited
   length. The 75-character default limit is rather arbitrary. Open
   edX does impose an upper limit of 5,000 characters on a password,
   but this should be well beyond the practical limit of password
   length.

This password policy is defined in the ``lms.yml`` configuration file,
under the ``AUTH_PASSWORD_VALIDATORS`` setting::

  AUTH_PASSWORD_VALIDATORS:
  -   NAME: django.contrib.auth.password_validation.UserAttributeSimilarityValidator
  -   NAME: common.djangoapps.util.password_policy_validators.MinimumLengthValidator
        OPTIONS:
          min_length: 8
  -   NAME: common.djangoapps.util.password_policy_validators.MaximumLengthValidator
        OPTIONS:
          max_length: 75

You can override these settings by modifying one of the existing
``OPTIONS``. For example, if you want to enforce a minimum password
length of 16 characters, and a maximum length of 256,
you would set::

  AUTH_PASSWORD_VALIDATORS:
  -   NAME: django.contrib.auth.password_validation.UserAttributeSimilarityValidator
  -   NAME: common.djangoapps.util.password_policy_validators.MinimumLengthValidator
        OPTIONS:
          min_length: 16
  -   NAME: common.djangoapps.util.password_policy_validators.MaximumLengthValidator
        OPTIONS:
          max_length: 256


.. warning:: If your Open edX configuration :ref:`enables third-party
   authentication <Enabling Third Party Authentication>`, the *maximum*
   value you can specify for the ``MinimumLengthValidator``'s
   ``min_length`` option is 25.

You can also substitute your own password policy for the default
policy. To configure a password policy in replacement of the default
password policy, follow these steps.

#. Create or import a new password validator. This is a Python class that defines how a 
   password is validated. For details about writing a password validator class, 
   see :ref:`Creating a Password Validator`.

#. Add your password validator to the list in the ``AUTH_PASSWORD_VALIDATORS`` 
   configuration key in the ``lms.yml`` configuration file. For details, 
   see :ref:`Configuring a Password Validator`.

.. _Creating a Password Validator:

*****************************
Creating a Password Validator
*****************************

An Open edX password validator is a Python class that specifies how user
passwords are validated. You can use whatever criteria you choose to establish
a password policy for your Open edX instance. You can create your own custom
password validator, or import one or more password validators from
`password_policy_validators`_ in the ``edx-platform``  repository on GitHub.
Those password validators include minimum length, maximum length, user
attribute similarity, minimum alphabetic, minimum numeric, minimum uppercase,
minimum lowercase, minimum punctuation, and minimum symbols. For more
information, see also the  `Django password validation documentation`_.

.. _Configuring a Password Validator:

*********************************
Configuring a Password Validator
*********************************

To configure your Open edX instance to use a particular password validator, 
add your password validator to the list in the ``AUTH_PASSWORD_VALIDATORS`` 
configuration key in the ``lms.yml`` configuration file. For example, to
add a password validator named ``MyPasswordValidator``, add a line like this 
to the ``lms.yml`` configuration file.
::
 
  AUTH_PASSWORD_VALIDATORS:
  -   NAME: path.to.module.MyPasswordValidatorClass

.. include:: ../../../links/links.rst
