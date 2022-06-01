.. _Course Live:

###########################
Course Live
###########################

Live app can be used to configure video conferencing LTI tools like Zoom. These tools
will help connect educators and learners within the platform.

.. _Enable or disable course live app
***********************************
Enable or disable course live app
***********************************
Once course live app has been enabled, and an LTI provider has been successfully configured, that provider
will be accessible in "Live" tab in course navigation.

1.  Go to "Pages & Resources" page and click gear icon on the "Live" configuration card.

.. image:: ../../../shared/images/Live_configuration_card.png
   :width: 200
   :alt: Image of Live configuration card

2.  Turn on the toggle on top-right to enable the app.

.. image:: ../../../shared/images/Live_app_configuration.png
   :width: 300
   :alt: Image of Live app configurations

3. Add credentials (if needed) for the selected LTI provider.

4. Click "Save" to enable the selected LTI provider.

Once successfully enabled, the LTI provider will be accessible in "Live" tab in course navigation.


********************************
Provider specific configuration
********************************

At present, edX supports 1 video conferencing LTI provider: Zoom


Zoom setup
==========

Zoom LTI pro app can be used to integrate Zoom video conferencing at the course level.
Course authors will need to generate their own credentials for the Zoom LTI pro app and
add those credentials in Live app configuration for Zoom.

Instructors can use the the LTI Pro app to schedule and start Zoom meetings and students can
see and join these meetings to attend classes, office hours, study groups etc. Learn more about
the app here.

To generate LTI credentials in LTI pro app:

1. Add Zoom LTI pro app to your Zoom account.

2. Navigate to configurations of LTI pro app and add a new credential.

3. Name the credential and select LTI 1.1.

4. LTI URL, LTI Secret, and LTI Key will be auto-generated.

5. In settings of the credential:

   a. Add "instructor_email" to `Email or Employee Unique ID Attribute Name` setting.

   b. Add "https://learning.edx.org" to `Approved Domains` setting.


To configure Zoom, navigate to Live app configurations (see :ref:`Enable or disable course live app`):


1. Copy LTI URL, LTI Secret, and LTI Key from LTI pro app and paste in LTI input fields
in Live app configuration for Zoom.

2. Add the email associated with your Zoom account, in "Launch Email" field.

Once successfully enabled, Zoom will be accessible in "Live" tab in course navigation.

.. image:: ../../../shared/images/Zoom_in_Live_tab.png
   :width: 600
   :alt: Image of Zoom rendered in Live tab

