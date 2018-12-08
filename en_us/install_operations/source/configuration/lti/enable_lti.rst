.. _Enable LTI Provider Functionality:

#################################################
Enable LTI Provider Functionality
#################################################

LTI provider functionality is provided in the ``lti_provider`` app, located in
``edx-platform/lms/djangoapps/lti_provider``.

By default, the ``lti_provider`` app is not used by edX installations. To
enable this functionality throughout the platform, follow these steps.

#. In the ``edx/app/edxapp/lms.env.json`` file, edit the file so that it
   includes the following line in the features section.

   .. code-block:: none

       "FEATURES" : {
           ...
           "ENABLE_LTI_PROVIDER": true
       }

#. Save the ``edx/app/edxapp/lms.env.json`` file.

#. Run database migrations.

#. Restart the LMS server.

To verify that the LTI provider functionality is enabled, you can check for the
presence of the following database tables.

::

  lti_provider_gradedassignment
  lti_provider_lticonsumer
  lti_provider_ltiuser
  lti_provider_outcomeservice

If these tables are not present, check that the migrations have run properly.
