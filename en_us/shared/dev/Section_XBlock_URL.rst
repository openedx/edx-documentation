.. _Section_XBlock_URL:

**************************************
Rendering XBlocks with the XBlock URL
**************************************

The XBlock URL supports HTML rendering of an individual XBlock without the user
interface of the LMS.

To use the XBlock URL and return the HTML rendering of an individual XBlock,
you use the following URL path for an XBlock on an edX site.

``https://{host}/xblock/{usage_id}``

========================
Finding the ``usage_id``
========================

The ``usage_id`` is the unique identifier for the problem, video, text, or
other course content component, or for sequential or vertical course container
component. There are several ways to find the ``usage_id`` for an XBlock in the
LMS, including viewing either the staff debug info or the page source. For more
information, see
:ref:`opencoursestaff:Finding the Usage ID for Course Content`.

In addition, API developers can call the Course Blocks API
``/api/courses/v1/blocks`` to find the ``usage_id`` for a course's XBlocks. For
more information, see :ref:`openplatformapi:Courses API Overview`.

===================
Example XBlock URLs
===================

For example, a video component in the "Creating Video for the edX Platform"
course on the edx.org site has the following URL.

``https://courses.edx.org/courses/course-v1:edX+VideoX+1T2016/courseware/ccc7c32c65d342618ac76409254ac238/1a52e689bcec4a9eb9b7da0bf16f682d/``

This video component appears as follows in the LMS.

.. image:: ../../../shared/images/XBlock_URL_example_before.png
    :alt: A video component presented in the context of the edX LMS, with
        navigational options to reach all other course content.

To construct the XBlock URL for the same video component, you obtain its
``usage_id`` and then use the following URL format.

``https://courses.edx.org/xblock/block-v1:edX+VideoX+1T2016+type@video+block@47faf3a03c4f4023b187528c25932e0a``

When you use this URL, the video component appears in your browser as follows.

.. image:: ../../../shared/images/XBlock_URL_example_after.png
    :alt: A video component presented without any options for accessing other
        course content.

For courses created prior to October 2014, the ``usage_id`` begins with
``i4x://``, as in the following example.

``https://courses.edx.org/xblock/i4x://edX/DemoX.1/problem/47bf6dbce8374b789e3ebdefd74db332``
