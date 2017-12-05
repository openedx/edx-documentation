.. _Enterprise API Reference:

########################################
EdX Enterprise API Reference
########################################

This API reference includes detailed information about the ``courses`` method
of the edX Enterprise API, including the request, response data, and examples.
The example API requests shown in this reference use the ``curl`` command-line
program to send HTTP messages to the edX API. You can use any technology to
send REST API requests. The examples use the ``curl`` program to show the
syntax and data for a request in a way that is easy to read.

You can use the ``/enterprise/v1/catalogs/{id}/courses/`` endpoint to get a
list of all the active courses in a specified course catalog, along with
details about each course. Active courses are courses that are currently open
for enrollment or that will open for enrollment in the future.


********************
Method and Endpoint
********************

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - Endpoint
   * - GET
     - ``/enterprise/v1/catalogs/{id}/courses/``

=====================
Example Request
=====================
::

   curl -X GET /oauth2/v1/access_token/\
   -H "Authorization: JWT {access token}" \
   https://api.edx.org/enterprise/v1/catalogs/1/courses/

=====================
Response Values
=====================

The ``GET /enterprise/v1/catalogs/{id}/courses/`` request returns the
following response values.

.. note::
  Responses to GET requests for the edX Enterprise API frequently contain
  the ``results`` response value. The ``results`` response value is a variable
  that represents the intended JSON object from the GET request. For the
  ``/enterprise/v1/catalogs/{id}/courses/`` endpoint, the ``results`` object
  holds an array of objects that list information about each individual course
  in the catalog.

.. list-table::
   :widths: 25 20 80
   :header-rows: 1

   * - Object
     - Data Type
     - Description
   * - ``count``
     - integer
     - The number of active courses in the catalog.
   * - ``next``
     - string
     - The URL for the next page of results.
   * - ``previous``
     - string
     - The URL for the previous page of results.
   * - ``results``
     - array
     - A list of courses in the catalog.


Each JSON object in the ``results`` array contains the following response
values. Many of these values are also arrays. For more information about
these arrays, see :ref:`Enterprise_API Arrays in the courses Endpoint`.

.. list-table::
   :widths: 25 20 80
   :header-rows: 1

   * - Object
     - Data Type
     - Description
   * - ``catalog_id``
     - string
     - An identifier for the catalog that the course is part of.
   * - ``course_runs``
     - array
     - Information about specific runs of the course. See
       :ref:`Enterprise_API course runs`.
   * - ``enterprise_id``
     - string
     - The unique identifier for the organization that is using the Enterprise API.
   * - ``entitlements``
     - array
     - WHAT IS THIS?
   * - ``expected_learning_items``
     - array
     - This element is not used.
   * - ``full_description``
     - string
     - The long description of the course and its content.
   * - ``image``
     - array
     - The About page image for this course. See :ref:`Enterprise_API image`.
   * - ``key``
     - string
     - An identifier for the course. For example, ``RITx+PM9003x``.
   * - ``level_type``
     - enum string
     - The course's level of difficulty. Can be one of ``high_school``,
       ``introductory``, ``intermediate``, or ``advanced``.
   * - ``marketing_url``
     - string
     - The URL for the course About page.
   * - ``modified``
     - datetime
     - The date and time the course was last modified.
   * - ``outcome``
     - string
     - A description of what learners will accomplish if they successfully
       complete the course.
   * - ``owners``
     - array
     - The institution that offers the course. See :ref:`Enterprise_API
       organization`.
   * - ``prerequisites``
     - array
     - Any courses a learner must complete before enrolling in the current
       course. See :ref:`Enterprise_API prerequisites`.
   * - ``short_description``
     - string
     - The short description of the course and its content.
   * - ``sponsors``
     - array
     - The corporate sponsor for the course. See :ref:`Enterprise_API
       organization`.
   * - ``subjects``
     - array
     - Academic subjects that this course covers. See :ref:`Enterprise_API
       subjects`.
   * - ``title``
     - string
     - The title of the course.
   * - ``tpa_hint``
     - string
     - SOMETHING ABOUT SSO. One of ``saml-mtd``.
   * - ``uuid``
     - string
     - The unique identifier for the course,
   * - ``video``
     - array
     - The course About video. See :ref:`Enterprise_API video`.


.. _Enterprise_API Arrays in the courses Endpoint:

*********************************
Arrays in the Courses Endpoint
*********************************

The response values in the ``/enterprise/v1/catalogs/{id}/courses/`` endpoint
contain a number of arrays. Some of these arrays contain additional arrays. The
following list includes the arrays contained in the response values for the
``/enterprise/v1/catalogs/{id}/courses/`` endpoint.

.. _Enterprise_API course runs:

============
course_runs
============

Each element returned in the ``course_runs`` array represents one session of
the course and contains the following response values.

.. list-table::
   :widths: 25 20 80
   :header-rows: 1

   * - Object
     - Data Type
     - Description
   * - ``announcement``
     - datetime
     - Day and time when the course run will be announced and visible.
   * - ``availability``
     - enum string
     - One of ``Upcoming``, MORE.
   * - ``content_language``
     - string
     - The language for this course run.
   * - ``course``
     - string
     - The key value for this course.
   * - ``eligible_for_financial_aid``
     - boolean
     - Whether financial aid is available for learners.
   * - ``end``
     - datetime
     - The course run end date.
   * - ``enrollment_start``
     - datetime
     - The course run enrollment start date.
   * - ``enrollment_end``
     - datetime
     - The course run enrollment end date.
   * - ``full_description``
     - string
     - The long description of the course and its content.
   * - ``hidden``
     - boolean
     - Whether this course run is hidden. FROM WHAT?
   * - ``image``
     - array
     - The About page image for the course. See :ref:`Enterprise_API image`.
   * - ``instructors``
     - array
     - Information about the course instructors. See :ref:`Enterprise_API
       person`. DO WE HAVE THIS AND STAFF?
   * - ``key``
     - string
     - An identifier for the course run.
   * - ``level_type``
     - enum string
     - The course's level of difficulty. Can be one of ``high_school``,
       ``introductory``, ``intermediate``, or ``advanced``.
   * - ``license``
     - string
     -
   * - ``marketing_url``
     - string
     - The URL for the course About page.
   * - ``min_effort``
     - integer
     - The minimum number of estimated hours of effort per week.
   * - ``max_effort``
     - integer
     - The maximum number of estimated hours of effort per week.
   * - ``mobile_available``
     - boolean
     - Whether the course run is available for mobile devices.
   * - ``modified``
     - datetime
     - The date and time the course was last modified.
   * - ``outcome``
     - string
     - A description of what learners will accomplish if they successfully
       complete the course.
   * - ``pacing_type``
     - enum string
     - The pacing of the course. May be ``self-paced`` or ``instructor-paced``.
   * - ``reporting_type``
     - enum string
     - Information about what type of reporting is available for the enterprise.
       May be ``mooc`` or WHAT?.
   * - ``seats``
     - array
     - The available modes for this course run. See :ref:`Enterprise_API seats`.
   * - ``short_description``
     - string
     - The short description of the course and its content.
   * - ``staff``
     - array
     - Information about the course staff. See :ref:`Enterprise_API person`.
   * - ``start``
     - datetime
     - The course run start date.
   * - ``status``
     - enum string
     - The published status of the course. May be ``published`` or WHAT?.
   * - ``title``
     - string
     - The title of the course.
   * - ``track_selection_url``
     - string
     - The URL of the page on which learners select enrollment mode (Verified
       or Audit).
   * - ``transcript_languages``
     - array[string]
     - ISO codes for languages in which video transcripts are available.
   * - ``uuid``
     - string
     - A unique identifier for this course run.
   * - ``video``
     - array
     - The About video for this course run. See :ref:`Enterprise_API video`.
   * - ``weeks_to_complete``
     - number
     - The number of weeks it should take a learner to complete this course.


.. _Enterprise_API image:

image
======

The following ``image`` objects have identical response values.

* ``image``
* ``logo_image``
* ``profile_image``

The ``image`` object has the following response values.

.. list-table::
   :widths: 25 20 80
   :header-rows: 1

   * - Object
     - Data Type
     - Description
   * - ``src``
     - string
     - The URL where the image is located.
   * - ``description``
     - string
     - A description of the image.
   * - ``height``
     - integer
     - The height of the image in pixels.
   * - ``width``
     - integer
     - The width of the image in pixels.


.. _Enterprise_API organization:

organization
==============

The following ``organization`` objects have identical response values.

* ``owners``
* ``sponsors``

The ``organization`` object has the following response values.

.. list-table::
   :widths: 25 20 80
   :header-rows: 1

   * - Object
     - Data Type
     - Description
   * - ``key``
     - string
     - The unique ID for the organization.
   * - ``name``
     - string
     - The name of the organization.
   * - ``description``
     - string
     - A description of the organization.
   * - ``logo_image``
     - array
     - See :ref:`Enterprise_API image`.
   * - ``homepage_url``
     - string
     - The URL of the organization's home page.


.. _Enterprise_API person:

person
=========

The following ``person`` objects have identical response values.

* ``instructor``
* ``staff``

The ``person`` object has the following response values.

.. list-table::
   :widths: 25 20 80
   :header-rows: 1

   * - Object
     - Data Type
     - Description
   * - ``uuid``
     - string
     - A unique identifier for the instructor or staff member.
   * - ``given_name``
     - string
     - The first name of the instructor or staff member.
   * - ``family_name``
     - string
     - The last name of the instructor or staff member.
   * - ``position``
     - array
     - Information about the instructor or staff member's job. See
       :ref:`Enterprise_API position`.
   * - ``email``
     - string
     - The email address of the instructor or staff member.
   * - ``profile_image``
     - array
     - See :ref:`Enterprise_API image`.
   * - ``urls``
     - array
     - The URLs of the person's blog, Twitter, and Facebook accounts.

.. _Enterprise_API position:

==============
position
==============

The ``position`` object in the ``person`` object is an array that contains the
following values.

.. list-table::
   :widths: 25 20 80
   :header-rows: 1

   * - Object
     - Data Type
     - Description
   * - ``organization_name``
     - string
     - The name of the person's organization.
   * - ``organization_id``
     - string
     - An identifier for the organization.
   * - ``title``
     - string
     - The official title of the instructor or staff member.

.. _Enterprise_API prerequisites:

prerequisites
==================

Any courses a learner must complete before enrolling in the current course.

.. list-table::
   :widths: 25 20 80
   :header-rows: 1

   * - Object
     - Data Type
     - Description
   * - ``name``
     - string
     - The name of the prerequisite course.


.. _Enterprise_API seats:

seats
=========

The available modes for this course.

.. list-table::
   :widths: 25 20 80
   :header-rows: 1

   * - Object
     - Data Type
     - Description
   * - ``type``
     - string
     - The course mode or modes that the course offers. Possible values are
       ``audit``, ``credit``, ``honor``, ``professional education``, or
       ``verified``.
   * - ``price``
     - string
     - The cost in USD of a verified certificate, a professional education
       certificate, or academic credit for the course.
   * - ``currency``
     - string
     - The currency in which the course accepts payment. This value will always
       be ``USD``.
   * - ``upgrade_deadline``
     - string
     - The deadline for learners to upgrade from the audit track to the
       verified certificate track.
   * - ``credit_provider``
     - string
     - The institution that offers academic credit for learners who pass the
       course.
   * - ``credit_hours``
     - integer
     - The number of credit hours that learners who pass the course earn.

.. _Enterprise_API subjects:

subjects
=========

Academic subjects that this course covers.

.. list-table::
   :widths: 25 20 80
   :header-rows: 1

   * - Object
     - Data Type
     - Description
   * - ``name``
     - string
     - Name of a subject, such as "computer science" or "history".

**Example values:**

::

    Architecture
    Chemistry
    Computer Science
    Economics & Finance
    Health & Safety
    History
    Music
    Physics
    Social Sciences

.. _Enterprise_API video:

video
=========

.. list-table::
   :widths: 25 20 80
   :header-rows: 1

   * - Object
     - Data Type
     - Description
   * - ``src``
     - string
     - The URL at which the video is available.
   * - ``description``
     - string
     - The description of the video.
   * - ``image``
     - array
     - See :ref:`Enterprise_API image`.


=======================================================
Example Response Showing Information about a Course
=======================================================

The following example response shows a single course. A catalog may contain
many courses.
::

 {
   "count":123,
   "next":"https://api.edx.org/enterprise/v1/catalogs/1/courses/?limit=20&offset=40",
   "previous":"https://api.edx.org/enterprise/v1/catalogs/1/courses/?limit=20&offset=0",
   "results":[
      {
         "key":"example_course_key",
         "title":"Title of the Course",
         "short_description":"Short description of course content",
         "full_description":"Longer, more detailed description of course content.",
         "level_type":"Introductory",
         "subjects":[
            {
               "name":"Name of subject"
            }
         ],
         "prerequisites":[

         ],
         "expected_learning_items":[

         ],
         "image":[
            {
               "src":"https://example.com/directory/course_image.jpg",
               "description":"Example image for the Example Title course",
               "height":"300",
               "width":"400"
            }
         ],
         "video":[
            {
               "src":"http://www.youtube.com/watch?v=abcdefghijk",
               "description":null,
               "image":null
            }
         ],
         "owners":[
            {
               "key":"example_institution_key",
               "name":"Example Institution",
               "description":null,
               "logo_image":[
                  {
                     "src":"https://example.com/directory/institution_logo.jpg",
                     "description":null,
                     "height":"200",
                     "width":"200"
                  }
               ],
               "homepage_url":null
            }
         ],
         "sponsors":[

         ],
         "modified":"YYYY-MM-DDTHH:MM:SS.SSSSSSZ",
         "course_runs":[
            {
               "course":"course_number",
               "key":"example_course_key",
               "title":"Title of the Course",
               "short_description":"Short description of course content",
               "full_description":"Longer, more detailed description of course content",
               "start":"YYYY-MM-DDTHH:MM:SSZ",
               "end":"YYYY-MM-DDTHH:MM:SSZ",
               "enrollment_start":"YYYY-MM-DDTHH:MM:SSZ",
               "enrollment_end":"YYYY-MM-DDTHH:MM:SSZ",
               "announcement":null,
               "image":[
                  {
                     "src":"https://example.com/directory/course_image.jpg",
                     "description":null,
                     "height":"200",
                     "width":"300"
                  }
               ],
               "video":null,
               "seats":[
                  {
                     "type":"credit",
                     "price":"100.00",
                     "currency":"USD",
                     "upgrade_deadline":"YYYY-MM-DDTHH:MM:SSZ",
                     "credit_provider":"example institution",
                     "credit_hours":3
                  }
               ],
               "content_language":null,
               "transcript_languages":[

               ],
               "instructors":[

               ],
               "staff":[
                  {
                     "key":"staff_key",
                     "name":"Staff Member Name",
                     "title":"Staff Member Title",
                     "bio":"Example staff member bio.",
                     "profile_image":{
                        "src":"https://example.com/image/staff_member_name.png",
                        "description":null,
                        "height":"150",
                        "width":"150"
                     }
                  }
               ],
               "pacing_type":"instructor_paced",
               "min_effort":null,
               "max_effort":null,
               "modified":"YYYY-MM-DDTHH:MM:SSZ"
            }
         ],
         "marketing_url":"https://courses.edx.org/course/edxd103?enterprise_id=b0990312-c5a3-48c4-b0fe-b8d844249623&tpa_hint=saml-example-shib&utm_medium=affiliate_partner&catalog_id=13&utm_source=mattdrayer"
      }
   ]
 }
