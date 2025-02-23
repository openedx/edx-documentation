.. _Numerical Input:

########################
Numerical Input Problem
########################

.. note:: EdX offers full support for this problem type.

The numerical input problem type is a simple problem type that can be added to
any course. At a minimum, numerical input problems include a question or
prompt and a response field for a numeric answer. By adding hints, feedback, or
both, you can give learners guidance and help when they work on a problem.

.. contents::
  :local:
  :depth: 2

For more information about the simple problem types, see
:ref:`Working with Problem Components`.

**********
Overview
**********

In numerical input problems, learners enter numbers or specific and relatively
simple mathematical expressions to answer a question. The LMS automatically
converts the answer that learners enter into a symbolic expression that appears
below the response field.

Responses for numerical input problems can include integers, fractions, and
constants such as pi and *g*. Responses can also include text representing
common functions, such as square root (sqrt) and log base 2 (log2), as well as
trigonometric functions and their inverses, such as sine (sin) and arcsine
(arcsin). For these functions, learners enter text that is converted into
mathematical symbols. The following example shows a response entered by a
learner and the numerical expression that results.

.. image:: ../../../shared/images/Math5.png
 :alt: A learner typed n*x^(n-1) to enter the symbolic expression n times x to
     the n minus 1 power.

For more information about how learners enter expressions, see
:ref:`learners:Math Formatting` in the *EdX Learner's Guide* or
:ref`Math Formatting` in the *Open edX Learner's Guide*.

Some of the options for numerical input problems include the following.

* You can specify a correct answer explicitly or use a Python script.

* You can specify a margin of error, or tolerance, for the answers to numerical
  input problems so that learners' responses do not have to be exact.

.. note::
  You can make a calculator tool available to your learners on every unit
  page. For more information, see :ref:`Calculator`.

================================
Example Numerical Input Problem
================================

In the LMS, learners enter a value into a response field to complete a
numerical input problem. An example of a completed numerical input problem follows.

.. image:: ../../../shared/images/NumericalInputExample.png
 :alt: A problem with one question, answered correctly, in the LMS.

***********************************
Adding a Numerical Input Problem
***********************************

You add numerical input problems in Studio by selecting the **Problem**
component. In the problem editor, select the **Numerical Input** option. Fill in
the fields on this screen to create your problem.

.. image:: ../../../shared/images/problem_editor_numerical_input.png
 :alt: An example numerical input problem in the problem editor with number
    indicators labeling the various features.
 :width: 800

Creating a numerical input problem is as simple as:

#. Editing the **Display Name**. Click the pen symbol to edit.
#. Filling in the **Question** field.
#. Filling in the **Explanation** field. When this is shown to learners is
   based on the selection in the **Show answer** panel on the right.
#. Filling in the **Answer** fields. For numerical input problems, only correct
   answers can be added here. Additional answers can be added by clicking the
   **Add answer** button. Answers can be deleted by clicking the trash can icon.
   Feedback can be provided for each answer. More information on feedback can be
   found in the following section.
#. Selecting and filling in any desired settings on the right.

.. note:: Only correct answers can be added to a numerical input problem.

If you have any questions on the specifics of using the simple editor, please check
out :ref:`Simple Editor` and :ref:`Problem Settings`.

============================================================
Adding a Tolerance or a Range
============================================================

To give learners the option to receive full credit for a close approximation of
the correct answer, and to support a wide range of possible correct numerical
answers, you can specify a tolerance for the correct answer or a range of values
to mark as correct for the numerical input problem type.

.. contents::
  :local:
  :depth: 1

.. note:: You can either have a **tolerance** or an **answer range** for a
  numerical input problem. You cannot add both.

-------------------
Adding a Tolerance
-------------------

You can specify a margin of error or tolerance for learner responses. You
can specify a percentage or number. The tolerance settings panel can be
found to the right of the editor.

.. image:: ../../../shared/images/problem_editor_tolerance_box.png
 :alt: An example tolerance setting set to 5%.
 :width: 200

--------------------------------------
Specifying an Answer Range
--------------------------------------

You can specify an answer range so that any learner response within that range
is marked correct.

Add an answer range by selecting the **Add answer range** button from the 
**Add answer** dropdown. This option can only be selected if you only have one
answer. This will replace your answer field with an answer range field.

.. image:: ../../../shared/images/problem_editor_answer_range_box.png
 :alt: An example answer range set from 1 to 10. This includes 1 but not 10.
 :width: 200

To format an answer range, you provide the starting and
ending values and then separate them with a comma character (``,``). You then
surround the range with bracket (``[ ]``) or parentheses characters (``( )``),
or a combination of one bracket and one parenthesis.

* Use a bracket to include the number next to it in the range, as in a less
  than or equal to, or greater than or equal to, inequality.

* Use a parenthesis to exclude the number from the range, as in a less than or
  greater than inequality.

For example, to identify the correct answers as 5, 6, or 7, but not 8, specify
``[5,8)``. To identify the correct answers as 6, 7, and 8, but not 5, specify
``(5,8]``.

.. _Use Feedback in a Numerical Input Problems:

=================
Adding Feedback
=================

For an overview of feedback in problems, see :ref:`Adding Feedback and Hints to
a Problem`. In numerical input problems, you can provide feedback for correct
responses. If you define multiple correct responses, you can define feedback
for each response. In numerical input problems, use feedback to reinforce the
process used to arrive at the correct answer.

You can add answer-specific feedback for each answer in a numerical input problem.
You can access the feedback panel shown below by clicking the button to the right
of the answer text.

.. image:: ../../../shared/images/problem_editor_feedback_box_2.png
 :alt: An example of an expanded feedback section for dropdown problems showing 
    the 'is selected' feedback field.
 :width: 600

Simply enter your feedback message in this text field. It will display when the
learner submits this answer.

.. note:: You cannot add feedback for an incorrect answer in numerical input
  problems. Add hints to guide the learners in the correct direction instead.

.. _Use Hints in a Numerical Input Problem:

=================
Adding Hints
=================

You can add hints to a numerical input problem using the simple editor or the
advanced editor. For an overview of hints in problems, see
:ref:`Adding Feedback and Hints to a Problem`.

.. include:: ../../../shared/exercises_tools/Subsection_configure_hints.rst

.. _Editing Numerical Input Problems using the Advanced Editor:

**************************************************************
Editing Numerical Input Problems using the Advanced Editor
**************************************************************

If the simple editor is not enough to meet your needs, you can switch over to the
advanced editor. In the setting panels on the right of the editor, click 
**Show advanced settings**, then scroll down and click 
**Switch to advanced editor**.

You can use the advanced editor to identify the elements of a numerical input problem
with OLX. For more information, see :ref:`Numerical Input Problem XML`. To format
equations, you can use MathJax. For more information, see :ref:`MathJax in Studio`.

You can see the OLX for the example problem from the Overview section below.

.. code-block:: xml

  <problem>
    <numericalresponse answer="10">
      <label>In what base is the decimal numeral system?</label>
      <formulaequationinput/>
      <solution>
        <div class="detailed-solution">
          <p>Explanation</p>
          <p>The decimal numeral system is base ten.</p>
        </div>
      </solution>
    </numericalresponse>
  </problem>

.. note:: You can begin work on the problem in the simple editor, and then
  switch to the advanced editor. However, after you save any advanced OLX
  changes you make in the advanced editor, you may not be able to cannot
  switch back to the simple editor.

===================
Adding Feedback
===================

In the advanced editor, you configure feedback with the following syntax.

.. code-block:: xml

  <problem>
    <numericalresponse answer="Correct Answer">
      <label>Question text</label>
      <formulaequationinput />
      <correcthint>Feedback for the correct answer</correcthint>
    </numericalresponse>
  </problem>

For example, the following problem has feedback for each answer.

.. code-block:: xml

  <problem>
    <numericalresponse answer="4">
      <label>What is the arithmetic mean for the following set of numbers?
      (1, 5, 6, 3, 5)</label>
      <formulaequationinput />
      <correcthint>The mean for this set of numbers is 20 / 5 which equals 4.</correcthint>
    </numericalresponse>
  </problem>

If you define multiple correct responses, you can define feedback for each response.

.. include:: ../../../shared/exercises_tools/Subsection_customizing_feedback_labels.rst

===================
Adding Hints
===================

.. include:: ../../../shared/exercises_tools/Subsection_configure_hints_advanced.rst

.. _Multiple Responses in Numerical Input Problems:

=========================================
Adding Multiple Correct Responses
=========================================

You can specify more than one specific, correct response for numerical input problems.
To do this, use the advanced editor.

If you specify multiple correct responses, you cannot also specify a tolerance, a range,
or a text string as correct answers. For example, when you define multiple correct
responses, you can specify a numeric value for each correct answer but not a tolerance,
range, or text string.

To specify an additional correct response in the advanced editor, within the
``<numericalresponse>`` element add the ``<additional_answer />`` element with an
``answer=""`` attribute value.

.. code-block:: xml

  <problem>
    <numericalresponse answer="9.3*10^7">
      <label>How many miles away from Earth is the sun?</label>
      <description>Use scientific notation to answer.</description>
      <additional_answer answer="9.296*10^7"/>
      <formulaequationinput/>
    </numericalresponse>
  </problem>

=========================================
Adding a Tolerance
=========================================

You can specify a margin of error or tolerance for learner responses. You can
specify a percentage, number, or range.

To add a tolerance in the advanced editor you include a ``<responseparam>``
element with a ``type="tolerance"`` attribute and a ``default`` attribute set
to either a number or a percentage value.

The following example shows a problem with a decimal tolerance.

.. code-block:: xml

  <problem>
    <numericalresponse answer="ANSWER (NUMBER)">
      <label>Question text</label>
      <responseparam type="tolerance" default=".02" />
      <formulaequationinput />
    </numericalresponse>
  </problem>

The following example shows a problem with a percentage tolerance.

.. code-block:: xml

  <problem>
    <numericalresponse answer="ANSWER (NUMBER)">
      <label>Question text</label>
      <responseparam type="tolerance" default="3%" />
      <formulaequationinput />
    </numericalresponse>
  </problem>

=========================================
Specifying an Answer Range
=========================================

You can specify an answer range so that any learner response within that
range is marked correct. To format an answer range, you provide the starting
and ending values and then separate them with a comma character (``,```). You
then surround the range with bracket (``[ ]``) or parentheses characters
(``( )``), or a combination of one bracket and one parenthesis.

* Use a bracket to include the number next to it in the range, as in a less
  than or equal to, or greater than or equal to, inequality.

* Use a parenthesis to exclude the number from the range, as in a less than or
  greater than inequality.

For example, to identify the correct answers as 5, 6, or 7, but not 8, specify
``[5,8)``. To identify the correct answers as 6, 7, and 8, but not 5, specify
``(5,8]``.

To specify a range in the advanced editor, you enter the complete, formatted
range in the ``<numericalresponse>`` element as the value for the ``answer``
attribute: ``<numericalresponse answer="[5,8)">`` or 
``<numericalresponse answer="(5,8]">``.


.. _Awarding Partial Credit in a Numerical Input Problem:

=========================================
Awarding Partial
=========================================

You can configure a numerical input problem to award partial credit to learners
who submit an answer that is close or related to the correct answer. You must
use the :ref:`advanced editor<Advanced Editor>` to configure partial credit.

.. only:: Partners

 .. note::
    Support for partial credit problems in courses on edx.org and edX
    Edge is provisional. Ensure that you test such problems thoroughly before
    releasing them to learners. For more information, contact your edX partner
    manager.

In the following example, the learner entered an answer that was close to the
correct answer and received partial credit.

.. image:: ../../../shared/images/partial_credit_numerical_input.png
 :alt: A numerical input problem with partial credit for a close answer.


For an overview of partial credit in problems, see
:ref:`Awarding Partial Credit for a Problem`.

You can use the following methods to award partial credit in a numerical input
problem.

.. contents::
  :local:
  :depth: 1

.. note:: You can use these methods of awarding partial credit individually or
 in combination.

--------------------------
Identifying Close Answers
--------------------------

You can configure a numerical input problem so that answers that are close to
the correct answer receive partial credit.

To do so, you configure the tolerance for incorrect answers. Learners receive
partial credit for close answers based on the tolerance. By default, the
tolerance is multiplied by 2 and the following rules are applied.

* An answer within the tolerance receives 100% of the points for the problem.

* An answer within or equal to 2x of the tolerance receives 50%.

* An answer more than 2x the outside of the tolerance receives 0%.

You can optionally specify a different multiplier for the tolerance. For
example, you could set the multiplier to 3. In this case, the following rules
apply.

* An answer within the tolerance receives 100% of the points for the problem.

* An answer within or equal to 3x of the tolerance receives 50%.

* An answer more than 3x outside of the tolerance receives 0%.

^^^^^^^^^^^^^^^^^^^^^^^^
Configure Close Answers
^^^^^^^^^^^^^^^^^^^^^^^^

To configure a numerical input problem to award partial credit for close
answers, you add the following attributes to the problem XML.

* Add the ``partial_credit="close"`` attribute to the ``<numericalresponse>``
  element.

  You can use close answers in combination with a list. Set the
  attribute to ``partial_credit="close,list"``.

* Optionally, add the ``partial_range`` attribute to the ``<responseparam>``
  element and set its value to the tolerance multiplier. If you do not set the
  ``partial_range`` attribute, 2 is used as the tolerance multiplier.

For example, the following OLX shows a numerical problem that provides partial
credit for close answers.

.. code-block:: xml

  <problem>
    <numericalresponse answer="9.3*10^7" partial_credit="close">
      <label>How many miles away from Earth is the sun?</label>
      <description>Use scientific notation to answer.</description>
      <formulaequationinput/>
      <responseparam type="tolerance" default="1%" partial_range="3"/>
    </numericalresponse>
  </problem>

----------------------------------------------------
Awarding Partial Credit for Answers in a List
----------------------------------------------------

For some numerical input problems, mistakes do not help a learner arrive at the
correct answer. For example, a small mistake can lead to negative instead of
positive results, or to an answer that is off by a square root or numerical
factor.

For these types of problems, you can configure a list of wrong answers that
receive partial credit. Learners who submit answers that are on the list
receive 50% of the problem's points.

^^^^^^^^^^^^^^^^^^
Configure a List
^^^^^^^^^^^^^^^^^^

To configure a numerical input problem to award partial credit for answers in a
list, you add the following attributes to the problem XML.

* Add the ``partial_credit="list"`` attribute to the ``<numericalresponse>``
  element.

  You can use a list in combination with close answers. Set the
  attribute to ``partial_credit="close,list"``.

* Add the ``partial_answers`` attribute to the ``<responseparam>`` element. Set
  its value to one or more answers that should earn 50% of the problem's
  points. Separate multiple values by a comma (,).

For example, the following XML shows the numerical problem template
updated to provide partial credit for a different answer.

.. code-block:: xml

  <problem>
    <numericalresponse answer="9.3*10^7" partial_credit="close">
      <label>How many miles away from Earth is the sun?</label>
      <description>Use scientific notation to answer.</description>
      <formulaequationinput />
      <responseparam partial_answers="150*10^6"/>
    </numericalresponse>
  </problem>

=============================================
Adding Text after the Numeric Response Field
=============================================

You might want to include a word, phrase, or sentence after the response field
in a numerical input problem to help guide your students or resolve ambiguity.

.. image:: ../../../shared/images/NI_trailing_text.png
 :width: 500
 :alt: Three numerical input problems with text after the response field:
     "km", a percent sign, and a symbol for meters per second squared.

To do this, you use the advanced editor.

In the problem, locate the ``formulaequationinput`` element. This element
creates the response field for the problem and is a child of the
``numericalresponse`` element.

To add text after the response field, add the ``trailing_text`` attribute
together with the symbol or text that you want to use inside the
``formulaequationinput`` element. An example problem follows with three
questions that use this attribute.

.. note:: You can use MathJax inside the ``trailing_text`` attribute, as the
 third question in this example shows. You cannot use HTML inside this
 attribute.

.. code-block:: xml

  <problem>
    <numericalresponse answer="12.87">
      <label>How far is 8 miles in kilometers?</label>
      <formulaequationinput trailing_text="km" />
    </numericalresponse>

    <numericalresponse answer="91">
      <label>According to the Pew Research Center's Internet and American Life
       Project, what percentage of the world's population had a cellular phone
       as of May 2013?</label>
      <formulaequationinput trailing_text="%" />
    </numericalresponse>

    <numericalresponse answer="9.81">
      <label>What is the strength of Earth's gravity, to two decimal places?</label>
      <formulaequationinput trailing_text="\(m/s^{2}\)" />
    </numericalresponse>
  </problem>

.. _Numerical Input Problem XML:

*************************************
Numerical Input Problem OLX Reference
*************************************

=========
Templates
=========

The following templates represent problems without, and with, a Python script.

--------------------------
Problem with No Tolerance
--------------------------

.. code-block:: xml

  <problem>
    <numericalresponse answer="ANSWER (NUMBER)">
      <label>Question text</label>
      <description>Optional tip</description>
      <formulaequationinput />
      <correcthint>Feedback for the correct answer.</correcthint>
      <solution>
        <div class="detailed-solution">
          <p>Explanation</p>
          <p>TEXT OF SOLUTION</p>
        </div>
      </solution>
    </numericalresponse>
  </problem>

------------------------------
Answer Created Using a Script
------------------------------

.. note:: The following example includes a Python script. When you add a
  script to a problem component, make sure that it is not indented. A "jailed
  code" error message appears when you save the problem in Studio if the script
  element is indented.

.. code-block:: xml

  <problem>
    <numericalresponse answer="$computed_response">
      <label>Question text</label>
      <description>Optional tip</description>
      <responseparam type="tolerance" default="0.0001" />
  <script type="loncapa/python">
  computed_response = math.sqrt(math.fsum([math.pow(math.pi,2), math.pow(math.e,2)]))
  </script>
      <formulaequationinput />
      <correcthint>Feedback for the correct answer.</correcthint>
      <solution>
        <div class="detailed-solution">
          <p>Explanation</p>
          <p>TEXT OF SOLUTION</p>
        </div>
      </solution>
    </numericalresponse>
  </problem>

=========
Elements
=========

For numerical input problems, the ``<problem>`` element can include this
hierarchy of child elements.

.. code-block:: xml

  <numericalresponse>
      <label>
      <description>
      <formulaequationinput>
      <additional_answer>
      <correcthint>
      <responseparam>
      <script>
      <solution>
  <demandhint>
      <hint>

In addition, standard HTML tags can be used to format text.

------------------------
``<numericalresponse>``
------------------------

Required. Indicates that the problem is a numerical input problem.

The ``<numericalresponse>`` element is similar to the ``<formularesponse>``
element used by the :ref:`math expression input<Math Expression Input>` problem
type, but the ``<numericalresponse>`` element does not allow unspecified
variables.

^^^^^^^^^^^^^^^^^^^^
Attributes
^^^^^^^^^^^^^^^^^^^^

.. list-table::
  :widths: 20 80
  :header-rows: 1

  * - Attribute
    - Description
  * - ``answer``
    - Required. The correct answer to the problem, given as a mathematical
      expression.
  * - ``partial_credit``
    - Optional. Specifies the type of partial credit given. ``close``,
      ``list``, or a combination of both in any order separated by a comma (,).

.. note:: If you include a variable name preceded with a dollar sign
 ($) in the problem ``answer``, you can include a script in the problem that
 computes the expression in terms of that variable.

The grader evaluates the answer that you provide and the learner's response
in the same way. The grader also automatically simplifies any numeric
expressions that you or a learner provides. Answers can include simple
expressions such as "0.3" and "42", or more complex expressions such as
"1/3" and "sin(pi/5)".

^^^^^^^^^^^^^^^^^^^^
Children
^^^^^^^^^^^^^^^^^^^^

* ``<label>``
* ``<description>``
* ``<formulaequationinput>``
* ``<additional_answer>``
* ``<responseparam>``
* ``<correcthint>``
* ``<script>``
* ``<solution>``

------------------------
``<label>``
------------------------

Required. Identifies the question or prompt. You can include HTML tags within
this element.

^^^^^^^^^^^^^^^^^^^^
Attributes
^^^^^^^^^^^^^^^^^^^^

None.

^^^^^^^^^^^^^^^^^^^^
Children
^^^^^^^^^^^^^^^^^^^^

None.

------------------------
``<description>``
------------------------

Optional. Provides clarifying information about how to answer the question. You
can include HTML tags within this element.

^^^^^^^^^^^^^^^^^^^^
Attributes
^^^^^^^^^^^^^^^^^^^^

None.

^^^^^^^^^^^^^^^^^^^^
Children
^^^^^^^^^^^^^^^^^^^^

None.

--------------------------
``<formulaequationinput>``
--------------------------

Required. Creates a response field in the LMS where learners enter a response.

.. note::
    Some older problems use a ``<textline math="1" />`` element instead of
    ``<formulaequationinput>``. However, the ``<textline math="1" />``
    element has been deprecated. All new problems should use the
    ``<formulaequationinput>`` element.

^^^^^^^^^^^^^^^^^^^^
Attributes
^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``size``
     - Optional. Defines the width, in characters, of the response field in
       the LMS.
   * - ``trailing_text``
     - Optional. Specified text to appear immediately after the response field.

^^^^^^^^^^^^^^^^^^^^
Children
^^^^^^^^^^^^^^^^^^^^

None.

--------------------------
``<additional_answer>``
--------------------------

Optional. Specifies an additional correct answer for the problem. A problem can
contain an unlimited number of additional answers.

^^^^^^^^^^^^^^^^^^^^
Attributes
^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``answer``
     - Required. The alternative correct answer.

^^^^^^^^^^^^^^^^^^^^
Children
^^^^^^^^^^^^^^^^^^^^

``correcthint``

--------------------------
``<responseparam>``
--------------------------

Specifies a tolerance, or margin of error, for an answer.

^^^^^^^^^^^^^^^^^^^^
Attributes
^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``type``
     - Optional. ``"tolerance"`` defines a tolerance for a number.
   * - ``default``
     - Optional. A number or a percentage specifying a numerical or percent
        tolerance.
   * - ``partial_range``
     - Optional. For partial credit problems of ``type="close"``, a
       multiplier for the tolerance. Default is 2.
   * - ``partial_answers``
     - Optional. For partial credit problems of ``type="list"``, a comma-
         separated list of values that are to receive 50% credit.

^^^^^^^^^^^^^^^^^^^^
Children
^^^^^^^^^^^^^^^^^^^^

None.

--------------------------
``<correcthint>``
--------------------------

Optional. Specifies feedback to appear after the learner submits the correct
answer.

^^^^^^^^^^^^^^^^^^^^
Attributes
^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 20 80

   * - Attribute
     - Description
   * - ``label``
     - Optional. The text of the custom feedback label.

^^^^^^^^^^^^^^^^^^^^
Children
^^^^^^^^^^^^^^^^^^^^

None.

--------------------------
``<script>``
--------------------------

Optional. Specifies a script that the grader uses to evaluate a learner's
response. A problem behaves as if all of the code in all of the ``<script>``
elements were in a single ``<script>`` element. Specifically, any variables
that are used in multiple ``<script>`` elements share a namespace and can be
overridden.

As with all Python, indentation matters, even though the code is embedded in
XML.

^^^^^^^^^^^^^^^^^^^^
Attributes
^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``type``
     - Required. Must be set to ``loncapa/python``.

^^^^^^^^^^^^^^^^^^^^
Children
^^^^^^^^^^^^^^^^^^^^

None.

--------------------------
``<solution>``
--------------------------

Optional. Identifies the explanation or solution for the problem, or for one of
the questions in a problem that contains more than one question.

This element contains an HTML division ``<div>``. The division contains one or
more paragraphs ``<p>`` of explanatory text.

--------------------------
``<demandhint>``
--------------------------

Optional. Specifies hints for the learner. For problems that include multiple
questions, the hints apply to the entire problem.

^^^^^^^^^^^^^^^^^^^^
Attributes
^^^^^^^^^^^^^^^^^^^^

None.

^^^^^^^^^^^^^^^^^^^^
Children
^^^^^^^^^^^^^^^^^^^^

``<hint>``

--------------------------
``<hint>``
--------------------------

Required. Specifies additional information that learners can access if needed.

^^^^^^^^^^^^^^^^^^^^
Attributes
^^^^^^^^^^^^^^^^^^^^

None.

^^^^^^^^^^^^^^^^^^^^
Children
^^^^^^^^^^^^^^^^^^^^

None.
