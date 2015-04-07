.. _Documenting the User Interface:

###############################
Documenting the User Interface
###############################

In describing UI interactions, we refer to labels alone, rather than include
specific descriptions of the UI controls. 

* Incorrect: In the **Randomization** drop-down list, click the **Never** option.

* Correct: From the **Randomization** list, select **Never**.

This is primarily to reduce word count, and also because the UI can change
without notice. Another reason is related to the use of screen readers:
controls can be styled to appear as other controls, such as a link that is
styled to look like a button. The screen reader organizes all link selections
together, and all button selections together, so if the documentation refers
to a link as a button, we can actually make it harder for people to find the
choice that they want.

*******************
List of UI Elements
*******************

To do: Add images to table

.. list-table::
   :widths: 20 80

   * - box
     - 
   * - button
     - 
   * - checkbox
     - One word. Users can select more than one checkbox at a time. See also
       "radio button". 

       Users "select" or "clear"  a checkbox. They do not "check" or
       "deselect" them.

   * - component editor
     - 
   * - control
     - 
   * - course accordion
     - Do not use. Use "left pane." Formerly the list of sections and
       subsections in the left pane of the **Courseware** page in the LMS.
   * - course pages
     - 
   * - course tabs
     - 
   * - dialog box
     - A small box that opens temporarily when a user performs an action. The
       user interacts with elements in the dialog box, which then disappears.
       A dialog box might just have cancel/OK buttons, or it may ask a user to
       specify a file.
   * - dropdown menu or list
     - 
   * - field
     - A box that a user types or pastes text into. Preferred over "text box".
   * - heading
     - 
   * - icon
     - A UI control that has an image for a label instead of words. Named
       icons have a mouseover tip that is used for identification. Unnamed
       icons, such as icons in a smartphone app, must be described.
   * - learning sequence, the
     - The strip at the top of the **Courseware** page in the LMS that lists
       the units in a subsection. Learning sequence is preferred over the
       previous term, "course ribbon".
   * - left pane
     - For an unnamed panel on the left side of the screen.
   * - page
     - 
   * - pane
     - 
   * - panel
     - A field on the right or left that doesn't extend for the entire length
       of the page.
   * - pop-up menu
     - A list of related options that opens when a user performs an action.
       The menu disappears after the user selects an option.
   * - publishing status panel
     - 
   * - radio button
     - A circular control that allows users to select only one of a list of
       options. See also "checkbox".
   * - right pane
     - For an unnamed panel on the right side of the screen.
   * - screen
     - Larger than a dialog box, with more options.
   * - window
     - 


****************************
Standards for UI Labels
****************************

When the doc team contributes to the wording and formatting of UI labels, we
follow these standards.

All UI elements should use sentence capitalization except the following items,
which use title capitalization.

* Page titles
* Tab titles
* Buttons (these usually have only a few words)

