.. _Deprecated Mobile Applications:

############################################
Deprecated Open edX Mobile Applications
############################################

.. warning::
   The following instructions refer to the older, now unsupported,
   mobile applications. They were last supported in the Quince release.

   Please see :ref:`Setting up the Mobile Applications` for more on the current apps.

Deprecated Mobile Applications
******************************

Accessing the Source Code
=========================

The deprecated mobile applications, one for iOS and one for
Android, are below. You can find the source code and additional documentation for each
application in the following repositories.

* iOS (`iOS app deprecation ticket <https://github.com/openedx/public-engineering/issues/260>`_): http://github.com/openedx-unsupported/edx-app-ios

* Android (`Android app deprecation ticket <https://github.com/openedx/public-engineering/issues/261>`_): http://github.com/openedx-unsupported/edx-app-android


Configuring Mobile Application Features
=======================================

For the mobile API and authentication to work correctly with the edX mobile
applications, you enable them in the ``edx/app/edxapp/lms.yml`` file. You
then complete the setup for authentication by creating OAuth clients and
adding their IDs to the custom configuration file of each mobile application.

Enable Mobile Application Features
----------------------------------

.. note:: Configuration settings added to the ``lms.yml`` file are reset
 to their default values when you use Ansible to update edx-platform.

To enable the mobile application features, follow these steps.

#. In the ``edx/app/edxapp/lms.yml`` file, add the following lines to the
   features section.

   .. code-block:: none

       "FEATURES" : {
           ...
           "ENABLE_MOBILE_REST_API": true,
           "ENABLE_OAUTH2_PROVIDER": true,
           "ENABLE_COMBINED_LOGIN_REGISTRATION": true
       }

  If you are running in a non-SSL environment, you can set
  ``"OAUTH_ENFORCE_SECURE": false``. This configuration setting should never be
  set to ``false`` in anything other than a development environment.

#. Save the ``edx/app/edxapp/lms.yml`` file.

#. Restart the server.

.. future: add server- and client-side configuration for Google and Facebook sign in, incl. add ``"ENABLE_THIRD_PARTY_AUTH": true`` to the ``"FEATURES"`` list

.. _Create the OAuth Clients:


Create the OAuth Clients
------------------------------

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

#. Enter a **Url** and **Redirect Url** for the first mobile application. For
   example, ``https://{your_URL}/api/mobile/{version}/?app=ios``. While the
   console requires values for these fields, they are not used by the edX
   mobile applications. You can enter the same value in both fields.

#. For the **Client type**, select **Public**.

#. Optionally, enter a **User** and an identifying **Name**.

#. Select **Save and add another**.

#. Repeat steps 4-6 for the second mobile application, and then select
   **Save**.

Configure the Applications with OAuth Client IDs
------------------------------------------------

The procedure that follows assumes that you have a different OAuth client ID
for each edX mobile application.

To configure each edX mobile application with its OAuth client ID, you add a
setting to its custom configuration .yaml file. For information about how to
set up custom configuration directories and files, see the GitHub repositories
for `iOS`_ and `Android`_.

#. Obtain the OAuth client ID for the first mobile application from your
   Django administration console. For more information, see :ref:`Create the
   OAuth Clients`.

#. In your custom GitHub configuration directory, edit the .yaml file for the
   first mobile application. For example, for the edX mobile application for
   iOS, edit your ``ios.yaml`` file.

#. Add the following line to the .yaml file.

   ::

    OAUTH_CLIENT_ID: '{client_id_for_iOS_app}'

#. Save the file.

#. Repeat steps 1-4 for the second mobile application.



.. _Configure OAuth Token Expiration Days:

Configure OAuth Token Expiration
-----------------------------------

When OAuth tokens expire, learners who use the mobile apps to access your site
must log in again.

The ``lms/envs/common.py`` file includes the default configuration settings for
the number of days before OAuth tokens expire for confidential clients and
public clients. Instead of modifying the defaults in ``lms/envs/common.py``, add
the configuration settings to the ``lms.yml`` file and set values that will
override the default settings.

To configure the number of days before OAuth tokens expire, follow these steps.

#. In the ``edx/app/edxapp/lms.yml`` file, add the following lines to
   specify the number of days that OAuth tokens remain valid for confidential
   or public clients.

   .. note:: Make sure you add these lines at the top level of the JSON
      dictionary, and not inside any other declarations.


   .. code-block:: none

      "OAUTH_EXPIRE_CONFIDENTIAL_CLIENT_DAYS" : 365
      "OAUTH_EXPIRE_PUBLIC_CLIENT_DAYS" : 30

#. Save the ``lms.yml`` file, then restart the edxapp app.

   The values that you defined in ``lms.yml`` override the default
   values defined in ``lms/envs/common.py``.


.. _Configuring Video Modules for Mobile:

Configuring Video Modules for Mobile
=====================================

Course videos must be specifically prepared to ensure that they are in
mobile accessible formats. Video modules in mobile-available courses should
have low resolution encodings that are readily accessible by mobile
devices.

After you obtain a low resolution encoding for a video file and post it
online, your course team can add its location to the video module that
includes the video in the course structure.

* To configure a video module in edX Studio, you edit the video component. On
  the **Advanced** tab, in the **Video File URLs** field, enter the URL to the
  mobile-targeted video as the first URL in the list. For more information, see
  :ref:`Working with Video Components` in *Building and Running
  an Open edX Course*.

* To configure a video module by editing the course XML, enter the URL to the
  mobile-targeted video as the first URL in the list of ``html5_sources``. For
  more information, see :ref:`Video Components` in the *edX
  Open Learning XML Guide*.

Enabling Push Notifications
=============================

You enable push notifications on the server and then configure each of the edX
mobile applications. Currently, you can use Parse for notification delivery.

The procedures that follow assume that you have obtained an application ID,
REST API key, and client key from Parse.

Enable Push Notification on the Server
-----------------------------------------

To enable the push notification feature, follow these steps.

#. In the ``edx/app/edxapp/studio.yml`` file, add the following lines.

   .. code-block:: none

    PARSE_KEYS = {
      "APPLICATION_ID": "{app_id}",
      "REST_API_KEY": "{API_key}"
    }

2. Save the ``edx/app/edxapp/studio.yml`` file.

#. Restart the server.

#. Log in to the Django administration console for your Studio URL. For
   example, ``http://studio.{your_URL}/admin``.

#. In the **Contentstore** section, select **Push notification configs**.

#. Select **Add push notification config**.

#. Verify that **Enabled** is selected, and then select **Save**.

Configure Push Notification on the Clients
-----------------------------------------------

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
