.. _PA Create an ORA Assignment:

#############################################
Create an Open Response Assessment Assignment
#############################################

Creating an open response assessment is a multi-step process. This section
covers each step in detail.

.. contents::
  :local:
  :depth: 1

In addition, see these other topics about different aspects of open response
assessments.

* Components of an open response assessment: :ref:`Open Response Assessments 2`

* Viewing metrics and learner responses for released open response assessments:
  :ref:`Accessing ORA Assignment Information`

* Actions you can take for an active ORA assignment: :ref:`Managing ORA
  Assignments`


.. _PA Create Component:

******************************
Step 1. Create the Component
******************************

To create the component for your open response assessment, complete these
steps.

.. note:: Do not add more than one ORA component in a course unit. Multiple ORA
   assignments in a unit cause errors when learners submit their assessments.

#. In Studio, open the unit where you want to create the open response
   assessment.

#. Under **Add New Component**, select **Problem**.

#. Select **Advanced**, and then select **Peer Assessment**.

#. In the problem component that appears, select **Edit**.

   You use this component editor to add prompts and the rubric, and to specify
   other settings for the open response assessment component.

#. Select **Save** each time you complete an editing session. You can continue
   to edit the problem until you publish the unit.

.. note:: After you publish an ORA assignment, you can no longer change the
   structure of the rubric or the point values associated with each criterion
   in the rubric. If you correct typographical errors in the text of the
   rubric, only learners who have not yet started the assignment will see the
   corrections. However, you can modify due dates and the weight of the ORA
   assignment after you publish an ORA assignment.


.. _PA Add Prompt:

******************************
Step 2. Add Prompts
******************************

To add prompts, or questions, complete these steps.

.. note:: If you want to add text formatting to the prompt, or include an
 image, see :ref:`Add Formatting or Images to a Prompt`.

#. In the open response assessment component editor, select **Prompt**.
#. Add the text of your question in the text field. Replace any default text if
   necessary.
#. Select **Add a Prompt** to add another prompt in the problem.

.. _Add Formatting or Images to a Prompt:

========================================
Add Formatting or Images to a Prompt
========================================

Currently, you cannot format text or add images inside the Peer Assessment
component. To include formatting or images in a prompt, you can add an HTML
component that contains your text above the Peer Assessment component, and
leave the text field in the **Prompt** tab blank. The instructions for the peer
assessment still appear above the **Your Response** field.

.. image:: ../../../../shared/images/PA_HTMLComponent.png
      :alt: A peer assessment that has an image in an HTML component.
      :width: 500

.. _PA Allow Images:

============================================
Allow Learners to Submit Files (optional)
============================================

Before you enable this feature for your open response assessment, be sure to
read about its limitations and best practices. For more information, see
:ref:`Asking Learners to Upload Other Files in Responses`.

To allow learners to submit a file along with their text responses, follow
these steps.

#. In the open response assessment component editor, select **Settings**.

#. Set **Allow File Upload** to one of these options.

   * **Image File**
   * **PDF or Image File**
   * **Custom File Types**

#. If you select **Custom File Types**, the **File Types** field appears. Enter
   the file extensions, separated by commas, of the types of files that
   you want learners to submit.

   .. note:: To reduce the potential for problems from files with malicious
    content, learners cannot upload certain file types. For more information,
    see :ref:`Asking Learners to Upload Other Files in Responses`.

#. Verify that the text of the prompt describes the file type or types that
   learners can upload.

.. _PA Add Rubric:

******************************
Step 3. Add the Rubric
******************************

In this step, you add your rubric to provide guidance for assessing responses
within the assignment. You add one rubric for each problem, regardless of the
number of prompts in the problem.

For each step below, replace any default text with your own text.

.. note:: All open response assessments include a feedback field below the
   rubric so that learners can provide written feedback on a peer's overall
   response. You can also allow or require learners to provide feedback for
   individual criteria. See step 6 below for instructions. For more
   information, see :ref:`Feedback Options`.

To add the rubric, follow these steps.

#. In the open response assessment component editor, select the **Rubric** tab.

#. In the first **Criterion** section, enter the name and prompt text of your
   first criterion.

#. In the first **Option** section, enter the name, explanation, and point
   value for the first option.

#. In the next **Option** section, enter the name, explanation, and point value
   for the next option.

#. Repeat step 4 for each option. If you need to add more options, select **Add
   Option**.

#. Next to **Feedback for This Criterion**, select a value in the dropdown list.

   * If you do not want to allow feedback for this individual criterion,
     select **None**.
   * If you want to require feedback, select **Required**.
   * If you want to allow feedback, but not require it, select **Optional**.

#. Repeat steps 2-6 to add your remaining criteria. If you need to add more
   criteria, select **Add Criterion** at the end of the list of criteria.

#. Include instructions for learners to provide overall written feedback on
   their peers' responses. You can leave the default text in the **Feedback
   Instructions** field or replace it with your own text.

.. note:: After you publish an ORA assignment, you can no longer change the
   structure of the rubric or the point values associated with each criterion
   in the rubric. If you correct typographical errors in the text of the
   rubric, only learners who have not yet started the assignment will see the
   corrections. However, you can modify due dates and the weight of the ORA
   assignment after you publish an ORA assignment.


.. _PA Criteria Comment Field Only:

==========================================================
Provide Only Comment Fields for Individual Criteria
==========================================================

When you add a comment field to a criterion, the comment field appears below
the options for the criterion. You can also provide a comment field, but no
options.

In the following image, the first criterion has a comment field but no
options. The second criterion includes options, but does not have a comment
field.

.. image:: ../../../../shared/images/PA_0_Option_Criteria.png
  :alt: Examples of criteria with and without a comment field.

To provide a comment field without options, complete these steps.

#. In the criterion, select **Remove** to remove, or delete, all the options.
#. Next to **Feedback for This Criterion**, select **Required** in the dropdown
   list.


.. _PA Specify Name and Dates:

************************************************************
Step 4. Specify the Assignment Name and Response Dates
************************************************************

Before you specify the start and due dates and times for a response, be sure
that you consider these aspects of, and best practices for, the open response
assessment feature.

* Unlike other problem types, ORA assignments are not governed by the
  subsection due date. Due dates for each ORA assignment are set in the
  assignment's settings.

* The :ref:`grace period <Set the Grace Period>` that you can set for the
  course does not apply to ORA assignments.

* EdX recommends that you set the response due date at least one week before
  the peer assessment due date and time, to allow enough time for peer
  assessments to be performed after learners have submitted their own
  responses. If the response due time and peer assessment due time are close
  together, and a learner submits a response just before responses are due,
  other learners may not have time to perform peer assessments before peer
  assessments are due. For details, see :ref:`Best Practices for ORA`.

* The times that you set, and the times that learners see, are in Coordinated
  Universal Time (UTC). You might want to verify that you have specified the
  times that you intend by using a time zone converter such as `Time and Date
  Time Zone Converter <http://www.timeanddate.com/worldclock/converter.html>`_

To specify a name for the assignment as well as start and due dates for all
learner responses, complete these steps.

#. In the component editor, select the **Settings** tab.

#. Next to **Display Name**, type the name you want to give the assignment.

#. Next to **Response Start Date** and **Response Start Time**, enter the date
   and time when you want learners to be able to begin submitting responses.

#. Next to **Response Due Date** and **Response Due Time**, enter the date and
   time by which all learner responses must be submitted.


.. _PA Select Assignment Steps:

****************************************
Step 5. Select Assignment Steps
****************************************

Open response assessment assignments can include learner training, peer
assessment, self assessment, and staff assessment steps.

The component editor provides the steps in a sequence that works well for most
courses. While you can change the order of the peer, self, and staff assessment
steps, edX recommends that you include them in this order.

.. note:: If you include a learner training step, you must also include a peer
   assessment step. The learner training step must come before peer or self
   assessment steps.

   If you include both peer and self assessment steps, edX recommends that you
   place the peer assessment before the self assessment.

   If you include a staff assessment step, it should be the final step in the
   assignment.

To add steps to the open response assignment, complete these actions.

#. In the component editor, select the **Settings** tab.

#. Scroll down past the **Allow Image Responses** and **Allow Latex
   Responses** fields.

#. Locate the following headings.

   * **Step: Learner Training**
   * **Step: Peer Assessment**
   * **Step: Self Assessment**
   * **Step: Staff Assessment**

   Select the check boxes for the steps that you want the assignment to
   include.

#. (optional) To change the order of the steps, drag the steps into the order
   that you want.


.. _PA Specify Step Settings:

******************************
Step 6. Specify Step Settings
******************************

After you select the steps that you want, you can specify settings for those
steps.

.. note:: If you make changes to a step, but then you clear the check box for
   that step, the step will no longer be part of the assignment and your
   changes will not be saved.

.. _PA Student Training:

========================
Learner Training
========================

For the learner training step, you enter one or more responses that you have
created, then select an option for each criterion in your rubric.

.. note:: You must enter your complete rubric on the **Rubric** tab before you
   can select options for the learner training responses. If you later change
   one of your criteria or any of its options, you must also update the learner
   training step.

To add and score learner training responses, follow these steps.

#. Under **Step: Learner Training**, locate the first **Scored Response**
   section.
#. In the **Response** field, enter the text of your example response.
#. Under **Response Score**, for each criterion, select the option that you
   want.

For more information about learner training steps, see :ref:`PA Student
Training Step`.


============================
Peer Assessment
============================

For the peer assessment step, you specify the number of responses that each
learner must grade, the number of learners who must grade each response, and
start and due dates. All fields are required.

To specify peer assessment settings, follow these steps.

#. Locate the **Step: Peer Assessment** heading.

#. Next to **Must Grade**, enter the number of responses that each learner must
   grade.

#. Next to **Graded By**, enter the number of learners that must grade each
   response.

#. Next to **Start Date** and **Start Time**, enter the date and time when
   learners can begin assessing their peers' responses.

#. Next to **Due Date** and **Due Time**, enter the date and time by which all
   peer assessments must be completed.

  .. note:: The times that you set, and the times that learners see, use
   Coordinated Universal Time (UTC). You might want to verify that you have
   specified the times that you intend by using a time zone converter such as
   `Time and Date Time Zone Converter
   <http://www.timeanddate.com/worldclock/converter.html>`_

For more information about peer assessment steps, see :ref:`Peer Assessment
Step`.

============================
Self Assessment
============================

For the self assessment step, you specify when the step starts and ends.

#. Locate the **Step: Self Assessment** heading.

#. Next to **Start Date** and **Start Time**, enter the date and time when
   learners can begin assessing their peers' responses.

#. Next to **Due Date** and **Due Time**, enter the date and time by which all
   peer assessments must be complete.

  .. note:: The times that you set, and the times that learners see, use
   Coordinated Universal Time (UTC). You might want to verify that you have
   specified the times that you intend by using a time zone converter such as
   `Time and Date Time Zone Converter
   <http://www.timeanddate.com/worldclock/converter.html>`_

For more information about self assessment steps, see :ref:`Self Assessment
Step`.

================
Staff Assessment
================

For the staff assessment step, there are no additional settings after you have
selected the step for inclusion in the assignment.

For more information about staff assessment steps, see :ref:`Staff Assessment
Step`.


.. _PA Show Top Responses:

******************************
Step 7. Show Top Responses
******************************

To allow learners to see the top scoring responses for the assignment, you
specify a number on the **Settings** tab.

#. In the component editor, select the **Settings** tab.

#. In the **Top Responses** field, specify the number of responses that you
   want to appear in the **Top Responses** section below the learner's final
   score. If you do not want this section to appear, set the number to 0. The
   maximum number is 100.

.. note:: Because each response can be up to 300 pixels in height, we recommend
   that you set the number of top responses to 20 or lower, to prevent the page
   from becoming too long.

For more information about the **Top Responses** section that you can include
for an ORA assignment, see :ref:`PA Top Responses`.


.. _PA Test Assignment:

******************************
Step 8. Test the Assignment
******************************

To test your ORA assignment, you can set up the assignment in your course, set
the section or subsection date in the future, publish the unit, and ask one or
more beta testers to submit responses and grade each other. The beta testers
can then let you know if they found the question and the rubric easy to
understand or if they had any problems with the assignment.

For more information about beta testing, see :ref:`Beta_Testing`.
