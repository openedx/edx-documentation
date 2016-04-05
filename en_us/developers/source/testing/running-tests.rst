*************
Running Tests
*************

Before your code is merged to the master branch it needs to pass all of
the automated tests, including unit, integration, acceptance, and accessibility.

All Tests
=========

You can run the entire suite of unit-level tests at once by running the command.

    ``paver test``

This includes Python, JavaScript, and documentation tests. It does not, however,
run any acceptance tests.

**Note:** paver is a scripting tool. To get information about various options,
you can run the this command.

    ``paver -h``

Python
======

We use `nose`_ through the `django-nose plugin`_ to run the test suite.

You can run all of the Python tests by running this command.

    ``paver test_python``

This command also runs collectstatic, which prepares the static files
used by the site (for example, compiling CoffeeScript to JavaScript).

You can re-run all failed python tests by running this command (see note at end of section).

    ``paver test_python --failed``

To test LMS python tests use this command.

    ``paver test_system -s lms``

To test Studio python tests use this command.

    ``paver test_system -s cms``

To run these tests without collectstatic, which is faster, append the following argument.

    ``paver test_system -s lms --fasttest``

For even more speed, use the ``--disable-migrations`` option to run tests without applying
migrations and instead create tables directly from apps' models.

    ``paver test_system -s lms --disable-migrations``

To run Studio python tests without collectstatic use this command.

    ``paver test_system -s cms --fasttest``

To run a single Django test class use this command.

    ``paver test_system -t lms/djangoapps/courseware/tests/tests.py:ActivateLoginTest``

When developing tests, it is often helpful to be able to really just run one single test
without the overhead of pip installs, UX builds, etc. In this case, it is helpful to look
at the output of paver, and run just the specific command (optionally, stripping away
coverage metrics). At the time of this writing, the command is the following.

    ``python ./manage.py lms test --verbosity=1 lms/djangoapps/courseware/tests/test_courses.py  --traceback --settings=test``

To run a single test format the command like this.

    ``paver test_system -t lms/djangoapps/courseware/tests/tests.py:ActivateLoginTest.test_activate_login``

To re-run all failing Django tests from LMS or Studio, use the ``--failed``, ``-f`` flag
(see note at end of section).

    ``paver test_system -s lms --failed``
    ``paver test_system -s cms --failed``

There is also a ``--fail_fast``, ``-x`` option that will stop nosetests after the first failure.

common/lib tests are tested with the ``test_lib`` task, which also accepts the
``--failed`` and ``--fail_fast`` options.

    ``paver test_lib -l common/lib/calc``
    ``paver test_lib -l common/lib/xmodule --failed``

For example, this command runs a single nose test file.

    ``nosetests common/lib/xmodule/xmodule/tests/test_stringify.py``

This command runs a single nose test within a specified file.

    ``nosetests common/lib/xmodule/xmodule/tests/test_stringify.py:test_stringify``

This is an example of how to run a single test and get ``stdout``, with proper env config.

    ``python manage.py cms --settings test test contentstore.tests.test_import_nostatic -s``

These are examples of how to run a single test and get `stdout` and get coverage.

    ``python -m coverage run which ./manage.py cms --settings test test --traceback --logging-clear-handlers --liveserver=localhost:8000-9000 contentstore.tests.test_import_nostatic -s # cms example``
    ``python -m coverage run which ./manage.py lms --settings test test --traceback --logging-clear-handlers --liveserver=localhost:8000-9000  courseware.tests.test_module_render -s # lms example``

Use this command to generate coverage report.

    ``coverage report

Use this command to generate an HTML report.

    ``coverage html``

The report is then saved in ``reports/common/lib/xmodule/cover/index.html``

To run tests for stub servers, for example for `YouTube stub server`_, you can run one of
these commands.

    ``paver test_system -s cms -t common/djangoapps/terrain/stubs/tests/test_youtube_stub.py``
    ``python -m coverage run `which ./manage.py` cms --settings test test --traceback common/djangoapps/terrain/stubs/tests/test_youtube_stub.py``

Very handy: if you pass the ``--pdb`` flag to a paver test function, or uncomment the
``pdb=1`` line in ``setup.cfg``, the test runner will drop you into pdb on error. This
lets you go up and down the stack and see what the values of the variables are. Check
out the `pdb documentation`_.

Use this command to put a temporary debugging breakpoint in a test. If you check this in,
your tests will hang on Jenkins.

    ``from nose.tools import set_trace; set_trace()``

Note: More on the ``--failed`` functionality

In order to use this, you must run the tests first. If you haven't already run the tests,
or if no tests failed in the previous run, then using the --failed switch will result in
all of the tests being run. See more about this in the nose documentation.

Note that ``paver test_python`` calls nosetests separately for Studio and LMS. This means that if
tests failed only in LMS on the previous run, then calling ``paver test_python --failed`` will
run all of the tests for Studio in addition to the previously failing LMS tests. If you want
it to run only the failing tests for LMS or Studio, use the ``paver test_system -s lms --failed``
or ``paver test_system -s cms --failed`` commands.

.. _nose: https://nose.readthedocs.org/en/latest/
.. _django-nose plugin: https://pypi.python.org/pypi/django-nose
.. _YouTube stub server: https://github.com/edx/edx-platform/blob/master/common/djangoapps/terrain/stubs/tests/test_youtube_stub.py
.. _pdb documentation: http://docs.python.org/library/pdb.html


JavaScript
==========

We use Jasmine to run JavaScript unit tests. Run JavaScript unit tests with the
following commands.

    ``paver test_js``

To run a specific set of JavaScript tests and print the results to the console,
run these commands.

    ``paver test_js_run -s lms``
    ``paver test_js_run -s lms-coffee``
    ``paver test_js_run -s cms``
    ``paver test_js_run -s cms-squire``
    ``paver test_js_run -s xmodule``
    ``paver test_js_run -s common``
    ``paver test_js_run -s common-requirejs``

To run JavaScript tests in a browser, run these commands.

    ``paver test_js_dev -s lms``
    ``paver test_js_dev -s lms-coffee``
    ``paver test_js_dev -s cms``
    ``paver test_js_dev -s cms-squire``
    ``paver test_js_dev -s xmodule``
    ``paver test_js_dev -s common``
    ``paver test_js_dev -s common-requirejs``

To debug these tests on devstack in a local browser, perform the following steps.

* run the appropriate ``test_js_dev`` command from above which will open a browser using XQuartz
* open the same URL in your browser but change the IP address to 192.168.33.10, e.g.
http://192.168.33.10:TEST_PORT/suite/cms
* this will run all the tests and show you the results including details of any failures
* you can click on an individually failing test and/or suite to re-run it by itself
* you can now use the browser's developer tools to debug as you would any other JavaScript code

**Note:** the port is also output to the console that you ran the tests from if
you find that easier.

These paver commands call through to a custom test runner. For more info, see `js-test-tool`_.

.. _js-test-tool: https://github.com/edx/js-test-tool


Bok Choy
=======

We use `Bok Choy`_ for acceptance testing. Bok Choy is a UI-level acceptance test
framework for writing robust `Selenium`_ tests in `Python`_. Bok Choy makes your acceptance
tests reliable and maintainable by utilizing the Page Object and Promise design patterns.

There are prerequisites which are all automatically installed and available in Devstack,
the supported development environment for the edX Platform.

* Chromedriver and Chrome (see Running Lettuce Acceptance Tests below for the latest tested versions)
* Mongo
* Memcache
* mySQL

To run all the Bok Choy acceptance tests run this command.

    ``paver test_bokchoy``

Once the database has been set up and the static files collected, you can use the 'fast'
option to skip those tasks. This option can also be used with any of the test specs below.

    ``paver test_bokchoy --fasttest``

For example to run a single test, specify the name of the test file.

    ``paver test_bokchoy -t lms/test_lms.py``

Notice the test file location is relative to common/test/acceptance/tests.
This is another example.

    ``paver test_bokchoy -t studio/test_studio_bad_data.py``

To run a single test faster by not repeating setup tasks use the ``--fasttest`` option.

    ``paver test_bokchoy -t studio/test_studio_bad_data.py --fasttest``

To test only a certain feature, specify the file and the testcase class.

    ``paver test_bokchoy -t studio/test_studio_bad_data.py:BadComponentTest``

To execute only a certain test case, specify the file name, class, and test case method.

    ``paver test_bokchoy -t lms/test_lms.py:RegistrationTest.test_register``

During acceptance test execution, log files and also screenshots of failed tests
are captured in ``test_root/log``.

Use this command to put a temporary debugging breakpoint in a test. If you check this in,
your tests will hang on Jenkins.

    ``from nose.tools import set_trace; set_trace()``

By default, all bokchoy tests are run with the 'split' ModuleStore. To override the modulestore that is used, use the default_store option. The currently supported stores are: 'split' (xmodule.modulestore.split_mongo.split_draft.DraftVersioningModuleStore) and 'draft' (xmodule.modulestore.mongo.DraftMongoModuleStore). This is an example for the 'draft' store.

    ``paver test_bokchoy --default_store='draft'``

.. _Bok Choy: http://bok-choy.readthedocs.org/en/latest/tutorial.html
.. _Selenium: http://docs.seleniumhq.org/
.. _Python: https://www.python.org/


Accessibility
=============

We use Bok Choy for `automated accessibility testing`_. Bok Choy, a UI-level acceptance test
framework for writing robust `Selenium`_ tests in `Python`_, includes the ability to perform
accessibility audits on web pages using `Google Accessibility Developer Tools`_ or
`Deque's aXe Core`_. For more details about how to write accessibility tests, please read the
`Bok Choy documentation`_ and the `Automated Accessibility Tests Open edX Confluence page`_.

There are prerequisites whcih are are all automatically installed and available in devstack
(since the Cypress release), the supported development environment for the edX Platform.

* Mongo
* Memcache
* mySQL

To run all the bok choy accessibility tests use this command.

    ``paver test_a11y``

To run specific tests, use the ``-t`` flag to specify a nose-style test spec relative to the
``common/test/acceptance/tests`` directory. This is an example for it.

    ``paver test_a11y -t test_lms_dashboard.py:LmsDashboardA11yTest.test_dashboard_course_listings_a11y``

To generate the coverage report for the views run during accessibility tests:

    ``paver a11y_coverage``

Note that this coverage report is just a guideline to find areas that are missing tests.
If the view isn't 'covered', there definitely isn't a test for it. If it is 'covered',
we are loading that page during the tests but not necessarily calling
``page.a11y_audit.check_for_accessibility_errors`` on it.

.. _automated accessibility testing: http://bok-choy.readthedocs.org/en/latest/accessibility.html
.. _Selenium: http://docs.seleniumhq.org/
.. _Python: https://www.python.org/
.. _Google Accessibility Developer Tools: https://github.com/GoogleChrome/accessibility-developer-tools/
.. _Deque's aXe Core: https://github.com/dequelabs/axe-core/
.. _Bok Choy documentation: http://bok-choy.readthedocs.org/en/latest/accessibility.html
.. _Automated Accessibility Tests Open edX Confluence page: https://openedx.atlassian.net/wiki/display/TE/Automated+Accessibility+Tests


Lettuce
=======

We use `Lettuce`_ for acceptance testing. Most of our tests use `Splinter`_ to simulate UI
browser interactions. Splinter, in turn, uses `Selenium`_ to control the Chrome browser.

You must have `ChromeDriver`_ installed to run the tests in Chrome. The tests are confirmed
to run with Chrome (not Chromium) version 34.0.1847.116 with ChromeDriver version 2.6.232917.

To run all the acceptance tests, run this command.

    ``paver test_acceptance``

To run only for LMS or Studio, run one of these commands.

    ``paver test_acceptance -s lms``
    ``paver test_acceptance -s cms``

For example, this command tests only a specific feature.

    ``paver test_acceptance -s lms --extra_args="lms/djangoapps/courseware/features/problems.feature"``

A command like this tests only a specific scenario.

    ``paver test_acceptance -s lms --extra_args="lms/djangoapps/courseware/features/problems.feature -s 3"``

To start the debugger on failure, pass the --pdb option to the paver command like this.

    ``paver test_acceptance -s lms --pdb --extra_args="lms/djangoapps/courseware/features/problems.feature"``

To run tests faster by not collecting static files, you can use
``paver test_acceptance -s lms --fasttest`` and ``paver test_acceptance -s cms --fasttest``.

By default, all acceptance tests are run with the 'draft' ModuleStore. To override the
modulestore that is used, use the default_store option. Currently, the possible stores for
acceptance tests are: 'split'
(xmodule.modulestore.split_mongo.split_draft.DraftVersioningModuleStore) and 'draft'
(xmodule.modulestore.mongo.DraftMongoModuleStore).

For example: ``paver test_acceptance --default_store='draft'`` Note, however, all acceptance
tests currently do not pass with 'split'.

Acceptance tests will run on a randomized port and can be run in the background of
paver cms and lms or unit tests. To specify the port, change the ``LETTUCE_SERVER_PORT`` constant
in ```cms/envs/acceptance.py`` and ``lms/envs/acceptance.py`` as well as the port listed in
``cms/djangoapps/contentstore/feature/upload.py``

During acceptance test execution, Django log files are written to
``test_root/log/lms_acceptance.log`` and ``test_root/log/cms_acceptance.log``.

**Note:** The acceptance tests can not currently run in parallel.

Using Queue Servers
===================

When testing problems that use a queue server on AWS (e.g. sandbox-xqueue.edx.org), you'll need to run your server on your public IP, like so.

./manage.py lms runserver 0.0.0.0:8000

When you connect to the LMS, you need to use the public ip. Use ifconfig to figure out the number, and connect e.g. to http://18.3.4.5:8000/

Acceptance Testing Techniques
=============================

* Element existence on the page: Do not use splinter's built-in browser methods directly f
or determining if elements exist. Use the world.is_css_present and world.is_css_not_present
wrapper functions instead. Otherwise errors can arise if checks for the css are performed
before the page finishes loading. Also these wrapper functions are optimized for the amount
of wait time spent in both cases of positive and negative expectation.
* Dealing with alerts: Chrome can hang on JavaScript alerts. If a
JavaScript alert/prompt/confirmation is expected, use the step 'I will confirm all alerts',
'I will cancel all alerts' or 'I will answer all prompts with "(.*)"' before the step that
causes the alert in order to properly deal with it.
* Dealing with stale element reference exceptions: These exceptions happen if any part of
the page is refreshed in between finding an element and accessing the element. When possible,
use any of the css functions in ``common/djangoapps/terrain/ui_helpers.py`` as they will retry
the action in case of this exception. If the functionality is not there, wrap the function
with world.retry_on_exception. This function takes in a function and will retry and return
the result of the function if there was an exception.
* Scenario Level Constants: If you want an object to be available for the entire scenario,
it can be stored in world.scenario_dict. This object is a dictionary that gets refreshed at
the beginning on the scenario. Currently, the current logged in user and the current created
course are stored under 'COURSE' and 'USER'. This will help prevent strings from being hard
coded so the acceptance tests can become more flexible.
* Internal edX Jenkins considerations: Acceptance tests are run in Jenkins as part of the
edX development workflow. They are broken into shards and split across workers. Therefore
if you add a new .feature file, you need to define what shard they should be run in or else
they will not get executed. See someone from TestEng to help you determine where they should go.

Also, the test results are rolled up in Jenkins for ease of understanding, with the
acceptance tests under the top level of "CMS" and "LMS" when they follow this convention:
name your feature in the .feature file CMS or LMS with a single period and then no other
periods in the name. The name can contain spaces. E.g. "CMS.Sign Up"

.. _Lettuce: http://lettuce.it/
.. _Splinter: http://splinter.cobrateam.info/
.. _Selenium: http://docs.seleniumhq.org/
.. _ChromeDriver: https://code.google.com/p/selenium/wiki/ChromeDriver
.. _radon: https://radon.readthedocs.org/en/latest/
.. _plato: https://github.com/es-analysis/plato
