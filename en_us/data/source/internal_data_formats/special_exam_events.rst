.. _special_exam_events:

=================================
Timed and Proctored Exam Events
=================================

.. include:: special_exam_events_overview.rst

Some special exam events are emitted when course teams develop and administer exams. For more information, see :ref:`special_exam_development_events`.

Because special exams include similiar functions and behavior, they share some
similar events. For example, the
``edx.special_exam.proctored.allowance.created``,
``edx.special_exam.practice.allowance.created``, and
``edx.special_exam.timed.allowance.created`` events include identical fields.

This section includes descriptions of the following events.

.. contents::
  :local:
  :depth: 1

.. _special_exam_attempt_created:

``edx.special_exam.proctored.attempt.created``, ``edx.special_exam.practice.attempt.created``, and ``edx.special_exam.timed.attempt.created``
************************************************************************************************************************************************

The server emits this event when a learner chooses to take a special exam.

**History**: Added 01 Dec 2015.

``event`` **Member Fields**:

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``attempt_allowed_time_limit_mins``
     - number
     - The amount of time, in minutes, that the learner has to complete
       the exam.
   * - ``attempt_code``
     - string
     - A generated identifier for the exam attempt.
   * - ``attempt_completed_at``
     - datetime
     - The UTC time stamp of the time at which the learner submitted the
       exam.
   * - ``attempt_event_elapsed_time_secs``
     - number
     - The number of seconds that passed between the time the learner started
       the exam and the time the event was emitted.
   * - ``attempt_id``
     - number
     - The primary identifier of the exam attempt.
   * - ``attempt_started_at``
     - datetime
     - The UTC time stamp of the time at which the learner began taking the
       exam.
   * - ``attempt_status``
     - string
     - The current state of the exam, for example, ``created``.
   * - ``attempt_user_id``
     - number
     - The primary identifier of the learner taking the exam.
   * - ``exam_content_id``
     - string
     - The primary identifier of the subsection that contains the exam.
   * - ``exam_default_time_limit_mins``
     - number
     - The standard amount of time, in minutes, that learners have to complete
       the exam.
   * - ``exam_id``
     - number
     - The primary identifier of the exam.
   * - ``exam_is_active``
     - Boolean
     - Indicates whether the special exam is currently available for learner
       attempts.
   * - ``exam_is_practice_exam``
     - Boolean
     - Indicates whether the special exam is a practice proctored exam.
   * - ``exam_is_proctored``
     - Boolean
     - Indicates whether the special exam is a proctored exam.
   * - ``exam_name``
     - string
     - The title of the exam in the course page, taken from the subsection
       title.


``edx.special_exam.proctored.attempt.declined``
***********************************************

The server emits this event when a learner chooses to take an exam without
proctoring.

The ``event`` fields for this event are the same as the ``event`` fields for
the ``edx.special_exam.proctored.attempt.created`` event. For more information,
see
:ref:`special_exam_attempt_created`.

**History**: Added 01 Dec 2015.

.. _special_exam_attempt_deleted:

``edx.special_exam.proctored.attempt.deleted``, ``edx.special_exam.practice.attempt.deleted``, and ``edx.special_exam.timed.attempt.deleted``
*********************************************************************************************************************************************

The server emits this event when a course team or edX platform administrator
removes an exam attempt record for an individual learner.

The ``event`` fields for this event are the same as the ``event`` fields for
the ``edx.special_exam.{special exam type}.attempt.created`` event. For more
information, see
:ref:`special_exam_attempt_created`.

**History**: Added 01 Dec 2015.

.. _special_exam_attempt_download_software_clicked:

``edx.special_exam.proctored.attempt.download_software_clicked`` and ``edx.special_exam.practice.attempt.download_software_clicked``
************************************************************************************************************************************

The server emits this event when a learner follows the link to download the
proctoring software for a proctored exam.

The ``event`` fields for this event are the same as the ``event`` fields for
the ``edx.special_exam.{special exam type}.attempt.created`` event. For more information,
see
:ref:`special_exam_attempt_created`.

**History**: Added 01 Dec 2015.

.. _special_exam_attempt_error:

``edx.special_exam.proctored.attempt.error`` and ``edx.special_exam.practice.attempt.error``
********************************************************************************************

The server emits this event when it loses the connection to the proctoring
software during a learner's exam attempt.

The ``event`` fields for this event are the same as the ``event`` fields for
the ``edx.special_exam.{special exam type}.attempt.created`` event. For more
information, see
:ref:`special_exam_attempt_created`.

**History**: Added 01 Dec 2015.

.. _special_exam_attempt_ready_to_start:

``edx.special_exam.proctored.attempt.ready_to_start`` and ``edx.special_exam.practice.attempt.ready_to_start``
**************************************************************************************************************

The server emits this event when a learner has installed the proctoring
software and is ready to begin taking a proctored exam.

The ``event`` fields for this event are the same as the ``event`` fields for
the ``edx.special_exam.{special exam type}.attempt.created`` event. For more
information, see
:ref:`special_exam_attempt_created`.

**History**: Added 01 Dec 2015.

.. _special_exam_attempt_ready_to_submit:

``edx.special_exam.proctored.attempt.ready_to_submit``, ``edx.special_exam.practice.attempt.ready_to_submit``, and ``edx.special_exam.timed.attempt.ready_to_submit``
*********************************************************************************************************************************************************************

The server emits this event when a learner has completed a proctored exam and
is prompted to submit the exam.

The ``event`` fields for this event are the same as the ``event`` fields for
the ``edx.special_exam.{special exam type}.attempt.created`` event. For more
information, see
:ref:`special_exam_attempt_created`.

**History**: Added 01 Dec 2015.

``edx.special_exam.proctored.attempt.rejected``
***********************************************

The server emits this event when a proctored exam attempt has been reviewed and
has been disqualified.

The ``event`` fields for this event are the same as the ``event`` fields for
the ``edx.special_exam.proctored.attempt.created`` event. For more information,
see
:ref:`special_exam_attempt_created`.

**History**: Added 01 Dec 2015.

``edx.special_exam.proctored.attempt.review_received``
******************************************************

The server emits this event when a proctored exam attempt has been reviewed and
the results of the review are available.

**History**: Added 01 Dec 2015.

``event`` **Member Fields**:

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``attempt_allowed_time_limit_mins``
     - number
     - The amount of time, in minutes, that the learner has to complete
       the exam.
   * - ``attempt_code``
     - string
     - A generated identifier for the exam attempt.
   * - ``attempt_completed_at``
     - datetime
     - The UTC time stamp of the time at which the learner submitted the
       exam.
   * - ``attempt_event_elapsed_time_secs``
     - number
     - The number of seconds that passed between the time the learner started
       the exam and the time the event was emitted.
   * - ``attempt_id``
     - number
     - The primary identifier of the exam attempt.
   * - ``attempt_started_at``
     - datetime
     - The UTC time stamp of the time at which the learner began taking the
       exam.
   * - ``attempt_status``
     - string
     - The current state of the exam, for example, ``created``.
   * - ``attempt_user_id``
     - number
     - The primary identifier of the learner taking the exam.
   * - ``exam_content_id``
     - string
     - The primary identifier of the subsection that contains the exam.
   * - ``exam_default_time_limit_mins``
     - number
     - The standard amount of time, in minutes, that learners have to complete
       the exam.
   * - ``exam_id``
     - number
     - The primary identifier of the exam.
   * - ``exam_name``
     - string
     - The title of the exam in the course page, taken from the subsection
       title.
   * - ``exam_is_active``
     - Boolean
     - Indicates whether the special exam is currently available for learner
       attempts.
   * - ``exam_is_practice_exam``
     - Boolean
     - Indicates whether the special exam is a practice proctored exam.
   * - ``exam_is_proctored``
     - Boolean
     - Indicates whether the special exam is a proctored exam.
   * - ``review_attempt_code``
     - string
     - A generated identifier for the review of the exam attempt.
   * - ``review_status``
     - string
     - The result of the review. Values include ``Clean``, ``Suspicious``, and
       ``Rules Violation``.
   * - ``review_video_url``
     - string
     - The URL of the proctored exam record.

.. _special_exam_attempt_started:

``edx.special_exam.proctored.attempt.started``, ``edx.special_exam.practice.attempt.started``, and ``edx.special_exam.timed.attempt.started``
*********************************************************************************************************************************************

The server emits this event when a learner begins taking a proctored exam.

The ``event`` fields for this event are the same as the ``event`` fields for
the ``edx.special_exam.{special exam type}.attempt.created`` event. For more
information, see
:ref:`special_exam_attempt_created`.

**History**: Added 01 Dec 2015.

.. _special_exam_attempt_submitted:

``edx.special_exam.proctored.attempt.submitted``, ``edx.special_exam.practice.attempt.submitted``, and ``edx.special_exam.timed.attempt.submitted``
***************************************************************************************************************************************************

The server emits this event when a learner completes a proctored exam and
submits it for grading and review.

The ``event`` fields for this event are the same as the ``event`` fields for
the ``edx.special_exam.{special exam type}.attempt.created`` event. For more
information, see
:ref:`special_exam_attempt_created`.

**History**: Added 01 Dec 2015.

``edx.special_exam.proctored.attempt.verified``
***********************************************

The server emits this event when the review of a proctored exam is complete and
the exam attempt is approved.

The ``event`` fields for this event are the same as the ``event`` fields for
the ``edx.special_exam.proctored.attempt.created`` event. For more information,
see
:ref:`special_exam_attempt_created`.

**History**: Added 01 Dec 2015.



``edx.special_exam.proctored.option-presented``
***********************************************

The server emits this event when a learner views the starting page of a
proctored exam. The starting page presents a link that learners can follow to
begin taking the proctored exam.

The ``event`` fields for this event are the same as the ``event`` fields for
the ``edx.special_exam.proctored.created`` event. For more information, see
:ref:`special_exam_created`.

**History**: Added 01 Dec 2015.

