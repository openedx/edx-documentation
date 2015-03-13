.. _Formatting and Layout:

#############################
Formatting and Content Layout
#############################


.. list-table::
  :widths: 15 15 15 25

  * - Item
    - rST Formatting
    - Examples
    - Notes
  * - Book or guide name
    - *Italic*
    - *Building and Running an edX Course*
    - Include links wherever possible
  * - Code samples
    - ``monospace``
    - In the **Discussion Topic Mapping** field, place your cursor on the line
      between the opening brace ({) and the closing brace (}), and then paste
      the following code. Make sure to include both braces.

      .. code-block:: xml

        "General": {
        "id": "i4x-Hx-101-course-2014_T4"
        }``

    - 
  * - Programming elements
    - TBD: **bold** or ``monospace`` (see MSTP)
    - Attributes, classes, events, functions, methods, parameters, properties

      The event_type parameter enables downstream processing.

      An XBlock must set has_score to True.

    - Identify the element type on first mention. (SP: May not be necessary
      for our technical audience, but this will help with localization -
      thoughts?)

      Element names only need an article when the text also includes the element type:

      * Set the has_score class property to True.

      * Set has_score to True.

      * NOT: Set the has_score to True.

  * - Heading 1
    - 

      .. code-block:: xml

       *********
       Heading 1
       *********

    - 
    - 
  * - Heading 2
    - 

       .. code-block:: xml

        =========
        Heading 2
        =========

    - 
    - 
  * - Heading 3
    - 

       .. code-block:: xml

        Heading 3
        *********

    - 
    - 
  * - Heading 4
    - 

       .. code-block:: xml

         Heading 4
         =========
    - 
    - 
  * - Heading 5
    - 

       .. code-block:: xml

        Heading 5
        ^^^^^^^^^

    - 
    - 
  * - Unnamed icons
    - TBD: Normal text, description in quotation marks
    - When a user uses the playback bar or the "back 30 seconds" button...
    - Icons are visual elements that do not have a label or mouseover
      tip/name. If the icon has a mouseover tip, use the mouseover tip text as
      the name of the control.

      (screen shot of un-named icons vs. icon with a mouseover tip)

  * - New term
    - *Italic*
    - Rubrics contain *criteria* and *options*.
    - Add new terms to the glossary.
  * - Title
    - 

      .. code-block:: xml

       #####
       Title
       #####

    - 
    - 
  * - UI item
    - **bold**
    - In the **Advanced Module List** field, type...

      On the **Tools** menu, click **Checklists**.

      Under **Add New Component**, click **HTML**, and then click **Text**.

      In the left pane, select the **Filter messages like this** check box.

    - A UI item is anything that the user views, clicks, selects, or interacts
      with and that has a name or a tooltip.
  * - User input
    - ``monospace``
    - In the **Show Calculator** field, type ``true``.
    - Inline if the user input is short (one line); indented if more than one line.
  * - Variables
    - Surround with braces ({}). 
    - 
    - Avoid angle brackets (< >) because rST interprets
      angle brackets as setting off XML examples.

