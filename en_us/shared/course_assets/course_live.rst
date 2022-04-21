.. _Course Live:

###########################
Course Live
###########################

You can add live video conferencing providers like zoom-lti-pro to your course via the course authoring app.


**********************
Zoom Credentials
**********************

Zoom: Course Authors will generate their own credentials for the Zoom LTI pro app.

1. Create or login into a Zoom account.

2. Install zoom-lti-pro app from the marketplace in your account App Marketplace

3. Click configure button or go to this URL https://applications.zoom.us/home/lti/rich

4. Click on create a new credential and add the name of your choice.

5. LTI URL, LTI Secret, and LTI Key will be auto-generated for you and will be used in the next steps.

.. image:: ../../../shared/images/zoom_credentials.png

6. Add Approved domains i.e https://courses.stage.edx.org .

.. image:: ../../../shared/images/zoom_domain.png

7. If your edx platform instructor email does not match your zoom account email you have to follow the next step.

8. In zoom LTI pro configuration add instructor_email in the “Email or Employee Unique ID Attribute Name“ field.

.. image:: ../../../shared/images/zoom_instructor_email.png

**********************
Setup Course Live
**********************

1.  In the course authoring app click on the course live app.

2.  Add credentials ie LTI URL, LTI Secret, LTI Key in the form.

.. image:: ../../../shared/images/course_live_config.png

3.  Add the email id that was used to create the zoom account and credentials in the previous step.


Now navigate to the course home page you should be able to see the new "Live" tab.

**********************
Disable course live
**********************
If you have configured course live but decide to opt-out of it later, follow the following steps.

1.  Go to the course authoring page and click the Live app.

2.  Un-check enabled.

.. image:: ../../../shared/images/course_live_toggle.png

3.  click save.
