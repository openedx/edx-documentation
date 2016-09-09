.. _Creating a Theme:

****************
Creating a Theme
****************

To create a theme, you create a directory in one of the comprehensive theme
directories that you configured for your Open edX installation. The name of the
directory that you create is the identifier for the theme. So to create a theme
named ``my-theme``, the name of the directory in your comprehensive theme
directory must be ``my-theme``. You include the UI files that you want to
override in the theme directory.

Because the UI files for the LMS and Studio are together in the edx-platform
repository, you can create a theme that applies to both the LMS and Studio. You
must create themes for Ecommerce in a separate theme directory.

Inside a theme directory, include UI files that override the corresponding default files.

For example, if the comprehensive theming directory for your site is ``/my-
open-edx-themes``, the files in the following example create a theme named
``my-theme``.

.. code-block:: none

    /my-open-edx-themes/my-theme/lms/static/images/logo.png
    /my-open-edx-themes/my-theme/lms/static/sass/partials/base/_variables.scss
    /my-open-edx-themes/my-theme/lms/templates/navigation.html
    /my-open-edx-themes/my-theme/cms/static/images/studio-logo.png
    /my-open-edx-themes/my-theme/cms/static/images/logo.png
    /my-open-edx-themes/my-theme/cms/templates/login.html
