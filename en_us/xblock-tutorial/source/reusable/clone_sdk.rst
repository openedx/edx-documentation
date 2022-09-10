********************************************
Clone the XBlock Software Development Kit
********************************************

.. include:: ../reusable/sdk_intro.rst

After you :ref:`create and activate the virtual environment <Create and
Activate the Virtual Environment>`, you clone the `XBlock SDK`_ and install its
requirements. To do this, complete the following steps at a command prompt.

#. In the ``xblock_development`` directory, run the following command to clone
   the XBlock SDK repository from GitHub.

   .. code-block:: bash

      (venv) $ git clone https://github.com/openedx/xblock-sdk.git

#. Run the following command to change to the ``xblock-sdk`` directory.

   .. code-block:: bash
  
      (venv) $ cd xblock-sdk

#. Run the following command to install the XBlock SDK requirements.

   .. code-block:: bash
  
      (venv) $ pip install -r requirements/base.txt

#. Run the following command to return to the ``xblock_development`` directory,
   where you will perform the rest of your work.

   .. code-block:: bash
  
      (venv) $ cd ..
