.. _Create Exercises:

###############################
Problems, Exercises, and Tools
###############################

You can add a wide variety of different types of problems, exercises, and
tools to your course outline. By default, a core set of :ref:`problem
types<Working with Problem Components>` is available in Studio for you to
include in your course. You have the option to expand the initial set of core
problem types by enabling additional exercises and tools.

.. contents::
  :local:
  :depth: 2

.. _Levels of Support:

******************
Levels of Support
******************

.. only:: Open_edX

 .. note:: The support level definitions described in this section and the
    level of support designated for each exercise, problem type, or tool are
    applicable only to edx.org.

The level of support that edX provides for each problem, exercise, or tool
varies. The levels of support are categorized as full, provisional, or no
support. This table provides the definition for each level of support.

In Studio, the support level for each exercise, problem type, or tool is
represented with an icon when you select **Advanced**, **Text**, or
**Problem** to add a new component to your course. By default, only fully
supported or provisionally supported exercises, problem types, or tools are
available for adding to your course. To add unsupported problem types and
tools, see :ref:`Add_Unsupported_Exercises_Problems`.

.. Internal note: For the OLX Guide there is a separate levels_of_support.rst file under olx/source/problem-xml that contains the levels of support info


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
       require. Third party tools are classified as provisionally supported
       because edX does not have control over the quality of the software, or
       of the content that can be provided using such tools.

       You should test provisionally supported tools thoroughly
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


**************************************************************
Enhancing Your Course with Additional Exercises and Tools
**************************************************************

"Exercises and tools" is a general way to refer to the robust variety of
content that you can integrate into an online course. Software developers use
the XBlock component architecture to contribute new exercises and tools to the
Open edX platform and provide new and varied options for reaching learners.
Exercises enhance the core set of problem types by challenging learners to
complete graded and ungraded assessments. Tools deliver a variety of other
types of course content.

* To use an exercise or tool in your course beyond the core set of problem
  types, you must explicitly enable that exercise or tool. For more
  information, see :ref:`Enable Additional Exercises and Tools`.

* After you enable an exercise or tool for use in your course, you might need
  to select **Advanced**, **Text**, or **Problem** on the unit page to
  add content of that type to your course.

The topics in this section introduce the core set of problem types and a
selection of other exercises and tools that you can add to your course.

*******************
Core Problem Types
*******************

The problem types that you can include in any course, without taking any
other steps to identify or enable additional exercises or tools, are the core
problem types. When you add a problem component in Studio, the core problem
types are classified as either **Common Problem Types** or **Advanced**.

.. contents::
  :local:
  :depth: 1

=====================
Common Problem Types
=====================

When you select any of the common problem types in Studio the :ref:`simple
editor<Simple Editor>` opens.

* If you choose the **Blank Common Problem** option, the editor opens without
  providing a template or example for you to follow You can begin to add text
  and markdown for required and optional problem elements immediately.

* If you choose one of the following problem types, a template appears in the
  editor with guidance for adding all of that problem type's required
  elements, as well as several optional elements.

.. list-table::
   :widths: 25 60 20
   :header-rows: 1

   * - Problem Type
     - Description
     - Support
   * - :ref:`Checkbox`
     - In checkbox problems, learners select one or more options from a list of
       possible answers. To answer the problem correctly, a learner must select
       all of the options that are correct answers, and none of the options
       that are incorrect.
     - Full support; mobile-ready
   * - :ref:`Dropdown`
     - In dropdown problems, learners choose one answer from a set of possible
       answers, which are presented in a dropdown list after the learner
       selects the dropdown arrow.
     - Full support; mobile-ready
   * - :ref:`Multiple Choice`
     - In multiple choice problems, learners select one answer from a set of
       possible answers, which are visible directly below the question.
     - Full support; mobile-ready
   * - :ref:`Numerical Input`
     - In numerical input problems, learners enter numbers or specific and
       relatively simple mathematical expressions to answer a question. These
       problems allow only integers and a few select constants. You can specify
       a margin of error, and you can specify a correct answer either
       explicitly or by using a Python script.
     - Full support; mobile-ready
   * - :ref:`Text Input`
     - In text input problems, learners enter text into a response field. The
       response can include numbers, letters, and special characters such as
       punctuation marks.
     - Full support; mobile-ready

By adding hints, feedback, or both, you can give learners guidance and help
when they work on a problem. When you choose one of the following common
problem types, a template provides additional guidance for these options. All
of these problem types also have full support and are mobile-ready.

* :ref:`Checkboxes with Hints and Feedback <Use Feedback in a Checkbox
  Problem>`

* :ref:`Dropdown with Hints and Feedback <Use Feedback in a Dropdown Problem>`

* :ref:`Multiple Choice with Hints and Feedback <Use Feedback in a Multiple
  Choice Problem>`

* :ref:`Numerical Input with Hints and Feedback <Use Feedback in a Numerical
  Input Problems>`

* :ref:`Text Input with Hints and Feedback <Use Feedback in a Text Input
  Problem>`

=========
Advanced
=========

When you select any of the advanced problem types in Studio the :ref:`advanced
editor<Advanced Editor>` opens.

* If you choose the **Blank Advanced Problem** option, the editor opens without
  providing a template or example for you to follow. You can begin to add OLX
  markup and the text for required and optional problem elements immediately.

* If you choose one of the following problem types, a template appears in the
  editor with guidance for adding all of that problem type's required elements,
  as well as several optional elements.

.. note:: Some advanced problem types are :ref:`unsupported<Levels of
   Support>` and are not available in the list of problem types unless you
   enable a setting in Studio. For more information, see :ref:`Unsupported
   Advanced Problem Types` and :ref:`Add_Unsupported_Exercises_Problems`.


.. list-table::
   :widths: 25 60 20
   :header-rows: 1

   * - Type
     - Description
     - Support

   * - :ref:`Custom JavaScript Display and Grading<Custom JavaScript>`
     - Custom JavaScript display and grading problems (also called custom
       JavaScript problems or JS input problems) allow you to create a custom
       problem or tool that uses JavaScript and then add the problem or tool
       directly into Studio.
     - Full support
   * - :ref:`Write Your Own Grader`
     - In custom Python-evaluated input (also called "write-your-own-grader")
       problems, the grader uses a Python script that you create and embed in
       the problem to evaluate a learner's response or provide hints. These
       problems can be any type.
     - Provisional support
   * - :ref:`Math Expression Input`
     - Learners enter mathematical expressions to answer a question. These
       problems can include unknown variables and more complex symbolic
       expressions. You can specify a correct answer either explicitly or by
       using a Python script.
     - Full support; mobile-ready
   * - :ref:`Open Response Assessment<Open Response Assessments Two>`
     - Learners receive feedback on responses that they submit and give
       feedback to other course participants. Open response assessments include
       self assessment, peer assessment, and optionally, staff assessment.
     - Full support

.. when new Drag and Drop is enabled and included in the dropdown, add an entry to this table (above) for it.

.. _Unsupported Advanced Problem Types:

++++++++++++++++++++++++++++++++++
Unsupported Advanced Problem Types
++++++++++++++++++++++++++++++++++

The following advanced problem types are :ref:`not supported<Levels of
Support>` by edX. You can enable an option to make unsupported problem types
available in Studio. For more information, see
:ref:`Add_Unsupported_Exercises_Problems`.

.. list-table::
   :widths: 25 60 20
   :header-rows: 1

   * - Type
     - Description
     - Support
   * - :ref:`Circuit Schematic Builder`
     - Learners arrange circuit elements such as voltage sources, capacitors,
       resistors, and MOSFETs on an interactive grid. They then submit a DC,
       AC, or transient analysis of their circuits to the system for grading.
     - Not supported
   * - :ref:`Drag and Drop`
     - Learners respond to a question by dragging text or objects to a specific
       location on an image. This version of the drag and drop problem type is
       deprecated and should not be added to a course. For more information
       about the fully supported drag and drop problem type, see
       :ref:`drag_and_drop_problem`.
     - Not supported
   * - :ref:`Image Mapped Input`
     - Learners answer prompts by selecting a defined area in an image. You
       define the area by including coordinates in the body of the problem.
     - Not supported
   * - :ref:`Molecular Structure<Molecule Editor>`
     - Learners draw molecules that follow the rules for covalent bond
       formation and formal charge, even if the molecules are chemically
       impossible, are unstable, or do not exist in living systems.
     - Not supported
   * - :ref:`Problem with Adaptive Hint`
     - A problem with an adaptive hint evaluates a learner's response, then
       gives the learner feedback or a hint based on that response so that the
       learner is more likely to answer correctly on the next attempt. These
       problems can be text input or multiple choice problems.
     - Not supported


******************************
Additional Exercises and Tools
******************************

This table lists the fully or provisionally supported additional exercises and
tools that you can add to your course.

.. note:: Some additional exercises and tools are :ref:`not supported<Levels
   of Support>` by edX. You can enable an option to make unsupported exercises
   and tools available in Studio. For more information, see :ref:`Unsupported
   Additional Exercises and Tools` and
   :ref:`Add_Unsupported_Exercises_Problems`.

.. to come: revise to eliminate entries with no support. Add pointer (at least for Open edX) to all of the XBlocks that are available.

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

   * - :ref:`Calculator`
     - Learners can enter input that includes Greek letters, trigonometric
       functions, and scientific or ``e`` notation in addition to common
       operators. The calculator tool is available for every course through the
       course advanced settings. When the calculator tool is enabled, it
       appears on every unit page.
     - Provisional support
   * - :ref:`Conditional Module`
     - You can create a conditional module to control versions of content that
       groups of learners see. For example, learners who answer "Yes" to a poll
       question then see a different block of text from the learners who answer
       "No" to that question.
     - Provisional support
   * - :ref:`drag_and_drop_problem`
     - Learners respond to a question by dragging text or objects to a specific
       location on an image.
     - Full support; mobile-ready
   * - :ref:`External Grader`
     - An external grader is a service that receives learner responses to a
       problem, processes those responses, and returns feedback and a problem
       grade to the edX platform. You build and deploy an external grader
       separately from the edX platform. An external grader is particularly
       useful for software programming courses where learners are asked to
       submit complex code.
     - Provisional support
   * - :ref:`Google Calendar Tool`
     - Learners see a Google calendar embedded in your course. You can use a
       Google calendar to share quiz dates, office hours, or other schedules of
       interest to learners.
     - Provisional support
   * - :ref:`Google Drive Files Tool`
     - Learners see a Google Drive file, such as a document, spreadsheet, or
       image, embedded in your course.
     - Provisional support
   * - :ref:`IFrame`
     - With the iframe tool, you can integrate ungraded exercises and tools
       from any Internet site into a Text component in your course.
     - Provisional support
   * - :ref:`LTI Component`
     - LTI components allow you to add an external learning application or non-
       PDF textbook to Studio.
     - Full support
   * - :ref:`Oppia Exploration Tool`
     - You can embed Oppia explorations in your course so that learners can
       interact with them directly in the course body.
     - Provisional support
   * - :ref:`UBC Peer Instruction`
     - This type of exercise offers the experience of the Peer Instruction
       learning system within your online course.
     - Full support
   * - :ref:`Poll Tool`
     - You can include polls in your course to gather learners' opinions on
       various questions. You can use the Poll Tool in Studio.
     - Full support
   * - :ref:`Qualtrics Survey`
     - You can import surveys that you have created in Qualtrics. The survey
       appears inside an iframe in your course.
     - Provisional support
   * - :ref:`Survey Tool`
     - You can include surveys in your course to collect learner responses to
       multiple questions.
     - Full support
   * - :ref:`Word Cloud`
     - Word clouds arrange text that learners enter in response to a question
       into a colorful graphic.
     - Provisional support



.. _Unsupported Additional Exercises and Tools:

===========================================
Unsupported Additional Exercises and Tools
===========================================

The following additional exercises and tools are :ref:`not supported<Levels of
Support>` by edX. You can enable an option to make unsupported exercises and
tools available in Studio. For more information, see
:ref:`Add_Unsupported_Exercises_Problems`.


.. list-table::
   :widths: 25 60 20
   :header-rows: 1

   * - Type
     - Description
     - Support
   * - :ref:`Annotation`
     - Learners respond to questions about a specific block of text. The
       question appears above the text so that learners can think about the
       question as they read.
     - Not supported
   * - :ref:`Chemical Equation`
     - Learners enter a value that represents a chemical equation into a text
       box. The grader uses Python script that you create and embed in the
       problem to evaluate learner responses.
     - Not supported
   * - :ref:`completion`
     - Learners mark sections of course content as completed. This tool helps
       learners track their progress through sections of the course (including
       ungraded activities such as reading text, watching videos, or
       participating in course discussions), and gives them a way to indicate
       to both themselves and course staff that they completed an activity.
     - Not supported
   * - :ref:`Full Screen Image`
     - Learners can enlarge an image in the entire browser window. This tool is
       useful for detailed images that are easier to view when enlarged.
     - Not supported
   * - :ref:`Gene Explorer`
     - The gene explorer (GeneX) simulates the transcription, splicing,
       processing, and translation of a small hypothetical eukaryotic gene.
       Learners make specific mutations in a gene sequence, and this tool
       calculates and displays the effects of the mutations on the mRNA and
       protein.
     - Not supported
   * - :ref:`Multiple Choice and Numerical Input`
     - Learners not only choose one answer from a set of possible options, they
       are also prompted to provide more specific information, if necessary.
     - Not supported
   * - :ref:`Molecule Viewer`
     - Learners view three-dimensional representations of molecules that you
       create.
     - Not supported
   * - :ref:`Periodic Table`
     - An interactive periodic table of the elements that shows detailed
       information about each element when learners move the pointer over each
       element.
     - Not supported
   * - :ref:`Poll`
     - You can run polls in your course so that your learners can share
       opinions on different questions. You can only add this type of poll to a
       course by using OLX (open learning XML). Support for this tool in Studio
       is not available. For more information, see the :ref:`olx:edX Open
       Learning XML Guide`.
     - Not supported
   * - :ref:`Problem Written in LaTeX`
     - If you have a problem that is already written in LaTeX, you can use this
       problem type to convert your code into XML.
     - Not supported
   * - :ref:`Protein Builder`
     - Learners create specified protein shapes by stringing together amino
       acids.
     - Not supported
   * - :ref:`RecommenderXBlock`
     - RecommenderXBlock can hold a list of resources for misconception
       remediation, additional reading, and so on. This tool allows the course
       team and learners to work together to maintain the list of resources.
       For example, team members and learners can suggest new resources, vote
       for useful ones, or flag abuse and spam.
     - Not supported
   * - :ref:`Zooming Image`
     - Learners can view sections of an image in detail. You specify the
       sections in an image that can be enlarged.
     - Not supported


*********************************
Mobile-Ready Problem Types
*********************************

.. include:: ../../../shared/exercises_tools/Section_mobile_problems.rst


.. _Add_Unsupported_Exercises_Problems:

***********************************************
Adding Unsupported Problem Types and Exercises
***********************************************

.. only:: Open_edX

 .. note:: These instructions are applicable only to edx.org.

.. When DOC-3163 is complete, update this Open edX only note to say "These instructions are applicable only to edx.org or if your Open edX site has configured {the name of the config setting}"

In general, you should use only problem types and exercises that are either
fully or provisionally supported by edX. By default, only supported problem
types and exercises are available in Studio for adding to courses.

However, in some situations, you might choose to use exercises and problem types
that edX does not support.

To add unsupported problem types, exercises, and tools to your course, follow
these steps.

#. In Studio, select **Settings**, then **Advanced Settings**.

#. Locate the **Add Unsupported Problems and Tools** field, and enter a value
   of ``true``.

#. Select **Save Changes**.

After you enable this setting, unsupported problem types, exercises, and tools
are available in the lists of new components that you can add to your course
in Studio.

