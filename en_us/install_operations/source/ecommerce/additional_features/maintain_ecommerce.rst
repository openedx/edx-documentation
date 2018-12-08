.. _Maintaining ECommerce:

####################################
Maintaining the E-Commerce Service
####################################

Most of the time, you do not have to perform maintenance on the E-Commerce
service. However, E-Commerce creates **basket** objects to track products that
users want to purchase before users place an order. As more baskets and orders
are created, the baskets table can grow large. Depending on your database
backend, a large table can become difficult to manage and migrate. After an
order is placed, you can delete the corresponding basket from the baskets
table.

To delete one or more baskets, follow these steps.

.. note::
 Baskets that contain products but that are not used to create orders, such as
 when a user adds a product to a basket but does not complete the order
 process, are not deleted. These baskets provide records that users intended to
 purchase a product.

#. To display the number of baskets that you can delete, run the following
   command.

   .. code-block:: bash

     $ ./manage.py delete_ordered_baskets

#. To delete all the baskets that appear after you run the command in step 1,
   use the --commit option.

   .. code-block:: bash

     $ ./manage.py delete_ordered_baskets --commit
