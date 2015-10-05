.. _Documentation Translation Guidelines:

###############################################
Guidelines for Translators
###############################################

This section provides basic guidelines for translators of edX documentation.
The complete edX documentation translation process is described in
:ref:`Documentation Translation Process`.

.. important:: Before you begin an edX documentation translation project,
   contact us at docs.edx.org to confirm the language or languages that you
   are translating into, and so that we can make sure the repository is ready
   for you to work with.

   To work on translations of edX documentation, you should have a basic
   understanding of reStructuredText and formatting in .rst files. For more
   information and links to some resources, see :ref:`Work with edX
   Documentation Source Files`.

   In addition, you or another person on the translation team should
   understand Github repositories and the Github pull request process. For
   more information about using Github, see https://help.git.com.

When you translate edX documentation source .rst files, follow these general
guidelines. For examples of each type of element, see :ref:`the Example .rst
file<Anchor For ExampleRSTFile>`.


*************************
What To Translate
*************************

In addition to obvious text, do translate the following items.

* Note and Warning text. Translate text following the tags ``.. note::`` or
  ``.. warning::``. Be careful to wrap and indent lines correctly, as described
  in :ref:`Work with edX Documentation Source Files`.

* Link text in inline links. Distinguish between anchor text and link text.
  Only translate link text; if you translate anchor text, the link will be
  broken.

  For example, in

  ``:ref:`Work with edX Documentation Source Files``` or
  ```Work with edX Documentation Source Files`_``

  the text between the grave accent
  characters (`) is actual anchor text and should not be translated.

  However, in the example

  ``:ref:`this is link text<Work with edX Documentation Source Files>```

  the actual anchor text is between the carets and should not be
  translated. The text string between the first grave accent character and the
  first caret ("this is link text") is link text, and should be translated.

* Alt text in image references. Translate text following the tag ``:alt:`` so
  that a useful description is provided for screen readers.

  For example, ::

   .. image:: ../../../data/source/Images/DataCzar_Initialization.png
      :width: 100
      :alt: Flowchart showing process for initializing a data czar




*****************************
What Not to Translate
*****************************

Do not translate or alter any of the following elements.

* The filenames and locations of any .rst files in the repository.

* The filenames and locations of any image files in the repository. If you
  replace any original source images with localized images, make sure the
  replacement image files have exactly the same filenames, and replace them in
  the same Images folder location, so that image links within the
  documentation are not broken.

* Words in file paths in cross-references or image references.

* Words that are part of .rst directives, including "note" or "warning".
  Examples are listed in :ref:`Work with edX Documentation Source Files` and
  :ref:`ExampleRSTFile<Anchor For ExampleRSTFile>`.

* The text of anchors in .rst files.

* Code examples that are tagged with ``.. code-block::``.

* Variables, database field names, or code examples that are tagged with
  monospace code font (placed between double grave accent characters).

  For example, in the following sentence, do not translate the event names that are between pairs of double grave accent characters.

  The edX mobile app for iOS now emits ````play_video````, ````pause_video````,
  ````stop_video````, ````load_video````, and ````seek_video```` events.


For information about working with edX Documentation source files, see
:ref:`Work with edX Documentation Source Files`.

For information about the documentation translation process, see
:ref:`Documentation Translation Process`.
