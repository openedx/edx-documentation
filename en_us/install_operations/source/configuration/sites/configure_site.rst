.. _Configuring Sites Independently:

#################################
Configuring Sites Independently
#################################

You can set configuration properties independently for individual sites. The
values that you define for individual sites override the default values that
are present in the ``cms.env.json`` or ``lms.env.json`` files. For example, you
can set the ``PLATFORM_NAME`` property to a different value for each of your
sites to indicate that the sites present courses for different organizations or
audiences.

*******************
Configuring a Site
*******************

To set configuration properties for a site, follow these steps.

#. Sign in to the Django administration console for your base URL. For example,
   ``http://{your_URL}/admin``.

#. Select **Site Configurations** .

#. Select **Add site configuration**.

#. From the **Site** menu, select the site you want to configure.

#. Enter configuration properties in the **Values** field. Structure all
   properties in valid JavaScript Object Notation (JSON) format.

   The following example shows a set of configuration properties for a site.

   .. code-block:: json

       {
         "course_email_from_addr":"courses@onlineu.edu",
         "university":"Online University",
         "PLATFORM_NAME":"Online University",
         "email_from_address":"courses@onlineu.edu",
         "payment_support_email":"payments@onlineu.edu",
         "SITE_NAME":"onlineu.edu",
         "site_domain":"onlineu.edu",
         "SESSION_COOKIE_DOMAIN":"onlineu.edu"
       }

   .. note:: To make courses site-specific, you set the ``course_org_filter``
     property to an organization identifier. Only that organization's courses
     are available from the site.

#. When you are ready for the configuration settings to take effect,
   select **Enabled**.

   The configuration properties that you set do not affect the site
   until you select **Enabled**. If needed, you can return to the **Site
   configurations** screen for this site to enable the configuration properties
   later.

#. Select **Save**.


*******************************
Site Configuration Reference
*******************************

An example of the properties that you define to configure a site follows.

.. code-block:: json

  {
    "ECOMMERCE_API_URL":"https://my-site.sandbox.edx.org/api/v2",
    "ECOMMERCE_PUBLIC_URL_ROOT":"https://my-site.sandbox.edx.org",
    "ECOMMERCE_API_SIGNING_KEY":"ecommerce-secret",
    "COURSE_CATALOG_VISIBILITY_PERMISSION":"see_in_catalog",
    "COURSE_ABOUT_VISIBILITY_PERMISSION":"see_about_page",
    "ENABLE_COMBINED_LOGIN_REGISTRATION":true,
    "ENABLE_PAID_COURSE_REGISTRATION":true,
    "ENABLE_SHOPPING_CART":true,
    "ENABLE_SHOPPING_CART_BULK_PURCHASE":false,
    "course_email_template_name":"my-site",
    "course_email_from_addr":"my-site@example.com",
    "ALLOW_AUTOMATED_SIGNUPS":true,
    "domain_prefix":"my-site",
    "university":"Education Programs",
    "PLATFORM_NAME":"Education Programs",
    "platform_name":"Education Programs",
    "show_only_org_on_student_dashboard":true,
    "email_from_address":"my-site@example.com",
    "payment_support_email":"payments@example.com",
    "SITE_NAME":"my-site.sandbox.edx.org",
    "site_domain":"my-site.sandbox.edx.org",
    "SESSION_COOKIE_DOMAIN":"my-site.sandbox.edx.org",
    "course_org_filter":"MyOrgX",
    "course_index_overlay_text":"<img src='/static/my-site/images/400x103.png' width='400' height='103' />",
    "homepage_overlay_html":"<img src='/static/my-site/images/400x103.png' width='400' height='103' />",
    "payment_email_signature":"Education Programs<br>The Digital Programs Team<br>my-site@example.com<br>101 Example Street<br>Example State"
  }
