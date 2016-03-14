.. _Run Migrations and Start the Server:

************************************
Run Migrations and Start the Server
************************************

To complete the installation and start the E-Commerce service, follow these
steps.

.. note::
    Local installations use SQLite by default. If you use another database
    backend, make sure you update your settings and create the database, if
    necessary, before you run migrations.

#. (Devstack only) If you are using devstack, switch to the ``ecommerce`` user
   and use the ``ecommerce.settings.devstack`` settings module to run the
   following commands.

    .. code-block:: bash

      $ sudo su ecommerce
      $ make devserve

#. To run migrations, execute the following command.

   .. code-block:: bash

      $ make migrate

#. To run the server, execute the following command.

   .. code-block:: bash

     $ python manage.py runserver 8002

   .. note::
     If you use a different port, make sure you update the OIDC client by using
     the Django administration panel in the LMS. For more information about
     configuring the OIDC client, see :ref:`Configure OIDC`.
