.. _The Visual Editor:

=========================
The Visual Editor
=========================

The visual editor provides a "what you see is what you get" (WYSIWYG) interface
that allows you to format text by selecting options at the top
of the editor.

The following image shows callouts for the editing options and is followed by
descriptions.

.. image:: ../../../shared/images/TextEditorToolbar.png
  :alt: The legend identifying the action of toolbar buttons for the text editor.

#. Arrows that perform undo/redo actions.

#. Select a formatting style for the selected text, such as paragraph,
   ``preformatted`` (monospace), or a heading level.

   .. note::
     The available heading levels in the Text component editor begin with
     heading 2 (``<h2>``). Text components are part of a complete page, and
     elements outside the Text component use heading level 1 by default.
     Because tools such as screen readers use heading levels to navigate
     through pages, using heading level 1 inside a Text component can
     interfere with the functionality of these tools.

#. Format the selected text in bold, or remove this formatting. The editor
   inserts ``<strong>`` tags around the selected text.

#. Format the selected text in italics, or remove this formatting. The editor
   inserts ``<em>`` tags around the selected text.

#. Underline the selected text, or remove this formatting. The editor encloses
   the selected text in the tag ``<span style="text-decoration: underline;">``.

#. Change the color of the selected text. The editor encloses the selected text
   in the tag ``<span style="color: color-hex-code;">``.

#. Change the background color of the selected text. The editor encloses the 
   selected text in the tag ``<span style="background-color: color-hex-code;">``.

#. Align text and images to the left. The editor adds ``style="text-align:
   left;"`` to the ``<p>`` tags that surround the text.

#. Center text and images. The editor adds ``style="text-align: center;"`` to
   the ``<p>`` tags that surround the text.

#. Align text and images to the right. The editor adds ``style="text-align:
   right;"`` to the ``<p>`` tags that surround the text.

#. Justify text and images. The editor adds ``style="text-align: justify;"`` to
   the ``<p>`` tags that surround the text.
   
#. Create a bulleted list, or remove this formatting. The editor inserts
   ``<ul>`` tags around the selected text, and encloses each paragraph in
   ``<li>`` tags.

#. Create a numbered list, or remove this formatting. The editor inserts
   ``<ol>`` tags around the selected text, and encloses each paragraph in
   ``<li>`` tags.

#. Decrease and increase the indentation of the selected paragraph.

#. Insert an image at the cursor. For more information, see :ref:`Add an Image
   to a Text Component`.

#. Create a hypertext link from the selected text. For more information, see
   :ref:`Add a Link in a Text Component`.

#. Remove a hypertext link from the selected text.

#. Format the selected paragraph as a blockquote. The editor inserts
   ``<blockquote>`` tags around the selected text, which is then displayed as a
   separate indented paragraph.

#. Format the selected text as a code block, or remove this formatting. The
   editor inserts ``<code>`` tags around the selected text, which is then
   displayed in a monospace font.
   
#. The table toolbar icon lets you drop in a table component and selecting a 
   given cell lets you create, remove, or adjust rows and columns. 

#. You can easily add emoticons to your text content. This can be a way to break  
   up long stretches of content. 

#. We have introduced a way to to include special characters into your text  
   content, including mathematical and symbolic elements.

#. Inject a horizontal line in the highlighted content.

#. Clear formatting button which removes all font formatting from the selected 
   text.  This does not remove paragraph formatting (e.g. blockquote).

#. Review the HTML markup.

#. Accessibility Checker, which allows you to check HTML in the editor for various accessibility problems. For more information, see :ref:`Accessibility Checker`.

.. note::
  The visual editor is not available for :ref:`course handouts <Adding Course
  Updates and Handouts>`.


