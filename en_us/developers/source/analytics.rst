.. _analytics:

##############
Analytics
##############

The edX LMS and Studio are instrumented to enable tracking of metrics and
events of interest. These data can be used for educational research, decision
support, and operational monitoring.

The primary mechanism for tracking events is the `Event Tracking`_ API. It
should be used for the vast majority of cases.

=================
Event Tracking
=================

The `event-tracking`_ library aims to provide a simple API for tracking point-
in-time events. The `event-tracking documentation`_ summarizes the features
and primary use cases of the library as well as the current and future design
intent.

Emitting Events
*****************

Emitting from server-side python code::

    from eventtracking import tracker
    tracker.emit('some.event.name', {'foo': 'bar'})

Emitting from client-side JavaScript::

    Logger.log 'some.event.name', 'foo': 'bar'

.. note::
    The client-side API currently uses a deprecated library (the ``track``
     djangoapp) instead of the event-tracking library. Eventually, event-tracking
     will publish a client-side API of its own: when available, that
     API should be used instead of the ``track``-based solution. See
     :ref:`deprecated_api`.

Naming Events
==============

Event names are intended to be formatted as `.` separated strings and help
processing of related events. The structure is intended to be
`namespace.object.action`. The namespace is intended to be a `.` separated
string that helps identify the source of events and prevent events with
similar or identical objects and actions from being confused with one another.
The object is intended to be a noun describing the object that was acted on.
The action is intended to be a past tense verb describing what happened.

Examples:

    * ``edx.course.enrollment.activated``
        * Namespace: ``edx``
        * Object: ``course.enrollment``
        * Action: ``activated``

Choosing Events to Emit
========================

Consider emitting events to capture user intent. These will typically be
emitted on the client side when a user interacts with the user interface in
some way.

Consider also emitting events when models change. Most models are not append-
only and it is frequently the case that an analyst would want to see the value
of a particular field at a particular moment in time. Given that many fields
are overwritten, that information is lost unless an event is emitted when the
model is changed.

Sensitive Information
=====================

By default, event information is written to an unencrypted file on disk.
Therefore, do not include clear text passwords, credit card numbers, or other
similarly sensitive information.

Size
======

A cursory effort to regulate the size of the event is appreciated. If an event
is too large, it may be omitted from the event stream. However, do not
sacrifice the clarity of an event in an attempt to minimize size. It is much
more important that the event is clear.

Debugging Events
================

On devstack, emitted events are stored in the ``/edx/var/log/tracking.log`` log
file. This file can be useful for validation and debugging.

.. _Testing Event Emission:

Testing Event Emission
======================

It is important to test instrumentation code since regressions can have a
significant negative impact on downstream consumers of the data.

Each test can make stronger or weaker assertions about the structure and
content of various fields in the event. Tests can make assertions about
particular fields in the nested hierarchical structures that are events. This
allows them to continue to pass even if a new global field is added to all
events (for example).

Failing tests are a form of communication with future developers. A test
failure is a way for you to tell those future developers that they have
changed something that you did not expect to change, and that there are
implications that they should think about carefully before making the change.
For this reason, limit the scope of your test to details you expect to remain
constant. Specifically, for eventing, this means only asserting on the
presence and correctness of fields your code is adding, not the precise set of
fields that happen to be present in all events today.

In general, it is acceptable for events to contain "unexpected" fields. If you
add a field, most JSON parsers will accept this new field and allow the
downstream code to process the event. Since that downstream code does not know
about the new field it will simply be ignored.

For this reason, most of our tests do not actually make assertions about
unexpected fields appearing in the events, instead they focus on the fields
that they *do* expect to be present and make assertions about the values of
these fields. This enables us to add global context without having to update
hundreds (or even thousands) of tests that were making assertions about the
exact set of fields present in the event. Instead, we prefer to only have a
small number of tests fail when making a change like this. Those tests might
be making more strict assertions about the global context, for example. When a
small number of targeted tests fail, they can be more effective at
communicating the exact set of assumptions that were being made before that
have now changed.

Assertions
----------

The ``openedx.core.lib.tests.assertions.events`` module contains helper
functions that can be used to make assertions about events. The key function in
this module is ``assert_event_matches`` which allows tests to make assertions
about parts of the event. The signature looks like this::

    def assert_event_matches(expected_event, actual_event, tolerate=None):

The ``expected_event`` parameter contains the assertion that is being made. The
``actual_event`` parameter contains the complete event that was emitted. The
``tolerate`` parameter allows the test to specify the types of discrepancies
that it cares about. This allows you to be very strict in assertions about some
parts of the event and more lenient in other areas.

Here are examples that highlight the default settings for ``tolerate``.

::

    # By default, decode string values for the "event" field as JSON and compare
    # the contents with the actual event. This will not raise an error.
    assert_event_matches(
        {'event': {'a': 'b'}},
        {'event': '{"a": "b"}'}
    )

    # Ignore "unexpected" root fields. This will not raise an error even though
    # the field "foo" does not appear in the expected event.
    assert_event_matches(
        {'event_type': 'test'},
        {'event_type': 'test', 'foo': 'bar'}
    )

    # Ignore "unexpected" fields in the context. This will not raise an error
    # even though the field "foo" does not appear in the expected event context.
    assert_event_matches(
        {'event_type': 'test'},
        {'event_type': 'test', 'context': {'foo': 'bar'}}
    )

    # Overriding "tolerate" allows more strict assertions to be made.
    # This assertion will raise an error!
    assert_event_matches(
        {'event_type': 'test'},
        {'event_type': 'test', 'context': {'foo': 'bar'}},
        tolerate=[]
    )


Unit testing
------------

Test classes should inherit from
``common.djangoapps.track.tests.EventTrackingTestCase``. Additionally, some
helper assertion functions are available to help with making assertions about
events.

Here is an example of a subclass.

::

    from common.djangoapps.track.tests import EventTrackingTestCase
    from openedx.core.lib.tests.assertions.events import assert_event_matches

    class MyTestClass(EventTrackingTestCase):

        def setUp(self):
            # The setUp() of the superclass must be called
            super(MyTestClass, self).setUp()

        def test_event_emitted(self):
            my_function_that_emits_events()

            # If the above function only emits a single event, this can be used.
            actual_event = self.get_event()

            # This will assert that the "event_type" of the event is "foobar".
            # Note that it makes no assertions about any of the other fields
            # in the event.
            assert_event_matches({'event_type': 'foobar'}, actual_event)

        def test_no_event_emitted(self):

            my_function_that_does_not_emit()

            # This will fail if any events were emitted by the above function
            # call.
            self.assert_no_events_emitted()

Bok Choy Testing
----------------

Test classes should use the mixin
``common.test.acceptance.tests.helpers.EventsTestMixin``. At its core, this
mixin captures all events that are emitted while the test is running and allows
you to make assertions about those events. Below some common patterns are
outlined. By default, Bok Choy event assertions are as lenient as possible. The
tests can be made more strict by passing in ``tolerate=[]`` to indicate that an
exact match is necessary. Similarly, other flags can be passed into the
``tolerate`` parameter to tightly control the level of validation performed.

Wait for some events and make assertions about their content.

::

    def test_foobar_event_emission(self):
        emit_foobar_event()

        # This will wait for the event to be emitted. It will time out if the
        # event is not emitted quickly enough (or not emitted at all).
        actual_events = self.wait_for_events({'event_type': 'foobar'})

        # This will compare the first event emitted with the first expected
        # event, the second with the second etc.
        self.assert_events_match(
          [
            {'event': {'a': 'b'}}
          ],
          actual_events
        )

        # ``wait_for_events`` also accepts arbitrary callable functions to check
        # to see if an event "matches"
        def some_custom_event_filter(event):
            return event['event']['old_time'] > 10

        # This will return when some_custom_event_filter returns true for at
        # at least one event.
        actual_events = self.wait_for_events(some_custom_event_filter)

    def test_multiple_events(self):
        emit_several_events()

        def my_event_filter(event):
            return event['event_type'] in ('first_event', 'second_event')

        # This will wait for 2 events to match the filter defined above. Note
        # that it makes no assertions about their ordering or content.
        actual_events = self.wait_for_events(my_event_filter, number_of_matches=2)

        # This ensures that first_event was emitted before second_event and
        # checks the payload of both events.
        self.assert_events_match(
          [
            {
              'event_type': 'first_event',
              'event': {'a': 'b'}
            },
            {
              'event_type': 'second_event',
              'event': {'a': 'other'}
            }
          ],
          actual_events
        )

    def test_granular_assertion(self):

        # This foobar event is emitted first, with the "a" field set to "NOT B"
        tracker.emit('foobar', {'a': 'NOT B'})

        # A context manager can be used to ensure that the first "foobar" event
        # is ignored. It only makes assertions about the events that are emitted
        # inside this context.
        with self.assert_events_match_during(
            {'event_type': 'foobar'},
            [
              {
                'event': {'a': 'b'}
              }
            ]
        ):
            emit_foobar_event()


Documenting Events
*******************

When you add events to the platform, your PR should describe the purpose of
the event and include an example event. In addition, consider including
comments that identify the purpose of the event and its fields. Your
descriptions and examples can help assure that researchers and other members
of the open edX community understand your intent and use the events correctly.

You might find the following references helpful as you prepare your PR.

* The *edX Platform Developer's Guide* provides guidelines for `contributing
  to open edX <http://edx.readthedocs.io/projects/edx-developer-
  guide/en/latest/process/index.html>`_.

* The `edX Research
  Guide <http://edx.readthedocs.io/projects/devdata/en/latest/>`_ is a
  reference for information about emitted events that are included in the edX
  tracking logs.

Request Context Middleware
**********************************

The platform includes a middleware class that enriches all events emitted
during the processing of a given request with details about the request that
greatly simplify downstream processing. This is called the ``TrackMiddleware``
and can be found in ``edx-platform/common/djangoapps/track/middleware.py``.

Legacy Application Event Processor
**********************************

In order to support legacy analysis applications, the platform emits standard
events using ``eventtracking.tracker.emit()``. However, it uses a custom event
processor which modifies the event before saving it to ensure that the event
can be parsed by legacy systems. Specifically, it replicates some information
so that it is accessible in exactly the same way as it was before. This state
is intended to be temporary until all existing legacy systems can be altered
to use the new field locations.

=======================
Other Tracking Systems
=======================

The following tracking systems are currently used for specialized analytics.
There is some redundancy with event-tracking that is undesirable. The event-
tracking library could be extended to support some of these systems, allowing
for a single API to be used while still transmitting data to each of these
service providers. This would reduce discrepancies between the measurements
made by the various systems and significantly clarify the instrumentation.

Segment
*****************

A selection of events can be transmitted to `Segment`_ in order to take
advantage of a wide variety of analytics-related third party services such as
Mixpanel and Chartbeat. It is enabled in the LMS if the ``SEGMENT_KEY``
key is set to a valid Segment API key in the ``lms.yml`` file. Additionally,
the setting ``EVENT_TRACKING_SEGMENTIO_EMIT_WHITELIST`` in the ``lms.yml``
file can be used to specify event names that should be emitted to Segment
from normal ``tracker.emit()`` calls. Events specified in this whitelist will be
sent to both the tracking logs and Segment.  Similarly, it is enabled in Studio
if the ``SEGMENT_KEY`` key is set to a valid Segment API key in the
``studio.yml`` file.


Google Analytics
*****************

Google analytics tracks all LMS page views. It provides several useful metrics
such as common referrers and search terms that users used to find the edX web
site.

.. _deprecated_api:

Deprecated APIs
*****************

The ``track`` djangoapp contains a deprecated mechanism for emitting events.
Direct usage of ``server_track`` is deprecated and should be avoided in new
code. Old calls to ``server_track`` should be replaced with calls to
``tracker.emit()``. The celery task-based event emission and client-side event
handling do not currently have a suitable alternative approach, so they
continue to be supported.

.. _event-tracking: https://github.com/edx/event-tracking
.. _event-tracking documentation: http://event-tracking.readthedocs.io/en/latest/overview.html#event-tracking
.. _Segment: https://segment.com/
