.. _Manage Static Assets:

##############################
Manage Static Assets
##############################

.. warning::
   This service is deprecated and was last tagged for the Redwood release. We are not fixing bugs or developing new features for it. For updates, `follow along on the DEPR ticket <https://github.com/openedx/public-engineering/issues/22>`_


After you :ref:`configure a partner and at least one site <Configure a Site
Partner and Site Configuration>` for the E-Commerce system to use, you must
compile all static assets and move them to the correct location to be served.
The edX E-Commerce service uses `django-compressor`_ and `RequireJS`_ to manage
static assets.

* django-compressor compiles and minifies CSS and JavaScript files,
  and names files to facilitate cache busting after new file deployment.

* RequireJS manages JavaScript dependencies.

.. note::

  The static file directories are set up so that ``make static`` reads the
  build output directory of ``r.js`` before it checks for assets in the
  ``ecommerce/static/`` directory. EdX does not recommend that you run ``make
  static`` locally. If you run ``make static`` or ``r.js`` locally, make sure
  you delete the ``ecommerce/static/build`` folder or that you run ``make
  static`` before you continue with development. If you do not run ``make
  static`` again, django-compressor ignores all changes that you make to
  static files.

**********************************
Compile and Move Static Assets
**********************************

To compile and move your static assets and deploy your E-Commerce service,
execute the following command locally or on another server.

.. code-block:: bash

  $ make static

If you create new pages that have RequireJS dependencies, remember to add your
new JavaScript modules to the RequireJS build file for the project. This is the
``build.js`` file.

.. include:: ../../../links/links.rst
