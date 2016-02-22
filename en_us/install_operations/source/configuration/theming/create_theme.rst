.. _Creating a Theme:

****************
Creating a Theme
****************

To make a theme, you start by creating a directory with an identifying name for
your theme. It is a good idea to put a README file into this directory with
a description of what your theme is for, and to put the entire directory under
version control.

In this example, the theme is named ``my-theme``.

.. code-block:: text

    my-theme
    └── README.rst

Next, you create a subdirectory for the Open edX component that you
want your theme to apply to. One theme can apply to multiple components:
LMS, Studio, certificates, emails, and so on.
Add a subdirectory for each component that your theme affects.
For the moment, only the LMS component
and the Studio component are supported.

For this example, you make a ``lms`` directory for the LMS component.

.. code-block:: text

    my-theme
    ├── README.rst
    └── lms

Most themes override one or more assets, such as overriding the logo in the LMS.
To override an asset in the LMS, make a ``static`` directory
inside the ``lms`` directory,
and add an asset with the same name and directory path as the asset
you want to override.

For example, to override the logo in the LMS,
the name and path is ``images/logo.png``.

.. code-block:: text

    my-theme
    ├── README.rst
    └── lms
        └── static
            └── images
                └── logo.png

You can override templates, as well. To override a template in the LMS,
make a ``templates`` directory in the ``lms`` directory,
and add a template with the same name
and directory path as the template you want to override. At the moment, only
Mako templates are supported.

For example, to override the header of the LMS,
the name and path is simply ``header.html``.

.. code-block:: text

    my-theme
    ├── README.rst
    └── lms
        ├── static
        |   └── images
        |       └── logo.png
        └── templates
            └── header.html

You can continue to add templates and assets to the ``my-theme`` directory.
For more information, see :ref:`Supported Themable Templates`
and :ref:`Supported Themable Assets`.

You can also theme CSS files using Sass variables.
For more information, see :ref:`Sass Theming` and
:ref:`Supported Themable Sass Variables`.

When you have finished creating your theme,
:ref:`activate your theme <Activating a Theme>`.
