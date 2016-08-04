.. _Creating a Theme:

################
Creating a Theme
################

To create a theme, you add a theme directory to the installation-wide themes
directory that you added when you enabled theming for your Open edX
installation. Then, you copy default UI files into your theme directory and
update them to change the appearance of the Open edX site or sites that will
use that theme.

.. contents::
   :local:
   :depth: 1

For more information about the themes directory, see
:ref:`enable_theming`.

.. _understanding_themeable_ui_files:

******************************************
Understanding Which UI Files to Customize
******************************************

You can customize the default images, Sass files, and web application template
files for the Open edX components in your installation.

* To replace an image, you can override any of the images in the
  ``static/images`` directories for the components you are theming.

* For the LMS and Studio, you can customize any of the Sass files in the
  ``static/sass`` directories.

* For the E-commerce service, you can customize any of the Sass files in the
  ``static/sass/partials`` directory.

  .. note:: Do not customize Sass files in the ``static/sass/base`` directory.

* You can override any of the HTML templates in the ``lms/templates`` or
  ``cms/templates`` directories for the components that you want to apply a
  theme to.

UI files for the LMS are stored in the directories shown in the following
example theme directory. You can examine the default UI files in the source
repository of the component that you want to apply the theme to.

.. code-block:: none

    /my-open-edx-themes/edx-platform/my-theme/lms/static/images
    /my-open-edx-themes/edx-platform/my-theme/lms/static/sass
    /my-open-edx-themes/edx-platform/my-theme/lms/templates

***********************************
Example File Path for a Theme File
***********************************

The default Open edX theme includes an image file named ``logo.png`` that
appears in the header of most LMS pages. The file path of that image in the
``edx-platform`` repository is ``lms/static/images/logo.png``.

The following example shows an absolute file path of the LMS logo image in a
theme directory. The file path after
``/my-open-edx-themes/edx-platform/my-theme/`` matches
the relative file path of that image in the default directory for the LMS UI.

.. code-block:: none

    /my-open-edx-themes/edx-platform/my-theme/lms/static/images/logo.png

***************************
Naming a Theme Directory
***************************

The name of the directory that you create to hold your versions of the image,
theme, and Sass styling files identifies the theme. As a result, if you want to
create a theme named ``my-theme``, the name of the directory within your
installation-wide themes directory must be ``my-theme``.

.. note::

    If you add more than one site-specific theme directory, make sure that each
    of the directory names is unique. The Open edX installation looks for a
    theme with a certain name, and selects the first one that matches.

Because the UI files for the LMS and Studio are located together in the
edx-platform repository, you can create one theme that applies to both the LMS
and Studio. If you want to create a theme for the E-commerce service, you must
add a separate theme directory for its files.

The theme directory holds the UI files that override the corresponding
default files.

For example, if the themes directory for your site is ``/my-open-edx-themes``,
the files in the following example create a theme named ``my-theme``.

.. code-block:: none

    /my-open-edx-themes/edx-platform/my-theme/lms/static/images/logo.png
    /my-open-edx-themes/edx-platform/my-theme/lms/static/sass/partials/base/_variables.scss
    /my-open-edx-themes/edx-platform/my-theme/lms/templates/navigation.html
    /my-open-edx-themes/edx-platform/my-theme/cms/static/images/studio-logo.png
    /my-open-edx-themes/edx-platform/my-theme/cms/static/images/logo.png
    /my-open-edx-themes/edx-platform/my-theme/cms/templates/login.html

Because the theme directory includes UI files in both the ``lms`` and ``cms``
subdirectories, you can apply the theme to both the LMS and Studio.

.. note::

    After you create or make changes to a theme, you must update the theme.
    Updating a theme compiles Sass files to create the CSS files that style
    your UI. For more information, see :ref:`Compiling a Theme`.
