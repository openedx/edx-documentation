.. _Conditional Module:

####################
Conditional Module
####################

.. note:: EdX offers provisional support for this problem type.

A conditional module controls the content that learners see after a response
that they make meets a certain condition. For example, learners who answer
"Yes" to a poll question see a different block of text from the learners who
answered "No" to the same question.

.. contents::
  :local:
  :depth: 1

*********************************
Enable the Conditional Module
*********************************

Before you can add a conditional component to your course, you must enable the
conditional module.

To enable the conditional module in Studio, you add the `"conditional"` key to
the **Advanced Module** List on the **Advanced Settings** page. Be sure to
include the quotation marks around the key value. For more information, see
:ref:`Enable Additional Exercises and Tools`.

============================
Create a Conditional Module
============================

To create a conditional module, follow these steps.

#. In the unit where you want to create the problem, select **Advanced** under
   **Add New Component**.

#. In the list of problem types, select **Conditional**.

#. In the component that appears, select **Edit**.

#. In the component editor, specify these settings.

    * **Blocked Content Message**: Optionally, enter the message that learners
      are shown when they do not satisfy the requirements to access the
      conditional content. To provide a link to the required component,
      include ``{link}`` within your message. If you have specified a source
      component in the **Source Component** field, a link to it is
      automatically generated in your message.

    * **Conditional Attribute**: The attribute from the source component that
      that is used to determine whether a learner is shown the content of this
      conditional module.

    * **Conditional Value**: The value of the conditional attribute specified in
      the **Conditional Attribute** field that must be true for a learner to
      be shown the content of this conditional module.

    * **Display Name**: This name appears in the horizontal navigation at the
      top of the page.

    * **Source Components**: The location IDs of the components whose
      attributes are used to determine whether a learner is shown the
      content of this conditional module.

#. Select **Save**.


*************
XML Examples
*************

Examples of open learning XML (OLX) markup for several conditional modules
follow. For more information about creating conditional modules using OLX, see
the *edX Open Learning XML Guide - Alpha Version*.

==============================================================
Example: Conditional Module Dependent on Poll Being Answered
==============================================================

.. code-block:: xml

    <conditional sources="i4x://MITx/0.000x/poll_question/first_real_poll_seq_with_reset" poll_answer="man"
    message="{link} must be answered for this to become visible.">
        <html>
            <h3>You see this because your vote value for "First question" was "man"</h3>
        </html>
    </conditional>

==============================================================
Example: Conditional Module Dependent on Poll Being Answered
==============================================================

This example uses the ``<show>`` tag.

.. code-block:: xml

    <conditional sources="i4x://MITx/0.000x/poll_question/first_real_poll_seq_with_reset" poll_answer="man"
    message="{link} must be answered for this to become visible.">
        <html>
            <show sources="i4x://MITx/0.000x/problem/test_1; i4x://MITx/0.000x/Video/Avi_resources; i4x://MITx/0.000x/problem/test_1"/>
        </html>
    </conditional>

==============================================================
Example: Conditional Module Dependent on Problem Attempted
==============================================================

.. code-block:: xml

    <conditional sources="i4x://MITx/0.000x/problem/Conditional:lec27_Q1" attempted="True">
        <html display_name="HTML for attempted problem">You see this because "lec27_Q1" was attempted.</html>
    </conditional>
    <conditional sources="i4x://MITx/0.000x/problem/Conditional:lec27_Q1" attempted="False">
        <html display_name="HTML for not attempted problem">You see this because "lec27_Q1" was not attempted.</html>
    </conditional>
