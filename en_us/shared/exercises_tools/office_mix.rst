.. include:: ../../../links/links.rst

.. _Office Mix Tool:

##########################
Office Mix Tool
##########################

.. note:: EdX offers provisional support for this tool.

`Office Mix`_ is a third-party tool that you can use to turn Microsoft®
PowerPoint® presentations into interactive online lessons that are called
mixes.

This topic describes how to embed PowerPoint (.ppt) format mixes in your
course.

.. contents::
  :local:
  :depth: 2

Before you make content from an external site available through your course, be
sure to review the content to ensure that it is accessible to people with
disabilities. For more information, see :ref:`Accessibility Best Practices for
Course Content Development`.

*********
Overview
*********

Office Mix is an extension to PowerPoint. With Office Mix, you can create
lessons by integrating quizzes, polls, website links, narration, screen
recordings, and more into your PowerPoint presentations. The `Office Mix
gallery`_ provides examples and links to more information.

When you design a lesson that uses PowerPoint with Office Mix, consider that
you can save the result in either PowerPoint (.ppt) format or export the file
to video (.mp4 format).

* Lessons that include interactive elements should be saved in PowerPoint
  format as mixes.

* Lessons that do not include interactive elements, but that do include audio
  narration or video tablet capture, can be exported as videos in .mp4 format.

.. note:: Because Office Mix is a third-party tool, its features are subject
 to change without notice. Be sure to consult the `Office Mix Knowledge Base`_
 for up to date information about this tool's features.

=============================================
Creating Interactive Mixes with Office Mix
=============================================

To embed mixes that have interactive elements, including quizzes, web pages,
and apps, in a course, you save the file in .ppt format. These files can
include any of the other Office Mix features as well, including audio and
video.

.. note:: While you can include questions in your mixes, these questions cannot
  be graded. EdX recommends that you add Office Mix components only to ungraded
  subsections in a course.

This topic describes how to embed PowerPoint (.ppt) format mixes in your
course. The following example shows a mix as learners see it in the edX LMS.

.. image:: ../../../shared/images/office_mix.png
  :alt: An Office mix in the course.
  :width: 800

For information about how to create mixes, see the `Office Mix Knowledge
Base`_.

======================================
Creating Video Files with Office Mix
======================================

You can use Office Mix to add audio, video, or both to a PowerPoint
presentation. These annotations can be recorded (or rerecorded) for the entire
presentation or for individual slides within the presentation. To embed mixes
that include audio and video only, you have the option to export the
presentation to a video file in .mp4 format.

You then use a video component to add the resulting .mp4 file to your course,
instead of the .ppt file. For more information about including .mp4 format
video files in your course, see :ref:`Working with Video Components`.

.. note:: Interactive features, such as hyperlinks, do not function in an .mp4
  video file. The quality of the output that is rendered by the Microsoft
  PowerPoint web client for mixes in .ppt format can be higher than the quality
  of a video file exported for the same presentation.

.. only:: Partners

  The video files that you create with Office Mix go through the same media
  encoding and hosting process that applies to any other video in your course.
  This process helps assure that high quality video experiences are delivered
  to as many learners as possible.

  For more information about video processing for courses that run on the
  edx.org site, see :ref:`partnercoursestaff:Video Processing Overview`.

=============================================
Adding Captions to Office Mix Presentations
=============================================

Typically, mixes include audio, video, or both. Mixes that include audio or
video are likely to qualify as time-based media, and as a result, they require
captions or a transcript to make all content accessible to all learners.

For more information about how to add captions to a mix, see the Microsoft
documentation for Office Mix, including the `How to add Closed Captions to an
Office Mix`_ knowledge base article.

For more information about making time-based media accessible, see
:ref:`Accessibility Best Practices for Course Content Development`.

******************************
Add an Office Mix to a Course
******************************

To add .ppt format mixes to your course, you create a mix, host it at an
external site, and then enable and use the Office Mix tool in Studio to add the
mix into a component in your course.

For information about how to create mixes, see the `Office Mix Knowledge
Base`_.

=================================
Create or Identify an Office Mix
=================================

#. On an external website, create or identify the mix that you want to add to
   your course. For examples of mixes, see the `Office Mix gallery`_.

#. Save the mix in .ppt format.

#. Make a note of the URL for the mix.

.. _Enable the Office Mix Tool:

==============================
Enable the Office Mix Tool
==============================

Before you can add a mix to your course, you must enable this tool in Studio.

To enable the Office Mix tool in Studio, you add the ``"officemix"`` key to the
**Advanced Module List** on the **Advanced Settings** page. (Be sure to
include the quotation marks around the key value.) For more information, see
:ref:`Enable Additional Exercises and Tools`.

==============================
Add a Mix in Studio
==============================

You must :ref:`enable the Office Mix tool <Enable the Office Mix Tool>` before
you add a component with a mix to your course. You must also create or identify
the mix that you want to add and obtain its URL.

#. On the **Course Outline** page, locate the ungraded subsection where you
   want to add the mix and add or open a unit.

#. Under **Add New Component**, select **Advanced**, and then select **Office
   Mix**. Studio adds the new component, which includes a sample mix, to the
   unit.

#. In the new component, select **Edit**.

   .. image:: ../../../shared/images/office_mix_studio.png
     :alt: The component editor for a Mix in Studio.
     :width: 600

#. In the **Component Display Name** field, enter an identifying name for the
   component. In the LMS, this name appears as a heading above the mix.

#. In the **Office Mix URL** field, enter the complete URL for the mix that you
   want to add. For example, ``https://mix.office.com/watch/1otxpj7hz6kbx``.

#. Select **Save**.

   To verify your work, select **play**.
