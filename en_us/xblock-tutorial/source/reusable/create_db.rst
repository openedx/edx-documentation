**************************
Create the SQLite Database
**************************

Before running the XBlock SDK the first time, you must create the SQLite
database.

#. In the ``xblock_development`` directory, run the following command to create
   the database.

   .. code-block:: bash

      (venv) $ python xblock-sdk/manage.py syncdb

#. You are prompted to indicate whether or not to create a Django superuser.

   .. code-block:: bash

      You just installed Django's auth system, which means you don't have any
      superusers defined. Would you like to create one now? (yes/no):

#. Enter ``no``.

   .. code-block:: bash

      (venv) $ python no

.. confirm ^^
