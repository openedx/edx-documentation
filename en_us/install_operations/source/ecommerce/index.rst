.. _Adding ECommerce to Open edX:

##########################################
Adding E-Commerce to the Open edX Platform
##########################################

EdX uses a Django application called ``ecommerce`` to provide the platform with
ecommerce functionality. This `E-Commerce service`_ extends `Oscar`_, an open
source Django ecommerce framework, to manage the edX product catalog and handle
orders for those products. The following sections describe how to install and
use the E-Commerce service with the Open edX platform.

.. toctree::
   :maxdepth: 2

   install_ecommerce
   manage_assets
   create_products/index
   manage_orders
   test_features
   test_ecommerce
   additional_features/index

To complete the procedures that this section describes, you use both the Django
administration site and the Course Administration Tool (CAT). The CAT is a web
app that is included with the E-Commerce service. The CAT enables you to
configure and manage products that are associated with the courses on your
instance of the Open edX learning management system (LMS).

In addition to these required steps, you can add optional features to the
E-Commerce service for your instance of the Open edX platform. For more
information, see :ref:`Additional Ecommerce Features`.


.. include:: ../../../links/links.rst

.. TODO
..   - Oscar Dashboard
..   - Payment processors
..   - API
..   - Course Administration Tool
