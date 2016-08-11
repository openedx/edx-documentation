.. _Annotation:

###################
Annotation Problem
###################

.. note:: EdX does not support this problem type.

In an annotation problem, you highlight specific text inside a larger text
block and then ask questions about that text. The questions appear when
learners move their cursors over the highlighted text. The questions also
appear in a section below the text block, along with space for learners'
responses.

.. image:: ../../../shared/images/AnnotationExample.png
  :alt: An example annotation problem.

.. contents::
  :local:
  :depth: 1

*****************************
Enable Annotation Problems
*****************************

Before you can add annotation problems to your course, you must enable
annotation problems in Studio.

To enable annotation problems in Studio, you add the ``"annotatable"`` key to
the **Advanced Module List** on the **Advanced Settings** page. (Be sure to
include the quotation marks around the key value.) For more information, see
:ref:`Enable Additional Exercises and Tools`.

****************************
Create an Annotation Problem
****************************

To create an annotation problem, you add the **Instructions** and **Guided
Discussion** segments of the problem, and then the **Annotation problem**
segment of the problem.

============================================
Add Instructions and Guided Discussion
============================================

To add the **Instructions** and **Guided Discussion** segments of the problem,
follow these steps.

#. In the unit where you want to create the problem, under **Add New
   Component** select **Advanced**.

#. In the list of problem types, select **Annotation**.

#. In the component that appears, select **Edit**.

#. In the component editor, replace the example code with your own code.

#. Select **Save**.

=================================
Add Annotation Problem
=================================

To add the **Annotation problem** segment of the problem, follow these steps.

#. Under the annotation component, create a new blank advanced problem
   component.

#. Paste the following code in the advanced problem component, replacing
   placeholders with your own information.

   .. code-block:: xml

       <problem>
           <annotationresponse>
               <annotationinput>
                 <text>PLACEHOLDER: Text of annotation</text>
                   <comment>PLACEHOLDER: Text of question</comment>
                   <comment_prompt>PLACEHOLDER: Type your response below:</comment_prompt>
                   <tag_prompt>PLACEHOLDER: In your response to this question, which tag below do you choose?</tag_prompt>
                 <options>
                   <option choice="incorrect">PLACEHOLDER: Incorrect answer (to make this option a correct or partially correct answer, change choice="incorrect" to choice="correct" or choice="partially-correct")</option>
                   <option choice="correct">PLACEHOLDER: Correct answer (to make this option an incorrect or partially correct answer, change choice="correct" to choice="incorrect" or choice="partially-correct")</option>
                   <option choice="partially-correct">PLACEHOLDER: Partially correct answer (to make this option a correct or partially correct answer, change choice="partially-correct" to choice="correct" or choice="incorrect")
                   </option>
                 </options>
               </annotationinput>
           </annotationresponse>
           <solution>
             <p>PLACEHOLDER: Detailed explanation of solution</p>
           </solution>
         </problem>

#. Select **Save**.
