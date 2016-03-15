.. _special_exam_development_events:

==============================================================
Timed and Proctored Exam Development and Administration Events
==============================================================

.. include:: special_exam_events_overview.rst

Some special exam events are emitted when learners interact with exams. For more information, see :ref:`special_exam_events`.

Because special exams include similiar functions and behavior, they share some
similar events. For example, the
``edx.special_exam.proctored.allowance.created``,
``edx.special_exam.practice.allowance.created``, and
``edx.special_exam.timed.allowance.created`` events include identical fields.

This section includes descriptions of the following events.

.. contents::
  :local:
  :depth: 1

.. _special_exam_allowance_created:

``edx.special_exam.proctored.allowance.created``, ``edx.special_exam.practice.allowance.created``, and ``edx.special_exam.timed.allowance.created``
***************************************************************************************************************************************************

The server emits this event when a course team grants an exception to the
standard exam rules for an individual learner.

**History**: Added 01 Dec 2015.

``event`` **Member Fields**:

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
   * - ``allowance_key``
     - string
     - The type of allowance granted.
   * - ``allowance_user_id``
     - number
     - The identifier of the learner who has been granted the allowance.
   * - ``allowance_value``
     - string
     - The specific details of the allowance granted.
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

.. _special_exam_allowance_deleted:

``edx.special_exam.proctored.allowance.deleted``, ``edx.special_exam.practice.allowance.deleted``, and ``edx.special_exam.timed.allowance.deleted``
***************************************************************************************************************************************************

The server emits this event when a course team removes an exception to the
standard exam rules that was previously granted to an individual learner.

The ``event`` fields for this event are the same as the ``event`` fields for
the ``edx.special_exam.{special exam type}.allowance.created`` event. For more
information, see :ref:`special_exam_allowance_created`.

**History**: Added 01 Dec 2015.

.. _special_exam_created:

``edx.special_exam.proctored.created``, ``edx.special_exam.practice.created``, and ``edx.special_exam.timed.created``
*********************************************************************************************************************

The server emits this event when a course team creates a proctored exam in
Studio.

**History**: Added 01 Dec 2015.

``event`` **Member Fields**:

.. list-table::
   :widths: 15 15 60
   :header-rows: 1

   * - Field
     - Type
     - Details
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

.. _special_exam_updated:

``edx.special_exam.proctored.updated``, ``edx.special_exam.practice.updated``, and ``edx.special_exam.timed.updated``
*********************************************************************************************************************

The server emits this event when a course team alters a proctored exam in
Studio.

The ``event`` fields for this event are the same as the ``event`` fields for
the ``edx.special_exam.{special exam type}.created`` event. For more
information, see
:ref:`special_exam_created`.

**History**: Added 01 Dec 2015.
