.. _Retrieve_Extended_Profile_Metadata:

#####################################
Retrieving Extended Profile Metadata
#####################################

This topic describes how an Open edX Administrator can configure their system to
retrieve extended profile metadata stored as part of a user's profile.

.. Note::
  Modifying the software to persist or display the extended profile metadata is
  beyond the scope of this document. This section describes how to enable and
  include the retrieval of extended profile metadata through the User API.

.. contents::
   :local:
   :depth: 2

*********
Overview
*********

The User API has a mechanism to accept and persist extra user metadata as part
of a user's profile. This is called the *Extended Profile*. While there is no
special configuration required to enable the storage of this data, it won't be
*returned* by default.

To enable retrieval of Extended Profile data, an Open edX Administrator must
update their instance's Site Configuration.

Updating the Site Configuration
===============================

An Open edX instance's Site Configuration is managed via Django Admin. To update
the configuration properties for a site, follow these steps.

#. Sign in to the Django administration console for your instance. For example,
   ``http://{your_instance_url}/admin``.

#. Select **Site Configurations**.

#. From the **Site Configurations** menu, select the site you want to update.

#. Enter a new configuration property in the **Site values** section named
   ``extended_profile_fields``. Ensure that the new property is in valid
   JavaScript Object Notion (JSON) format.

   Consider the following example where we want to retrieve an extended profile
   field named ``occupation``.

   .. code-block:: none

      {
        "PLATFORM_NAME": "Online University",
        ...other_fields,
        "extended_profile_fields": [
          "occupation"
        ]
      }

#. Select **Save**.

After the updated Site Configuration is saved, when making a GET request to the
User REST API, we should see the ``occupation`` field returned in our requests:

.. code-block:: none

    {
      ...other_fields,
      "extended_profile": [
        {
          "field_name": "occupation",
          "field_value": {
            "name": "Organic Farmer"
          }
        }
      ]
    }
