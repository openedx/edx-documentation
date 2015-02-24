.. include:: links.rst

.. _Setting up the Mobile Applications:

######################################
Setting up the edX Mobile Applications
######################################

This chapter is intended for those are who are building the edX mobile
applications and customizing their Open edX installation to support their use.

.. contents:: Chapter Contents:

****
Code
****

There are currently two edX mobile applications, one for iOS and one for Android. You can find the source code and additional documentation for each:

- iOS: http://github.com/edx/edx-app-ios

- Android http://github.com/edx/edx-app-android

**************
Authentication
**************

The edX mobile apps require you to adjust your ``edx-platform`` configuration settings in ``lms.env.json`` to enable mobile API support.

In particular, you need to add the following under the features section:

.. code-block:: json

    "FEATURES" : {
        ...
        "ENABLE_MOBILE_REST_API": true,
        "ENABLE_OAUTH2_PROVIDER": true,
        ...
    }

You also need to set the following configuration value at the top level of the configuration dictionary:

.. code-block:: json

    "OAUTH_ENFORCE_SECURE": ""


Additionally, you need to create an OAuth key and secret specific to your installation for use by the apps. You can do this by logging into the Django administration console at ``<YOUR_EDX_INSTALLATION>/admin``. From there, choose **Clients** under the **Oauth2** section. If you don't already have any clients set up, you will need to add one. Choose **Add client** and create a client. The client id and secret that you see will need to be added to your mobile app configuration. For more information about how to do that, see the documentation for each app linked above.


*****
Video
*****

Courseware videos must be specifically prepared to ensure they're in mobile accessible formats.  Video modules in mobile-available courses should have low resolution encodings that can be readily accessible by mobile devices.  

To configure a video module with a low resolution encoding for mobile, enter the URL to the mobile-targeted video as the first URL in the "Video File URLs" list in the video module's Advanced Editor in edX Studio.

Alternatively, if the course is edited directly in XML, enter the URL to the mobile-targeted video as the first URL in the list of html5_sources.
