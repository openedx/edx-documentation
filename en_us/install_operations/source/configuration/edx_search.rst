.. _Enable edX Search:

#########################
Enabling Open edX Search
#########################

This section describes how to enable search in your instance of Open edX.

.. contents::
 :local:
 :depth: 1

*********
Overview
*********

`EdX Search`_ is a Django application that provides access to search services
from within edX Platform applications. Searching is accomplished by creating an
index of documents, and then searching within that index for matching
information.

.. Note::
  Before proceeding, review :ref:`Guidelines for Updating the edX Platform`.

.. _EdX Search: https://github.com/edx/edx-search/

**********************************
Search Engines and edX Search
**********************************

By default, edX Search uses MockSearchEngine for testing and ElasticSearch
Engine for production. You can configure edX Search to use a different search
engine.

=================
MockSearchEngine
=================

MockSearchEngine is a simple implementation using a JSON file for index
storage. It has no specific requirements, but it does not scale well and should
only be used for testing.

====================
ElasticSearchEngine
====================

ElasticSearchEngine is a ElasticSearch back-end implementation. It uses same
ElasticSearch version that is already part of edX Platform. The current version
is v0.90.13, and Django Elasticsearch is 0.4.5.

************************
EdX Search Requirements
************************

EdX Search requires the following applications.

* Django (edX Platform version)
* pyMongo (edX Platform version)
* pytz
* Django elasticsearch (0.4.5)

*************************
Install edX Search
*************************

EdX Search is included in edX Platform Github requirements and is installed
automatically when you install edX Platform.

For existing installations, you must install edX Search manually.

To install edX Search, make sure you are logged to your server as the
``edxapp`` user and are located in ``edx-platform`` directory.

If you are not, run the following before continuing:

.. code-block:: bash

  sudo su edxapp -s /bin/bash cd ~source edxapp_env

Then install edX Search using one of the three following options.

==========================
Option 1 – Add Requirement
==========================

Add the Github link to edx-search to the ``requirements/edx/github.txt`` file.

.. code-block:: bash

  -e git+https://github.com/edx/edx-search.git@ae459ead41962c656ce794619f58cdae46eb7896#egg=edx-search

Then reinstall Github requirements.

.. code-block:: bash

  pip install -r requirements/edx/github.txt

==========================
Option 2 – Install Locally
==========================

Checkout the ``edx-search`` Github repository.

Then in the ``edx-search`` directory, run the following command.

.. code-block:: bash

  pip install -e ./

==============================
Option 3 – Install from Github
==============================

Run ``pip`` with a Github link.

.. code-block:: bash

  pip install -e git+https://github.com/edx/edx-search.
    git@ae459ead41962c656ce794619f58cdae46eb7896

*****************
Enable Indexing
*****************

You enable course indexing by setting the  ``ENABLE_COURSEWARE_INDEX`` flag.

You enable library indexing by setting the ``ENABLE_LIBRARY_INDEX`` flag.

Indexing is done from Studio as a Celery task. Every publish event triggers the
reindex procedure.

You can also reindex the course manually through the **Reindex** button in the
**Course Overview** page.

==============================
Which Data Gets Indexed
==============================

Which data gets indexed is determined by the module :func:`index_dictionary`
function implementation. Modules supporting this method are ``Sequence``,
``Vertical``, ``Video`` and ``HTML Block``. You can add support to any module
type.

Course metadata, including the name, description, and start and end dates are
also indexed.

***************
Supported Flags
***************

The following flags are supported in the CMS and LMS applications.

===
CMS
===

* ``ENABLE_COURSEWARE_INDEX``: Enables/disables courseware content and course
  info indexing.

* ``ENABLE_LIBRARY_INDEX``: Enables/disables library content indexing.

* ``SEARCH_ENGINE``: Sets used search engine. There are 2 predefined values,
  but more can be added:

  * ``"search.elastic.ElasticSearchEngine"``
  * ``"search.tests.mock_search_engine.MockSearchEngine"``

* ``ELASTIC_FIELD_MAPPINGS``: Sets any additional field mappings that elastic
  search should be aware of. For example, the following code includes the
  course start date:

  .. code-block:: bash

      ELASTIC_FIELD_MAPPINGS = {
        "start_date": {
          "type": "date"
        }
      }

===
LMS
===

* ``ENABLE_COURSEWARE_SEARCH``: Enables/disables Courseware Search feature (in
  course searching)

* ``ENABLE_DASHBOARD_SEARCH``: Enables/disables Dashboard Search feature (in
  enrolled courses searching)

* ``ENABLE_COURSE_DISCOVERY``: Enables/disables Course Discovery feature (over
  courses searching and facet filtering)
 
* ``COURSE_DISCOVERY_FILTERS``: If provided, overrides the list of facets 
  that are used in Course Discovery feature to filter the results.
  By default, all facets will be displayed. List of available facets includes:
  
  * Course organization: ``"org"``
  * Course type: ``"modes"``
  * Course language: ``"language"``

* ``SEARCH_ENGINE``: Sets used search engine. There are 2 predefined values,
  but more can be added:

  * ``"search.elastic.ElasticSearchEngine"``
  * ``"search.tests.mock_search_engine.MockSearchEngine"``

* ``SEARCH_INITIALIZER``: Used to set custom
  SearchInitializer.SearchInitializer provides an extension to achieve
  masquerade and other presearch environmental settings.

  * default: ``SearchInitializer``
  * LMS implementation:
    :class:`lms.lib.courseware_search.lms_search_initializer.LmsSearchInitializer`

* ``SEARCH_RESULT_PROCESSOR``: Used to set custom SearchResultProcessor.
  SearchResultProcessor does post processing and data manipulation on a result
  set returned by SearchEngine.

  * default: ``SearchResultProcessor``
  * LMS implementation:
    :class:`lms.lib.courseware_search.lms_result_processor.LmsSearchResultProcessor`

* ``SEARCH_FILTER_GENERATOR``: Used to set custom SearchFilterGenerator.
  SearchFilterGenerator sets filters defined by current active user. Basic
  implementation sets only course start date filter.

  * default: ``SearchFilterGenerator``
  * LMS implementation:
    :class:`"lms.lib.courseware_search.lms_filter_generator.LmsSearchFilterGenerator`

.. include:: ../../../links/links.rst