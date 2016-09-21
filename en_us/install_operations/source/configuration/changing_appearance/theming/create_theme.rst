.. _Creating a Theme:

################
Creating a Theme
################

To create a theme, you add a theme directory to the installation-wide themes
directory that you added when you enabled theming for your Open edX
installation. Then, you copy default UI files into your theme directory and
update them to change the appearance of the Open edX site or sites that will
use that theme.

.. contents::
   :local:
   :depth: 1

For more information about the themes directory, see
:ref:`enable_theming`.

.. _understanding_themeable_ui_files:

******************************************
Understanding Which UI Files Can Be Themed
******************************************

You can customize the default images, Sass, and web application template files
for the Open edX components in your installation.

* To replace an image, you can override any of the images in the
  ``static/images`` directories for the components you are theming.

* For the LMS and Studio, you can customize any of the Sass files in the
  ``static/sass`` directories.

* For the E-commerce service, you can customize any of the Sass files in the
  ``static/sass/partials`` directory.

  .. note:: Do not customize Sass files in the ``static/sass/base`` directory.

* You can override any of the HTML templates in the ``lms/templates`` or
  ``cms/templates`` directories for the components that you want to apply a
  theme to.

UI files for the LMS are stored in the directories shown in the following
example theme directory. You can examine the default UI files in the source
repository of the component that you want to apply the theme to.

.. code-block:: none

    /my-open-edx-themes/my-theme/lms/static/images
    /my-open-edx-themes/my-theme/lms/static/sass
    /my-open-edx-themes/my-theme/lms/templates

***************************
Naming a Theme Directory
***************************

The name of the directory that you create to hold your versions of the image,
theme, and Sass styling files identifies the theme. As a result, if you want to
create a theme named ``my-theme``, the name of the directory in your
installation-wide themes directory must be ``my-theme``.

.. note::

    If you add more than one site-specific theme directory, make sure that each
    of the directory names is unique. The Open edX installation looks for a
    theme with a certain name, and selects the first one that matches.

Because the UI files for the LMS and Studio are located together in the
edx-platform repository, you can create one theme that applies to both the LMS
and Studio. If you want to create a theme for the E-commerce service, you must
add a separate theme directory for its files.

The theme directory holds the UI files that override the corresponding
default files.

For example, if the themes directory for your site is ``/my-open-edx-themes``,
the files in the following example create a theme named ``my-theme``.

.. code-block:: none

    /my-open-edx-themes/my-theme/lms/static/images/logo.png
    /my-open-edx-themes/my-theme/lms/static/sass/partials/base/_variables.scss
    /my-open-edx-themes/my-theme/lms/templates/navigation.html
    /my-open-edx-themes/my-theme/cms/static/images/studio-logo.png
    /my-open-edx-themes/my-theme/cms/static/images/logo.png
    /my-open-edx-themes/my-theme/cms/templates/login.html

Because the theme directory includes UI files in both the ``lms`` and ``cms``
subdirectories, you can apply the theme to both the LMS and Studio.

.. Matt, I checked out https://github.com/edx/sample-themes/pull/1/files, but based on your explanation of needing unique directory names for each theme, I can't quite tell if that is unique *regardless* of the products that it applies to? does a theme directory for a green ecom theme have to have a different name then a theme directory for a green Studio+LMS theme? So, is this a reasonable example of an ecom theme file (note ecom in theme dir name)?
.. my-open-edx-themes/my-ecom-theme/ecommerce/static/sass/partials/utilities/_variables.scss ? or can it have the same dir name as the other examples above, and be my-open-edx-themes/my-theme/ecommerce/static/sass/partials/utilities/_variables.scss? - Alison

.. note::

    After you create or make changes to a theme, you must update the theme.
    Updating a theme compiles Sass files to create the CSS files that style
    your UI. For more information, see :ref:`updating_themes`.

.. _updating_themes:

**************************
Updating a Theme
**************************

When you update a theme, the process compiles the Sass files and creates the
CSS files that style your UI when you apply the theme.

====================================
Update a Theme for the LMS or Studio
====================================

To update a theme for Studio or the LMS, follow these steps.

#. Log in to the Open edX machine as the ``edxapp`` user.

#. Change to the ``/edx/app/edxapp/edx-platform`` directory.

#. Invoke the ``paver update_assets`` command to update and apply all themes.

   If you want to update specific themes, use the options described in the
   following table.

   .. list-table::
    :header-rows: 1
    :widths: 30 70

    * - Option
      - Description
    * - ``--theme-dirs``
      - Provide a space-separated list of the theme directories that you want
        to update. Only files in the theme directories that you include
        are updated.
    * - ``--themes``
      - Provide a space-separated list of the themes that you want to update.
        Only the themes that you include are updated.

=========================================
Update a Theme for the E-commerce Service
=========================================

To update a theme for the E-commerce service, follow these steps.

#. Log in to the server for the E-commerce service as the ``ecommerce`` user.

#. Change to the ``/edx/app/ecommerce/ecommerce`` directory.

#. Invoke the ``python manage.py update_assets`` command to update and apply
   all themes.

   To specify specific themes to update or other settings, use the
   options described in the following table.

   .. list-table::
    :header-rows: 1
    :widths: 30 70

    * - Option
      - Description
    * - ``--settings``
      - Supply the database ID of the site for which you want to update themes.
        For example, ``--settings=ecommerce.settings.production``.
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


.. The descriptions of these commands need testing. (per Peter) ^^
.. This has the same description as skip-system in the wiki page. That doesn't
.. seem correct to me. (per Peter) I think he means the command on the next line. I don't know what wiki page he's referring to - Alison
.. * - ``--enable-source-comments``
..   -

