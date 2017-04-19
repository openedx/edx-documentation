.. _Enabling Course Visibility in Catalog:

#####################################
Enabling Course Visibility in Catalog
#####################################

#. In lms.env.json and cms.env.json set the values for the following settings:

   .. code-block:: bash

    COURSE_CATALOG_VISIBILITY_PERMISSION: "see_in_catalog",
    COURSE_ABOUT_VISIBILITY_PERMISSION: "see_about_page",

#. Recompile your assets for CMS and LMS. For further informations :ref:`Updating Assets<Assets>`.

#. Restart LMS and CMS services.

***************************
Setting Course Visibility
***************************

#. Select a course from Studio. In the Settings menu, select Advanced Settings.

#. Edit section "Course Visibility in Catalog".

#. This can be set to one of three values:

    * 'both' - show in catalog and allow access to about page
    * 'about' - only allow access to about page
    * 'none' - do not show in catalog and do not allow access to an about page

#. Save

.. include:: ../../../links/links.rst
