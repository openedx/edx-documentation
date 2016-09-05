.. _Theming Open edX:

######################################################
Theming Open edX
######################################################

Theming changes the appearance of an Open edX site by overriding the page
templates, CSS styling, and assets such as images that are provided in the Open
edX code by default. This section describes how to create and use themes to
change how an Open edX site looks, without changing how it works.

When an Open edX site overrides user interface files, it uses files that you
create instead of the default files included with the Open edX source code. The
files that you create must match the relative file paths and file names of the
default user interface files that they override. Relative file paths are from
the root of the Open edX installation directory.

For example, an Open edX site includes an image file named ``logo.png`` that it
displays in the header of most LMS pages. The file path of that image is
``lms/static/images/logo.png``.

Installed on an Open edX site server, the absolute file path of the logo image might be similar to the path shown below.

.. code-block:: none

    /edx/app/edxapp/edx-platform/lms/static/images/logo.png

To use theming, you place your customized user interface files in a separate
theme directory. The Open edX site looks for overridden user interface files in
that directory. It uses files if they match the exact file path and file name
of the default user interface files. The following example shows an absolute
file path of the logo image in a theme directory. The file path after ``/my-
themes/my-special-theme/`` matches the file path of that image, relative to the
root of the Open edX installation directory.

.. code-block:: none

    /my-themes/my-special-theme/lms/static/images/logo.png

The following sections provide more information about using theming in your Open edX site.

.. toctree::
   :maxdepth: 2

   theming_sites

..   what_is_theming
..   create_theme
..   sass
..   activate_theme
..   supported_assets
..   supported_templates
..   supported_sass
..   theming_glossary
