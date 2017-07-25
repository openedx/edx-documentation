
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

**Type:** object

**Details:**

The ``context`` field includes member fields that provide contextual
information.

* This field contains a core set of member fields that are common to all
  events.
* For certain events with additional contextual requirements, this field
  contains a set of additional member fields that are common to those events
  only.
* For any event, this field can also include one or more additional member
  fields. For more information about the ``context`` member fields for an
  event, see the description of that event later in this section.

``context`` Member Fields Common to All Events
***********************************************

The following member fields are present in the ``context`` field for all
events.

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
     - number
     - Identifies the individual who is performing the action.

.. note:: Occasionally, an event is recorded with a missing or blank
 ``context.user_id`` value. This can occur when a user logs out, or the login
 session times out, while a browser window remains open. Subsequent actions are
 logged, but the system cannot supply the user identifier. EdX recommends that
 you ignore these events during analysis.

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
     - object
     - Contains the key(s) and value(s) from the ``user_api_usercoursetag``
       table for the user. See :ref:`user_api_usercoursetag`.
   * - ``module``
     - object
     - Provides identifying information for the components involved in a
       server event.

       For example, in a server ``problem_check`` event, the ``module`` field
       indicates the problem component that the server checked successfully.
       The member fields are ``display_name`` and ``usage_key``.

       For modules that are used in a course to present content from a
       library, ``module`` also includes the ``original_usage_key`` and
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

**Type:** object

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

.. _referer_field:

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

**Details:** The username of the user who caused the event to be emitted.

.. note:: Occasionally, an event is recorded with a blank ``username``
 value. This can occur when a user logs out, or the login session times out,
 while a browser window remains open. Subsequent actions are logged, but the
 system cannot supply the user identifier. EdX recommends that you ignore these
 events during analysis.

.. include:: ../../../../links/links.rst
