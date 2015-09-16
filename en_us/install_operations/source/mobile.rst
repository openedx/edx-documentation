.. _Setting up the Mobile Applications:

############################################
Setting Up the Open edX Mobile Applications
############################################

This section is intended for those are who are building Open edX mobile
applications and customizing an Open edX installation to support their use.

.. contents::
   :local:
   :depth: 1

******************************
Accessing the Source Code
******************************

There are currently two edX mobile applications, one for iOS and one for
Android. You can find the source code and additional documentation for each
application here.

* iOS: http://github.com/edx/edx-app-ios

* Android: http://github.com/edx/edx-app-android

*****************************************
Configuring Mobile Application Features
*****************************************

For the mobile API and authentication to work correctly with the edX mobile
applications, you enable them in the ``lms.env.json`` file. You then complete
the setup for authentication by creating OAuth clients and adding their IDs to
the custom configuration file of each mobile application.

====================================
Enable Mobile Application Features
====================================

.. note:: Configuration settings added to the ``lms.env.json`` file are reset 
 to their default values when you use Ansible to update edx-platform. 

To enable the mobile application features, follow these steps. 

#. In the ``edx/app/edxapp/lms.env.json`` file, add the following lines to the
   features section.

   .. code-block:: json

       "FEATURES" : {
           ...
           "ENABLE_MOBILE_REST_API": true,
           "ENABLE_OAUTH2_PROVIDER": true,
           "ENABLE_COMBINED_LOGIN_REGISTRATION": true
       }

#. Save the ``edx/app/edxapp/lms.env.json`` file.

#. Restart the server.

.. future: add server- and client-side configuration for Google and Facebook sign in, incl. add ``"ENABLE_THIRD_PARTY_AUTH": true`` to the ``"FEATURES"`` list

.. _Create the OAuth Clients:

=======================================
Create the OAuth Clients
=======================================

You create an OAuth client ID and secret that are specific to your
installation for use by the mobile applications. The procedure that follows
assumes that you create a different client for each of the edX mobile
applications.

Before you can create OAuth clients, a superuser must exist on the server. For
more information, see `edX Managing the Full Stack`_.

To create your OAuth clients, follow these steps.

#. Log in to the Django administration console for your base URL. For example,
   ``http://{your_URL}/admin``.

#. In the **Oauth2** section, select **Clients**. 

#. Select **Add client**. A dialog box opens with the **Client id** and
   **Client secret** populated for the new client.

#. Enter a **Url** and **Redirect Url** for the first application. For
   example, ``https://{your_URL}/api/mobile/{version}/?app=ios``. While the
   console requires values for these fields, they are not used by the edX
   mobile applications. You can enter the same value in both fields.

#. For the **Client type**, select **Public**.

#. Optionally, enter a **User** and an identifying **Name**.

#. Select **Save and add another**.

#. Repeat steps 4-6 for the second application, and then select **Save**. 

================================================
Configure the Applications with OAuth Client IDs
================================================

The procedure that follows assumes that you have a different OAuth client ID
for each edX mobile application.

To configure each edX mobile application with its OAuth client ID, you add a setting
to its corresponding custom configuration .yaml file. For information about
how to set up custom configuration directories and files, see the GitHub
repositories for `iOS`_ and `Android`_.

#. Obtain the OAuth client id for the first application from your Django
   administration console. For more information, see :ref:`Create the OAuth
   Clients`.
 
#. In your custom GitHub configuration directory, edit the .yaml file for the
   edX mobile application for iOS. For example, edit your ``ios.yaml`` file.

#. Add the following line to the .yaml file. 
   
   ::

    OAUTH_CLIENT_ID: '{client_id_for_iOS_app}'
   
#. Save the file.

#. Repeat steps 1-4 for the edX mobile application for Android.
   
************************************
Configuring Video Modules for Mobile
************************************

Courseware videos must be specifically prepared to ensure that they are in
mobile accessible formats. Video modules in mobile-available courses should
have low resolution encodings that are readily accessible by mobile
devices.

After you obtain a low resolution encoding for a video file and post it
online, your course team can add its location to the video module that
includes the video in the course structure.

* To configure a video module in edX Studio, you edit the video component. On
  the **Advanced** tab, in the **Video File URLs** field, enter the URL to the
  mobile-targeted video as the first URL in the list. For more information,
  see :ref:`opencoursestaff:Working with Video Components` in *Building and Running an Open edX Course*.

* To configure a video module by editing the course XML, enter the URL to the
  mobile-targeted video as the first URL in the list of ``html5_sources``. For
  more information, see :ref:`olx:Video Components` in the *edX
  Open Learning XML Guide*.

****************************************
Enabling Push Notifications
****************************************

You enable push notifications on the server and then configure each of the edX
mobile applications. Currently, you can use Parse for notification delivery.

The procedures that follow assume that you have obtained an application ID,
REST API key, and client key from Parse.

============================================
Enable Push Notification on the Server  
============================================

To enable the push notification feature, follow these steps. 

#. In the ``edx/app/edxapp/cms.auth.json`` file, add the following lines.

   .. code-block:: json

    PARSE_KEYS = { 
      "APPLICATION_ID": "{app_id}", 
      "REST_API_KEY": "{API_key}" 
    }

2. Save the ``edx/app/edxapp/cms.auth.json`` file.

#. Restart the server.

#. Log in to the Django administration console for your Studio URL. For
   example, ``http://studio.{your_URL}/admin``.

#. In the **Contentstore** section, select **Push notification configs**. 

#. Select **Add push notification config**. 

#. Verify that **Enabled** is selected, and then select **Save**.

=============================================
Configure Push Notification on the Clients
=============================================

The procedure that follows assumes that you use a single set of Parse
credentials for both of the edX mobile applications.

You add push notification settings to the applicable custom configuration
.yaml file. For information about how to set up custom configuration
directories and files, see the GitHub repositories for `iOS`_ and `Android`_.

#. In your custom GitHub configuration directory, edit the .yaml file that
   stores configuration settings that are common to both of the edX mobile
   applications. For example, edit your ``shared.yaml`` file.

#. Add the following lines to the .yaml file.

   ::

    PARSE:
      NOTIFICATIONS_ENABLED: true
      APPLICATION_ID: {your application id}
      CLIENT_KEY: {your client key}

    PUSH_NOTIFICATIONS: true
   
#. Save the file.

.. include:: ../../links/links.rst
