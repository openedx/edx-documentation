.. _Activating a Theme:

******************
Activating a Theme
******************

To activate a theme, you must first install your theme onto the same server
that is running Open edX. If you are using devstack or fullstack, you must
be sure that the theme is present on the Vagrant virtual machine. If you
are installing Open edX onto a server using the configuration scripts,
you must update the configuration scripts to install your theme onto the server,
as well. It is up to you where to install the theme on the server, but
a good default location is ``/edx/app/edxapp/themes/my-theme``.

There are three core variables that must be updated to enable a
comprehensive theme:

- ``ENABLE_COMPREHENSIVE_THEMING`` - a Boolean value that enables the
  comprehensive theme system.
- ``COMPREHENSIVE_THEME_DIRS`` - specifies the location(s) of your theme folders.
- ``DEFAULT_SITE_THEME`` - specifies the name of the default theme.

Once the theme is installed on the server, you can activate it by setting
the ``EDXAPP_COMPREHENSIVE_THEME_DIRS`` Ansible variable to contain the full paths of
your base theme directories. You can do that by adding the following value to your
``/edx/app/edx_ansible/server-vars.yml`` file:

.. code-block:: yaml

    EDXAPP_ENABLE_COMPREHENSIVE_THEMING: True
    EDXAPP_COMPREHENSIVE_THEME_DIRS:
      - /edx/app/themes
    EDXAPP_DEFAULT_SITE_THEME: my-theme

Where ``/edx/app/edxapp/themes`` is the path to the base directory where you have
installed the theme on your server, and ``my-theme`` is the name of the
directory containing your theme.

To propogate this variable to the ``lms.env.json`` file, you run Ansible.

.. code-block:: bash

    sudo /edx/bin/update edx-platform master

Alternatively, the ``lms.env.json`` file can be modified directly to set these
variables:

.. code-block:: none

  ENABLE_COMPREHENSIVE_THEMING: true,
  COMPREHENSIVE_THEME_DIRS: ["/edx/app/themes" ],
  DEFAULT_SITE_THEME: "my-theme"

You will then need to restart the LMS in order for it to pick up these values
from the ``lms.env.json`` file.

Test that your theme is activated by visiting the LMS in your browser, and
verifying that the changes in your theme appear on your Open edX installation.
