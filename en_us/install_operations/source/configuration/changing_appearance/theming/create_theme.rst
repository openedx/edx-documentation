.. _Creating a Theme:

################
Creating a Theme
################

To create a theme, you create a directory for it within the themes directory
that you configured for your Open edX installation when you enabled theming.
For more information about the themes directory, see :ref:`enable_theming`.

.. _understanding_themeable_ui_files:

******************************************
Understanding Which UI Files Can Be Themed
******************************************

You can customize the default images, Sass, and web application template files
for the Open edX components in your installation. The UI files are stored in
the directories shown in the following example theme directory. You can examine
the default UI files in the source repository of the component you are theming.

.. code-block:: none

    /my-open-edx-themes/my-theme/lms/static/images
    /my-open-edx-themes/my-theme/lms/static/sass
    /my-open-edx-themes/my-theme/lms/templates

==================
Customizing Images
==================

You can override any of the images in the ``static/images`` directories for the
components you are theming.

The following table lists image assets that many Open edX sites choose to
override.

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - Component
     - Asset
     - Description
   * - LMS
     - ``images/logo.png``
     - The logo for the LMS. Displayed in the upper left corner of the LMS.
   * - Studio
     - ``images/studio-logo.png``
     - The logo for Studio. Displayed in the upper left corner of Studio.
   * - LMS
     - ``images/profiles/default_30.png``
       ``images/profiles/default_50.png``
       ``images/profiles/default_120.png``
       ``images/profiles/default_500.png``
     - Default profile images for learner profiles.
       The default image displays for learners until they upload their own
       profile images. These image files are named based on their sizes:
       30px by 30px, 50px by 50px, 120px by 120px, and 500px by 500px,
       respectively.

========================
Customizing Sass Styling
========================

For the LMS and Studio, you can customize any of the Sass files in the
``static/sass`` directories.

For Ecommerce, you can customize any of the Sass files in the
``static/sass/partials`` directory. Do not customize Sass files in the
``static/sass/base`` directory.

==========================================
Customizing Web Application Page Templates
==========================================

You can override any of the images in the ``static/images`` directories for the
components you are theming.

.. ^^ reviewers can you help me out here? this seems to be a copy and paste error - Alison

The following table lists templates that many Open edX sites choose to
override.

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - Component
     - Template
     - Description
   * - LMS
     - ``header.html``
     - The page header for the LMS. This template is used for the top of the
       ``<body>`` element on the page, not for the ``<head>`` element of the
       page. EdX recommends that you start by copying the contents of the
       ``navigation.html`` core template, and modifying it as necessary.
   * - LMS
     - ``footer.html``
     - The page footer for the LMS. EdX recommends that you start by copying
       the contents of the ``footer.html`` core template, and modifying it as
       necessary.

***************************
Naming a Theme Directory
***************************

The name of the directory that you create identifies the theme. Therefore, to
create a theme named ``my-theme``, the name of the directory in your
comprehensive theme directory must be ``my-theme``. You put copies of the UI
files that you want to override in that directory.

.. note::

    If your Open edX installation is configured to use more than one theme
    directory, you must ensure that each directory name is unique across all
    directories. The Open edX installation looks for a named theme in all of
    the theme directories that you configure.

.. Maybe it's just me, but I think the distinction between the instance-wide themes directory (plural) and the site-specific theme directories (singular) is really hard to follow, and might not be accurately reflected in this draft. I'm also not understanding the multiple theme directories thing. - Alison

Because the UI files for the LMS and Studio are located together in the
edx-platform repository, you can create a theme that applies to both the LMS
and Studio. You must create themes for the E-commerce service in a separate
theme directory.

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

.. more accurate to say that the theme applies to both Studio and LMS?

.. note::

    After you create or make changes to a theme, you must update the theme.
    Updating a theme compiles Sass files to create the CSS files that style
    your UIs. For more information, see :ref:`updating_themes`.


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

#. Log in to the Studio and LMS server as the ``edxapp`` user.

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

.. The descriptions of these commands need testing. (per Peter)

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

.. This has the same description as skip-system in the wiki page. That doesn't
.. seem correct to me. (per Peter) I think he means the command on the next line. I don't know what wiki page he's referring to - Alison
.. * - ``--enable-source-comments``
..   -

