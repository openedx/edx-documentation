.. _Test ECommerce:

###################################
Test Your E-Commerce Application
###################################

To test new applications that you develop for the E-Commerce service, you
create and run tests for the Open edX platform first, and then you run a set of
tests that are specific to E-Commerce.

********************
Tests for E-Commerce
********************

When you develop E-Commerce applications, you must run a pre-packaged set of
unit tests, Python tests, and E-Commerce acceptance tests.

=============================
Run E-Commerce Unit Tests
=============================

The E-Commerce unit tests include migrations, the unit test suite, and quality
checks. You can run the full unit test, or save time for a local test by
disabling the migrations. (You can also run the quality checks independent of
the unit test suite.)

* To run the full unit test, including migrations and quality checks, use the
  following command.

  .. code-block:: bash

     $ make validate

  .. note::
    If numerous unit tests fail with an ``OfflineGenerationError`` message, run
    the following command, then try to run unit tests again.

    .. code-block:: bash

       $ DJANGO_SETTINGS_MODULE=ecommerce.settings.test make static

* To run unit tests with quality checks but without migrations, run the
  following command.

  .. code-block:: bash

      $ DISABLE_MIGRATIONS=1 make validate

  .. note::
    We recommend that you only run tests without migrations when you run the
    tests locally.

* To validate code quality independently, run the following command.

  .. code-block:: bash

      $ make quality


Python Unit Tests
********************

When you create E-Commerce tests, use the ``TestCase`` class in
``ecommerce/tests/testcases.py`` to ensure every test has ``Site`` and
``Partner`` objects configured. This will help you test any code that relies on
these models, which are used for multi-tenancy.

* To run all Python unit tests and quality checks, run the following command.

  .. code-block:: bash

      $ make validate_python

* To run all Python unit tests and quality checks *in parallel*, run the
  following command.

  .. code-block:: bash

      $ make fast_validate_python

* To run the Python unit tests in a specific file, such as
  ``ecommerce/courses/tests/test_utils.py``, run the following command and
  substitute the desired file path.

  .. code-block:: bash

      $ DISABLE_ACCEPTANCE_TESTS=True ./manage.py test
      ecommerce.courses.tests.test_utils --settings=ecommerce.settings.test
      --with-ignore-docstrings --logging-level=DEBUG

  Setting the DISABLE_MIGRATIONS variable significantly decreases the time
  needed to run tests by creating the test database directly from Django model
  definitions as opposed to applying the defined migrations.

  .. code-block:: bash

      $ DISABLE_MIGRATIONS=1 DISABLE_ACCEPTANCE_TESTS=True ./manage.py test
      ecommerce.courses.tests.test_utils --settings=ecommerce.settings.test
      --with-ignore-docstrings --logging-level=DEBUG


JavaScript Unit Tests
**********************

The E-Commerce project uses `Jasmine`_ for JavaScript unit testing. To create
these tests, place your tests in the ``ecommerce/static/js/test/specs``
directory, and add a ``_spec`` suffix. For example, your test name may be
``ecommerce/static/js/test/specs/course_list_view_spec.js``.

All JavaScript code must adhere to standards outlined in the `edX JavaScript Style Guide`_. These standards are enforced using `ESLint`_.

* To run all JavaScript unit tests and linting checks, run the following
  command.

  .. code-block:: bash

      $ make validate_js


===================================
Run E-Commerce Acceptance Tests
===================================

To run specific acceptance tests for the E-Commerce service, you must complete
the following procedures.

.. contents::
   :depth: 1
   :local:

Configure the LMS
********************

To configure the LMS, follow these steps.

#. Verify that the following settings in ``/edx/app/edxapp/lms.yml`` are
   correct. ::

       "ECOMMERCE_API_URL": "http://localhost:8002/api/v2/"
       "ECOMMERCE_PUBLIC_URL_ROOT": "http://localhost:8002"
       "JWT_ISSUER": "http://127.0.0.1:8000/oauth2" // Must match the E-Commerce JWT_ISSUER setting
       "OAUTH_ENFORCE_SECURE": false
       "OAUTH_OIDC_ISSUER": "http://127.0.0.1:8000/oauth2"

#. Verify that the following settings in ``/edx/app/edxapp/lms.yml`` are
   correct. ::

       "ECOMMERCE_API_SIGNING_KEY": "insecure-secret-key" // Must match the E-Commerce JWT_SECRET_KEY setting
       "EDX_API_KEY": "PUT_YOUR_API_KEY_HERE" // Must match the E-Commerce EDX_API_KEY setting

#. Verify that an LMS account with staff and superuser permissions exists.

   By default, most devstack and fullstack LMS instances include a user
   account that has staff permissions. This account has the username
   ``staff``, the email address ``staff@example.com``, and the password
   ``edx``. Run the following commands to grant the account superuser
   permissions.

   .. code:: sh

       cd ~/edx-platform
       ./manage.py lms set_superuser staff --settings=devstack


   .. the ecomm version has these commands for granting superuser permissions
   .. to the account:

      ..  ./manage.py lms shell --settings=devstack
          from django.contrib.aut.models import User
          u = User.objects.get(username-'staff')
          u. is_superuser = True
          u.save()

#. Navigate to the OAuth2 Clients section of the Django administration console
   (e.g. http://localhost:8000/admin/oauth2/client/). Sign in using the
   superuser account you created earlier.

   Verify that an OAuth2 client with the following attributes exists.  If one
   does not already exist, :ref:`create a new OAuth 2 client <Create Register
   Client>`.

   The client ID and secret must match the values of the E-Commerce
   ``SOCIAL_AUTH_EDX_OIDC_KEY`` and ``SOCIAL_AUTH_EDX_OIDC_SECRET`` settings,
   respectively. ::

       Name: ecommerce
       URL: http://localhost:8002/
       Redirect URI: http://localhost:8002/complete/edx-oidc/
       Client ID: 'ecommerce-key'
       Client Secret: 'ecommerce-secret'
       Client Type: Confidential (Web applications)
       Logout url: http://localhost:8002/logout/

#. Navigate to the Edx\_Oauth2\_Provider Trusted clients section of the Django
   administration console (http://localhost:8000/admin/edx_oauth2_provider/trustedclient/).

   Verify that the OAuth2 client referred to above is designated as a
   trusted client (look for the Redirect URI). If this isn't already
   the case, add the client created above as a new trusted client.

#. In the Django administration panel, create a new access token for
   the superuser account. Set the client to the OAuth2 client referred
   to above. Make note of this token; it is required to run the
   acceptance tests.

#. Make sure that the LMS instance that you will use for testing has at least
   two courses that learners can enroll in. By default, most LMS instances
   include the edX demonstration course. Use Studio to create a second course.


Configure E-Commerce
********************

You use the E-Commerce Course Administration Tool ("ECAT") to finish
configuring the two courses in your LMS instance.

#. Become the ``ecommerce`` user.

   .. code:: sh

       sudo su ecommerce

#. Verify that the following keys in ``/edx/etc/ecommerce.yml`` match your
   settings in ``/edx/app/edxapp/lms.yml`` and
   ``/edx/app/edxapp/lms.yml``.

   * One of the ``JWT_AUTH:JWT_ISSUERS`` entries should match
     ``/edx/app/edxapp/lms.yml:JWT_ISSUER``. The default value is
     ``http://127.0.0.1:8000/oauth2``.
   * ``JWT_AUTH:JWT_SECRET_KEY`` should match
     ``/edx/app/edxapp/lms.yml:ECOMMERCE_API_SIGNING_KEY``. The default
     value is ``lms-secret``.
   * ``EDX_API_KEY`` should match
     ``/edx/app/edxapp/lms.yml:EDX_API_KEY``. The default value is
     ``PUT_YOUR_API_KEY_HERE``.

#. Set up the E-Commerce environment.

   .. code:: sh

       cd /edx/app/ecommerce/ecommerce
       source ../ecommerce_env
       source ../venvs/ecommerce/bin/activate
       make requirements
       make static
       make migrate

#. Create a new site linking to the LMS.

   .. code:: sh

       ./manage.py create_or_update_site \
         --site-id=1 \
         --site-domain=localhost:8002 \
         --partner-code=edX \
         --partner-name='Open edX' \
         --lms-url-root=http://localhost:8000 \
         --theme-scss-path=sass/themes/edx.scss \
         --payment-processors=cybersource,paypal \
         --client-id=ecommerce-key \
         --client-secret=ecommerce-secret \
         --from-email staff@example.com

#. Start the E-Commerce Django development server.

   .. code:: sh

       ./manage.py runserver 0.0.0.0:8002

#. Get the course key from the LMS by navigating to a course and examining its
   URL. The course key should look something like
   ``course-v1:edX+DemoX+Demo_Course``.

#. Navigate to the E-Commerce Courses page (http://localhost:8002/courses/) to
   add the two test courses that are on your LMS instance to E-Commerce. Configure
   one course as a "Free (Audit)" course, and the second as a "Verified" course.

#. To configure the "Verified" course, click **Add New Course**. Leave the
   default values in all fields, with the exception of the following fields.

   ::

       Course ID: The course key from the LMS
       Course Name: Use any name
       Course Type: Verified
       Include Honor Seat: No

#. Navigate to the learner dashboard (e.g. http://localhost:8000/dashboard) and
   confirm that the course you added in E-Commerce now has a green "Upgrade to
   Verified" badge, which you can select.

#. In the ECAT, add the second course on your LMS instance to E-Commerce.
   Specify its course type as ``Free (Audit)``.

#. To test integration with external payment processors, update the contents
   of the ``PAYMENT_PROCESSOR_CONFIG`` dictionary found in the settings with
   valid credentials. To override the default values for development, create a
   private settings module, ``private.py``, and set
   ``PAYMENT_PROCESSOR_CONFIG`` inside the module.

   .. note::
     If you created a ``private.py`` file to create settings overrides when you
     :ref:`set up your virtual environment <Set Up a Virtual Environment>`, you
     can use that same ``private.py`` file.

.. _Configure Acceptance Tests:


Configure Acceptance Tests
*********************************

You configure acceptance tests by using the settings in the ``e2e/config.py``
file. You can use the default values for most settings in this file. However,
for the following settings, you must specify values using environment
variables.

  .. ecomm version has this file path instead:
  .. ecommerce/blobmaster/acceptance_tests/config.py

.. list-table::
 :widths: 30 60
 :header-rows: 1

 * - Variable
   - Description
 * - ACCESS_TOKEN
   - The OAuth2 access token used to authenticate requests.
 * - ECOMMERCE_URL_ROOT
   - The URL root for the E-Commerce service.
 * - LMS_URL_ROOT
   - The URL root for the LMS.
 * - LMS_USERNAME
   - A username for any current LMS user, to use during testing.
 * - LMS_EMAIL
   - The email address used to sign in to the LMS.
 * - LMS_PASSWORD
   - The password used to sign in to the LMS.

If you test PayPal integration, you must also specify values for the following
settings by using environment variables.

.. list-table::
 :widths: 30 60
 :header-rows: 1

 * - Variable
   - Description
 * - PAYPAL_EMAIL
   - The email address used to sign in to PayPal during payment.
 * - PAYPAL_PASSWORD
   - The password used to sign in to PayPal during payment.



Run Acceptance Tests
******************************

Run all acceptance tests by executing ``make e2e``.

  .. ecomm version has ``make accept``?

To run a specific test, execute the following command.

.. code-block:: bash

    $ nosetests -v <path/to/the/test/module>

The acceptance tests rely on the :ref:`environment variables that you have
configured <Configure Acceptance Tests>`. For example, when you run the
acceptance tests against local instances of E-Commerce and the LMS, you might
run the following command, replacing values between angle brackets (<>) with
your own values.

::

    $ ECOMMERCE_URL_ROOT="http://localhost:8002" LMS_URL_ROOT="http://127.0.0.1:8000" LMS_USERNAME="<username>" LMS_EMAIL="<email address>" LMS_PASSWORD="<password>" ACCESS_TOKEN="<access token>" LMS_HTTPS="False" LMS_AUTO_AUTH="True" PAYPAL_EMAIL="<email address>" PAYPAL_PASSWORD="<password>" ENABLE_CYBERSOURCE_TESTS="False" VERIFIED_COURSE_ID="<course ID>" make e2e

When you run the acceptance tests against a production-like staging
environment, you might run the following command.

::

    $ ECOMMERCE_URL_ROOT="https://ecommerce.stage.edx.org" LMS_URL_ROOT="https://courses.stage.edx.org" LMS_USERNAME="<username>" LMS_EMAIL="<email address>" LMS_PASSWORD="<password>" ACCESS_TOKEN="<access token>" LMS_HTTPS="True" LMS_AUTO_AUTH="False" PAYPAL_EMAIL="<email address>" PAYPAL_PASSWORD="<password>" BASIC_AUTH_USERNAME="<username>" BASIC_AUTH_PASSWORD="<password>" HONOR_COURSE_ID="<course ID>" VERIFIED_COURSE_ID="<course ID>" make e2e

.. include:: ../../../links/links.rst
