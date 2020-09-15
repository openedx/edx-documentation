.. _Enable Custom Course Settings:

####################################
Enabling Custom Course Settings
####################################

To enable course developers to add custom fields to a course on your instance 
of Open edX, you must configure the ``studio.yml`` file in the edX platform.

.. Note::
  Before proceeding, review :ref:`Guidelines for Updating the Open edX
  Platform`.

#. Stop the LMS server.

#. Create or update the file ``studio.yml`` to include the custom course 
   settings feature flag.

   .. code-block:: yaml

     'ENABLE_OTHER_COURSE_SETTINGS': true,

#. Restart the LMS server.

.. include:: ../../../links/links.rst
