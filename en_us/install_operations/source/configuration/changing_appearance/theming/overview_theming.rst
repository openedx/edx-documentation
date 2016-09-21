.. _Theming Overview:

###################
Themes Overview
###################

To override the files that constitute the default Open edX theme, you create
replacements for one or more of those files, place them in file paths that are
constructed and named in parallel to the default file locations, and then
configure your Open edX instance to use the files in your theme's directories
instead of the default locations. To render the website for your instance Open
edX first looks for files in your theme directories, and uses any file that
matches the exact file path and file name of a default UI file. If matching
files are not found, then Open edX looks in the default location.

.. contents::
   :local:
   :depth: 1

************************************
Root Directories for the Theme Files
************************************

You must give the files that you create for a theme the same relative file
paths and file names as the default files that they override. Different root
directories for the relative paths apply to Studio, the LMS, and the E-commerce
service.

* For Studio and the LMS, relative file paths are from the root directory of
  the local clone of the ``edx/edx-platform`` repository in your installation
  directory.

* For the E-commerce service, relative file paths are from the ``ecommerce``
  directory of the local clone of the ``edx/ecommerce`` repository in your
  installation directory.

For example, the root directory for the relative file paths of your theme files
might be at one of the following file paths.

* For the LMS UI or Studio UI, ``/edx/app/edxapp/edx-platform``.

* For the UI of the E-commerce service,
  ``/edx/app/ecommerce/ecommerce/ecommerce``.

The following subdirectories hold the UI files that you can override.

* ``static`` holds media files such as images and styling resources such as
  syntactically awesome style sheet (Sass) files that produce cascading style
  sheet (CSS) files.

* ``templates`` holds Python web application page templates that produce the
  HTML for UI pages.

***********************************
Example File Path for a Theme File
***********************************

The default Open edX theme includes an image file named ``logo.png`` that
appears in the header of most LMS pages. The file path of that image in the
``edx-platform`` repository is ``lms/static/images/logo.png``.

The following example shows an absolute file path of the LMS logo image in a
theme directory. The file path after ``/my-open-edx-themes/my-theme/`` matches
the relative file path of that image in the default directory for the LMS UI.

.. code-block:: none

    /my-open-edx-themes/my-theme/lms/static/images/logo.png

