.. _Poll Tool:

###################
Poll Tool
###################

.. note:: EdX offers full support for this tool.

This section describes how to include polls in your course.

.. contents::
   :local:
   :depth: 2

*********
Overview
*********

You can include polls in your course to gather learners' opinions on various
questions.

For a poll, you configure one question and multiple possible
answers. If you need to ask multiple questions, use the :ref:`Survey Tool`.

The following example poll has four possible answers to the question.

.. image:: ../../../shared/images/poll_tool.png
    :alt: A poll asking if the learner's favorite color is red, green, blue, or
     other.
    :width: 400

After learners submit their answers to the poll question, they see the poll
results that have been gathered at this time, unless the poll has been
configured to hide results.

.. image:: ../../../shared/images/poll_with_results.png
    :alt: A poll showing results after the learner has submitted a response.
    :width: 400

*******************************************
Enable the Poll Tool
*******************************************

Before you can add a poll to your course, you must enable the poll tool in
Studio or OLX (open learning XML).

To enable the poll tool in Studio, you add the ``"poll"`` key to the **Advanced
Module List** on the **Advanced Settings** page. (Be sure to include the
quotation marks around the key value.) For more information, see
:ref:`Enable Additional Exercises and Tools`.


Alternatively, you can use OLX to enable the poll tool.

======================================
Enable the Poll Tool in OLX
======================================

To enable polls in your course, you edit the XML file that defines
the course structure.

Open the XML file for the course in the ``course`` directory. In the ``course``
element's ``advanced-modules`` attribute, add the string ``poll``.

For example, the following XML code enables polls in a course.

.. code-block:: xml

  <course advanced_modules="[&quot;survey&quot;,
      &quot;poll&quot;]" display_name="Sample Course"
      start="2015-01-01T00:00:00Z">
      ...
  </course>

***************************
Add a Poll in edX Studio
***************************

You must :ref:`enable the poll <Enable Additional Exercises and Tools>` tool
before you add the component.

#. On the Course Outline page, open the unit where you want to add the poll.

#. Under **Add New Component** click **Advanced**, and then select **Poll**.

   The new component is added to the unit, with the default poll that contains
   three answer fields.

   .. image:: ../../../shared/images/poll_studio.png
    :alt: The poll component in Studio.
    :width: 600

#. In the new component, select **Edit**.

#. In the **Display Name** field, enter the name for the component.

#. In the **Question/Prompt** field, enter text that learners see above the
   poll. You can use Markdown in this field.

#. In the **Feedback** field, enter text that learners see after they submit a
   responses. You can use Markdown in this field.

#. In the **Private Results** field, to hide poll results from learners,
   select **True**. If you leave the default value, **False**, learners see
   poll results after they submit responses.

#. In the **Maximum Submissions** field, change the value to the number of
   times that you want to allow learners to submit responses. Enter **0** to
   allow unlimited responses.

   .. note::
    If you allow learners to submit responses more than once, you should set
    **Private Results** to **True**. Otherwise, learners will be able to change
    their responses after seeing others' responses.

#. Configure answers for the poll.

   #. In each **Answer** field, enter the answer text that learners see.

   #. You must enter either text or an image path, or both, for each answer.
      To enter an image, use the :ref:`Studio URL <File URLs>` for the image.

   #. If you use an image, you must enter useful alternative text in the
      **Image alternate text** field for non-sighted users.

   #. To add answers, select **Add answer** at the bottom of the editor. New
      answers are added at the bottom of the list.

   #. To change the order of answers, select the up and down buttons next to
      each answer.

   #. To remove an answer, select **Delete** next to the answer.

#. Select **Save**.

***************************
Add a Poll in OLX
***************************

To add a poll XBlock in OLX, you create the ``poll`` element. You can embed
the ``poll`` element in the ``vertical`` element, or you can create the
``poll`` element as a standalone file that you reference in the vertical.

The following example shows the OLX definition for a poll with four answers.

.. code-block:: xml

  <poll url_name="f4ae7de0006f426aa4eed4b0b8112da5" xblock-family="xblock.v1"
    feedback="Feedback"
    display_name="Poll"
    private_results="false"
    question="What is your favorite color?"
    max_submissions="1"
    answers="[
               [&quot;R&quot;,
                 {
                   &quot;img&quot;: &quot;/static/image.png&quot;,
                   &quot;img_alt&quot;: &quot;Alt 1&quot;,
                   &quot;label&quot;: &quot;Red&quot;
                 }
               ],
               [&quot;B&quot;,
                 {
                   &quot;img&quot;: &quot;/static/image.png&quot;,
                   &quot;img_alt&quot;: &quot;Alt 2&quot;,
                   &quot;label&quot;: &quot;Blue&quot;
                 }
               ],
               [&quot;G&quot;,
                 {
                   &quot;img&quot;: &quot;/static/image.png&quot;,
                   &quot;img_alt&quot;: &quot;Alt3&quot;,
                   &quot;label&quot;: &quot;Green&quot;
                 }
               ],
               [&quot;O&quot;,
                 {
                   &quot;img&quot;: &quot;/static/image.png&quot;,
                   &quot;img_alt&quot;: &quot;Alt 4&quot;,
                   &quot;label&quot;: &quot;Other&quot;
                 }
               ]
             ]
  "/>

==========================
poll Element Attributes
==========================

The following table describes the attributes of the ``poll`` element.

.. list-table::
     :widths: 20 80

     * - Attribute
       - Description
     * - ``url_name``
       - The unique identifier of the poll.
     * - ``xblock-family``
       - The XBlock version used. Must be ``xblock.v1``.
     * - ``private_results``
       - Whether the poll results are shown to learners (``true``) or not
         (``false``).
     * - ``display_name``
       - The display name for the poll.
     * - ``question``
       - The prompt for the poll.
     * - ``feedback``
       - The text shown to learners after they submit a response.
     * - ``max_submissions``
       - The number of times a learner can submit poll answers.  Use ``0`` to
         allow unlimited submissions. If you use a value other than ``1``, set
         ``private_results`` to ``true``. Otherwise, learners will be able to
         change their responses after seeing others' responses.
     * - ``answers``
       - An array of answers in the poll. Each answer has a unique
         identifier, and a dictionary that defines values for the following
         names.

         * ``img``, the static URL of the answer image.
         * ``img_alt``, the alternative text for the image.
         * ``label``, the answer text.

         Each answer must have a value for ``img`` or ``label``, or both.

***************************
Editing Published Polls
***************************

Do not publish a poll until you have completed and tested it. You should
avoid changing a poll after learners have begun to use it.

If you must edit a poll after learners have submitted answers take into account
the following implications.

* If you edit the value of an answer, previous submissions are associated with
  the new answer value. This change can result in an inaccurate picture of the
  responses.

* If you change the poll so that previous submissions are invalid, by removing
  an answer, those submissions are deleted when learners next view the unit.
  Learners with invalid submissions can submit new responses.

***************************
View Poll Results
***************************

When you view the poll as a course staff member, you can view results of the
poll inside the course.

Select **View results** in the poll.

.. image:: ../../../shared/images/poll_view_results.png
    :alt: A poll with the View Results button for course staff.
    :width: 400

The results of the poll are then displayed.

.. image:: ../../../shared/images/poll_with_results.png
    :alt: A poll showing results after the learner has submitted a response.
    :width: 400
