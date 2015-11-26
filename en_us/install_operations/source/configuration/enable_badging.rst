.. _Enable Badging:

##################
Enabling Badging
##################

This topic describes how to enable badging in your instance of Open edX.

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

Open edX supports Open Badges, an open standard originally developed by the
Mozilla Foundation. For more information about Open Badges, see
http://openbadges.org/.

Enabling the badges feature on your instance of Open edX involves the
following set up and configuration tasks.

.. Note::
  Before proceeding, review :ref:`Guidelines for Updating the Open edX
  Platform`.

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

For more information about issuing Open Badges, see the `Issuing Badges`_ topic
on the Mozilla wiki.

*****************************************************************
Enable Badges in Studio and the Learning Management System
*****************************************************************

To enable badges, you modify the ``lms.env.json`` and ``cms.env.json`` files,
which are located one level above the ``edx-platform`` directory.

#. In the ``lms.env.json`` and ``cms.env.json`` files, set the
   value of ``ENABLE_OPENBADGES``  to ``True``.

   .. code-block:: bash

     # Enable OpenBadge support. See the BADGR_* settings later in this file.
     'ENABLE_OPENBADGES': True,

#. In ``lms.env.json``, set the values for the following parameters.

   * ``BADGR_API_TOKEN``: A string containing the API token for the Badgr
     superuser account. Obtain the token from the /v1/user/auth-token page while
     logged in to the API as the superuser.

   * ``BADGR_BASE_URL``: A string containing the base URL for Badgr Server. The
     Badgr Server must be installed at a publicly accessible IP address.

   * ``BADGR_ISSUER_SLUG``: A string that is the slug for the Badgr issuer. The
     slug can be obtained from the URL of the Badgr Server page that displays
     the issuer. For example, in the URL ``http://exampleserver.com/issuer/test-issuer``, the issuer slug is ``test-issuer``.

     .. code-block:: bash

       ############## Badgr OpenBadges generation ##############

       BADGR_API_TOKEN = None
       # Do not add the trailing slash here.
       BADGR_BASE_URL = "http://localhost:8005"
       BADGR_ISSUER_SLUG = "test-issuer"

#. Save the ``lms.env.json`` and ``cms.env.json`` files.

#. Run database migrations.

#. Restart the Studio and Learning Management System processes so that the
   updated environment configurations are loaded.

***************************************************************
Configure Badges and Badge Images for Your Open edX Instance
***************************************************************

.. important:: Default images are supplied for badges. You must replace the
  default images with your organization's own badge images before any badges
  are issued. When the first badge is issued for a given course, badge images
  are uploaded to Badgr Server. All badges issued in future for this course
  will use the original badge image, even if you subsequently change badge
  images in the Django Administration badge image configuration.

#. Access the Django Administration website for your instance of Open edX. To
   do this, go to ``https://<host name of your Open edX instance>/admin``. For
   example, this might be ``https://YourOrganization.org/admin``.

#. Under **Site Administration** > **Certificates**, define a Badge Image
   Configuration for each course mode on your platform for which you want to
   issue badges. For example, "honor" and "verified".

#. For each badge image configuration, set these parameters.

   * Course Mode
   * Icon: The badge image to use for the specified course mode.

   .. important:: Be sure to replace the default badge images with your
      organization's own badge images before any badges are issued.

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

******************************************
Configuring Course Event Badges
******************************************

Open edX comes with a handful of optional course events you can customize. Badges 
can be awarded when:

* A student enrolls in a certain number of courses.
* A student receives a completion certificate for a certain number of courses.
* A student receives a completion certificate for every course in a specified list.

These badges can be customized with your own images and descriptions. To set these up:

#. Access the Django Administration website for your instance of Open edX. To
   do this, go to ``https://<host name of your Open edX instance>/admin``. For
   example, this might be ``https://YourOrganization.org/admin``

#. Under **Site Administration** > **Badges** select **Badge Classes**, define some Badge 
   Classes. You will want to make note of the slugs you set, and set the issuing component
   to ``edx__course`` so that they will be recognized by the configuration later. You may
   fill the display name, description and criteria as you wish, though it would be helpful 
   to convey which of the events the badge is for. An example might be:
   
   * ``slug``: ``enrolled_three``
   * ``display_name``: Triple Enrollment
   * ``description``: Enrolled in three courses
   * ``criteria``: A student must enroll in three courses to receive this badge
   * ``image``: Upload a square PNG, under 250KB in size.


#. Go back to the main Admin page. Under **Site Administration** > ** Course event badges 
   configurations**, create a new Course event badges configuration. Each field has example
   help text underneath on how to fill its contents. For example, using the Triple Enrollment
   badge example, you could fill the **Courses Completed** field like so:
   
   ``3,enrolled_three``
  
  .. important:: Be sure to check the ``Enabled`` checkbox before saving, or this configuration
  will not be activated.
  
#. If you made the example badge, test your newly made badge by enrolling in three courses.

.. include:: ../../../links/links.rst
