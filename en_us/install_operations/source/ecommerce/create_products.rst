.. _Create Products:

####################
Create Products
####################

After you :ref:`configure a partner <Partner Configuration>` and
:ref:`configure at least one site <Site Configuration>` for the E-Commerce
service to use, and you have compiled and moved your static assests, you can
create products.

EdX products are "course seats" that represent enrollment types. Each course
seat has an associated set of attributes, such as price and certificate
availability. The edX code uses course seats to determine how a given
enrollment should be handled.

To create a product, you use the Course Administration Tool (CAT) to specify a
course type. The E-Commerce service then creates the products, or course
seats, that are associated with that course type. You access the CAT through
your browser, similar to the Django administration panel.

*********************
Create Products
*********************

To create products, follow these steps.

#. In the ecommerce and LMS configuration files (``/edx/etc/ecommerce.yml`` and
   ``/edx/app/edxapp/lms.auth.json``, respectively), verify the following
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
#. On the E-Commerce server, go to ``http://localhost:8002/courses`` to access
   the **Courses** page.
#. On the **Courses** page, select **Add New Course**.
#. On the **Add New Course** page, enter the information for your course in the
   following fields.

   * **Course ID**
   * **Course Name**
   * **Course Type**

#. Select **Create Course**.

To use these products in additional courses, follow these steps again for each
course.

.. include:: ../../../links/links.rst
