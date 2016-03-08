.. _Customize Registration Page:

#############################################
Adding Custom Fields to the Registration Page
#############################################

This topic describes how to add custom fields to the registration page for your
instance of Open edX.

.. contents::
   :local:
   :depth: 1

*********
Overview
*********

By default, the registration page for each instance of Open edX has fields that
ask for information such as a user's name, country, and highest level of
education completed. You can add custom fields to the registration page for
your own Open edX instance. These fields can be different types, including
text entry fields and drop-down lists.

*********************************************
Add Custom Fields to the Registration Page
*********************************************

Before you add a custom field to the registration page, you must make sure that
the combined sign-in and registration form is enabled for your Open edX
instance. To do this, open the ``lms.env.json`` and ``cms.env.json`` files, and
set the ``ENABLE_COMBINED_LOGIN_REGISTRATION`` feature flag to True. These
files are located one level above the ``edx- platform`` directory.

To add custom fields to the registration page, follow these steps.

#. Start the LMS and sign in to your instance of Open edX.

#. Use Python to create a Django form that contains the fields that you want to
   add to the page, and then create a Django model to store the information
   from the form.

   For more information about how to create Django forms, see `Django Forms`_
   on the `Django website`_.

#. In the ``lms.env.json`` file, add the app for your model to the
   ``ADDL_INSTALLED_APPS`` array.

#. In the ``lms.env.json`` file, set the ``REGISTRATION_EXTENSION_FORM``
   setting to the path of the Django form that you just created, as a dot-
   separated Python string.

   For example, if your form is named "ExampleExtensionForm" and is located at
   "path/to/the_form.py", the value of the setting is
   ``path.to.the_form.ExampleExtensionForm``.

#. Run database migrations.

#. Restart the LMS and verify that the new fields appear on your registration
   form.

.. note::

  For an example app for custom forms, see the OpenCraft `custom_form_app`_
  page in `GitHub`_.


.. include:: ../../../links/links.rst
