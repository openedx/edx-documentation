.. _Enable the Third Party Authentication Feature:

#################################################
Enable the Third Party Authentication Feature
#################################################

By default, third party authentication is not enabled on edX installations. To
enable this feature, follow these steps.

#. In the ``edx/app/edxapp/lms.env.json`` file, edit the file so that it
   includes the following line in the features section.

   .. code-block:: none

       "FEATURES" : {
           ...
           "ENABLE_COMBINED_LOGIN_REGISTRATION": true,
           "ENABLE_THIRD_PARTY_AUTH": true
       }

#. Save the ``edx/app/edxapp/lms.env.json`` file.
