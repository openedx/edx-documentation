.. _Comprehensive Theming:

###############
Comprehensive Theming
###############

.. This guide will tell about how to setup of Comprehensive Theming in E-commerce / Otto

Any application, including Otto, can be loosely divided into two parts:

* the user interface ("how it looks"),
* and the application logic ("how it works").

For example, when considering a product in Otto,
the user interface consists of how the products are laid out on the page, how the selectors look,
how the checkout button is labelled, what sort of fonts and colors are used to display the text,
and so on. The application logic consists of how Otto adjusts product price based on the discount
coupons, and how it records that information to be displayed in the future.

Theming consists of changing the user interface without changing the application logic. When setting
up an E-Commerce website, the website operator often wants to use their own logo, modify the color scheme,
change links in the header and footer for SEO (search engine optimization) purposes, and so on. However,
although the user interface may look different, the application logic must remain the same so that Otto
continues to work properly. A well-designed theme preserves the general layout and structure of the user
interface, so that users of the website still find it familiar and easy to use. Be careful about making
sweeping changes to the user interface without warning: your users will be very confused!

---------------
Theme Structure
---------------
From a technical perspective, theming consists of overriding core

* Templates
* Static Assets
* Sass

With themed versions of those resources. Every theme must conform to a directory structure. This structure
mirrors the Otto directory structure and looks like this

.. code-block:: text

    my-theme
        ├── README.rst
        ├── static
        |      └── images
        |      |     └── logo.png
        |      |
        |      └── sass
        |            └── partials
        |                   └── utilities
        |                           └── _variables.scss
        |
        └── templates
                └── oscar
                |     └── dashboard
                |             └── index.html
                └── 404.html

.. _Templates:

****************************
Templates
****************************

Any template included in ``ecommerce/templates`` directory is themable. However, make sure not to override
class names or id values of html elements inside a template, as these are used by javascript and/or css and
overriding these could cause unwanted behavior.

.. _Static Assets:

****************************
Static Assets
****************************

Any static asset included in ``ecommerce/static`` can be overridden except css files present in
``ecommerce/static/css``. Css styles can be overridden via sass overrides explained below.

.. caution::
    Theme names should be unique and no static asset and/or directory name should be same as theme's name.
    Otherwise static assets would not work correctly.

.. _Sass:

****************************
Sass
****************************

Sass overrides are a little different from static asset or template overrides. There are two types of
styles included in ``ecommerce/static/sass``:

- ``base``
- ``partials``

.. WARNING::
    Styles present in ``ecommerce/static/sass/base`` should not be overridden as overriding these could
    result in an unexpected behavior.

Any styles included in ``ecommerce/static/sass/partials`` can be overridden. Styles included in this
directory contain variable definitions that are used by main sass files. This is the best place if you
want to update things like header/footer background, fonts etc.

----------------
Enabling a Theme
----------------
To enable a theme, you must first install your theme onto the same server that is running Otto. If you are
using devstack or fullstack to run Otto, you must be sure that the theme is present on the Vagrant virtual
machine. It is up to you where to install the theme on the server, but a good default location is
``/edx/app/ecommerce/ecommerce/themes``.

.. note::
    All themes must reside in the same physical directory.

.. note::
    Like other settings, comprehensive theming settings can also be changed by using

    * ``ecommerce/ecommerce/settings/base.py``
    * ``ecommerce/ecommerce/settings/private.py`` (preferred)
    * ``edx/etc/ecommerce.yml`` (in devstack)

In order for Otto to use the installed themes, you must specify the location of the theme directory in
Django settings by setting COMPREHENSIVE_THEME_DIRS in your settings file:

.. code-block:: python

    COMPREHENSIVE_THEME_DIRS = ["/edx/app/ecommerce/ecommerce/themes", ]

Where ``/edx/app/ecommerce/ecommerce/themes`` is the path to where you have installed the
themes on your server. You can list any/all theme directories through this setting.

After installing a theme, associate it with sites by adding appropriate entries to the following tables

- ``Site``
- ``Site Themes``

For local devstack, if Otto server is running at ``localhost:8002`` you can enable a ``my-theme`` by
following these steps.

#. Start the Otto Server.
#. In your browser, go to ``http://localhost:8002/admin/sites/site/``.
#. Select **Add site**.
#. For **Domain Name**, enter ``localhost:8002``.
#. For **Display name**, enter ``Otto My Theme``.
#. Select **Save**.
#. In your browser, go to ``http://localhost:8002/admin/theming/sitetheme/``.
#. Select **Site** from dropdown.
#. For **Theme dir name**, enter ``my-theme``.
#. Select **Save**.

Otto server can now be started, and ``my-theme`` should be applied now. If you have overridden sass
styles and you are not seeing those overrides then you need to compile sass files as discussed
in `Compiling Theme Sass`_.

.. _Theming Settings:

****************************
Theming Settings
****************************

Some more settings are also available

#. ``DISABLE_THEMING_ON_RUNTIME_SWITCH``

   There is a waffle switch available to enable/disable themes on run time
   Form Django Admin this switch can be controlled.
#. ``DEFAULT_SITE_THEME``

   ``Default = None`` You can also specify default theme dir, if this value is not set, then
   for sites for which Site Themes are not defined templates and assets will be serverd from
   ``ecommerce/ecommerce/templates`` and ``ecommerce/ecommerce/static`` respectively.

-----------------
Disabling a Theme
-----------------
Theme can be disabled by removing its corresponding ``Site Theme`` entry using django admin.

.. note::
    Comprehensive Theming can be disabled by setting ``ENABLE_COMPREHENSIVE_THEMING`` to ``False``.

    .. code-block:: python

        ENABLE_COMPREHENSIVE_THEMING = False

--------------------
Compiling Theme Sass
--------------------
Management command ``update_assets`` can be used for compiling and collecting themed sass.

.. code-block:: Bash

    python manage.py update_assets

``update_assets`` accepts the following optional arguments

.. list-table::

   * - Option
     - Description & Example

   * - ``--settings``
     - Database ID of a site you want to update.

       .. code-block:: Bash

           python manage.py update_assets
           --settings=ecommerce.settings.production

   * - ``--themes``
     - Space separated list of themes to compile sass for.
       'all' for all themes, 'no' to skip sass compilation for themes,
       ``default: 'all'``

       .. code-block:: Bash

           # compile sass for all themes
           python manage.py update_assets --theme=all

           # compile sass for only given themes, useful for situations
           # if you have installed a new theme and want to compile sass
           # for just this theme
           python manage.py update_assets
           --themes my-theme second-theme third-theme

           # skip sass compilation for themes, useful for testing
           # changes to system sass, keeping theme styles unchanged
           python manage.py update_assets --theme=no

   * - ``--output-style``
     - Coding style for compiled css files. Possible options are ``nested``,
       ``expanded``, ``compact`` and ``compressed``. ``default: 'nested'``

       .. code-block:: Bash

           python manage.py update_assets --output-style='compressed'

   * - ``--skip-system``
     - This flag disables system sass compilation.

       .. code-block:: Bash

           # Useful in cases where you have updated theme
           # sass and system sass is unchanged.
           python manage.py update_assets --skip-system

   * - ``--enable-source-comments``
     - This flag disables system sass compilation.

       .. code-block:: Bash

            python manage.py update_assets --enable-source-comments

   * - ``--skip-collect``
     - This flag can be used to skip collectstatic call after sass compilation.

       .. code-block:: Bash

           # Useful if you just want to compile sass, and collectstatic
           # would later be called, may be by a script
           python manage.py update_assets --skip-collect



---------------
Troubleshooting
---------------
If you have gone through the above procedure and you are not seeing theme overrides, you need to make sure

- ``ENABLE_COMPREHENSIVE_THEMING`` is set to ``True``.
- ``COMPREHENSIVE_THEME_DIRS`` must contain path for the directory containing themes e.g. if your theme is
  ``/edx/app/ecommerce/ecommerce/themes/my-theme`` then correct value for ``COMPREHENSIVE_THEME_DIRS`` is
  ``['/edx/app/ecommerce/ecommerce/themes']``.
- ``domain`` name for site is the name users will put in the browser to access the site, it also includes port number
  e.g. if Otto is running on ``localhost:8002`` then domain should be ``localhost:8002``.
- Theme dir name is the name of the directory of you theme, for our ongoing example ``my-theme``
  is the correct theme dir name.
- Waffle Switch for theming ``DISABLE_THEMING_ON_RUNTIME_SWITCH`` is on.
- Assets are compiled.

.. include:: ../../../links/links.rst
