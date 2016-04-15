.. _Starting the Open edX Developer Stack:

#######################################
Starting Open edX Devstack
#######################################

This section describes how to start the components in the Open edX developer
stack (devstack). To do this, you must connect to the devstack virtual machine, and then
start each component.

.. contents::
   :local:
   :depth: 1

.. _Connect to Devstack VM:

********************************************
Connecting to the Devstack Virtual Machine
********************************************

#. To connect to the devstack virtual machine, use the following SSH command
   from the ``devstack`` directory.

   .. code-block:: bash

     vagrant ssh

#. To connect as the **edxapp** user, run the following command.

   .. code-block:: bash

    sudo su edxapp

   This command loads the edxapp environment from the file
   ``/edx/app/edxapp/edxapp_env``. This puts ``venv python`` in your search
   path.

   This command also sets the current working directory to the edx-platform
   repository (``/edx/app/edxapp/edx-platform``).

***********************
Starting the Components
***********************

After you connect to the devstack virtual machine as the **edxapp** user, you
can start the individual components.

================
Starting the LMS
================

When you run the LMS on devstack, the command updates requirements and
compiles assets, unless you use the ``fast`` option.

The command uses the file ``lms/envs/devstack.py``. This file
overrides production settings for the LMS.

To run the LMS on devstack, follow these steps.

#. :ref:`Connect to the Devstack virtual machine<Connect to Devstack VM>`.

#. Run the following command.

   .. code-block:: bash

    paver devstack lms

   Or, to start the LMS without updating requirements and compiling assets, use
   the ``fast`` option.

   .. code-block:: bash

    paver devstack lms --fast

   The LMS starts.

#. Open the LMS in your browser at ``http://localhost:8000/``.

   Vagrant forwards port 8000 to the LMS server running in the virtual machine.

===============
Starting Studio
===============

When you run Studio on devstack, the command updates requirements and compiles
assets, unless you use the ``fast`` option.

You run Studio on devstack with the file ``cms/envs/devstack.py``. This file
overrides production settings for Studio.

To run Studio on devstack, follow these steps.

#. :ref:`Connect to the Devstack virtual machine<Connect to Devstack VM>`.

#. Run the following command.

   .. code-block:: bash

    paver devstack studio

   Or, to start Studio without updating requirements and compiling assets, use
   the ``fast`` option.

   .. code-block:: bash

    paver devstack studio --fast

   Studio starts.

#. Open Studio in your browser at ``http://localhost:8001/``.

   Vagrant forwards port 8001 to the Studio server running in the virtual
   machine.


Viewing Available Studio Commands
************************************


To view all available commands for Studio, enter the following command.

.. code-block:: bash

  ./manage.py cms -h --settings=devstack

=================================
Starting Course Discussions
=================================

To run course discussions on devstack, follow these steps.

#. :ref:`Connect to the Devstack virtual machine<Connect to Devstack VM>`.

#. Switch to the discussion forum account by entering the following command.

   .. code-block:: bash

    sudo su forum

#. Update Ruby requirements.

   .. code-block:: bash

    bundle install

   .. note::
     If you get a message for entering a password to install the bundled
     RubyGems to the system, you can safely exit by entering ``control+c`` on a
     Mac or ``Ctrl+C`` on Windows. The RubyGems will still be installed
     correctly for the forum user.

#. Start the discussion forums server.

   .. code-block:: bash

    ruby app.rb -p 18080

The discussions forum server starts. You can access the discussion forums API
at ``http://localhost:18080/``.



.. include:: ../../../../links/links.rst
