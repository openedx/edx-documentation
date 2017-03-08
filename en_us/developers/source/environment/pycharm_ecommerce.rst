**************************************
Setting up PyCharm to Debug E-Commerce
**************************************

With the correct run configurations set up, `PyCharm Professional Edition
<https://www.jetbrains.com/pycharm/download/>`_ is capable of starting and
visually debugging an instance of E-Commerce on devstack.

Before following the steps below, you should already have PyCharm Professional
Edition installed and set up PyCharm to remotely debug LMS following `these
instructions <https://openedx.atlassian.net/wiki/display/ENG/Working+with+devstack+and+PyCharm>`_
in the edX wiki.

#. If the 'ecommerce' user on devstack currently has no password, SSH into the
   devstack box and set one.

    .. code-block:: bash

      $ vagrant ssh
      $ sudo passwd ecommerce

#. Tell PyCharm where to find the remote interpreter for E-Commerce.

    #. Open **PyCharm**, **Preferences**, **Project: Devstack**, and then **Project Interpreter**.

    #. Click the button to the right of the interpreter dropdown; select **Add
       Remote** and then **SSH Credentials**.

    #. Specify the following SSH configurations:

        - Host: ``127.0.0.1``
        - Port: ``2222``
        - User name: ``ecommerce``
        - Auth type: ``Password``

          .. note:: If you are having issues authenticating using a password,
            you can also authenticate using an OpenSSH key pair. You should
            inform PyCharm where your private key is located (the default on a
            Mac is ``/Users/insert_your_user_name/.ssh/id_rsa``), then append
            the contents of your public key (default location on a Mac is
            ``/Users/insert_your_user_name/.ssh/id_rsa.pub``) to the file
            ``~edxapp/.ssh/authorized_keys2`` **on devstack**. If this file
            does not already exist on the VM, you will have to create it.

        - Password: the password you set for the ``ecommerce`` user
        - Python interpreter path:
          ``/edx/app/ecommerce/venvs/ecommerce/bin/python``

         .. image:: ../images/ECommerce_SSH_Config.png
          :width: 750
          :alt: Configuration for E-Commerce remote Python interpreter.

        - PyCharm will automatically update the helpers file. Once your
          configuration looks like the above, click **OK**.

#. Set up a debug configuration for E-Commerce:

   #. Go to **Run**, then **Edit Configurations...**. Click on LMS, then click
      the **Copy Configuration** button next to the **-** sign (or hit **⌘D**).
   #. Name the new configuration descriptively; for example, ``eCommerce``.
   #. Change the following configurations:

       - Change the script parameters to ``runserver 0.0.0.0:8002``.
       - On the Python interpreter dropdown menu, select the remote
         configuration created for E-Commerce.

         .. note:: Make sure you do not pick the LMS remote configuration.

       - Set the working directory to ``/edx/app/ecommerce/ecommerce``.
       - Click the ellipsis next to **Path Mappings**; set the local path to
         ``/Users/insert_your_username/devstack/ecommerce//`` and the remote
         path to ``/edx/app/ecommerce/ecommerce``.
       - Click **OK** to save the new E-Commerce configuration.


        .. image:: ../images/ECommerce_Debug_Config.png
         :width: 750
         :alt: Settings for E-Commerce debug configuration.

#. You can now start and debug an instance of E-Commerce on port 8002 from
   PyCharm by choosing **Run**, **Debug...**, and then **eCommerce**. Make sure
   the LMS is also started in PyCharm so E-Commerce can talk to it.

.. include:: ../../../links/links.rst
