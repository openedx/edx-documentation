.. _enable_theming:

#############################################
Enable Theming for Your Open edX Installation
#############################################

You must enable theming for your Open edX installation before you can apply
themes to your Open edX sites.

To enable theming for your Open edX installation, follow these steps.

#. For each Open edX component that you want to theme, set the
   ``ENABLE_COMPREHENSIVE_THEMING`` configuration property to ``true``.

   .. It would be great to be able to cross-reference to an explanation of the
   .. different ways to set and maintain configuration properties in the
   .. following paragraph.

   The specific method that you use to configure Open edX components depends on
   the type of environment you are using. For example, you can set the
   configuration property in the following files.

   * For the LMS, you edit ``/edx/app/edxapp/lms.env.json`` to set
     ``"ENABLE_COMPREHENSIVE_THEMING": true``.

   * For Studio, you edit ``/edx/app/edxapp/cms.env.json`` to set
     ``"ENABLE_COMPREHENSIVE_THEMING": true``.

   * For the E-commerce service, you edit ``/edx/etc/ecommerce.yml`` to set
     ``ENABLE_COMPREHENSIVE_THEMING: true``.

#. Create a directory to hold the customized UI files for all of the themes
   that you create. This directory will hold subdirectories for each theme.
   Your Open edX installation will look in the directory to find the themes you
   apply to sites.

   You can create this directory at any location on a file system that is
   accessible to your Open edX installation. For example, you might place it at
   the root of the file system in a directory named ``/my-open-edx-themes``.

#. Set the file permissions on the themes directory, and all of its
   subdirectories, to allow the Open edX server users to read and write it in.
   For example, to allow the ``edxapp`` user for the LMS and Studio to read and
   write files in the themes directory, you might use the following commands.

   .. code-block:: bash

     sudo chown -R edxapp:edxapp /my-open-edx-themes
     sudo chmod -R u+rw /my-open-edx-themes

#. For each Open edX component that you want to theme, add the absolute path of
   the themes directory to the ``COMPREHENSIVE_THEME_DIRS`` configuration
   property.

   .. It would be great to be able to cross-reference to an explanation of the
   .. different ways to set and maintain configuration properties in the
   .. following paragraph.

   The specific method that you use to configure Open edX components depends on
   the type of environment you are using. For example, you can set the
   configuration property in the following files.

   * For Studio, add the path to ``COMPREHENSIVE_THEME_DIRS`` in
     ``/edx/app/edxapp/cms.env.json``.

     .. code-block:: none

        "COMPREHENSIVE_THEME_DIRS": [
            "/my-open-edx-themes"
        ],

   * For the LMS, add the path to ``COMPREHENSIVE_THEME_DIRS`` in
     ``/edx/app/edxapp/lms.env.json``.

     .. code-block:: none

        "COMPREHENSIVE_THEME_DIRS": [
            "/my-open-edx-themes"
        ],

   * For the E-commerce service, add the path to ``COMPREHENSIVE_THEME_DIRS``
     in ``/edx/etc/ecommerce.yml``.

     .. code-block:: none

       COMPREHENSIVE_THEME_DIRS: ["/opt/my-open-edx-themes"]

#. Restart all servers.

.. note::

    You can create more than one themes directory for your Open edX
    installation. To use multiple themes directories, include the path to each
    directory in the ``COMPREHENSIVE_THEME_DIRS`` configuration property. The
    following example shows the configuration for multiple themes directories.

    .. code-block:: none

        "COMPREHENSIVE_THEME_DIRS": [
            "/my-open-edx-themes",
            "/my-other-open-edx-themes"
        ],
