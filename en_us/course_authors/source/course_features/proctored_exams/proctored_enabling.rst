.. _Enabling Proctored Exams:

########################################
Enabling and Creating Proctored Exams
########################################

This section describes how to enable and create proctored exams in a course.
For more information, see :ref:`CA_ProctoredExams_Overview` and
:ref:`Managing Proctored Exams`.

**************************************************
Enabling Proctored Exams in Your Course
**************************************************


To enable proctored exams in your course, follow these steps.

#. In Studio, select **Settings**, then select **Advanced Settings**.

#. Locate the **Enable Proctored Exams** policy key. The default value is
   ``false``.

#. Change the value of the setting to ``true``.

#. Select **Save Changes**. You can now create proctored exams in your course.

After you enable this setting for your course, you can perform the
following tasks.

.. contents::
 :local:
 :depth: 1


.. _Create a Proctored Exam:

=================================
Create a Proctored Exam
=================================

To create an exam that includes online proctoring, follow these steps.

.. note:: Proctored exams are always timed exams.

#. Add and :ref:`develop a subsection <Developing Course Subsections>` as you
   would any other subsection.

#. Select the **Configure** icon for the subsection.

   .. image:: ../../../../shared/images/subsections-settings-icon.png
    :alt: A subsection in the course outline with the configure icon indicated.
    :width: 600

   The **Settings** dialog box opens to the **Basic** tab.

#. In the **Grading** section, set the :ref:`assignment type and due date<Set
   the Assignment Type and Due Date for a Subsection>` for the subsection.

#. Select the **Advanced** tab.

#. In the **Set as a Special Exam** section, select **Proctored**.

#. In the **Time Allotted** field, enter the length of time that you want
   learners to have to complete the problems in the subsection. Enter the time
   as HH:MM, where HH is hours and MM is minutes.

#. Optionally, in the **Review Rules** field, enter any additions or exceptions
   to the :ref:`default rules for proctored exams<CA Online Proctoring Rules>`.
   For more information, see :ref:`specifying_exam_rules_and_exceptions`.

#. Select **Save**.

For information about how learners experience a proctored exam, see
:ref:`CA_LearnerExperience_Proctored Exams`. For information about creating a
practice exam that learners can take, see :ref:`Create a Practice Proctored
Exam`.


.. _Create a Practice Proctored Exam:

===================================
Create a Practice Proctored Exam
===================================

You can add a practice proctored exam to your course so that learners can
confirm that their systems are compatible with the proctoring software and
familiarize themselves with the steps to perform the identity and environment
checks.

.. note:: Unlike actual proctored exams, practice exams are visible to all
   learners, regardless of the track that they are enrolled in.

Practice exams are not linked to credit eligibility requirements and
no monitoring by the proctoring software is actually done, but learners will
be guided through the same steps as in a real proctored exam, to install the
proctoring software, perform the identify checks and a room scan.

Learners who have performed the proctoring software installation for a
practice exam are required to perform the same installation and setup steps
when they prepare to take an actual proctored exam, including a webcam scan of
the room that they intend to take the actual exam in.

.. note:: Make sure you create the practice exam as an ungraded exam.

To create a practice exam, follow these steps.

#. Add and :ref:`develop a subsection <Developing Course Subsections>` as you
   would any other subsection.

#. Select the **Configure** icon for the subsection.

   .. image:: ../../../../shared/images/subsections-settings-icon.png
    :alt: A subsection in the course outline with the configure icon indicated.
    :width: 600

   The **Settings** dialog box opens to the **Basic** tab.

#. In the **Grading** section, set the :ref:`assignment type and due date<Set
   the Assignment Type and Due Date for a Subsection>` for the subsection.

#. Select the **Advanced** tab.

#. In the **Set as a Special Exam** section, select **Practice Proctored**.

#. In the **Time Allotted** field, enter the length of time that you want
   learners to have to complete the problems in the subsection. Enter the time
   as HH:MM, where HH is hours and MM is minutes.

   For a practice exam, edX recommends that you specify a relatively short
   duration that is appropriate for the number of example problems you
   include in the subsection.

#. Select **Save**.

#. Optionally, add a unit with a text component to the practice exam
   subsection. You can use the text component to provide learners with
   information about the proctored exam in your course.

The practice exam is added to the course, and is visible to all learners
regardless of their enrollment track.

