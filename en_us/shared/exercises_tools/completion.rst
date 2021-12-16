.. _completion:

##################
Completion Tool
##################

.. note:: EdX does not support this tool.

The completion tool provides learners with a way to mark sections of the
course as completed. It helps learners to track their progress through
sections of the course, including for ungraded activities such as reading
text, watching video, or participating in course discussions.

.. contents::
  :local:
  :depth: 1

***********
Overview
***********

The completion tool provides learners with a way to indicate both to themselves
and to the course team that they have completed an activity.

The completion tool is itself a graded component and is therefore always
included on the learner **Progress** page. However, depending on whether it is
used in a graded or ungraded section of the course, it appears either as a
part of the learner's final grade or as a practice score, respectively.

If you use the completion tool in an ungraded section of the course, the score
for completing the activity that it is associated with is listed as a practice
score on the **Progress** page. Practice scores are not included in the
learner's final grade for the course.

You can also use the completion tool in graded sections of the course. If you
do so, a score for completing the activity is included in learners' final
grades. For example, if you include a completion component in a particular unit
of the course content, learners who use the component to mark the unit as
complete receive 1/1 points, while learners who do not mark the unit as
complete receive 0/1 points. These scores are included in learners' final
grades on the **Progress** page.

.. note:: EdX recommends using the completion tool primarily to track progress
   for ungraded activities such as reading assigned texts, watching videos,
   or participating in course discussions.


=========================
The Completion Control
=========================

When you add a completion component to a unit, learners see a control that is
labeled **Mark as complete**. In this example, the completion component follows
a Text component.

.. image:: ../../../shared/images/completion_markcomplete.png
  :alt: The completion component in an incomplete state.
  :width: 400

After a learner selects this control, the label changes to **Unmark**. Learners
who revisit their work in a unit and want to change the completion status can
select this control as many times as needed.

.. image:: ../../../shared/images/completion_unmark.png
  :alt: The completion component in a complete state.


******************************************
Enable the Completion Tool
******************************************

Before you can add a completion component to your course, you must enable the
completion tool in Studio.

To enable the completion tool in Studio, add the ``"done"`` key to the
**Advanced Module List** on the **Advanced Settings** page, then select **Save
Changes**. (Be sure to include the quotation marks around the key value.) For
more information, see :ref:`Enable Additional Exercises and Tools`.

*************************************
Add a Completion Component
*************************************

After you have enabled the completion tool in Studio, to add a completion
component to a unit in a course, follow these steps.

#. In the course outline in Studio, locate the unit to which you want to add
   the completion component.
#. Under **Add New Component**, select **Advanced**.
#. Select **Completion**.
   The completion component is added to the unit.

.. note:: Select **Edit** in the completion component for information about the
   tool.


.. only:: OLX

 ****************************************
 Add the Completion Tool to an OLX Course
 ****************************************

 To add the completion tool to a unit in an OLX (open learning XML) course, it
 is sufficient to add the ``<done>`` tag to the OLX.

 EdX recommends that you also explicitly specify a ``url_name`` within the
 ``<done>`` tag, as shown in the following example. If you do not explicitly
 specify a ``url_name``, a value is automatically assigned, which can be
 problematic if the same course is imported several times. For example, if the
 ``url_name`` value is automatically generated each time you import your
 course, and if you import your course more than once, the learner state for
 the associated problems is lost each time a new ``url_name`` value is
 assigned.

 .. code-block:: xml

    <done url_name="video_3_completion"/>


