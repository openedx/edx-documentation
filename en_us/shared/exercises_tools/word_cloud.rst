.. _Word Cloud:

##################
Word Cloud Tool
##################

.. note:: EdX offers provisional support for this tool.

In a word cloud, students enter words into a field in response
to a question or prompt. The words that all of the students enter then
appear instantly as a colorful graphic, with the most popular responses
appearing largest. The graphic becomes larger as more students answer.
Students can both see the way their peers have answered and contribute
their thoughts to the group.

For example, the following word cloud was created from students'
responses to a question in a HarvardX course.

.. image:: ../../../shared/images/WordCloudExample.png
  :alt: Image of a word cloud problem.

.. contents::
   :local:
   :depth: 2

************************************************
Enable the Word Cloud Tool
************************************************

Before you can add a word cloud to your course, you must enable the word cloud
tool.

To enable the word cloud tool in Studio, you add the ``"word_cloud"`` key to
the **Advanced Module List** on the **Advanced Settings** page. (Be sure to
include the quotation marks around the key value.) For more information, see
:ref:`Enable Additional Exercises and Tools`.

****************************
Create a Word Cloud
****************************

To create a word cloud, follow these steps.

#. In the unit where you want to create the problem, select **Advanced**
   under **Add New Component**.
#. In the list of problem types, select **Word Cloud**.
#. In the component that appears, select **Edit**.
#. In the component editor, specify the settings that you want. You can
   leave the default value for everything except **Display Name**.

   * **Display Name**: This name appears as a heading above the problem.
   * **Inputs**: The number of text boxes into which students can enter words,
     phrases, or sentences.
   * **Maximum Words**: The maximum number of words that the word cloud
     displays. If students enter 300 different words but the maximum is set to
     250, only the 250 most commonly entered words appear in the word cloud.
   * **Show Percents**: The number of times that students have entered a given
     word as a percentage of all words entered appears near that word.

#. Select **Save**.
