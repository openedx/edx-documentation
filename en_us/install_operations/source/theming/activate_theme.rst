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
a good default location is ``/edx/app/themes/my-theme``.

Once the theme is installed on the server, you can activate it by setting
the ``COMPREHENSIVE_THEME_DIR`` Ansible variable to the full path of your theme's
directory. You can do that by adding the following value to your
``/edx/app/edx_ansible/server-vars.yml`` file:

.. code-block:: yaml

    COMPREHENSIVE_THEME_DIR: "/edx/app/themes/my-theme"

Where ``/edx/app/themes/my-theme`` is the path to where you have installed the
theme on your server.

To propogate this variable to the ``lms.env.json`` file, you run Ansible.

.. code-block:: bash

    sudo /edx/bin/update edx-platform master

You will then need to restart the LMS in order for it to pick up this value
from the ``lms.env.json`` file.

Test that your theme is activated by visiting the LMS in your browser, and
verifying that the changes in your theme appear on your Open edX installation.
