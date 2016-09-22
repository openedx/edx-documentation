.. _Themes Root Directories:

#################################
Root Directories for Theme Files
#################################

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
