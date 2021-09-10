.. _Discovery API Reference:

###########################
EdX Discovery API Reference
###########################

This API reference includes information about the endpoints of the edX
Discovery API, including the request, response data, and examples. You can use
any technology to send REST API requests as HTTP messages to the edX API. The
example API requests shown in this reference use the ``curl`` command-line program
to show the syntax and data for a request in a way that is easy to read. To view all
these endpoints hosted by Discovery service go to ``/api-docs/``

******************
Taxonomy Endpoints
******************

The following endpoints are available in Taxonomy application under the Discovery API.

* **/skills**
    The ``skills`` are extracted using course's full description by third party tools
    and services. Skills are linked with courses to help learners choose their courses
    for their desired skills. You can make GET calls to the ``/skills`` endpoint to get
    all the skills available in the system. See :ref:`skills_list Endpoint` for more details.


* **/skills/{skill_id}**
    You can make GET calls to the ``/skills/{skill_id}``
    endpoint to get details for a specified skill. For details, see
    :ref:`skills_detailed Endpoint`.


* **/jobs**
    We also collect and save the data about `jobs` that are related to
    `skills`. We extract this information using third party tools and services.
    Jobs are linked with the skills to help learners align their career plans
    with their course work. You can make GET calls to the ``/jobs`` endpoint
    to get all the jobs. See, :ref:`jobs_list Endpoint` for more details.

* **/jobs/{job_id}**
    You can make GET calls to the ``/jobs/{job_id}`` endpoint to get details of
    a specified job. For details, see :ref:`jobs_detailed Endpoint`.

* **/jobpostings**
    JobPostings contains the number of job postings with posting companies and
    median salary information. You can make GET calls to
    the ``/jobpostings`` endpoint to get all the job postings
    available in the system. See :ref:`jobpostings_list Endpoint` for more details.

* **/jobpostings/{jobpostings_id}**
    You can make GET calls to the ``/jobpostings/{jobpostings_id}`` endpoint to get
    details of a specified JobPostings object. For details,
    see :ref:`jobpostings_detailed Endpoint`.



==================================
Taxonomy Endpoints Response layout
==================================

Responses to GET requests for the edX Discovery API frequently contain
the ``results`` response value. The ``results`` response value is a variable
that represents the intended object from the GET request. Here are the details.


.. list-table::
   :widths: 25 20 80
   :header-rows: 1

   * - Field
     - Data Type
     - Description
   * - ``count``
     - integer
     - The number of objects in the system.
   * - ``next``
     - string
     - The URL for the next page of results.
   * - ``previous``
     - string
     - The URL for the previous page of results.
   * - ``results``
     - array
     - A list of objects of relative data.

For example in :ref:`skills_list Endpoint` Each top-level object in the ``results`` array represents a skill.
See :ref:`skills<skills Fields>` for information about the fields in a skill item in the ``results``.


.. _skills_list Endpoint:

********************
Skills List Endpoint
********************

GET call to the ``/skills`` endpoint returns a list of all the available skills in the system.

===================
Method and Endpoint
===================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - Endpoint
   * - GET
     - ``/taxonomy/api/v1/skills/``


===============
Example Request
===============
::

   curl -X GET \
   https://discovery.edx.org/taxonomy/api/v1/skills/ \
   -H "Authorization: JWT {access token}"

==========
Parameters
==========

You can use an optional ``page_size`` parameter to specify the number of
records you want to load in a single page. If not provided the default of
20 is used for `page_size`. For example:

::


   curl -X GET \
   https://discovery.edx.org/taxonomy/api/v1/skills/?page_size=10 \
   -H "Authorization: JWT {access token}"


.. _skills_detailed Endpoint:

**************************
skills/{skill_id} Endpoint
**************************

GET call to the ``skills/{skill_id}`` endpoint returns information about a single skill.
In the GET call, The information returned is described in
:ref:`Skill Fields <skills Fields>`.

===================
Method and Endpoint
===================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - Endpoint
   * - GET
     - ``/taxonomy/api/v1/skills/{skill_id}``

===============
Example Request
===============
::

   curl -X GET \
   https://discovery.edx.org/taxonomy/api/v1/skills/14 \
   -H "Authorization: JWT {access token}"


===============
Response Values
===============

The ``GET https://discovery.edx.org/taxonomy/api/v1/skills/{skill_id}``
request returns the response values described in :ref:`Skill Fields <skills Fields>`.

.. _skills Fields:

=================
Fields in a Skill
=================


.. list-table::
   :widths: 25 20 80
   :header-rows: 1

   * - Field
     - Data Type
     - Description
   * - ``id``
     - integer
     - Unique identifier in edx system. It is Used to get detailed views.
   * - ``name``
     - string
     - Skill title
   * - ``description``
     - string
     - Skill short description
   * - ``courses``
     - array
     - A list of all the courses relevant to the skill.
   * - ``course_key``
     - string
     - Course unique identifier in edx system. Example: "TUMx+QPLS4x".
   * - ``confidence``
     - float
     - Represents the relevance the skill to course. It's value ranges from 0 to 1.
   * - ``created``
     - string
     - object creation time. Example: "2021-02-23T11:01:08.164127Z".
   * - ``modified``
     - string
     - object modified time. Example: "2021-02-23T11:01:08.164127Z".
   * - ``external_id``
     - string
     - An identifier for the skill in the source system. Example: "KS122LN6CLX3P61KWSP2".
   * - ``info_url``
     - string
     - URL to get more details for skill from the source.
   * - ``type_id``
     - string
     - Skill type id, Example: "ST1"
   * - ``type_name``
     - string
     - Skill type name, Example: "Hard Skill"


======================================================
Example Response Showing Information about skills list
======================================================

The following example response shows a skills list response for 3 page_size.

::

      {
      "count": 3522,
      "next": "https://discovery.edx.org/taxonomy/api/v1/skills/?page=2&page_size=3",
      "previous": null,
      "results": [
        {
          "id": 124,
          "courses": [
            {
              "course_key": "TUMx+QPLS4x",
              "confidence": 1
            },
            {
              "course_key": "BerkeleyX+BUSADM466.3x",
              "confidence": 1
            },
            {
              "course_key": "TUMx+QEMx",
              "confidence": 1
            },
            {
              "course_key": "IIMBx+MK102x",
              "confidence": 1
            },
            {
              "course_key": "KyotoUx+008x",
              "confidence": 1
            },
            {
              "course_key": "LinuxFoundationX+LFS163x",
              "confidence": 1
            },
            {
              "course_key": "QueensX+QBUS502x",
              "confidence": 1
            },
            {
              "course_key": "QueensX+QBUS503x",
              "confidence": 1
            },
            {
              "course_key": "TecdeMonterreyX+DCRx",
              "confidence": 1
            },
            {
              "course_key": "logycaX+ECLLM002",
              "confidence": 1
            }
          ],
          "created": "2021-02-23T11:01:08.164127Z",
          "modified": "2021-04-21T07:09:24.779053Z",
          "external_id": "KS122LN6CLX3P61KWSP2",
          "name": "Customer Satisfaction",
          "description": "Customer satisfaction is a term frequently used in marketing. It is a measure of how products and services supplied by a company meet or surpass customer expectation. Customer satisfaction is defined as \"the number of customers, or percentage of total customers, whose reported experience with a firm, its products, or its services (ratings) exceeds specified satisfaction goals.\" Customers play an important role and are essential in keeping a product or service relevant so it is in the best interest of the business to ensure customer satisfaction, and build customer loyalty.",
          "info_url": "https://skills.emsidata.com/skills/KS122LN6CLX3P61KWSP2",
          "type_id": "ST1",
          "type_name": "Hard Skill"
        },
        {
          "id": 125,
          "courses": [
            {
              "course_key": "TUMx+QPLS4x",
              "confidence": 1
            }
          ],
          "created": "2021-02-23T11:01:08.229934Z",
          "modified": "2021-04-21T07:09:24.812122Z",
          "external_id": "KS127CR6S5TQJVYMG3HB",
          "name": "Operational Excellence",
          "description": "Operational excellence of an organization is the execution of its operations in an excellent way. Given two commercial companies with the same strategy, the operationally more excellent company will in general have better operational results, creating value for customers and shareholders. The term can be explained and applied in many ways, and is popular with management.",
          "info_url": "https://skills.emsidata.com/skills/KS127CR6S5TQJVYMG3HB",
          "type_id": "ST1",
          "type_name": "Hard Skill"
        },
        {
          "id": 126,
          "courses": [
            {
              "course_key": "TUMx+QPLS4x",
              "confidence": 1
            },
            {
              "course_key": "UC3Mx+IM.1x",
              "confidence": 1
            },
            {
              "course_key": "USMx+CC607x",
              "confidence": 1
            },
            {
              "course_key": "Microsoft+DAT227x",
              "confidence": 1
            },
            {
              "course_key": "USMx+BUMM621",
              "confidence": 1
            },
            {
              "course_key": "WitsX+DTx",
              "confidence": 1
            },
            {
              "course_key": "USMx+DIGITAL01",
              "confidence": 1
            },
            {
              "course_key": "UTAustin_BUx+LDSCTx",
              "confidence": 1
            },
            {
              "course_key": "State-Bank-of-India+SBIIT002x",
              "confidence": 1
            }
          ],
          "created": "2021-02-23T11:01:08.277514Z",
          "modified": "2021-04-21T07:09:24.844532Z",
          "external_id": "KS1218Y74WJ6YV4KH0DM",
          "name": "Business Process",
          "description": "A business process, business method or business function is a collection of related, structured activities or tasks by people or equipment in which a specific sequence produces a service or product for a particular customer or customers. Business processes occur at all organizational levels and may or may not be visible to the customers. A business process may often be visualized (modeled) as a flowchart of a sequence of activities with interleaving decision points or as a process matrix of a sequence of activities with relevance rules based on data in the process. The benefits of using business processes include improved customer satisfaction and improved agility for reacting to rapid market change. Process-oriented organizations break down the barriers of structural departments and try to avoid functional silos.",
          "info_url": "https://skills.emsidata.com/skills/KS1218Y74WJ6YV4KH0DM",
          "type_id": "ST1",
          "type_name": "Hard Skill"
        }
      ]
    }


.. _jobs_list Endpoint:

******************
Jobs List Endpoint
******************

GET call to ``/jobs`` endpoint returns a list of all the available jobs in the system.

===================
Method and Endpoint
===================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - Endpoint
   * - GET
     - ``/taxonomy/api/v1/jobs/``


===============
Example Request
===============
::

   curl -X GET \
   https://discovery.edx.org/taxonomy/api/v1/jobs/ \
   -H "Authorization: JWT {access token}"

==========
Parameters
==========

You can use an optional ``page_size`` parameter to specify the number of
records you want to load in a single page. If not provided the default of
20 is used for `page_size`. For example:

::


   curl -X GET \
   https://discovery.edx.org/taxonomy/api/v1/jobs/?page_size=10 \
   -H "Authorization: JWT {access token}"


.. _jobs_detailed Endpoint:

**********************
jobs/{job_id} Endpoint
**********************

GET call to the ``jobs/{job_id}``
endpoint returns information about a single job.
In the GET call, The information returned is described in
:ref:`Jobs Fields <jobs Fields>`.

===================
Method and Endpoint
===================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - Endpoint
   * - GET
     - ``/taxonomy/api/v1/jobs/{job_id}``

===============
Example Request
===============
::

   curl -X GET \
   https://discovery.edx.org/taxonomy/api/v1/jobs/14 \
   -H "Authorization: JWT {access token}"


===============
Response Values
===============

The ``GET https://discovery.edx.org/taxonomy/api/v1/jobs/{jobs}``
request returns the response values described in :ref:`Jobs Fields <jobs Fields>`.

.. _jobs Fields:

===============
Fields in a Job
===============


.. list-table::
   :widths: 25 20 80
   :header-rows: 1

   * - Field
     - Data Type
     - Description
   * - ``id``
     - integer
     - Unique identifier in edx system. It is Used to get detailed views.
   * - ``name``
     - string
     - Job title
   * - ``skills``
     - array
     - A list of all the skills relevant to the job. see :ref:`Skills Fields <Skills Fields>` for skill details.
   * - ``unique_postings``
     - integer
     - Number of unique posting for the job for the particular skill.
   * - ``significance``
     - float
     - Represents the significance of the skill to job. It's value ranges from 0 to 100.
   * - ``created``
     - string
     - object creation time. Example: "2021-02-23T11:01:08.164127Z".
   * - ``modified``
     - string
     - object modified time. Example: "2021-02-23T11:01:08.164127Z".
   * - ``external_id``
     - string
     - An identifier for the job in the source system. Example: "ETB716DA673BC8BE08".


======================================================
Example Response Showing Information about Job details
======================================================

The following example response shows a job detail response.

::

    {
      "id": 101,
      "skills": [
        {
          "skill": {
            "id": 167,
            "created": "2021-02-26T16:37:21.922596Z",
            "modified": "2021-03-15T14:28:41.168869Z",
            "external_id": "KS120HM73ZTBQQFJZY52",
            "name": "Annuities",
            "description": "An annuity is a series of payments made at equal intervals. Examples of annuities are regular deposits to a savings account, monthly home mortgage payments, monthly insurance payments and pension payments. Annuities can be classified by the frequency of payment dates. The payments (deposits) may be made weekly, monthly, quarterly, yearly, or at any other regular interval of time. Annuities may be calculated by mathematical functions known as \"annuity functions\".",
            "info_url": "https://skills.emsidata.com/skills/KS120HM73ZTBQQFJZY52",
            "type_id": "ST1",
            "type_name": "Hard Skill"
          },
          "significance": 166.0414834976898,
          "unique_postings": 2986
        },
        {
          "skill": {
            "id": 181,
            "created": "2021-02-26T16:49:37.542590Z",
            "modified": "2021-03-15T14:28:31.605044Z",
            "external_id": "KS680DR6QC1G86H8NYBK",
            "name": "Securities (Finance)",
            "description": "A security is a tradable financial asset. The term commonly refers to any form of financial instrument, but its legal definition varies by jurisdiction. In some countries and languages people commonly use the term \"security\" to refer to any form of financial instrument, even though the underlying legal and regulatory regime may not have such a broad definition. In some jurisdictions the term specifically excludes financial instruments other than equities and fixed-income instruments. In some jurisdictions it includes some instruments that are close to equities and fixed income, e.g., equity warrants.",
            "info_url": "https://skills.emsidata.com/skills/KS680DR6QC1G86H8NYBK",
            "type_id": "ST1",
            "type_name": "Hard Skill"
          },
          "significance": 119.89026886137088,
          "unique_postings": 2987
        },
        {
          "skill": {
            "id": 159,
            "created": "2021-02-26T16:28:23.211533Z",
            "modified": "2021-03-23T17:18:20.511619Z",
            "external_id": "KS123Y170CZM0V5Z3XXB",
            "name": "Financial Services",
            "description": "",
            "info_url": "https://skills.emsidata.com/skills/KS123Y170CZM0V5Z3XXB",
            "type_id": "ST1",
            "type_name": "Hard Skill"
          },
          "significance": 52.45900298889593,
          "unique_postings": 5237
        },
        {
          "skill": {
            "id": 3446,
            "created": "2021-03-11T22:09:18.464621Z",
            "modified": "2021-03-15T14:27:46.046679Z",
            "external_id": "KS123YS74NRDCKYXNS7Z",
            "name": "Financial Industry Regulatory Authorities",
            "description": "",
            "info_url": "https://skills.emsidata.com/skills/KS123YS74NRDCKYXNS7Z",
            "type_id": "ST1",
            "type_name": "Hard Skill"
          },
          "significance": 12.739547451804325,
          "unique_postings": 619
        },
        {
          "skill": {
            "id": 2334,
            "created": "2021-03-11T22:04:18.375199Z",
            "modified": "2021-03-15T14:22:53.139528Z",
            "external_id": "KS44253607FYTYCJNMPZ",
            "name": "Workplace Diversity",
            "description": "",
            "info_url": "https://skills.emsidata.com/skills/KS44253607FYTYCJNMPZ",
            "type_id": "ST1",
            "type_name": "Hard Skill"
          },
          "significance": 8.049648490659921,
          "unique_postings": 229
        },
        {
          "skill": {
            "id": 183,
            "created": "2021-02-26T16:49:37.629231Z",
            "modified": "2021-08-03T06:20:03.927297Z",
            "external_id": "KS121CX75Q8F638ZCJVZ",
            "name": "Investments",
            "description": "To invest is to allocate money in the expectation of some benefit in the future.",
            "info_url": "https://skills.emsidata.com/skills/KS121CX75Q8F638ZCJVZ",
            "type_id": "ST1",
            "type_name": "Hard Skill"
          },
          "significance": 6.686575375167631,
          "unique_postings": 1361
        }
      ],
      "created": "2021-03-01T00:04:39.398313Z",
      "modified": "2021-03-16T00:04:44.054473Z",
      "external_id": "ETB716DA673BC8BE08",
      "name": "Financial Services Representative"
    }


.. _jobpostings_list Endpoint:

*************************
JobPostings List Endpoint
*************************

GET call to the ``/jobpostings`` endpoint returns a list of all the available JobPostings in the system.

===================
Method and Endpoint
===================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - Endpoint
   * - GET
     - ``/taxonomy/api/v1/jobpostings/``


===============
Example Request
===============
::

   curl -X GET \
   https://discovery.edx.org/taxonomy/api/v1/jobpostings/ \
   -H "Authorization: JWT {access token}"

==========
Parameters
==========

You can use an optional ``page_size`` parameter to specify the number of
records you want to load in a single page. If not provided the default of
20 is used for `page_size`. For example:

::


   curl -X GET \
   https://discovery.edx.org/taxonomy/api/v1/jobpostings/?page_size=10 \
   -H "Authorization: JWT {access token}"


.. _jobpostings_detailed Endpoint:

*************************************
jobpostings/{jobpostings_id} Endpoint
*************************************

GET call to the ``jobpostings/{jobpostings_id}``
endpoint returns information about a single JobPostings object.
In the GET call, The information returned is described in
:ref:`JobPostings Fields <JobPostings fields>`.

===================
Method and Endpoint
===================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - Endpoint
   * - GET
     - ``/taxonomy/api/v1/jobpostings/{jobpostings_id}``

===============
Example Request
===============
::

   curl -X GET \
   https://discovery.edx.org/taxonomy/api/v1/jobpostings/14 \
   -H "Authorization: JWT {access token}"


===============
Response Values
===============

The ``GET https://discovery.edx.org/taxonomy/api/v1/jobpostings/{jobpostings_id}``
request returns the response values described in :ref:`JobPostings Fields <JobPostings Fields>`.

.. _JobPostings Fields:

==============================
Fields in a JobPostings Object
==============================


.. list-table::
   :widths: 25 20 80
   :header-rows: 1

   * - Field
     - Data Type
     - Description
   * - ``id``
     - integer
     - Unique identifier in edx system. It is Used to get detailed views.
   * - ``job``
     - object
     - The related job object. see :ref:`Jobs Fields <Jobs Fields>` for job details.
   * - ``median_salary``
     - integer
     - Median Salary for the post.
   * - ``median_posting_duration``
     - integer
     - Median posting duration for the post.
   * - ``unique_postings``
     - integer
     - Number of unique posting for the job.
   * - ``unique_companies``
     - integer
     - Number of unique companies offering the post.
   * - ``created``
     - string
     - object creation time. Example: "2021-02-23T11:01:08.164127Z".
   * - ``modified``
     - string
     - object modified time. Example: "2021-02-23T11:01:08.164127Z".


======================================================
Example Response Showing Information about JobPostings
======================================================

The following example response shows a JobPostings List response.

::

    {
      "count": 216,
      "next": "https://discovery.edx.org/taxonomy/api/v1/jobpostings/?page=6&page_size=3",
      "previous": "https://discovery.edx.org/taxonomy/api/v1/jobpostings/?page=4&page_size=3",
      "results": [
        {
          "id": 63,
          "job": {
            "id": 39,
            "created": "2021-03-01T00:04:36.457661Z",
            "modified": "2021-03-16T00:04:43.507558Z",
            "external_id": "ETD8659FB16C6E7A79",
            "name": "Team Member"
          },
          "created": "2021-03-10T00:04:50.051149Z",
          "modified": "2021-08-25T00:01:44.399651Z",
          "median_salary": 26048,
          "median_posting_duration": 41,
          "unique_postings": 85538,
          "unique_companies": 3368
        },
        {
          "id": 64,
          "job": {
            "id": 17,
            "created": "2021-03-01T00:04:35.263889Z",
            "modified": "2021-03-16T00:04:42.418874Z",
            "external_id": "ET32340120BB9E6B7C",
            "name": "Assistant Manager"
          },
          "created": "2021-03-10T00:04:50.066938Z",
          "modified": "2021-08-25T00:01:44.420155Z",
          "median_salary": 34496,
          "median_posting_duration": 39,
          "unique_postings": 85159,
          "unique_companies": 4068
        },
        {
          "id": 65,
          "job": {
            "id": 42,
            "created": "2021-03-01T00:04:36.613092Z",
            "modified": "2021-03-16T00:04:42.155163Z",
            "external_id": "ET6659D06425508C0D",
            "name": "Maintenance Technician"
          },
          "created": "2021-03-10T00:04:50.083016Z",
          "modified": "2021-08-25T00:01:44.356245Z",
          "median_salary": 41664,
          "median_posting_duration": 34,
          "unique_postings": 91321,
          "unique_companies": 10701
        }
      ]
    }
