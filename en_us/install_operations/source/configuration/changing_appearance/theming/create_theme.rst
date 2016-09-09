.. _Creating a Theme:

################
Creating a Theme
################

To create a theme, you create a directory in the themes directory that you
configured for your Open edX installation when you enabled theming. For more
information about the themes directory, see :ref:`enable_theming`.

The name of the directory that you create is the identifier for the theme. So
to create a theme named ``my-theme``, the name of the directory in your
comprehensive theme directory must be ``my-theme``. You include the UI files
that you want to override in the theme directory.

.. note::

    If your Open edX installation is configured to use more than one themes
    directory, you must ensure that each of the theme directories that you
    create is unique. The Open edX installation looks for a named theme in all
    of the themes directories that you configure.

Because the UI files for the LMS and Studio are together in the edx-platform
repository, you can create a theme that applies to both the LMS and Studio. You
must create themes for Ecommerce in a separate theme directory.

Inside a theme directory, include UI files that override the corresponding
default files.

For example, if the themes directory for your site is ``/my- open-edx-themes``,
the files in the following example create a theme named ``my-theme``. Because
the theme directory includes UI files in both the ``lms`` and ``cms``
subdirectories, you can apply the theme to both the LMS and Studio.

.. code-block:: none

    /my-open-edx-themes/my-theme/lms/static/images/logo.png
    /my-open-edx-themes/my-theme/lms/static/sass/partials/base/_variables.scss
    /my-open-edx-themes/my-theme/lms/templates/navigation.html
    /my-open-edx-themes/my-theme/cms/static/images/studio-logo.png
    /my-open-edx-themes/my-theme/cms/static/images/logo.png
    /my-open-edx-themes/my-theme/cms/templates/login.html

.. note::

    After you create or make changes to a theme, you must update the theme.
    Updating a theme compiles Sass files to create the CSS files that style
    your UIs. For more information, see :ref:`updating_themes`.

.. _understanding_themeable_ui_files:

******************************************
Understanding Which UI Files Can Be Themed
******************************************

You can customize the default images, Sass, and web application template files for the Open edX components in your installation. The UI files are stored in the directories shown in the following example theme directory. You can examine the default UI files in the source repository of the component you are theming.

.. code-block:: none

    /my-open-edx-themes/my-theme/lms/static/images
    /my-open-edx-themes/my-theme/lms/static/sass
    /my-open-edx-themes/my-theme/lms/templates

==================
Customizing Images
==================

You can override any of the images in the ``static/images`` directories for the components you are theming.

========================
Customizing Sass Styling
========================

For the LMS and Studio, you can customize any of the Sass files in the ``static/sass`` directories.

For Ecommerce, you can customize any of the Sass files in the ``static/sass/partials`` directory. Do not customize Sass files in the ``static/sass/base`` directory.

==========================================
Customizing Web Application Page Templates
==========================================

You can override any of the images in the ``static/images`` directories for the components you are theming.

.. _updating_themes:

**************************
Updating Themes
**************************

You update themes to compile Sass files to create the CSS files that style your UI when you apply a theme.

====================================
Update Themes for the LMS or Studio
====================================

To update a theme for the LMS or Studio, do the following.

#. Log into the LMS and Studio server as the ``edxapp`` user.

#. Change to the ``/edx/app/edxapp/edx-platform`` directory.

#. Invoke the ``paver update_assets`` command to update and apply all themes.
   If you want to update specific themes, use the options described in the
   following table.

.. list-table::

 * - Option
   - Description
 * - ``--theme-dirs``
   - A space-separated list of the themes directories that you want to update.
     Only the themes in the themes directories that you include will be
     updated.
 * - ``--themes``
   - A space-separated list of the themes that you want to update. Only the
     themes that you include will be updated.

=============================
Update Themes for Ecommerce
=============================

To update a theme for Ecommerce, do the following.

#. Log into the Ecommerce server as the ``ecommerce`` user.

#. Change to the ``/edx/app/ecommerce/ecommerce`` directory.

#. Invoke the ``python manage.py update_assets`` command to update and apply
   all themes. If you want to update specific themes, use the options described
   in the following table.

.. The descriptions of these commands need testing.

.. list-table::

 * - Option
   - Description
 * - ``--settings``
   - The database ID of the site you want to update themes for. For example,
     ``--settings=ecommerce.settings.production``.
 * - ``--themes``
   - A space-separated list of the themes that you want to update. Only the
     themes that you include will be updated.
 * - ``--output-style``
   - The coding style for the compiled CSS files. Possible values are
     ``nested``, ``expanded``, ``compact``, and ``compressed``. The default
     value is ``nested``.
 * - ``--skip-system``
   - Disables Sass file compilation for the default Sass files provided in the
     Open edX software. Use this option if you have only updated the Sass files
     in your theme.
 * - ``--skip-collect``
   - Only compile the Sass files and do not deploy the resulting CSS files.

.. This has the same description as skip-system in the wiki page. That doesn't
.. seem correct to me.
.. * - ``--enable-source-comments``
..   -

