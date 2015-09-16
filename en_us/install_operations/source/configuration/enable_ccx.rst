.. _Enable CCX:

####################################
Enabling Custom Courses
####################################

To enable designated users to create custom courses (CCX) on your instance of
Open edX, you must configure the ``server-vars.yml`` file in the edX platform.

.. Note::  
  Before proceeding, review :ref:`Guidelines for Updating the edX Platform`.

#. Stop the LMS server.

#. Create or update the file ``/edx/app/edx_ansible/server-vars.yml`` to
   include the CCX feature flag.

  .. code-block:: yaml

    EDXAPP_FEATURES:
      CUSTOM_COURSES_EDX: true

3. Run the command ``/edx/bin/update``.

  .. code-block:: bash

     sudo /edx/bin/update edx-platform <your-branch-name>

4. Restart the LMS server.

.. include:: ../../../links/links.rst