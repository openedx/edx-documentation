.. _FeedbackXBlock:

##################
FeedbackXBlock
##################

.. note:: EdX offers full support for this tool.

The FeedbackXBlock provides learners with a way to rate and provide
feedback on course content. They are given two questions, one which
allows for Likert feedback (a rating on a scale of 1-5), and a second
which allows for freeform feedback. A histogram of the Likert feedback
is provided to the course staff directly, while the freeform feedback
is prohibitively large to display, so is available only in edX
research data dumps.

.. contents::
  :local:
  :depth: 2

***********
Overview
***********

The most common uses of the FeedbackXBlock are:

* To give students a chance to reflect on the course content and what
  they have learned. Similar reflection is associated with
  demonstrably improved learning outcomes.
* To provide instructors with feedback on what parts of the course are
  working well, what parts are working poorly, and why.

When using this component, edX recommends asking students specific,
well-structured questions. For example, "Was this material clear or
confusing?" or "How long did this material take?" is a more helpful
question than "Did you like this material?"

.. image:: ../../../shared/images/FeedbackXBlockExample.png
  :alt: A few examples of the FeedbackXBlock.

**************************************************
Enable the Feedback Tool
**************************************************

Before you can add a feedback component to your course, you must enable the
Feedback tool in Studio.

To enable the Feedback tool in Studio, you add the ``"feedback"`` key to
the **Advanced Module List** on the **Advanced Settings** page. For more
information, see :ref:`Enable Additional Exercises and Tools`.

********************************
Add a Feedback
********************************

To add a Feedback to a course, follow these steps.

#. Go to the unit in the course outline where you want to add the
   FeedbackXBlock.

#. Under **Add New Component**, select **Advanced**.

#. Select **Provide Feedback**.

#. In the component that appears, select **Edit**, and then specify settings as
   needed.

  * The prompt for freeform feedback

  * The grayed out placeholder text a student sees before having provided
    any feedback

  * Whether the icons are happy-to-sad ("Did you like this?"),
    sad-to-happy-to-sad ("Was this too short, just right, or too long?"),
    or the numbers 1 through 5.

  * The prompt for the numerical feedback.

  * The five numerical options.

#. Select **Save**.
