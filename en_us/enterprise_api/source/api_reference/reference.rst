.. _Enterprise API Reference:

################################
EdX Enterprise API Reference
################################

This API reference includes detailed information about the endpoints of the edX
Enterprise API, including the request, response data, and examples. You can use
any technology to send REST API requests as HTTP messages to the edX API. The
example API requests shown in this reference use the ``curl`` command-line program
to show the syntax and data for a request in a way that is easy to read.

*********
Endpoints
*********

The following endpoints are available in the Enterprise API.

* **/enterprise-catalogs** - You can make GET calls to the
  ``/enterprise-catalogs`` endpoint to get a list of all the course catalogs
  that are available to your organization.

* **/enterprise-catalogs/{catalog_id}** - You can make GET calls to the
  ``/enterprise-catalogs/{catalog_id}`` endpoint to get a list of all the
  active courses in a specified course catalog. Active courses are courses
  that are currently open for enrollment or that will open for enrollment in
  the future. For details, see :ref:`enterprise_catalogs_catalogID Endpoint`.

* **/enterprise-catalogs/{catalogID}/courses/{course_key}** - You can make GET
  calls to the ``/enterprise-catalogs/{catalog_id}/courses/{course_key}``
  endpoint to get information about a single course. For details, see
  :ref:`enterprise_catalogs_courses Endpoint`.

* **/enterprise-catalogs/{catalogID}/course-runs/{course_run_ID}** -
  You can make GET calls to the
  ``/enterprise-catalogs/{catalog_id}/course-runs/{course_run_ID}`` endpoint
  to get information about a single course run. For details, see
  :ref:`enterprise_catalogs_courserun Endpoint`.

* **/enterprise-catalogs/{catalogID}/programs/{program_ID}**
  - You can make GET calls to the
  ``/enterprise-catalogs/{catalog_id}/programs/{program_ID}`` endpoint
  to get information about a single program. For details, see
  :ref:`enterprise_catalogs_programs Endpoint`.

* **/learner-summary** - You can make GET calls to the
  ``/learner-summary`` endpoint to get a list of information about your
  enterprise learners and their status in the courses they are enrolled in.
  For details, see :ref:`learner_summary Endpoint`.

.. _Returning XML Data:

************************************
Returning Data in XML or JSON Format
************************************

By default, the edX Enterprise API returns data in XML format. It can also
return data in JSON format. To specify that return data should use JSON format,
include the ``Accept: application/json`` header in your API request. For
example, to request JSON-formatted information about a course run using
``curl``, send a request similar to the following command.

::

   curl -X GET \
   https://api.edx.org/enterprise/v2/enterprise-catalogs/3f56a21c-76c8-47c0-add8-a99714d40d94/courses/MyUni+Sport101x \
   -H "Authorization: JWT {access token}"
   -H "Accept: application/json"

.. _enterprise_catalogs_catalogID Endpoint:

*****************************************
enterprise-catalogs/{catalog_id} Endpoint
*****************************************

GET calls to the ``enterprise-catalogs/{catalog_id}`` endpoint return a list
of all of the active courses in a specified course catalog. You can then make a
GET call to the ``/enterprise-catalogs/{catalog_id}/courses/{course_key}``
endpoint to return details about a single course.

===================
Method and Endpoint
===================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - Endpoint
   * - GET
     - ``/enterprise/v2/enterprise-catalogs/{catalog_id}``


=====================
Example Request
=====================
::

   curl -X GET \
   https://api.edx.org/enterprise/v2/enterprise-catalogs/3f56a21c-76c8-47c0-add8-a99714d40d94/ \
   -H "Authorization: JWT {access token}"

=====================
Parameters
=====================

You can use an optional ``limit`` parameter to specify the number of
courses that ``enterprise-catalogs/{catalog_id}`` calls return
on each page of the response. If you do not supply the ``limit``
parameter, the ``enterprise-catalogs/{catalog_id}`` call returns the default
value of 20 courses per page. For example:

::

   curl -X GET https://api.edx.org/enterprise/v2/\
   enterprise-catalogs/3f56a21c-76c8-47c0-add8-a99714d40d94?limit=250 \
   -H "Authorization: JWT {access token}"

=====================
Response Values
=====================

The ``GET /enterprise/v2/enterprise-catalogs/{catalog_id}`` request
returns the following response values.

.. note::
  Responses to GET requests for the edX Enterprise API frequently contain
  the ``results`` response value. The ``results`` response value is a variable
  that represents the intended object from the GET request. For the
  ``/enterprise/api/v2/enterprise-catalogs/{catalog_id}`` endpoint, the
  ``results`` object holds an array of objects that list information about
  each individual course in the catalog.

.. list-table::
   :widths: 25 20 80
   :header-rows: 1

   * - Field
     - Data Type
     - Description
   * - ``count``
     - integer
     - The number of courses in the catalog.
   * - ``next``
     - string
     - The URL for the next page of results.
   * - ``previous``
     - string
     - The URL for the previous page of results.
   * - ``results``
     - array
     - A list of content items in the catalog.

Each top-level object in the ``results`` array represents a course
in the catalog. See :ref:`course<course Fields>` for information about the
fields in a course item in the ``results``.


.. _enterprise_catalogs_courses Endpoint:

*********************************************************************
enterprise-catalogs/{catalog_id}/courses/{course_key} Endpoint
*********************************************************************

GET calls to the ``enterprise-catalogs/{catalog_id}/courses/{course_key}``
endpoint return information about a single course in a specified course
catalog. In the GET call, you pass a catalog ID, which you can get using the
``enterprise-catalogs`` endpoint, and a course key (a unique identifier for a
course), which you can get from the ``key`` value returned by the
``enterprise-catalogs/{catalog_id}`` endpoint. By default, the information is
returned in XML format. The information returned is described in
:ref:`course Fields`.

===================
Method and Endpoint
===================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - Endpoint
   * - GET
     - ``/enterprise/v2/enterprise-catalogs/{catalog_id}/courses/{course_key}``

=====================
Example Request
=====================
::

   curl -X GET \
   https://api.edx.org/enterprise/v2/enterprise-catalogs/3f56a21c-76c8-47c0-add8-a99714d40d94/courses/MyUni+Sport101x \
   -H "Authorization: JWT {access token}"

=====================
Response Values
=====================

The ``GET /enterprise/v2/enterprise-catalogs/{catalog_id}/courses/{course_key}``
request returns the response values described in :ref:`course Fields`.

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
     - ``/enterprise/v2/enterprise-catalogs/{catalog_id}/course-runs/{course_run_ID}``

=====================
Example Request
=====================
::

   curl -X GET \
   https://api.edx.org/enterprise/v2/enterprise-catalogs/3f56a21c-76c8-47c0-add8-a99714d40d94/course-runs/course-v1:MyUni+Sport101x \
   -H "Authorization: JWT {access token}"

=====================
Response Values
=====================

The ``GET /enterprise/v2/enterprise-catalogs/{catalog_id}/course-runs/{course_run_ID}``
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
     - ``/enterprise/v2/enterprise-catalogs/{catalog_id}/programs/{program_ID}``

=====================
Example Request
=====================
::

   curl -X GET \
   https://api.edx.org/enterprise/v2/enterprise-catalogs/3f56a21c-76c8-47c0-add8-a99714d40d94/programs/7b24a21c-98c8-47c0-b9c8-g54714d40d94 \
   -H "Authorization: JWT {access token}"


=====================
Response Values
=====================

The ``GET /enterprise/v2/enterprise-catalogs/{catalog_id}/programs/{program_uuid}``
request returns the response values described in :ref:`program Fields`.

.. _content item Fields:

***************************************
Course, Course Run, and Program Fields
***************************************

Each top-level object in the ``results`` array represents a content item
in the catalog, which may be a course, a course run, or a program. The
``results`` array returns different fields, depending on whether
the content item is a :ref:`course<course Fields>`, a
:ref:`course run<course_run Fields>`, or a :ref:`program<program Fields>`.

.. _course Fields:

================================
Fields in a course Content Item
================================

.. list-table::
   :widths: 25 20 80
   :header-rows: 1

   * - Field
     - Data Type
     - Description
   * - ``course_runs``
     - array
     - The currently existing :ref:`course runs<course_run Fields>` for the
       course.
   * - ``enrollment_url``
     - string
     - The URL for the enrollment page.
   * - ``entitlements``
     - array
     - Information about seat purchase options.
   * - ``expected_learning_items``
     - array
     - Elements of the course.
   * - ``full_description``
     - string
     - The HTML full description of the course.
   * - ``image``
     - array
     - The About page image for the course.
   * - ``key``
     - string
     - A unique identifier for the course. Example: ``edX+DemoX``.
   * - ``level_type``
     - enum string
     - The course's level of difficulty, such as ``Intermediate`` or
       ``Advanced``.
   * - ``marketing_url``
     - string
     - The URL for the course About page.
   * - ``modified``
     - datetime
     - The most recent date and time when the course metadata was modified.
   * - ``original_image``
     - string
     - The URL of the original unmodified image for the course About page.
   * - ``outcome``
     - string
     - What learners will learn from the course.
   * - ``owners``
     - array
     - The institution that offers the course.
   * - ``prerequisites``
     - array
     - Any courses a learner must complete before enrolling in the current
       course.
   * - ``prerequisites_raw``
     - array
     - Any courses a learner must complete before enrolling in the current
       course.
   * - ``programs``
     - array
     - Any programs that the course is part of.
   * - ``short_description``
     - string
     - The HTML short description of the course.
   * - ``sponsors``
     - array
     - The corporate sponsors for the course.
   * - ``subjects``
     - array
     - The academic subjects that the course covers.
   * - ``syllabus_raw``
     - string
     - The course syllabus.
   * - ``title``
     - string
     - The title of the course.
   * - ``uuid``
     - string
     - The unique identifier for the course. Example: ``0dbd8181-8866-47fc...``
   * - ``video``
     - array
     - The course About video.


.. _course_run Fields:

====================================
Fields in a course_run Content Item
====================================

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
     - Type of learning item. In this case, the value is ``courserun``.
   * - ``end``
     - datetime
     - The end date of the course run.
   * - ``enrollment_end``
     - datetime
     - The last date and time when this course run is open for learners to enroll.
       Learners cannot enroll after this date and time.
   * - ``enrollment_start``
     - datetime
     - The first date and time when this course run is open for learners to enroll.
       Learners cannot enroll before this date and time.
   * - ``enrollment_url``
     - string
     - The URL for the enrollment page.
   * - ``full_description``
     - string
     - The long description of the course and its content.
   * - ``has_enrollable_seats``
     - boolean
     - Whether learners can enroll in the course run.
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
     - integer
     - The number of weeks required to complete the content item.

.. _program Fields:

====================================
Fields in a program Content Item
====================================

A program is a collection of related courses.

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
     - Type of learning item. In this case, the value is ``program``.
   * - ``enrollment_url``
     - string
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
       or ``MicroMasters``.
   * - ``uuid``
     - string
     - The unique identifier for the program.
   * - ``weeks_to_complete_max``
     - integer
     - The maximum number of estimated weeks required to complete the program.
   * - ``weeks_to_complete_min``
     - integer
     - The minimum number of estimated weeks required to complete the
       program.

=======================================================
Example Response Showing Information about a Course Run
=======================================================

The following example response shows a single course run. A catalog may
contain many course runs.

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


.. _learner_summary Endpoint:

************************
learner-summary Endpoint
************************

GET calls to the ``learner-summary`` endpoint get information about learners'
course enrollments and progress.

===================
Method and Endpoint
===================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - Endpoint
   * - GET
     - ``/enterprise/v2/enterprise-customer/{enterprise_uuid}/learner-summary``

=====================
Example Request
=====================
::

   curl -X GET
     https://api.edx.org/enterprise/v2/enterprise-customer/{{enterprise_uuid}}/learner-summary \
     -H "Authorization: JWT {access token}"
     -H "Content-Type: application/json" \
    }]"

=====================
Response Values
=====================

The
``GET /enterprise/v2/enterprise-customer/{enterprise_uuid}/learner-summary``
request returns the following data.

.. list-table::
   :widths: 25 20 80
   :header-rows: 1

   * - Field
     - Data Type
     - Description
   * - ``consent_granted``
     - boolean
     - Whether the learner has consented to share their course data with the
       enterprise.
   * - ``coupon_code``
     - string
     - The enrollment code string used by the learner to enroll in their course. (Not applicable to Subscriptions or
       Offers)
   * - ``coupon_name``
     - string
     - The name of the enrollment code batch used by the learner to enroll in their course. (Not applicable to 
       Subscriptions or Offers)
   * - ``course_api_url``
     - string
     - The complete url for the course when using the edX API Retrieve Course Metadata endpoint.
   * - ``course_duration_weeks``
     - integer
     - The course duration in weeks.
   * - ``course_end``
     - date
     - The date the course ends, in YYYY-MM-DD format. This is the last date on
       which learners can submit answers or assessments, or otherwise be credited
       with completion of a course subsection.
   * - ``course_id``
     - string
     - A unique identifier for the course.
   * - ``course_max_effort``
     - integer
     - The estimated maximum effort required by the course, in hours per week.
   * - ``course_min_effort``
     - integer
     - The estimated minimum effort required by the course, in hours per week.
   * - ``course_pacing_type``
     - enum string
     - Whether the course is self-paced or instructor-paced.
   * - ``course_price``
     - string
     - The original price of the course, before any discounts were applied.
   * - ``course_start``
     - date
     - The date when the course begins, in YYYY-MM-DD format. This is the date
       when course content is available for learners to interact with. In most
       cases, learners can enroll in the course before the ``course_start`` date.
   * - ``course_title``
     - string
     - The name of the course.
   * - ``current_grade``
     - decimal
     - The learner's current grade, which will update as the learner proceeds through the course. For more information
       about progress and grading information, please visit: https://support.edx.org/hc/en-us/articles/4402116362519-Why-does-my-Progress-page-look-different-
   * - ``discount_price``
     - string
     - The discounted price of the course.
   * - ``enrollment_created_timestamp``
     - timestamp
     - The date and time when the learner enrolled in the course.
   * - ``enterprise_id``
     - string
     - A unique identifier for the enterprise.
   * - ``enterprise_name``
     - string
     - The name of the enterprise.
   * - ``enterprise_site_id``
     - integer
     - An identifier for the enterprise site.
   * - ``enterprise_sso_uid``
     - string
     - The learner's user ID in the Enterprise authentication system.
   * - ``enterprise_user``
     - integer
     - The learner's user ID.
   * - ``id``
     - integer
     - The enrollment ID.
   * - ``last_activity_date``
     - date
     - The most recent date the learner was active in edX.
   * - ``letter_grade``
     - string
     - Blank if the learner progress status is in progress, 'Pass' if the learner has passed the course.
   * - ``lms_user_id``
     - integer
     - The learner's user ID in the edx.org LMS.
   * - ``offer``
     - string
     - The offer ID used by the learner to enroll in their course. (Not applicable for Subscriptions, or Codes)
   * - ``passed_timestamp``
     - timestamp
     - The date and time when the learner passed the course. Null if progress status is in progress.
   * - ``progress_status``
     - enum string
     - The current status of the learner in the course. Possible values are: Failed, In Progress, Passed.
   * - ``unenrollment_end_within_date``
     - boolean
     - True if the learner has unenrolled from the course.  
   * - ``unenrollment_timestamp``
     - timestamp
     - The date the learner unenrolled from the course.
   * - ``user_account_creation_timestamp``
     - timestamp
     - The date and time when the learner's account was created in the edx.org
       LMS.
   * - ``user_country_code``
     - string
     - A two-letter country code. 
   * - ``user_current_enrollment_mode``
     - string
     - The learner's current enrollment mode in the course.
   * - ``user_email``
     - string
     - The learner's email address.
   * - ``user_username``
     - string
     - The learner's username on edx.org.


