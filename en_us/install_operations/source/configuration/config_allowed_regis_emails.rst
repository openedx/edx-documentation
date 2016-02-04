.. _Configure Allowed Registration Email Patterns:

################################################
Specifying Allowed Registration Email Patterns
################################################

This topic describes how to restrict registration on your site by specifying
which email address patterns are allowed in registration emails.

.. contents::
   :local:
   :depth: 1

*********
Overview
*********

By default, all email addresses are accepted when learners register for an
account on your Open edX site. You have the option of restricting registrations
to learners who use an allowed email address pattern. Doing so can be useful in
cases where you want to allow only learners who are members of a school,
organization, or corporation to register and access your courses.

.. note:: Configuring your site using the procedure below only restricts
   registration to learners whose email addresses match the specified patterns.
   It does not hide courses from any learners, or prevent access to pages on
   your site that can be accessed without registration.


*********************************
Configure Allowed Email Patterns
*********************************

To specify the email patterns that are allowed for registration, follow these steps.

#. Locate the ``lms.env.json`` and ``cms.env.json`` files, which are located
   one level above the ``edx-platform`` directory. You make the same changes
   to both files.

#. In the ``lms.env.json`` and ``cms.env.json`` files add the
   ``REGISTRATION_EMAIL_PATTERNS_ALLOWED`` setting.

   .. code-block:: bash

    "REGISTRATION_EMAIL_PATTERNS_ALLOWED": null


   If the value for this setting is ``null``, there are no restrictions, and all
   email addresses are accepted for registration.

#. Use one or more Python regular expressions to specify the email domains that
   allowed email addresses must match.

   The following example allows email addresses using the pattern
   ``example.com`` or ``any.example.com`` to register. It also allows
   ``school.tld`` addresses, but only if those addresses have a  ``.`` before
   the ``@`` symbol.

   .. code-block:: bash

     "REGISTRATION_EMAIL_PATTERNS_ALLOWED" = [

        "^.*@(.*\\.)?example\\.com$",
        "(^\\w+\\.\\w+)@school\\.tld$"
     ]

#. Save the ``lms.env.json`` and ``cms.env.json`` files.

#. Restart your ``edxapp`` instances.
