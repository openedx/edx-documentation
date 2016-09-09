.. _Theming Open edX:

######################################################
Theming Open edX
######################################################

Theming changes the appearance of an Open edX installation by overriding the
page templates, CSS styling, and assets such as images that are provided in the
Open edX code by default. This section describes how to create and use themes
to change how an Open edX installation looks, without changing how it works.

You can use theming to change the appearance of the following parts of your
Open edX installation.

* The LMS user interface (UI), for learners.
* The Studio UI, for course authors.
* The Ecommerce UI, for course offering and order managers.

When an Open edX installation overrides UI files, it uses files that you create
instead of the default files included with the Open edX source code. The files
that you create must match the relative file paths and file names of the
default UI files that they override. The root directory for relative paths is different for the LMS, Studio, and Ecommerce.

* For the LMS and Studio, relative file paths are from the root directory of
  the local clone of the ``edx/edx-platform`` repository in your installation
  directory.

* For Ecommerce, relative file paths are from the ``ecommerce`` directory of
  the local clone of the ``edx/ecommerce`` repository in your installation
  directory.

For example, the root directory for the relative file paths of overriding UI files might be at one of the following file paths.

* For the LMS UI or Studio UI, ``/edx/app/edxapp/edx-platform``.

* For the Ecommerce UI, ``/edx/app/ecommerce/ecommerce/ecommerce``.

The UI files that you can override are held in two subdirectories.

* ``static`` - a directory that holds media files such as images and styling
  resources such as syntactically awesome style sheets (Sass) files that
  produce cascading style sheet (CSS) files.

* ``templates`` - a directory that holds Python web application page templates
  that produce the HTML for UI pages.

For example, an Open edX installation includes an image file named ``logo.png``
that it displays in the header of most LMS pages. The file path of that image
in the ``edx-platform`` repository is ``lms/static/images/logo.png``.

To use theming, you place customized UI files in a theme directory that you
designate in the configuration for your Open edX installation. The Open edX
site looks for overridden UI files in that directory and uses files if they
match the exact file path and file name of the default UI files.

The following example shows an absolute file path of the LMS logo image in a
theme directory. The file path after ``/my-open-edx-themes/my-theme/`` matches
the relative file path of that image in the default directory for the LMS UI.

.. code-block:: none

    /my-open-edx-themes/my-theme/lms/static/images/logo.png

The following sections provide more information about using theming in your Open edX installation.

.. toctree::
   :maxdepth: 2

   enable_theming
   create_theme
   using_default_themes
   theming_sites


..   what_is_theming
..   create_theme
..   sass
..   activate_theme
..   supported_assets
..   supported_templates
..   supported_sass
..   theming_glossary
