.. include:: ../links.rst

.. _Enable Certificates:

#######################
Enabling Certificates
#######################

In this Open edX release, a new feature allows organizations and course teams
to generate certificates for learners who have completed courses. Learners can
view, print, or share their certificates.

For information about certificates, see the *Building and Running an Open edX
Course* and *Open edX Learner's* guides.

To enable this feature on your instance of Open edX, you must enable the
feature flag in both Studio and the Learning Management System and perform the
configuration tasks described in this topic.

.. Note::  
  Before proceeding, review :ref:`Guidelines for Updating the edX Platform`.

.. contents::
   :local:


*****************************************************************
Enable Certificates in Studio and the Learning Management System
*****************************************************************

#. In the ``/cms/envs/common.py`` and ``/lms/envs/common.py`` files, set the
   value of ``CERTIFICATES_HTML_VIEW``  to ``True``.

   .. code-block:: bash

     # Certificates Web/HTML Views
     'CERTIFICATES_HTML_VIEW': True,

#. Save the ``/cms/envs/common.py`` and ``/lms/envs/common.py`` files.

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

Set up the certificate templates for certificates that your organization will
issue. Base templates are included, but you must ensure that they are
customized for your organization. Assets for HTML certificates exist in the
following locations.

* **lms/templates/certificates** - this folder contains .html files for
  certificates. The file ``valid.html`` is an example of a certificate file.
  Files with names starting with an underscore, such as
  ``_certificate_footer.html`` are partial files that can be referenced in the
  main certificate .html files

* **lms/static/certificates** - subfolders of this folder contain assets used in
  creating certificates, such as images, fonts, and sass/css files. 

  .. note:: The organization logo on a certificate is uploaded in Studio. For
     details, see `Set Up Course HTML Certificates`_ in *Building and Running
     an Open edX Course*.


*****************************************
Configure Certificates Within Each Course
*****************************************

Within Studio, course team members with Admin privileges can create and edit a
certificate configuration that is used to generate certificates for their
course, including adding signatories and images for organization logo and
signature images for signatories. For details, see `Set Up Course HTML
Certificates`_ in *Building and Running an Open edX Course*.


