.. _Troubleshooting the Devstack Installation:

*************************************************
Troubleshooting Virtual Machine Installations
*************************************************

In some cases, you see an error when you attempt to create an edX virtual
machine (``vagrant up``). For example:

``mount.nfs: mount to NFS server '192.168.33.1:/path/to/edx-platform' failed: timed out, giving up``

This error situation arises because Vagrant uses a host-only network in
Virtualbox to communicate with your computer. If a network does not exist, one
is created on ``vagrant up``. If this network is created with the VPN up, it
will not work. You must recreate the network with the VPN down.

To resolve the error, follow these steps.

#. Stop the VPN.
#. Type ``vagrant halt``.
#. Open Virtualbox.
#. Navigate to **Preferences > Network > Host-only Networks** and remove the
   most-recently-created host-only network.
#. Type ``vagrant up``.

.. include:: ../../../links/links.rst
