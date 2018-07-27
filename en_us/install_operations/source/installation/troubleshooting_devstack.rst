.. _Troubleshooting Devstack:

########################
Troubleshooting Devstack
########################

If you are having trouble running Devstack on Docker, here are some 
troubleshooting tips.

==============
Check the logs
==============

If a container stops unexpectedly, you can look at its logs for clues::

    docker-compose logs lms

==========================
Update the code and images
==========================

Make sure you have the latest code and Docker images.

Pull the latest Docker images by running the following command from the ``devstack``
directory.

.. code:: sh

   make pull

Pull the latest Docker Compose configuration and provisioning scripts by running
the following command from the ``devstack`` directory.

.. code:: sh

   git pull

The images are built from the master branches of the application repositories 
(for example, ``edx-platform``, ``ecommerce``, etc.). Make sure you are using 
the latest code from the master branches, or have rebased your branches on master.

=====================
Clean the containers
=====================

Sometimes containers end up in strange states and need to be rebuilt. Run
``make down`` to remove all containers and networks. This will **not** remove 
your data volumes.

==============================
Reset your local installation
==============================

Somtimes you just aren't sure what's wrong, if you would like to hit the reset button
run ``make dev.reset``.

Running this command will perform the following steps:

* Bring down all containers.
* Reset all git repositories to the HEAD of master.
* Pull new images for all services.
* Compile static assets for all services.
* Run migrations for all services.

==========
Start over
==========

If you want to completely start over, run ``make destroy``. This command removes
all containers, networks, **and** data volumes.

====================
Resetting a database
====================

In case you botched a migration or just want to start with a clean database.

1. Open up the mysql shell and drop the database for the desired service, using
   the following commands.::

    make mysql-shell
    mysql
    DROP DATABASE (insert database here)

2. From your ``devstack`` directory, run the provision script for the service. The
   provision script should handle populating data such as Oauth clients and
   Open edX users, and running migrations.
   ::

    ./provision-(service_name)

=====================
File ownership change
=====================

If you notice that the ownership of some or all files have changed and you need
to enter your root password when editing a file, you might have pulled changes
to the remote repository from within a container. When you run ``git pull``, git
changes the owner of the files that you pull to the user that runs that command.
Within a container, that is the root user, so git operations should be run
outside of the container.

To fix this situation, change the owner back to yourself outside of the container 
by running the following command.

.. code:: sh

  $ sudo chown <user>:<group> -R .

=======================================
Running LMS commands within a container
=======================================

Most of the ``paver`` commands require a settings flag. If the flag is omitted,
the flag defaults to ``devstack``, which is the settings flag for vagrant-based
devstack instances. If you run into issues running ``paver`` commands in a
docker container, you should append the ``devstack_docker`` flag. For example:

.. code:: sh

  $ paver update_assets --settings=devstack_docker

=======================
Resource busy or locked
=======================

While running ``make static`` within the ecommerce container, you could get an error
saying:

.. code:: sh

  Error: Error: EBUSY: resource busy or locked, rmdir '/edx/app/ecommerce/ecommerce/ecommerce/static/build/'

To fix this, remove the directory manually outside of the container and run the command again.

=======================
No space left on device
=======================

If you see the error ``no space left on device`` on a Mac, Docker has run
out of space in its ``Docker.qcow2`` file.

Here is an example of this error while running ``make pull``.

.. code:: sh

   ...
   32d52c166025: Extracting [==================================================>] 
   1.598 GB/1.598 GB ERROR: failed to register layer: Error processing tar 
   file(exit status 1): write /edx/app/edxapp/edx-platform/.git/objects/pack/
   pack-4ff9873be2ca8ab77d4b0b302249676a37b3cd4b.pack: no space left on device
   make: *** [pull] Error 1

To address this error, first try the following command to clean up dangling 
images.

.. code:: sh

   docker image prune -f  # (This is very safe, so try this first.)

If you are still seeing issues, you can try cleaning up dangling volumes.

**Warning**: In most cases this removes only volumes that you no longer 
need, but this is not a guarantee.

.. code:: sh

   docker volume prune -f  # (Be careful, this will remove your persistent data!)


============
Memory Limit
============

While provisioning, some have seen the following error:

.. code:: sh

   ...
   Build failed running pavelib.assets.update_assets: Subprocess return code: 137

This error is an indication that your docker process died during execution.  Most likely,
this error is due to running out of memory.  Try increasing the memory
allocated to Docker.

========================================================
Docker is using lots of CPU time when it should be idle
========================================================

On the Mac, this often manifests as the ``hyperkit`` process using a high
percentage of available CPU resources.  To identify the container(s)
responsible for the CPU usage:

.. code:: sh

    make stats

Once you've identified a container using too much CPU time, check its logs.
For example, run the following command to check the LMS logs.

.. code:: sh

    make lms-logs

The most common culprit is an infinite restart loop where an error during
service startup causes the process to exit, but we've configured
``docker-compose`` to immediately try starting it again (so the container will
stay running long enough for you to use a shell to investigate and fix the
problem). Make sure the set of packages installed in the container matches
what your current code branch expects; you may need to rerun ``pip`` on a
requirements file or pull new container images that already have the required
package versions installed.

*******
Support
*******

File any issues you encounter in JIRA under the 
:jira:`PLAT` (Platform) project.


.. include:: ../../../links/links.rst
