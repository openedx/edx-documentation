.. _Test Features:

###############
Test Features
###############

.. This topic will move to a different section in the ICR guide after the reorg
.. of the guide is complete.

When you create a new feature for the Open edX platform, you must write two
kinds of tests for that feature: general tests that evaluate the feature on the
Open edX platform, and tests that are specific to the type of feature that you
create. For example, if you create a coupon codes feature for use with the edX
Ecommerce service, you must write both Open edX tests and Ecommerce tests. This
section describes the general tests that you must write for the Open edX
platform.

***********************************
Tests for the Open edX Platform
***********************************

You must write the following types of tests for all new features that you
create for the Open edX platform.

* Django tests. To learn how to test Django code, see the `Testing in Django`_
  documentation provided by the Django Software Foundation.

* Acceptance tests. These tests verify behavior that relies on external
  systems, such as the LMS or payment processors. At a minimum, you must run
  these tests against a staging environment before you deploy code to
  production to verify that critical user workflows are functioning as
  expected. With the right configuration, you can also run the tests locally.


.. include:: ../../../links/links.rst
