.. _Enable Certificates:

#######################
Enabling Certificates
#######################

This topic describes how to enable certificates in your instance of Open edX.

.. contents::
   :local:
   :depth: 1

*********
Overview
*********

Organizations and course teams can generate certificates for learners who pass
a course. Learners can view, print, or share their certificates.

For information about certificates, see :ref:`opencoursestaff:Setting Up Course
Certificates` in *Building and Running an Open edX Course* or
:ref:`openlearners:Print a Web Certificate` in the *Open edX Learner's Guide*.

To enable this feature on your instance of Open edX, you must enable a
feature flag in both Studio and the Learning Management System and complete the
configuration tasks described in this topic.

.. Note::
  Before proceeding, review :ref:`Guidelines for Updating the Open edX
  Platform`.

*****************************************************************
Enable Certificates in Studio and the Learning Management System
*****************************************************************

To enable certificates, you modify the ``lms.env.json`` and ``cms.env.json``
files, which are located one level above the ``edx-platform`` directory.

#. In the ``lms.env.json`` and ``cms.env.json`` files, set the value of
   ``CERTIFICATES_HTML_VIEW`` within the ``FEATURES`` object  to ``true``.

   .. code-block:: bash

     "FEATURES": {
         ...
         'CERTIFICATES_HTML_VIEW': true,
         ...
     }

#. Save the ``lms.env.json`` and ``cms.env.json`` files.

#. If it does not exist already, create the folder ``/tmp/certificates`` owned
   by the user and group ``www-data``. Depending on your configuration, this
   folder might not survive reboots, and so might need to be created by a
   script.

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
   ``certificate_type``, ``certificate_title``, and
   ``document_body_class_append``. The mode name should match your course mode
   name exactly. An example follows.

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

#. Save the configuration parameters and exit the Django Administration
   website.

#. Restart the Studio and Learning Management System processes so that the
   updated environment configurations are loaded.

.. _Discontinue Audit Certificates:

=====================================
Discontinue Audit Track Certificates
=====================================

Organizations that offer certificates to audit track learners who pass a
course can discontinue generation of this type of certificate. For example,
your organization makes a strategic decision to offer certificates only to
learners who select an enrollment mode other than "audit". Learners can
continue to audit courses, but they no longer receive certificates.

An outline of the steps you might take if your organization decides to stop
offering certificates for learners in the audit track follows.

#. Stop advertising audit track certificates for new courses.

#. Identify running courses that offer an audit track certificate and, for
   those courses, determine the course end date that is furthest in the future.

#. Select a cutoff date for generating audit track certificates that is after
   the last course end date identified in step 2.

#. Set ``AUDIT_CERT_CUTOFF_DATE`` to a date in YYYY-MM-DD format. Specifying
   this date ensures that certificates are not generated for audit track
   learners in any course after the specified date.

The ``AUDIT_CERT_CUTOFF_DATE`` feature flag affects only the generation of
audit certificates. Learners who audit courses continue to receive grades,
which are shown on the course **Progress** page.

******************************************************
Customize Certificate Templates For Your Organization
******************************************************

Set up the templates for certificates that your organization will issue. Base
templates are included, but you must ensure that they are customized for your
organization. For example, you can change the images that appear on
certificates for each course mode that your organization supports, as well as
fonts and colors that are used on certificates.

Assets for HTML certificates exist in the following locations.

* ``lms/templates/certificates`` - this folder contains .html files for
  certificates. The file ``valid.html`` is an example of a certificate file.
  Files with names that start with an underscore, such as
  ``_certificate_footer.html``, are partial files that can be referenced in the
  main certificate .html files.

* ``lms/static/certificates`` - subfolders of this folder contain assets used
  in creating certificates, such as images, fonts, and sass/css files.

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

.. _Generate Certificates for a Course:

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
     If the LMS is running on a server that does not have https support (such
     as a locally run fullstack for testing) you will need to use the
     ``--insecure`` flag so that the certificate generation service contacts
     the LMS on http instead of on https.

#. View the certificate generation status for a course using
   ``gen_cert_report``. An example follows.

   ``./manage.py lms --settings=aws gen_cert_report -c course-v1:edX+demoX_Demo_2015``.

.. include:: ../../../links/links.rst
