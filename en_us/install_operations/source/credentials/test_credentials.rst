.. _Test Credentials:

###################################
Test Your Credentials Application
###################################

To test new applications that you develop for the Credentials service, you
create and run tests for the Open edX platform first, and then you run a set of
tests that are specific to Credentials.

For more information about tests for the Open edX platform, see
:ref:`Test Features`.

**********************
Tests for Credentials
**********************

When you develop E-Commerce applications, you must run a pre-packaged set of
unit tests, Python tests, and Credentials acceptance tests.

=============================
Run Credentials Unit Tests
=============================

The Credentials unit tests include the unit test suite and quality
checks.

* To run the full unit test, including Pylint and PEP8 quality checks, use the
  following command.

  .. code-block:: bash

     $ make validate

* To validate code quality independently, run the following command.

  .. code-block:: bash

      $ make quality


===================================
Run Credentials Acceptance Tests
===================================

To run specific acceptance tests for the Credentials service, you must complete
the following procedures.

.. contents::
   :depth: 1
   :local:

Configure an XSeries Program and Certificate
************************************************

#. In the Programs Django administration panel, create a new XSeries program
   that includes only the demo course that is installed on Devstack by default.
#. In the Credentials Django administration panel, configure a certificate for
   this XSeries program.


Configure the LMS
********************

To configure the LMS, follow these steps.

#. Verify that the following settings in ``lms.env.json`` are correct.

   .. code-block:: bash

      "CREDENTIALS_ROOT_URL": "http://localhost:8150/"
      "LMS_ROOT_URL": "http://127.0.0.1:8000"
      "OAUTH_ENFORCE_SECURE": false
      "OAUTH_OIDC_ISSUER": "http://127.0.0.1:8000/oauth2"

#. In the Django administration panel, verify that the following two OAuth2
   clients exist. If they do not already exist, :ref:`create a new client
   <Create Register Client>`. For both clients, the client ID and secret must
   match the values of the Credentials ``SOCIAL_AUTH_EDX_OIDC_KEY`` and
   ``SOCIAL_AUTH_EDX_OIDC_SECRET`` settings, respectively.

   .. code-block:: bash

      URL:  http://localhost:8150/
      Redirect URI: http://localhost:8150/complete/edx-oidc/
      Client ID: 'credentials-key'
      Client Secret: 'credentials-secret'
      Client Type: Confidential

      URL:  http://localhost:8004/
      Redirect URI: http://localhost:8004/complete/edx-oidc/
      Client ID: 'programs-key'
      Client Secret: 'programs-secret'
      Client Type: Confidential

#. In the Django administration panel, verify that these OAuth2 clients are
   designated as trusted clients. If this isn't already the case,
   :ref:`designate these clients as trusted clients <Credentials Designate
   the Client as Trusted>`.

#. In the Django administration panel, create a new access token for the
   superuser account. Set the client to the OAuth2 client for credentials.
   Make note of this token; it is required to run the acceptance tests.

#. Make sure that the LMS instance that you will use for testing has only the
   edX demonstration course. By default, most LMS instances include the edX
   demonstration course.

#. Enroll the user in the demonstration course, complete the course, and
   generate a certificate. You may have to allow on-demand certificate
   generation for the course.

   For more information, see :ref:`opencoursestaff:Checking Student Progress
   and Issuing Certificates`.

.. _Configure Credentials Acceptance Tests:

Configure Credentials Acceptance Tests
********************************************

You configure acceptance tests by using the settings in the
``credentials/blob/master/acceptance_tests/config.py`` file. You can use the
default values for most settings in this file. However, you must specify values
for the following settings by using environment variables.

.. list-table::
 :widths: 30 60
 :header-rows: 1

 * - Variable
   - Description
 * - ACCESS_TOKEN
   - The OAuth2 access token used to authenticate requests.
 * - CREDENTIALS_ROOT_URL
   - The URL root for the Credentials service.
 * - JWT_SECRET_KEY
   - This value must match the ``SOCIAL_AUTH_EDX_OIDC_SECRET`` value for the
     Credentials service.
 * - LMS_URL_ROOT
   - The URL root for the LMS.
 * - LMS_USERNAME
   - A username for any current LMS user, to use during testing.
 * - LMS_EMAIL
   - The email address used to sign in to the LMS.
 * - LMS_PASSWORD
   - The password used to sign in to the LMS.
 * - USER_JWT_AUDIENCE
   - This value must match the ``CREDENTIALS_JWT_AUDIENCE`` value for the
     Credentials service.




Run Acceptance Tests
******************************

Run all acceptance tests by executing ``make accept``. To run a specific test,
execute the following command.

.. code-block:: bash

    $ nosetests -v <path/to/the/test/module>

The acceptance tests rely on the :ref:`environment variables that you have
configured <Configure Acceptance Tests>`. For example, when you run the
acceptance tests against local instances of Programs and the LMS, you might
run the following command, replacing values between angle brackets (<>) with
your own values.

.. code-block:: bash

    $ CREDENTIALS_ROOT_URL="http://localhost:8150/" LMS_ROOT_URL="http://127.0.0.1:8000" LMS_USERNAME="<username>" LMS_EMAIL="<email address>" LMS_PASSWORD="<password>" JWT_SECRET_KEY="<secret-key>" ACCESS_TOKEN="<access token>" PROGRAM_ID=<program_id> make accept

When you run the acceptance tests against a production-like staging
environment, you might run the following command.

.. code-block:: bash

    $ CREDENTIALS_ROOT_URL="https://credentials.stage.edx.org" LMS_URL_ROOT="https://courses.stage.edx.org" LMS_USERNAME="<username>" LMS_EMAIL="<email address>" LMS_PASSWORD="<password>" JWT_SECRET_KEY="<secret-key>" ACCESS_TOKEN="<access token>" PROGRAM_ID=<program_id> make accept

.. include:: ../../../links/links.rst
