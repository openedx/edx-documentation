.. _Configuring Open edX Sites:

######################################################
Configuring Open edX Sites
######################################################

You can configure multiple sites within your Open edX installation. A site
presents your Open edX courses and content in an individual way. You can
configure sites independently of each other. For example, you can assign
different themes to your Open edX sites.

By default, an Open edX installation has one site. The default site is what
users interact with when they visit your site. You do not need to add multiple
sites to your Open edX installation. You can apply themes to the default site.

Sites are hosted on separate domains or subdomains from your Open edX
installation. You configure the domain name for a site in the Django admin site
when you create it. For example, you might configure one site
with the domain name ``universityofhere.edu`` and another site with the domain
name ``universityofthere.edu``. Or you might configure one site with the domain
name ``arts.myuniversity.edu`` and another site with the domain name
``sciences.myuniversity.edu``.

.. _Create a Site:

****************************************
Create an Open edX Site
****************************************

To create an Open edX site, do the following.

#. Log into the Django admin site for your Open edX site.

#. Select **Sites** to open the ``http://{hostname}/admin/sites/site`` page.

#. Enter the domain name for the site. This is the domain name in the URL for
   the site. For example ``myuniversity.edu``.

.. note::

    If a site is available on a non-default port, and you need to enter the
    port number in the site URL, the domain name must include the port number.
    For example, if an LMS site is available at ``my-site.localhost:8000``, the
    domain name for the site must be ``my-site.localhost:8000``.

.. _Configuring Sites Independently:

****************************************
Configure Sites Independently
****************************************

You can set configuration properties independently for individual sites. For
example, you can set the ``PLATFORM_NAME`` property to different values for
sites to indicate that the sites present courses for different organizations.

.. What is the complete set of configuration properties that you can set for a
.. site? If you set a property for one or more site, do you need to remove it
.. from lms.env.json?

To set configuration properties for an individual site, do the following.

#. Log into the Django admin site for your Open edX site.

#. Select **Site Configurations** to open the
   ``http://{hostname}/admin/site_configuration/siteconfiguration`` page.

#. Select **Add site configuration**.

#. From the **Site** menu, select the site you want to configure.

#. Enter configuration properties in the **Values** field. Structure all
   properties in valid JavaScript Object Notation (JSON) format. This section
   includes an example of site configuration properties in JSON format.

#. If you want the configuration properties to affect the site immediately,
   select **Enabled**. The configuration properties will not affect the site
   until you select **Enabled**. If needed, you can return to the **Site
   configurations** screen for this site to enable the configuration properties
   later.

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
      "SESSION_COOKIE_DOMAIN":"onlineu.edu",
    }

