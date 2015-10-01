.. _Text Input:

########################
Text Input Problem
########################

.. contents:: 
  :local:
  :depth: 1

**********
Overview
**********

In text input problems, learners enter text into a response field. The
response can include numbers, letters, and special characters such as
punctuation marks. Because the text that the learner enters must match the
instructor's specified answer exactly, including spelling and punctuation, we
recommend that you specify more than one correct answer for text input
problems to allow for differences in capitalization and typographical errors.

.. image:: ../../../shared/building_and_running_chapters/Images/TextInputExample.png
 :alt: An example text input problem.

**************************************************
Analyzing Performance on Multiple Choice Problems
**************************************************

For the text input problems in your course, you can use edX Insights to review
aggregated learner performance data and examine submitted answers. For more
information, see `Using edX Insights`_.

******************************
Creating a Text Input Problem
******************************

You can create text input problems in the Simple Editor or in the Advanced
Editor. You can set up a problem in the Simple Editor, and then switch to the
Advanced Editor to add more configuration options in XML. However, you cannot
switch back to the Simple Editor from the Advanced Editor. Therefore, you
might want to format the problem as completely as possible before you begin to
use the Advanced Editor.

.. _Use the Simple Editor to Create a Text Input Problem:

========================================================================
Use the Simple Editor to Create a Text Input Problem
========================================================================

To use the :ref:`Simple Editor<Simple Editor>` to create a text input problem,
follow these steps.

#. In the unit where you want to create the problem, under **Add New
   Component** select **Problem**.
#. Select one of the two text input problem templates.
   
  * From the list of **Common Problem Types**, select **Text Input**. 
   
  * From the list of **Common Problems with Hints and Feedback**, select **Text
    Input with Hints and Feedback**. For more information, see `Use Feedback in
    a Text Input Problem`_.

    Studio adds the problem to the unit.

3. Select **Edit**. The Simple Editor opens. 
#. Replace the sample problem text with your own text.
#. Determine the text that describes the question you want learners to answer,
   and surround that text with two pairs of angle brackets (``>>question<<``).
   This question text is the accessible label for the problem.
#. Select the text of the problem's answer, and then select **Text Input** from
   the toolbar. An equals signe (=) appears next to the answer.

   You can identfy more than one correct answer. For more information, see
   :ref:`Multiple Responses in Text Input Problems`.

7. To provide an explanation, select the explanation text and then select 
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

    >>What was the first post-secondary school in China to allow both male and 
    female students?<<

    = Nanjing Higher Normal Institute
    or= National Central University
    or= Nanjing University

    [explanation]
    Nanjing Higher Normal Institute first admitted female students in 1920.
    [explanation]

========================================================================
Use the Advanced Editor to Edit a Text Input Problem 
========================================================================

To use the Advanced Editor to edit a text input problem, follow these steps.

#. Follow the steps for creating the problem in the :ref:`Simple Editor<Use
   the Simple Editor to Create a Text Input Problem>`. 
#. Select **Advanced Editor**, and then edit the XML to add the tags and
   attributes you want. An example follows.

**Problem Code**:

.. code-block:: xml

  <problem> 
    <p>What was the first post-secondary school in China to allow both male and female students?</p>

    <stringresponse answer="Nanjing Higher Normal Institute" type="ci" >
      <additional_answer>National Central University</additional_answer>
      <additional_answer>Nanjing University</additional_answer> 
      <textline label="What was the first post-secondary school in China to 
        allow both male and female students?" size="20"/> 
    </stringresponse>
    <solution>
      <div class="detailed-solution">
        <p>Explanation</p>
        <p>Nanjing Higher Normal Institute first admitted female students in 
        1920.</p>
      </div>
    </solution>
  </problem>

.. _Use Feedback in a Text Input Problem:

********************************************
Use Feedback in a Text Input Problem
********************************************

You can add feedback in a text input problem using the simple editor
or the advanced editor. For an overview of feedback in problems, see
:ref:`Adding Feedback and Hints to a Problem`.

In text input problems, you can provide feedback for each option that a
learner can select. 

Use feedback on correct answers to reinforce why the answer is
correct. 

Use feedback on incorrect answers as an opportunity to address common learner
misconceptions. Feedback for text input questions should also provide guidance
to the learner on how to arrive at the correct answer.

=======================================
Configure Feedback in the Simple Editor
=======================================

In the :ref:`Simple Editor<Simple Editor>`, you configure answer feedback with
the following syntax. When you create a new text input problem, select the
template  **Text Input with Hints and Feedback**. This template has example
feedback syntax that you can replace.

::

  = Correct Answer {{Feedback for learners who select this answer.}}
  not= Incorrect Answer {{Feedback for learners who select this answer.}}

For example, the following problem has feedback for the correct answer and two
common incorrect answers.

::

  >>What is the largest state in the U.S. in terms of land area?<<

  =Alaska {{Alaska is the largest state in the U.S. in terms of not only land
  area, but also total area and water area. Alaska is 576,400 square miles,
  more than double the land area of the second largest state, Texas.}}

  not=Texas {{While many people think Texas is the largest state in terms of
  land area, it is actually the second largest and contains 261,797 square
  miles.}}

  not=California {{California is the third largest state and contains 155,959
  square miles.}}


=========================================
Configure Feedback in the Advanced Editor
=========================================

In the :ref:`Advanced Editor<Advanced Editor>`, you configure answer feedback
with the following syntax.

.. code-block:: xml

    <stringresponse answer="Correct Answer" type="ci" >
      <correcthint>Hint for correct answer.</correcthint>
      <stringequalhint answer="Incorrect Anser">
        Hint for incorrect answer.
      </stringequalhint>
    </stringresponse>

For example, the following problem has feedback for the correct answer and two
common incorrect answers.

.. code-block:: xml

  <problem>

    <p>What was the first post-secondary school in China to allow both male and female students?</p>
    <stringresponse answer="Alaska" type="ci" >
      <correcthint>
        Alaska is the largest state in the U.S. in terms of not only land 
        area, but also total area and water area. Alaska is 576,400 square 
        miles, more than double the land area of the second largest state, 
        Texas.
      </correcthint>
      <stringequalhint answer="Texas">
        While many people think Texas is the largest state in terms of land 
        area, it is actually the second largest of the 50 U.S. states 
        containing 261,797 square miles.
      </stringequalhint>
      <stringequalhint answer="California">
        California is the third largest state in the U.S. in terms of land 
        area containing 155,959 square miles.</stringequalhint>
      <textline label="What is the largest state in the U.S. in terms of land 
        area?" size="20"/>
    </stringresponse>
  </problem>

=========================
Customize Feedback Labels
=========================

By default, the feedback labels shown to learners are **Correct** and
**Incorrect**. If you do not define feedback labels, learners see these terms
when they submit an answer, as in the following example.

.. image:: ../../../shared/building_and_running_chapters/Images/text_input_feedback.png
 :alt: Image of text input feedback with the standard label.
 :width: 600

You can configure the problem to override the default labels. For example, you
can configure a custom label for a specific wrong answer.

.. image:: ../../../shared/building_and_running_chapters/Images/text_input_feedback_custom_label.png
 :alt: Image of text input feedback with a custom label.
 :width: 600

.. note::
  The default labels **Correct** and **Incorrect** are displayed in the
  learner's requested language. If you provide custom labels, they are
  displayed to all users as you configure them and are not translated into
  different languages.

Customize Feedback Labels in the Simple Editor
***********************************************

In the :ref:`Simple Editor<Simple Editor>`, you configure custom feedback
labels with the following syntax.

::

  not=Answer {{Label:: Feedback}}

For example, the following feedback is configured to use a custom label.

::

  not=Texas {{Close but wrong:: While many people think Texas is the largest 
  state in terms of land area, it is actually the second largest of the 50 U.S.
  states, containing 261,797 square miles.}}

Customize Feedback Labels in the Advanced Editor
*************************************************

In the :ref:`Advanced Editor<Advanced Editor>`, you configure custom feedback
labels with the following syntax.

.. code-block:: xml

    <stringequalhint answer="Incorrect Anser" label="Custom Label">
      Feedback
    </stringequalhint>

For example, the following feedback is configured to use a custom label.

.. code-block:: xml

    <stringequalhint answer="Texas" label="Close but wrong">
      While many people think Texas is the largest state in terms of land 
      area, it is actually the second largest of the 50 U.S. states containing 
      261,797 square miles.
    </stringequalhint>

.. _Use Hints in a Text Input Problem:

********************************************
Use Hints in a Text Input Problem
********************************************

You can add hints in a text input problem, using the simple editor
or the advanced editor. For an overview of hints in problems, see
:ref:`Adding Feedback and Hints to a Problem`.

.. include:: ../../../shared/exercises_tools/Subsection_configure_hints.rst

.. _Multiple Responses in Text Input Problems:

******************************************
Multiple Responses in Text Input Problems
******************************************

You can specify more than one correct response for text input problems. For
example, instead of requiring learners to enter "Dr. Martin Luther King,
Junior" exactly, you can also allow answers of "Martin Luther King," "Doctor
Martin Luther King," and other variations. To do this, you can use the Simple
Editor or the Advanced Editor.

==============
Simple Editor
==============

To specify additional correct responses in the Simple Editor, include``or= ``
before each additional correct response.

::

    >>What African-American led the United States civil rights movement during 
    the 1960s?<<
    = Dr. Martin Luther King, Jr.
    or= Dr. Martin Luther King, Junior
    or= Martin Luther King, Jr.
    or= Martin Luther King

=====================
Advanced Editor
=====================

To specify additional correct responses in the Advanced Editor, add an
``<additional_answer>`` for each correct response inside the opening and
closing ``<stringresponse>`` tags.

.. code-block:: xml

  <problem>

  <p>What African-American led the United States civil rights movement during the 1960s?</p>
    
  <stringresponse answer="Dr. Martin Luther King, Jr." type="ci" >
    <additional_answer>Dr. Martin Luther King, Junior</additional_answer>
    <additional_answer>Martin Luther King, Jr.</additional_answer>
    <additional_answer>Martin Luther King</additional_answer>
    <textline label="What African-American led the United States civil rights 
      movement during the 1960s?" size="20"/>
  </stringresponse>
  </problem>

******************************************
Add Text after the Text Response Field
******************************************

You might want to include a word, phrase, or sentence after the answer field
in a text input problem to help guide your students or resolve ambiguity.

.. image:: ../../../shared/building_and_running_chapters/Images/MC_trailing_text.png
 :width: 500
 :alt: Multiple choice problem with the word "Institute" after the answer field.

To do this, you must use the :ref:`Advanced Editor<Advanced Editor>`.

In the problem, locate the ``textline`` element. This element creates the
response field for the problem and is a child of the ``stringresponse``
element. An example follows.

::

  <stringresponse answer="Ashmun" type="ci" >
    <textline label="What Pennsylvania school was founded in 1854 to provide 
     educational opportunities for African-Americans?" size="20" />
  </stringresponse>

To add text after the answer field, add the ``trailing_text`` attribute
together with the text that you want to use inside the ``textline`` element.

::

  <stringresponse answer="Ashmun" type="ci" >
    <textline label="What Pennsylvania school was founded in 1854 to provide educational
     opportunities for African-Americans?" size="20" trailing_text="Institute" />
  </stringresponse>


******************************************
Case Sensitivity and Text Input Problems
******************************************

By default, text input problems do not require a case sensitive response. You
can change this and require a case sensitive answer.

To make a text input response case sensitive, you must use :ref:`Advanced
Editor`.

In the Advanced Editor, you see that the ``type`` attribute of the
``stringresponse`` element equals ``ci``, for "case insensitive". An example
follows.

::

    <stringresponse answer="Michigan" type="ci">
      <textline size="20"/>
    </stringresponse>

To make the response case sensitive, change the value of the ``type``
attribute to ``cs``.

::

    <stringresponse answer="Michigan" type="cs">
      <textline size="20"/>
    </stringresponse>

*************************************************
Response Field Length in Text Input Problems
*************************************************

By default, the response field for text input problems is 20 characters long.

You should preview the unit to ensure that the length of the response input
field accommodates the correct answer, and provides extra space for possible
incorrect answers.

If the default response field length is not sufficient, you can change it
using :ref:`Advanced Editor`.

In the Advanced Editor, in the XML block for the answer, you see that the
``size`` attribute of the ``textline`` element equals ``20``.

::

    <stringresponse answer="Democratic Republic of the Congo" type="ci">
      <textline size="20"/>
    </stringresponse>

To change the response field length, change the value of the ``size``
attribute.

::

    <stringresponse answer="Democratic Republic of the Congo" type="ci">
      <textline size="40"/>
    </stringresponse>

********************************************************
Regular Expressions in Text Input Problems
********************************************************

You can configure a text input problem to allow a regular expression as an
answer. To do this, you modify the problem's XML in the Advanced Editor.

The regular expression that the learner enters must contain the part of the
answer that the course team specifies. For example, if you 
specify  ``<answer="example answer" type="regexp">``, correct answers
include ``example answered``, ``two example answers``, or even ``==example
answer==``, but not ``examples`` or ``example anser``.

You can add ``regexp`` to the value of the ``type`` attribute, for example:
``type="ci regexp"`` or ``type="regexp"`` or ``type="regexp cs"``. In this
case, any answers or hints are treated as regular expressions.

.. _Text Input Problem XML:

***********************
Text Input Problem XML
***********************

==============
Template
==============

.. code-block:: xml

  <problem>
      <p>Problem text</p>
      <stringresponse answer="Correct answer 1" type="ci regexp">
          <additional_answer>Correct answer 2</additional_answer>
          <additional_answer>Correct answer 3</additional_answer>
          <textline size="20" label="label text"/>
          <correcthint>Provides feedback when learners submit the correct response.</correcthint>
          <stringequalhint answer="Incorrect answer 1">Provides feedback when learners submit the specified incorrect response.</stringequalhint>
          <stringequalhint answer="Incorrect answer 2">Provides feedback when learners submit the specified incorrect response.</stringequalhint>
          <textline label="Which U.S. state has the largest land area?" size="20"/>
      </stringresponse>

      <demandhint>
        <hint>The first text string to display when learners request a hint.</hint>
        <hint>The second text string to display when learners request a hint.</hint>
      </demandhint>
  </problem>

=======
Tags
=======

* ``<stringresponse>``: Indicates that the problem is a text input problem. The
  ``<stringresponse>`` tag has the following child tags.

  - ``<textline>``: Creates the response field in the LMS where the learner
    enters a response.

  - ``<additional_answer>`` (optional): Specifies an additional correct answer
    for the problem. A problem can contain an unlimited number of additional
    answers.

  - ``<correcthint>`` (optional): Specifies feedback for the correct answer.

  - ``<stringequalhint>`` (optional): Specifies feedback for an incorrect
    answer.

* ``<demandhint>`` (optional): Specifies one or more hints that learners can
  request to help them arrive at the correct answer. The ``<demandhint>`` tag
  has a child tag of ``<hint>``.


**Tag:** ``<stringresponse>``

Indicates that the problem is a text input problem.

  Attributes

  .. list-table::
     :widths: 20 80

     * - Attribute
       - Description
     * - answer (required)
       - Specifies the correct answer. To designate the answer as a regular
         expression, add "regexp" to the **type** attribute. If you do not add
         "regexp" to the **type** attribute, the learner's answer must match
         the value in this attribute exactly.
     * - type (optional)
       - Specifies whether the problem requires a case sensitive response and
         if it allows regular expressions. 

         * If the ``<stringresponse>`` tag includes ``type="ci"``, the problem
           is not case sensitive.
         * If the tag includes ``type="cs"``, the problem is case sensitive.
         * If the tag includes ``type="regexp"``, the problem allows regular
           expressions.

         A **type** attribute in a ``<stringresponse>`` tag can also combine
         these values. For example, ``<stringresponse type="regexp cs">``
         specifies that the prolem allows regular expressions and is case
         sensitive.


  Children

  * ``<textline />`` (required)
  * ``<additional_answer>`` (optional)
  * ``<correcthint>`` (optional)
  * ``<stringequalhint>`` (optional)
    
**Tag:** ``<textline />``
 
Creates a response field in the LMS where the learner enters a response.

  Attributes

  .. list-table::
     :widths: 20 80

     * - Attribute
       - Description
     * - label (required)
       - Contains the text of the problem.
     * - size (optional)
       - Specifies the size, in characters, of the response field in the LMS.
     * - hidden (optional)
       - If set to "true", learners cannot see the response field.
     * - correct_answer (optional)
       - Lists the correct answer to the problem.
     * - trailing_text
       - Adds the text that you specify after the response field.

  Children
  
  (none)

**Tag:** ``<additional_answer>``

Specifies an additional correct answer for the problem. A problem can contain
an unlimited number of additional answers.

  Attributes

  (none)

  Children

  (none)

**Tag:** ``<correcthint>``

Indicates that the course team has provided hints for certain common incorrect
answers.

  Attributes

  (none)

  Children
  
  (none)

**Tag:** ``<stringequalhint>``

Specifies the feedback for an incorrect answer.

  Attributes

  .. list-table::
     :widths: 20 80

     * - Attribute
       - Description
     * - answer (required)
       - The text of the incorrect answer.

  Children

  (none)

**Tag:** ``<demandhint>``

Specifies one or more hints that learners can request to help them arrive at
the correct answer.

  Attributes

  (none)

  Children

**Tag:** ``<hint>``
 
Contains the text of a hint. The LMS shows each of the defined hints to the
learners in the order that the ``<hint>`` tags  are included within the
``<demandhint>`` tag.

**************************
Deprecated Hinting Method
**************************

The following example shows the XML format with the ``<hintgroup>`` element
that you could use in the past to configure hints for text input problems.
Problems using this XML format will continue to work in the edX Platform.
However, edX recommends that you use the new way of configuring hints
documented above.

.. code-block:: xml

  <problem>
      <p>Problem text</p>
      <stringresponse answer="Correct answer 1" type="ci regexp">
          <additional_answer>Correct answer 2</additional_answer>
          <additional_answer>Correct answer 3</additional_answer>
          <textline size="20" label="label text"/>
          <hintgroup>
              <stringhint answer="Incorrect answer A" type="ci" name="hintA" />
                <hintpart on="hintA">
                    <startouttext />Text of hint for incorrect answer A<endouttext />
                </hintpart >
              <stringhint answer="Incorrect answer B" type="ci" name="hintB" />
                <hintpart on="hintB">
                    <startouttext />Text of hint for incorrect answer B<endouttext />
                </hintpart >
              <stringhint answer="Incorrect answer C" type="ci" name="hintC" />
                <hintpart on="hintC">
                    <startouttext />Text of hint for incorrect answer C<endouttext />
                </hintpart >
          </hintgroup>
      </stringresponse>
      <solution>
      <div class="detailed-solution">
      <p>Explanation or Solution Header</p>
      <p>Explanation or solution text</p>
      </div>
    </solution>
  </problem>

.. _Using edX Insights: http://edx.readthedocs.org/projects/edx-insights/en/latest/
