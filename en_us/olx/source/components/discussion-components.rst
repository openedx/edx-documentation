.. _Discussion Components:

#################################
Discussion Components
#################################

You can add inline discussion components to any container in your
course.

.. contents::
  :local:
  :depth: 1

**********************************************
Create the XML File for a Discussion Component
**********************************************

There are two ways to create an inline discussion component in your course.
The preferred way is to include a discussion tag inside a vertical, as
demonstrated in the following example.

.. code-block:: xml

  <vertical display_name="Lesson_1_Unit_1">
    ...
    <discussion
      display_name="Peer Grading"
      discussion_category="Essays"
      discussion_target="Peer Grading"
      discussion_id="unique_id_here"
    />
  </vertical>

The second way, which is deprecated, is to create an XML file in the
``discussion`` directory for each inline discussion component in your course,
and to then reference XML file in a discussion tag inside a vertical, as shown
in the following example.

The following is inside a vertical:

.. code-block:: xml

  <vertical display_name="Lesson_1_Unit_1">
    <discussion
      url_name="Peer_Grading"
    />
  </vertical>

Create the file ``discussion/Peer_Grading.xml`` to define the inline discussion
component, containing the following code.

.. code-block:: xml

  <discussion
    display_name="Peer Grading"
    discussion_category="Essays"
    discussion_target="Peer Grading"
    discussion_id="unique_id_here"
  />

Note that the name of the XML file must match the value of the @url_name
attribute of the ``discussion`` element in the vertical XML file.

***************************************
Discussion Component XML File Elements
***************************************

The root element of the XML file for the discussion component file is
``discussion``.

The ``discussion`` element contains no children.

*************************************
``discussion`` Element Attributes
*************************************

.. list-table::
   :widths: 10 70
   :header-rows: 1

   * - Attribute
     - Meaning
   * - Required. ``discussion_category``
     - The name of the category for the inline discussion as shown in the main
       **Discussion** tab of the course. For example: ``Problem Set 1``
   * - Required. ``discussion_target``
     - The name of the subcategory for the inline discussion as shown in the
       **Discussion** tab of the course. For example: ``Problem 2``
   * - ``display_name``
     - Optional. The value that is displayed to students as the name of the
       discussion component. If you do not supply a ``display_name`` value,
       "Discussion" is supplied for you.
   * - Optional. ``discussion_id``
     - The unique identifier that the discussion forum service uses to refer to
       this inline discussion component. This value must be unique across all
       courses in the edX deployment. We recommend that you leave this value
       blank so that a unique identifier is automatically generated.
   * - Obsolete. ``id``
     - Use ``discussion_id`` instead.
   * - Obsolete. ``for``
     - Use ``discussion_target`` instead.

*************************************
Example Discussion Component XML File
*************************************

The following example shows an XML file for a discussion component.

.. code-block:: xml

  <discussion
      discussion_category="Essays"
      discussion_target="Peer Grading"
      display_name="Peer Grading"
   />
