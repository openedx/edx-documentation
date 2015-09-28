.. _Tracking Logs:

############################################
Events in the Tracking Logs
############################################

This section provides reference information about the event data that is
delivered in data packages. Events are emitted by the server, the browser, or
the mobile device to capture information about interactions with the courseware
and the Instructor Dashboard in the LMS, and are stored in JSON documents. In
the data package, event data is delivered in a log file.

.. contents:: 
  :local:
  :depth: 1

The student and course team events are grouped into categories in this section.
For a complete, alphabetical list of events, see the :ref:`event_list`.

.. _sample_events:

*************************
Reviewing a Sample Event
*************************

A sample event from an edX.log file follows. This sample was edited to remove
personally identifiable information. Events are stored in JSON documents, which
can be difficult to read before standard formatting is applied.

.. code-block:: json

    {"agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) 
    Chrome/30.0.1599.101 Safari/537.36", "context": {"course_id": "edx/AN101/2014_T1", 
    "module": {"display_name": "Multiple Choice Questions"}, "org_id": "edx", "user_id": 
    9999999}, "event": {"answers": {"i4x-edx-AN101-problem-a0effb954cca4759994f1ac9e9434bf4_2_1": 
    "yellow", "i4x-edx-AN101-problem-a0effb954cca4759994f1ac9e9434bf4_4_1": ["choice_0", "choice_2"]}, 
    "attempts": 1, "correct_map": {"i4x-edx-AN101-problem-a0effb954cca4759994f1ac9e9434bf4_2_1": 
    {"correctness": "incorrect", "hint": "", "hintmode": null, "msg": "", "npoints": null, 
    "queuestate": null}, "i4x-edx-AN101-problem-a0effb954cca4759994f1ac9e9434bf4_4_1": 
    {"correctness": "correct", "hint": "", "hintmode": null, "msg": "", "npoints": null, 
    "queuestate": null}}, "grade": 2, "max_grade": 3, "problem_id": "i4x://edx/AN101/problem/
    a0effb954cca4759994f1ac9e9434bf4", "state": {"correct_map": {}, "done": null, "input_state": 
    {"i4x-edx-AN101-problem-a0effb954cca4759994f1ac9e9434bf4_2_1": {}, "i4x-edx-AN101-problem-
    a0effb954cca4759994f1ac9e9434bf4_4_1": {}}, "seed": 1, "student_answers": {}}, "submission": 
    {"i4x-edx-AN101-problem-a0effb954cca4759994f1ac9e9434bf4_2_1": {"answer": "yellow", "correct": 
    false, "input_type": "optioninput", "question": "What color is the open ocean on a sunny day?", 
    "response_type": "optionresponse", "variant": ""}, "i4x-edx-AN101-problem-
    a0effb954cca4759994f1ac9e9434bf4_4_1": {"answer": ["a piano", "a guitar"], "correct": true, 
    "input_type": "checkboxgroup", "question": "Which of the following are musical instruments?", 
    "response_type": "choiceresponse", "variant": ""}}, "success": "incorrect"}, "event_source": 
    "server", "event_type": "problem_check", "host": "precise64", "referer": "http:\/\/localhost:8001\/
    container\/i4x:\/\/edX\/DemoX\/vertical\/69dedd38233a46fc89e4d7b5e8da1bf4?action=new", 
    "accept_language": "en-US,en;q=0.8","ip": "NN.N.N.N", "page": "x_module", 
    "time": 2014-03-03T16:19:05.584523+00:00", "username": "AAAAAAAAAA"}

If you use a JSON formatter to "pretty print" this event, a version that is
more readable is produced.

.. code-block:: json

 {
    "agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36", 
    "context": {
        "course_id": "edx/AN101/2014_T1", 
        "module": {
            "display_name": "Multiple Choice Questions"
        }, 
        "org_id": "edx", 
        "user_id": 9999999
    }, 
    "event": {
        "answers": {
            "i4x-edx-AN101-problem-a0effb954cca4759994f1ac9e9434bf4_2_1": "yellow", 
            "i4x-edx-AN101-problem-a0effb954cca4759994f1ac9e9434bf4_4_1": [
                "choice_0", 
                "choice_2"
            ]
        }, 
        "attempts": 1, 
        "correct_map": {
            "i4x-edx-AN101-problem-a0effb954cca4759994f1ac9e9434bf4_2_1": {
                "correctness": "incorrect", 
                "hint": "", 
                "hintmode": null, 
                "msg": "", 
                "npoints": null, 
                "queuestate": null
            }, 
            "i4x-edx-AN101-problem-a0effb954cca4759994f1ac9e9434bf4_4_1": {
                "correctness": "correct", 
                "hint": "", 
                "hintmode": null, 
                "msg": "", 
                "npoints": null, 
                "queuestate": null
            }
        }, 
        "grade": 2, 
        "max_grade": 3, 
        "problem_id": "i4x://edx/AN101/problem/a0effb954cca4759994f1ac9e9434bf4", 
        "state": {
            "correct_map": {}, 
            "done": null, 
            "input_state": {
                "i4x-edx-AN101-problem-a0effb954cca4759994f1ac9e9434bf4_2_1": {}, 
                "i4x-edx-AN101-problem-a0effb954cca4759994f1ac9e9434bf4_4_1": {}
            }, 
            "seed": 1, 
            "student_answers": {}
        }, 
        "submission": {
            "i4x-edx-AN101-problem-a0effb954cca4759994f1ac9e9434bf4_2_1": {
                "answer": "yellow", 
                "correct": false, 
                "input_type": "optioninput", 
                "question": "What color is the open ocean on a sunny day?", 
                "response_type": "optionresponse", 
                "variant": ""
            },
            "i4x-edx-AN101-problem-a0effb954cca4759994f1ac9e9434bf4_4_1": {
                "answer": [
                    "a piano", 
                    "a guitar"
                ], 
                "correct": true, 
                "input_type": "checkboxgroup", 
                "question": "Which of the following are musical instruments?", 
                "response_type": "choiceresponse", 
                "variant": ""
            }
        }, 
        "success": "incorrect"
    }, 
    "event_source": "server", 
    "event_type": "problem_check", 
    "host": "precise64", 
    "referer": "http:\/\/localhost:8001\/container\/i4x:\/\/edX\/DemoX\/vertical\/69dedd38233a46fc89e4d7b5e8da1bf4?action=new",
    "accept_language": "en-US,en;q=0.8",
    "ip": "NN.N.N.N", 
    "page": "x_module", 
    "time": "2014-03-03T16:19:05.584523+00:00", 
    "username": "AAAAAAAAAA"
 }

For more information about fields that are included in every event, see
:ref:`common`. For more information about this ``problem_check`` event and
other types of events, see :ref:`Student_Event_Types` or
:ref:`Instructor_Event_Types`.

.. _common:

*****************************
Common Fields
*****************************

This section describes the JSON fields that are common to the schema
definitions of all events. These fields are at the root level of the event
JSON documents.

This section presents the common fields in alphabetical order. Actual events
in your data package can include these fields in different sequences.

===========================
``accept_language`` Field
===========================

**Type:** string

**Details:** The value from the HTTP Accept-Language request-header field. For
more information, see the HTTP/1.1 header field definition for 
`Accept-Language`_.

**History:** Added 23 Feb 2015.

=====================
``agent`` Field
=====================

**Type:** string

**Details:** Browser agent string of the user who triggered the event. 

.. _context:

===================
``context`` Field
===================

**Type:** dictionary

**Details:** 

The ``context`` field includes member fields that provide contextual
information. 

* This field contains a core set of member fields that are common to all events.
* For certain events with additional contextual requirements, this field
  contains a set of additional member fields that are common to those events
  only.
* For any event, this field can also include one or more additional member
  fields. For more information about the ``context`` member fields for an
  event, see the description of that event later in this section.

``context`` Member Fields Common to All Events 
***********************************************

The following member fields are present in the ``context`` field for all events. 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - ``context`` Member Field
     - Type
     - Details
   * - ``course_id``
     - string
     - Identifies the course that generated the event.
   * - ``org_id``
     - string
     - The organization that lists the course.
   * - ``path``
     - string
     - The URL that generated the event. 
   * - ``user_id``
     - integer
     - Identifies the individual who is performing the action.


``context`` Member Fields for Applicable Events
******************************************************

When applicable for an event, the ``context`` field also includes these member
fields to provide additional information.

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - ``context`` Member Field
     - Type
     - Details
   * - ``course_user_tags``
     - dictionary
     - Contains the key(s) and value(s) from the ``user_api_usercoursetag``
       table for the user. See :ref:`user_api_usercoursetag`.
   * - ``module``
     - dictionary
     - Contains a dictionary that identifies the components involved in a
       server event.

       For example, in a server ``problem_check`` event, the ``module`` field
       indicates the problem component that the server checked successfully.
       The member fields of this dictionary are ``display_name`` and
       ``usage_key``.

       For modules that are used in a course to present content from a
       library, this dictionary also includes the ``original_usage_key`` and
       ``original_usage_version`` fields. These member fields provide a
       consistent way to identify components that are sourced from a library,
       and can be used to identify the source library.


The ``context`` member fields are blank if values cannot be determined. 

**History**: ``usage_key`` added 28 Jan 2015. ``path`` added 07 May 2014.
``course_user_tags`` added 12 Mar 2014. ``user_id`` added 6 Nov 2013. Other
event fields may duplicate this data. Added 23 Oct 2013.

===================
``event`` Field
===================

**Type:** dictionary

**Details:** This field includes member fields that identify specifics of each
triggered event. Different member fields are supplied for different events.
For more information about the ``event`` member fields for an event, see the
description of that event later in this section.

========================
``event_source`` Field
========================

**Type:** string

**Details:** Specifies the source of the interaction that triggered the event.
The values in this field are:

* 'browser'
* 'mobile'
* 'server'
* 'task'

**History**: Updated 16 Oct 2014 to identify events emitted from mobile
devices.

=====================
``event_type`` Field
=====================

**Type:** string

**Details:** The type of event triggered. Values depend on ``event_source``.

:ref:`Student_Event_Types` and :ref:`Instructor_Event_Types` later in this 
section provide descriptions of each type of event that is included in 
data packages. To locate information about a specific event type, see the
:ref:`event_list`.

===================
``host`` Field
===================

**Type:** string

**Details:** The site visited by the user, for example, ``courses.edx.org``.

===================
``ip`` Field
===================

**Type:** string

**Details:** IP address of the user who triggered the event. Empty for events
that originate on mobile devices.

===================
``name`` Field
===================

**Type:** string

**Details:** Identifies the type of event triggered.

**History:** Server and mobile events added beginning on 07 May 2014 include a
``name`` field. When this field is present for an event, it supersedes the
``event_type`` field.

===================
``page`` Field
===================

**Type:** string

**Details:** The '$URL' of the page the user was visiting when the event was
emitted. 

For video events that originate on mobile devices, identifies the URL for the
video component.

===================
``referer`` Field
===================

**Type:** string

**Details:** The URI from the HTTP Referer request-header field. For more
information, see the HTTP/1.1 header field definition for `Referer`_.

**History:** Added 23 Feb 2015.

===================
``session`` Field
===================

**Type:** string

**Details:** This 32-character value is a key that identifies the user's
session. All browser events and the server :ref:`enrollment<enrollment>` events
include a value for the session. Other server events and mobile events do not
include a session value.

===================
``time`` Field
===================

**Type:** string

**Details:** Gives the UTC time at which the event was emitted in 
'YYYY-MM-DDThh:mm:ss.xxxxxx' format.

===================
``username`` Field
===================

**Type:** string

**Details:** The username of the user who caused the event to be emitted. This
string is empty for anonymous events, such as when the user is not logged in.

.. _Student_Event_Types:

****************************************
Student Events
****************************************

This section lists the events that are typically initiated by learners. These
events are generated by interactions with the learning management system (LMS)
other than the Instructor Dashboard.

.. contents::  
  :local:
  :depth: 1


The descriptions that follow include what each event represents, the system
component it originates from, the history of any changes made to the event
over time, and any additional member fields that the common ``context`` or
``event`` fields contain. For more information about the common ``context`` or
``event`` fields, see :ref:`common`.

The value in the ``event_source`` field (see the :ref:`common` section above)
distinguishes between events that originate in the browser (in JavaScript) and
events that originate on the server (during the processing of a request).

.. _enrollment:

=========================
Enrollment Events
=========================

This section includes descriptions of the following events. 

* ``edx.course.enrollment.activated`` 
* ``edx.course.enrollment.deactivated``
* ``edx.course.enrollment.mode_changed``
* ``edx.course.enrollment.upgrade.clicked``
* ``edx.course.enrollment.upgrade.succeeded``

``edx.course.enrollment.activated`` and ``edx.course.enrollment.deactivated``
*****************************************************************************

The server emits these events in response to course enrollment
activities completed by a student.

* When a student enrolls in a course, the server emits an
  ``edx.course.enrollment.activated`` event. For example, when a student
  clicks **Enroll** for a course on the edx.org site, the server emits this
  event.

* When a student unenrolls from a course, the server emits an
  ``edx.course.enrollment.deactivated`` event. For example, when a student
  clicks **Unenroll** for a course on the edx.org site, the server emits this
  event.

In addition, actions by course team members also generate
enrollment events. For the actions that members of the course team complete
that result in these events, see :ref:`instructor_enrollment`.

**Event Source**: Server

**History**: These enrollment events were added on 03 Dec 2013. On 07 May
2014, the ``name`` field was added. These enrollment events include both a
``name`` field and an ``event_type`` field.

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``course_id``
     - string
     - The course in which the student was enrolled or unenrolled. 
       
       If an external tool is used to enroll or unenroll students, this field
       contains a value and the ``context.course_id`` field is null.

   * - ``mode``
     - string
     - 'audit', 'honor', 'professional', 'verified'. Identifies the student's
       enrollment mode.
   * - ``user_id``
     - integer
     - Identifies the student who was enrolled or unenrolled. 

Example
*******

.. code-block:: json

    {
        "username": "AAAAAAAAAA",
        "event_source": "server",
        "name": "edx.course.enrollment.deactivated",
        "referer": "http:\/\/localhost:8001\/container\/i4x:\/\/edX\/DemoX\/vertical\/69dedd38233a46fc89e4d7b5e8da1bf4?action=new",
        "accept_language": "en-US,en;q=0.8",
        "time": "2014-01-26T00:28:28.388782+00:00", 
        "agent": "Mozilla\/5.0 (Windows NT 6.1; WOW64; Trident\/7.0; rv:11.0) like Gecko",
        "page": null
        "host": "courses.edx.org",
        "session": "a14j3ifhskngw0gfgn230g",
        "context": {
          "user_id": 9999999,
          "org_id": "edX",
          "course_id": "edX\/DemoX\/Demo_Course",
          "path": "\/change_enrollment",
        },
        "ip": "NN.NN.NNN.NNN",
        "event": {
          "course_id": "edX\/DemoX\/Demo_Course",
          "user_id": 9999999,
          "mode": "honor"
        },
        "event_type": "edx.course.enrollment.deactivated"
      }

``edx.course.enrollment.mode_changed``
**************************************

The server emits an ``edx.course.enrollment.mode_changed`` event when the
process of changing a student's ``student_courseenrollment.mode`` to a
different mode is complete.

**Event Source**: Server

**History**: Added 21 Aug 2014.

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``course_id``
     - string
     - The course in which the student's enrollment mode has changed. 
   * - ``mode``
     - string
     - 'audit', 'honor', 'professional', verified'. Identifies the student's
       new enrollment mode.
   * - ``user_id``
     - integer
     - Identifies the student whose enrollment mode changed. 

``edx.course.enrollment.upgrade.clicked``
*****************************************

Students who enroll with a ``student_courseenrollment.mode`` of 'audit' or
'honor' in a course that has a verified certificate option see a **Challenge
Yourself** link for the course on their dashboards. The browser emits this
event when a student clicks this option, and the process of upgrading the
``student_courseenrollment.mode`` for the student to 'verified' begins. See
:ref:`student_courseenrollment`.

**Event Source**: Browser

**History**: Added 18 Dec 2013.

``context`` **Member Fields**: 

In addition to the :ref:`common<context>` ``context`` member fields, this
event type also includes the following ``context`` member field.

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details and Member Fields
   * - ``mode``
     - string
     - Enrollment mode when the user clicked **Challenge Yourself**: 'audit' or
       'honor'.

``event`` **Member Fields**: None.

``edx.course.enrollment.upgrade.succeeded``
*******************************************

The server emits this event when the process of upgrading a student's
``student_courseenrollment.mode`` from 'audit' or 'honor' to 'verified' is
complete.

**Event Source**: Server

**History**: Added 18 Dec 2013.

``context`` **Member Fields**: 

In addition to the :ref:`common<context>` ``context`` member fields, this
event type also includes the following ``context`` member field.

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details and Member Fields
   * - ``mode``
     - string
     - Set to 'verified'.

``event`` **Member Fields**: None.

.. _navigational:

==============================
Navigational Events 
==============================

This section includes descriptions of the following events. 

* ``page_close``
* ``seq_goto``
* ``seq_next``
* ``seq_prev``

``page_close``
**************

The ``page_close`` event originates from within the JavaScript Logger itself.

**Component**: JavaScript Logger

**Event Source**: Browser

``event`` **Member Fields**: None


``seq_goto``, ``seq_next``, and ``seq_prev``
********************************************

The browser emits these events when a user selects a navigational control. 

* ``seq_goto`` is emitted when a user jumps between units in a sequence. 

* ``seq_next`` is emitted when a user navigates to the next unit in a sequence.

* ``seq_prev`` is emitted when a user navigates to the previous unit in a
  sequence.

**Component**: Sequence 

**Event Source**: Browser

``event`` **Member Fields**: 

All of these navigational events have the same ``event`` member fields.

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``id``
     - integer
     - The edX ID of the sequence. 
   * - ``new``
     - integer
     - For ``seq_goto``, the index of the unit being jumped to. 
       
       For ``seq_next`` and ``seq_prev``, the index of the unit being navigated
       to.

   * - ``old``
     - integer
     - For ``seq_goto``, the index of the unit being jumped from. 
       
       For ``seq_next`` and ``seq_prev``, the index of the unit being navigated
       away from.


.. _video:

==================================
Video Interaction Events
==================================

This section includes descriptions of the following events. Due to a naming
convention change, many of these events have two identifying names. In this
list, the original name, which is present in the ``event_type`` field for all
events, is followed by a newer, revised name. The revised name is present in
the ``name`` field only for events that have an ``event_source`` of 'mobile'.

* ``hide_transcript``/``edx.video.transcript.hidden``
* ``load_video``/``edx.video.loaded``
* ``pause_video``/``edx.video.paused``
* ``play_video``/``edx.video.played``
* ``seek_video``/``edx.video.position.changed``
* ``show_transcript``/``edx.video.transcript.shown``
* ``speed_change_video`` 
* ``stop_video``/``edx.video.stopped``
* ``video_hide_cc_menu``
* ``video_show_cc_menu``

A browser or the edX mobile app emits video interaction events when a user
interacts with a video.

* When users use a browser to stream video files on a desktop computer or
  mobile device, the browser emits the events.

* When users use the edX mobile app to stream or download course videos for
  offline viewing, the mobile app emits the events.

  When a user interacts with a downloaded video file offline using the edX
  mobile app, note that the app can only forward its events during the next
  connection opportunity. As a result, the date and time in the event's
  ``time`` field can be different from the date and time in its
  ``context.received_at`` field. Data packages can include events emitted on
  past dates.

This section presents the video interaction events alphabetically. Typically,
an interaction with the video player begins with a :ref:`play_video` event. 

For courses that include a pre-roll video, user interactions with the pre-roll
video result in different events. For more information, see :ref:`pre-roll`.

**Component**: Video

**History**: The edX mobile app for iOS began to emit a subset of the video
events on 25 Feb 2015. The edX mobile app for Android began to emit a subset
of the video events on 23 Dec 2014.


``hide_transcript``/``edx.video.transcript.hidden``
***************************************************

When a user selects **CC** to suppress display of the video transcript, the
browser or mobile app emits a ``hide_transcript`` event.

In addition to the identifying ``event_type`` of ``hide_transcript``, events
that the edX mobile app emits also include a ``name`` field with a value of
``edx.video.transcript.hidden``.

**Event Source**: Browser or Mobile

**History**: Updated 25 Feb 2015 to include events emitted by the edX mobile
app for iOS. Updated 23 Dec 2014 to include events emitted by the edX mobile
app for Android.

``context`` **Member Fields**: 

Only video interaction events with an ``event_source`` of 'mobile' include
additional ``context`` member fields in addition to the :ref:`common<context>`
member fields. The same set of additional context fields are added for
``hide_transcript``/ ``edx.video.transcript.hidden`` events as for the
:ref:`play_video` events. For an example of an event with these fields, see
:ref:`Example Mobile App Event`.

``event`` **Member Fields**: 

The ``hide_transcript``/``edx.video.transcript.hidden`` events include the
following ``event`` member fields. These fields serve the same purpose for
events of this type as for the :ref:`play_video` events.

* ``code``
* ``currentTime``: The point in the video file at which the transcript was
  hidden.
* ``id``

``load_video``/``edx.video.loaded``
***********************************

When the video is fully rendered and ready to play, the browser or mobile app
emits a ``load_video`` event.

In addition to the identifying ``event_type`` of ``load_video``, the events
that the edX mobile app emits also include a ``name`` field with a value of
``edx.video.loaded``.

**Event Source**: Browser or Mobile

**History**: Updated 25 Feb 2015 to include events emitted by the edX mobile
app for iOS. Updated 23 Dec 2014 to include events emitted by the edX mobile
app for Android.

``context`` **Member Fields**: 

Only video interaction events with an ``event_source`` of 'mobile' include
additional ``context`` member fields in addition to the :ref:`common<context>`
member fields. The same set of additional context fields are added for
``load_video`` events as for :ref:`play_video`. For an example of an event
with these fields, see
:ref:`Example Mobile App Event`.

``event`` **Member Fields**: 

The ``load_video``/ ``edx.video.loaded`` events include the following ``event``
member fields. These fields serve the same purpose for events of this type as
for the :ref:`play_video` events.

* ``code``
* ``id``

``pause_video``/``edx.video.paused``
*************************************

When a user selects the video player's **pause** control, the player emits a
``pause_video`` event. For videos that are streamed in a browser, when the
player reaches the end of the video file and play automatically stops it emits
both this event and a ``stop_video`` event (as of June 2014).

Note that course teams can specify a **Video Stop Time** for video files. 

* If the user streams a video file in a browser and a **Video Stop Time** is
  present for the video, the player stops at the specified time and emits the
  ``pause_video`` and ``stop_video`` events.

* If the user plays a streaming or downloaded video in the edX mobile app, the
  app ignores the **Video Stop Time** and plays the file to its end. The app
  then emits only the ``stop_video`` event.

For more information, see `Working with Video Components`_ in the *Building
and Running an edX Course* guide.

In addition to the identifying ``event_type`` of ``pause_video``, the events
that the edX mobile app emits include a ``name`` field with a value of
``edx.video.paused``.

**Event Source**: Browser or Mobile

**History**: 

* Updated 5 May 2015 to include the effect of a **Video Stop Time**. 
* Updated 25 Feb 2015 to include events emitted by the edX mobile app for iOS.
* Updated 23 Dec 2014 to include events emitted by the edX mobile app for
  Android.

``context`` **Member Fields**: 

Only video interaction events with an ``event_source`` of 'mobile' include
additional ``context`` member fields in addition to the :ref:`common<context>`
member fields. The same set of additional context fields are added for
``pause_video``/ ``edx.video.paused`` events as for
:ref:`play_video`. For an example of an event with these fields, see
:ref:`Example Mobile App Event`.

``event`` **Member Fields**: 

The ``pause_video``/``edx.video.paused`` events include the following
``event`` member fields. These fields serve the same purpose for events of
this type as for the :ref:`play_video` events.

* ``code``
* ``currentTime``: The time in the video at which the video paused.
* ``id``

.. _play_video:

``play_video``/``edx.video.played``
***********************************

When a user selects the video player's **play** control, the player emits a
``play_video`` event.

Note that course teams can specify a **Video Start Time** for video files. 

* If the user streams a video file in a browser and a **Video Start Time** is
  present for the video, the player starts at the specified time and emits the
  ``play_video`` event.

* If the user plays a streaming or downloaded video in the edX mobile app, the
  app ignores the **Video Start Time** and emits the ``play_video`` event
  when it plays the file from the beginning.

For more information, see `Working with Video Components`_ in the *Building
and Running an edX Course* guide.

In addition to the identifying ``event_type`` of ``play_video``, events
that the edX mobile app emits also include a ``name`` field with a value of
``edx.video.played``.

**Event Source**: Browser or Mobile

**History**: 

* Updated 5 May 2015 to include the effect of a **Video Start Time**. 
* Updated 25 Feb 2015 to include events emitted by the edX mobile app for iOS.
* Updated 23 Dec 2014 to include events emitted by the edX mobile app for
  Android.

``context`` **Member Fields**: 

Only video interaction events with an ``event_source`` of 'mobile' include
additional ``context`` member fields in addition to the :ref:`common<context>`
member fields. Other video interaction events with an ``event_source`` of
mobile also include these fields. For an example of an event with these
fields, see :ref:`Example Mobile App Event`.

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details and Member Fields
   * - ``application``
     - dictionary
     - Includes ``name`` and ``version`` member fields to identify the edX
       mobile app. 
   * - ``client``
     - dictionary
     - Includes member dictionaries and fields with device-specific data.

       The ``client`` data is gathered by the event collection library, which
       is provided by a third party.

       The content of this field is subject to change without notice.

   * - ``component``
     - string
     - 'videoplayer'
   * - ``received_at``
     - float
     - Indicates the time at which the event collection library received the
       event. 

       Events can only be forwarded when the mobile device is connected to the
       Internet. Therefore, this value can be different than the event's
       ``time`` value.

       The data in this field reflects a third-party integration and is subject
       to change at any time without notice.


``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``code``
     - string
     - For YouTube videos played in a browser, the ID of the video being
       loaded (for example, OEyXaRPEzfM).

       For non-YouTube videos played in a browser, 'html5'.

       For videos played by the edX mobile app, 'mobile'.

   * - ``currentTime``
     - float
     - The time in the video at which the event was emitted. 
   * - ``id``
     - string
     - The optional name value supplied by the course creators, or the system-
       generated hash code for the video being watched.

       For example, ``0b9e39477cf34507a7a48f74be381fdd``.
       
       This value is part of the ``courseware_studentmodule.module_id``. See
       :ref:`courseware_studentmodule`.

       **History**: In October 2014, identifiers for some new courses began to
       use the format shown above. Other new courses, and all courses created
       prior to October 2014, use an HTML-escaped version of the
       ``courseware_studentmodule.module_id``. For example, 
       ``i4x-HarvardX-PH207x-video-Simple_Random_Sample``.


Example: Browser-Emitted ``play_video`` Event 
**********************************************

.. code-block:: json

  {
    "event_source": "browser",
    "event": "{\"id\":\"i4x-BerkeleyX-Stat_2_1x-video-58424ad2f75048798b4480aa699cc215\",\"currentTime\":243,\"code\":\"iOOYGgLADj8\"}",
    "time": "2014-12-23T14:26:53.723188+00:00",
    "referer": "http:\/\/localhost:8001\/container\/i4x:\/\/edX\/DemoX\/vertical\/69dedd38233a46fc89e4d7b5e8da1bf4?action=new",
    "accept_language": "en-US,en;q=0.8",
    "event_type": "play_video",
    "session": "11a1111111a1a1a1aa1a11a1a1111111",
    "agent": "Mozilla\/5.0 (Windows NT 6.1; WOW64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/39.0.2171.95 Safari\/537.36",
    "page": "https:\/\/courses.edx.org\/courses\/BerkeleyX\/Stat_2.1x\/1T2014\/courseware\/d4ff35dabfe64ed5b1f1807eb0292c73\/bd343b7dcb2c4817bd1992b0cef66ff4\/",
    "username": "AAAAAAAAAA",
    "ip": "123.123.123.123",
    "context": {
      "org_id": "BerkeleyX",
      "path": "\/event",
      "course_id": "BerkeleyX\/Stat_2.1x\/1T2014",
      "user_id": 99999999
    },
    "host": "courses.edx.org"
  }

.. _Example Mobile App Event:

Example: Mobile App-Emitted ``edx.video.played`` Event 
*******************************************************

.. code-block:: json

  {
    "username": "AAAAAAAAAA",
    "event_source": "mobile",
    "name": "edx.video.played",
    "time": "2014-12-09T03:57:24+00:00",
    "agent": "Dalvik/1.6.0 (Linux; U; Android 4.0.2; sdk Build/ICS_MR0)",
    "page": "http://courses.edx.org/courses/edX/DemoX/Demo_Course/courseware/d8a6192ade314473a78242dfeedfbf5b/edx_introduction",
    "host": "courses.edx.org",
    "session": "",
    "context": {
        "component": "videoplayer",
        "received_at": "2014-12-09T03:57:56.373000+00:00",
        "course_id": "edX/DemoX/Demo_Course",
        "path": "/segmentio/event",
        "user_id": 99999999,
        "org_id": "edX",
        "application": {
          "name": "edx.mobileapp.android",
          "version": "0.1.8",
        },
        "client": {
            "network": {
                "wifi": false,
                "carrier": "Android",
                "cellular": true,
                "bluetooth": false
            },
            "locale": "en-US",
            "app": {
                "name": "edX",
                "packageName": "org.edx.mobile",
                "version": "0.1.8",
                "build": "org.edx.mobile@29",
                "versionName": "0.1.8",
                "versionCode": 29
            },
            "library": {
                "version": 203,
                "name": "analytics-android",
                "versionName": "2.0.3"
            },
            "device": {
                "model": "sdk",
                "type": "android",
                "id": "aaa11111aaaa11a1",
                "name": "generic",
                "manufacturer": "unknown"
            },
            "os": {
                "version": "4.0.2",
                "name": "REL",
                "sdk": 14
            },
            "screen": {
                "densityBucket": "xhdpi",
                "density": 2,
                "height": 1184,
                "width": 768,
                "densityDpi": 320,
                "scaledDensity": 2
            }
        }
    },
    "ip": "",
    "event": "{\"code\": \"mobile\", \"id\": \"i4x-edX-DemoX-video-0b9e39477cf34507a7a48f74be381fdd\", \"currentTime\": 114}",
    "event_type": "play_video"
  }


``seek_video``/``edx.video.position.changed``
*********************************************

A browser emits ``seek_video`` events when a user selects a user interface
control to go to a different point in the video file.

* On a desktop computer, users can click and drag in the playback bar or click
  in a transcript to change position.
* In the edX mobile app, users can click and drag in the playback bar or tap
  the "back 30 seconds" button to change position.
* When using a browser on a mobile device, users can click and drag in the
  playback bar to change position.

In addition to the value ``seek_video`` in the ``event_type`` field, the
events that the edX mobile app emits include the value
``edx.video.position.changed`` in the ``name`` field.

**Event Source**: Browser or Mobile

**History**: 

* Updated 10 Mar 2015 to include the final implementation for events emitted
  by the edX mobile app for Android and iOS. Prototype events were emitted by
  the mobile app in February and March 2015.
  
* Prior to 25 Jun 2014, the ``old_time`` and ``new_time`` fields were set to
  the same value.

``context`` **Member Fields**: 

Only video interaction events with an ``event_source`` of 'mobile' include
additional ``context`` member fields in addition to the :ref:`common<context>`
member fields. The same set of additional context fields are added for
``seek_video``/ ``edx.video.position.changed`` events as for
:ref:`play_video`. For an example of an event with these fields, see
:ref:`Example Mobile App Event`.

``event`` **Member Fields**: 

The ``seek_video``/``edx.video.position.changed`` events include the following
``event`` member fields. These fields serve the same purpose for events of
this type as for the :ref:`play_video` events.

* ``code``
* ``id``

The following additional ``event`` member fields apply specifically to
``seek_video``/``edx.video.position.changed`` events.

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``new_time``
     - integer
     - The time in the video, in seconds, that the user selected as the
       destination point.
   * - ``old_time``
     - integer
     - The time in the video, in seconds, at which the user chose to go to a
       different point in the file.
   * - ``requested_skip_interval``
     - integer
     - Applies only to events with an  ``event_source`` of 'mobile'. The number
       of seconds that the user moved backward (expressed as a negative) or
       forward in the file.

       **History**: Added 10 Mar 2015.
       
   * - ``type``
     - string
     - The navigational method used to change position within the video.
       
       In events for a user of a desktop computer, this value can be
       'onCaptionSeek' or 'onSlideSeek'. In events for a user of the mobile
       app, this value can be 'onSlideSeek' or 'onSkipSeek'.


``show_transcript``/``edx.video.transcript.shown``
**************************************************

When a user selects **CC** to display the video transcript, the browser or
mobile app emits a ``show_transcript`` event.

In addition to the identifying ``event_type`` of ``show_transcript``, events
that the edX mobile app emits also include a ``name`` field with a value of
``edx.video.transcript.shown``.

**Event Source**: Browser or Mobile

**History**: Updated 25 Feb 2015 to include events emitted by the edX mobile
app for iOS. Updated 23 Dec 2014 to include events emitted by the edX mobile
app for Android.

``context`` **Member Fields**: 

Only video interaction events with an ``event_source`` of 'mobile' include
additional ``context`` member fields in addition to the :ref:`common<context>`
member fields. The same set of additional context fields are added for
``show_transcript``/ ``edx.video.transcript.shown`` events as for
:ref:`play_video`. For an example of an event with these fields, see
:ref:`Example Mobile App Event`.

``event`` **Member Fields**: 

The ``show_transcript``/``edx.video.transcript.shown`` events include the
following ``event`` member fields. These fields serve the same purpose for
events of this type as for the :ref:`play_video` events.

* ``code``
* ``currentTime``: The point in the video file at which the transcript was
  opened.
* ``id``

``speed_change_video`` 
*********************************

A browser emits ``speed_change_video`` events when a user selects a different
playing speed for the video.

**Event Source**: Browser

**History**: Prior to 12 Feb 2014, this event was emitted when a user
selected either the same speed or a different speed. 

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``current_time``
     - integer
     - The time in the video that the user chose to change the playing speed. 
   * - ``new_speed``
     - float
     - The speed that the user selected for the video to play: '0.75', '1.0',
       '1.25', '1.50'.
   * - ``old_speed``
     - float
     - The speed at which the video was playing. 

``stop_video``/``edx.video.stopped``
*************************************

When the video player reaches the end of the video file and play automatically
stops, the player emits a ``stop_video`` event.

Note that course teams can specify a **Video Stop Time** for video files. 

* If the user streams a video file in a browser and a **Video Stop Time** is
  present for the video, the player stops at the specified time and emits the
  ``pause_video`` and ``stop_video`` events.

* If the user plays a streaming or downloaded video in edX mobile app, the
  app ignores the **Video Stop Time** and plays the file to its end. The
  app then emits the ``stop_video`` event.

For more information, see `Working with Video Components`_ in the *Building
and Running an edX Course* guide.

In addition to the identifying ``event_type`` of ``stop_video``, the events
that the edX mobile app emits include a ``name`` field with a value of
``edx.video.stopped``.

**Event Source**: Browser or Mobile

**History**: 

* Updated 5 May 2015 to include the effect of a **Video Stop Time**. 
* Updated 25 Feb 2015 to include events emitted by the edX mobile app for iOS.
* Updated 23 Dec 2014 to include events emitted by the edX mobile app for
  Android.
* Added 25 June 2014.

``context`` **Member Fields**: 

Only video interaction events with an ``event_source`` of 'mobile' include
additional ``context`` member fields in addition to the :ref:`common<context>`
member fields. The same set of additional context fields are added for
``stop_video``/ ``edx.video.stopped`` events as for
:ref:`play_video`. For an example of an event with these fields, see
:ref:`Example Mobile App Event`.

``event`` **Member Fields**: 

The ``stop_video``/``edx.video.stopped`` events include the following
``event`` member fields. These fields serve the same purpose for events of
this type as for the :ref:`play_video` events.

* ``code``
* ``currentTime``: The time in the video at which play stopped.
* ``id``


``video_hide_cc_menu``
************************************************

When a user selects a language from the **CC** menu for a video that
has transcripts in multiple languages, the browser emits a
``video_hide_cc_menu`` event.

**Event Source**: Browser

**History**: Added 17 Feb 2015. 

``event`` **Member Fields**: 

The ``video_hide_cc_menu`` events include the following ``event`` member
fields. These fields serve the same purpose for events of this type as for
:ref:`play_video`.

* ``code``
* ``id``

``video_show_cc_menu``
************************************************

When a user selects **CC** for a video that has transcripts in multiple
languages, the browser emits a ``video_show_cc_menu`` event. This event is
emitted in addition to the ``show_transcript`` event.

**Event Source**: Browser

**History**: Added 17 Feb 2015. 

``event`` **Member Fields**: 

The ``video_show_cc_menu`` events include the following ``event`` member
fields. These fields serve the same purpose for events of this type as for
:ref:`play_video`.

* ``code``
* ``id``


.. _pre-roll:

==================================
Pre-Roll Video Interaction Events
==================================

Course teams can create a short video message and configure it to play
automatically before the videos in a course. 

* The pre-roll video plays on an infrequent schedule of once per user per week.

* Only courses that run on the edx.org website can include a pre-roll video.

* The edX mobile applications do not play pre-roll videos.

When a user interacts with the pre-roll video, different events are emitted
than for the other videos in the course. This section presents the pre-roll
video events alphabetically.

For more information about pre-roll videos, see `Adding a Pre-Roll Video to
Your edX Course`_ in the *Building and Running an edX Course* guide.

**Component**: Video

**History**: Added 10 Jun 2015.

``edx.video.bumper.dismissed``
*******************************

A browser emits this event when a user selects **Do not show again** for a 
pre-roll video. This option allows the user to opt out of viewing the course 
pre-roll video in the future.

**Event Source**: Browser

``event`` **Member Fields**: 

The ``edx.video.bumper.dismissed`` events include the following ``event``
member fields. These fields serve the same purpose for events of this type as
for the :ref:`edx.video.bumper.played` events.

* ``bumper_id``
* ``code``
* ``currentTime``
* ``duration``
* ``host_component_id``

``edx.video.bumper.loaded``
****************************

When the pre-roll video is fully rendered and ready to play, the browser emits
an ``edx.video.bumper.loaded`` event.

**Event Source**: Browser

``event`` **Member Fields**: 

The ``edx.video.bumper.loaded`` events include the following ``event``
member fields. These fields serve the same purpose for events of this type as
for the :ref:`edx.video.bumper.played` events.

* ``bumper_id``
* ``code``
* ``duration``
* ``host_component_id``

.. _edx.video.bumper.played:

``edx.video.bumper.played``
****************************

When a user selects the **play** control in the video player for a pre-roll
video, the browser emits an ``edx.video.bumper.played`` event.

**Event Source**: Browser

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``bumper_id``
     - string
     - The escaped URL identifying the location of the pre-roll video that
       played.
   * - ``code``
     - string
     - Contains the value 'html5'. All pre-roll videos are non-YouTube videos. 
   * - ``currentTime``
     - float
     - The time in the file at which the video played. 
   * - ``duration``
     - integer
     - The length of the video file, in seconds. 
   * - ``host_component_id``
     - string
     - Identifier for the video component that the user selected, and that is
       queued to play after the pre-roll video.

Example: ``edx.video.bumper.played`` Event 
**********************************************

.. code-block:: json

  {
    "username": "honor",
    "event_source": "browser",
    "name": "edx.video.bumper.played",
    "accept_language": "en-US,en;q=0.5",
    "time": "2015-05-26T18:22:07.684172+00:00",
    "agent": "Mozilla\/5.0 (X11; Ubuntu; Linux x86_64; rv:37.0) Gecko\/20100101 Firefox\/37.0",
    "page": "http:\/\/edx.org\/courses\/edX\/DemoX.1\/2015\/courseware\/0af8db2309474971bfa70cda98668a30\/ec3364075f2845baa625bfecd5970410\/",
    "host": "precise64",
    "session": "feae6efa342b309e776d388b16da89a6",
    "referer": "http:\/\/localhost:8001\/container\/i4x:\/\/edX\/DemoX\/vertical\/69dedd38233a46fc89e4d7b5e8da1bf4?action=new",
    "context": {
      "user_id": 7911,
      "org_id": "edX",
      "course_id": "edX\/DemoX.1\/2015",
      "path": "\/event"
    },
    "ip": "123.0.0.1",
    "event": "{\"duration\": 10, \"bumper_id\": \"http:\/\/www.w3schools.com\/html\/mov_bbb.webm\", \"code\": \"html5\", \"currentTime\": 0, \"host_component_id\": \"i4x-edX-DemoX_1-video-4e2eeecf597040e3b5e1a27600bc8ddc\"}",
    "event_type": "edx.video.bumper.played"
  }


``edx.video.bumper.skipped`` 
*********************************

A browser emits this event when a user selects **Skip** for a bumper video.
This option allows the user to advance past the pre-roll video and begin to
play the selected video immediately.

**Event Source**: Browser

``event`` **Member Fields**: 

The ``edx.video.bumper.skipped`` events include the following ``event`` member
fields. These fields serve the same purpose for events of this type as for the
:ref:`edx.video.bumper.played` events.

* ``bumper_id``
* ``code``
* ``currentTime``: The point in the file at which the pre-roll video was
  skipped.
* ``duration``
* ``host_component_id``

``edx.video.bumper.stopped``
****************************

A browser emits this event when the video player reaches the end of the pre-
roll video file and play automatically stops.

This is the only event that is emitted when a user pauses a pre-roll video. 

**Event Source**: Browser

``event`` **Member Fields**: 

The ``edx.video.bumper.stopped`` events include the following ``event`` member
fields. These fields serve the same purpose for events of this type as for the
:ref:`edx.video.bumper.played` events.

* ``bumper_id``
* ``code``
* ``currentTime``: The point in the file at which the pre-roll video was
  stopped.
* ``duration``
* ``host_component_id``

``edx.video.bumper.transcript.hidden``
**************************************

When a user selects **CC** to suppress display of the transcript for a pre-roll
video, the browser emits a ``edx.video.bumper.transcript.hidden`` event.

**Event Source**: Browser

``event`` **Member Fields**: 

The ``edx.video.bumper.transcript.hidden`` events include the following
``event`` member fields. These fields serve the same purpose for events of this
type as for the :ref:`edx.video.bumper.played` events.

* ``bumper_id``
* ``code``
* ``currentTime``: The point in the file at which the transcript was hidden.
* ``duration``
* ``host_component_id``

``edx.video.bumper.transcript.menu.hidden``
************************************************

When a user selects a language from the **CC** menu for a pre-roll video that
has transcripts in multiple languages, the browser emits an
``edx.video.bumper.transcript.menu.hidden`` event.

**Event Source**: Browser

``event`` **Member Fields**: 

The ``edx.video.bumper.transcript.menu.hidden`` events include the following
``event`` member fields. These fields serve the same purpose for events of this
type as for the :ref:`edx.video.bumper.played` events.

* ``bumper_id``
* ``code``
* ``currentTime``: The point in the file at which the language was selected and
  the transcript menu was hidden.
* ``duration``
* ``host_component_id``

``edx.video.bumper.transcript.menu.shown``
************************************************

When a user selects **CC** for a pre-roll video that has transcripts in
multiple languages, the browser emits an
``edx.video.bumper.transcript.menu.shown`` event. This event is emitted in
addition to the ``edx.video.bumper.transcript.shown`` event.

**Event Source**: Browser

``event`` **Member Fields**: 

The ``edx.video.bumper.transcript.menu.shown`` events include the following
``event`` member fields. These fields serve the same purpose for events of this
type as for the :ref:`edx.video.bumper.played` events.

* ``bumper_id``
* ``code``
* ``currentTime``: The point in the file at which the transcript menu was
  shown.
* ``duration``
* ``host_component_id``

``edx.video.bumper.transcript.shown``
**************************************

When a user selects **CC** to display the transcript for a pre-roll video, the
browser emits a ``edx.video.bumper.transcript.shown`` event. If the video has
more than one transcript file, the ``edx.video.bumper.transcript.menu.shown``
event is also emitted.

The ``edx.video.bumper.transcript.shown`` events include the following
``event`` member fields. These fields serve the same purpose for events of this
type as for the :ref:`edx.video.bumper.played` events.

* ``bumper_id``
* ``code``
* ``currentTime``: The point in the file at which the transcript was shown.
* ``duration``
* ``host_component_id``

.. _pdf:

=================================
Textbook Interaction Events   
=================================

This section includes descriptions of the following events. 

* ``book``
* ``textbook.pdf.thumbnails.toggled``
* ``textbook.pdf.thumbnail.navigated``
* ``textbook.pdf.outline.toggled``
* ``textbook.pdf.chapter.navigated``
* ``textbook.pdf.page.navigated``
* ``textbook.pdf.zoom.buttons.changed``
* ``textbook.pdf.zoom.menu.changed``
* ``textbook.pdf.display.scaled``
* ``textbook.pdf.display.scrolled``
* ``textbook.pdf.search.executed``
* ``textbook.pdf.search.navigatednext``
* ``textbook.pdf.search.highlight.toggled``
* ``textbook.pdf.search.casesensitivity.toggled``

``book``
*********************************

The browser emits ``book`` events when a user navigates within the PDF Viewer
or the PNG Viewer.

* For textbooks in PDF format, the URL in the common ``page`` field contains
  '/pdfbook/'.
* For textbooks in PNG format, the URL in the common ``page`` field contains
  '/book/'.

**Component**: PDF Viewer, PNG Viewer 

**Event Source**: Browser

**History**: This event changed on 16 Apr 2014 to include ``event`` member
fields ``name`` and ``chapter``.

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``chapter``
     - string
     - The name of the PDF file. 
       **History**: Added for events produced by the PDF Viewer on 16 Apr 2014.
   * - ``name``
     - string
     -  
       * For 'gotopage', set to ``textbook.pdf.page.loaded``.
       * For 'prevpage', set to ``textbook.pdf.page.navigatedprevious``. 
       * For 'nextpage', set to ``textbook.pdf.page.navigatednext``. 
       
       **History**: Added for events produced by the PDF Viewer on 16 Apr 2014.
   * - ``new``
     - integer
     - Destination page number.
   * - ``old``
     - integer
     - The original page number. Applies to 'gotopage' event types only. 
   * - ``type``
     - string
     -  
       * 'gotopage' is emitted when a page loads after the student manually
         enters its number.
       * 'prevpage' is emitted when the next page button is clicked.
       * 'nextpage' is emitted when the previous page button is clicked.


``textbook.pdf.thumbnails.toggled``
*************************************

The browser emits ``textbook.pdf.thumbnails.toggled`` events when a user clicks
on the icon to show or hide page thumbnails.

**Component**: PDF Viewer 

**Event Source**: Browser

**History**: This event was added on 16 Apr 2014.

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``chapter``
     -  string
     -  The name of the PDF file.
   * - ``name``
     - string
     - ``textbook.pdf.thumbnails.toggled``
   * -  ``page``
     -  integer
     -  The number of the page that is open when the user clicks this icon. 

``textbook.pdf.thumbnail.navigated``
*************************************

The browser emits ``textbook.pdf.thumbnail.navigated`` events when a user
clicks on a thumbnail image to navigate to a page.

**Component**: PDF Viewer 

**Event Source**: Browser

**History**: This event was added on 16 Apr 2014.

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``chapter`` 
     - string
     - The name of the PDF file. 
   * - ``name``
     - string
     - ``textbook.pdf.thumbnail.navigated``
   * - ``page``
     - integer
     - The page number of the thumbnail clicked.
   * - ``thumbnail_title``
     - string
     - The identifying name for the destination of the thumbnail. For example,
       Page 2.

``textbook.pdf.outline.toggled``
*********************************

The browser emits ``textbook.pdf.outline.toggled`` events when a user clicks
the outline icon to show or hide a list of the book's chapters.

**Component**: PDF Viewer 

**Event Source**: Browser

**History**: This event was added on 16 Apr 2014.

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``chapter`` 
     - string
     - The name of the PDF file.
   * - ``name``
     - string
     - ``textbook.pdf.outline.toggled``
   * - ``page`` 
     - integer
     - The number of the page that is open when the user clicks this link.

``textbook.pdf.chapter.navigated``
************************************

The browser emits ``textbook.pdf.chapter.navigated`` events when a user clicks
on a link in the outline to navigate to a chapter.

**Component**: PDF Viewer 

**Event Source**: Browser

**History**: This event was added on 16 Apr 2014.

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``chapter``
     - string
     - The name of the PDF file.
   * - ``chapter_title``
     - string
     - The identifying name for the destination of the outline link. 
   * - ``name``
     - string
     - ``textbook.pdf.chapter.navigated``
     
``textbook.pdf.page.navigated``
*********************************

The browser emits ``textbook.pdf.page.navigated`` events when a user manually
enters a page number.

**Component**: PDF Viewer 

**Event Source**: Browser

**History**: This event was added on 16 Apr 2014.

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``chapter``
     - string
     - The name of the PDF file.
   * - ``name``
     - string
     - ``textbook.pdf.page.navigated``
   * - ``page``
     - integer
     - The destination page number entered by the user.

``textbook.pdf.zoom.buttons.changed``
**************************************

The browser emits ``textbook.pdf.zoom.buttons.changed`` events when a user
clicks either the Zoom In or Zoom Out icon.

**Component**: PDF Viewer 

**Event Source**: Browser

**History**: This event was added on 16 Apr 2014.

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``chapter``
     - string
     - The name of the PDF file.
   * - ``direction``
     -  string
     -  'in', 'out'
   * - ``name``
     - string
     - ``textbook.pdf.zoom.buttons.changed``
   * - ``page``
     - integer
     - The number of the page that is open when the user clicks the icon.

``textbook.pdf.zoom.menu.changed``
***********************************

The browser emits ``textbook.pdf.zoom.menu.changed`` events when a user selects
a magnification setting.

**Component**: PDF Viewer 

**Event Source**: Browser

**History**: This event was added on 16 Apr 2014.

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``amount``
     - string
     - '1', '0.75', '1.5', 'custom', 'page_actual', 'auto', 'page_width',
       'page_fit'.
   * - ``chapter``
     - string
     - The name of the PDF file.
   * - ``name``
     - string
     - ``textbook.pdf.zoom.menu.changed``
   * - ``page``
     - integer
     - The number of the page that is open when the user selects this value.

``textbook.pdf.display.scaled``
*********************************

The browser emits ``textbook.pdf.display.scaled`` events when the display
magnification changes. These changes occur after a student selects a
magnification setting from the zoom menu or resizes the browser window.

**Component**: PDF Viewer 

**Event Source**: Browser

**History**: This event was added on 16 Apr 2014.

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``amount``
     - string
     - The magnification setting; for example, 0.95 or 1.25.
   * - ``chapter``
     - string
     - The name of the PDF file. 
   * - ``name``
     - string
     - ``textbook.pdf.display.scaled``
   * - ``page`` 
     - integer
     - The number of the page that is open when the scaling takes place.

``textbook.pdf.display.scrolled``
*********************************

The browser emits ``textbook.pdf.display.scrolled`` events each time the
displayed page changes while a user scrolls up or down.

**Component**: PDF Viewer 

**Event Source**: Browser

**History**: This event was added on 16 Apr 2014.

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``chapter``
     - string
     - The name of the PDF file. 
   * - ``direction``
     - string
     - 'up', 'down' 
   * - ``name``
     - string
     - ``textbook.pdf.display.scrolled``
   * - ``page``
     - integer
     - The number of the page that is open when the scrolling takes place.

``textbook.pdf.search.executed``
*********************************

The browser emits ``textbook.pdf.search.executed`` events when a user searches
for a text value in the file. To reduce the number of events produced, instead
of producing one event per entered character this event defines a search string
as the set of characters that is consecutively entered in the search field
within 500ms of each other.

**Component**: PDF Viewer 

**Event Source**: Browser

**History**: This event was added on 16 Apr 2014.

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1


   * - Field
     - Type
     - Details
   * - ``caseSensitive``
     - Boolean
     - 'true' if the case sensitive option is selected. 
       
       'false' if this option is not selected.

   * - ``chapter``
     - string
     - The name of the PDF file. 
   * - ``highlightAll``
     - Boolean
     - 'true' if the option to highlight all matches is selected. 
       
       'false' if this option is not selected.

   * - ``name``
     - string
     - ``textbook.pdf.search.executed``
   * - ``page``
     - integer
     - The number of the page that is open when the search takes place.
   * - ``query``
     - string
     - The value in the search field.
   * - ``status``
     - string
     - A "not found" status phrase for a search string that is unsuccessful.
       
       Blank for successful search strings.


``textbook.pdf.search.navigatednext``
**************************************

The browser emits ``textbook.pdf.search.navigatednext`` events when a user
clicks on the Find Next or Find Previous icons for an entered search string.

**Component**: PDF Viewer 

**Event Source**: Browser

**History**: This event was added on 16 Apr 2014.

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``caseSensitive``
     - Boolean
     - 'true' if the case sensitive option is selected. 
       
       'false' if this option is not selected.

   * - ``chapter``
     - string
     - The name of the PDF file. 
   * - ``findprevious``
     - Boolean
     - 'true' if the user clicks the Find Previous icon. 
       
       'false' if the user clicks the Find Next icon.

   * - ``highlightAll``
     - Boolean
     - 'true' if the option to highlight all matches is selected. 
       
       'false' if this option is not selected.

   * - ``name``
     - string
     - ``textbook.pdf.search.navigatednext`` 
   * - ``page``
     - integer
     - The number of the page that is open when the search takes place.
   * - ``query``
     - string
     - The value in the search field.
   * - ``status``
     -  string
     - A "not found" status phrase for a search string that is unsuccessful.
       
       Blank for successful search strings.


``textbook.pdf.search.highlight.toggled``
******************************************

The browser emits ``textbook.pdf.search.highlight.toggled`` events when a user
selects or clears the **Highlight All** option for a search.

**Component**: PDF Viewer 

**Event Source**: Browser

**History**: This event was added on 16 Apr 2014.

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``caseSensitive``
     - Boolean
     - 'true' if the case sensitive option is selected. 
       
       'false' if this option is not selected.

   * - ``chapter``
     - string
     - The name of the PDF file. 
   * - ``highlightAll``
     - Boolean
     - 'true' if the option to highlight all matches is selected. 
       
       'false' if this option is not selected.

   * - ``name``
     - string
     - ``textbook.pdf.search.highlight.toggled``
   * - ``page``
     - integer
     - The number of the page that is open when the search takes place.
   * - ``query``
     - string
     - The value in the search field. 
   * - ``status``
     - string
     - A "not found" status phrase for a search string that is unsuccessful.
       
       Blank for successful search strings.


``textbook.pdf.search.casesensitivity.toggled``
************************************************

The browser emits ``textbook.pdf.search.casesensitivity.toggled`` events when a
user selects or clears the **Match Case** option for a search.

**Component**: PDF Viewer 

**Event Source**: Browser

**History**: This event was added on 16 Apr 2014.

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``caseSensitive``
     - Boolean
     - 'true' if the case sensitive option is selected. 
       
       'false' if this option is not selected.

   * - ``chapter``
     - string
     - The name of the PDF file. 
   * - ``highlightAll``
     - Boolean
     - 'true' if the option to highlight all matches is selected.
       
       'false' if this option is not selected.

   * - ``name``
     - string
     - ``textbook.pdf.search.casesensitivity.toggled``
   * - ``page``
     - integer
     - The number of the page that is open when the search takes place.
   * - ``query``
     - string
     - The value in the search field.
   * - ``status``
     -  string
     - A "not found" status phrase for a search string that is unsuccessful.
       
       Blank for successful search strings.


.. _problem:

=================================
Problem Interaction Events 
=================================

This section includes descriptions of the following events. 

.. contents:: Section Contents
  :local:
  :depth: 1

Problem interaction events are emitted by the server or the browser to capture
information about interactions with problems. 

These events were designed for the problem types implemented in the edX
platform by the ``capa_module.py`` XBlock. Problem types that are implemented
by other XBlocks, such as :ref:`open response assessments<ora2>` or :ref:`polls
and surveys<Poll and Survey Events>`, are instrumented with different events.

For more information about designing problems to include hints, feedback, or
both, see `Adding Hints and Feedback to a Problem`_ in the *Building and
Running an edX Course* guide.

``edx.problem.hint.demandhint_displayed``
******************************************

Course teams can design problems to include one or more hints. For problems
that include hints, the server emits an
``edx.problem.hint.demandhint_displayed`` event each time a user requests a
hint.

**Event Source**: Server

**History**: This event was added on 1 Jul 2015.

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``hint_index``
     - integer
     - Identifier for the hint that was displayed to the user. The first hint
       defined for a problem is identified with ``hint_index: 0``.
   * - ``hint_len``
     - integer
     - The total number of hints defined for this problem. 
   * - ``hint_text``
     - string
     - The text of the hint that was displayed to the user.
   * - ``module_id``
     - string
     - Identifier for the problem component for which the user requested the
       hint.

``edx.problem.hint.feedback_displayed``
*****************************************

Course teams can design problems to include feedback messages that appear after
a user submits an answer. For problems that include feedback messages, the
server emits an ``edx.problem.hint.feedback_displayed`` event each time a user
selects **Check**.

**Event Source**: Server

**History**: This event was added on 1 Jul 2015.

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``choice_all``
     - array
     - For problems that have a set of possible answers defined, such as
       checkbox problems, lists all of the answer choices.
   * - ``correctness``
     - Boolean
     - 'True' if the ``student_answer`` response is correct. 'False' if the
       ``student_answer`` is incorrect.
   * - ``hint_label``
     - string
     - The optional label, such as 'Correct: ' or 'Incorrect: ', provided for
       the feedback message.
   * - ``hints``
     - array
     - Contains a ``text`` member field with the feedback string that was
       displayed to the user. For some problem types, such as checkbox
       problems, feedback can be provided for more than one answer at a time,
       including both correct and incorrect answers. A separate ``text`` member
       field is included for each feedback message that was displayed.
   * - ``module_id``
     - string
     - Identifier for the problem component for which the user received the
       feedback.
   * - ``problem_part_id``
     - string
     - For problem components that contain more than one problem, identifies
       the specific problem for which the user received feedback.
   * - ``question_type``
     - string
     - The XML tag that identifies the problem type. For example,
       'stringresponse' for a text input problem.
   * - ``student_answer``
     - array
     - The answer value selected or supplied by the user. For problem types
       that accept multiple answers, such as checkbox problems, every response,
       including both selected and unselected options, is included.
   * - ``trigger_type``
     - string
     - Identifies the type of feedback elicited by the ``student_answer``
       response. For checkbox problems only, course teams can design 'compound'
       feedback that is provided when a user's response matches an exact set of
       correct and incorrect selections across all of the available choices.
       All other types of feedback are identified as 'single'.

       For more information, see `Adding Hints and Feedback to a Problem`_ in
       the *Building and Running an edX Course* guide.


``problem_check`` (Browser)
*********************************

.. no sample to check

Both browser interactions and server requests produce ``problem_check`` events.
The browser emits ``problem_check`` events when a user checks a problem.

**Event Source**: Browser 

``event`` **Member Fields**: For browser-emitted ``problem_check`` events, the
``event`` field contains the values of all input fields from the problem being
checked, styled as GET parameters.

``problem_check`` (Server)
*********************************

.. no sample to check

Both browser interactions and server requests produce ``problem_check`` events.

The server emits ``problem_check`` events when a problem is successfully
checked.
  
**Event Source**: Server

**History**: 

* On 5 Mar 2014, the ``submission`` dictionary was added to the ``event`` field
  and  ``module`` was added to the ``context`` field.

* Prior to 15 Oct 2013, this server-emitted event was named
  ``save_problem_check``.

* Prior to 15 Jul 2013, this event was emitted twice for the same action.

``context`` **Member Fields**: 

This event type includes the :ref:`common<context>` ``context.module`` member
field.

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``answers``
     - dictionary
     - The problem ID and the internal answer identifier in a name/value pair.
       For a component with multiple problems, lists every problem and
       answer.
   * - ``attempts``
     - integer
     - The number of times the user attempted to answer the problem.
   * - ``correct_map``
     - dictionary
     - For each problem ID value listed by ``answers``, provides:
       
       * ``correctness``: string; 'correct', 'incorrect'
       * ``hint``: string; Gives optional hint. Nulls allowed.
       * ``hintmode``: string; None, 'on_request', 'always'. Nulls allowed.
       * ``msg``: string; Gives extra message response.
       * ``npoints``: integer; Points awarded for this ``answer_id``. Nulls
         allowed.
       * ``queuestate``: dictionary; None when not queued, else ``{key:'',
         time:''}`` where ``key`` is a secret string dump of a DateTime object
         in the form '%Y%m%d%H%M%S'. Nulls allowed.

   * - ``grade``
     - integer
     - Current grade value. 
   * - ``max_grade``
     - integer
     - Maximum possible grade value.
   * - ``problem_id``
     - string
     - ID of the problem that was checked.
   * - ``state``
     - dictionary
     - Current problem state.
   * - ``submission``
     - object
     - Provides data about the response made. 
       
       For components that include multiple problems, a separate submission
       object is provided for each one.

       * ``answer``: string; The value that the student entered, or the display
         name of the value selected.
       * ``correct``: Boolean; 'true', 'false'
       * ``input_type``: string; The type of value that the student supplies
         for the ``response_type``. Based on the XML element names used in the
         Advanced Editor. Examples include 'checkboxgroup', 'radiogroup',
         'choicegroup', and 'textline'.
       * ``question``: string; Provides the text of the question.
       * ``response_type``: string; The type of problem. Based on the XML
         element names used in the Advanced  Editor. Examples include
         'choiceresponse', 'optionresponse', and 'multiplechoiceresponse'.
       * ``variant``: integer; For problems that use problem randomization
         features such as answer pools or choice shuffling, contains the unique
         ID of the variant that was presented to this user. 

   * - ``success``
     - string
     - 'correct', 'incorrect' 

``problem_check_fail``
*********************************

.. no sample to check

The server emits ``problem_check_fail`` events when a problem cannot be checked
successfully.

**Event Source**: Server

**History**: Prior to 15 Oct 2013, this event was named
``save_problem_check_fail``.

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``answers`` 
     - dictionary
     - 
   * - ``failure`` 
     - string
     - 'closed', 'unreset'
   * - ``problem_id``
     - string
     - ID of the problem being checked.
   * - ``state``  
     - dictionary
     - Current problem state.

``problem_graded``
*********************************

.. return Logger.log('problem_graded', [_this.answers, response.contents], _this.id);

The server emits a ``problem_graded`` event each time a user clicks **Check**
for a problem and it is graded successfully.

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``[answers, contents]``
     - array
     - ``answers`` provides the value checked by the user. 
       
       ``contents`` delivers HTML using data entered for the problem in Studio,
       including the display name, problem text, and choices or response field
       labels.

       The array includes each problem in a problem component that has multiple
       problems.


``problem_rescore``
*********************************

.. no sample to check

The server emits ``problem_rescore`` events when a problem is successfully
rescored.

**Event Source**: Server

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``attempts``
     - integer
     - 
   * - ``correct_map``
     - dictionary
     - See the fields for the ``problem_check`` server event above.
   * - ``new_score`` 
     - integer
     - 
   * - ``new_total``
     - integer
     - 
   * - ``orig_score``
     - integer
     - 
   * - ``orig_total``
     - integer
     - 
   * - ``problem_id``
     - string
     - ID of the problem being rescored.
   * - ``state``
     - dictionary
     - Current problem state.
   * - ``success``
     - string
     - 'correct', 'incorrect'

``problem_rescore_fail``
*********************************

.. no sample to check

The server emits ``problem_rescore_fail`` events when a problem cannot be
successfully rescored.

**Event Source**: Server

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``failure`` 
     - string
     - 'unsupported', 'unanswered', 'input_error', 'unexpected'
   * - ``problem_id``
     - string
     - ID of the problem being checked.
   * - ``state``
     - dictionary
     - Current problem state. 


``problem_reset``
*********************************

The browser emits ``problem_reset`` events when a user clicks **Reset** to
reset the answer to a problem.

.. return Logger.log('problem_reset', [_this.answers, response.contents], _this.id);

**Event Source**: Browser

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``answers``
     - string
     - The value reset by the user. 


``problem_save``
*********************************

.. no sample to check

The browser emits ``problem_save`` events when a user saves a problem.

**Event Source**: Browser

``event`` **Member Fields**: None

``problem_show``
*********************************

.. no sample to check

The browser emits ``problem_show`` events when a problem is shown.  

.. %%

**Event Source**: Browser

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``problem``
     - string
     - The optional name value that the course creators supply or the 
       system-generated hash code for the problem being shown.

       For example, ``input_303034da25524878a2e66fb57c91cf85_2_1`` or
       ``303034da25524878a2e66fb57c91cf85_2_1``.
       
       This value is based on part of the
       ``courseware_studentmodule.module_id``. See
       :ref:`courseware_studentmodule`.

       **History**: In October 2014, identifiers for some new courses began to
       use the format shown above. Other new courses, and all courses created
       prior to October 2014, use an HTML-escaped version of the
       ``courseware_studentmodule.module_id``. For example,
       ``i4x://MITx/6.00x/problem/L15:L15_Problem_2``.

``reset_problem``
*********************************

.. no sample to check

The server emits ``reset_problem`` events when a problem has been reset
successfully.

.. %%what is the difference between reset_problem and problem_reset?

**Event Source**: Server

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``new_state``
     - dictionary
     - New problem state.  
   * - ``old_state``
     - dictionary
     - The state of the problem before the reset was performed. 
   * - ``problem_id``
     - string
     - ID of the problem being reset.

``reset_problem_fail`` 
*********************************

.. no sample to check

The server emits ``reset_problem_fail`` events when a problem cannot be reset
successfully.

**Event Source**: Server

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details 
   * - ``failure``
     - string
     - 'closed', 'not_done'
   * - ``old_state``
     - dictionary
     - The state of the problem before the reset was requested.
   * - ``problem_id``
     - string
     - ID of the problem being reset. 

``save_problem_fail`` 
*********************************

.. no sample to check

The server emits ``save_problem_fail``  events when a problem cannot be saved
successfully.

**Event Source**: Server

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``answers`` 
     - dictionary
     - 
   * - ``failure`` 
     - string
     - 'closed', 'done' 
   * - ``problem_id``
     - string
     - ID of the problem being saved. 
   * - ``state``
     - dictionary
     - Current problem state.

``save_problem_success``
*********************************

.. no sample to check

The server emits ``save_problem_success`` events when a problem is saved
successfully.

**Event Source**: Server

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``answers``
     -  dictionary
     -  
   * - ``problem_id``
     - string
     - ID of the problem being saved. 
   * - ``state``
     - dictionary
     - Current problem state. 

``show_answer`` 
*********************************

.. no sample to check

The server emits ``show_answer`` events when the answer to a problem is shown. 

**Event Source**: Server

**History**: The original name for this event was ``showanswer``. 

.. **Question** is this renaming info correct?

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``problem_id``
     - string
     - EdX ID of the problem being shown. 

.. _library_events:

==========================
Library Interaction Events
==========================

This section includes descriptions of the following events. 

* ``edx.librarycontentblock.content.assigned``
* ``edx.librarycontentblock.content.removed``

Course teams in an organization can collaboratively contribute to libraries of
content, such as a collection of problem components for a particular subject.
Libraries are created and maintained separately from courses so that their
content can be used in different courses.

In a course outline, course teams can include randomized content block
components that reference a library and deliver its content to students. In a
randomized content block component, the course team defines how many of the
library components to deliver to each student.

For more information, see `Working with Libraries`_.

.. xref to come from Carol

``edx.librarycontentblock.content.assigned``
********************************************

The server emits an ``edx.librarycontentblock.content.assigned`` event the
first time that content from a randomized content block is delivered to a
user. The ``edx.librarycontentblock.content.assigned`` event identifies the
components delivered from the library to a user.

Additional ``edx.librarycontentblock.content.assigned`` events can also be
emitted if the course team makes a change that results in an increase in the
number of components that the randomized content block delivers. After such a
change, the randomized content block delivers more components to any user who
revisits it after that change. For those users, the
``edx.librarycontentblock.content.assigned`` event identifies the complete set
of components delivered from the library and also the components that were
delivered for the first time.

**Event Source**: Server

**History** Added 18 Mar 2015.

``event`` **Member Fields**:

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``added``
     - list
     - Lists the library components that were delivered to the user for the
       first time. The content of this field is different from the content of
       the ``result`` field only if the user revisited the randomized content
       block and it delivered additional components from the library.
   * - ``location``
     - string
     - Identifies the randomized content block component. 
   * - ``max_count``
     - integer
     - The **Count** specified by a course team member in Studio. Defines the
       number of library components to deliver. This number is greater than
       the number of library components listed by the ``result`` field only
       when the library has too few matching blocks available.
   * - ``previous_count``
     - integer
     - The number of components assigned to this student before this event.
       The first time the user views the randomized content block, this value
       is 0. 
   * - ``result``
     - list
     - Lists all of the library components delivered to the user. 

       * ``descendants``, when present, is a list that identifies each
         part of a library component that contains multiple parts (the
         children of an XBlock with children).

       * ``original_usage_key`` and ``original_usage_version`` identify the
         component in the library. 

         When students attempt a problem component delivered by a randomized
         content block, the resulting problem events also reference the
         ``original_usage_key`` and ``original_usage_version`` in
         ``context.module`` member fields. See :ref:`context`.

       * ``usage_key`` identifies the location of this component in the
         course. This value identifies a child of the randomized
         content block component.
       
       To identify a component consistently within a course, you can use
       either ``usage_key`` or ``original_usage_key`` as a consistent
       identifier. To identify components across courses, use
       ``orignal_usage_key``.
       
       
``edx.librarycontentblock.content.removed``
*******************************************

The server emits an ``edx.librarycontentblock.content.removed`` event when a
user revisits a randomized content block and one or more of the components
that were previously delivered to that user can no longer be delivered.

* If components are removed from the library and the course team
  resynchronizes the randomized content block to the library, the server emits
  an ``edx.librarycontentblock.content.removed`` event if a user who was
  previously assigned one of those components revisits the randomized content
  block or accesses the progress page.

* If the course team changes settings for the randomized content block so that
  fewer or different components are allowed.

  For example, the course team reduces the number of library components to
  deliver or specifies a different type of problem to deliver.

**Event Source**: Server

**History** Added 18 Mar 2015.

``event`` **Member Fields**:

The ``edx.librarycontentblock.content.removed`` events include the following
``event`` member fields. These fields serve the same purpose for events of
this type as for the ``edx.librarycontentblock.content.assigned`` events.

* ``location``
* ``max_count``
* ``previous_count``
* ``result``

The following additional ``event`` member fields apply specifically to
``edx.librarycontentblock.content.removed`` events.

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``reason``
     - string
     - 'overlimit' if a course team member reduces the **Count** of library
       components to deliver.
       
       'invalid' if the component is no longer included in the library, or no
       longer matches the settings specified for the randomized content block.

   * - ``removed``
     - list
     - Identifies the components that are no longer delivered to this user.
       This field contains the same member fields as the ``event.result``
       field for ``edx.librarycontentblock.content.assigned`` events.


.. _forum_events:

==========================
Discussion Forums Events
==========================

This section includes descriptions of the following events. 

* ``edx.forum.comment.created``
* ``edx.forum.response.created``
* ``edx.forum.searched``
* ``edx.forum.thread.created``

The server emits discussion forums events when a user interacts with a course
discussion. This section presents the discussion forum events alphabetically.
However, several of these events have hierarchical or sequential
relationships.

* When a user creates a new thread, such as a student asking a question, the
  server emits an :ref:`forum_thread` event.

* When a user responds to a thread, such as another student answering the
  question, the server emits an :ref:`forum_response` event.

* When a user adds a comment to a response, such as a course team member adding
  a clarification to the student answer, the server emits an
  :ref:`forum_comment` event.

These events are included in the daily event logs in addition to the MongoDB
discussion forums database data that is included in the weekly database data
files. For information about the discussion forums database, see
:ref:`Discussion Forums Data`.

If a thread, response, or comment was part of a team discussion within a
course, a ``team_id`` field is included in the ``edx.forum.thread.created``,
``edx.forum.response.created``, or ``edx.forum.comment.created`` event to
identify the team in which the discussion event was triggered. For more
information about events for teams, see :ref:`student_teams_events`.


.. _forum_comment:

``edx.forum.comment.created``
*********************************

Users create a comment about a response by entering text and then submitting
the contributions. When these actions are complete, the server emits an
``edx.forum.comment.created`` event.

**Component**: Discussion

**Event Source**: Server

**History**: Added 5 Mar 2015.

``event`` **Member Fields**:

The ``edx.forum.comment.created`` events include many of the same ``event``
member fields that are described for :ref:`forum_thread` and
:ref:`forum_response` events. The following member fields serve the same
purpose for comments as they do for threads or responses.

* ``body``
* ``commentable_id``
* ``discussion``
* ``id``
* ``options``
* ``team_id``
* ``truncated``
* ``url``
* ``user_course_roles``
* ``user_forums_roles``

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``response``
     - dictionary
     - Contains a member ``id`` field with the unique identifier of the
       response that the user added this comment to.

.. _forum_response:

``edx.forum.response.created``
*********************************

Users create a reply to a post by clicking **Add a Response** and then
submitting their contributions. When these actions are complete, the server
emits an ``edx.forum.response.created`` event.

**Component**: Discussion

**Event Source**: Server

**History**: Added 5 Mar 2015. 

``event`` **Member Fields**:

The ``edx.forum.response.created`` events include many of the same ``event``
member fields that are described for :ref:`forum_thread` events. The following
member fields serve the same purpose for responses as they do for threads.

* ``body``
* ``commentable_id``
* ``id``
* ``options``
* ``team_id``
* ``truncated``
* ``url``
* ``user_course_roles``
* ``user_forums_roles``

The following additional ``event`` member field applies specifically to
``edx.forum.response.created`` events.

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``discussion``
     - dictionary
     - Contains a member ``id`` field with the unique identifier of the thread
       that the user responded to.

       Also present for ``edx.forum.comment.created`` events.


``edx.forum.searched``
*********************************

After a user executes a text search in the navigation sidebar of the course
**Discussion** page, the server emits an ``edx.forum.searched`` event.

**Component**: Discussion

**Event Source**: Server

**History**: Added 16 May 2014.  The ``corrected_text`` field was added 5
Jun 2014. The ``group_id`` field was added 7 October 2014.

``event`` **Member Fields**:

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``corrected_text``
     - string
     - A re-spelling of the query, suggested by the search engine, which was
       automatically substituted for the original one. 

       This happens only when there are no results for the original query, but
       the index contains matches for a similar term or phrase.

       Otherwise, this field is null.

   * - ``group_id``
     - integer
     - The numeric ID of the cohort to which the user's search is
       restricted, or ``null`` if the search is not restricted in this way. 

       In a course with cohorts enabled, a student's searches will always be
       restricted to the student's cohort. 

       Discussion admins, moderators, and Community TAs in such a course can
       search all discussions without specifying a cohort, which leaves
       this field ``null``, or they can specify a single cohort to
       search.

   * - ``page``
     - integer
     - Results are returned in sets of 20 per page. 
       
       Identifies the page of results requested by the user.

   * - ``query``
     - string
     - The text entered into the search box by the user.
   * - ``total_results``
     - integer
     - The total number of results matching the query.

.. _forum_thread:

``edx.forum.thread.created``
*********************************

Users create a new top-level thread, also known as a post, by clicking **New
Post** and then submitting their contributions. When these actions are
complete, the server emits an ``edx.forum.thread.created`` event.

**Component**: Discussion

**Event Source**: Server

**History**: Added 5 Mar 2015.

``event`` **Member Fields**:

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details

   * - ``anonymous``
     - Boolean
     - Applies only to courses that allow discussion posts that are anonymous
       to all other users.

       'true' only if the user selected the **post anonymously** check box.

   * - ``anonymous_to_peers``
     - Boolean
     - Applies only to courses that allow discussion posts that are anonymous
       to other students. The username of the thread creator is visible only
       to users who have discussion management privileges.

       'true' only if the user selected the **post anonymously to classmates**
       check box.

   * - ``body``
     - string
     - The text supplied for the new post.      
       
       Also present for ``edx.forum.response.created`` and
       ``edx.forum.comment.created`` events.

   * - ``category_id``
     - string
     - Identifier for the specific discussion component or top-level,
       course-wide discussion.

       Also present for ``edx.forum.response.created`` and
       ``edx.forum.comment.created`` events.  

   * - ``category_name``
     - string
     - The display name for the specific discussion component or top-level,
       course-wide discussion.

       Also present for ``edx.forum.response.created`` and
       ``edx.forum.comment.created`` events.

   * - ``commentable_id``
     - string
     - Identifier for the specific discussion component or top-level,
       course-wide discussion. Duplicates the ``category_id``.

       Also present for ``edx.forum.response.created`` and
       ``edx.forum.comment.created`` events.

   * - ``group_id``
     - string
     - The numeric ID of the cohort to which the contribution is restricted,
       or ``null`` if the contribution is not restricted to a specific cohort.

   * - ``id``
     - string
     - A unique identifier for this forum contribution.

       Also present for ``edx.forum.response.created`` and
       ``edx.forum.comment.created`` events.

   * - ``options``
     - dictionary
     - Contains the ``followed`` Boolean, which identifies whether the user
       elected to track the responses that others make to this post.

       Also present for ``edx.forum.response.created`` and
       ``edx.forum.comment.created`` events.

   * - ``team_id``
     - string
     - If the thread is part of a team discussion within a course, this field
       identifies the team that the thread was created in. For more
       information about events for teams, see :ref:`student_teams_events`.

   * - ``thread_type``
     - string
     - The person who creates the thread specifies either 'discussion' or
       'question' to characterize the purpose of the post.

   * - ``title``
     - string
     - The brief descriptive text supplied to identify the post.

   * - ``truncated``
     - Boolean
     - 'true' only if the post was longer than 2000 characters, which is the
       maximum included in the event.

       Also present for ``edx.forum.response.created`` and
       ``edx.forum.comment.created`` events.

   * - ``url``
     - string
     - The escaped URL of the page the user was visiting when this event was
       emitted.

       Also present for ``edx.forum.response.created`` and
       ``edx.forum.comment.created`` events.

   * - ``user_course_roles``
     - array
     - Identifies the course-level 'Instructor' (that is, Admin) or 'Staff'
       privilege assigned to the user. No value is reported for students.

       Also present for ``edx.forum.response.created`` and
       ``edx.forum.comment.created`` events.

   * - ``user_forums_roles``
     - array
     - Identifies a user who does not have discussion management privileges as
       a 'Student'. Identifies users who have discussion management privileges
       as a course 'Community TA', 'Moderator', or 'Administrator'. Also
       present for ``edx.forum.response.created`` and
       ``edx.forum.comment.created`` events.


.. _ora2:

======================================
Open Response Assessment Events 
======================================

This section includes descriptions of the following events. 

.. contents::  
  :local:
  :depth: 1

In an open response assessment, students review a question and then submit a
text response and, optionally, an image file. To evaluate their own and one or
more other students' responses to the questions, students use a scoring rubric
designed by the course team. For more information about open response
assessments, see `Creating a Peer Assessment`_.

**Component**: Open Response Assessments

**History:** The open response assessment feature was released in August 2014;
limited release of this feature began in April 2014.

``openassessmentblock.get_peer_submission``
********************************************

After students submit their own responses for evaluation, they use the scoring
rubric to evaluate the responses of other course participants. The server emits
this event when a response is delivered to a student for evaluation.

**Event Source**: Server

**History**: Added 3 April 2014.

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``course_id``
     - string
     - The identifier of the course that includes this assessment. For open
       response assessment problems, the course ID is stated in
       {org}/{course}/{run} format.

       (For courses created after mid-2014, the course ID is converted to this
       format for open response assessment problems only.)

   * - ``item_id``
     - string
     - The i4x:// style locator that identifies the problem in the course. 
   * - ``requesting_student_id``
     - string
     - The course-specific anonymized user ID of the student who requested the
       response.
   * - ``submission_returned_uuid``
     - string
     - The unique identifier of the response that the student retrieved for
       assessment. 

       If no assessment is available, this is set to "None".

       
``openassessmentblock.peer_assess`` and ``openassessmentblock.self_assess``
****************************************************************************

The server emits this event when a student either submits an assessment of a
peer's response or submits a self-assessment of her own response.

**Event Source**: Server

**History**: Added 3 April 2014.

``event`` **Member Fields**:

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``feedback``
     - string
     - The student's comments about the submitted response.
   * - ``parts: [criterion, option, feedback]``
     - array
     - The ``parts`` field contains member fields for each ``criterion`` in the
       rubric, the ``option`` that the student selected for it, and any
       ``feedback`` comments that the student supplied. 

       These member fields are repeated in an array to include all of the
       rubric's criteria.

       * ``criterion`` (object) contains ``points possible`` and ``name``
         member fields.
       * ``option`` (string).
       * ``feedback`` (string).

       When the only criterion in the rubric is student feedback, ``points
       possible`` is 0 and the ``option`` field is not included.
       
   * - ``rubric``
     - dictionary
     - This field contains the member field ``contenthash``, which identifies
       the rubric that the student used to assess the response.
   * - ``scored_at``
     - datetime
     - Timestamp for when the assessment was submitted.
   * - ``scorer_id``
     - string
     - The course-specific anonymized user ID of the student who submitted this
       assessment.
   * - ``score_type``
     - string
     - "PE" for a peer evaluation, "SE" for a self evaluation.
   * - ``submission_uuid``
     - string
     - The unique identifier for the submitted response.

``openassessmentblock.submit_feedback_on_assessments``
******************************************************************

The server emits this event when a student submits a suggestion, opinion, or
other feedback about the assessment process.

**Event Source**: Server

**History**: Added 3 April 2014.

``event`` **Member Fields**:

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``feedback_text``
     - string
     - The student's comments about the assessment process.
   * - ``options``
     - array
     - The label of each check box option that the student selected to evaluate
       the assessment process.
   * - ``submission_uuid``
     - string
     - The unique identifier of the feedback.

``openassessmentblock.create_submission``
******************************************

The server emits this event when a student submits a response. The same event
is emitted when a student submits a response for peer assessment or for self
assessment.

**Event Source**: Server

**History**: Added 3 April 2014.

``event`` **Member Fields**:

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``answer``
     - dictionary
     - This field contains a ``text`` (string) member field for the response. 
       
       For responses that also include an image file, this field contains a
       ``file_upload_key`` (string) member field with the AWS S3 key that
       identifies the location of the image file on the Amazon S3 storage
       service. This key is provided for reference only.

   * - ``attempt_number``
     - int
     - This value is currently always set to 1.
   * - ``created_at``
     - datetime
     - Timestamp for when the student submitted the response.
   * - ``submitted_at``
     - datetime
     - Timestamp for when the student submitted the response. This value is
       currently always the same as ``created_at``.
   * - ``submission_uuid``
     - string
     - The unique identifier of the response.

``openassessmentblock.save_submission``
****************************************

The server emits this event when a student saves a response. Students
save responses before they submit them for assessment.

**Event Source**: Server

**History**: Added 3 April 2014.

``event`` **Member Fields**:

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``saved_response``
     - dictionary
     - This field contains a ``text`` (string) member field for the response. 
       
       For responses that also include an image file, this field contains a
       ``file_upload_key`` (string) member field with the AWS S3 key that
       identifies the location of the image file on the Amazon S3 storage
       service.


``openassessment.student_training_assess_example``
******************************************************************

The server emits this event when a student submits an assessment for an
example response. To assess the example, the student uses a scoring rubric
provided by the course team. These events record the options the student
selected to assess the example and identifies any criteria that the student
scored differently than the course team.

**Event Source**: Server

**History**: Added 6 August 2014.

``event`` **Member Fields**:

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``corrections``
     - object
     - A set of name/value pairs that identify criteria for which the student
       selected a different option than the course team, in the format
       ``criterion_name: course-team-defined_option_name``.
   * - ``options_selected``
     - object
     - A set of name/value pairs that identify the option that the student
       selected for each criterion in the rubric, in the format
       ``'criterion_name': 'option_name'``.
   * - ``submission_uuid``
     - string
     - The unique identifier of the response. Identifies the student who
       is undergoing training.

``openassessment.upload_file``
*********************************

The browser emits this event when a student successfully uploads an image file
as part of a response. Students complete the upload process before they submit
the response.

**Event Source**: Browser

**History**: Added 6 August 2014.

``event`` **Member Fields**:

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``fileName``
     - string
     - The name of the uploaded file, as stored on the student's client
       machine.
   * - ``fileSize``
     - int
     - The size of the uploaded file in bytes. Reported by the student's
       browser.
   * - ``fileType``
     - string
     - The MIME type of the uploaded file. Reported by the student's browser.


.. _Poll and Survey Events:

===========================
Poll and Survey Events
===========================

This section describes events emitted by the poll and survey XBlocks. 

.. contents::  
  :local:
  :depth: 1

**History**: Added 8 Jul 2015.

``xblock.poll.submitted``
************************************

The server emits an ``xblock.poll.submitted`` event each time a user submits a
response to a poll.

**Event Source**: Server

``event`` **Member Fields**:

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``url_name``
     - string
     - The unique location identifier for the poll XBlock.
   * - ``choice``
     - string
     - The unique internal identifier for the response that the user submitted.


``xblock.poll.view_results``
************************************

The server emits an ``xblock.poll.view_results`` event when a tally of the
responses to a poll is displayed to a user. For a poll that has the **Private
Results** option set to False, the tally appears after a user submits a
response.

**Event Source**: Server

``event`` **Member Fields**: None

``xblock.survey.submitted``
************************************

The server emits an ``xblock.survey.submitted`` event each time a user submits
responses to a survey.

**Event Source**: Server

``event`` **Member Fields**:

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``url_name``
     - string
     - The unique location identifier for the survey XBlock.
   * - ``choices``
     - object
     - Name/value pairs that identify each question in the survey and the
       responses that the user selected, in the format 
       ``"question_name": "'response_name"``.


``xblock.survey.view_results``
************************************

The server emits an ``xblock.survey.view_results`` event when a matrix of
survey response percentages is displayed to a user. For surveys that have the
**Private Results** option set to False only, the matrix appears after a user
submits survey responses.

**Event Source**: Server

``event`` **Member Fields**: None

.. _content:

===========================
Third-Party Content Events
===========================

This section includes descriptions of the following events. 

* ``edx.googlecomponent.calendar.displayed`` 
* ``edx.googlecomponent.document.displayed``

EdX courses can include components that present content that is hosted by a
third party. The server emits events when third-party content is shown to
students.

``edx.googlecomponent.calendar.displayed`` and ``edx.googlecomponent.document.displayed``
*********************************************************************************************

The server emits an ``edx.googlecomponent.calendar.displayed`` event when a
Google Calendar component is shown in the LMS. The server emits an
``edx.googlecomponent.document.displayed`` event when a Google Drive file,
such as a document, spreadsheet, or image, is shown in the LMS.

For more information about adding Google calendars or Google Drive files
to a course, see `Creating Exercises and Tools`_.

**Event Source**: Server

**History**: Added 5 Mar 2015.

``event`` **Member Fields**:

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``displayed_in``
     - string
     - 'img' for Google Drive image files. 
       
       'iframe' for Google Calendars and for Google Drive files of other
       types.

   * - ``url``
     - string
     - The URL of the image file or of the file loaded by the iFrame.

.. _AB_Event_Types:

========================================
Testing Events for Content Experiments
========================================

This section includes descriptions of the following events. 

* ``assigned_user_to_partition``
* ``child_render``

Course authors can configure course content to present modules that contain
other modules. Content experiments, also known as A/B or split tests, use this
structure. For example, a parent module can include two child modules that
contain content that differs in some way for comparison testing. 

* Internally, a *partition* defines the type of experiment: comparing the
  effectiveness of video alone to text alone, for example. A course can include
  any number of modules that have the same partition or experiment type.

* For each partition, students are randomly assigned to a *group*. The group
  determines which content, either video or text in this example, is shown by
  every module with that partitioning.

* Students are assigned to groups randomly. Assignment to a group takes place
  when student navigation through the course requires data from that module.
  For example, one student is assigned to a group when he visits the course
  progress page, while another student is assigned to a group when she visits a
  course component that is the parent module of a content experiment. Based on
  this random group assignment, the content of just one of the two child
  modules is shown to the student.

* For investigations into which students in each group actually interacted with
  tested content, review the events for the behavior you want to learn about.
  For example, review the students' ``play_video`` ,
  ``textbook.pdf.page.navigated``, or ``problem_check`` events.

The events that follow apply to modules that are set up to randomly assign
students to groups so that different content can be shown to the different
groups. 

For more information about how course teams add content experiments to their
courses, see `Creating Content Experiments`_.

**History**: These events were added on 12 Mar 2014.

``assigned_user_to_partition``
*********************************

When a student views a module that is set up to test different child modules,
the server checks the ``user_api_usercoursetag`` table for the student's
assignment to the relevant partition, and to a group for that partition. 

* The partition ID is the ``user_api_usercoursetag.key``.

* The group ID is the ``user_api_usercoursetag.value``.

If the student does not yet have an assignment, the server emits an
``assigned_user_to_partition`` event and adds a row to the
``user_api_usercoursetag`` table for the student. See
:ref:`user_api_usercoursetag`.

.. note:: After this event is emitted, the common ``context`` field in all 
 subsequent events includes a ``course_user_tags`` member field with the
 student's assigned partition and group.

**Component**: Split Test

**Event Source**: Browser

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``group_id``
     - integer
     - Identifier of the group.
   * - ``group_name``
     - string
     - Name of the group. 
   * - ``partition_id``
     - integer
     - Identifier for the partition, in the format
       ``xblock.partition_service.partition_ID`` where ID is an integer.
   * - ``partition_name``
     - string
     - Name of the partition.

``child_render``
*********************************

When a student views a module that is set up to test different content using
child modules, the server emits a ``child_render`` event to identify
the child module that was shown to the student.

**Component**: Split Test

**Event Source**: Server

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``child_id``
     - string
     - ID of the module that was displayed to the student. 
       
       **History**: Renamed on 16 Oct 2014 from ``child-id`` to ``child_id``.
       

.. _student_cohort_events:

==========================
Student Cohort Events
==========================

This section includes descriptions of the following events. 

* ``edx.cohort.created``
* ``edx.cohort.user_added``
* ``edx.cohort.user_removed``

For information about including student cohorts in a course, see `Including
Student Cohorts`_ in the *Building and Running an edX Course* guide.

``edx.cohort.created``
*********************************

When a course team or the system creates a cohort, the server emits an
``edx.cohort.created`` event. Cohorts can be created manually by members of the
course team. The system automatically creates the default cohort and any
cohorts that are defined by the ``auto_cohort_groups`` advanced setting when
they are needed (for example, when a student is assigned to one of those
cohorts).

Additional events are emitted when members of the course team interact with the
Instructor Dashboard to create a cohort. See
:ref:`instructor_cohort_events`.

**Event Source**: Server

**History** Added 7 Oct 2014.

``event`` **Member Fields**:

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``cohort_id``
     - integer
     - The numeric ID of the cohort.
   * - ``cohort_name``
     - string
     - The display name of the cohort.

``edx.cohort.user_added``
*********************************

When a user is added to a cohort, the server emits an 
``edx.cohort.user_added`` event. Members of the course team can add users to
cohorts individually or by uploading a .csv file of student cohort
assignments. The system automatically adds a user to the default cohort or a
cohort included in the course's ``auto_cohort_groups`` setting if a user who
has not yet been assigned to a cohort accesses course content.

Additional events are emitted when members of the course team interact with the
Instructor Dashboard to add a user to a cohort. See
:ref:`instructor_cohort_events`.

**Event Source**: Server

**History** Added 7 Oct 2014.

``event`` **Member Fields**:

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``cohort_id``
     - integer
     - The numeric ID of the cohort.
   * - ``cohort_name``
     - string
     - The display name of the cohort.
   * - ``user_id``
     - integer
     - The numeric ID (from ``auth_user.id``) of the added user.

``edx.cohort.user_removed``
*********************************

When a course team member changes the cohort assignment of a user on the
Instructor Dashboard, the server emits an ``edx.cohort.user_removed`` event.

**Event Source**: Server

**History** Added 7 Oct 2014.

``event`` **Member Fields**:

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``cohort_id``
     - integer
     - The numeric ID of the cohort.
   * - ``cohort_name``
     - string
     - The display name of the cohort.
   * - ``user_id``
     - integer
     - The numeric ID (from ``auth_user.id``) of the removed user.


.. _student_teams_events:

==========================
Teams-Related Events
==========================

This section includes descriptions of the following events, which are
generated if a course includes teams, and learners or course team members
perform particular teams-related actions. This list includes both student
events and course team events, because some of these events are triggered by
actions that can be performed both by students and course staff (with the
Staff, Admin, Discussion Admin or Discussion Moderator roles), or by students
with special roles such as Community TAs.

This section presents teams-related events alphabetically. Typically, the
first event produced when teams are included in a course is the
``edx.team.created`` event.

.. note:: The Teams feature is in limited release. For more information,
   contact your edX Partner Manager. For Open edX sites, contact your system
   administrator.

.. contents:: 
  :local:
  :depth: 1


For information about including teams in a course, see `Teams Setup`_ in the
*Building and Running an edX Course* guide.


.. _edx_team_activity_updated:

``edx.team.activity_updated``
*********************************

When team discussion activity has occurred on a team, including a team member
posting, editing posts, commenting, responding, endorsing, and so on), the
server emits an ``edx.team.activity_updated`` event. 

The definition of activity that would trigger this event does not include
changes in team membership. 

**Event Source**: Server

**History** Added 16 Sept 2015.

``event`` **Member Fields**:


In addition to the :ref:`common<context>` ``context`` member fields, this
event type also includes the following ``event`` member field.

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``team_id``
     - string
     - The identifier for the team.


.. _edx_team_changed:

``edx.team.changed``
*********************************

When a team's information is edited, the server emits one
``edx.team.team_changed`` event for each modified field.

**Event Source**: Server

**History** Added 16 Sept 2015.

``event`` **Member Fields**:

In addition to the :ref:`common<context>` ``context`` member fields, this
event type also includes the following ``event`` member fields.

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``field``
     - string
     - The name of the field within the team's details that was modified such
       as team name, description, primary country, or primary language.
   * - ``new``
     - string
     - The value of the field after the modification. If this value is longer
       than 1250 characters, the string is truncated, ``...`` is added at the
       end of the string, and this field is included in the ``truncated``
       array.
   * - ``old``
     - string
     - The value of the field before the modification. If this value is longer
       than 1250 characters, the string is truncated, ``...`` is added at the
       end of the string, and this field is included in the ``truncated``
       array.  
   * - ``truncated``
     - array
     - The ``truncated`` event field is an array of the ``old`` and ``new``
       fields that have been truncated.

The ``edx.team.changed`` event also includes the following ``event`` member
field.

* ``team_id``

This field serves the same purpose for this event as it does for the
:ref:`edx_team_activity_updated` event.


``edx.team.created``
*********************************

When a team is created, either by a course team member or by a learner, the
server emits an ``edx.team.created`` event.

**Event Source**: Server

**History** Added 16 Sept 2015.

``event`` **Member Fields**:

In addition to the :ref:`common<context>` ``context`` member fields, this
event type also includes the following ``event`` member field.

This field serves the same purpose for this event as it does for the
:ref:`edx_team_activity_updated` event.

* ``team_id``


``edx.team.deleted``
*********************************

When a team is deleted, the server emits an ``edx.team.deleted`` event. Course
team members who have any of the **Staff**, **Admin**, **Discussion Admin**,
**Discussion Moderator**, or **Community TA** roles can delete teams.

**Event Source**: Server

**History** Added 16 Sept 2015.

``event`` **Member Fields**:

In addition to the :ref:`common<context>` ``context`` member fields, this
event type also includes the following ``event`` member field.

This field serves the same purpose for this event as it does for the
:ref:`edx_team_activity_updated` event.

* ``team_id``


``edx.team.learner_added``
*********************************

When a user joins a team or is added by someone else, the server emits an
``edx.team.learner_added`` event.

**Event Source**: Server

**History** Added 16 Sept 2015.

``event`` **Member Fields**:

In addition to the :ref:`common<context>` ``context`` member fields, this
event type also includes the following ``event`` member fields.


.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``add_method``
     - string
     - The method by which the user joined the team. Possible values are
       ``added_on_create``, ``joined_from_team_view``, or
       ``added_by_another_user``.
   * - ``user_id``
     - string
     - The identifier for the user who joined or was added to the team.  

The ``edx.team.learner_added`` event also includes the following ``event``
member field. 

* ``team_id``

This field serves the same purpose for this event as it does for the
:ref:`edx_team_activity_updated` event.



``edx.team.learner_removed``
*********************************

When a user leaves a team or is removed by someone else, the server emits an
``edx.team.learner_deleted`` event. This event is also triggered when a team
is deleted, because all members are removed when a team is deleted.

Course team members who have any of the **Staff**, **Admin**, **Discussion
Admin**, **Discussion Moderator**, or **Community TA** roles can remove
learners from teams.

**Event Source**: Server

**History** Added 16 Sept 2015.

``event`` **Member Fields**:

In addition to the :ref:`common<context>` ``context`` member fields, this
event type also includes the following ``event`` member fields.

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``remove_method``
     - string
     - The method by which the user was removed from the team. Possible
       values are ``self_removal``, ``team_deleted``, or ``removed_by_admin``.
   * - ``user_id``
     - string
     - The identifier for the user who left or was removed from the team.

The ``edx.team.learner_removed`` event also includes the following ``event``
member field. 

* ``team_id``

This field serves the same purpose for this event as it does for the
:ref:`edx_team_activity_updated` event.   


``edx.team.page_viewed``
*********************************

When a user views any page with a unique URL under the **Teams** page in the
courseware, the server emits an ``edx.team.page_viewed`` event.

**Event Source**: Server

**History** Added 16 Sept 2015.

``event`` **Member Fields**:

In addition to the :ref:`common<context>` ``context`` member fields, this
event type also includes the following ``event`` member fields.

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details  
   * - ``page_name``  
     - string
     - The name of the page that was viewed. Possible values are: ``browse``,
       ``edit-team``, ``my-teams``, ``new-team``, ``search teams``, ``single-
       team``, and ``single-topic``.
   * - ``topic_id``
     - string
     - The identifier of the topic related to the page that was viewed. This
       value is set to ``null`` if a topic is not applicable to the page that
       was viewed, or if the topic does not exist.


The ``edx.team.page_viewed`` event also includes the following ``event``
member field. 

* ``team_id``

This field serves the same purpose for this event as it does for the
:ref:`edx_team_activity_updated` event. For the ``edx.team.page_viewed`` event,
the value of this field is set to ``null`` if the page that was viewed has no
applicable team, or if a team does not exist.


``edx.team.searched``
*********************************

When a user performs a search for teams from the topic view under the
**Teams** page of the courseware, the server emits an ``edx.team.searched``
event.

**Event Source**: Server

**History** Added 16 Sept 2015.

``event`` **Member Fields**:

In addition to the :ref:`common<context>` ``context`` member fields, this
event type also includes the following ``event`` member fields.

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``number_of_results``
     - integer
     - The count of results that matched the search text.  
   * - ``search_text``
     - string
     - The text or keywords used in the search.
   * - ``topic_id``
     - string
     - The identifier for the topic under which this search for teams was
       performed. 



.. Commenting out badging events; add back when Badging supported on edx.org

  .. _badging_events:

  =================================
  Badging Events 
  =================================

  This section includes descriptions of the following events related to badges,
  which are created when learners have achieved some course milestone, usually
  the awarding of a course certificate. Badges are created automatically when
  certificates are generated. A badge is uniquely identifiable by its assertion
  information. A badge assertion represents a badge being awarded to a learner,
  and describes the following three items.

       * Who the badge was awarded to.
       * What the badge represents (for example, course identifier, enrollment mode).
       * Who issued the badge (the issuing organization).

      When learners earn badges, they can download a badge image and share it on
      social networks or on badge display sites such as Mozilla Backpack. When
      other parties visit the shared badge links, they can view information that
      gives evidence of the learner's achievement. 


      * ``edx.badge.assertion.created`` 
      * ``edx.badge.assertion.shared`` 
      * ``edx.badge.assertion.evidence_visited``


      ``edx.badge.assertion.created``
      *********************************

      When a badge is created that associates a specific learner with a specific
      achievement, the server emits an ``edx.badge.assertion.created`` event.

      **Event Source**: Server

      **History** Added 8 June 2015.

      ``event`` **Member Fields**:

      .. list-table::
         :widths: 15 15 60
         :header-rows: 1

         * - Field
           - Type
           - Details
         * - ``assertion_id``
           - integer
           - The unique ID of the BadgeAssertion object.
         * - ``assertion_image_url``
           - string
           - The URL of an image file of the badge that includes badge assertion
             information in the header. These files can serve to verify the user's
             accomplishment and can be easily shared.
         * - ``assertion_json_url``
           - string
           - The URL of a JSON object containing the badge assertion information.
         * - ``course_id``
           - string
           - The course associated with this badge. 
         * - ``enrollment_mode``
           - string
           - The course enrollment mode associated with this badge.
         * - ``issuer``
           - string
           - The URL of the badge issuer's web site.
         * - ``user_id``
           - integer
           - The numeric ID of the learner who earned this badge.    


      ``edx.badge.assertion.shared``
      *********************************

      When a learner downloads a badge that she has earned for the purpose of
      sharing it on social media, the server emits an
      ``edx.badge.assertion.shared`` event.

      **Event Source**: Browser

      **History** Added 8 June 2015.

      ``event`` **Member Fields**:

      The ``edx.badge.assertion.shared`` event includes many of the same ``event``
      member fields that are described for the ``edx.badge.assertion.created``
      event. The following member fields serve the same purpose for
      ``edx.badge.assertion.shared`` as they do for
      ``edx.badge.assertion.created``.

      * ``assertion_id``
      * ``assertion_image_url``
      * ``assertion_json_url``
      * ``course_id``
      * ``enrollment_mode``
      * ``issuer``
      * ``user_id``


      The following additional ``event`` member field applies specifically to
      ``edx.badge.assertion.shared`` events.

      .. list-table::
         :widths: 15 15 60
         :header-rows: 1

         * - Field
           - Type
           - Details
         * - ``social_network``
           - string
           - The social network to which the badge is shared.


      ``edx.badge.assertion.evidence_visited``
      *****************************************
       
      Each badge contains assertion information that includes an "evidence" field.
      When badges are displayed on sites such as Mozilla Backpack, the evidence
      field is used to provide a link to evidence that confirms the badge owner's
      achievement, usually a certificate.
       
      When other users visit social networks or a site such as Mozilla Backpack and
      use a badge's evidence link to view a badge owner's certificate, the server
      emits an ``edx.badge.assertion.evidence_visited`` event.

      **Event Source**: Browser

      **History** Added 8 June 2015.

      ``event`` **Member Fields**:

      The ``edx.badge.assertion.evidence_visited`` event includes all of the same
      ``event`` member fields that are described for the
      ``edx.badge.assertion.created`` event. The following member fields serve the
      same purpose for ``edx.badge.assertion.evidence_visited`` as they do for
      ``edx.badge.assertion.created``.

      * ``assertion_id``
      * ``assertion_image_url``
      * ``assertion_json_url``
      * ``course_id``
      * ``enrollment_mode``
      * ``issuer``
      * ``user_id``


.. _certificate_events:

=================================
Certificate Events 
=================================

This section includes descriptions of the events related to certificates, which
are awarded to qualified learners when they complete a course.

* ``edx.certificate.created`` 
* ``edx.certificate.shared`` 
* ``edx.certificate.evidence_visited``


``edx.certificate.created``
*********************************

When a certificate is generated, a record is created in the
``certificates_generatedcertificate`` table, triggering an
``edx.certificate.created`` event. For details, see
:ref:`certificates_generatedcertificate`.

**Event Source**: Server

**History** Added 2 September 2015.

``event`` **Member Fields**:

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details

   * - ``certificate_id``
     - string
     - The ``verify.uuid`` value from the
       ``certificates_generatedcertificate`` table. This string appears at the
       bottom of each certificate.
   * - ``certificate_url``
     - string
     - The URL for the certificate web page.  
   * - ``course_id``
     - string
     - The course for which this certificate is issued. 
   * - ``enrollment_mode``
     - string
     - The course enrollment mode associated with this certificate.
   * - ``generation_mode``
     - string
     - Indicates whether this certificate was generated for all learners in a
       course by a batch command, or whether a learner generated her own
       certificate. Possible values are "batch" and "self".
   * - ``user_id``
     - integer
     - The numeric ID of the learner who earned this certificate.    


``edx.certificate.shared``
*********************************

When a learner shares the URL for her certificate on a social media web site,
the server emits an ``edx.certificate.shared`` event.

**Event Source**: Browser

**History** Added 2 September 2015.

``event`` **Member Fields**:

The ``edx.certificate.shared`` event includes many of the same ``event``
member fields that are described for the ``edx.certificate.created`` event.
The following member fields serve the same purpose for
``edx.certificate.shared`` as they do for `edx.certificate.created`_.

* ``certificate_id``
* ``certificate_url``
* ``course_id``
* ``enrollment_mode``
* ``user_id``

The following additional ``event`` member field applies specifically to
``edx.certificate.shared`` events.

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``social_network``
     - string
     - The social network to which the certificate is shared, such as
       "LinkedIn", "Facebook", or "Twitter".


``edx.certificate.evidence_visited``
**************************************
 
When a learner shares her certificates on social network sites such as
LinkedIn, and the link back to the certificate is followed by some visitor to
that social network site, the server emits an
``edx.certificate.evidence_visited`` event.

**Event Source**: Browser

**History** Added 2 September 2015.

``event`` **Member Fields**:

The ``edx.certificate.evidence_visited`` event includes all of the same
``event`` member fields that are described for the ``edx.certificate.created``
event. The following member fields serve the same purpose for
``edx.certificate.evidence_visited`` as they do for
``edx.certificate.created``.

* ``certificate_id``
* ``certificate_url``
* ``course_id``
* ``enrollment_mode``
* ``user_id``


The following additional ``event`` member fields apply specifically to
``edx.certificate.evidence_visited`` events.

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details  
   * - ``social_network``
     - string
     - The social network to which the certificate is shared, such as
       "LinkedIn", "Facebook", or "Twitter".
   * - ``source_url``
     - string
     - The URL of the web site where the certificate evidence link was
       selected. This URL is the same as the URI in the ``context.referer``
       field. For details, see `referer field`_.


.. _ora:

============================================
Open Response Assessment Events (Deprecated)
============================================

The events described in this section recorded interactions with the prototype
implementation of open response assessment (ORA 1) problem types. EdX
deprecated this feature in May 2014, and removed the ability to add a new ORA 1
assignment to courses in December 2014.

For more information about events for the current implementation of open
response assessments, see :ref:`ora2`.

``oe_hide_question`` and ``oe_show_question``
******************************************************************

The browser emits ``oe_hide_question`` and ``oe_show_question`` events when the
user hides or redisplays a combined open-ended problem.

**History**: These events were previously named ``oe_hide_problem`` and
``oe_show_problem``.

**Component**: Combined Open-Ended

**Event Source**: Browser

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``location``
     - string
     - The location of the question whose prompt is being shown or hidden.

``rubric_select`` 
*********************************

**Component**: Combined Open-Ended

**Event Source**: Browser

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``category``
     - integer
     - Rubric category selected.
   * - ``location``
     - string
     - The location of the question whose rubric is being selected. 
   * - ``selection``
     - integer
     - Value selected on rubric. 

``oe_show_full_feedback`` and ``oe_show_respond_to_feedback``
******************************************************************

**Component**: Combined Open-Ended

**Event Source**: Browser

``event`` **Member Fields**: None.

``oe_feedback_response_selected`` 
*********************************

**Component**: Combined Open-Ended

**Event Source**: Browser

``event`` **Member Fields**:

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``value``
     - integer
     - Value selected in the feedback response form.

``peer_grading_hide_question`` and ``peer_grading_show_question``
******************************************************************

The browser emits ``peer_grading_hide_question`` and 
``peer_grading_show_question`` events when the user hides or redisplays a
problem that is peer graded.

**History**: These events were previously named ``peer_grading_hide_problem``
and ``peer_grading_show_problem``.

**Component**: Peer Grading

**Event Source**: Browser

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``location``
     - string
     - The location of the question whose prompt is being shown or hidden.

``staff_grading_hide_question`` and ``staff_grading_show_question``
********************************************************************

The browser emits ``staff_grading_hide_question`` and 
``staff_grading_show_question`` events when the user hides or redisplays a
problem that is staff graded.

**History**: These events were previously named ``staff_grading_hide_problem``
and ``staff_grading_show_problem``.

**Component**: Staff Grading

**Event Source**: Browser

``event`` **Member Fields**: 

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``location``
     - string
     - The location of the question whose prompt is being shown or hidden.

.. _Instructor_Event_Types:

*************************
Course Team Events
*************************

This section lists events that are generated by interactions with the
Instructor Dashboard in the LMS.

The schema definitions for events include only the JSON fields that are common
to all events follow.

* ``dump-answer-dist-csv``
* ``dump-graded-assignments-config``
* ``dump-grades``
* ``dump-grades-csv``
* ``dump-grades-csv-raw``
* ``dump-grades-raw``
* ``list-beta-testers``
* ``list-instructors``
* ``list-staff``
* ``list-students``

For more information about the common fields, see :ref:`common`.

Course team events that have additional ``context`` or ``event`` member fields
follow.

.. contents:: Section Contents 
  :local:
  :depth: 1

======================================================
``add_instructor`` and ``remove_instructor`` 
======================================================

.. previously a comma-separated list; "Rows identical after the second column" (which means the name and description columns) were combined

**Component**: Instructor Dashboard

**Event Source**: Server

``event`` **Member Fields**: 

.. list-table::
   :widths: 40 40
   :header-rows: 1

   * - Field
     - Type
   * - ``instructor``
     - string


.. _rescore_student:

===================================================================
 ``delete-student-module-state`` and ``rescore-student-submission``
===================================================================

.. previously a comma-separated list; "Rows identical after the second column" (which means the name and description columns) were combined

**Component**: Instructor Dashboard

**Event Source**: Server

``event`` **Member Fields**: 

.. list-table::
   :widths: 40 40
   :header-rows: 1

   * - Field
     - Type
   * - ``course``
     - string
   * - ``problem``
     - string
   * - ``student``
     - string


======================================================
``edx.instructor.report.downloaded`` 
======================================================

The browser emits an  ``edx.instructor.report.downloaded`` event when the user
clicks a report link on the Instructor Dashboard to download a report.

**History**: Added 8 May 2015.

**Component**: Instructor Dashboard

**Event Source**: Browser

``event`` **Member Fields**: 

.. list-table::
   :widths: 20 20 40
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``report_url``
     - string
     - The URL to the report file.  


======================================================
``edx.instructor.report.requested`` 
======================================================

The server emits an  ``edx.instructor.report.requested`` event when the user
clicks to request the generation of a report on the Instructor Dashboard. 

**History**: Added 8 May 2015.

**Component**: Instructor Dashboard

**Event Source**: Server

``event`` **Member Fields**: 

.. list-table::
   :widths: 20 20 40
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``report_type``
     - string
     - The type of report that was requested.


.. _progress:

======================================================
``get-student-progress-page`` 
======================================================

**Component**: Instructor Dashboard

**Event Source**: Server

``event`` **Member Fields**: 

.. list-table::
   :widths: 40 40
   :header-rows: 1

   * - Field
     - Type
   * - ``course``
     - string
   * - ``instructor``
     - string
   * - ``student``
     - string


.. _rescore_all:

======================================================
``rescore-all-submissions`` and ``reset-all-attempts``
======================================================

**Component**: Instructor Dashboard

**Event Source**: Server

``event`` **Member Fields**: 

.. list-table::
   :widths: 40 40
   :header-rows: 1

   * - Field
     - Type
   * - ``course``
     - string
   * - ``problem`` 
     - string


.. _reset_attempts:

======================================================
``reset-student-attempts``
======================================================

**Component**: Instructor Dashboard

**Event Source**: Server

``event`` **Member Fields**: 

.. list-table::
   :widths: 40 40
   :header-rows: 1

   * - Field
     - Type
   * - ``course``
     - string
   * - ``old_attempts``
     - string
   * - ``problem``
     - string 
   * - ``student``
     - string




.. _list_forum:

======================================================
List Discussion Team Events
======================================================

.. previously a comma-separated list; "Rows identical after the second column" (which means the name and description columns) were combined

* ``list-forum-admins``

* ``list-forum-mods``

* ``list-forum-community-TAs``

**Component**: Instructor Dashboard

**Event Source**: Server

``event`` **Member Fields**: 

.. list-table::
   :widths: 40 40
   :header-rows: 1

   * - Field
     - Type
   * - ``course``
     - string

.. _forum:

======================================================
Manage Discussion Team Events   
======================================================

.. previously a comma-separated list; "Rows identical after the second column" (which means the name and description columns) were combined

* ``add-forum-admin``

* ``remove-forum-admin``

* ``add-forum-mod``

* ``remove-forum-mod``

* ``add-forum-community-TA``

* ``remove-forum-community-TA``

**Component**: Instructor Dashboard

**Event Source**: Server

``event`` **Member Fields**: 

.. list-table::
   :widths: 40 40
   :header-rows: 1

   * - Field
     - Type
   * - ``course``
     - string
   * - ``username``
     - string

.. _histogram:

======================================================
``psychometrics-histogram-generation``
======================================================

**Component**: Instructor Dashboard

**Event Source**: Server

``event`` **Member Fields**: 

.. list-table::
   :widths: 40 40
   :header-rows: 1

   * - Field
     - Type
   * - ``problem``
     - string

.. _user_group:

======================================================
``add-or-remove-user-group``   
======================================================

**Component**: Instructor Dashboard

**Event Source**: Server

``event`` **Member Fields**: 

.. list-table::
   :widths: 40 40
   :header-rows: 1

   * - Field
     - Type
   * - ``event``
     - string
   * - ``event_name``
     - string
   * - ``user``
     - string

.. _instructor_enrollment:

=============================
Instructor Enrollment Events
=============================

In addition to the enrollment events that are generated when students enroll in
or unenroll from a course, actions by course team members also generate
enrollment events.

* When a course author creates a course, his or her user account is enrolled in
  the course and the server emits an ``edx.course.enrollment.activated`` event.

* When a user with the Admin or Staff role enrolls in a course, the
  server emits ``edx.course.enrollment.activated``. The server emits
  ``edx.course.enrollment.deactivated`` events when these users unenroll from a
  course.

* When a user with the Admin or Staff role uses the **Batch Enrollment**
  feature to enroll students or other course team members in a course, the
  server emits an ``edx.course.enrollment.activated`` event for each
  enrollment. When this feature is used to unenroll students from a course, the
  server emits a ``edx.course.enrollment.deactivated`` for each unenrollment.

  For events emitted as a result of a batch enrollment, the ``username`` and
  ``context.user_id`` identify the course team member who made the change, and
  the ``event.user_id`` identifies the student who was enrolled or unenrolled.

For details about the enrollment events, see :ref:`enrollment`.

.. _instructor_cohort_events:

=============================
Course Team Cohort Events
=============================

In addition to the cohort events that are generated when cohorts are created
and users are assigned to them (see :ref:`student_cohort_events`), actions by
course team members also generate cohort-related events.

For more information about student cohorts, see `Including Student Cohorts`_
in the *Building and Running an edX Course* guide.

``edx.cohort.creation_requested``
*********************************

When a course team member manually creates a cohort on the
Instructor Dashboard, the server emits an ``edx.cohort.creation_requested``
event.

**Event Source**: Server

**History** Added 7 Oct 2014.

``event`` **Member Fields**:

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``cohort_id``
     - integer
     - The numeric ID of the cohort.
   * - ``cohort_name``
     - string
     - The display name of the cohort.

``edx.cohort.user_add_requested``
*********************************

When a course team member adds a student to a cohort on the
Instructor Dashboard, the server emits an ``edx.cohort.user_add_requested``
event. Course team members can add students to a cohort individually, or by
uploading a .csv file of student cohort assignments.

**Event Source**: Server

**History** Added 7 Oct 2014.

``event`` **Member Fields**:

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``cohort_id``
     - integer
     - The numeric ID of the cohort.
   * - ``cohort_name``
     - string
     - The display name of the cohort.
   * - ``previous_cohort_id``
     - integer
     - The numeric ID of the cohort that the user was previously assigned to.

       Null if the user was not previously assigned to a cohort.

   * - ``previous_cohort_name``
     - string
     - The display name of the cohort that the user was previously assigned to.

       Null if the user was not previously assigned to a cohort.

   * - ``user_id``
     - integer
     - The numeric ID (from ``auth_user.id``) of the added user.






.. _Creating a Peer Assessment: http://edx.readthedocs.org/projects/edx-partner-course-staff/en/latest/exercises_tools/open_response_assessments/OpenResponseAssessments.html

.. _Creating Content Experiments: http://edx.readthedocs.org/projects/edx-partner-course-staff/en/latest/content_experiments/index.html#creating-content-experiments

.. _Including Student Cohorts: http://edx.readthedocs.org/projects/edx-partner-course-staff/en/latest/cohorts/index.html#including-student-cohorts

.. _Referer: http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.36

.. _Accept-Language: http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.4

.. _Creating Exercises and Tools: http://edx-partner-course-staff.readthedocs.org/en/latest/exercises_tools/index.html

.. _Working with Libraries: http://edx.readthedocs.org/projects/edx-partner-course-staff/en/latest/creating_content/libraries.html

.. _Working with Video Components: http://edx.readthedocs.org/projects/edx-partner-course-staff/en/latest/creating_content/create_video.html#advanced-options

.. _Adding a Pre-Roll Video to Your edX Course: http://edx.readthedocs.org/projects/edx-partner-course-staff/en/latest/creating_content/create_video.html#adding-a-pre-roll-video-to-your-edX-course

.. _Adding Hints and Feedback to a Problem: http://edx.readthedocs.org/projects/edx-partner-course-staff/en/latest/creating_content/create_problem.html#adding-hints-and-feedback-to-a-problem

.. _Teams Setup: http://draft-course-author-teams.readthedocs.org/en/latest/teams/teams_setup.html

.. note that the above Teams Course Author doc is available only in draft
.. form. As of 15 Sept 2015 the feature used in a course pilot but not
.. widely released on edx.org, so doc has not been published. When it is
.. published we need to update the link to point to docs.edx.org location.
