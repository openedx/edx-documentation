.. _Install and Start ECommerce:

############################################
Install and Start the E-Commerce Service
############################################

To install and start the edX E-Commerce service, you must complete the
following steps.

.. contents::
   :depth: 1
   :local:

.. note::
 These steps assume that you are running Open edX `devstack`_. If you prefer to
 run the E-Commerce service locally on your computer instead of on the virtual
 machine (VM) that devstack uses, see :ref:`Development Outside Devstack`.


.. include:: ../../../shared/ecom_idas/IDA_virtualenv.rst

.. include:: ../../../shared/ecom_idas/IDA_oidc.rst

.. include:: ../../../shared/ecom_idas/IDA_start_server.rst



.. _Development Outside Devstack:

*******************************
Development Outside Devstack
*******************************

If you are running the LMS in `devstack`_ but would prefer to run the
E-Commerce service on your host, set up a reverse port-forward. This reverse
port-forward allows the LMS process inside your devstack to use
``127.0.0.1:8002`` to make calls to the E-Commerce service running on your
host. This simplifies LMS URL configuration.

To set up a reverse port-forward, execute the following command when you SSH
into your devstack. Make sure that you run this command on the VM host, not the
guest.

.. code-block:: bash

    $ vagrant ssh -- -R 8002:127.0.0.1:8002




.. include:: ../../../links/links.rst
