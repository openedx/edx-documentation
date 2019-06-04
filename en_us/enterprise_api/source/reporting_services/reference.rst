.. _Reporting Services Reference:

#####################################
EdX Reporting Services Reference
#####################################

This reference contains detailed information about edX Enterprise Reporting Services,
including the xAPI (Experience API) reporting channel.


**********************
xAPI Reporting Channel
**********************

xAPI (experience API) allows content providers to report user experience analytics back to the client.
xAPI can be used to track learner events starting from course enrollment through course completion.

Here is the list of events currently reported via the edX xAPI reporting channel.

#. Learner registered (enrolled) in a course.
    * Learner info (e.g. lms_user_id, username, user_email, country_code etc.)
    * Course info (e.g. course_id, course_title, course_description etc.)
#. Learner completed a course.
    * Learner info  (e.g. lms_user_id, username, user_email, country_code etc.)
    * Course info (e.g. course_id, course_title, course_description etc.)
    * Learner grades for course completion (grade, pass/fail status etc.)

The following information is required in order to broadcast xAPI events from edX to a
client's LRS (Learning Record Store):

#. Learning Record Store (LRS) Endpoint URL (e.g. `https://cloud.scorm.com/lrs/E2OS62MR52/`)
#. Learning Record Store Client ID/Key (e.g. `8m_eBxqax4UhTUbSlaM`)
#. Learning Record Store Client Secret (e.g. `DIEYXmwJnyZPem5h7iY`)


******************************
xAPI Event Delivery Mechanism:
******************************

The edX xAPI Event Delivery Mechanism currently transmits events in batches on a daily basis.
Each event is transmitted separately. Information contained within each xAPI event depends on the type
of event being transmitted.

***************************************
Sample Payload Data for edX xAPI Events
***************************************

Sample data for xAPI events sent to a client Learning Record Store is as follows:

Learner registered (enrolled) in a course.
------------------------------------------
Following is the payload data in JSON format that is sent to the xAPI LRS whenever an
enterprise learner enrolls in a course.

.. code-block:: json

    {
        "id": "d0df8e65-f9ae-4c72-951e-7ae25cc69157",
        "actor": {
            "objectType": "Agent",
            "mbox": "mailto:staff@example.com",
            "name": "staff"
        },
        "verb": {
            "id": "http://adlnet.gov/expapi/verbs/registered",
            "display": {
                "en-US": "registered"
            }
        },
        "context": {
            "extensions": {
                "http://id.tincanapi.com/extension/course-details": {
                    "course_id": "course-v1:edX+DemoX+Demo_Course",
                    "course_title": "edX Demonstration Course",
                    "course_description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry",
                    "course_duration": "50 weeks 4 days."
                },
                "http://id.tincanapi.com/extension/user-details": {
                    "lms_user_id": 5,
                    "user_username": "staff",
                    "user_email": "staff@example.com",
                    "user_country_code": "US",
                    "user_account_creation_date": "2017-05-04T01:30:28Z",
                    "enterprise_user_id": 444
                }
            }
        },
        "timestamp": "2018-08-15T09:18:31.066Z",
        "stored": "2018-08-15T09:18:31.066Z",
        "authority": {
            "account": {
                "homePage": "http://cloud.scorm.com",
                "name": "8m_eBxqax4UhTUbSlaM"
            },
            "objectType": "Agent",
            "name": "Test Account"
        },
        "version": "1.0.1",
        "object": {
            "id": "http://adlnet.gov/expapi/activities/course",
            "definition": {
                "name": {
                    "en-US": "edX Demonstration Course"
                },
                "description": {
                    "en-US": "Lorem Ipsum is simply dummy text of the printing and typesetting industry"
                }
            },
            "objectType": "Activity"
        }
    }


Learner completed a course.
---------------------------
Following is the payload data in JSON format that is sent to the xAPI LRS whenever an
enterprise learner completes a course.

.. code-block:: json

    {
        "id": "90cd19fd-73aa-475d-82ba-117c7ea04756",
        "actor": {
            "objectType": "Agent",
            "mbox": "mailto:staff@example.com",
            "name": "staff"
        },
        "verb": {
            "id": "http://adlnet.gov/expapi/verbs/completed",
            "display": {
                "en-US": "completed"
            }
        },
        "result": {
            "score": {
                "scaled": 0.4,
                "raw": 40,
                "min": 0,
                "max": 100
            },
            "success": true,
            "completion": true
        },
        "context": {
            "extensions": {
                "http://id.tincanapi.com/extension/course-details": {
                    "course_id": "course-v1:edX+DemoX+Demo_Course",
                    "course_title": "edX Demonstration Course",
                    "course_description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
                    "course_duration": "50 weeks 4 days."
                },
                "http://id.tincanapi.com/extension/user-details": {
                    "lms_user_id": 5,
                    "user_username": "staff",
                    "user_email": "staff@example.com",
                    "user_country_code": "US",
                    "user_account_creation_date": "2017-05-04T01:30:28Z",
                    "enterprise_user_id": 444
                }
            }
        },
        "timestamp": "2018-08-15T11:22:52.113Z",
        "stored": "2018-08-15T11:22:52.113Z",
        "authority": {
            "account": {
                "homePage": "http://cloud.scorm.com",
                "name": "8m_eBxqax4UhTUbSlaM"
            },
            "objectType": "Agent",
            "name": "Test Account"
        },
        "version": "1.0.1",
        "object": {
            "id": "http://adlnet.gov/expapi/activities/course",
            "definition": {
                "name": {
                    "en-US": "edX Demonstration Course"
                },
                "description": {
                    "en-US": "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
                }
            },
            "objectType": "Activity"
        }
    }
