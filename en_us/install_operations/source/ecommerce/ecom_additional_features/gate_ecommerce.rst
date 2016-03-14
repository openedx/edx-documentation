.. _Gating ECommerce Features:

####################################
Gating E-Commerce Service Features
####################################

You can release new E-Commerce service features and functionality behind a
feature gate. This project uses the `Waffle`_ library for feature gating.

****************************
Types of Feature Gates
****************************

Waffle supports the following types of feature gates.

* Flag: This gate allows you to enable a feature for specific users, groups,
  users who meet certain criteria (such as authenticated users or staff), or a
  certain percentage of visitors.

* Switch: This gate is a Boolean that turns a feature on or off for all
  users.

* Sample: This gate allows you to define the probability with which a given
  feature will be on.

For more information about creating or updating features and feature gates, see
the `Waffle documentation`_.

***************
Feature Gates
***************

Waffle offers the following feature gates.

.. list-table::
   :widths: 35 10 60
   :header-rows: 1

   * - Name
     - Type
     - Purpose
   * - user_enrollments_on_dashboard
     - Switch
     - Display a user's current enrollments on the dashboard user detail page.
   * - publish_course_modes_to_lms
     - Switch
     - Publish prices and SKUs to the LMS after every course modification.
   * - async_order_fulfillment
     - Sample
     - Specify what percentage of orders are fulfilled asynchronously.
   * - ENABLE_CREDIT_APP
     - Switch
     - Enable the credit checkout page, from which learners can purchase credit
       in a course.
   * - ENABLE_NOTIFICATIONS
     - Switch
     - Enable email notifications for a variety of user actions, such as when
       an order is placed.
   * - PAYPAL_RETRY_ATTEMPTS
     - Switch
     - Enable users to retry unsuccessful PayPal payments.

**********************************
Enable a Feature Permanently
**********************************

If you want to make a feature permanent, remove its feature gate from relevant
code and tests, and delete the gate from the database.


.. include:: ../../../../links/links.rst
