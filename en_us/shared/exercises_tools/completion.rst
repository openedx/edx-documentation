.. _completion:

##################
Completion Tool
##################

.. note:: EdX offers full support for this tool.

The Completion tool provides learners with a way to mark sections of the
course as completed. It helps learners to track their progress through
sections of the course, including for ungraded activities such as reading
text, watching video, or participating in course discussions.

.. contents::
  :local:
  :depth: 1

***********
Overview
***********

The Completion tool adds a toggle control that provides learners with a way to
indicate both to themselves and to the course team that they have completed an
activity.

The Completion tool is itself a graded component and is therefore always
included on the learner **Progress** page. However, depending on whether it is
used in a graded or ungraded section of the course, it appears either as a
part of the learner's final grade or as a practice score, respectively.

If you use the Completion tool in an ungraded section of the course, the score
for completing the activity that it is associated with is listed as a practice
score on the **Progress** page. Practice scores are not included in the
learner's final grade for the course.

You can also use the Completion tool in graded sections of the course. If you
do so, a score for completing the activity is included in learners' final
grades. For example, if you include a Completion toggle control in a
particular section of the course content, learners who mark the section as
completed receive 1/1 points, while learners who do not mark the section as
completed receive 0/1 points. These scores are included in learners' final
grades on the **Progress** page.

.. note:: EdX recommends using the Completion tool primarily to track progress
   for ungraded activities such as reading assigned texts, watching videos,
   or participating in course discussions.


===================
The Toggle Control
===================

The Completion tool's toggle control looks like this to a learner if she has not
yet marked an activity as completed.

.. image:: ../../../shared/images/completion_markcomplete.png
  :alt: The Completion tool in an "unmarked" state.

After a learner selects the Completion toggle to indicate that she has
completed an activity, the toggle looks like this. Learners can select the
toggle again to unmark the unit.

.. image:: ../../../shared/images/completion_unmark.png
  :alt: The Completion tool in an "completed" state.


******************************************
Enable the Completion Tool
******************************************

Before you can add Completion toggle control to sections in your course, you
must enable the Completion tool in Studio.

To enable the Completion tool in Studio, add the ``"done"`` key to the
**Advanced Module List** on the **Advanced Settings** page, then select **Save
Changes**. (Be sure to include the quotation marks around the key value.) For
more information, see :ref:`Enable Additional Exercises and Tools`.

*************************************
Add the Completion Tool to a Course
*************************************

After you have enabled the Completion tool in Studio, to add the Completion
toggle control to a unit in a course, follow these steps.

#. In the course outline in Studio, locate the unit to which you want to add
   the Completion toggle control.
#. Under **Add New Component**, select **Advanced**.
#. Select **Completion**.
   The Completion toggle control is added to the unit.

.. note:: Select **Edit** in the Completion component for information about the
   tool.


.. only:: OLX

 ****************************************
 Add the Completion Tool to an OLX Course
 ****************************************

 To add the Completion tool to a unit in an OLX course, it is sufficient to add
 the ``<done>`` tag to the OLX.

 EdX recommends that you also explicitly specify a ``url_name`` within the
 ``<done>`` tag, as shown in the following example. If you do not explicitly
 specify a ``url_name``, a value is automatically assigned, which can be
 problematic if the same course is imported several times. For  example, if the
 ``url_name`` value is automatically generated each time you  import your course,
 and if you import your course more than once, the learner  state for the
 associated problems is lost each time a new ``url_name`` value  is assigned.

 .. code-block:: xml

    <done url_name="video_3_completion"/>


