.. _Enterprise API Reference:

################################
EdX Enterprise API Reference
################################

This API reference includes detailed information about the
``/enterprise-catalogs`` and ``/course-enrollments`` endpoints of the edX
Enterprise API, including the request, response data, and examples. The
example API requests shown in this reference use the ``curl`` command-line
program to send HTTP messages to the edX API. You can use any technology to
send REST API requests. The examples use the ``curl`` program to show the
syntax and data for a request in a way that is easy to read.

*********
Endpoints
*********

The following endpoints are available in the Enterprise API.

* **/enterprise-catalogs** - You can make GET calls to the
  ``/enterprise-catalogs`` endpoint to get a list of all the course catalogs
  that are available to your organization.

* **/enterprise-catalogs/{catalog_id}** - You can make GET calls to the
  ``/enterprise-catalogs/{catalog_id}`` endpoint to get a
  list of all the active content items (courses, course runs, and programs) in
  a specified course catalog, along with details about each course. Active
  courses are courses that are currently open for enrollment or that will open
  for enrollment in the future. For details, see
  :ref:`enterprise_catalogs_catalogID Endpoint`.

* **/enterprise_catalogs/{catalogID}/course_runs/{course_run_ID}** -
  You can make GET calls to the
  ``/enterprise-catalogs/{catalog_id}/course_runs/{course_run_ID}`` endpoint
  to get information about a single course run. For details, see
  :ref:`enterprise_catalogs_courserun Endpoint`.

* **/enterprise-catalogs/{catalogID}/programs/{program_ID}**
  - You can make GET calls to the
  ``/enterprise-catalogs/{catalog_id}/programs/{program_ID}`` endpoint
  to get information about a single program. For details, see
  :ref:`enterprise_catalogs_programs Endpoint`.

* **/course-enrollments** - You can make POST calls to the
  ``/course-enrollments`` endpoint to enroll a single learner in a single
  course run. For details, see :ref:`course_enrollments Endpoint`.

.. _enterprise_catalogs_catalogID Endpoint:

*****************************************
enterprise_catalogs/{catalog_id} Endpoint
*****************************************

GET calls to the ``enterprise_catalogs/{catalog_id}`` endpoint return a list
of all of the active content items (courses, course runs, and programs) in a
specified course catalog.

===================
Method and Endpoint
===================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - Endpoint
   * - GET
     - ``/enterprise/v1/enterprise-catalogs/{catalog_id}``

=====================
Example Request
=====================
::

   curl -X GET \
   https://api.edx.org/enterprise/v1/enterprise-catalogs/1/4g1BB0us321/ \
   -H "Authorization: JWT {access token}"

=====================
Response Values
=====================

The ``GET /enterprise/v1/enterprise-catalogs/{catalog_id}`` request
returns the following response values.

.. note::
  Responses to GET requests for the edX Enterprise API frequently contain
  the ``results`` response value. The ``results`` response value is a variable
  that represents the intended JSON object from the GET request. For the
  ``/enterprise/api/v1/enterprise_catalogs/{catalog_id}`` endpoint, the
  ``results`` object holds an array of objects that list information about
  each individual content item (course run, course, or program) in the catalog.

.. list-table::
   :widths: 25 20 80
   :header-rows: 1

   * - Field
     - Data Type
     - Description
   * - ``count``
     - integer
     - The number of active content items (course run, course, or program) in
       the catalog.
   * - ``next``
     - string
     - The URL for the next page of results.
   * - ``previous``
     - string
     - The URL for the previous page of results.
   * - ``results``
     - array
     - A list of content items in the catalog.

Each top-level JSON object in the ``results`` array represents a content item
in the catalog, which may be a course, a course run, or a program. The
``results`` array returns different fields, depending on whether
the content item is a :ref:`course<course Fields>`, a
:ref:`course run<course_run Fields>`, or a :ref:`program<program Fields>`.

.. _course Fields:

Fields in a course Content Item
***********************************

.. list-table::
   :widths: 25 20 80
   :header-rows: 1

   * - Field
     - Data Type
     - Description
   * - ``aggregation_key``
     - string
     - Example: ``course:edX+DemoX``.
   * - ``content_type``
     - enum string
     - Type of learning item. One of ``course``, ``courserun``, or ``program``.
   * - ``full_description``
     - string
     - The HTML full description of the course.
   * - ``key``
     - string
     - A unique identifier for the course. Example: ``edX+DemoX``.
   * - ``short_description``
     - string
     - The HTML short description of the course.
   * - ``title``
     - string
     - The title of the course.

.. _course_run Fields:

Fields in a course_run Content Item
***********************************

.. list-table::
   :widths: 25 20 80
   :header-rows: 1

   * - Field
     - Data Type
     - Description
   * - ``aggregation_key``
     - string
     - Example: ``courserun:edX+DemoX``.
   * - ``authoring_organization_uuids``
     - array
     - The unique user IDs for the organizations that produced the content
       item.
   * - ``availability``
     - enum string
     - One of ``Current``, ``Upcoming``.
   * - ``content_type``
     - enum string
     - Type of learning item. One of ``course``, ``courserun``, or ``program``.
   * - ``end``
     - datetime
     - The end date of the course run.
   * - ``enrollment_end``
     - datetime
     - The last time at which learners can enroll.
   * - ``enrollment_start``
     - datetime
     - The first time at which learners can enroll.
   * - ``enrollment_url``
     - sring
     - The URL for the enrollment page.
   * - ``full_description``
     - string
     - The long description of the course and its content.
   * - ``has_enrollable_seats``
     - boolean
     - Whether learners can enroll in the course.
   * - ``image_url``
     - string
     - The URL for the About page image for the course.
   * - ``key``
     - string
     - An identifier for the course. For example, ``RITx+PM9003x``.
   * - ``language``
     - string
     - The language used by the content item.
   * - ``level_type``
     - enum string
     - The course's level of difficulty. Can be one of ``high_school``,
       ``introductory``, ``intermediate``, or ``advanced``.
   * - ``logo_image_urls``
     - array
     - The URLs of the enterprise's logos.
   * - ``marketing_url``
     - string
     - The URL for the course About page.
   * - ``max_effort``
     - integer
     - The maximum number of estimated hours of effort per week.
   * - ``min_effort``
     - integer
     - The minimum number of estimated hours of effort per week.
   * - ``mobile_available``
     - boolean
     - Whether the content item is available for mobile devices.
   * - ``number``
     - string
     - The content item's course number identifier.
   * - ``org``
     - string
     - The university or other entity offering the course.
   * - ``pacing_type``
     - enum string
     - The pacing of the course. May be ``self-paced`` or ``instructor-paced``.
   * - ``partner``
     - string
     - The university or other entity offering the course.
   * - ``program_types``
     - array
     - The type of program. One of Professional Certificate, XSeries,
       MicroMasters, or Professional Program.
   * - ``published``
     - boolean
     - Whether the content item has been published.
   * - ``seat_types``
     - enum string
     - The enrollment types that are available. One of ``audit``,
       ``verified``, ``professional``.
   * - ``short_description``
     - string
     - The short description of the content item and its content.
   * - ``staff_uuids``
     - array
     - The unique identifiers of the staff for the content item.
   * - ``start``
     - datetime
     - The start time for the content item.
   * - ``subject_uuids``
     - array
     - The unique identifiers of the subject categories of the content item.
   * - ``title``
     - string
     - The title of the content item. For example, "Introduction to Plasma
       Physics".
   * - ``transcript_languages``
     - array
     - The languages for which video transcripts are available.
   * - ``type``
     - enum string
     - One of ``verified``, ``professional``
   * - ``weeks_to_complete``
     - int
     - The number of weeks required to complete the content item.

.. _program Fields:

Fields in a program Content Item
***********************************

.. list-table::
   :widths: 25 20 80
   :header-rows: 1

   * - Field
     - Data Type
     - Description
   * - ``aggregation_key``
     - string
     - Example: ``program:7a8b9c6ead``.
   * - ``authoring_organization_uuids``
     - array
     - The unique user IDs for the organizations that produced the program.
   * - ``authoring_organizations``
     - array
     - Information about the organizations that produced the program.
   * - ``card_image_url``
     - string
     - The URL of an image that represents the program.
   * - ``content_type``
     - enum string
     - Type of learning item. One of ``course``, ``courserun``, or ``program``.
   * - ``enrollment_url``
     - sring
     - The URL for the enrollment page.
   * - ``language``
     - string
     - The language used by the program.
   * - ``marketing_url``
     - string
     - The URL for the program About page.
   * - ``max_hours_effort_per_week``
     - integer
     - The maximum number of estimated hours of effort per week.
   * - ``min_hours_effort_per_week``
     - integer
     - The minimum number of estimated hours of effort per week.
   * - ``partner``
     - string
     - The organization offering the program.
   * - ``published``
     - boolean
     - Whether the program has been published.
   * - ``published``
     - boolean
     - Whether the content item has been published.
   * - ``staff_uuids``
     - array
     - The unique identifiers of the staff for the program.
   * - ``subject_uuids``
     - array
     - The unique identifiers of the subject categories of the program.
   * - ``subtitle``
     - string
     - A subtitle for the program.
   * - ``title``
     - string
     - The title of the program. For example, "MicroMasters: Plasma
       Physics".
   * - ``type``
     - enum string
     - The program type. One of ``Professional Certificate``, ``XSeries``,
       ``MicroMasters``, or ``Professional Program``.
   * - ``uuid``
     - string
     - The unique identifier for the program.
   * - ``weeks_to_complete_max``
     - int
     - The maximum number of estimated weeks required to complete the program.
   * - ``weeks_to_complete_min``
     - int
     - The minimum number of estimated weeks required to complete the
       program.



=======================================================
Example Response Showing Information about a Course Run
=======================================================

The following example response shows a single course run. A catalog may
contain many courses, course runs, or programs.

::

  {
    "uuid": "0e871df0-6e43-4cfc-92cc-357ebf1fda75",
    "title": "All Content",
    "enterprise_customer": "58152f7f-6d0e-41cf-862d-0a27c6fad72c",
    "count": 13,
    "previous": null,
    "next": null,
    "results": [
      {
        "content_type": "courserun",
        "number": "DemoX",
        "weeks_to_complete": 3,
        "partner": "edx",
        "enrollment_url": "https://courses.edx.org/
        enterprise/58152f7f-6d0e-41cf-862d-0a27c6fad72c/course/
        course-v1:edX+DemoX+Demo_Course/enroll/?catalog=0e871df0-6e43-4cfc-92cc-3
        57ebf1fda75&utm_medium=enterprise&utm_source=degreed-company",
        "availability": "Upcoming",
        "transcript_languages": [

        ],
        "logo_image_urls": [
          "https://www.edx.org/sites/default/files/school/image/logo/
          gtx-logo-200x101.png"
        ],
        "end": null,
        "title": "edX Demonstration Course",
        "enrollment_start": "2017-10-01T00:00:00",
        "start": "2017-11-01T05:00:00",
        "min_effort": 5,
        "short_description": "A hands-on introduction to basic programming
        principles and practice relevant to modern data analysis, data mining,
        and machine learning.",
        "image_url": "https://courses.edx.org/
        asset-v1:edX+DemoX+Demo_Course+type@asset+block@images_course_image.jpg",
        "level_type": "Beginner",
        "type": "verified",
        "marketing_url": "course/edxdemoslug?utm_medium=enterprise
        &utm_source=degreed-company",
        "seat_types": [
          "audit",
          "verified"
        ],
        "max_effort": 6,
        "full_description": "<p>The modern data analysis pipeline involves
        collection, preprocessing, storage, analysis, and interactive
        visualization of data.</p>\\n<p>The goal of this course, part of the
        Analytics: Essential Tools and Methods MicroMasters program, is for you
        to learn how to build these components and connect them using modern
        tools and techniques.</p>",
        "key": "course-v1:edX+DemoX+Demo_Course",
        "enrollment_end": null,
        "org": "edX",
        "authoring_organization_uuids": [
          "12de950c-6fae-49f7-aaa9-778c2fbdae56"
        ],
        "subject_uuids": [

        ],
        "has_enrollable_seats": true,
        "language": "English",
        "staff_uuids": [
          "a1b2c3d4-3185-4233-a323-2fbeb401cb82",
          "a1b2c3d4-4ebe-4e5c-b0a2-2ff630c0dae0",
          "b2c3d4e5-bf58-47cf-ae9a-994c0eb22062",
          "1111a42a-b667-4664-bdaa-4754e1cfd480"
        ],
        "mobile_available": true,
        "pacing_type": "self_paced",
        "aggregation_key": "courserun:edX+DemoX",
        "published": true,
        "program_types": [
          "Professional Certificate"
        ]
      }

.. _enterprise_catalogs_courserun Endpoint:

*********************************************************************
enterprise-catalogs/{catalog_id}/course-runs/{course_run_ID} Endpoint
*********************************************************************

GET calls to the ``enterprise-catalogs/{catalog_id}/course-runs/{course_run_ID}``
endpoint return information about a single course run in a specified course
catalog. In the GET call, you pass a catalog ID, which you can get using the
``enterprise-catalogs`` endpoint, and a course run ID, which you can get from
the ``key`` value returned by the ``enterprise-catalogs/{catalog_id}``
endpoint. The information returned is described in :ref:`course_run Fields`.

===================
Method and Endpoint
===================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - Endpoint
   * - GET
     - ``/enterprise/v1/enterprise-catalogs/{catalog_id}/course-runs/{course_run_ID}``

=====================
Example Request
=====================
::

   curl -X GET \
   https://api.edx.org/enterprise/v1/enterprise-catalogs/1/4g1BB0us321/course-runs/course-v1:MyUni+Sport101x \
   -H "Authorization: JWT {access token}"

=====================
Response Values
=====================

The ``GET /enterprise/v1/enterprise-catalogs/{catalog_id}/course-runs/{course_run_ID}``
request returns the response values described in :ref:`course_run Fields`.

.. _enterprise_catalogs_programs Endpoint:

*********************************************************************
enterprise-catalogs/{catalog_id}/programs/{program_ID} Endpoint
*********************************************************************

GET calls to the ``enterprise-catalogs/{catalog_id}/programs/{program_ID}``
endpoint return information about a single program in a specified course
catalog. In the GET call, you pass a catalog ID, which you can get using the
``enterprise-catalogs`` endpoint, and a program ID, which you can get from
the ``uuid`` value returned by the ``enterprise-catalogs/{catalog_id}``
endpoint. The information returned is described in :ref:`program Fields`.

===================
Method and Endpoint
===================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - Endpoint
   * - GET
     - ``/enterprise/v1/enterprise-catalogs/{catalog_id}/programs/{program_ID}``

=====================
Example Request
=====================
::

   curl -X GET /oauth2/v1/access_token/ \
   https://api.edx.org/enterprise/v1/enterprise-catalogs/4g1BB0us321/programs/21g1bB0us545 \
   -H "Authorization: JWT {access token}"


=====================
Response Values
=====================

The ``GET /enterprise/v1/enterprise-catalogs/{catalog_id}/programs/{program_id}``
request returns the response values described in :ref:`program Fields`.

.. _course_enrollments Endpoint:

*******************************
course-enrollments Endpoint
*******************************

POST calls to the ``course-enrollments`` endpoint enroll learners in specified
course runs. Calls to this endpoint require the enterprise's UUID, which is
assigned to the enterprise by your edX account representatlve.

===================
Method and Endpoint
===================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - Endpoint
   * - POST
     - ``/enterprise/v1/enterprise-customer/{enterprise_uuid}/course-enrollments``

=====================
Example Request
=====================
::

   curl -X POST
     https://api.edx.org/enterprise/v1/enterprise-customer/\
     e1b2c4/course-enrollments \
     -H "Authorization: JWT {access token}"
     -H "Content-Type: application/json" \
     -d "[{
           "course_run_id":"course-v1:MyUniX+Writing101x+2T2018_2",
           "course_mode":"audit",
           "user_email":efraim.symbolist@example.com",
           "email_students":"true"
    }]"

=================
POST Data Values
=================

POST calls to the ``course-enrollments`` endpoint include the following fields
in JSON format. For each learner, a call must include the ``course_run_id``
field and the ``course_mode``, as well as one or more of the ``user_email``,
``lms_user_id``, or ``tpa_user_id`` fields.

.. list-table::
   :widths: 25 20 80
   :header-rows: 1

   * - Field
     - Data Type
     - Description
   * - ``course_run_id``
     - string
     - Required. The ID of a course run in your edX course catalog. Example:
       ``course-v1:UMy+Intro_to_Education``.
   * - ``course_mode``
     - enum string
     - Required. The enrollment mode in which the learner will be enrolled in
       the course run. One of ``verified``, ``professional``, or ``audit``.
   * - ``user_email``
     - string
     - The learner's email address.
   * - ``lms_user_id``
     - string
     - The learner's ID on edx.org.
   * - ``tps_user_id``
     - string
     - The learner's ID on the enterprise's Identity Provider (IdP) system.
   * - ``email_students``
     - boolean
     - Whether the learner has consented to be contacted by email. Default is
       ``false``.

POST Payload Example
*********************

Here is an example of the payload of a ``course-enrollments`` call. In this
example, we enroll two learners in two different course runs.

::

  [
    {
      "course_run_id":"course-v1:edX+DemoX+Demo_Course",
      "course_mode":"verified",
      "user_email":"ephraim_symbolist@example.com",
      "email_students": true
    },
    {
      "course_run_id":"course-v1:UMy+Intro_to_Education`",
      "course_mode":"audit",
      "tpa_user_id":"abcdefg"
    }
  ]

=====================
Response Values
=====================

The ``POST /enterprise/api/v1/enterprise-customer/{enterprise_uuid}/course_enrollments``
request returns a ``details`` response with a success or error message.

