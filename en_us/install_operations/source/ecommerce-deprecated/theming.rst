.. _Comprehensive Theming:

######################
Comprehensive Theming
######################

.. warning::
   This service is deprecated and was last tagged for the Redwood release. We are not fixing bugs or developing new features for it. For updates, `follow along on the DEPR ticket <https://github.com/openedx/public-engineering/issues/22>`_


Any application, including Otto, can be loosely divided into two parts:

* the user interface ("how it looks"), and
* the application logic ("how it works").

Considerations of the Otto user interface include, for example, how the
products are laid out on the page, how the selectors look, how the checkout
button is labelled, what sort of fonts and colors are used to display the
text, and so on. Considerations of Otto's application logic includes how Otto
adjusts product price based on discount coupons, and how it records that
information to be displayed in the future.

Theming consists of changing the user interface without changing the
application logic. When you set up an E-Commerce website for use with your
Open edX site, you probably want to use your organization's own logo, modify
the color scheme, change links in the header and footer for SEO (search engine
optimization) purposes, and so on.

However, although the user interface might look different, the application
logic must remain the same so that Otto continues to work properly. A well-
designed theme preserves the general layout and structure of the user
interface, so that users of the website still find it familiar and easy to
use. Be careful about making sweeping changes to the user interface without
warning: your users will be very confused!

The default Open edX theme is named "Comprehensive Theming". You can disable
Comprehensive Theming by setting ``ENABLE_COMPREHENSIVE_THEMING`` to
``False``, as shown in this example, then applying your custom theme.

    .. code-block:: python

        ENABLE_COMPREHENSIVE_THEMING = False


.. contents::
   :local:
   :depth: 1

***************
Theme Structure
***************

From a technical perspective, theming consists of overriding core templates,
static assets, and Sass with themed versions of those resources.

Every theme must conform to a directory structure that mirrors the Otto directory structure.

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


=========
Templates
=========

Any template included in ``ecommerce/templates`` directory can be "themed".
However, make sure not to override class names or ID values of HTML elements
within a template, as these are used by JavaScript or CSS. Overriding these
names and values can cause unwanted behavior.

==================
Static Assets
==================

Any static asset included in ``ecommerce/static`` can be overridden except for
the CSS files in the ``ecommerce/static/css`` directory. CSS styles can be
overridden via Sass overrides explained below.

.. caution:: Theme names must be unique. The names of static assets or
   directories must not be same as the theme's name, otherwise static assets
   will not work correctly.

=====
Sass
=====

Sass overrides are a little different from static asset or template overrides.
There are two types of styles included in ``ecommerce/static/sass``:

* base
* partials

.. caution:: Styles present in ``ecommerce/static/sass/base`` should not be
   overridden as overriding these could result in an unexpected behavior.

Any styles included in ``ecommerce/static/sass/partials`` can be overridden.
Styles included in this directory contain variable definitions that are used
by main Sass files. Elements of the user interface such as header/footer,
background, fonts, and so on, can be updated in this directory.


*****************
Enabling a Theme
*****************

To enable a theme, you must first install your theme onto the same server that
is running Otto. If you are using devstack or fullstack to run Otto, you must
be sure that the theme is present on the Vagrant virtual machine. It is up to
you where to install the theme on the server, but a good default location is
``/edx/app/ecommerce/ecommerce/themes``.

.. note:: All themes must reside in the same physical directory.

In order for Otto to use the installed themes, you must specify the location
of the theme directory in Django settings by defining
``COMPREHENSIVE_THEME_DIRS`` in your settings file, as shown in the example,
where ``/edx/app/ecommerce/ecommerce/themes`` is the path to where you have
installed the themes on your server.

.. code-block:: python

    COMPREHENSIVE_THEME_DIRS = ["/edx/app/ecommerce/ecommerce/themes", ]

You can list all theme directories using this setting.

After you install a theme, you associate it with your site by adding appropriate
entries to the following tables.

*  ``Site``
*  ``Site Themes``

For local devstack, if the Otto server is running at ``localhost:8002`` you can
enable a ``my-theme`` by following these steps.

#. Add a new site with the domain ``localhost:8002`` and the name "Otto My Theme".

#. Add a site theme with the theme dir name ``my-theme``,  selecting
   ``localhost:8002`` from the ``site`` dropdown.

The Otto server can now be started, and you should see that ``my-theme`` has
been applied. If you have overridden Sass styles and you are not seeing those
overrides, then you need to compile Sass files as described in `Compiling
Theme Sass`_.

******************
Disabling a Theme
******************

A theme can be disabled by removing its corresponding ``Site Theme`` entry
using django admin.

=======================================
Creating or Updating Site and SiteTheme
=======================================

If you have already set up ``COMPREHENSIVE_THEME_DIRS``, you can use the
management command for adding ``Site`` and ``SiteTheme`` directly from the
terminal.

.. code-block:: Bash

    python manage.py create_or_update_site_theme --site-domain=localhost:8002 --site-name=localhost:8002 --site-theme=my-theme

The ``create_or_update_site_theme`` command accepts the following optional
arguments, listed below with examples.

* settings: The settings file to use. The default file is
  ``ecommerce.settings.devstack``.

.. code-block:: Bash

    python manage.py create_or_update_site_theme --settings=ecommerce.settings.production

* site-id: The ID of the site that you want to update.

.. code-block:: Bash

    # update domain of the site with id 1 and add a new theme
    # ``my-theme`` for this site
    python manage.py create_or_update_site_theme --site-id=1 --site-domain=my-theme.localhost:8002 --site-name=my-theme.localhost:8002 --site-theme=my-theme

* site-domain: The domain of the site to be created.

.. code-block:: Bash

    python manage.py create_or_update_site_theme --site-domain=localhost:8002 --site-theme=my-theme

* site-name: The name of the site to be created. The default setting is  ``''``.

.. code-block:: Bash

    python manage.py create_or_update_site_theme --site-domain=localhost:8002 --site-name=localhost:8002 --site-theme=my-theme

* site-theme: The theme dir for the new theme.

.. code-block:: Bash

    python manage.py create_or_update_site_theme --site-domain=localhost:8002 --site-name=localhost:8002 --site-theme=my-theme


=====================
Compiling Theme Sass
=====================

You use the management command ``update_assets`` to compile and collect themed
Sass.

.. code-block:: yaml

    python manage.py update_assets

The ``update_assets`` command accepts the following optional arguments, listed
below with examples.

* settings: The settings file to use. The default file is
  ``ecommerce.settings.devstack``.

.. code-block:: Bash

    python manage.py update_assets --settings=ecommerce.settings.production

* themes: The space-separated list of themes to compile Sass for. Possible
  options are ``all`` for all themes, ``no`` to skip Sass compilation for
  themes. The default option is ``all``.

.. code-block:: Bash

    # compile Sass for all themes
    python manage.py update_assets --theme=all

    # compile Sass for only given themes, useful for situations if you have
    # installed a new theme and want to compile Sass for just this theme

    python manage.py update_assets --themes my-theme second-theme third-theme

    # skip Sass compilation for themes, useful for testing changes to system
    # Sass, keeping theme styles unchanged

    python manage.py update_assets --theme=no

* output-style: The coding style for compiled CSS files. Possible options are
  ``nested``, ``expanded``, ``compact`` and ``compressed``. The default option
  is ``nested``.

.. code-block:: Bash

    python manage.py update_assets --output-style='compressed'

* skip-system: This flag disables system Sass compilation.

.. code-block:: Bash

    # useful in cases where you have updated theme Sass, and system Sass is
    # unchanged.

    python manage.py update_assets --skip-system

* enable-source-comments: This flag enables source comments in generated CSS
  files.

.. code-block:: Bash

    python manage.py update_assets --enable-source-comments

* skip-collect: Use this flag to skip the ``collectstatic`` call after Sass
  compilation.

.. code-block:: Bash

    # useful if you just want to compile Sass, and call ``collectstatic`` later,
    # possibly by a script

    python manage.py update_assets --skip-collect


******************
Troubleshooting
******************

If you have gone through the preceding procedures and you are not seeing theme
overrides, check the following areas.


*  ``COMPREHENSIVE_THEME_DIRS`` must contain the path for the directory
   containing themes. For example, if your theme is
   ``/edx/app/ecommerce/ecommerce/themes/my- theme`` then the correct value
   for ``COMPREHENSIVE_THEME_DIRS`` is
   ``['/edx/app/ecommerce/ecommerce/themes']``.

*  The ``domain`` name for site is the name that users will put in the browser
   to access the site, and includes the port number. For example, if Otto is
   running on ``localhost:8002`` then the value for ``domain`` should be
   ``localhost:8002``.

* The theme dir name is the name of the directory of your theme. For example,
  for our ongoing example, ``my-theme`` is the correct theme dir name.
