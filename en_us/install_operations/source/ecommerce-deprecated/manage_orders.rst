.. _Manage Orders:

##################
Manage Orders
##################

.. warning::
   This service is deprecated and was last tagged for the Redwood release. We are not fixing bugs or developing new features for it. For updates, `follow along on the DEPR ticket <https://github.com/openedx/public-engineering/issues/22>`_


EdX has created a framework that manages order placement and fulfillment for
digital products. Most of the products that edX supports involve modifications
to enrollments.

The edX framework allows modules that fulfill enrollment-related products to
interact with the `edX Enrollment API`_, which is a part of the LMS. This
process can be either synchronous or asynchronous.


******************
Place an Order
******************

To place an order, you need the following information.

* Order number
* User
* Basket
* Shipping method
* Shipping charge
* Billing address
* Order total

To place an order, use the ``handle_order_placement()`` method that
``EdxOrderPlacementMixin`` provides. If you modify this code, make sure that
the code collects payment before it creates order objects.

******************
Fulfill Orders
******************

To fulfill orders, emit a ``post_checkout`` signal. An internal fulfillment API
then delegates fulfillment of individual order items to the appropriate
fulfillment modules.

***************************
About Fulfillment Modules
***************************

The E-Commerce base fulfillment module has the following interface.

.. code-block:: python

    fulfill_product(product)

    revoke_line(line)

Every ``ProductType`` has a corresponding module that extends this interface
and fulfills order items of that particular ``ProductType``. To fulfill an
order, the system gives each fulfillment module configured in settings
(``_oscar.py``) an opportunity to fulfill order lines.

* The ``fulfill_product`` method fulfills the order. For example,
  ``fulfill_product`` might enroll a learner in a course or upgrade the learner
  to a verified certificate).

* The ``revoke_line`` method revokes a specific order line. For example,
  ``revoke_line`` might unenroll learners from courses or downgrade a learner
  from a verified seat.



*************************************
Recover from a Fulfillment Error
*************************************

If a fulfillment operation fails, the E-Commerce service assigns the order a
status indicating the reason for the failure. If you have enabled asynchronous
order fulfillment, the service tries again to fulfill the order. You can also
manually retry fulfillment of a failed order from the `Oscar`_ order dashboard.

.. include:: ../../../links/links.rst

