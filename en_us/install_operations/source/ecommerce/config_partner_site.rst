.. _Configure Ecom Partner Site:

###########################################
Configure an E-Commerce Partner and Site
###########################################

To use the E-Commerce service, you must configure both a partner and a site for
the service to use. To configure a partner and a site, you use the Django
administration panel.

.. note::
 The **Site** and **Partner** fields for the ``SiteConfiguration`` model have a
 **unique together** constraint. The model allows only one entry per site, per
 partner. When you configure a site, make sure that only one partner is
 associated with that site.

.. _Ecom Partner Configuration:

**************************************
Configuring an E-Commerce Partner
**************************************

When you configure a partner, you specify a short code that serves as a unique
identifier for that partner. The system creates a **partner** object that
the Open edX platform uses when you perform tasks such as specifying a theme
for a site in the ``SiteConfiguration`` model.

.. _Configure Ecom Partner:

==============================================
Create and Configure an E-Commerce Partner
==============================================

To configure a new partner, follow these steps.

#. In a browser, go to ``http://localhost:8002/admin/partner/partner/`` to view
   the partner model in the Django administration panel.
#. On the home page, select **Add Partner**.
#. On the **Add Partner** page, enter the following values.

   * For **Name**, enter the name of your institution or Open edX instance.
   * For **Short code**, enter a unique value to identify your institution.
     This value is used as the order number prefix (for example, "EDX" is the
     prefix in order number EDX-1000).

#. Select **Save**.


.. _Ecom Site Configuration:

******************************
Configuring an E-Commerce Site
******************************

To configure a site, you use the edX ``SiteConfiguration`` model that extends
the `Django sites framework`_. With this model, you map domains to a **site**
object, which consists of an ID and a name. You can also add and update themes
and payment processors for a site.

The edX E-Commerce service supports multitenancy. The multitenant
implementation has one site per partner.

.. _Configure Ecom Site:

==========================================
Create and Configure an E-Commerce Site
==========================================

To configure an E-Commerce site, follow these steps.

#. Make sure that you have created and configured a partner for the site. For
   more information, see :ref:`Configure Ecom Partner`.
#. In a browser, go to ``http://localhost:8002/admin/core/siteconfiguration``
   to open the **Site configurations** page in the Django administration panel.
#. On the **Site configurations** page, select **Add site configuration**.
#. For a devstack installation, for **Site**, leave the default value of
   ``example.com``.

   For any other installation, for **Site**, use the hostname under which your
   service is running. For example, the hostname may be ``localhost:8002``.

#. For **Partner**, select the name of the institution that you want.
#. For **LMS base url for custom site/microsite**, enter
   ``http://localhost:8000``.
#. For **Path to custom site theme**, enter a path.

   This field is required. If you do not have a custom site theme, enter
   placeholder text in this field. For example, you could enter
   ``sass/themes/default.scss``.

#. For **Payment processors**, enter the names of the payment processor or
   processors for your site.
#. Select **Save**.


.. include:: ../../../links/links.rst
