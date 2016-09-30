.. _Themes Root Directories:

#################################
Root Directories for Theme Files
#################################

Themes are located outside of the Open edX source directories, in any location
you like. For example, you might make a directory called
``/my-open-edx-themes``.

Within that directory, you create a separate directory for each Open edX
repository that you want to create a theme for, such as ``edx-platform``
and ``ecommerce``.

Within each of those directories, you create another directory and name it for
your theme, such as ``my-theme``. You can create a number of themes, each with
their own name. Within each theme directory, you create directories and files
to parallel the structure in the corresponding Open edX repository.

After you create these directories, you might have a structure like this one.

.. code::

    my-open-edx-themes
    ├── ecommerce
    │   └── my-theme
    └── edx-platform
        └── my-theme
            ├── cms
            └── lms

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
  Syntactically Awesome Style Sheet (Sass) files that produce Cascading Style
  Sheet (CSS) files.

* ``templates`` holds Python web application page templates that produce the
  HTML for UI pages.
