.. _enable_theming:

##############################
Enabling and Applying Themes
##############################

You must enable the use of themes for your Open edX installation before you can
apply themes to your Open edX sites. If your installation has only one site,
you apply a theme to that default site.

For more information about Open edX sites, see :ref:`Configuring Open edX
Sites`.

.. contents::
   :local:
   :depth: 1

***************
Enable Themes
***************

To enable the use of themes for your Open edX installation, follow these steps.

#. Create an installation-wide themes directory to hold the customized UI files
   for all of the themes that you create. This directory will hold
   subdirectories for each theme. Your Open edX installation will look in the
   directory to find the themes you apply to sites.

   You can create this directory at any location on a file system that is
   accessible to your Open edX installation. For example, you might place it at
   the root of the file system in a directory named ``/my-open-edx-themes``.

#. Set the file permissions on the themes directory, and all of its
   subdirectories, to enable read+write permissions for the Ubuntu user.

   For example, to allow the devstack ``edxapp`` user for the LMS and Studio to
   read and write files in the themes directory, you might use the following
   commands.

   .. code-block:: bash

     sudo chown -R edxapp:edxapp /my-open-edx-themes
     sudo chmod -R u+rw /my-open-edx-themes

   On fullstack and native installations the Ubuntu user is ``www-data``.

#. For each Open edX component that you want to theme, set the
   ``ENABLE_COMPREHENSIVE_THEMING`` configuration property to ``true``.

   The specific method that you use to configure Open edX components depends on
   the type of environment you are using. For example, you can set the
   configuration property in the following files.

   * For the LMS, you edit ``/edx/app/edxapp/lms.env.json`` to set
     ``"ENABLE_COMPREHENSIVE_THEMING": true``.

   * For Studio, you edit ``/edx/app/edxapp/cms.env.json`` to set
     ``"ENABLE_COMPREHENSIVE_THEMING": true``.

   * For the E-commerce service, you edit ``/edx/etc/ecommerce.yml`` to set
     ``ENABLE_COMPREHENSIVE_THEMING: true``.

   If any of these files do not exist, you can add them to define this
   configuration setting.

#. For each Open edX component that you want to apply a theme to, add the
   absolute path of the themes directory to the ``COMPREHENSIVE_THEME_DIRS``
   configuration property.

   The specific method that you use to configure Open edX components depends on
   the type of environment you are using. For example, you can set the
   configuration property in the following files.

   * For Studio, add the path to ``COMPREHENSIVE_THEME_DIRS`` in
     ``/edx/app/edxapp/cms.env.json``.

     .. code-block:: none

        "COMPREHENSIVE_THEME_DIRS": [
            "/my-open-edx-themes/edx-platform"

        ],

   * For the LMS, add the path to ``COMPREHENSIVE_THEME_DIRS`` in
     ``/edx/app/edxapp/lms.env.json``.

     .. code-block:: none

        "COMPREHENSIVE_THEME_DIRS": [
            "/my-open-edx-themes/edx-platform"
        ],

   * For the E-commerce service, add the path to ``COMPREHENSIVE_THEME_DIRS``
     in ``/edx/etc/ecommerce.yml``.

     .. code-block:: none

       COMPREHENSIVE_THEME_DIRS: ["/my-open-edx-themes/ecommerce"]

#. Restart all servers.

.. note::

    You can create more than one themes directory for your Open edX
    installation. To use multiple themes directories, include the path to each
    directory in the ``COMPREHENSIVE_THEME_DIRS`` configuration property. The
    following example shows the configuration for multiple themes directories.

    .. code-block:: none

        "COMPREHENSIVE_THEME_DIRS": [
            "/my-open-edx-themes/edx-platform",
            "/my-other-open-edx-themes/edx-platform"
        ],

****************************************
Example Settings for Comprehensive Theme
****************************************

For the following file structure:

.. code-block:: none

    edx
    └── my-themes
       └── my-theme-red
            ├── cms
            └── lms
               └── static
               └── templates

set these in lms.env.json and cms.env.json:

.. code:: json

    "COMPREHENSIVE_THEME_DIRS": [
        "/edx/my-themes",
    ],
    "THEME_NAME": "my-theme-red"


************************
Apply a Theme to a Site
************************

To apply a theme to an Open edX site, follow these steps.

#. Make sure that you have enabled theming for your Open edX installation and
   that you have configured an installation-wide themes directory. For more
   information, see :ref:`enable_theming`.

#. Make sure that you have created a theme and that you know the identifier of
   the theme. The identifier of a theme is the name of the directory for that
   theme, within your installation-wide themes directory. For more information,
   see :ref:`Creating a Theme`.

#. Sign in to the Django administration console for your base URL. For example,
   ``http://{your_URL}/admin``.

#. Select **Site themes**.

#. Select **Add site theme**.

#. From the **Site** menu, select the site you want to apply a theme to.

#. In the **Theme dir name** field, enter the identifier of the theme.

#. Select **Save**.

