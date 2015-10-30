.. _Enabling Social Sharing of Courses and Certificates:

#######################################################
Enabling Social Sharing of Courses and Certificates
#######################################################

This section describes how to configure Open edX so that learners can share
their certificates, and so course teams can enable learners to share their
courses on social media.

.. contents::
 :local:
 :depth: 1

*********
Overview
*********

You can enable learners to share courses and certificates that they earn on
social media sites such as Facebook and Twitter.

To use this feature on your instance of Open edX, you must configure social
sharing settings.

Optionally, you can also enable course teams to set custom URLs for social
sharing. If a course team sets a custom course URL, posts to the social sharing
site can include a link back to that URL. If you do not enable custom course
URLS, a link to the course About page in the LMS is used.

.. note::
   Before proceeding, review :ref:`Guidelines for Updating the Open edX
   Platform`.

*******************************
Configure Social Sharing
*******************************

To enable social sharing icons for courses, you modify the ``lms.env.json``
file, which is located one level above the ``edx-platform`` directory.

#. In the ``lms.env.json`` file, modify the ``SOCIAL_SHARING_SETTINGS``
   dictionary as needed.

   .. code-block:: bash

        SOCIAL_SHARING_SETTINGS = {
            'CUSTOM_COURSE_URLS': True,
            'DASHBOARD_FACEBOOK': True,
            'CERTIFICATE_FACEBOOK': True,
            'CERTIFICATE_FACEBOOK_TEXT': None,
            'CERTIFICATE_TWITTER': True,
            'CERTIFICATE_TWITTER_TEXT': None,
            'DASHBOARD_TWITTER': True,
            'DASHBOARD_TWITTER_TEXT': None
        }

   a. For each social sharing icon that you want to enable, set the value of
      the setting to ``True``.

   b. If you set ``DASHBOARD_TWITTER`` or ``CERTIFICATE_TWITTER`` to ``True``,
      you can also specify default text that learners will see in the Twitter
      sharing dialog and that can be included in their tweet. Set the default
      text in the ``DASHBOARD_TWITTER_TEXT`` and ``CERTIFICATE_TWITTER_TEXT``
      values. Learners can edit this text before they select the **Share with
      Twitter** button in the LMS.

   c. If you set ``CUSTOM_COURSE_URLS`` to ``True``, you must `Enable Custom
      Course URLs`_.

#. Configure the ``SOCIAL_MEDIA_FOOTER_NAMES`` array to the order of links
   you want learners to see in the footer.

   .. code-block:: bash

        SOCIAL_MEDIA_FOOTER_NAMES = [
            "facebook",
            "twitter",
            "youtube",
            "linkedin",
            "google_plus",
            "reddit",
        ]

#. Configure the ``SOCIAL_MEDIA_FOOTER_DISPLAY`` dictionary to define how you
   want social media icons to be displayed. For each social media icon you
   enable, you define a ``title``, ``icon``, and ``action``.

   .. code-block:: bash

        "facebook": {
            "title": _("Facebook"),
            "icon": "fa-facebook-square",
            "action": _("Like {platform_name} on Facebook")
        },
        "twitter": {
            "title": _("Twitter"),
            "icon": "fa-twitter",
            "action": _("Follow {platform_name} on Twitter")
        },
        "linkedin": {
            "title": _("LinkedIn"),
            "icon": "fa-linkedin-square",
            "action": _("Follow {platform_name} on LinkedIn")
        }
     }

#. Save the ``lms.env.json`` file.

*****************************************
Enable Custom Course URLs
*****************************************

In addition to enabling the social sharing icons, you can allow course
teams to provide a custom URL for social sharing sites to link back to.

You must set the ``CUSTOM_COURSE_URLS`` parameter to ``True`` in both the
``lms.env.json`` and ``cms.env.json`` files. In the ``cms.env.json`` file, this
parameter is the only social sharing setting.

.. code-block:: bash

    SOCIAL_SHARING_SETTINGS = {
        'CUSTOM_COURSE_URLS': True
    }

When finished, save the ``lms.env.json`` and ``cms.env.json`` files.

=================================
Set a Custom URL for a Course
=================================

When you enable custom course URLs in your instance of Open edX, course teams
can then set custom URLs for their courses.

In Studio **Advanced Settings**, the course team specifies the custom course
URL in the **Social Media Sharing URL** setting.

This URL is provided to the social sharing site for linking back to a course
location. This URL is used only if you have enabled custom URLs in your
instance of Open edX.

.. note:: If custom URLs are enabled but a course team does not provide a
  value in the **Social Media Sharing URL** advanced setting in Studio,
  social sharing icons are not visible in the LMS for that course.

.. include:: ../../../links/links.rst
