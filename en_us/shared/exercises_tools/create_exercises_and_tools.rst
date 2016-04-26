.. _Create Exercises:

############################
Exercises and Tools
############################

You can add a wide variety of different types of exercises and tools to your
course outline. By default, a core set of exercises is available for you to add
to your course. There are also numerous additional exercises and tools that you
can review and add to your course.

.. contents::
  :local:
  :depth: 2

************************************
Levels of Support for Tools
************************************

The level of support that edX provides for each tool varies. The description
of each exercise and tool in the following sections indicates the level of
support designated for each tool: full, provisional, or no support. This table
provides the definition for each level of support.

.. list-table::
   :widths: 25 60
   :header-rows: 1

   * - Level of Support
     - Description
   * - Full support
     - Fully supported tools and features are available on edx.org, are fully
       tested, have user interfaces where applicable, and are documented in the
       official edX guides that are available on docs.edx.org.
   * - Provisional support
     - Provisionally supported tools and features are available on edx.org,
       but might lack the robustness of functionality that your courses
       require. You should test provisionally supported tools thoroughly
       before using them in your course, especially in graded sections.
       Complete documentation might not be available for provisionally
       supported tools, or documentation might be available from sources other
       than the official edX guides.
   * - Not supported
     - Exercises and tools with no support are not maintained by edX, and
       might be deprecated in the future. They are not recommended for use in
       courses due to non-compliance with one or more of the base
       requirements, such as testing, accessibility, internationalization, and
       documentation.

************************************
Introduction to Exercises and Tools
************************************

"Exercises and tools" is a general way to refer to the robust variety of
content that you can integrate into an online course. You create the graded and
ungraded assessments in your course with different exercises or problem types,
while various tools deliver different types of course content. Software
developers use the XBlock component architecture to contribute new exercises
and tools to the Open edX platform and provide new and varied options for
reaching learners.

* You might need to explicitly enable an exercise or tool that you want to use
  in your course. For more information, see :ref:`Enable Additional Exercises
  and Tools`.

* After you enable an exercise or tool for use with your course, when you add a
  component to a unit, that exercise or tool might be listed as one of the
  **Advanced**, **HTML**, or **Problem** options.

The topics in this section describe different exercises and tools. Information
about how to enable specific exercises and tools is provided, followed by
examples and step-by-step instructions for how you use Studio to add components
to your course. For many of the exercises and tools, when you add a component
Studio presents a template for you to use as a starting point for your work.
XML examples and descriptions of the attributes, tags, and elements that you
can use in an XML editor are also provided.

.. _General Exercises and Tools:

****************************
General Exercises and Tools
****************************

Exercises and tools with a wide range of uses are listed alphabetically in this
table.

.. only:: Open_edX

  .. note:: In addition to the following exercises and tools, Open edX offers
   the :ref:`Notes tool<Notes Tool>`. The Notes tool allows learners to
   highlight and make notes about what they read in the course. This tool
   is not available for courses on edx.org.

.. list-table::
   :widths: 25 60 20
   :header-rows: 1

   * - Type
     - Description
     - Support
   * - :ref:`Annotation`
     - Annotation problems ask learners to respond to questions about a
       specific block of text. The question appears above the text when the
       learner moves the cursor to the highlighted text so that learners can
       think about the question as they read.
     - Provisional support
   * - :ref:`Calculator`
     - The calculator tool is available for every course through the course
       advanced settings. When the calculator tool is enabled, it appears on
       every unit page. Learners can enter input that includes Greek
       letters, trigonometric functions, and scientific or ``e`` notation in
       addition to common operators.
     - Provisional support
   * - :ref:`completion`
     - This tool allows learners to mark sections of course content as
       completed. It helps learners to track their progress through sections of
       the course (including for ungraded activities such as reading text,
       watching video, or participating in course discussions), and gives them
       a way to indicate to both themselves and course staff that they
       completed the required activities.
     - Full support
   * - :ref:`Conditional Module`
     - You can create a conditional module to control versions of content that
       groups of learners see. For example, learners who answer "Yes" to a poll
       question then see a different block of text from the learners who answer
       "No" to that question.
     - Provisional support
   * - :ref:`Custom JavaScript`
     - Custom JavaScript display and grading problems (also called custom
       JavaScript problems or JS input problems) allow you to create a
       custom problem or tool that uses JavaScript and then add the problem or
       tool directly into Studio.
     - Full support
   * - :ref:`External Grader`
     - An external grader is a service that receives learner responses to a
       problem, processes those responses, and returns feedback and a problem
       grade to the edX platform. You build and deploy an external grader
       separately from the edX platform. An external grader is particularly
       useful for software programming courses where learners are asked to
       submit complex code.
     - Provisional support
   * - :ref:`Google Calendar Tool`
     - You can embed a Google calendar in your course so that learners see the
       calendar in the course body. You can use a Google calendar to share quiz
       dates, office hours, or other schedules of interest to learners.
     - Full support
   * - :ref:`Google Drive Files Tool`
     - You can embed a Google Drive file, such as a document, spreadsheet, or
       image, in your course so that learners see the file in the course body.
     - Full support
   * - :ref:`Google Instant Hangout`
     - You can add the ability for learners to participate in instant hangouts
       directly from your course. With instant hangouts, learners can interact
       through live video and voice, share screens and watch videos together,
       and collaborate on documents.
     - Provisional support
   * - :ref:`IFrame`
     - With the iframe tool, you can integrate ungraded exercises and tools
       from any Internet site into an HTML component in your course.
     - Provisional support
   * - :ref:`LTI Component`
     - LTI components allow you to add an external learning application or non-
       PDF textbook to Studio.
     - Full support
   * - :ref:`Office Mix Tool`
     - You can embed interactive lessons created from PowerPoint files so that
       learners can experience them directly in the course body.
     - Full support
   * - :ref:`Open Response Assessments 2`
     - In open response assessments, learners receive feedback on written
       responses of varying lengths as well as image files that the learners
       upload. Open response assessments include self assessment and peer
       assessment.
     - Full support
   * - :ref:`Oppia Exploration Tool`
     - You can embed Oppia explorations in your course so that learners can
       interact with them directly in the course body.
     - Full support
   * - :ref:`UBC Peer Instruction`
     - This tool offers the experience of the Peer Instruction learning system
       within your online course.
     - Full support
   * - :ref:`Poll Tool`
     - You can include polls in your course to gather learners' opinions on
       various questions. You can use the Poll Tool in Studio.
     - Full support
   * - :ref:`Poll`
     - You can run polls in your course so that your learners can share
       opinions on different questions. You can only add this type of poll to a
       course by using OLX. Support for this tool in Studio is not available.
       For more information, see the :ref:`olx:edX Open Learning XML Guide`.
     - Provisional support
   * - :ref:`Problem with Adaptive Hint`
     - A problem with an adaptive hint evaluates a learner's response, then
       gives the learner feedback or a hint based on that response so that the
       learner is more likely to answer correctly on the next attempt. These
       problems can be text input or multiple choice problems.
     - Provisional support
   * - :ref:`Problem Written in LaTeX`
     - If you have a problem that is already written in LaTeX, you can use
       this problem type to easily convert your code into XML.
     - No support
   * - :ref:`Qualtrics Survey`
     - You can import surveys that you have created in Qualtrics. The survey
       appears inside an iframe in your course.
     - Full support
   * - :ref:`RecommenderXBlock`
     - RecommenderXBlock can hold a list of resources for misconception
       remediation, additional reading, and so on. This tool allows the
       course team and learners to work together to maintain the list of
       resources. For example, team members and learners can suggest new
       resources, vote for useful ones, or flag abuse and spam.
     - Full support
   * - :ref:`Survey Tool`
     - You can include surveys in your course to collect learner responses to
       multiple questions. You can use the survey tool in Studio.
     - Full support
   * - :ref:`Text Input`
     - In text input problems, learners enter text into a response field. The
       response can include numbers, letters, and special characters such as
       punctuation marks.
     - Full support; mobile-ready
   * - :ref:`Word Cloud`
     - Word clouds arrange text that learners enter - for example, in response
       to a question - into a colorful graphic that learners can see.
     - Provisional support
   * - :ref:`Write Your Own Grader`
     - In custom Python-evaluated input (also called "write-your-own-grader")
       problems, the grader uses a Python script that you create and embed in
       the problem to evaluates a learner's response or provide hints. These
       problems can be any type.
     - Provisional support

********************************
Image-Based Exercises and Tools
********************************

Exercises and tools that involve image files are listed alphabetically in
this table.

.. list-table::
   :widths: 25 60 20
   :header-rows: 1

   * - Type
     - Description
     - Support
   * - :ref:`drag_and_drop_problem`
     - In drag and drop problems, learners respond to a question by dragging
       text or objects to a specific location on an image.
     - Full support; mobile-ready
   * - :ref:`Full Screen Image`
     - The full screen image tool allows a learner to enlarge an image in the
       whole browser window. This is useful when the image contains a large
       amount of detail and text that is easier to view in context when
       enlarged.
     - Full support
   * - :ref:`Image Mapped Input`
     - In an image mapped input problem, learners click inside a defined area
       in an image. You define this area by including coordinates in the body
       of the problem.
     - Provisional support
   * - :ref:`Zooming Image`
     - Zooming images allow you to enlarge sections of an image so that
       learners can see the section in detail.
     - Full support

************************************
Multiple Choice Exercises and Tools
************************************

Exercises and tools that provide ways for learners to select from
several options are listed alphabetically in this table.

.. list-table::
   :widths: 25 60 20
   :header-rows: 1

   * - Type
     - Description
     - Support
   * - :ref:`Checkbox`
     - In checkbox problems, the learner selects one or more options from a
       list of possible answers. The learner must select all the options that
       apply to answer the problem correctly.
     - Full support; mobile-ready
   * - :ref:`Dropdown`
     - Dropdown problems allow the learner to choose from a collection of
       answer options, presented as a dropdown list. Unlike multiple choice
       problems, whose answers are always visible directly below the question,
       dropdown problems don't show answer choices until the learner clicks the
       dropdown arrow.
     - Full support; mobile-ready
   * - :ref:`Multiple Choice`
     - In multiple choice problems, learners select one option from a list of
       answer options. Unlike with dropdown problems, whose answer choices
       don't appear until the learner clicks the drop-down arrow, answer
       choices for multiple choice problems are always visible directly below
       the question.
     - Full support; mobile-ready
   * - :ref:`Multiple Choice and Numerical Input`
     - You can create a problem that combines a multiple choice and numerical
       input problems. Students not only select a response from options that
       you provide, but also provide more specific information, if necessary.
     - Provisional support; mobile-ready


********************************
STEM Exercises and Tools
********************************

Exercises and tools that are most suitable for use in science, technology,
engineering, or math courses are listed alphabetically in this table.

.. list-table::
   :widths: 25 60 20
   :header-rows: 1

   * - Type
     - Description
     - Support
   * - :ref:`Chemical Equation`
     - Chemical equation problems allow the learner to enter text that
       represents a chemical equation into a text box. The grader evaluates the
       learner's response by using a Python script that you create and embed in
       the problem.
     - Full support
   * - :ref:`Circuit Schematic Builder`
     - In circuit schematic builder problems, learners can arrange circuit
       elements such as voltage sources, capacitors, resistors, and MOSFETs on
       an interactive grid. They then submit a DC, AC, or transient analysis of
       their circuit to the system for grading.
     - Provisional support
   * - :ref:`Gene Explorer`
     - The gene explorer (GeneX) simulates the transcription, splicing,
       processing, and translation of a small hypothetical eukaryotic gene.
       GeneX allows learners to make specific mutations in a gene sequence, and
       it then calculates and displays the effects of the mutations on the mRNA
       and protein.
     - Provisional support
   * - :ref:`Math Expression Input`
     - The more complex of Studio's two types of math problems. In math
       expression input problems, learners enter mathematical expressions to
       answer a question. These problems can include unknown variables and more
       complex symbolic expressions. You can specify a correct answer either
       explicitly or by using a Python script.
     - Full support; mobile-ready
   * - :ref:`Molecule Editor`
     - The molecule editor allows learners to draw molecules that follow the
       rules for covalent bond formation and formal charge, even if the
       molecules are chemically impossible, are unstable, or do not exist in
       living systems.
     - No support
   * - :ref:`Molecule Viewer`
     - The molecule viewer allows you to create three-dimensional
       representations of molecules for learners to view.
     - No support
   * - :ref:`Numerical Input`
     - The simpler of Studio's two types of math problems. In numerical input
       problems, learners enter numbers or specific and relatively simple
       mathematical expressions to answer a question. These problems only allow
       integers and a few select constants. You can specify a margin of error,
       and you can specify a correct answer either explicitly or by using a
       Python script.
     - Full support; mobile-ready
   * - :ref:`Periodic Table`
     - An interactive periodic table of the elements shows detailed information
       about each element as the learner moves the mouse over the element.
     - No support
   * - :ref:`Protein Builder`
     - The Protex protein builder asks learners to create specified protein
       shapes by stringing together amino acids.
     - No support


*********************************
Mobile-Ready Problem Types
*********************************

.. include:: ../../../shared/exercises_tools/Section_mobile_problems.rst
