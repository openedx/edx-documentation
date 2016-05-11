.. _Documenting the User Interface:

########################################
Documenting User Interface Interactions
########################################

When you describe interactions with the user interface, refer to the control
labels and do not describe the control types.

* Incorrect: In the **Randomization** drop-down list, click the **Never**
  option.

* Correct: From the **Randomization** list, select **Never**.

This convention reduces word count and makes the documentation less likely to
go out of date after a software change.

Because screen readers organize all link selections together, and all button
selections together, and so on, if you do include the control type, it is
critical that you describe it as it is coded, even if it is styled to look like
a different type of control.

***********************
List of edX UI Elements
***********************

This table lists edX-specific terms and exceptions to Microsoft style.

.. list-table::
   :widths: 20 80

   * - checkbox
     - Use a single word, not "check box". Users can select more than one
       checkbox at a time.

       Users "select" or "clear" a checkbox. They do not "check" or "deselect"
       them.

   * - component editor
     - Present in lower case.
   * - course accordion
     - Do not use. Previously used to describe the navigation frame that shows
       course sections and subsections at the left side of the **Course** page
       in the LMS. Use "left pane."
   * - dialog box
     - Do not use "dialog" alone to refer to the user interface control. Do not
       use "modal" or "modal dialog".
   * - field
     - A control that accepts user input that is typed or pasted in. Use in
       place of "text box".
   * - icon
     - A user interface control that has an image for a label instead of text.
       To identify icons, use the mouseover help text as the icon label. If the
       icon does not have help text, such as an icon in a mobile app, it must
       be described.
   * - learning sequence, the
     - The horizontal navigation frame that appears above course content on
       the **Course** page in the LMS. An icon appears in the learning sequence
       for each unit in the selected subsection. Use learning sequence instead
       of "course ribbon" or "filmstrip".


***********************************
Standards for User Interface Labels
***********************************

When the edX documentation team writes or copy edits labels, we follow these
standards.

Use title capitalization for labels for the following user interface elements.

* Page titles
* Tab titles
* Buttons (these usually have only a few words)

Use sentence capitalization for all other labels.
