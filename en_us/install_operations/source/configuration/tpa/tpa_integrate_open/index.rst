.. _Integrate TPA in Open edX:

##################################################
Integrating Third Party Authentication in Open edX
##################################################

For the Open edX platform, you complete two steps to integrate third party
authentication.

#. Enable the third party authentication feature.
#. Set up a provider.

.. _Enable the Third Party Authentication Feature:

***********************************************
Enable the Third Party Authentication Feature
***********************************************

By default, third party authentication is not enabled on Open edX
installations. To enable this feature, follow these steps.

#. In the ``edx/app/edxapp/lms.env.json`` file, edit the file so that it
   includes the following line in the features section.

   .. code-block:: none

       "FEATURES" : {
           ...
           "ENABLE_COMBINED_LOGIN_REGISTRATION": true,
           "ENABLE_THIRD_PARTY_AUTH": true
       }

#. Save the ``edx/app/edxapp/lms.env.json`` file.

For information about enabling third party auth on Edge, see :ref:`Enabling
Third Party Authentication Edge`.

***********************************************
Set Up a Third Party Authentication Provider
***********************************************

You can set up an OAuth or SAML provider. For information about the differences
between the two providers, see :ref:`Supported Identity Providers`.

.. toctree::
   :maxdepth: 1

   tpa_oauth
   tpa_SAML_IdP

