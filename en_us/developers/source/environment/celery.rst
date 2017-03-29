**************************
Running Celery on Devstack
**************************

Testing celery task interaction on devstack requires some caution. In order
to make things simple for the most common cases, the standard ``devstack``
settings cause celery tasks to be run synchronously in the main process.
Running celery tasks synchronously can hide behavior which might cause
unexpected or bad results on sandboxes or other production-like environments.
Some examples follow:

* The sender and the listener for a signal might be in different processes in
  production despite working in devstack (because the celery task ran in the
  web application process).
* Environment variables or Django settings which are used by a task in the web
  application process might not have been set for the celery worker processes.

To test such cases, you can instead use the ``devstack_with_worker`` settings
files to allow for local debugging of this type of situation.  Settings files
with this name exist for both LMS and Studio.

.. note::

  If you need to trigger a Studio task from an LMS web application server
  (or vice versa), you'll need to define ``ALTERNATE_WORKER_QUEUES`` in your
  environment in order to correctly configure the relevant Django settings.

======================
Starting the Processes
======================

The key is that celery and the main web application need to be running in
separate processes. So, start two separate terminal instances, and log into
devstack as usual with each instance.  To start the web application server in
the first terminal, run the following command:

.. code-block:: bash

    $ paver devstack {studio|lms} --settings=devstack_with_worker

And to start celery in the second terminal, run the following command:

.. code-block:: bash

    $ ./manage.py {cms|lms} celery worker --settings=devstack_with_worker

Note that this procedure scales as needed, so if, for example, you want
Studio, LMS, Studio workers, and LMS workers you can open four separate
terminals and run the appropriate commands.
