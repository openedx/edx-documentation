.. _edx_user_interfaces:

##############################
Developing User Interfaces
##############################

This section provides information about developing user interfaces (UI) for edX
applications.

All new edX pages should be composed of elements and styling shown in the edX
Pattern Library. You can use JavaScript from the edX UI Toolkit JavaScript
library to implement pages in a way that is consistent with edX UI
architecture.

.. Add an overview of the current architecture.
.. * Django views generated using Mako templates
.. * Dynamic pages created using RequireJS, Backbone and Underscore,
..   making AJAX calls to Django REST APIs
.. * Sass is used to create style sheets and libsass is used to convert
..   them to CSS files
.. * Production pages are bundled and minified using RequireJS
..   Optimizer and served through the Django Pipeline

.. Add a performance section that explains best practices for ensuring
.. performant pages.

.. contents::
 :local:
 :depth: 2


.. 20160518 - any important information about UI development should be moved
.. from the wiki to the developer's guide here.

The Open edX wiki includes additional details about developing edX user
interfaces. For more information, see `edX Front End Development`_.

.. _pattern_library:

*****************************
Using the edX Pattern Library
*****************************

The edX Pattern Library is a collection of web application
components and visual styles that you can use to develop UIs that
are consistent with the edX platform.

The edX Pattern Library is available at `ux.edx.org`_.

The edx-platform GitHub repository includes an `example web page`_ that
demonstrates using the Pattern Library. You can use the example page as a
template for creating your own new LMS or Studio pages.

To create a new page using the Pattern Library, you use the same ``main.html``
template as for non-Pattern Library pages, and pass the following context
parameters.

    .. code-block:: none

        {
            ...
            'disable_courseware_js': True,
            'uses_pattern_library': True,
        }

When you create a page using the Pattern Library, create two new root
syntactically awesome style sheets (Sass) files for your page, one for left-to-
right (LTR) and one for right-to-left (RTL) localizations. For more information
about Sass, see the `Sass site`_.

The RTL version of the style sheet must have the same filename as the
LTR version but ending with ``-rtl``.

Register the two new style sheets in the ``PIPELINE_CSS`` configuration. You
can see the full list for the LMS in `lms/envs/common.py`_.

After you register the LTR and RTL style sheets, you refer to the configuration
name in your Mako template. Mako will then dynamically pick either the LTR or
the RTL version based upon the current user's localization preference.

The following example shows how a pair of style sheets are registered in the
``PIPELINE_CSS`` configuration.

.. code-block:: python

    'style-learner-dashboard': {
        'source_filenames': [
            'css/lms-learner-dashboard.css',
        ],
        'output_filename': 'css/lms-learner-dashboard.css',
    },
    'style-learner-dashboard-rtl': {
        'source_filenames': [
            'css/lms-learner-dashboard-rtl.css',
        ],
        'output_filename': 'css/lms-learner-dashboard-rtl.css',
    },

After you register your Sass style sheets, you must also declare the name of
your Sass files at the top of your main Mako file. The following example
declares files that are configured with the names ``style- learner-dashboard``
and ``style-learner-dashboard-rtl``.

.. code-block:: mako

    <%! main_css = "style-learner-dashboard" %>

You can refer to the following examples.

* `Pattern Library test page`_

* PR to convert the programs list to be a Pattern Library page: `PR 12380`_


.. _ui_toolkit:

************************
Using the edX UI Toolkit
************************

The edX UI Toolkit is a JavaScript library for building edX web applications.
The UI toolkit consists of:

* Backbone views to implement patterns as defined by the edX Pattern Library.

* Utility methods to simplify the creation and testing of user interfaces.

The edX UI Toolkit is available from the `edx-ui-toolkit GitHub repository`_ .
For more information about the UI Toolkit, see `ui-toolkit.edx.org`_ .

For more information about writing JavaScript for edX UIs, see
:ref:`edx_javascript_guidelines`.

.. _adding_a_new_ui_page:

********************
Adding a UI Page
********************

This topic is a collection of things to think about when creating a new page
in Studio or the LMS.

You should also read :ref:`Contributing to Open edX` to understand
more general best practices, as well as how to submit your new code for review.

.. contents::
 :local:
 :depth: 2

======================================
Use JavaScript Instead of CoffeeScript
======================================

The edX front end code base is currently a mixture of CoffeeScript and
JavaScript. The edX development team is now standardizing the use of JavaScript
for new work. There are a number of reasons for this decision, including the
following list.

* It is hard to jump back and forth between the two syntaxes.

* It adds a compilation step which slows down iterative development.

* Most third party libraries are implemented and documented in
  JavaScript.

* Client-side debugging is done in JavaScript, which makes it hard to correlate
  to the original code.

* The diff-cover tools are not compatible with CoffeeScript so code coverage is
  not tracked.

* A lot of the traditional benefits of CoffeeScript can now be achieved using
  JavaScript libraries.

All new front end development should be done in JavaScript, while legacy
CoffeeScript code will be converted on an as-needed basis. For pragmatic
reasons, targeted changes to CoffeeScript will still be accepted.

For more information about writing JavaScript for edX UIs, see
:ref:`edx_javascript_guidelines`.

.. _use_requirejs_to_manage_file_dependencies:

=========================================
Use RequireJS to Manage File Dependencies
=========================================

All new pages should use `RequireJS`_ to manage loading
of file dependencies.

* Use the standard syntax to load JavaScript dependencies.

  .. note::

      For the LMS, you have to wrap each call to define or require in
      order for it to work with the namespaced version of RequireJS.

  .. code-block:: javascript

    ;(function (define) {
        'use strict';
        define([...], function (...) {
            ...
        });
    }).call(this, define || RequireJS.define);

* Use RequireJS Text for your templates (see
  :ref:`requirejs_optimization_javascript` for details).

* Create a factory class that is included by your Mako template using
  ``require_module``.

    * This Mako function ensures that the factory is loaded correctly for both
      the optimized and non-optimized pipeline.

    * When accessed in the optimized mode, the query parameter ``?raw`` will be
      added to the URL to ensure that the file is not post-processed.

  .. note::

     ``require_module`` is needed for the unified optimizer pipeline in Studio.

* If you need server-side data passed to your page, pass it as one or more
  parameters to your factory.

  For information about avoiding cross-site scripting, see :ref:`JavaScript
  Context in Mako`.

* For information about adding third-party JavaScript libraries, see
  :ref:`adding_javascript_libraries`.

* If the dependency is pre-loaded, then be sure to specify its path as empty in
  build.js so that the optimizer does not include it in the bundled file. This
  is especially important for files that are used by both by JavaScript
  leveraging RequireJS and "non-RequireJS JavaScript" within the same page.

  .. code-block:: javascript

    paths: {
        'gettext': 'empty:',
        'jquery': 'empty:',
        ...
    }

See an example Mako code block in :ref:`JavaScript Context in Mako`.

The following list includes more examples.

* `Studio Course Outline (Studio)`_

* `Courseware Search (LMS)`_

* `Student Notes (LMS)`_

* `Teams courseware tab (LMS)`_

.. note::

    Using RequireJS in XBlocks is not currently supported. Future development
    is planned to add this support.

.. _adding_javascript_libraries:

===========================
Adding JavaScript Libraries
===========================

Install JavaScript libraries using the ``npm`` package manager.

If the library you want to add is available from `npmjs.com`_,  update edx-
platform's package.json file to reference the library. Use the tilde ``~``
prefix for the version to allow patches to be picked up automatically.

For more information about versioning, see `semver.org`_.

Execute the following command to install your library.

.. code-block:: shell

    paver install_prereqs

Add the new library to the `list of npm-installed libraries`_.

Execute the following command to make your library available as a Django static
asset (choose LMS, Studio, or both).

.. code-block:: shell

    paver update_assets lms --settings=devstack

To add the new library to the LMS, follow these steps.

#. Add the library to the `lms/env/common.py` file at https://github.com/edx
   /edx-platform/blob/master/lms/envs/common.py#L1246

#. Add the library to `lms/static/lms/js/require-config.js`_.

Add the new library to the list of vendor libraries that are installed by
``update_assets``. Update the variable ``NPM_INSTALLED_LIBRARIES`` in
`/pavelib/assets.py`_.

.. note::

    Reference the unminified version of the library. This allows debugging
    tools to step through readable library code, and the Django static asset
    pipeline will ensure that it get optimized for production.

If you cannot use npm, check the file into the `common/static/js/vendor`_
directory.

.. _use_underscore_and_requirejs_text:

===========================================================
Use Underscore and RequireJS Text for Client-Side Templates
===========================================================

The edX development team has standardized using Underscore for all client-side
templates. There are some things to consider.

* Add your templates to a static/templates directory in your Django app.

* If you need mock HTML for Jasmine, put them in a subdirectory named ``mock``.

* Use :ref:`RequireJS Text <use_underscore_and_requirejs_text>` to load your
  templates (note that most code today statically includes the template in the
  page).

RequireJS Text is superior to the old mechanism of statically
including the templates in the Mako-generated HTML for several reasons.

* Mako templates no longer need to explicitly include every template that is
  needed in the HTML.

* The template lookup is much faster when optimized for production use because
  JavaScript code does not have to extract the templates it needs from the DOM.
  For developers, the templates are fetched asynchronously like any other
  RequireJS dependency.

* The templates get included in the minified .js file for the page so the
  content is only downloaded once and then cached in the browser. Including the
  template in the Mako template causes it to be downloaded every time.

* Unit tests do not need to load all the templates into fixtures for the views
  to work, as the view will load its template dependencies directly.

Here are a few examples.

* `Paging Header component`_

* `Teams topic card`_

.. _requirejs_optimization_javascript:

============================================================
Ensure That RequireJS Optimizer Can Optimize Your JavaScript
============================================================

We use `RequireJS Optimizer`_ to optimize the JavaScript that we use in
production. This works as part of the production pipeline to merge all of a
page's JavaScript and templates into a single minified file. This greatly
reduces the number of files that the browser needs to request, as well as the
number of bytes that need to be fetched. Furthermore, in the LMS un-optimized
RequireJS files are never cached, leading to significant performance
degradation.

The basic approach is to move all of the page view construction logic into a
single factory file. This factory is responsible for creating the models and
views required to render the page. The idea is that the optimizer can produce a
single minified file for the factory by statically determining all of its
dependencies.

* Structure your page so that it has a single root factory file (see
  :ref:`use_requirejs_to_manage_file_dependencies`).

  Be sure to use ``require_module`` to load the factory as described above.

* List your factory in the RequireJS Optimizer build file.

    * `Studio build file`_

    * `LMS build file`_

* By default, devstack runs with unoptimized files so that changes are picked
  up immediately.

  To run with optimized files, specify the ``--optimized`` parameter to Paver's
  ``devstack`` command:

  .. code-block:: bash

    paver devstack lms --optimized

* Note that Bokchoy tests run with optimized files to verify that they are
  being generated as expected.

* Be sure to test your page in a production environment, checking that all
  dependencies are included in the optimized factory file.

    * For LMS files, take care that all of the JS files have a MD5 hash code
      between their filename and the js extension. Files without MD5 hash codes
      will not be cached in production and indicate incorrect optimization.

    * Studio RequireJS files currently do not use the MD5 hashing mechanism,
      and instead store files within a unique directory that changes with each
      release. We hope to change this in the future.

=================================
Use Backbone to Build Your New UI
=================================

Code written with Backbone is more modular, more extensible, and more easily
unit tested with Jasmine.

See `How to add a new feature to LMS or Studio`_ to see how to
structure your Backbone code.

.. TODO: move the content from the wiki page into the developer's guide.

.. Link destinations

.. _example web page: https://github.com/edx/edx-platform/blob/master/lms/templates/ux/reference/pattern-library-test.html

.. _Studio build file: https://github.com/edx/edx-platform/blob/master/cms/static/build.js#L24

.. _LMS build file: https://github.com/edx/edx-platform/blob/master/lms/static/lms/js/build.js

.. _RequireJS Optimizer: http://requirejs.org/docs/optimization.html

.. _Teams topic card: https://github.com/edx/edx-
  platform/blob/master/lms/djangoapps/teams/static/teams/js/views/topics.js

.. _Paging Header component: https://github.com/edx/edx- platform/blob/master/common/static/common/js/components/views/paging_header.js

.. _common/static/js/vendor: https://github.com/edx/edx-platform/tree/master/common/static/js/vendor

.. _/pavelib/assets.py: https://github.com/edx/edx-platform/blob/master/pavelib/assets.py#L47

.. _lms/static/lms/js/require-config.js: https://github.com/edx/edx-platform/blob/master/lms/static/lms/js/require-config.js#L51>

.. _list of npm-installed libraries: https://github.com/edx/edx-platform/blob/master/pavelib/assets.py#L43

.. _How to add a new feature to LMS or Studio: https://openedx.atlassian.net/wiki/display/AC/How+to+add+a+new+feature+to+LMS+or+Studio

.. _npmjs.com: https://www.npmjs.com/

.. _edX Front End Development: https://openedx.atlassian.net/wiki/display/FEDX/edX+Front+End+Development

.. _Sass site: http://sass-lang.com/

.. _lms/envs/common.py: https://github.com/edx/edx-platform/blob/master/lms/envs/common.py#L1373

.. _Pattern Library test page: https://github.com/edx/edx-platform/blob/master/lms/templates/ux/reference/pattern-library-test.html

.. _PR 12380: https://github.com/edx/edx-platform/pull/12380

.. _RequireJS: http://requirejs.org/

.. _Studio Course Outline (Studio): https://github.com/edx/edx-platform/blob/master/cms/static/js/views/pages/course_outline.js

.. _Courseware Search (LMS): https://github.com/edx/edx-platform/blob/master/lms/static/js/search/course/views/search_results_view.js

.. _Student Notes (LMS): https://github.com/edx/edx-platform/blob/master/lms/static/js/edxnotes/views/notes_factory.js

.. _Teams courseware tab (LMS): https://github.com/edx/edx-platform/blob/master/lms/djangoapps/teams/static/teams/js/views/teams_tab.js

.. _semver.org: http://semver.org/

.. _

.. include:: ../../links/links.rst
