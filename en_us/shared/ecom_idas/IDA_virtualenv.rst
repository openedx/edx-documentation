.. _Set Up a Virtual Environment:

******************************
Set Up a Virtual Environment
******************************

#. Create or activate a Python virtual environment. You execute all of the
   commands described in this section within the virtualenv (unless otherwise
   noted).

   For more information, see `Virtual Environments`_.

#. Run the following command to install dependencies.

   .. code-block:: bash

    $ make requirements

#. (Optional) Create settings overrides that you do not commit to the
   repository. To do this, create a file named
   ``ecommerce/settings/private.py``. The ``ecommerce/settings/local.py`` file
   reads the values in this file, but Git ignores the file.


.. include:: ../../../links/links.rst
