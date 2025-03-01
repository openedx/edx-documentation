.. _Create Products Overview:

###########################
Creating Products Overview
###########################

The edX platform offers several types of products. You create these products in
E-Commerce web pages.

* Course seats represent an :ref:`enrollment track<enrollment_track_g>`. Each
  course seat has an associated set of attributes, such as price and
  certificate availability. The edX code uses course seats to determine how a
  given enrollment should be handled. For more information, see :ref:`Create
  Course Seats`.

* Coupons allow you to offer learners a discount, either percentage or fixed
  amount, on a course enrollment. For more information, see :ref:`Create and
  Manage Coupons`.

* Enrollment codes allow users to purchase bulk enrollments for a course. For
  more information, see :ref:`Enable and Create Enrollment Codes`.

* Programs are collections of related courses. Learners can enroll in and
  purchase courses separately, or you can configure programs to allow one-
  click purchasing of all courses in a program. For more information, see
  :ref:`Programs`.


.. _Start ECommerce Service:

******************************
Start the E-Commerce Service
******************************

Before you can create a product, you must start the E-Commerce service on your
site. Follow these steps to start the E-Commerce service.

#. In the ecommerce and LMS configuration files (``/edx/etc/ecommerce.yml`` and
   ``/edx/app/edxapp/lms.yml``, respectively), verify the following
   settings.

   .. note::
    If you are using `devstack`_, these values are set correctly for you.
    However, edX recommends that you verify these values.

   * The ``EDX_API_KEY`` value in the LMS file must be the same as the
     ``EDX_API_KEY`` value in the ecommerce file. If the values differ, change
     the value in the LMS file to match the ecommerce file.
   * The ``ECOMMERCE_API_SIGNING_KEY`` value in the LMS file must be the same
     as the ``JWT_SECRET_KEY`` value in the ecommerce file. If the values
     differ, change the value in the LMS file to match the ecommerce file.

#. On devstack, start the E-Commerce server on port 8002, and start the LMS
   on port 8000.


.. include:: ../../../../links/links.rst
