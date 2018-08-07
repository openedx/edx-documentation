.. _Installing and Updating Devstack:

#################################
Installing and Updating Devstack
#################################

This section provides information about how to install and update
the Open edX developer stack (Devstack).

.. contents::
   :local:
   :depth: 1

.. _Installing the Open edX Developer stack:

***************************************
Installation Prerequisites for Devstack
***************************************


Before you install Devstack, make sure that you have met the
:ref:`installation prerequisites<Installation Prerequisites>`.

.. _Install Devstack:

****************
Install Devstack
****************

To install Devstack, follow these steps.

#. Decide which branch you will be working with.  "master" is the latest code
   in the repositories, changed daily.  Open edX releases are more stable,
   for example, Hawthorn.

#. Check out a local copy of the ``edx/devstack`` repository from
   ``https://github.com/edx/devstack``.

    .. code-block:: bash

     git clone https://github.com/edx/devstack

#. Navigate to the ``devstack`` directory

    .. code-block:: bash

     cd devstack

#. If you are not using the master branch, check out the branch you want.

    .. code-block:: bash

     git checkout open-release/hawthorn.master

#. If you are not using the master branch, define an environment variable for
   the Open edX version you are using, such as ``hawthorn.master`` or
   ``zebrawood.rc1``. Note that unlike a server install, the value of the
   ``OPENEDX_RELEASE`` variable should not use the ``open-release/`` prefix.

    .. code-block:: bash

     export OPENEDX_RELEASE=hawthorn.master

#. Run ``make dev.checkout`` to check out the correct branch in the local
   checkout of each service repository.

    .. code-block:: bash

     make dev.checkout

#. Clone the Open edX service repositories. The Docker Compose file
   mounts a host volume for each service's executing code. The host directory
   defaults to be a sibling of the ``/devstack`` directory. For example, if
   you clone the ``edx/devstack`` repository to ``~/workspace/devstack``, host
   volumes will be expected in ``~/workspace/course-discovery``,
   ``~/workspace/ecommerce``, etc. You can clone these repositories with the
   following command.

    .. code-block:: bash

     make dev.clone

   To customize where the local repositories are found, set the
   ``DEVSTACK_WORKSPACE`` environment variable.

#. (macOS only) Share the cloned service directories in Docker, using
   **Docker -> Preferences -> File Sharing** in the Docker menu.

#. Run the provision command to configure the various services with superusers
   (for development without the auth service) and tenants (for multi-tenancy).

   .. note::
    When you run the provision command, databases for ``ecommerce`` and
    ``edxapp`` will be dropped and recreated.

   Use the following default provision command.

    .. code-block:: bash

     make dev.provision

The default username and password for the superusers are both ``edx``. You can
access the services directly using Django admin at the ``/admin/`` path, or
log in using single sign-on at ``/login/``.

When you have completed these steps, see :ref:`Starting the Open edX Developer
Stack` to begin using Devstack.

For help with running Devstack, see :ref:`Troubleshooting Devstack`.

.. _Updating Devstack:

*****************
Updating Devstack
*****************

EdX publishes new images for Open edX services frequently. After you have
installed and started Devstack, you can update your Devstack installation to
use the most up-to-date versions of the Devstack images by running the
following sequence of commands.

   .. code-block:: bash

    make down
    make pull
    make dev.up

This stops any running Devstack containers, pulls the latest images, and then 
starts all of the Devstack containers.


.. include:: ../../../links/links.rst

