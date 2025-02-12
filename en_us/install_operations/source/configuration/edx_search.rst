.. _Enable edX Search:

#########################
Enabling Open edX Search
#########################

You can add a search feature to your Open edX site so that prospective learners
can find courses more easily. When a learner searches for a key word or words,
the search feature returns a list of the courses that are currently open for
enrollment and that match the entered key words.

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

When you install the Open edX devstack, edX search is enabled by
default. You must enable this feature to use it with Open edX fullstack.

.. Note::
  Before proceeding, review :ref:`Guidelines for Updating the Open edX
  Platform`.

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
ElasticSearch version that is already part of Open edX Platform. The current
version is v1.5.2. The ElasticSearch Python client is the latest 1.x version.

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

EdX Search is included in Open edX Platform GitHub requirements and is
installed automatically when you install the Open edX Platform.


*****************
Enable Indexing
*****************

You enable course indexing by setting the  ``ENABLE_COURSEWARE_INDEX`` flag.

You enable library indexing by setting the ``ENABLE_LIBRARY_INDEX`` flag.

Indexing is done from Studio as a Celery task. Every publish event triggers the
reindex procedure.

You can also reindex the course manually through the **Reindex** button in the
**Course Overview** page.

.. note:: The search feature only returns results for courses that are
 currently open for enrollment. Course teams can set the enrollment start and
 end dates for their courses in Studio. For more information, see
 :ref:`Guidelines for Start and End Dates` in the *Building
 and Running an Open edX Course* guide.

==============================
Which Data Gets Indexed
==============================

Which data gets indexed is determined by the module ``index_dictionary()``
function implementation. Modules supporting this method are ``Sequence``,
``Vertical``, ``Video``, and ``HTML Block``. You can add support to any module
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

* ``ENABLE_COURSEWARE_INDEX``: Enables and disables courseware content and
  course info indexing.

* ``ENABLE_LIBRARY_INDEX``: Enables and disables library content indexing.

* ``SEARCH_ENGINE``: Sets the search engine to use. There are two predefined
  values.

  * ``"search.elastic.ElasticSearchEngine"``
  * ``"search.tests.mock_search_engine.MockSearchEngine"``

* ``ELASTIC_FIELD_MAPPINGS``: Sets any additional field mappings that elastic
  search should be aware of. For example, the following code includes the
  course start date.

  .. code-block:: none

      ELASTIC_FIELD_MAPPINGS = {
        "start_date": {
          "type": "date"
        }
      }

===
LMS
===

* ``ENABLE_COURSEWARE_SEARCH``: Enables and disables Courseware Search feature
  (in course searching).

* ``ENABLE_DASHBOARD_SEARCH``: Enables and disables Dashboard Search feature
  (in enrolled courses searching).

* ``ENABLE_COURSE_DISCOVERY``: Enables and disables Course Discovery feature
  (over courses searching and facet filtering).

* ``COURSE_DISCOVERY_FILTERS``: If provided, overrides the list of facets that
  are used in the Course Discovery feature to filter the results. By default,
  all facets will be displayed. The list of available facets includes:

  * Course organization: ``"org"``
  * Course type: ``"modes"``
  * Course language: ``"language"``

* ``SEARCH_ENGINE``: Sets the search engine to use. The following values are
  predefined.

  * ``"search.elastic.ElasticSearchEngine"``
  * ``"search.tests.mock_search_engine.MockSearchEngine"``

* ``SEARCH_INITIALIZER``: Used to set custom SearchInitializer.
  SearchInitializer provides an extension to achieve masquerade and other
  presearch environmental settings.

  * default: ``SearchInitializer``
  * LMS implementation:
    ``lms.lib.courseware_search.lms_search_initializer.LmsSearchInitializer``

* ``SEARCH_RESULT_PROCESSOR``: Used to set custom SearchResultProcessor.
  SearchResultProcessor does post processing and data manipulation on a result
  set returned by SearchEngine.

  * default: ``SearchResultProcessor``
  * LMS implementation:
    ``lms.lib.courseware_search.lms_result_processor.LmsSearchResultProcessor``

* ``SEARCH_FILTER_GENERATOR``: Used to set custom SearchFilterGenerator.
  SearchFilterGenerator sets filters defined by current active user. Basic
  implementation sets only course start date filter.

  * default: ``SearchFilterGenerator``
  * LMS implementation:
    ``lms.lib.courseware_search.lms_filter_generator.LmsSearchFilterGenerator``

.. include:: ../../../links/links.rst
