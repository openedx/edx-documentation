This section provides information about problems that you might encounter when
using Open edX virtual machines (VMs). Open edX VMs are devstack,
fullstack, or analytics devstack installations.

=============================================
Time out Error While Creating an Open edX VM
=============================================

In some cases, you might see a time out error when you attempt to create an edX
VM. For example, you might see the following error message during a virtual
machine installation.

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

=================================================
Starting Open edX Servers after a MongoDB Failure
=================================================

If you do not stop Open edX servers such as the LMS before halting the Vagrant
VM that they are running on, the server leaves a `MongoDB® database`_ lock file
in place. This lock file will prevent the Open edX server from starting MongoDB
when you try to start the server again.

The following error message appears in the console when this problem occurs.

.. code-block:: none

    File "/edx/app/edxapp/venvs/edxapp/local/lib/python2.7/site-
    packages/pymongo/mongo_client.py", line 425, in __init__ raise
    ConnectionFailure(str(e)) pymongo.errors.ConnectionFailure: [Errno 111]
    Connection refused

Invoke the following commands as the ``vagrant`` user on the VM to remove the
MongoDB lock file, restore its configuration, and start the database service.
After you invoke these commands, you can start the Open edX server again.

.. code-block:: shell

    sudo rm /edx/var/mongo/mongodb/mongod.lock
    sudo mongod -repair --config /etc/mongod.conf
    sudo chown -R mongodb:mongodb /edx/var/mongo/.
    sudo service mongod start

.. include:: ../../../../links/links.rst
