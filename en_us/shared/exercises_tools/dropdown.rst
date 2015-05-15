.. _Dropdown:

#####################
Dropdown Problem
#####################

Dropdown problems allow learners to choose from a collection of answer options
that are presented in a dropdown list. Unlike :ref:`multiple choice<Multiple
Choice>` problems, which have answers that are always visible directly below
the question, dropdown problems do not show answer choices until the learner
clicks the dropdown arrow.

.. image:: ../../../shared/building_and_running_chapters/Images/DropdownExample.png
 :alt: A problem component with 3 dropdown problems, 2 marked correct and 1
     incorrect

For the dropdown problems in your course, you can use edX Insights to review
aggregated learner performance data and examine submitted answers. For
more information, see `Using edX Insights`_.

********************************
Creating a Dropdown Problem
********************************

You can create dropdown problems in the Simple Editor or in the Advanced
Editor. You can set up a problem in the Simple Editor, and then switch to the
Advanced Editor to add more configuration options in XML. However, you cannot
switch back to the Simple Editor from the Advanced Editor. Therefore, you
might want to format the problem as completely as possible before you begin to
use the Advanced Editor.
 
.. _Use the Simple Editor to Create a Dropdown Problem:

========================================================================
Use the Simple Editor to Create a Dropdown Problem
========================================================================

To use the :ref:`Simple Editor<Simple Editor>` to create a dropdown problem,
follow these steps.

#. In the unit where you want to create the problem, under **Add New
   Component** select **Problem**.
#. From the list of **Common Problem Types**, select **Dropdown**. Studio
   adds an example dropdown problem to the unit.
#. Select **Edit**. The Simple Editor opens.
#. Replace the sample problem text with your own text.
#. Determine the text that describes the question you want learners to answer,
   and surround that text with two pairs of angle brackets (``>>question<<``).
   This question text is the accessible label for the problem.
#. Edit your text to place all of the possible answers on the same line,
   separated by commas.
#. Select all of the answer options, and then select **Dropdown** from 
   the toolbar. A double set of brackets ([[ ]]) appears to surround
   the answer options.
#. To identify the problem's answer, locate that answer inside the brackets
   and surround the correct answer with parentheses.
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

::

    >>What type of data are the following?<<

    Age:
    [[Nominal, Discrete, (Continuous)]]
    Age, rounded to the nearest year:
    [[Nominal, (Discrete), Continuous]]
    Life stage - infant, child, and adult:
    [[(Nominal), Discrete, Continuous]]

========================================================================
Use the Advanced Editor to Edit a Dropdown Problem 
========================================================================

To use the Advanced Editor to edit a dropdown problem, follow these steps.

#. Follow the steps for creating the problem in the :ref:`Simple Editor<Use
   the Simple Editor to Create a Dropdown Problem>`. 
#. Select **Advanced Editor**, and then edit the XML to add the tags and
   attributes you want. An example follows.

**Problem Code**:

.. code-block:: xml

  <problem>
  <p>
    <em>This exercise first appeared in HarvardX's PH207x Health in Numbers: Quantitative Methods in Clinical &amp; Public Health Research course, fall 2012.</em>
  </p>
  <p>What type of data are the following?</p>
  <p>Age:</p>
  <optionresponse>
    <optioninput options="('Nominal','Discrete','Continuous')" correct="Continuous" label="Age"/>
  </optionresponse>
  <p>Age, rounded to the nearest year:</p>
  <optionresponse>
    <optioninput options="('Nominal','Discrete','Continuous')" correct="Discrete" label="Age, rounded to the nearest year"/>
  </optionresponse>
  <p>Life stage - infant, child, and adult:</p>
  <optionresponse>
    <optioninput options="('Nominal','Discrete','Continuous')" correct="Nominal" label="Life stage"/>
  </optionresponse>
  </problem>

.. _Dropdown Problem XML:

************************
Dropdown Problem XML
************************

========
Template
========

.. code-block:: xml

  <problem>
  <p>Question text</p>
  <optionresponse>
    <optioninput options="('Option 1','Option 2','Option 3')" correct="Option 2" label="label text"/>
  </optionresponse>
    <solution>
      <div class="detailed-solution">
      <p>Explanation or Solution Header</p>
      <p>Explanation or solution text</p>
      </div>
    </solution>
  </problem>

.. code-block:: xml

  <problem>
  <p>Question text</p>
    <optionresponse>
     options="('A','B')"
      correct="A"/>
      label="label text"
    </optionresponse>
   
    <solution>
      <div class="detailed-solution">
      <p>Explanation or Solution Header</p>
      <p>Explanation or solution text</p>
      </div>
    </solution>
  </problem>

========
Tags
========

* ``<optionresponse>`` (required): Indicates that the problem is a dropdown problem.
* ``<optioninput>`` (required): Lists the answer options.

**Tag:** ``<optionresponse>``

Indicates that the problem is a dropdown problem.

  Attributes

  (none)

  Children

  ``<optioninput>``  

**Tag:** ``<optioninput>``

Lists the answer options.

  Attributes

  .. list-table::
     :widths: 20 80

     * - Attribute
       - Description
     * - options (required)
       - Lists the answer options. The list of all answer options is
         surrounded by parentheses. Individual answer options are surrounded
         by single quotation marks (') and separated by commas (,).
     * - correct (required)
       - Indicates whether an answer is correct. Possible values are "true"
         and "false". Only one **correct** attribute can be set to "true".
     * - label (required)
       - Specifies the name of the response field.
  
  Children

  (none)



.. _Using edX Insights: http://edx.readthedocs.org/projects/edx-insights/en/latest/
