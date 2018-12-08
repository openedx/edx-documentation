.. _Formatting and Layout:

####################################
Style Conventions and Content Layout
####################################

The edX documentation is authored using reStructuredText markup syntax. For a
description and complete documentation, see `reStructuredText`_ .

For a sample .rst file that contains examples of the markup used by the edX
documentation team, see the
``edx-documentation/en_us/edx_style_guide/source/ExampleRSTFile.rst`` file.

.. list-table::
  :widths: 15 15 15 25

  * - Item
    - .rst Formatting
    - Examples
    - Notes
  * - Book or guide name
    - ``*italic*``
    - *Building and Running an edX Course*
    - When you provide the title of the guide in addition to a cross-reference
      to a specific section or topic in the guide, link the section or topic
      and then place the name of the guide in italics. Otherwise, make the
      title the cross reference link instead of presenting it in italics.

      Translator guidance is that strings in italic font should be translated.

  * - Code samples
    - ````monospace````
    - The member fields of this dictionary are ``display_name`` and
      ``usage_key``.
    - Use ``monospace`` markup only for strings that should not be translated,
      including code, settings, commands, SQL table columns, and event names.

      For longer examples, such as XML templates that include text that can
      be translated, use the code block markup and include a comment for
      translators with explicit instructions.

      ``.. Translators: In the following XML code block, do not translate any``
      ``.. text that is between the < > characters.``

      .. code-block:: xml

          <problem display_name="webGLDemo">
          In the image below, click the cone.

  * - Programming elements
    - ````monospace````
    - The ``event_type`` parameter enables downstream processing.

      An XBlock must set ``has_score`` to ``True``.

    - Follow the same rules as for code samples. Programming elements include
      attributes, classes, events, functions, methods, parameters, and
      properties.

      Identify the element type on first mention. Element names only need an
      article when the text also includes the element type.

      * Set the ``has_score`` property to ``True``.

      * Set ``has_score`` to ``True``.

      * Incorrect: Set the has_score to true.

  * - Unnamed icons
    - "brief description"
    - Select "back 30 seconds" on the playback bar.
    - In most cases, icons have mouseover help text. If the icon has
      help text, use that text as the name of the control and
      use ``**bold**`` like other UI elements.
  * - New term
    - optional: link to glossary definition
    - This section provides conceptual and procedural information about
      using ``:ref:`teams_g``` in your courses.
    - Add new terms to the glossary. If you want to be sure that people
      understand how you are using the term, provide a link to the glossary
      definition. Do not italicize newly introduced terms.
  * - User interface controls
    - ``**bold**``
    - From the **Tools** menu, select **Import**.

      In the discussion navigation pane, select **Filter messages like this**.

    - For more information about user interface controls in edX products, see
      :ref:`Documenting the User Interface`.

      Translator guidance is that strings in boldface font can be
      translated.

  * - User input
    - ````monospace````
    - In the **Show Calculator** field, type ``true``.
    - Follow the same rules as for code samples. The assumption is that values
      presented in monospace font must be entered exactly as documented, and
      that translated versions of the value are not acceptable.

      If the user input value can be translated, add a "Translator:" comment to
      that effect.

  * - Variables
    - Surround with braces ({}).
    - ...in the format ``{org}-{course}-{run}-{site}.mongo``.
    - Avoid angle brackets (< >) because rST uses angle brackets to identify
      XML examples.

.. _reStructuredText: http://docutils.sourceforge.net/rst.html
