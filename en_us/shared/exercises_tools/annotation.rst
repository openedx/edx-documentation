.. _Annotation:

###################
Annotation Problem
###################

In an annotation problem, you highlight specific text inside a larger text
block and then ask questions about that text. The questions appear when
students move their cursors over the highlighted text. The questions also
appear in a section below the text block, along with space for students'
responses.

.. image:: ../../../shared/building_and_running_chapters/Images/AnnotationExample.png
  :alt: An example annotation problem.

****************************
Create an Annotation Problem
****************************

To create an annotation problem, you add the Annotation advanced component to
your course, add the **Instructions** and **Guided Discussion** segments of the
problem, and then the **Annotation problem** segment of the problem.

=================================
Add the Annotation Component 
=================================

To add the Annotation advanced component, follow these steps.

#. From the **Settings** menu select **Advanced Settings**.

#. In the field for the **Advanced Module List** policy key, place your cursor
   between the brackets.

#. Enter the following value. Make sure to include the quotation marks.

   ``"annotatable"``

4. At the bottom of the page, select **Save Changes**.

   The page refreshes automatically. At the top of the page, you see a
   notification that your changes have been saved.

5. Return to the unit where you want to add the specialized problem. The list
   of possible components now contains an Advanced component.

   .. image:: ../../../shared/building_and_running_chapters/Images/AdvancedComponent.png
      :alt: The Add a New Component panel with the Advanced component option.

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

#. Under the Annotation component, create a new blank Advanced Problem
   component.
       
#. Paste the following code in the Advanced Problem component, replacing
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

3. Select **Save**.
