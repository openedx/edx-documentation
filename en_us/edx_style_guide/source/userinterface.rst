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

The edX documentation team makes an effort to use the aria-label values that
identify elements of the user interface in the document object model (DOM).
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
     - Do not use. Previously used to describe the course navigation pane.
   * - course navigation pane
     - On the **Courses** page, the navigation frame for selecting sections and
       subsections.
   * - course ribbon
     - Do not use. Previously used to describe the unit navigation bar.
   * - dialog box
     - Do not use "dialog" alone to refer to the user interface control. Do not
       use "modal" or "modal dialog".
   * - discussion navigation pane
     - On the **Discussion** page, the navigation frame for selecting and
       filtering discussion categories, subcategories, and posts.
   * - field
     - A control that accepts user input that is typed or pasted in. Use in
       place of "text box".
   * - filmstrip
     - Do not use.
   * - handout navigation sidebar
     - On the **Home** page, the navigation frame for selecting course
       materials added as handouts.
   * - icon
     - A user interface control that has an image for a label instead of text.
       To identify icons, use the mouseover help text as the icon label. If the
       icon does not have help text, such as an icon in a mobile app, it must
       be described.
   * - learning sequence
     - Do not use. Previously used to describe the unit navigation bar.
   * - left pane
     - Do not use. On the **Courses** page, the navigation frame for selecting
       sections and subsections is called the course navigation pane. On the
       **Discussion** page, the navigation frame for selecting categories and
       subcategories is called the discussion navigation pane.
   * - unit navigation bar
     - The navigation frame on the **Course** page with icons for each unit in
       the selected subsection, and with **Previous** and **Next** options on
       either end.


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
