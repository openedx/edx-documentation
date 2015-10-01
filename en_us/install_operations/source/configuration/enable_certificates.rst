.. _Enable Certificates:

#######################
Enabling Certificates
#######################

This section describes how to enable certificates in your instance of Open edX.

.. contents::
   :local:
   :depth: 1

*********
Overview
*********

Organizations and course teams can now generate certificates for learners who
have completed courses. Learners can view, print, or share their certificates.

For information about certificates, see the *Building and Running an Open edX
Course* and *Open edX Learner's* guides.

To enable this feature on your instance of Open edX, you must enable the
feature flag in both Studio and the Learning Management System and perform the
configuration tasks described in this topic.

.. Note::  
  Before proceeding, review :ref:`Guidelines for Updating the edX Platform`.

*****************************************************************
Enable Certificates in Studio and the Learning Management System
*****************************************************************

#. In the ``/cms/envs/common.py`` and ``/lms/envs/common.py`` files, set the
   value of ``CERTIFICATES_HTML_VIEW``  to ``True``.

   .. code-block:: bash

     # Certificates Web/HTML Views
     'CERTIFICATES_HTML_VIEW': True,

#. Save the ``/cms/envs/common.py`` and ``/lms/envs/common.py`` files.

#. If it does not exist already, create the folder ``/tmp/certificates`` owned by
   the user and group ``www-data``. Depending on your configuration, this folder 
   might not survive reboots, and so might need to be created by script.

#. Run database migrations.


**********************************************************
Configure Certificates for Your Open edX Instance
**********************************************************

#. Access the Django Administration website for your instance of Open edX. To
   do this, go to ``https://<host name of your Open edX instance>/admin``. For
   example, this might be ``https://YourOrganization.com/admin``.

#. Under **Site Administration** > **Certificates**, add an HTML View
   Configuration, and select **Enabled**.

#. Modify the configuration parameters. You must set the following
   certificates-related parameters for your Open edX instance.

 * ``platform_name``
 * ``company_about_url``
 * ``company_privacy_url``
 * ``company_tos_url``
 * ``company_verified_certificate_url``
 * ``logo_src``
 * ``logo_url``
  

   For each course mode, such as "honor" or "verified", define
   ``certificate_type``, ``certificate_title`` and
   ``document_body_class_append``. The mode name should match your course mode
   name exactly.

   .. code-block:: bash

    {
        "default": {
            "accomplishment_class_append": "accomplishment-certificate",
            "platform_name": "YourPlatformName", 
            "company_about_url":"http://www.YourOrganization.com/about-us",
            "company_privacy_url": "http://www.YourOrganization.com/our-privacy-policy",
            "company_tos_url": "http://www.YourOrganization.com/our-terms-service",
            "company_verified_certificate_url": "http://www.YourOrganization.com/about_verified_certificates",
            "logo_src": "/static/certificates/images/our_logo.svg",
            "logo_url": "www.YourOrganization.com"
        },
        "honor": {
            "certificate_type": "honor",
            "certificate_title": "Honor Certificate",
            "document_body_class_append": "is-honorcode"
        },
        "verified": {
            "certificate_type": "verified",
            "certificate_title": "Verified Certificate",
            "document_body_class_append": "is-idverified"
        },
        "base": {
            "certificate_type": "base",
            "certificate_title": "Certificate of Achievement",
            "document_body_class_append": "is-base"
        },
        "distinguished": {
            "certificate_type": "distinguished",
            "certificate_title": "Distinguished Certificate of Achievement",
            "document_body_class_append": "is-distinguished"
        }
    }   

4. Save the configuration parameters and exit the Django Administration website.

#. Restart the Studio and Learning Management System processes so that the
   updated environment configurations are loaded.


******************************************************
Customize Certificate Templates For Your Organization
******************************************************

Set up the templates for certificates that your organization will issue. Base
templates are included, but you must ensure that they are customized for your
organization. For example, you can change the images that appear on
certificates for each course mode that your organization supports, as well as
fonts and colors that are used on certificates.

Assets for HTML certificates exist in the following locations.

* **lms/templates/certificates** - this folder contains .html files for
  certificates. The file ``valid.html`` is an example of a certificate file.
  Files with names starting with an underscore, such as
  ``_certificate_footer.html`` are partial files that can be referenced in the
  main certificate .html files

* **lms/static/certificates** - subfolders of this folder contain assets used in
  creating certificates, such as images, fonts, and sass/css files. 

  .. note:: The organization logo on a certificate is uploaded in Studio. For
     details, see :ref:`opencoursestaff:Setting Up Course Certificates` in
     *Building and Running an Open edX Course*.


*****************************************
Configure Certificates Within Each Course
*****************************************

Within Studio, course team members with the Admin role can create and edit a
certificate configuration that is used to generate certificates for their
course, including adding signatories and images for organization logo and
signature images for signatories. For details, :ref:`opencoursestaff:Setting Up
Course Certificates` in *Building and Running an Open edX Course*.


*****************************************
Generate Certificates For a Course
*****************************************

To generate certificates for a course, run the ``manage.py`` script with the
following settings. When the script finishes running, grades are calculated
for learners who are enrolled in the course, and certificates are generated
for eligible learners.

#. Obtain the course ID for the course for which you are generating
   certificates. When you view course content in your browser, the course ID
   appears as part of the URL. For example, in the URL
   ``http://www.edx.org/course/course-v1:edX+demoX_Demo_2015``, the course ID
   is ``course-v1:edX+demoX_Demo_2015``. For some courses, the course ID 
   contains slashes. For example, ``edX/Demox/Demo_2014``. 

#. Run ``manage.py`` with the following settings, replacing ``{CourseID}``
   with the actual course ID. Do not include beginning or trailing slashes.

   ``./manage.py lms --settings=aws ungenerated_certs -c {CourseID}``

   For example, 

   ``./manage.py lms --settings=aws ungenerated_certs -c course-v1:edX+demoX_Demo_2015``.
   
   .. Note:: 
     If the LMS is running on a server that does not have https support 
     (such as a locally run fullstack for testing) you will need to use the ``--insecure``
     flag so that the certificate generation service contacts the lms on http instead of
     https.

3. View the certificate generation status for a course using ``gen_cert_report``. For example,

   ``./manage.py lms --settings=aws gen_cert_report -c course-v1:edX+demoX_Demo_2015``.

.. include:: ../../../links/links.rst
