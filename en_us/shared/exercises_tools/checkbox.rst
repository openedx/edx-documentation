.. _Checkbox:

##################
Checkbox Problem
##################

In checkbox problems, learners select one or more options from a list of
possible answers. To answer the problem correctly, a learner must select all
of the options that apply. Each checkbox problem must have at least one
correct answer.

.. image:: ../../../shared/building_and_running_chapters/Images/CheckboxExample.png
 :alt: A checkbox problem with four options, 2 of which are required for the
     correct answer

For the checkbox problems in your course, you can use edX Insights to review
aggregated learner performance data and examine submitted answers. For more
information, see `Using edX Insights`_.

****************************
Creating a Checkbox Problem
****************************

You can create checkbox problems in the Simple Editor or in the Advanced
Editor. You can set up a problem in the Simple Editor, and then switch to the
Advanced Editor to add more configuration options in XML. However, you cannot
switch back to the Simple Editor from the Advanced Editor. Therefore, you
might want to format the problem as completely as possible before you begin to
use the Advanced Editor.

.. _Use the Simple Editor to Create a Checkbox Problem:

======================================================
Use the Simple Editor to Create a Checkbox Problem
======================================================

To use the :ref:`Simple Editor<Simple Editor>` to create a checkbox problem,
follow these steps.

#. In the unit where you want to create the problem, under **Add New
   Component** select **Problem**.
#. From the list of **Common Problem Types**, select **Checkboxes**. Studio
   adds an example checkbox problem to the unit.
#. Select **Edit**. The Simple Editor opens. 
#. Replace the sample problem text with your own text.
#. Determine the text that describes the question you want learners to answer,
   and surround that text with two pairs of angle brackets (``>>question<<``).
   This question text is the accessible label for the problem.
#. Edit your text to place each answer option on a separate line.
#. Select your set of answer options, and then select **Checkboxes** from the
   toolbar. A pair of brackets appears next to each answer choice.
#. To identify each correct answer, add an **x** between the brackets for that option.
#. To provide an explanation, select the explanation text and then select 
   **Explanation** from the toolbar. ``[explanation]`` appears before
   and after the explanation text.
#. Select **Settings** and provide an identifying **Display Name** for the
   problem.
#. Define additional settings for the problem. For more information, see
   :ref:`Problem Settings`.
#. Select **Save**.

For the example problem illustrated above, the following text displays in the
problem component.

.. code-block:: xml

    Learning about the benefits of preventative healthcare can be particularly 
    difficult. >>Check all of the reasons below why this may be the case.<<

    [x] A large amount of time passes between undertaking a preventative measure and seeing the result. 
    [ ] Non-immunized people will always fall sick. 
    [x] If others are immunized, fewer people will fall sick regardless of a particular individual's choice to get immunized or not. 
    [x] Trust in healthcare professionals and government officials is fragile. 

.. please do not line wrap this example:

    [explanation]
    People who are not immunized against a disease may still not fall sick from the disease. If someone is trying to learn whether or not preventative measures against the disease have any impact, he or she may see these people and conclude, since they have remained healthy despite not being immunized, that immunizations have no effect. Consequently, he or she would tend to believe that immunization (or other preventative measures) have fewer benefits than they actually do.
    [explanation]


========================================================================
Use the Advanced Editor to Edit a Checkbox Problem 
========================================================================

To use the :ref:`Advanced Editor<Advanced Editor>` to edit a checkbox
problem, follow these steps.

#. Follow the steps for creating the problem in the :ref:`Simple Editor<Use
   the Simple Editor to Create a Checkbox Problem>`.
#. Select **Advanced Editor**, and then edit the XML to add the tags and
   attributes you want. An example follows.

.. code-block:: xml

  <problem>
  <p>Learning about the benefits of preventative healthcare can be particularly difficult. Check all of the reasons below why this may be the case.</p>

  <choiceresponse>
    <checkboxgroup label="Check all of the reasons below why this may be the case">
      <choice correct="true"><text>A large amount of time passes between undertaking a preventative measure and seeing the result.</text></choice>
      <choice correct="false"><text>Non-immunized people will always fall sick.</text></choice>
      <choice correct="true"><text>If others are immunized, fewer people will fall sick regardless of a particular individual's choice to get immunized or not.</text></choice>
      <choice correct="true"><text>Trust in healthcare professionals and government officials is fragile.</text></choice>
    </checkboxgroup>
  </choiceresponse>

   <solution>
   <div class="detailed-solution">
   <p>Explanation</p>
   <p>People who are not immunized against a disease may still not fall sick from the disease. If someone is trying to learn whether or not preventative measures against the disease have any impact, he or she may see these people and conclude, since they have remained healthy despite not being immunized, that immunizations have no effect. Consequently, he or she would tend to believe that immunization (or other preventative measures) have fewer benefits than they actually do.</p>
   </div>
   </solution>
  </problem>

.. _Checkbox Problem XML:

****************************
Checkbox Problem XML 
****************************

============
Template
============

.. code-block:: xml

  <problem>
  <p>Question text</p>

  <choiceresponse>

  <checkboxgroup label="label text">
  <choice correct="false"><text>Answer option 1 (incorrect)</text></choice>
  <choice correct="true"><text>Answer option 2 (correct)</text></choice>
  </checkboxgroup>
  </choiceresponse>

   <solution>
   <div class="detailed-solution">
   <p>Solution or Explanation Heading</p>
   <p>Solution or explanation text</p>
   </div>
   </solution>

  </problem>

======
Tags
======

* ``<choiceresponse>`` (required): Specifies that the problem contains options
  for learners to choose from.
* ``<checkboxgroup>`` (required): Specifies that the problem is a checkbox problem.
* ``<choice>`` (required): Designates an answer option.

**Tag:** ``<choiceresponse>``

Specifies that the problem contains options for learners to choose from.

  Attributes

  (none)

  Children

  ``<checkboxgroup>``

**Tag:** ``<checkboxgroup>``

Specifies that the problem is a checkbox problem.

  Attributes

  .. list-table::
     :widths: 20 80

     * - Attribute
       - Description
     * - label (required)
       - Specifies the name of the response field.

  Children

  ``<choice>`` 

**Tag:** ``<choice>``

Designates an answer option.

  Attributes

  .. list-table::
     :widths: 20 80

     * - Attribute
       - Description
     * - true (at least one required)
       - Indicates a correct answer. For checkbox problems, one or more
         ``<choice>`` tags can contain a correct answer.
     * - false (at least one required)
       - Indicates an incorrect answer.

  Children
  
  (none)


.. _Using edX Insights: http://edx.readthedocs.org/projects/edx-insights/en/latest/
