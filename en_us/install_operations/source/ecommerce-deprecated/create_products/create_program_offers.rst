.. _Create Program Offers:

#####################
Create Program Offers
#####################

Program offers are discounts, either percentage or fixed amount discounts, that
apply to a specific program. When a program offer is active for a program, the
program's price appears discounted both on the program's purchase button and on
the e-commerce checkout page.

You create program offers on the **Create Program Offer** page in the E-Commerce
Program Offers Administration tool, which is located at
``http://localhost:8002/programs/offers``.

.. note:: Each program can be associated with only one program offer.
   To offer a new discount, edit the existing program offer for your program.

To create a program offer, follow these steps.

#. Start the E-Commerce Service on your site. For details, see :ref:`Start
   ECommerce Service`.

#. Obtain the Program UUID for the program for which you are creating an offer.
   Find your program's UUID in the Discovery Service Django administration site,
   under **Course Metadata > Programs**.

#. In a browser on your E-Commerce server, go to
   ``http://localhost:8002/programs/offers/`` to access the E-Commerce Program
   Offers Administration tool.

#. On the **Program Offers** page, select **Create Program Offer**.

#. On the **Create Program Offer** page, enter the following information for
   your program offer.

   * Program UUID
   * Start Date
   * End Date
   * Discount Type - either percentage or absolute.
   * Discount Value - the value of the discount based on the discount type.

.. note:: To ensure that your program discount is reflected even when only some,
   not all, of a program's courses are in a learner's basket for checkout, you
   must select the **Enable Partial Program Offer** setting in the E-Commerce
   Service Django Administration site, under **Core > Site configurations**.

#. Select **Create Program Offer**.

.. include:: ../../../../links/links.rst
