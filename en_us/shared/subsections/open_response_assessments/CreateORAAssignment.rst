.. _PA Create an ORA Assignment:

#############################################
Create an Open Response Assessment Assignment
#############################################


Creating an open response assessment is a multi-step process. Each step is covered in detail below.

* :ref:`PA Create Component`
* :ref:`PA Add Prompt`
* :ref:`PA Add Rubric`
* :ref:`PA Specify Name and Dates`
* :ref:`PA Select Assignment Steps`
* :ref:`PA Specify Step Settings`
* :ref:`PA Show Top Responses`
* :ref:`PA Test Assignment`

For more information about the components of an open response assessment, see
:ref:`Open Response Assessments 2`. For information about viewing metrics and
learner responses for released open response assessments, see :ref:`Accessing
ORA Assignment Information`.


.. _PA Create Component:

******************************
Step 1. Create the Component
******************************

To create the component for your open response assessment, complete these steps.

#. In Studio, open the unit where you want to create the open response
   assessment.   
#. Under **Add New Component**, select **Problem**, select the **Advanced** tab,
   and then select **Peer Assessment**.
#. In the Problem component that appears, select **Edit**.

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

#. In the open response assessment component editor, select the **Prompt** tab.
#. Add the text of your question in the text field. Replace any default text if
   necessary.
#. Select **Add a Prompt** to add another prompt in the problem.


========================================
Add Formatting or Images to a Prompt
========================================

Currently, you cannot add text formatting or images inside the Peer Assessment
component. To include formatting or images within the text of a prompt, you
can add an HTML component that contains your text above the Peer Assessment
component, and leave the text field in the **Prompt** tab blank. The
instructions for the peer assessment still appear above the **Your Response**
field.

.. image:: ../../../../shared/building_and_running_chapters/Images/PA_HTMLComponent.png
      :alt: A peer assessment that has an image in an HTML component
      :width: 500

.. _PA Allow Images:

============================================
Allow Learners to Submit Images (optional)
============================================

To allow learners to submit an image with a response, complete these steps.

#. In the open response assessment component editor, select the **Settings** tab.
#. For **Allow Image Responses**, select **True**.

.. note:: 
 
   * The image file must be a .jpg or .png file, and it must be smaller than 5
     MB in size. 
   * Currently, course teams cannot see any of the images that
     learners submit. Images are not visible in the body of the assignment in
     the courseware, and they are not included in the course data package.
   * You can allow learners to upload an image, but you cannot require it.
   * Learners can only submit one image with each response.     
   * All responses must contain text. Learners cannot submit a response that
     contains only an image.

.. _PA Add Rubric:

******************************
Step 3. Add the Rubric
******************************

In this step, you add your rubric and provide your learners with feedback
options. You add one rubric for each problem, regardless of the number of
prompts in the problem.

For each step below, replace any default text with your own text.

.. note:: All open response assessments include a feedback field below the
   rubric so that learners can provide written feedback on a peer's overall
   response. You can also allow or require learners to provide feedback for
   individual criteria. See step 2.4 below for instructions. For more
   information, see :ref:`Feedback Options`.

To add the rubric, complete these steps.

#. In the open response assessment component editor, select the **Rubric** tab.
#. In the first **Criterion** section, enter the name and prompt text of your first criterion.
#. In the first **Option** section, enter the name, explanation, and point value for the first option.
#. In the next **Option** section, enter the name, explanation, and point value for the next option.
#. Repeat step 4 for each option. If you need to add more options, select **Add Option**.
#. Next to **Feedback for This Criterion**, select a value in the dropdown list.

   * If you do not want learners to provide feedback for this individual criterion, select **None**.
   * If you want to require learners to provide feedback, select **Required**.
   * If you want to allow learners to provide feedback, but not require it, select **Optional**.

7. Follow the instructions in steps 2-6 to add your remaining criteria. If you need to add more criteria, select **Add Criterion** at the end of the list of criteria.
#. Include instructions for learners to provide overall written feedback on their peers' responses. You can leave the default text in the **Feedback Instructions** field or replace it with your own text.

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

When you add a comment field to a criterion, the comment field appears below the
options for the criterion. You can also provide a comment field, but no options.

In the following image, the first criterion has a comment field but no options. The second includes options, but does not have a comment field.

.. image:: ../../../../shared/building_and_running_chapters/Images/PA_0_Option_Criteria.png

To provide a comment field without options, complete these steps.

#. In the criterion, select **Remove** to remove, or delete, all the options.
#. Next to **Feedback for This Criterion**, select **Required** in the dropdown list.


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
student responses, complete these steps.

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

Open response assessment assignments can include learner training, peer assessment, and self assessment steps. 

.. note:: If you include a learner training step, you must also include a peer
   assessment step. The learner training step must come before peer or self
   assessment steps. If you include both peer and self assessment steps, edX
   recommends that you place the peer assessment before the self assessment.


To add steps to the open response assignment, complete these actions.

#. In the component editor, select the **Settings** tab.

#. Scroll down past the **Allow Image Responses** and **Allow Latex
   Responses** fields.

#. Locate the following headings.

   * **Step: Student Training**
   * **Step: Peer Assessment**
   * **Step: Self Assessment**

   Select the check boxes for the steps that you want the assignment to include. 

#. (optional) To change the order of the steps, drag the steps into the order
   that you want.

.. note:: If you include a student training step, make sure it is the first
   step in the assignment.

.. _PA Specify Step Settings:

******************************
Step 6. Specify Step Settings
******************************

After you select the steps that you want, you can specify settings for those
steps.

.. note:: If you make changes to a step, but then you clear the check box for
   that step, the step will no longer be part of the assignment and your
   changes will not be saved.

.. _PA Student Training Step:

========================
Student Training
========================

For the student training step, you enter one or more responses that you have
created, then select an option for each criterion in your rubric.

.. note:: You must enter your complete rubric on the **Rubric** tab before you
   can select options for the student training responses. If you later change one
   of your criteria or any of its options, you must also update the student
   training step.

To add and score student training responses, follow these steps.

#. Under **Step: Student Training**, locate the first **Scored Response** section.
#. In the **Response** field, enter the text of your example response.
#. Under **Response Score**, for each criterion, select the option that you want.

For more information, see :ref:`PA Learner Training Assessments`.


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
   peer assessments must be complete.

  .. note:: The times that you set, and the times that learners see, are in
   Coordinated Universal Time (UTC). You might want to verify that you have
   specified the times that you intend by using a time zone converter such as
   `Time and Date Time Zone Converter
   <http://www.timeanddate.com/worldclock/converter.html>`_

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

.. _PA Show Top Responses:

******************************
Step 7. Show Top Responses
******************************

To allow learners to see the top-scoring responses for the assignment, you
specify a number on the **Settings** tab.

#. In the component editor, select the **Settings** tab.
   
#. In the **Top Responses** field, specify the number of responses that you
   want to appear in the **Top Responses** section below the learner's final
   score. If you do not want this section to appear, set the number to 0. The
   maximum number is 100.

.. note:: Because each response can be up to 300 pixels in height, we recommend
   that you set the number of top responses to 20 or lower, to prevent the page
   from becoming too long.

For more information, see :ref:`PA Top Responses`.


.. _PA Test Assignment:

******************************
Step 8. Test the Assignment
******************************

To test your assignment, set up the assignment in your course, set the section
or subsection date in the future, and ask a group of beta users to submit
responses and grade each other. The beta testers can then let you know if they
found the question and the rubric easy to understand or if they had any problems
with the assignment.

For more information about beta testing, see :ref:`Beta_Testing`.
