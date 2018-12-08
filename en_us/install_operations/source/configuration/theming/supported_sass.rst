.. _Supported Themable Sass Variables:

*********************************
Supported Themable Sass Variables
*********************************

There are currently no supported themable Sass variables.

Sass variables in the LMS and Studio *can* be overriden, but the
meaning and usage of these variables are subject to change, so they are not
considered to be "supported". If you choose to override these Sass variables
anyway, you can find these variables defined in a ``_variables.scss`` Sass
partial in the edx-platform repository.

.. list-table::
    :header-rows: 1

    * - Component
      - File

    * - LMS
      - ``lms/static/sass/base/_variables.scss``

    * - Studio
      - ``cms/static/sass/_variables.scss``

You can only override variables that use the Sass ``!default`` flag.
For more information, see `the documentation for Sass variable defaults`_.

.. include:: ../../../../links/links.rst
