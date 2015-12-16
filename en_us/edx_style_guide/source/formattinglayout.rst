.. _Formatting and Layout:

#############################
Formatting and Content Layout
#############################

For an .rst file that contains examples of the markup used by the
documentation team, see the
edx-documentation/en_us/edx_style_guide/source/Format Cheat
Sheet.rstnouse file.

.. list-table::
  :widths: 15 15 15 25

  * - Item
    - rST Formatting
    - Examples
    - Notes
  * - Book or guide name
    - *Italic*
    - *Building and Running an edX Course*
    - When mentioning the guide in general, link the title to the HTML rather
      than presenting in italics. When providing the title in addition to a
      specific section or topic in the guide, link the section or topic and
      then place the name of the guide in italics.

      Translator guidance is that strings in italic font should be translated.

  * - Code samples
    - ``monospace``
    - The member fields of this dictionary are ``display_name`` and
      ``usage_key``.
    - To make the efforts of translators easier, use ``monospace`` markup only
      for strings that should not be translated: code, commands, SQL table
      columns, and event names.

      For longer examples, such as XML templates, which include text that can
      be translated, use the code block markup and include a comment for
      translators with explicit instructions.

      .. Translators: In the following XML code block, do not translate any
      .. text that is between the < > characters.

      .. code-block:: xml

          <problem display_name="webGLDemo">
          In the image below, click the cone.

  * - Programming elements
    - ``monospace``
    - The ``event_type`` parameter enables downstream processing.

      An XBlock must set ``has_score`` to ``True``.

    - Follow the same rules as for code samples. Programming elements include
      attributes, classes, events, functions, methods, parameters, and
      properties.

      Identify the element type on first mention. Element names only need an
      article when the text also includes the element type.

      * Set the ``has_score`` property to ``True``.

      * Set ``has_score`` to ``True``.

      * Incorrect: Set the has_score to True.

  * - Unnamed icons
    - Enclose a description in quotation marks
    - Select "back 30 seconds" on the playback bar.
    - In most cases, icons have a label or mouseover tip. If the icon has a
      mouseover tip, use the mouseover tip text as the name of the control and
      put it in **bold** like other UI elements.
  * - New term
    - link to glossary definition
    -
    - Add new terms to the glossary. If you want to be sure that people
      understand how you are using the term, provide a link to the glossary
      definition.
  * - UI item
    - **bold**
    - From the **Tools** menu, select **Import**.

      In the left pane, select **Filter messages like this**.

    - A UI item is anything that the user views, clicks, selects, or interacts
      with and that has a name or a tooltip. If it doesn't have a label or
      tooltip, see Unnamed icons above.

      Translator guidance is that strings in boldface font should be
      translated.

  * - User input
    - ``monospace``
    - In the **Show Calculator** field, type ``true``.
    - Follow the same rules as for code samples. The assumption is that values
      presented in monospace font must be entered exactly as documented, and that translated versions of the value are not acceptable.

      If the user input value can be translated, add a "Translator:" comment
      to that effect.

      Inline if the user input is short (one line); indented if more than one
      line.

  * - Variables
    - Surround with braces ({}).
    -
    - Avoid angle brackets (< >) because rST interprets angle brackets as
      setting off XML examples.

