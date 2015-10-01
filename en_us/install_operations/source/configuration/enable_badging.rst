.. _Enable Badging:

##################
Enabling Badging
##################

This section describes how to enable badging in your instance of Open edX.

.. contents::
   :local:
   :depth: 1

*********
Overview
*********

Badges provide a way for learners to share their course achievements. For
courses that have badges enabled, learners receive a badge at the same time as
they receive a course certificate, and have the option of sharing their badges
to a badging site such as Mozilla Backpack.

Open EdX supports Open Badges, an open standard originally developed by the
Mozilla Foundation. For more information about Open Badges, see
http://openbadges.org/.

Enabling the badges feature on your instance of Open edX involves the
following set up and configuration tasks.

.. Note::  
  Before proceeding, review :ref:`Guidelines for Updating the edX Platform`.

*****************************************************************
Make Sure that Certificates are Enabled
*****************************************************************

Badge generation depends on certificate generation. Badges are automatically
generated when a certificate is generated for a learner. Make sure
certificates are enabled on your Open edX instance. For details, see
:ref:`Enable Certificates`.


*****************************************************************
Install Badgr Server
*****************************************************************

Badgr Server provides an API for issuing Open Badges. Follow the instructions
at https://github.com/concentricsky/badgr-server to install and run Badgr
Server.

.. important:: You must install Badgr Server at a publicly accessible IP
   address, to allow the Open edX LMS and services such as Mozilla Backpack to
   contact Badgr Server.


*****************************************************************
Specify a Badge Issuer for Your Organization
*****************************************************************

Log in to your installation of Badgr Server and add an issuer of Open Badges
for your organization.

For information about issuing Open Badges, see https://wiki.mozilla.org/Badges
/Onboarding-Issuer#Issuing_Badges


*****************************************************************
Enable Badges in Studio and the Learning Management System
*****************************************************************

#. In the ``/cms/envs/common.py`` and ``/lms/envs/common.py`` files, set the
   value of ``ENABLE_OPENBADGES``  to ``True``.

   .. code-block:: bash

     # Enable OpenBadge support. See the BADGR_* settings later in this file.
     'ENABLE_OPENBADGES': True,

#. In ``/lms/envs/common.py``, set the values for the following parameters.
  
   * ``BADGR_API_TOKEN`` - a string containing the API token for the Badgr
     superuser account. Obtain the token from the /v1/user/auth-token page
     while logged in to the API as the superuser.

   * ``BADGR_BASE_URL`` - a string containing the base URL for Badgr Server.
     The Badgr Server must be installed at a publicly accessible IP address.

   * ``BADGR_ISSUER_SLUG`` - a string that is the slug for the Badgr issuer.
     The slug can be obtained from the URL of the Badgr Server page that
     displays the issuer. For example, in the URL
     ``http://exampleserver.com/issuer /test-issuer``, the issuer slug is
     ``test-issuer``.    

   .. code-block:: bash

     ############## Badgr OpenBadges generation ##############

     BADGR_API_TOKEN = None
     # Do not add the trailing slash here.
     BADGR_BASE_URL = "http://localhost:8005"
     BADGR_ISSUER_SLUG = "test-issuer"


#. Save the ``/cms/envs/common.py`` and ``/lms/envs/common.py`` files.

#. Run database migrations.

#. Restart the Studio and Learning Management System processes so that the
   updated environment configurations are loaded.

***************************************************************
Configure Badges and Badge Images for Your Open edX Instance
***************************************************************

#. Access the Django Administration website for your instance of Open edX. To
   do this, go to ``https://<host name of your Open edX instance>/admin``. For
   example, this might be ``https://YourOrganization.org/admin``.

#. Under **Site Administration** > **Certificates**, define a Badge Image
   Configuration for each course mode on your platform for which you want to
   issue badges. For example, "honor" and "verified".

#. For each badge image configuration, set these parameters.

   * Course Mode
   * Icon -- the badge image to use for the specified course mode

   .. important:: Default images are supplied for badges. You must replace the
    default images with your organization's own badge images before any badges
    are issued. When the first badge is issued for a given course, badge images
    are uploaded to Badgr Server. All badges issued in future for this course
    will use the original badge image, even if you subsequently change badge
    images in the Django Administration badge image configuration.

#. Optionally, define a default image for any course modes that do not have an
   explicitly specified badge image. Select **Default** in the badge image
   configuration. 

   .. note:: You can specify only one default badge image.

#. Save each configuration parameter and exit the Django Administration
   website.

*****************************************
Enable Badges Within Each Course
*****************************************

Badge issuing is enabled by default for all courses, but can be turned off or
on again using an advanced setting in Studio. For details, see
:ref:`opencoursestaff:Enable Badges in Course` in *Building and Running an Open
edX Course*.

.. include:: ../../../links/links.rst

