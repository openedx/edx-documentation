.. _Survey Tool:

###################
Survey Tool
###################

.. note:: EdX offers full support for this tool.

This section describes how to include surveys in your course.

.. contents::
   :local:
   :depth: 2

*********
Overview
*********

You can include surveys in your course to collect learner responses to multiple
questions.

For a survey, you configure multiple question and multiple possible answers.
The set of answers is used for each question in the survey. If you need to ask
only one question, use the :ref:`Poll Tool`.

The following example survey has three questions, each with the same three
possible answers.

.. image:: ../../../shared/images/survey.png
    :alt: A survey asking multiple questions about the learner's view of the
     course.
    :width: 600

After learners submit their answers to the survey, they see the survey
results that have been gathered at this time, unless the survey has been
configured to hide results.

.. image:: ../../../shared/images/survey_results.png
    :alt: The results of a survey asking multiple questions about the
     learner's view of the course.
    :width: 600

.. _Enable the Survey Tool:

*********************************************
Enable the Survey Tool
*********************************************

Before you can add a survey to your course, you must enable the survey tool in
Studio or OLX (open learning XML).

To enable the survey tool in Studio, you add the ``"survey"`` key to the
**Advanced Module List** on the **Advanced Settings** page. (Be sure to
include the quotation marks around the key value.) For more information, see
:ref:`Enable Additional Exercises and Tools`.

Alternatively, you can use OLX to enable the survey tool.

======================================
Enable the Survey Tool in OLX
======================================

To enable the survey tool, you edit the XML file that defines the course
structure.

Open the XML file for the course in the ``course`` directory. In the ``course``
element's ``advanced-modules`` attribute, add the string ``survey``.

For example, the following XML code enables the survey tool.

.. code-block:: xml

  <course advanced_modules="[&quot;survey&quot;,
      &quot;poll&quot;]" display_name="Sample Course"
      start="2015-01-01T00:00:00Z">
      ...
  </course>

***************************
Add a Survey in edX Studio
***************************

You must :ref:`enable the survey tool <Enable the Survey Tool>` before you add
the component.

#. On the Course Outline page, open the unit where you want to add the survey.

#. Under **Add New Component** click **Advanced**, and then select **Survey**.

   The new component is added to the unit, with the default survey that
   contains three answer fields and three questions.

   .. image:: ../../../shared/images/survey_studio.png
    :alt: The survey component in Studio.
    :width: 600

#. In the new component, select **Edit**.

#. In the **Display Name** field, enter the name for the component.

#. In the **Feedback** field, enter text that learners see after they submit
   responses.

#. In the **Private Results** field, to hide survey results from learners,
   select **True**. If you leave the default value, **False**, learners see
   survey results after they submit responses.

#. In the **Maximum Submissions** field, to allow learners to submit responses
   more than once, change the value. Enter **0** to allow unlimited
   responses.

   .. note::
    If you allow learners to submit responses more than once, you should set
    **Private Results** to **True**. Otherwise, learners will be able to change
    their responses after seeing others' responses.

#. Configure answers for the survey. Each answer is displayed to learners as a
   column, with a radio button they can select. Each answer is used for each
   survey question.

   #. In each **Answer** field, enter the text for the column heading that
      learners will see.

   #. To add answers, select **Add answer** at the bottom of the editor. New
      answers are added at the bottom of the list.

   #. The top answer in the list is displayed to learners as the left-most
      answer column in the survey, and the bottom answer is displayed in the
      right-most column.  To change the order of answers, select the up and
      down buttons next to each answer.

   #. To remove an answer, select **Delete** next to the answer.

#. Configure questions for the survey. Each question is displayed to learners
   in the left-most column.

   #. You must enter either text or an image path, or both, for each question.
      To enter an image, use the :ref:`Studio URL <File URLs>` for the image.

   #. The survey template contains three questions. To add questions, select
      **Add question** at the bottom of the editor. New questions are added at
      the bottom of the list.

   #. If you use an image, you must enter useful alternative text in the
      **Image alternate text** field for non-sighted users.

   #. Questions are displayed to learners as rows in the order you configure
      them. To change the order of questions, select the up and down buttons
      next to each question.

   #. To remove a question, select **Delete** next to the question.

#. Select **Save**.

***************************
Add a Survey in OLX
***************************

To add a survey XBlock in OLX, you create the ``survey`` element. You can embed
the ``survey`` element in the ``vertical`` element, or you can create the
``survey`` element as a stand-alone file that you reference in the vertical.

The following example shows the OLX definition for a survey with two questions.

.. code-block:: xml

  <survey
    url_name="unique identifier for the survey"
    xblock-family="xblock.v1"
    questions="[
                 [&quot;unique code for question 1&quot;,
                   {
                     &quot;img&quot;: &quot;Static URL to image&quot;,
                     &quot;img_alt&quot;: &quot;Alternative text for image&quot;,
                     &quot;label&quot;: &quot;Text of question 1&quot;
                   }
                 ],
                 [&quot;unique code for question 2&quot;,
                   {
                     &quot;img&quot;: &quot;Static URL to image&quot;,
                     &quot;img_alt&quot;: &quot;Alternative text for image&quot;,
                     &quot;label&quot;: &quot;Text of question 2&quot;
                    }
                  ]
                ]"
    feedback="Feedback displayed to learner after submission"
    private_results="false"
    block_name="Display name for survey"
    max_submissions="1"
    answers="[
              [
                &quot;Unique identifier for answer 1&quot;,
                &quot;Answer text&quot;
              ],
              [
                &quot;Unique identifier for answer 2&quot;,
                &quot;Answer text&quot;
              ]
            ]"
  />

==========================
survey Element Attributes
==========================

The following table describes the attribute of the ``survey`` element.

.. list-table::
     :widths: 20 80

     * - Attribute
       - Description
     * - ``url_name``
       - The unique identifier of the survey.
     * - ``xblock-family``
       - The XBlock version used. Must be ``xblock.v1``.
     * - ``questions``
       - An array of questions in the survey. Each question has a unique
         identifier, and a dictionary that defines values for the following
         names.

         * ``img``, the static URL of the question image.
         * ``img_alt``, the alternative text for the image.
         * ``label``, the question text.

         Each question must have a value for ``img`` or ``label``, or both.
     * - ``answers``
       - An array of answers in the survey. Each answer has a unique
         identifier, and a dictionary that defines values for the following
         names.

         * ``img``, the static URL of the answer image.
         * ``img_alt``, the alternative text for the image.
         * ``label``, the answer text.

         Each answer must have a value for ``img`` or ``label``, or both.
     * - ``feedback``
       - The text shown to learners after they submit a response.
     * - ``private_results``
       - Whether the survey results are shown to learners (``true``) or not
         (``false``).
     * - ``block_name``
       - The display name for the survey.
     * - ``max_submissions``
       - The number of times a learner can submit survey answers.  Use ``0`` to
         allow unlimited submissions. If you use a value other than ``1``, set
         ``private_results`` to ``true``. Otherwise, learners will be able to
         change their responses after seeing others' responses.

***************************
Editing Published Surveys
***************************

Do not publish a survey until you have completed and tested it. You should
avoid changing a survey after learners have begun using it.

If you must edit a survey after learners have submitted answers, take into
account the following implications.

* If you edit the value of a question or answer, previous submissions are
  associated with the new question or answer value. This change can result in
  an inaccurate picture of the responses.

* If you change the survey so that previous submissions are invalid, by
  removing a question or answer, those submissions are deleted when learners
  next view the unit. Learners with invalid submissions are permitted to submit
  new responses.

***************************
View Survey Results
***************************

When you view the survey as a course staff member, you can view results of the
survey inside the course.

Select **View results** in the survey.

.. image:: ../../../shared/images/survey_view_results.png
    :alt: A survey with the View Results button for course staff.
    :width: 600

The results of the survey are then displayed.

.. image:: ../../../shared/images/survey_results.png
    :alt: The results of a survey asking multiple questions about the
     learner's view of the course.
    :width: 600
