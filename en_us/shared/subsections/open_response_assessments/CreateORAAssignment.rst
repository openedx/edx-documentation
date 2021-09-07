.. _PA Create an ORA Assignment:

#############################################
Create an Open Response Assessment Assignment
#############################################

Creating an :ref:`open response assessment (ORA) assignment <Open Response
Assessments Two>` is a multi-step process. This section covers each step in
detail.

.. contents::
  :local:
  :depth: 1

In addition, see these other topics about different aspects of open response
assessments.

* Components of an open response assessment: :ref:`Open Response Assessments
  Two`

* Viewing metrics and learner responses for released open response assessments:
  :ref:`Accessing ORA Assignment Information`

* Actions you can take for an active ORA assignment: :ref:`Managing ORA
  Assignments`


.. _PA Create Component:

******************************
Step 1. Add the Component
******************************

To add the open response assessment component to your course, complete these
steps.

.. note:: Do not add more than one ORA component in a course unit. Multiple ORA
   assignments in a unit cause errors when learners submit their assessments.

#. In Studio, open the unit where you want to create the open response
   assessment.

#. Under **Add New Component**, select **Open Response**.

#. Select one of the the Open Response Assessment templates listed.

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

You can format text and add images inside an open response assessment prompt
the same way you would for an HTML component. For more information, see
:ref:`The Visual Editor`.

To add :ref:`prompts<PA Prompts>`, or questions, to your ORA assignment,
complete these steps.

#. In the open response assessment component editor, select **Prompt**.
#. Replace the example prompt with your prompt.
#. To add another prompt in the assignment, select **Add a Prompt**, and then
   repeat step 2.


.. _PA Add Rubric:

******************************
Step 3. Add the Rubric
******************************

In this step, you add your :ref:`rubric<PA Rubric>` to provide guidance for
assessing responses within the assignment. You add one rubric for each
problem, regardless of the number of prompts in the problem.

.. note::

    The most effective rubrics for peer grading are written in clear, simple
    language, have concrete details, and are as specific as possible. Many
    novice learners will find it diffidult to make the types of value
    judgments required by more holistic rubrics.


For each step below, replace any default text with your own text.

.. note:: All open response assessments include a feedback field below the
   rubric so that learners can provide written feedback on a peer's overall
   response. You can also allow or require learners to provide feedback for
   individual criteria. See step 4 in the following procedure for instructions.
   For more information, see :ref:`Feedback Options`.

To add the rubric, follow these steps.

#. In the ORA component editor, select the **Rubric** tab.

#. In the first **Criterion** section, enter the name and prompt text of your
   first criterion (100 character limit).

#. In the **Option** sections for this criterion, for each option that you
   provide for the criterion enter a name, explanation, and point value.

   To remove options, select **Remove** at the top right of the option section.

   To add more options, select **Add Option**.

#. Next to **Feedback for This Criterion**, select a value in the dropdown
   list.

   * If you do not want to allow feedback for this individual criterion,
     select **None**.
   * To require feedback for this criterion, select **Required**.
   * To allow feedback, but not require it, select **Optional**.

#. Repeat steps 2-4 to create additional criteria. To add more criteria than
   provided for in the template, select **Add Criterion** at the end of the
   list of criteria.

#. Under **Feedback for This Response**, add instructions for learners to
   provide overall written feedback on responses that they assess. You can
   leave the default text in the **Feedback Instructions** and **Default
   Feedback Text** fields, or replace it with your own text.

.. note:: After you publish an ORA assignment, you can no longer change the
   structure of the rubric or the point values associated with each criterion
   in the rubric. If you correct typographical errors in the text of the
   rubric, only learners who have not yet started the assignment will see the
   corrections. However, you can modify due dates and the weight of the ORA
   assignment after you publish an ORA assignment.

.. note:: If you wish to allow learners to view the rubric as they work on their
   response, see  :ref:`Show Rubric During Response<PA Show Rubric During Response>`

.. _PA Criteria Comment Field Only:

==========================================================
Provide Only Comment Fields for Individual Criteria
==========================================================

For an individual criterion, you can omit options, but if you do not include
options, you must include the ability to add feedback comments.

To provide a comment field without options, complete these steps.

#. In the ORA component editor, select the **Rubric** tab.

#. In the **Criterion** section for the criterion that you want to only
   provide a comment field for, select **Remove** to remove each option.

#. Next to **Feedback for This Criterion**, select **Required** from the list.

=============
Reuse Rubrics
=============

If your course uses multiple Open Response Assessments with similar assessment
criteria, reusing rubrics may save time and prevent having to re-author the same
rubric across many ORAs.

To reuse a rubric, complete the following steps:

#. In Studio, navigate to an ORA with a completed rubric you'd like to copy.

#. In the ORA component editor, select the **Rubric** tab.

#. Expand the **Clone Rubric** section (if it is not already expanded) and copy or note
   the value following "Block ID for this ORA". This will allow you to uniquely
   identify this ORA later.

#. Navigate to (or create) an unpublished ORA where you'd like to reuse the rubric.

#. In the ORA component editor, select the **Rubric** tab and expand the
   **Clone Rubric** section.

#. In the "Block ID" dropdown, paste or select the ID of the ORA to copy rubric data
   from.

#. Click "Clone". A banner should appear saying "Rubric Successfully Cloned from
   Block ID: <block ID>".

#. **Note**: Cloning rubric data clears Learner Training examples. If applicable,
   follow the instructions at :ref:`learner training step<PA Student Training Step>` to
   add updated Learner Training examples.

.. _PA Specify Additional Settings:

***********************************
Step 4. Specify Additional Settings
***********************************

After you have added a prompt and rubric, you must specify additional settings
for the assignment. These settings include the type of response that learners
must submit, assignment dates, and whether learners will see a list of top
scoring responses.

.. _PA Specify Name and Dates:

========================
Specify a Name and Dates
========================

Before you specify the start and due dates and times for a response, be sure
that you consider these aspects of, and best practices for, the open response
assessment feature. For more information, see
:ref:`Best Practices for ORA`.

* Unlike other problem types, ORA assignments are not governed by the
  subsection due date. You set due dates for each ORA assignment in the
  assignment's settings.

* The :ref:`grace period <Set the Grace Period>` that you can set for the
  course does not apply to ORA assignments. For more information about the
  grade period setting, see :ref:`Set the Grace Period`.

* You should allow sufficient time for peer assessments to be performed after
  learners have submitted their own responses. EdX recommends that you allow at
  least one week between the due date for responses and the due date for peer
  assessments. If the response due time and peer assessment due time are close
  together, and a learner submits a response just before responses are due,
  other learners may not have time to perform peer assessments before peer
  assessments are due.

* The times that you set are in Coordinated Universal Time (UTC). To verify
  that you have specified the times that you intend, use a time zone converter
  such as `Time and Date Time Zone Converter
  <https://www.timeanddate.com/worldclock/converter.html>`_.

To specify a name for the assignment as well as start and due dates for all
learner responses, follow these steps.

#. In the ORA component editor, select **Settings**.

#. Next to **Display Name**, enter the name you want to give the assignment.

#. Select **Schedule** at the top of the ORA component editor.

#. Next to **Response Start Date** and **Response Start Time**, enter the date
   and time when you want learners to be able to begin submitting responses.

#. Next to **Response Due Date** and **Response Due Time**, enter the date and
   time by which all learner responses must be submitted.

.. _PA Allow Images:

=========================
Specify the Response Type
=========================

Learners can submit written responses, files, or both in their responses to the
assigment. If you want learners to upload files, make sure the text of your
prompt includes adequate instructions for learners to upload the required
files, including the file types that learners can upload.

.. note::
  Before you ask learners to submit files for your open response assessment, be
  sure to read about limitations and best practices. For more information, see
  :ref:`Asking Learners to Upload Other Files in Responses`.

  If you allow or require learners to upload image files, learners must also
  provide a brief written description of each image for accessibility.

To specify the response type that learners must submit, follow
these steps.

#. In the ORA component editor, select **Settings**.

#. For **Text Response**, select one of the following options.

   * **None**
   * **Required**
   * **Optional**

#. The **Response Editor** field allows you to select an editor that the students
   will use to format their responses. Select one of the following options:

   * **Simple text editor**: a simple text field without formatting options.
   * **WYSIWYG Editor**: a visual text editor that allows text formatting.

#. For **File Uploads Response**, select one of the following options.

   * **None**
   * **Required**
   * **Optional**

   If you select **Required** or **Optional**, **Allow Multiple Files** and **File Upload Types** will
   appear.

   For **Allow Multiple Files**, select either **True** or **False**. If **Allow Multiple Files** is
   **True**, learners will be able to upload multiple files in their response. If you would like to
   restrict learner responses to a single file, set **Allow Multiple Files** to **False**.

   For **File Upload Types**, select one of the following options.

   * **PDF or Image Files**
   * **Image Files**
   * **Custom File Types**

   If you select **Custom File Types**, the **File Types** field appears.
   Enter the file name extensions, separated by commas, of the types of files
   that you want learners to submit.

   .. note:: To reduce the potential for problems from files with malicious
    content, learners cannot upload certain file types. For more information,
    see :ref:`Prohibited File Extensions`.

#. For **Allow LaTeX Responses**, select **True** or **False**.

.. _PA Show Rubric During Response:

==============================================
Allow Learners to View Rubric While Responding
==============================================

By default, learners cannot see the rubric while they are working on their response.
However, you may decide that it would be helpful for learners to be able to view the
rubric while they work on their response so they know how they will be evaluated. To
enable this functionality:

#. In the ORA component editor, select **Settings**.

#. Set **Show Rubric During Response** to **True**.

When this setting is enabled, a collapsable section will appear in the Response step,
above the first prompt, that shows learners a detailed breakdown of how their response
will be graded.

.. note:: This is the rubric you set up in :ref:`Add Rubric<PA Add Rubric>`. For each Criterion, learners
   will see all Option names, descriptions, and point values.

.. _PA Show Top Responses:

=====================
Include Top Responses
=====================

You can specify whether learners see a section that shows the :ref:`highest
scoring responses<PA Top Responses>` that were submitted for each question in
the assignment. If offered, this section displays only after each learner has
completed all steps in the assignment. You specify the number of highest
scoring responses to show.

.. note:: Because each response can be up to 300 pixels in height, we
   recommend that you set the number of top responses lower than 20, to
   prevent the page from becoming too long.

#. In the ORA component editor, select **Settings**.

#. In the **Top Responses** field, specify the number of responses that you
   want to appear in the **Top Responses** section below the learner's final
   score.

   If you do not want this section to appear, set the number to 0. The
   maximum number is 100.

.. _PA Select Assignment Steps:

****************************************
Step 5. Select Assignment Steps
****************************************

Open response assessment assignments can include learner training, peer
assessment, self assessment, and staff assessment steps.

When adding an ORA problem, the component editor provides some predefined ORA
problem templates with different :ref:`steps<PA Assessment Steps>` set up
in a sequence that works well for most courses. While you can change the
order of the peer, self, and staff assessment steps, edX recommends that
you include them in this order.

.. note:: If you include a learner training step, you must also include a peer
   assessment step. The learner training step must come before peer or self
   assessment steps.

   If you include both peer and self assessment steps, edX recommends that you
   place the peer assessment before the self assessment.

   If you include a staff assessment step, it should be the final step in the
   assignment.

To add steps to the open response assignment, complete these actions.

#. In the ORA component editor, select the **Assessment Steps** tab.

#. Locate the following headings.

   * **Step: Learner Training**
   * **Step: Peer Assessment**
   * **Step: Self Assessment**
   * **Step: Staff Assessment**

   Select the check boxes for the steps that you want the assignment to
   include.

#. (optional) To change the order of the steps, drag the steps into the order
   that you want using the bar at the left side of the steps.


.. _PA Specify Step Settings:

******************************
Step 6. Specify Step Settings
******************************

After you select the steps that you want, you can specify settings for those
steps.

.. note::

   If you make changes to a step, and then clear the check box for that step,
   the step will no longer be part of the assignment and your changes will not
   be saved.

.. _PA Student Training:

========================
Learner Training
========================

For the :ref:`learner training step<PA Student Training Step>`, you enter one
or more example responses that you have created, then specify the expected
option for each criterion in your rubric.

.. note::

   You must enter your complete rubric on the **Rubric** tab before you can
   select options for the learner training responses. If you later change one
   of your criteria or any of its options, you must also update the learner
   training step.

To add and score learner training responses, follow these steps.

#. Under **Step: Learner Training**, select **View / Add Sample Responses**.
   The section will expand and display the sample responses already set up.
#. Select **Add sample reponse**.
#. In the **Response** field, enter the text of your example response.
#. Under **Response Score**, for each criterion, select the option that you
   want.

============================
Peer Assessment
============================

For the :ref:`peer assessment step<Peer Assessment Step>`, you specify the
number of responses that each learner must grade, the number of learners who
must grade each response, and start and due dates. All fields are required.

To specify peer assessment settings, follow these steps.

#. Locate the **Step: Peer Assessment** heading.

#. Select **View Options & configuration** to display the step settings.

#. Next to **Must Grade**, enter the number of responses that each learner
   must grade.

#. Next to **Graded By**, enter the number of learners that must grade each
   response.

#. Next to **Enable Flexible Peer Grade Averaging**, select **True** if you
   want to enable :ref:`Flexible Peer Grade Averaging`.

#. Switch to the **Schedule** tab.

#. Locate the **Peer Assessment Deadlines** heading.

#. Next to **Start Date** and **Start Time**, enter the date and time when
   learners can begin assessing their peers' responses.

#. Next to **Due Date** and **Due Time**, enter the date and time by which all
   peer assessments must be completed.

  .. note::

     The times that you set are in Coordinated Universal Time (UTC). To verify
     that you have specified the times that you intend, use a time zone
     converter such as `Time and Date Time Zone Converter
     <https://www.timeanddate.com/worldclock/converter.html>`_.

     Additionally, the course grace period setting does not apply to open
     response assessments. For more information about the grace period setting,
     see :ref:`Set the Grace Period`.

For more information about peer assessment steps, see :ref:`Peer Assessment
Step`.

============================
Self Assessment
============================

For the :ref:`self assessment step<Self Assessment Step>`, you specify when
the step starts and ends.

#. Locate the **Step: Self Assessment** heading and enable it.

#. Switch to the **Schedule** tab.

#. Locate the **Self Assessment Deadlines** heading.

#. Next to **Start Date** and **Start Time**, enter the date and time when
   learners can begin assessing their peers' responses.

#. Next to **Due Date** and **Due Time**, enter the date and time by which all
   peer assessments must be complete.

  .. note::

     The times that you set are in Coordinated Universal Time (UTC). To verify
     that you have specified the times that you intend, use a time zone
     converter such as `Time and Date Time Zone Converter
     <https://www.timeanddate.com/worldclock/converter.html>`_.

     Additionally, the course grace period setting does not apply to open
     response assessments. For more information about the grace period setting,
     see :ref:`Set the Grace Period`.


================
Staff Assessment
================

For the :ref:`staff assessment step<Staff Assessment Step>`, there are no
additional settings to specify after you have selected the step for inclusion
in the assignment.

.. _PA Test Assignment:

******************************
Step 7. Test the Assignment
******************************

To test your ORA assignment, you can set up the assignment in your course, set
the section or subsection date in the future, publish the unit, and ask one or
more beta testers to submit responses and grade each other. The beta testers
can then let you know if they found the question and the rubric easy to
understand or if they had any problems with the assignment.

For more information about beta testing, see :ref:`Beta_Testing`.
