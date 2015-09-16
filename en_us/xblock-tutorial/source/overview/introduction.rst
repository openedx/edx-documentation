.. _Introduction to XBlocks:

#############################
Introduction to XBlocks
#############################

This section introduces XBlocks.

.. contents::
 :local:
 :depth: 1

***************
Overview
***************

As a developer, you build XBlocks that course teams use to create independent
course components that work seamlessly with other components in an online
course.

For example, you can build XBlocks to represent individual problems or pieces
of text or HTML content. Furthermore, like Legos, XBlocks are composable; you
can build XBlocks to represent larger structures such as lessons, sections, and
entire courses.

A primary advantage to XBlocks is that they are deployable. The code you write
can be deployed in any instance of the edX Platform or other XBlock runtime
application, then used by any course team using that system.

By combining XBlocks from a wide variety of sources, from text and video, to
multiple choice and numerical questions, to sophisticated collaborative and
interactive learning laboratories, course teams can create rich and engaging
courseware.

*****************************
XBlock API and Runtimes
*****************************

XBlock is an API than can be used by different applications, referred to as
XBlock :ref:`runtimes<XBlock Runtimes>`.

As described below, the edX Platform uses the XBlock API, and is the most
common XBlock runtime.

If you are planning to use your XBlock in a different rutime, check the
documentation to understand the runtime's requirements.

*****************************
XBlocks and the edX Platform
*****************************

The edX Platform uses many built-in XBlocks that are available to course
developers. For example, HTML content, videos, and interactive problems are all
XBlocks. The edX Platform also includes many specialized XBlocks such as
:ref:`opencoursestaff:Google Drive Files Tool` and :ref:`opencoursestaff:Open
Response Assessments 2`. For more information, see :ref:`XBlocks and the
edX Platform`.

EdX recognizes the ever expanding need to provide new and innovative types
of content. The XBlock API and XBlock SDK are available for developers to
create new types of XBlocks for course teams to use.

***********************
XBlocks for Developers
***********************

Developers can extend the types of content available in the edX Platform by
creating and deploying XBlocks. EdX provides the `XBlock SDK`_ to support the
creation of new XBlocks.

===================
Prerequisites
===================

This tutorial is for developers who are new to XBlock. To use this tutorial,
you should have basic knowledge of the following technologies.

* Python
* JavaScript
* HTML and CSS
* Python virtualenv
* Git

===================
XBlock Resources
===================

This tutorial is meant to guide developers through the process of creating an
XBlock, and to explain the :ref:`concepts<XBlock Concepts>` and
:ref:`anatomy<Anatomy of an XBlock>` of XBlocks.

Developers should also see the :ref:`xblockapi:EdX XBlock API Guide`.

=========================================
XBlock Independence and Interoperability
=========================================

You must design your XBlock to meet two goals.

* The XBlock must be independent of other XBlocks. Course teams must be able to
  use the XBlock without using other XBlocks.

* The XBlock must work together with other XBlocks. Course teams must be
  able to combine different XBlocks in flexible ways.

=========================================
XBlocks Compared to Web Applications
=========================================

XBlocks are like miniature web applications: they maintain state in a storage
layer, render themselves through views, and process user actions through
handlers.

XBlocks differ from web applications in that they render only a small piece of
a complete web page.
	
Like HTML ``<div>`` tags, XBlocks can represent components as small as a
paragraph of text, a video, or a multiple choice input field, or as large as a
section, a chapter, or an entire course.

.. include:: ../../../links/links.rst
