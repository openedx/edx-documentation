

To complete the installation and start the service, follow these
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


