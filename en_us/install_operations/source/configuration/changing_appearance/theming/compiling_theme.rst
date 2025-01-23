.. _Compiling a Theme:

#######################
Compiling a Theme
#######################

To update a theme, you compile the Sass files to create the CSS files that
style your UI when you apply the theme.

.. contents::
   :local:
   :depth: 1

*************************************
Update a Theme for the LMS or Studio
*************************************

To update a theme for Studio or the LMS, follow these steps.

#. Log in to the Open edX machine as the ``edxapp`` user.

#. Change to the ``/edx/app/edxapp/edx-platform`` directory.

#. Execute the ``npm run compile-sass`` command to update all themes.

   If you want to update specific themes, use the arguments described in the
   following table.

   .. list-table::
    :header-rows: 1
    :widths: 30 70

    * - Argument
      - Description
    * - ``--theme-dirs``
      - Provide a space-separated list of the theme directories that you want
        to update. Only files in the theme directories that you include
        are updated.
    * - ``--themes``
      - Provide a space-separated list of the themes that you want to update.
        Only the themes that you include are updated.

******************************************
Update a Theme for the E-commerce Service
******************************************

For the E-commerce service, commands are available for you to update
all themes at once, or to update only the themes you specify.

To update a theme for the E-commerce service, follow these steps.

#. Log in to the server for the E-commerce service as the ``ecommerce`` user.

#. Change to the ``/edx/app/ecommerce/ecommerce`` directory.

#. To update all themes, execute one of these commands.

   * ``make migrate``

   * ``python manage.py update_assets``

#. To specify a theme or set of themes to update, or to include optional
   arguments, execute ``python manage.py update_assets`` with the options
   described in the following table.

   .. list-table::
    :header-rows: 1
    :widths: 30 70

    * - Argument
      - Description
    * - ``--settings``
      - Provide the name of a Django `settings module <https://docs.djangoproject.com/en/1.10/ref/django-admin/#cmdoption--settings>`_
        in Python package syntax. For example,
        ``--settings=ecommerce.settings.production``.
    * - ``--themes``
      - Provide a space-separated list of the themes that you want to update.
        Only the themes that you include are updated.
    * - ``--output-style``
      - Defines the coding style for the compiled CSS files. Possible values
        are ``nested``, ``expanded``, ``compact``, and ``compressed``. The
        default value is ``nested``.
    * - ``--skip-system``
      - Disables Sass file compilation for the default Sass files provided in
        the Open edX software. Use this option if you have only updated the
        Sass files in your theme.
    * - ``--skip-collect``
      - Only compile the Sass files and do not deploy the resulting CSS files.
    * - ``--enable-source-comments``
      - Include the location of the source file as comments in the resulting
        CSS files.  Enabling this argument can be useful when you are testing a
        theme.

