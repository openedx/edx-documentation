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

- **/policy-allocation/{policy_uuid}/allocate/** - You can make POST calls to the
  ``/enterprise/v1/policy-allocation/{policy_uuid}/allocate/`` endpoint to allocate
  an assignment in the requested SubsidyAccessPolicy record to a list of users.
  For details, see :ref:`policy_allocation Endpoint`.

- **/assignment-configurations/remind** - You can make POST calls to the
  ``/enterprise/v1/assignment-configurations/{assignment_configuration_uuid}/admin/assignments/remind/`` to remind learner(s) of their content assignments.
  For details, see :ref:`assignment-configurations-remind Endpoint`.

- **/assignment-configurations/cancel** - You can make POST calls to the
  ``enterprise/v1/assignment-configurations/{assignment_configuration_uuid}/admin/assignments/cancel/`` to cancel the learner(s) content assignments.
  For details, see :ref:`assignment-configurations-cancel Endpoint`.

- **/subscriptions** - You can make GET calls to the
  ``/enterprise/v1/subscriptions`` endpoint to get a list of subscription plans.
  For details, see :ref:`subscriptions_summary Endpoint`.

- **/subscriptions/{subscription_plan_uuid}/licenses/assign** - You can make POST calls to the
  ``/enterprise/v1/subscriptions/{subscription_plan_uuid}/licenses/assign`` endpoint to assign
  licenses to a list of users in the given subscription plan.
  For details, see :ref:`licenses_assign Endpoint`.

- **/subscriptions/{subscription_plan_uuid}/licenses/bulk-revoke** - You can make POST calls to the
  ``/enterprise/v1/subscriptions/{subscription_plan_uuid}/licenses/bulk-revoke`` endpoint to revoke
  licenses of learners in the given subscription plan.
  For details, see :ref:`licenses_revoke Endpoint`.

- **/bulk-license-enrollment** - You can make POST calls to the
  ``/enterprise/v1/bulk-license-enrollment`` to bulk enroll learners in given list of courses.
  For details, see :ref:`bulk-license-enrollment Endpoint`.

- **/enterprise-catalogs** - You can make GET calls to the
  ``/enterprise/v2/enterprise-catalogs`` endpoint to get a list of all the course catalogs
  that are available to your organization.
  For details, see :ref:`enterprise_catalogs Endpoint`.

- **/enterprise-catalogs/{catalog_id}** - You can make GET calls to the
  ``/enterprise/v2/enterprise-catalogs/{catalog_id}`` endpoint to get a list of all the
  active courses in a specified course catalog. Active courses are courses
  that are currently open for enrollment or that will open for enrollment in
  the future.
  For details, see :ref:`enterprise_catalogs_catalogID Endpoint`.
- **/enterprise-catalogs/{catalogID}/courses/{course_key}** - You can make GET
  calls to the ``/enterprise/v2/enterprise-catalogs/{catalog_id}/courses/{course_key}``
  endpoint to get information about a single course.
  For details, see :ref:`enterprise_catalogs_courses Endpoint`.
- **/enterprise-catalogs/{catalogID}/course-runs/{course_run_ID}** - You can make GET calls to the
  ``/enterprise/v2/enterprise-catalogs/{catalog_id}/course-runs/{course_run_ID}`` endpoint
  to get information about a single course run.
  For details, see :ref:`enterprise_catalogs_courserun Endpoint`.

- **/enterprise-catalogs/{catalogID}/programs/{program_ID}** - You can make GET calls to the
  ``/enterprise/v2/enterprise-catalogs/{catalog_id}/programs/{program_ID}`` endpoint
  to get information about a single program.
  For details, see :ref:`enterprise_catalogs_programs Endpoint`.

- **/learner-summary** - You can make GET calls to the
  ``/enterprise/v3/enterprise-customer/{enterprise_uuid}/learner-summary`` endpoint to get a list of information about your
  enterprise learners and their status in the courses they are enrolled in.
  For details, see :ref:`learner_summary Endpoint`.


  `Use this JSON file <https://raw.githubusercontent.com/openedx/edx-documentation/master/en_us/enterprise_api/source/api_reference/edX_Enterprise_API_Reference%20Collection.postman_collection.json>`_ to import into your `Postman enviroment <https://learning.postman.com/docs/getting-started/importing-and-exporting-data/>`_ . It includes the endpoints mentioned above.

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

.. _Policy_allocation Endpoint:

**************************
policy-allocation Endpoint
**************************

POST calls to the ``policy-allocation`` endpoint to allocate an assignment to a list of users provided in the request body in the requested content_key.

===================
Method and Endpoint
===================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - Endpoint
   * - POST
     - ``/enterprise/v1/policy-allocation/{policy_uuid}/allocate/``

==============
Request Values
==============
The ``POST /enterprise/v1/policy-allocation/{policy_uuid}/allocate/`` request accepts the following values in the body of the request:

.. list-table::
   :widths: 25 20 80
   :header-rows: 1

   * - Field
     - Data Type
     - Description
   * - ``learner_emails``
     - array
     - Learner emails to whom assignment should be allocated.
   * - ``content_key``
     - string
     - Course content_key to which these learners are assigned.
   * - ``content_price_cents``
     - integer
     - The price, in USD cents, of this content at the time of allocation. Must be >= 0.

===============
Example Request
===============
::

   curl -X POST
     https://api.edx.org/enterprise/v1/policy-allocation/904b1785-9d3a-1000-848d-6ae7a56e6355/allocate/ \
     -H 'Authorization: JWT {access token}'
     -H 'Content-Type: application/json' \
     -d '{"learner_emails":["abc@example.com","xyz@example.com"],"content_key":"edx+api101","content_price_cents":1000}'

===============
Response Values
===============
The ``/enterprise/v1/policy-allocation/{policy_uuid}/allocate/`` request returns the following response values:

.. list-table::
   :widths: 25 20 80
   :header-rows: 1

   * - Field
     - Data Type
     - Description
   * - ``updated``
     - integer
     - Assignment records whose state was transitioned to "allocated" as a result of this action.
   * - ``created``
     - integer
     - New assignment records that were created as a result of this action.
   * - ``no_change``
     - array
     - Already-allocated assignment records related to the requested policy, learner email(s), and content for this action.

===================
Example Response
===================

A sample response with a status `202 Accepted` will look like:

::

   {
        "updated": [],
        "created": [
            {
                "uuid": "4fa11bd53f29c131aa72",
                "assignment_configuration": "6fc7ef56e6eb209f7668",
                "learner_email": "abc@example.com",
                "lms_user_id": 123123,
                "content_key": "edx+101",
                "content_title": "edX 101",
                "content_quantity": -10000,
                "state": "allocated",
                "transaction_uuid": null,
                "actions": [],
                "earliest_possible_expiration": {
                    "date": "2024-08-20T11:58:34.666249Z",
                    "reason": "NINETY_DAYS_PASSED"
                }
            }
        ],
        "no_change": []
   }

.. _Assignment-configurations-remind Endpoint:

*************************************************************************************
assignment-configurations-remind  Endpoint
*************************************************************************************

POST calls to the ``assignment-configurations-remind`` endpoint reminds learners of their content assignments.

===================
Method and Endpoint
===================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - Endpoint
   * - POST
     - ``enterprise/v1/assignment-configurations/{assignment_configuration_uuid}/admin/assignments/remind/``

=====================
Request Values
=====================
The ``POST enterprise/v1/assignment-configurations/{assignment_configuration_uuid}/admin/assignments/remind/`` request accepts the following values in the body of the request:

.. list-table::
   :widths: 25 20 80
   :header-rows: 1

   * - Field
     - Data Type
     - Description
   * - ``assignment_uuids``
     - array
     - List of assignment UUIDs for the learners that need to be reminded of, associated with the assignment configuration UUID specified in the URL.

=====================
Example Request
=====================

Request payload
::

   curl -X POST
     https://api.edx.org/enterprise/v1/assignment-configurations/6fc7ef56-d1c4-4aa8-a649-e6eb209f0000/admin/assignments/remind/ \
     -H 'Authorization: JWT {access token}'
     -H 'Content-Type: application/json' \
     -d '{"assignment_uuids":["8977ef56-d1c4-4aa8-a649-e6eb209f0000","8907ef56-d1c4-4aa8-a649-e6eb209f0000"]'

===================
Example Response
===================

A sample response with a status `200 OK` will be returned


.. _Assignment-configurations-cancel Endpoint:

*************************************************************************************
assignment-configurations-cancel  Endpoint
*************************************************************************************

POST calls to the ``/assignment-configurations-cancel`` cancels content assignments of learners.

===================
Method and Endpoint
===================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - Endpoint
   * - POST
     - ``enterprise/v1/assignment-configurations/{assignment_configuration_uuid}/admin/assignments/cancel/``

=====================
Request Values
=====================
The ``POST enterprise/v1/assignment-configurations/{assignment_configuration_uuid}/admin/assignments/cancel/`` request accepts the following values in the body of the request:

.. list-table::
   :widths: 25 20 80
   :header-rows: 1

   * - Field
     - Data Type
     - Description
   * - ``assignment_uuids``
     - array
     - List of assignment UUIDs for the learners that need to be canceled, associated with the assignment configuration UUID specified in the URL.

=====================
Example Request
=====================

Request payload
::

   curl -X POST
     https://api.edx.org/enterprise/v1/assignment-configurations/6fc7ef56-d1c4-4aa8-a649-e6eb209f0000/admin/assignments/cancel/ \
     -H 'Authorization: JWT {access token}'
     -H 'Content-Type: application/json' \
     -d '{"assignment_uuids":["8977ef56-d1c4-4aa8-a649-e6eb209f0000","8907ef56-d1c4-4aa8-a649-e6eb209f0000"]'

===================
Example Response
===================

A sample response with a status `200 OK` will be returned

.. _Subscriptions_summary Endpoint:

**********************
subscriptions Endpoint
**********************

GET calls to the ``subscriptions`` endpoint to get a list of subscription plans.

===================
Method and Endpoint
===================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - Endpoint
   * - GET
     - ``/enterprise/v1/subscriptions``

=====================
Example Request
=====================

::

   curl -X GET
     https://api.edx.org/enterprise/v1/subscriptions \
     -H "Authorization: JWT {access token}"
     -H "Content-Type: application/json"

=====================
Parameters
=====================

You can use optional query parameters to get specific subscription plans.

.. list-table::
   :widths: 25 20 80
   :header-rows: 1

   * - Parameter
     - Data Type
     - Description
   * - ``enterprise_customer_uuid``
     - string
     - The unique identifier for the customer.
   * - ``page``
     - integer
     - The page number of the results.
   * - ``current``
     - bool (Nullable)
     - returns the active subscription plan

For example:

::

   curl -X GET
    https://api.edx.org/enterprise/v1/subscriptions?enterprise_customer_uuid=904b1785-9d3a-1000-848d-6ae7a56e6355&page=1&current=true \
    -H "Authorization: JWT {access token}"
    -H "Content-Type: application/json"

=====================
Response Values
=====================

The ``GET /enterprise/v1/subscriptions`` request returns the following response values:

.. list-table::
   :widths: 25 20 80
   :header-rows: 1

   * - Field
     - Data Type
     - Description
   * - ``count``
     - integer
     - The number of subscription plans.
   * - ``next``
     - string
     - The URL for the next page of results.
   * - ``previous``
     - string
     - The URL for the previous page of results.
   * - ``results``
     - array (obj)
     - A list of subscription plans.

Each top-level object in the ``results`` array represents a subscription plan.
The ``results`` for a subscription plan returns an array of objects with the following fields:

.. list-table::
   :widths: 25 20 80
   :header-rows: 1

   * - Field
     - Data Type
     - Description
   * - ``title``
     - string
     - The title of the subscription plan.
   * - ``uuid``
     - string
     - A unique identifier for the subscription plan.
   * - ``start_date``
     - string
     - Datetime string of the start date of the subscription plan.
   * - ``expiration_date``
     - string
     - Datetime string of the expiration date of the subscription plan.
   * - ``enterprise_customer_uuid``
     - string
     - The customer's unique identifier linked to the subscription plan.
   * - ``enterprise_catalog_uuid``
     - string
     - The catalog's unique identifier linked to the subscription plan.
   * - ``is_active``
     - bool (Nullable)
     - Whether or not the subscription plan is active.
   * - ``is_revocation_cap_enabled``
     - bool (Nullable)
     - Whether or not the subscription plan allows the revocation of licenses.
   * - ``days_until_expiration``
     - integer
     - The number of days until the subscription plan expires.
   * - ``days_until_expiration_including_renewals``
     - integer
     - The number of days until the subscription plan expires, including renewals.
   * - ``is_locked_for_renewal_processing``
     - bool (Nullable)
     - Whether or not the subscription plan is locked for renewal processing.
   * - ``should_auto_apply_licenses``
     - bool (Nullable)
     - Whether or not the subscription plan should automatically apply licenses.
   * - ``licenses``
     - obj
     - The details about the licenses in the subscription plan.
   * - ``revocations``
     - bool (Nullable)
     - The details about the revocations in the subscription plan.
   * - ``prior_renewals``
     - array
     - The details about the prior renewals in the subscription plan.

===================
Example Response
===================

A sample response with a status `200 OK` will look like:

::

   {
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "title": "Enterprise Subscription",
            "uuid": "104b1785-1d3a-1000-148d-1ae7a56e6355",
            "start_date": "2023-01-01T00:00:00Z",
            "expiration_date": "2024-01-01T00:00:00Z",
            "enterprise_customer_uuid": "204b1785-2d3a-2000-248d-2ae7a56e6355",
            "enterprise_catalog_uuid": "304b1785-3d3a-3000-348d-3ae7a56e6355",
            "is_active": true,
            "is_revocation_cap_enabled": true,
            "days_until_expiration": 365,
            "days_until_expiration_including_renewals": 365,
            "is_locked_for_renewal_processing": false,
            "should_auto_apply_licenses": true,
            "licenses": {
                "activated": 0,
                "assigned": 0,
                "unassigned": 100,
                "revoked": 0,
                "total": 100,
                "allocated": 0
            },
            "revocations": {
                "total": 0,
                "used": 0,
                "remaining": 0
            },
            "prior_renewals": [
                {
                    "prior_subscription_plan_id": "4b27b24a-48f5-4266-448e-47d5b7deacb2",
                    "prior_subscription_plan_start_date": "2021-01-01 00:00:00+00:00",
                    "renewed_subscription_plan_id": "59f50cb8-4b22-4e21-9119-e0022955f9cb",
                    "renewed_subscription_plan_start_date": "2021-07-01 00:00:00+00:00"
                }
            ]
        }
    ]
   }


.. _Licenses_assign Endpoint:

************************
licenses/assign Endpoint
************************

POST calls to the ``licenses/assign`` endpoint to assign a license to a list of users provided in request body in the given subscription plan specified in the path.

===================
Method and Endpoint
===================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - Endpoint
   * - POST
     - ``enterprise/v1/subscriptions/{subscription_plan_uuid}/licenses/assign``

=====================
Request Values
=====================
The ``POST enterprise/v1/subscriptions/{subscription_plan_uuid}/licenses/assign`` request accepts the following values in the body of the request:

.. list-table::
   :widths: 25 20 80
   :header-rows: 1

   * - Field
     - Data Type
     - Description
   * - ``user_emails``
     - array
     - A list of user emails to assign licenses to.
   * - ``user_sfids``
     - array
     - A list of user Salesforce ids.
   * - ``greeting``
     - string
     - An opening body that will be added at the start of email if users are supposed to be notified of their assignment.
   * - ``closing``
     - string
     - A closing body that will be added at the bottom of email.
   * - ``notify_users``
     - boolean
     - To specify if learners should be notified after assignment.

=====================
Example Request
=====================
::

   curl -X POST
     https://api.edx.org/enterprise/v1/subscriptions/904b1785-9d3a-1000-848d-6ae7a56e6355/licenses/assign \
     -H 'Authorization: JWT {access token}'
     -H 'Content-Type: application/json' \
     -d '{"user_emails":["abc@example.com","xyz@example.com"],"user_sfids":["001OE000001f26OXZP","001OE000001a25WXYZ"],"greeting":"Hello","closing":"Bye","notify_users":true}'

=====================
Response Values
=====================
The ``POST enterprise/v1/subscriptions/{subscription_plan_uuid}/licenses/assign`` request returns the following response values:

.. list-table::
   :widths: 25 20 80
   :header-rows: 1

   * - Field
     - Data Type
     - Description
   * - ``num_successful_assignments``
     - integer
     - Number of successful license assignments for given learners.
   * - ``num_already_associated``
     - integer
     - Number of users that have already been associated with a non-revoked license in the given subscription.
   * - ``license_assignments``
     - array
     - A list of objects where each object holds a pair of user email and license uuid for successful assignments.

===================
Example Response
===================

A sample response with a status `200 OK` will look like:

::

   {
        "num_successful_assignments": 2,
        "num_already_associated": 0,
        "license_assignments": [
            {
                "user_email": "abc@example.com",
                "license": "30824248-e671-449f-8bf7-02715478abce"
            },
            {
                "user_email": "xyz@example.com",
                "license": "30821223-e671-449f-8bf7-02715478xyze"
            }
        ]
   }

.. _Licenses_revoke Endpoint:

*****************************
licenses/bulk-revoke Endpoint
*****************************

POST calls to the ``licenses/bulk-revoke`` endpoint to revoke one or more licenses in the given subscription plan.

===================
Method and Endpoint
===================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - Endpoint
   * - POST
     - ``enterprise/v1/subscriptions/{subscription_plan_uuid}/licenses/bulk-revoke``

=====================
Request Values
=====================
The ``POST enterprise/v1/subscriptions/{subscription_plan_uuid}/licenses/bulk-revoke`` request accepts the following values in the body of the request:

.. list-table::
   :widths: 25 20 80
   :header-rows: 1

   * - Field
     - Data Type
     - Description
   * - ``user_emails``
     - array
     - List of emails with which licenses are associated.
   * - ``filters``
     - array
     - A list of objects that either hold user email value for lookup or a list of valid statuses of license for filtering. A request must either provide ``user_email`` or ``filters``, but not both. Valid values for statuses are: ``activated``, ``assigned``, ``unassigned``, and ``revoked``.

=====================
Example Request
=====================

Request payload with ``user_emails``
::

   curl -X POST
     https://api.edx.org/enterprise/v1/subscriptions/904b1785-9d3a-1000-848d-6ae7a56e6355/licenses/bulk-revoke \
     -H 'Authorization: JWT {access token}'
     -H 'Content-Type: application/json' \
     -d '{"user_emails":["abc@example.com","xyz@example.com"]}'

Request payload with ``filters``
::

   curl -X POST
     https://api.edx.org/enterprise/v1/subscriptions/904b1785-9d3a-1000-848d-6ae7a56e6355/licenses/bulk-revoke \
     -H 'Authorization: JWT {access token}'
     -H 'Content-Type: application/json' \
     -d '{"filters":[{"user_email": "al"}]}'

::

   curl -X POST
     https://api.edx.org/enterprise/v1/subscriptions/904b1785-9d3a-1000-848d-6ae7a56e6355/licenses/bulk-revoke \
     -H 'Authorization: JWT {access token}'
     -H 'Content-Type: application/json' \
     -d '{"filters":[{"status_in": ["activated", "assigned"]}]}'


=====================
Response
=====================

The ``POST enterprise/v1/subscriptions/{subscription_plan_uuid}/licenses/bulk-revoke`` request can return the following responses:

    204 No Content - All revocations were successful.

    400 Bad Request - Some error occurred when processing one of the revocations, no revocations were committed. An error message is provided.

    404 Not Found - No license exists in the plan for one of the given email addresses, or the license is not in an assigned or activated state. An error message is provided.

.. _Bulk-license-enrollment Endpoint:

*************************************************************************************
/bulk-license-enrollment Endpoint
*************************************************************************************

POST calls to the ``/bulk-license-enrollment`` to bulk enroll learners in given list of courses.

===================
Method and Endpoint
===================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - Endpoint
   * - POST
     - ``enterprise/v1/bulk-license-enrollment``

=====================
Request Values
=====================
The ``POST enterprise/v1/bulk-license-enrollment`` request accepts the following values in the body of the request:

.. list-table::
   :widths: 25 20 80
   :header-rows: 1

   * - Field
     - Data Type
     - Description
   * - ``enterprise_customer_uuid``
     - string
     - The uuid of the associated enterprise customer provided as a query param.
   * - ``emails``
     - array
     - List of learner emails to bulk enroll in given list of courses. Limit is ``1000`` learners + course keys.
   * - ``course_run_keys``
     - array
     - List of course keys.
   * - ``notify``
     - boolean
     - Notify users about the enrollment.

=====================
Example Request
=====================

Request payload
::

   curl -X POST
     https://api.edx.org/enterprise/v1/bulk-license-enrollment?enterprise_customer_uuid=abcd-aeiou-wxyz \
     -H 'Authorization: JWT {access token}'
     -H 'Content-Type: application/json' \
     -d '{"emails":["abc@example.com","xyz@example.com"], "course_run_keys":["testX"], "notify": true}'

===================
Example Response
===================

A sample response with a status `201 Created` will look like:

::

   {
    "job_id": "<UUID4>"
   }


.. _Enterprise_catalogs Endpoint:

****************************
enterprise-catalogs Endpoint
****************************

GET calls to the ``enterprise-catalogs`` endpoint to get list of all the course catalogs that are available to your organization.

===================
Method and Endpoint
===================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - Endpoint
   * - GET
     - ``/enterprise/v2/enterprise-catalogs``

=====================
Example Request
=====================
::

   curl -X GET
     https://api.edx.org/enterprise/v2/enterprise-catalogs \
     -H "Authorization: JWT {access token}"
     -H "Content-Type: application/json" \
    }]"

=====================
Response Values
=====================
The ``GET /enterprise/v2/enterprise-catalogs`` request returns  the values: ``count``, ``next``, ``previous``, ``results`` described here: :ref:`response_Values`.
The ``results`` response value include these fields:

.. list-table::
   :widths: 25 20 80
   :header-rows: 1

   * - Field
     - Data Type
     - Description
   * - ``uuid``
     - string
     - A unique identifier for the catalog.
   * - ``title``
     - string
     - The name that describes the catalog.
   * - ``enterprise_customer``
     - string
     - The customer's unique identifier links to a catalog.
   * - ``catalog_query_uuid``
     - string
     - A unique identifier for the catalog query.
   * - ``content_last_modified``
     - string
     - Datetime string of the last time the content in the catalog was updated.
   * - ``catalog_modified``
     - string
     - Datetime string of the last time the catalog was modified.
   * - ``query_title``
     - string
     - The string title of the query used by the catalog.
   * - ``include_exec_ed_2u_courses``
     - bool (Nullable)
     - Whether or not the catalog allows the linking of Executive Education content.

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

.. _response_Values:

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
   * - ``key``
     - string
     - A unique identifier for the course. Example: ``edX+DemoX``.
   * - ``uuid``
     - string
     - The unique identifier for the course. Example: ``0dbd8181-8866-47fc...``
   * - ``title``
     - string
     - The title of the course.
   * - ``course_runs``
     - array (obj)
     - The currently existing :ref:`course runs<course_run Fields>` for the
       course.
   * - ``enrollment_url``
     - string
     - The URL for the enrollment page.
   * - ``entitlements``
     - array (obj)
     - Information about seat purchase options. Items includes ``mode``,
       ``price``, ``currency``, ``sku`` and ``expires``.
   * - ``owners``
     - array
     - The institution that offers the course.
   * - ``image``
     - obj
     - The About page image for the course.
   * - ``short_description``
     - string
     - The HTML short description of the course.
   * - ``type``
     - string
     - UUID associated with the course type object.
   * - ``url_slug``
     - string
     - The course identifying slug used in related url paths
   * - ``course_type``
     - string
     - The course type. Example: ``verified-audit``.
   * - ``enterprise_subscription_inclusion``
     - boolean
     - Signifies if this course is in the enterprise subscription catalog.
   * - ``excluded_from_seo``
     - boolean
     - Signifies if the course's About Page will be excluded from indexing.
   * - ``excluded_from_search``
     - boolean
     - Signifies if this course will show up in search results.
   * - ``full_description``
     - string
     - The HTML full description of the course.
   * - ``level_type``
     - enum string
     - The course's level of difficulty, such as ``Intermediate`` or
       ``Advanced``.
   * - ``subjects``
     - array (obj)
     - The academic subjects that the course covers.
   * - ``prerequisites``
     - array (obj)
     - Any courses a learner must complete before enrolling in the current
       course.
   * - ``prerequisites_raw``
     - array
     - Any courses a learner must complete before enrolling in the current
       course.
   * - ``expected_learning_items``
     - array
     - Elements of the course learning items records.
   * - ``video``
     - obj
     - The course About video record.
   * - ``sponsors``
     - array
     - The corporate sponsors for the course.
   * - ``modified``
     - datetime
     - The most recent date and time when the course metadata was modified.
   * - ``marketing_url``
     - string
     - The URL for the course About page.
   * - ``syllabus_raw``
     - string
     - The course syllabus.
   * - ``outcome``
     - string
     - What learners will learn from the course.
   * - ``original_image``
     - string
     - The URL of the original unmodified image for the course About page.
   * - ``card_image_url``
     - string
     - The URL of the card image for the various course card enterprise components.
   * - ``canonical_course_run_key``
     - string
     - The unique identifying key for the course's canonical course run.
       Example: ``course-v1:edx+tr1012+1T2021``
   * - ``extra_description``
     - string
     - additional description text provided by the course author.
   * - ``additional_information``
     - string
     - Additional information relating to the course in HTML form. This
       information is only provided by administrators, not course authors,
       and as such may hold special HTML that is normally not allowed.
   * - ``additional_metadata``
     - obj
     - Additional course metadata associated with 2U courses external to the
       edX platform.
   * - ``faq``
     - string
     - HTML representation of the course FAQ section.
   * - ``learner_testimonials``
     - string
     - HTML representation of hte course learner testimonials section.
   * - ``enrollment_count``
     - integer
     - Total number of learners who have enrolled in this course.
   * - ``recent_enrollment_count``
     - integer
     - Total number of learners who have enrolled in this course in the last 6
       months.
   * - ``topics``
     - array (obj)
     - Topics associated with the course.
   * - ``key_for_reruns``
     - string
     - Course author provided key that is used for all reruns of the course.
   * - ``url_slug_history``
     - array (string)
     - List of course slugs used for the course throughout its lifespan.
   * - ``url_redirects``
     - array (string)
     - List of course url redirects.
   * - ``course_run_statuses``
     - array (string)
     - All unique course run status values associated with this course.
   * - ``editors``
     - array (obj)
     - List of course editor users.
   * - ``collaborators``
     - array (obj)
     - List of course collaborators.
   * - ``skill_names``
     - array (string)
     - List of skill names associated with the course.
   * - ``skills``
     - array (obj)
     - List of skill records associated with the course.
   * - ``organization_short_code_override``
     - string
     - Organization short code overwritten string.
   * - ``organization_logo_override_url``
     - string
     - Organization logo url overwritten.
   * - ``geolocation``
     - obj
     - Geographic location for the course, if one exists.
   * - ``location_restriction``
     - obj
     - Course location restriction record.
   * - ``in_year_value``
     - obj
     - Record related to projected value for a course.
   * - ``product_source``
     - obj
     - Record related to course origin.
   * - ``data_modified_timestamp``
     - datetime
     - The timestamp of the last time the course data was modified.
   * - ``watchers``
     - array (string)
     - The list of email addresses that will be notified if any of the course
       runs are published or scheduled.
   * - ``programs``
     - array (obj)
     - Any programs that the course is part of.
   * - ``course_run_keys``
     - array (string)
     - The list of associated course run keys.
   * - ``editable``
     - boolean
     - Whether the course is editable.
   * - ``advertised_course_run_uuid``
     - string
     - Unique identifier of the primary advertised course run associated with
       the course.
   * - ``enrollment_url``
     - string
     - The enrollment url related to the course.

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
   * - ``key``
     - string
     - An identifier for the course run. For example, ``course-v1:RITx+PM9003x``.
   * - ``uuid``
     - string
     - The unique identifier for the course run. Example: ``0dbd8181-8866-47fc...``
   * - ``title``
     - string
     - The title of the content item. For example, "Introduction to Plasma Physics".
   * - ``external_key``
     - string
     - Content item unique identifying key external to the edX platform.
   * - ``image``
     - obj
     - The About page image for the course.
   * - ``short_description``
     - string
     - The short description of the content item and its content.
   * - ``marketing_url``
     - string
     - The URL for the course About page.
   * - ``seats``
     - array (obj)
     - List of seat records available for enrollment for the course run.
   * - ``start``
     - datetime
     - The start date for the content item.
   * - ``end``
     - datetime
     - The end date of the course run.
   * - ``go_live_date``
     - datetime
     - Datetime when the course run will go live
   * - ``enrollment_start``
     - datetime
     - The first date and time when this course run is open for learners to enroll.
       Learners cannot enroll before this date and time.
   * - ``enrollment_end``
     - datetime
     - The last date and time when this course run is open for learners to enroll.
       Learners cannot enroll after this date and time.
   * - ``weeks_to_complete``
     - integer
     - The number of weeks required to complete the content item.
   * - ``pacing_type``
     - enum string
     - The pacing of the course. May be ``self-paced`` or ``instructor-paced``.
   * - ``type``
     - enum string
     - Typing for the course. One of ``verified``, ``professional``, ``audit``.
   * - ``status``
     -  string
     -  String representation of the course run status. Example: ``published``
   * -  ``is_enrollable``
     - boolean
     - Whether the course run is currently enrollable.
   * - ``is_marketable``
     - boolean
     - Whether the course run is specified as marketable.
   * - ``availability``
     - enum string
     - One of ``Current``, ``Upcoming``.
   * - ``variant_id``
     - string
     -  The UUID for a product variant.
   * - ``course``
     - string
     - Course unique key associated with the course run. Example:
       ``HarvardX+FIH``
   * - ``full_description``
     - string
     - The long description of the course and its content.
   * - ``announcement``
     - datetime
     - Datetime when the most recent course run announcement was released.
   * - ``video``
     - obj
     - The course About video record.
   * - ``content_language``
     - string
     - Shortened representation of course run language. Example: ``en-us``
   * - ``license``
     - string
     - The license associated with the course run
   * - ``outcome``
     - string
     - HTML element for what learners will learn from the course.
   * - ``transcript_languages``
     - array (string)
     - The languages for which video transcripts are available.
   * - ``instructors``
     - array (obj)
     - Instructor users associated with the course run.
   * - ``staff``
     -  array (obj)
     - Staff users associated with the course run.
   * - ``min_effort``
     - integer
     - The minimum number of estimated hours of effort per week.
   * - ``max_effort``
     - integer
     - The maximum number of estimated hours of effort per week.
   * - ``modified``
     - datetime
     - Datetime string of the last time the content in the courserun was updated.
   * - ``level_type``
     - enum string
     - The course's level of difficulty. Can be one of ``high_school``,
       ``introductory``, ``intermediate``, or ``advanced``.
   * - ``mobile_available``
     - boolean
     - Whether the content item is available for mobile devices.
   * - ``hidden``
     - boolean
     - Whether the course run has been hidden by the authors or administrators.
   * - ``reporting_type``
     - string
     - Reporting type designated for the course. Example: ``mooc``.
   * - ``eligible_for_financial_aid``
     - bool
     - Whether the course run is eligible for financial aid to a learner.
   * - ``first_enrollable_paid_seat_price``
     - integer
     - Available seat price for enrollment in the course.
   * - ``has_ofac_restrictions``
     - boolean
     - Whether the course run has OFAC restrictions, i.e. geographical
       restrictions as to where the course run can be sold.
   * - ``ofac_comment``
     - string
     - Additional information on ofac restrictions relating to the course run.
   * - ``enrollment_count``
     - integer
     - Total number of learners who have enrolled in this course run.
   * - ``recent_enrollment_count``
     - integer
     - Total number of learners who have enrolled in this course run in the last 6
       months.
   * - ``expected_program_type``
     - obj
     - Designated program type record for the course run.
   * - ``expected_program_name``
     - string
     - Designated expected program name for the course run.
   * - ``course_uuid``
     - string
     - The UUID of the course object associated with the course run.
   * - ``estimated_hours``
     - float
     - Estimated number of hours it takes to complete the course.
   * - ``content_language_search_facet_name``
     - string
     - The language associated with the course run that is indexed for search
       throughout the platform.
   * - ``enterprise_subscription_inclusion``
     - boolean
     - Signifies whether the course run is included in the Enterprise Subscription catalog.
   * - ``programs``
     - array (obj)
     - An array of programs that the course run is associated with.
   * - ``enrollment_url``
     - string
     - The URL for the enrollment page.

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
   * - ``uuid``
     - string
     - The unique identifier for the program.
   * - ``title``
     - string
     - The title of the program. For example, "MicroMasters: Plasma
       Physics".
   * - ``subtitle``
     - string
     - A subtitle for the program.
   * - ``type``
     - enum string
     - The program type. One of ``Professional Certificate``, ``XSeries``,
       or ``MicroMasters``.
   * - ``type_attrs``
     - obj
     - The object representation of the type record associated with the
       program
   * - ``status``
     -  string
     -  String representation of the program status. Example: ``published``
   * - ``marketing_slug``
     - string
     - The slug used in the marketing URL related to the program.
   * - ``marketing_url``
     - string
     - The full url string related to the marketing URL for the program.
   * - ``banner_image``
     - obj
     - The banner image record relating to the program
   * - ``hidden``
     - boolean
     - Whether the program has been hidden by the authors or administrators.
   * - ``courses``
     - array (obj)
     - List of course records that are offered by the program.
   * - ``authoring_organizations``
     - array (obj)
     - List of organizations records responsible for authoring the courses
       within the program.
   * - ``card_image_url``
     - string
     - The URL of an image that represents the program.
   * - ``is_program_eligible_for_one_click_purchase``
     - boolean
     - Whether learners can purchase the program with a single click.
   * - ``degree``
     - obj
     - The degree record associated with the program.
   * - ``curricula``
     - array (obj)
     - Curricula items related to the program.
   * - ``marketing_hook``
     - string
     - Marketing hook written for the program.
   * - ``total_hours_of_effort``
     - integer
     - Total number of hours estimated to take in order to complete the
       program.
   * - ``recent_enrollment_count``
     - integer
     - Total number of learners who have enrolled in program in the last 6
       months.
   * - ``organization_short_code_override``
     - string
     - Organization short code overwritten string.
   * - ``organization_logo_override_url``
     - string
     - Organization logo url overwritten.
   * - ``primary_subject_override``
     - obj
     - Subject record override for the program.
   * - ``level_type_override``
     - obj
     - Level type record override for the program.
   * - ``language_override``
     - string
     - Language record override for the program.
   * - ``labels``
     - array (string)
     - List of labels for the courses in the program.
   * - ``taxi_form``
     - object
     - Represents the data needed for a single Taxi (2U form library) lead
       capture form.
   * - ``program_duration_override``
     - integer
     - Override value for the program duration.
   * - ``data_modified_timestamp``
     - datetime
     - The timestamp of the last time the program data was modified.
   * - ``excluded_from_search``
     - boolean
     - Whether or not the content is searchable by the various enterprise
       program search tools.
   * - ``excluded_from_seo``
     - boolean
     - Whether the program should be excluded from the edX SEO.
   * - ``has_ofac_restrictions``
     - boolean
     - Whether the program and program content has OFAC restrictions, i.e.
       geographical restrictions as to where the course run can be sold.
   * - ``ofac_comment``
     - string
     - Additional information on OFAC restrictions relating to the course run.
   * - ``overview``
     - string
     - Overview text surrounding the program.
   * - ``weeks_to_complete``
     - integer
     - The estimated number of weeks required to complete the program.
   * - ``weeks_to_complete_max``
     - integer
     - The maximum number of estimated weeks required to complete the program.
   * - ``weeks_to_complete_min``
     - integer
     - The minimum number of estimated weeks required to complete the
       program.
   * - ``min_hours_effort_per_week``
     - integer
     - The minimum number of estimated hours of effort per week.
   * - ``max_hours_effort_per_week``
     - integer
     - The maximum number of estimated hours of effort per week.
   * - ``video``
     - obj
     - The program About video record.
   * - ``expected_learning_items``
     - array (obj)
     - Elements of the course learning items records.
   * - ``faq``
     - array (string)
     - List of HTML representations of the course FAQ sections under the
       program.
   * - ``credit_backing_organizations``
     - array (obj)
     - List of organization records associated with the credit earned by the
       program.
   * - ``corporate_endorsements``
     - array (obj)
     - List of endorsement records associated with the program.
   * - ``job_outlook_items``
     - array (obj)
     - Job outlook records associated with the program.
   * - ``individual_endorsements``
     - array (obj)
     - List of endorsement records associated with the program.
   * - ``languages``
     - array (string)
     - List of languages used in the program.
   * - ``transcript_languages``
     - array (string)
     - List of languages used in the program's transcripts.
   * - ``subjects``
     - array (obj)
     - The academic subjects that the program covers.
   * - ``price_ranges``
     - array (integer)
     - Price ranges for the program.
   * - ``staff``
     - array (obj)
     - Staff users associated with the course run.
   * - ``credit_redemption_overview``
     - obj
     - Redemption overview record associated with the program.
   * - ``applicable_seat_types``
     - array (string)
     - Array of string representation of the different seat types offered
       by the program.
   * - ``instructor_ordering``
     - array (obj)
     - Ordered instructor records associated with the programs.
   * - ``enrollment_count``
     - integer
     - Total number of learners who have enrolled in this program.
   * - ``topics``
     - array (obj)
     - List of topic records related to the program.
   * - ``credit_value``
     - integer
     - The total credit value for the program.
   * - ``enterprise_subscription_inclusion``
     - bool
     - Whether the program is tagged to be included in the enterprise
       subscription package.
   * - ``geolocation``
     - obj
     - Geographic location for the course, if one exists.
   * - ``location_restriction``
     - obj
     - Course location restriction record.
   * - ``is_2u_degree_program``
     - boolean
     - Whether or not the program is a 2u degree program.
   * - ``in_year_value``
     - obj
     - Record related to projected value for a course.
   * - ``skill_names``
     - array (string)
     - List of skill names associated with the program.
   * - ``skills``
     - array (obj)
     - List of skill records associated with the program.
   * - ``product_source``
     - obj
     - Product source record associated with the program.
   * - ``subscription_eligible``
     - boolean
     - Whether the program is eligible for subscriptions.
   * - ``subscription_prices``
     - array (integer)
     - List of subscription prices for the program.
   * - ``enrollment_url``
     - string
     - The URL for the enrollment page.

===================================================
Example Response Showing Information about a Course
===================================================

The following example shows a single course. A catalog may contain many
courses.

.. code-block:: json

  {
    "key": "edx+tr1012",
    "uuid": "04d8eb8e-7773-42b3-97fc-a42f8266e1e5",
    "title": "Trench Run 10",
    "course_runs": [
      {
        "key": "course-v1:edx+tr1012+1T2021",
        "uuid": "293e187e-c1d7-42cf-85b7-760e98a6f02d",
        "title": "Trench Run 10",
        "external_key": "",
        "image": {
          "src": "https://stage-discovery.edx-cdn.org/media/course/image/04d8eb8e-7773-42b3-97fc-a42f8266e1e5-5daa73db36a3.small.png",
          "description": null,
          "height": null,
          "width": null
        },
        "short_description": "<p>t</p>",
        "marketing_url": "https://stage.edx.org/course/trench-run-10-course-v1edxtr10121t2021?utm_source=lms_catalog_service_user&utm_medium=affiliate_partner",
        "seats": [
          {
            "type": "audit",
            "price": "0.00",
            "currency": "USD",
            "upgrade_deadline": null,
            "upgrade_deadline_override": null,
            "credit_provider": null,
            "credit_hours": null,
            "sku": "4A19EC2",
            "bulk_sku": null
          },
          {
            "type": "verified",
            "price": "100.00",
            "currency": "USD",
            "upgrade_deadline": "2030-09-05T23:59:59Z",
            "upgrade_deadline_override": null,
            "credit_provider": null,
            "credit_hours": null,
            "sku": "DE707ED",
            "bulk_sku": "8BA9C3A"
          }
        ],
        "start": "2022-04-12T16:00:00Z",
        "end": "2090-09-15T16:00:00Z",
        "go_live_date": "2021-04-22T04:00:00Z",
        "enrollment_start": null,
        "enrollment_end": null,
        "weeks_to_complete": 3,
        "pacing_type": "instructor_paced",
        "type": "verified",
        "run_type": "946d043a-7b2c-414d-a106-8b7761e86eba",
        "status": "published",
        "is_enrollable": true,
        "is_marketable": true,
        "availability": "Current",
        "variant_id": null,
        "course": "edx+tr1012",
        "full_description": "<p>t</p>",
        "announcement": "2021-04-22T16:19:27.987040Z",
        "video": null,
        "content_language": "en-us",
        "license": "",
        "outcome": "<p>t</p>",
        "transcript_languages": [
          "en-us"
        ],
        "instructors": [],
        "staff": [
          {
            "uuid": "16a4422b-55f2-45eb-81da-ac1d0655d065",
            "salutation": null,
            "given_name": "New",
            "family_name": "Instructor1",
            "bio": "",
            "slug": "new-instructor1",
            "position": {
              "title": "Dr",
              "organization_name": "edX",
              "organization_id": 11,
              "organization_override": null,
              "organization_marketing_url": "https://stage.edx.org/school/edx",
              "organization_uuid": "4f8cb2c9-589b-4d1e-88c1-b01a02db3a9c",
              "organization_logo_image_url": "https://stage-discovery.edx-cdn.org/organization/logos/4f8cb2c9-589b-4d1e-88c1-b01a02db3a9c-086cef28bdf5.png"
            },
            "areas_of_expertise": [],
            "profile_image": {
              "medium": {
                "url": "https://stage-discovery.edx-cdn.org/media/people/profile_images/16a4422b-55f2-45eb-81da-ac1d0655d065.medium.png",
                "width": 110,
                "height": 110
              }
            },
            "works": [],
            "urls": {
              "facebook": "adding fb url",
              "twitter": null,
              "blog": null
            },
            "urls_detailed": [
              {
                "id": 9,
                "type": "facebook",
                "title": "",
                "display_title": "Facebook",
                "url": "adding fb url"
              }
            ],
            "email": null,
            "profile_image_url": "https://stage-discovery.edx-cdn.org/media/people/profile_images/16a4422b-55f2-45eb-81da-ac1d0655d065.png",
            "major_works": "",
            "published": false
          }
        ],
        "min_effort": 1,
        "max_effort": 2,
        "modified": "2024-01-12T16:45:17.436871Z",
        "level_type": "Introductory",
        "mobile_available": false,
        "hidden": false,
        "reporting_type": "mooc",
        "eligible_for_financial_aid": true,
        "first_enrollable_paid_seat_price": 100,
        "has_ofac_restrictions": false,
        "ofac_comment": "",
        "enrollment_count": 3,
        "recent_enrollment_count": 3,
        "expected_program_type": null,
        "expected_program_name": "",
        "course_uuid": "04d8eb8e-7773-42b3-97fc-a42f8266e1e5",
        "estimated_hours": 4.5,
        "content_language_search_facet_name": "English",
        "enterprise_subscription_inclusion": false,
        "enrollment_url": "https://courses.stage.edx.org/enterprise/40709edf-3748-4fcf-aa18-99abd765b692/course/course-v1:edx+tr1012+1T2021/enroll/?catalog=fcbb8cc6-85f5-427e-b154-4055fdd69472&utm_medium=enterprise&utm_source=dusenbery-devices"
      }
    ],
    "entitlements": [
      {
        "mode": "verified",
        "price": "100.00",
        "currency": "USD",
        "sku": "0E5F108",
        "expires": null
      }
    ],
    "owners": [
      {
        "uuid": "4f8cb2c9-589b-4d1e-88c1-b01a02db3a9c",
        "key": "edx",
        "name": "edX",
        "auto_generate_course_run_keys": false,
        "certificate_logo_image_url": "https://stage-discovery.edx-cdn.org/organization/certificate_logos/4f8cb2c9-589b-4d1e-88c1-b01a02db3a9c-80a7fb4abe88.png",
        "logo_image_url": "https://stage-discovery.edx-cdn.org/organization/logos/4f8cb2c9-589b-4d1e-88c1-b01a02db3a9c-086cef28bdf5.png",
        "organization_hex_color": null,
        "data_modified_timestamp": null,
        "description": "<p>EdX is a non-profit created by founding partners Harvard and MIT. We're bringing the best of higher education to students around the world. EdX offers MOOCs and interactive online classes in subjects including law, history, science, engineering, business, social sciences, computer science, public health, and artificial intelligence (AI).</p>",
        "description_es": "",
        "homepage_url": null,
        "tags": [
          "charter"
        ],
        "marketing_url": "https://stage.edx.org/school/edx",
        "slug": "edx",
        "banner_image_url": "https://stage-discovery.edx-cdn.org/organization/banner_images/4f8cb2c9-589b-4d1e-88c1-b01a02db3a9c-86aa2499c053.png",
        "enterprise_subscription_inclusion": false
      }
    ],
    "image": {
      "src": "https://stage-discovery.edx-cdn.org/media/course/image/04d8eb8e-7773-42b3-97fc-a42f8266e1e5-5daa73db36a3.small.png",
      "description": null,
      "height": null,
      "width": null
    },
    "short_description": "<p>t</p>",
    "type": "69b8a063-e5fb-4a91-96d6-e50c8335c5da",
    "url_slug": "trench-run-10",
    "course_type": "verified-audit",
    "enterprise_subscription_inclusion": false,
    "excluded_from_seo": false,
    "excluded_from_search": false,
    "full_description": "<p>t</p>",
    "level_type": "Introductory",
    "subjects": [
      {
        "name": "Social Sciences",
        "subtitle": "<p>Learn about the social sciences and more from the best universities and institutions around the world.</p>",
        "description": "<p>Enroll in free online courses in the social sciences including sociology, political science, human geography, demography and more. Learn about the science of happiness or the history and effect of social programs. Courses are available from major universities worldwide.</p>",
        "banner_image_url": "https://stage.edx.org/sites/default/files/social-sciences-1440x210.jpg",
        "card_image_url": "https://stage.edx.org/sites/default/files/subject/image/card/social-sciences.jpg",
        "slug": "social-sciences",
        "uuid": "eefb009b-0a02-49e9-b1b1-249982b6ce86"
      }
    ],
    "prerequisites": [],
    "prerequisites_raw": null,
    "expected_learning_items": [],
    "video": null,
    "sponsors": [],
    "modified": "2024-01-12T16:45:17.341223Z",
    "marketing_url": "https://stage.edx.org/course/trench-run-10?utm_source=lms_catalog_service_user&utm_medium=affiliate_partner",
    "syllabus_raw": null,
    "outcome": "<p>t</p>",
    "original_image": {
      "src": "https://stage-discovery.edx-cdn.org/media/course/image/04d8eb8e-7773-42b3-97fc-a42f8266e1e5-5daa73db36a3.png",
      "description": null,
      "height": null,
      "width": null
    },
    "card_image_url": null,
    "canonical_course_run_key": "course-v1:edx+tr1012+1T2021",
    "extra_description": null,
    "additional_information": null,
    "additional_metadata": null,
    "faq": null,
    "learner_testimonials": null,
    "enrollment_count": 3,
    "recent_enrollment_count": 3,
    "topics": [],
    "key_for_reruns": "",
    "url_slug_history": [
      "trench-run-10",
      "trench-run-10-course-v1edxtr10121t2021",
      "learn/social-sciences/edx-trench-run-10"
    ],
    "url_redirects": [],
    "course_run_statuses": [
      "published"
    ],
    "editors": [],
    "collaborators": [],
    "skill_names": [],
    "skills": [],
    "organization_short_code_override": "",
    "organization_logo_override_url": null,
    "geolocation": null,
    "location_restriction": null,
    "in_year_value": null,
    "product_source": {
      "name": "edX",
      "slug": "edx",
      "description": "Open courses"
    },
    "data_modified_timestamp": "2023-11-21T21:09:56.175672Z",
    "watchers": [],
    "programs": [],
    "course_run_keys": [
      "course-v1:edx+tr1012+1T2021"
    ],
    "editable": true,
    "advertised_course_run_uuid": "293e187e-c1d7-42cf-85b7-760e98a6f02d",
    "enrollment_url": "https://courses.stage.edx.org/enterprise/40709edf-3748-4fcf-aa18-99abd765b692/course/edx+tr1012/enroll/?catalog=fcbb8cc6-85f5-427e-b154-4055fdd69472&utm_medium=enterprise&utm_source=dusenbery-devices"
  }

====================================================
Example Response Showing Information about a Program
====================================================

The following example response shows a single program. A catalog may
contain many programs.

.. code-block:: json

  {
    "uuid": "fcfe93c3-9123-4a58-a190-8614c96b8eab",
    "title": "Master of Business Administration",
    "subtitle": "",
    "type": "Masters",
    "type_attrs": {
      "uuid": "1399475e-cca8-4676-a669-fe5ba477c73f",
      "slug": "masters",
      "coaching_supported": false
    },
    "status": "unpublished",
    "marketing_slug": "ucd-master-of-business-administration",
    "marketing_url": "https://stage.edx.org/masters/ucd-master-of-business-administration",
    "banner_image": {},
    "hidden": false,
    "courses": [],
    "authoring_organizations": [
      {
        "uuid": "2c17b012-432f-4182-a914-bee8baea4f2a",
        "key": "UCDavis",
        "name": "University of California, Davis",
        "auto_generate_course_run_keys": true,
        "certificate_logo_image_url": null,
        "logo_image_url": null,
        "organization_hex_color": null,
        "data_modified_timestamp": null,
        "description": "",
        "description_es": "",
        "homepage_url": null,
        "tags": [],
        "marketing_url": "https://stage.edx.org/school/ucdavis",
        "slug": "ucdavis",
        "banner_image_url": null,
        "enterprise_subscription_inclusion": false
      }
    ],
    "card_image_url": "https://stage-discovery.edx-cdn.org/media/programs/card_images/fcfe93c3-9123-4a58-a190-8614c96b8eab-6ec5c946a62b.png",
    "is_program_eligible_for_one_click_purchase": true,
    "degree": {
      "application_requirements": "TBD",
      "apply_url": "",
      "banner_border_color": "",
      "campus_image": null,
      "title_background_image": null,
      "costs": [],
      "deadlines": [],
      "lead_capture_list_name": "Master_default",
      "quick_facts": [],
      "overall_ranking": "",
      "prerequisite_coursework": "TBD",
      "rankings": [],
      "lead_capture_image": {},
      "micromasters_path": null,
      "micromasters_url": null,
      "micromasters_long_title": null,
      "micromasters_long_description": null,
      "micromasters_background_image": {},
      "micromasters_org_name_override": null,
      "costs_fine_print": null,
      "deadlines_fine_print": null,
      "hubspot_lead_capture_form_id": null,
      "additional_metadata": {
        "external_identifier": "65390275-9b17-4dda-bcf0-d24250bf0a00",
        "external_url": "https://onlinemba.ucdavis.edu/requestinfo/plp/?lsrc=edx&utm_source=edx&utm_medium=referral&utm_campaign=ucd-mba",
        "organic_url": "https://onlinemba.ucdavis.edu/?utm_source=edx&utm_medium=referral&utm_campaign=UCD_MBA"
      },
      "specializations": [
        "Business Analytics",
        "Finance",
        "Marketing Strategy and Analytics",
        "Strategic Management",
        "Organizational Leadership",
        "Technology Management",
        "Entrepreneurship",
        "Product Management",
        "Business"
      ],
      "program_duration_override": null,
      "display_on_org_page": false,
      "excluded_from_search": false,
      "excluded_from_seo": false
    },
    "curricula": [
      {
        "uuid": "8ef7ba75-0b2f-434e-ab55-8f3436c6471f",
        "name": "",
        "marketing_text": "<ul><li>Markets and the Firm</li><li>Business Taxation</li><li>Financial Accounting</li><li>Individual and Group Dynamics</li><li>Negotiations in Organizations</li><li>Data Analysis for Managers (was Statistics)</li><li>Marketing Management</li><li>Financial Theory and Policy</li><li>Integrated Management Project (Capstone)</li><li>Organizational Strategy and Structure</li></ul>",
        "marketing_text_brief": null,
        "is_active": true,
        "courses": [],
        "programs": []
      }
    ],
    "marketing_hook": "",
    "total_hours_of_effort": null,
    "recent_enrollment_count": 0,
    "organization_short_code_override": "University of California, Davis",
    "organization_logo_override_url": null,
    "primary_subject_override": {
      "name": "Business & Management",
      "subtitle": "<p>Learn about business and management and more from the best universities and institutions around the world.</p>",
      "description": "<p>Online courses cover the core concepts in all areas of business including entrepreneurship, economics, finance, marketing and product development. Learn about business contracts, supply chain management, statistical analysis and much more with online courses from Harvard, MIT, Cornell and other top universities.</p>\n<h3>Browse Popular Business and Management Subjects</h3>\n<p><a href=\"/course/subject/business-management/finance\">Finance</a> | <a href=\"/course/subject/business-management/marketing\">Marketing</a> | <a href=\"/course/subject/business-management/accounting\">Accounting</a> | <a href=\"/course/subject/business-management/communications\">Communications</a> | <a href=\"/course/subject/business-management/international-business\">International Business</a> | <a href=\"/course/subject/business-management/risk-management\">Risk Management</a></p>\n<p><a href=\"/course/subject/business-management/innovation-entrepreneurship\">Innovation &amp; Entrepreneurship</a></p>",
      "banner_image_url": "https://stage.edx.org/sites/default/files/business-and-management-1440x210.jpg",
      "card_image_url": "https://stage.edx.org/sites/default/files/subject/image/card/business.jpg",
      "slug": "business-management",
      "uuid": "409d43f7-ff36-4834-9c28-252132347d87"
    },
    "level_type_override": {
      "name": "Intermediate",
      "sort_value": 3
    },
    "language_override": "en-us",
    "labels": [],
    "taxi_form": null,
    "program_duration_override": null,
    "data_modified_timestamp": "2023-05-23T12:13:31.380214Z",
    "excluded_from_search": false,
    "excluded_from_seo": false,
    "has_ofac_restrictions": null,
    "ofac_comment": "",
    "overview": "The online MBA from the University of California, Davis, features the same curriculum and globally recognized faculty as the on-campus MBA program. You'll experience our culture of collaboration and make Silicon Valley connections. The program can be completed in as few as 24 months. Bachelor’s required     \n",
    "weeks_to_complete": null,
    "weeks_to_complete_min": null,
    "weeks_to_complete_max": null,
    "min_hours_effort_per_week": null,
    "max_hours_effort_per_week": null,
    "video": null,
    "expected_learning_items": [],
    "faq": [],
    "credit_backing_organizations": [],
    "corporate_endorsements": [],
    "job_outlook_items": [],
    "individual_endorsements": [],
    "languages": [],
    "transcript_languages": [],
    "subjects": [],
    "price_ranges": [],
    "staff": [],
    "credit_redemption_overview": null,
    "applicable_seat_types": [
      "credit",
      "verified"
    ],
    "instructor_ordering": [],
    "enrollment_count": 0,
    "topics": [],
    "credit_value": 0,
    "enterprise_subscription_inclusion": false,
    "geolocation": null,
    "location_restriction": null,
    "is_2u_degree_program": true,
    "in_year_value": null,
    "skill_names": [],
    "skills": [],
    "product_source": {
      "name": "2u",
      "slug": "2u",
      "description": "2U, Trilogy, Getsmarter -- external source for 2u courses and programs"
    },
    "subscription_eligible": null,
    "subscription_prices": [],
    "enrollment_url": "https://courses.stage.edx.org/enterprise/943b1234-58cf-4376-b8e0-0efcbf4bfdf9/program/fcfe93c3-9123-4a58-a190-8614c96b8eab/enroll/?catalog=9014df44-e8eb-41c0-ab39-fb9a508ac716&utm_medium=enterprise&utm_source=pied-piper"
  }

=======================================================
Example Response Showing Information about a Course Run
=======================================================

The following example response shows a single course run. A catalog may
contain many course runs.

.. code-block:: json

  {
    "key": "course-v1:HarvardX+FIH+3T2023",
    "uuid": "359e8f1c-627e-421b-9c5c-5e8560455219",
    "title": "Harvard VPAL FinTech online short course",
    "external_key": null,
    "image": {
      "src": "https://stage-discovery.edx-cdn.org/media/course/image/b718b44e-ac0e-4371-921a-bc7d02ea5a4a-a6e1b555a479.small.jpg",
      "description": null,
      "height": null,
      "width": null
    },
    "short_description": "<p>Step beyond current FinTech disruption and prepare for future financial services priorities.</p>",
    "marketing_url": "https://stage.edx.org/course/harvard-vpal-fintech-online-short-course-course-v1-harvardx-fih-3t2023?utm_source=lms_catalog_service_user&utm_medium=affiliate_partner",
    "seats": [
      {
        "type": "unpaid-executive-education",
        "price": "0.00",
        "currency": "USD",
        "upgrade_deadline": null,
        "upgrade_deadline_override": null,
        "credit_provider": null,
        "credit_hours": null,
        "sku": "C33ACD3",
        "bulk_sku": null
      }
    ],
    "start": "2023-11-09T00:00:00Z",
    "end": "2023-12-18T23:59:59Z",
    "go_live_date": "2023-12-15T00:00:00Z",
    "enrollment_start": null,
    "enrollment_end": "2024-02-07T23:59:59Z",
    "weeks_to_complete": 6,
    "pacing_type": "instructor_paced",
    "type": null,
    "run_type": "6fb73168-371b-419e-8f33-b30619497164",
    "status": "published",
    "is_enrollable": true,
    "is_marketable": true,
    "availability": "Current",
    "variant_id": "73b264ba-d49b-4012-93d1-ddc97553e9ab",
    "course": "HarvardX+FIH",
    "full_description": "<p>A practical sustainability action plan to overcome the barriers and aid in seizing the opportunities associated with creating a sustainable businessAs awareness of climate change, resource scarcity, pollution, and social inequality rises, businesses and governments are being held increasingly responsible. There is a need for positive, sustainable change. By taking this Business Sustainability Management online short course you’ll become that change, and set yourself up for success.</p>",
    "announcement": "2023-12-18T19:15:13.218663Z",
    "video": null,
    "content_language": "en-us",
    "license": "",
    "outcome": "<p>Al finalizar este curso, obtendrá lo siguiente:Claridad en la especulación y el despliegue del panorama de tecnología financiera, y las habilidades y el conocimiento para abordar las iniciativas de innovación. Comprensión de las tecnologías que dan forma al futuro de las finanzas y el potencial de asociaciones entre empresas establecidas, empresas tecnológicas de la nueva era e inversionistas. La capacidad de evaluar críticamente el futuro de la tecnología financiera y pensar estratégica y creativamente sobre los problemas que enfrentan las compañías reales. La oportunidad de establecer contactos con una cohorte de profesionales de ideas afines en una semana de conferencias adicional. Un certificado de primer nivel de la VPAL de Harvard, en asociación con HarvardX, como validación de sus conocimientos de tecnología financiera.</p>",
    "transcript_languages": [
      "en-us"
    ],
    "instructors": [],
    "staff": [],
    "min_effort": 2,
    "max_effort": 3,
    "modified": "2023-12-18T19:29:52.582607Z",
    "level_type": "Introductory",
    "mobile_available": false,
    "hidden": false,
    "reporting_type": "mooc",
    "eligible_for_financial_aid": true,
    "first_enrollable_paid_seat_price": null,
    "has_ofac_restrictions": false,
    "ofac_comment": "",
    "enrollment_count": 0,
    "recent_enrollment_count": 0,
    "expected_program_type": null,
    "expected_program_name": "",
    "course_uuid": "b718b44e-ac0e-4371-921a-bc7d02ea5a4a",
    "estimated_hours": 15,
    "content_language_search_facet_name": "English",
    "enterprise_subscription_inclusion": false,
    "programs": [],
    "enrollment_url": "https://courses.stage.edx.org/enterprise/4a3d7eae-fbf9-4786-b648-f7565289aeb7/course/course-v1:HarvardX+FIH+3T2023/enroll/?catalog=1236fd56-ede6-487f-8335-eb9fca8f0ad1&utm_medium=enterprise&utm_source=stripe-co"
  }


.. _learner_summary Endpoint:

************************
learner-summary Endpoint
************************

GET calls to the ``learner-summary`` endpoint get information about learners'
course enrollments and progress. The response data is by default sorted on the basis of ``last_activity_date``. The data
can be sorted on other fields available in response by passing it in query_param as ``?ordering=field_name``.

===================
Method and Endpoint
===================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - Endpoint
   * - GET
     - ``/enterprise/v3/enterprise-customer/{enterprise_uuid}/learner-summary``

=====================
Example Request
=====================
::

   curl -X GET
     https://api.edx.org/enterprise/v3/enterprise-customer/{{enterprise_uuid}}/learner-summary \
     -H "Authorization: JWT {access token}"
     -H "Content-Type: application/json" \
    }]"

=====================
Response Values
=====================

The
``GET /enterprise/v3/enterprise-customer/{enterprise_uuid}/learner-summary``
request returns the following data.

.. list-table::
   :widths: 25 20 80
   :header-rows: 1

   * - Field
     - Data Type
     - Description
   * - ``is_consent_granted``
     - boolean
     - Whether the learner has granted consent for edX to share information about their course enrollment and progress with the enterprise.
   * - ``amount_learner_paid``
     - decimal
     - The amount the learner paid towards the enrollment, if any.
   * - ``contract_id``
     - string
     - A unique identifier for the contract that this enrollment is associated with.
   * - ``coupon_code``
     - string
     - The enrollment code string used by the learner to enroll in their course. (Not applicable for Subscriptions or Offers).
   * - ``coupon_name``
     - string
     - The name of the enrollment code batch used by the learner to enroll in their course. (Not applicable for Subscriptions or Offers).
   * - ``course_api_url``
     - string
     - The complete url for the course when using the edX API Retrieve Course Metadata endpoint.
   * - ``course_duration``
     - integer
     - The duration in weeks, for instructor-paced courses, or the expected duration for self-paced courses.
   * - ``course_end``
     - date
     - The date the course ends, in YYYY-MM-DD format. This is the last date on which learners can submit answers or assessments, or otherwise be credited with completion of a course subsection.
   * - ``course_key``
     - string
     - The unique identifier for the overall course.
   * - ``course_list_price``
     - decimal
     -  The original price of the course, before any discount were applied.
   * - ``course_max_effort``
     - integer
     - The estimated maximum effort required by the course, in hours per week.
   * - ``course_min_effort``
     - integer
     - The estimated minimum effort required by the course, in hours per week.
   * - ``course_pacing_type``
     - string
     - Whether the course is self-paced or instructor-paced.
   * - ``course_primary_program``
     - string
     - The primary program a course belongs to. (Not applicable to courses that aren't part of a program).
   * - ``course_primary_subject``
     - string
     - The subject category this course falls under when searching on edX.org.
   * - ``course_start``
     - date
     - The date when the course begins, in YYYY-MM-DD format. This is the date when course content is available for learners to interact with. In most cases, learners can enroll in the course before the ``course_start`` date.
   * - ``course_title``
     - string
     - The title of the edX course.
   * - ``courserun_key``
     - string
     - The unique identifier for the individual courserun.
   * - ``created``
     - timestamp
     - The date and time the learner progress report was last updated.
   * - ``current_grade``
     - decimal
     - The learner's current grade, which will update as the learner proceeds through the course.
   * - ``enrollment_date``
     - date
     - The date, YYYY-MM-DD, the learner enrolled in the course.
   * - ``enrollment_id``
     - integer
     - A unique identifier for this enrollment.
   * - ``enterprise_customer_uuid``
     - string
     - The enterprise account ID assigned by edX.
   * - ``enterprise_enrollment_id``
     - integer
     - A unique identifier for this enrollment, specific to enterprise enrollments.
   * - ``enterprise_name``
     - string
     - The enterprise account name.
   * - ``enterprise_sso_uid``
     - string
     - The learner’s user ID in the enterprise’s Identity Provider. (Only applicable for customers using Single Sign On).
   * - ``enterprise_user_id``
     - integer
     - The learner’s ID assigned by edX.
   * - ``has_passed``
     - boolean
     - Whether or not the learner has passed this course.
   * - ``is_consent_granted``
     - boolean
     - Whether the learner has granted consent for edX to share information about their course enrollment and progress with the enterprise.
   * - ``is_refunded``
     - boolean
     - Whether or not the learner received a refund on their enrollment.
   * - ``last_activity_date``
     - date
     - The most recent date, YYYY-MM-DD,the learner was active in an edX.
   * - ``letter_grade``
     - string
     - The learner's letter grade, if they have passed the course.
   * - ``offer_name``
     - string
     - The offer ID used by the learner to enroll in their course. (Not applicable for Subscriptions or Codes).
   * - ``offer_type``
     - string
     - The offer type and discount percentage used by the learner to enroll in their course. (Not applicable for Subscriptions or Codes).
   * - ``paid_by``
     - string
     - Whether the enrollment was paid for by the enterprise, the learner, or a third party.
   * - ``passed_date``
     - date
     - The date, YYYY-MM-DD, the learner passed the course.
   * - ``progress_status``
     - string
     - Whether the learner is still working on the course, has passed, or has failed.  Possible values are: Failed, In Progress, Passed.
   * - ``seat_delivery_method``
     - string
     - The type of subsidy used by the learner to enroll in their course.
   * - ``unenrollment_date``
     - date
     - The date,YYYY-MM-DD, the learner unenrolled from the course.
   * - ``unenrollment_end_within_date``
     - date
     - The date ,YYYY-MM-DD, the learner must unenroll by, in order to receive a refund on the enrollment. This date is traditionally 14 days from the enrollment date or the course start date, whichever is later.
   * - ``user_account_creation_date``
     - timestamp
     - The date and time when the learner’s account was created in the edx.org LMS.
   * - ``user_country``
     - string
     - A two-letter country code.
   * - ``user_current_enrollment_mode``
     - string
     - The learner’s current enrollment mode in the course.
   * - ``user_email``
     - string
     - The learner’s email address.
   * - ``user_username``
     - string
     - The learner’s username on edx.org.
