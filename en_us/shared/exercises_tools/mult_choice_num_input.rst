.. _Multiple Choice and Numerical Input:

############################################
Multiple Choice and Numerical Input Problem
############################################

.. note:: EdX offers provisional support for this problem type.

You can create a problem that combines a multiple choice and numerical input
problems. Students not only select a response from options that you provide,
but also provide more specific information, if necessary.

.. image:: ../../../shared/images/MultipleChoice_NumericalInput.png
  :alt: Image of a multiple choice and numerical input problem

.. note::
 Currently, students can only enter numerals in the text field. Students
 cannot enter words or mathematical expressions, which might be confusing to
 students who are accustomed to other edX numerical input fields.

 You can make a calculator available to your learners on every courseware
 page. For more information, see :ref:`Calculator`.

.. _Create an MCNI Problem:

********************************************************
Create a Multiple Choice and Numerical Input Problem
********************************************************

To create a multiple choice and numerical input problem:

#. In the unit where you want to create the problem, click **Problem** under
   **Add New Component**, and then click the **Advanced** tab.
#. Click **Blank Advanced Problem**.
#. In the component that appears, click **Edit**.
#. In the component editor, paste the code from below.
#. Replace the example problem and response options with your own text.
#. Click **Save**.

.. _MCNI Problem Code:

************************************************
Multiple Choice and Numerical Input Problem Code
************************************************

.. code-block:: xml

  <problem>
  The numerical value of pi, rounded to two decimal places, is 3.24.
    <choicetextresponse>
      <radiotextgroup>
        <choice correct="false">True.</choice>
        <choice correct="true">False. The correct value is <numtolerance_input answer="3.14"/>.</choice>
      </radiotextgroup>
    </choicetextresponse>
  </problem>
