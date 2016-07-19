In some cases, you might see a time out error when you attempt to create an edX
virtual machine. Open edX virtual machines are devstack, fullstack, or
analytics devstack installations.

For example, you might see the following error message during a virtual machine
installation.

.. code-block:: shell

    mount.nfs: mount to NFS server '192.168.33.1:/path/to/edx-platform' failed:
    timed out, giving up

This error happens because the Vagrant virtual machine software that is used by
devstack and fullstack cannot create a host-only network while the host
computer (for example, your laptop) is connected to a virtual private network
(VPN). The Vagrant software can only create the network required by devstack
and fullstack while your VPN software is disconnected. Be sure to disconnect
your VPN before you attempt to install devstack or fullstack.

To correct the error, follow these steps.

#. Stop any VPNs that are active on the host computer.
#. Enter ``vagrant halt`` on the command line from the installation directory
   of your devstack or fullstack environment.
#. Start the Oracle Virtualbox program if it is not running.
#. In Virtualbox, choose **Preferences > Network > Host-only Networks** and
   remove the host-only network that was most recently created.
#. Enter ``vagrant up`` on the command line.

.. include:: ../../../../links/links.rst
