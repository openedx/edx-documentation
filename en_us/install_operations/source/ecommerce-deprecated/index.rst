.. _Adding ECommerce (Deprecated) to Open edX:

#########################################################
Adding E-Commerce (Deprecated) to the Open edX Platform
#########################################################

.. warning::
   This service is deprecated and was last tagged for the Redwood release. We are not fixing bugs or developing new features for it. For updates, `follow along on the DEPR ticket <https://github.com/openedx/public-engineering/issues/22>`_

edX uses a Django application called ``ecommerce`` to provide the platform with
ecommerce functionality. This `E-Commerce service`_ extends `Oscar`_, an open
source Django ecommerce framework, to manage the edX product catalog and handle
orders for those products. The following sections describe how to install and
use the E-Commerce service with the Open edX platform.

To complete the procedures that this section describes, you use both the
E-Commerce Service's Django administration site and the E-Commerce
Administration Tool (CAT). The CAT is a web app that is included with the
E-Commerce service and enables you to configure and manage products that are
associated with the courses and programs on your instance of the Open edX
learning management system (LMS).

In addition to these required steps, you can add optional features to the
E-Commerce service for your instance of the Open edX platform. For more
information, see :ref:`Additional Ecommerce Features`.


.. toctree::
   :maxdepth: 2

   install_ecommerce
   theming
   manage_assets
   create_products/index
   enable_receipt_page
   manage_orders
   test_ecommerce
   additional_features/index
   internationalization



.. include:: ../../../links/links.rst

.. TODO
..   - Oscar Dashboard
..   - Payment processors
..   - API
..   - Course Administration Tool
