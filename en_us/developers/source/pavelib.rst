*******************************************
Paver
*******************************************


Paver provides a standardized way of managing development and operational tasks
in edX.

To run individual commands, use the following syntax.

::

  paver <command_name> --option=<option value>


Paver Commands
*******************************************

Paver commands are grouped as follows:

- Prereqs_ Install all of the prerequisite environments for Python and Node.
- Docs_ Docs is used to build and then optionally display the edX guides
  relating to development, authoring, and data management.
- Assets_ Assets will compile Sass (CSS), Coffeescript (Javascript), and
  XModule assets. Optionally, it can call Django’s ``collectstatic`` method.
- `Run Servers`_ Run servers.


.. _Prereqs:

Prereqs
=============

Install all of the prerequisites for Python and Node.

   **install_prereqs** : installs Node and Python requirements.

::

   paver install_prereqs

..


.. _Docs:

Docs
=============

Docs is used to build and then optionally display the edX guides relating to
development, authoring, and data management.

   **build_docs**:  Invoke sphinx 'make build' to generate docs.

    *--type=* <dev, author, data> Type of docs to compile.

    *--verbose* Display verbose output.

::

   paver build_docs --type=dev --verbose

..


.. _Assets:

Assets
=============

Assets will compile Sass (CSS), CoffeeScript (Javascript), and XModule assets.
Optionally, it can call Django's ``collectstatic`` command.


   **update_assets**: Compiles Coffeescript, Sass, and Xmodule assets, and runs
   ``collectstatic``.

    *system* ``lms`` or ``studio``

    *--settings=* Django settings, for example, ``aws``, ``dev``, ``devstack``
     (the default).

    *--debug* Disable Sass compression.

    *--skip-collect* Skip collection of static assets.

::

   paver update_assets lms

..

.. _Run Servers:

Run Servers
=============

    **lms**: Runs the LMS server.

     *--settings=* Django settings, for example, ``aws``, ``dev``, ``devstack``
     (the default).

     *--fast*   Skip updating assets.

::

   paver lms --settings=dev

..


    **studio**: Runs Studio.

     *--settings=* Django settings, for example, ``aws``, ``dev``, ``devstack``
     (the default).

     *--fast*   Skip updating assets.

::

   paver studio --settings=dev

..


    **run_all_servers**: Runs the ``lms`` server, the ``cms`` server, and the
    ``celery`` workers.

     *--settings=* Django settings, for example, ``aws``, ``dev``, ``devstack``
     (the default).

     *--worker_settings=* Django settings for celery workers.


::

   paver run_all_servers --settings=dev --worker_settings=celery

..


    **run_celery**: Runs celery for a specified system.

     *--settings=* Environment settings, for example, ``aws`` or ``dev``, for
     both the LMS and Studio.

     *--settings_lms=* Override Django settings for the LMS, for example,
     ``lms.dev``.

     *--settings_cms=* Override Django settings for Studio.


::

   paver celery --settings=dev

..

    **update_db**: Runs ``migrate``.

     *--settings=* Django settings, for example, ``aws``, ``dev``, ``devstack``
     (the default).

::

   paver update_db --settings=dev

..


    **check_settings**: Checks settings files.

     *system*: System to check (``lms`` or ``studio``).
     *settings*: Django settings to check.

::

   paver check_settings lms aws

..

