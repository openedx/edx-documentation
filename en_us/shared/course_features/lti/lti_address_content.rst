.. _Determining Content Addresses:

#####################################
Determining Content Addresses
#####################################

.. only:: Partners

.. note:: This feature was a closed pilot experiment. This feature is not
 supported for new users.

To include the content of an existing course in another system, you use the edX
LMS to find the location identifiers for the content you want to include. You
then format the identifiers into an LTI URL.

.. contents::
   :local:
   :depth: 2

You might find using a tool like a spreadsheet helpful as a way to organize the
course ID and each of the usage IDs that correspond to the course content you
want to include in an external LMS.

.. _Find the Course ID:

********************
Find the Course ID
********************

The identifier for your course can be in one of these formats.

* ``{key type}:{org}+{course}+{run}``, for example,
  ``course-v1:edX+DemoX+2014``

* ``{org}/{course}/{run}``, for example, ``edX/DemoX/2014``

Courses created since Fall 2014 typically have an ID that uses the first
format, while older courses have IDs that use the second format.

To find the course ID for your course, follow these steps.

#. In the edX LMS, open your course.

#. In the URL shown by your browser, find the course ID.

For example, you open the "Blended Learning with edX" course to the **Course**
page for the course. The URL for the **Course** page is
``https://courses.edx.org/courses/course-v1:edX+BlendedX+1T2015/course``. From
the URL, you determine that the course ID is ``course-v1:edX+BlendedX+1T2015``.

Another example is the edX DemoX course. The URL is
``https://courses.edx.org/courses/course-v1:edX+DemoX.1+2T2017/course``, and
its course ID is ``course-v1:edX+DemoX.1+2T2017``.

The same course ID applies to every item of content in the course.

.. _Finding the Usage ID for Course Content:

****************************************
Finding the Usage ID for Course Content
****************************************

The identifier for a specific component, unit, or subsection in your course can
be in one of these formats.

* ``{key type}:{org}+{course}+{run}+type@{type}+block@{display name}``, for
  example, ``block-v1:edX+DemoX+2014+type@sequential+block@basic_questions``

* ``i4x:;_;_{org};_{course};_{type};_{display name}``, for example,
  ``i4x:;_;_edX;_DemoX;_sequential;_basic_questions``

Courses created since Fall 2014 typically have usage IDs in the first format,
while older courses have usage IDs in the second format.

The following terms are used in the usage identifiers to indicate subsections,
units, and components.

.. list-table::
   :widths: 45 45
   :header-rows: 1

   * - EdX Studio
     - Page Source
   * - subsection
     - sequential
   * - unit
     - vertical
   * - component
     - problem, html, or video

The example usage IDs shown above include the word "sequential", so they
indicate subsections in a course.

Several methods are available to help you find the usage IDs for items in your
course.

To find the usage ID for a unit or a component in the LMS, you can use
either of these methods.

* :ref:`View staff debug info<View Staff Debug Info for the Usage ID>` for the
  unit or component.

* :ref:`View the page source<View the Page Source for the Usage ID>` for the
  unit or component.

To find the usage ID for a subsection, you
:ref:`view the page source<View the Page Source for the Usage ID>`.

.. note:: You must have the Staff or Admin role in a course to follow these
  procedures for finding usage IDs.

.. _View Staff Debug Info for the Usage ID:

==========================================
View Staff Debug Info for the Usage ID
==========================================

To find the usage ID for a unit or component in the LMS, follow these steps.

#. In the edX LMS, open your course.

#. Select **Course**, and then go to the page that contains the unit or
   component.

#. Select **Staff Debug Info**.

#. To find the usage ID for a component, find the **location**.

   For example, ``location = block-v1:edX+BlendedX+1T2015+type@html+block@2114b1b8fd7947d28fba53414459ff01``

#. To find the usage ID for a unit, scroll down to find the **parent**.

   For example, ``parent  block-v1:edX+BlendedX+1T2015+type@vertical+block@ae7d9c34c2f34f7aa793ed7b55543ae5``

The usage ID value begins with ``block-v1`` for newer courses or ``i4x://`` for
older courses. If you are using a spreadsheet to organize your location
identifiers, you can select the usage ID value, and then copy and paste it into
the spreadsheet.

To close the Staff Debug viewer, click on the browser page outside of the
viewer.

For more information, see :ref:`Staff Debug Info`.

.. _View the Page Source for the Usage ID:

==========================================
View the Page Source for the Usage ID
==========================================

To find the usage ID for a subsection, unit, or component, you view the
HTML page source for that page of the edX course.

To find the usage ID for a subsection, unit, or component, follow these steps.

#. In the edX LMS, open your course.

#. Select **Course**, and then go to the page with the content that you
   want to include in an external LMS.

#. Open the HTML source for the page. For example, in a Chrome browser you
   right click on the page, and then select **View Page Source**.

#. Use your browser's Find feature to locate the term ``data-usage-id``. This
   attribute contains the usage ID.

#. Review the value for the usage id to determine the part of the course it
   identifies: the sequential (subsection), a unit (vertical) or a specific
   component (problem, html, or video).

   .. important:: You might need to search beyond the first match to retrieve
     the usage ID for the content you want to identify. Be sure to check the
     ``data-usage-id`` for sequential, vertical, or problem, html, or video to
     be sure that you specify the content that you want.


For example, you want to link to a subsection in the edX Demo course. You open
the course, go to the problem, and then right click to view the page source.
When you search for ``data-usage-id``, the first match is
``block-v1:edX+DemoX+Demo_Course+type@sequential+block@basic_questions``. You
verify that this usage ID value is for the subsection by checking for the
presence of ``sequential``.

A more complex example gets the usage ID for the Drag and Drop problem in the
edX DemoX course. The Drag and Drop problem is the second problem in the first
homework assignment in Week 1 of the course. After you view the page source and
search for ``data-usage-id``, the first match is for the subsection
(sequential). You search again, and see a usage ID that uses a slightly
different format than the first usage ID, but contains the word "vertical", so
you know that it is for the unit. The third time that you search, you get the
usage ID for the first of the problems (problem) in the assignment. You
search again, and find the usage ID for the second problem in the assignment,
``block-v1:edX+DemoX+Demo_Course+type@problem+block@d2e35c1d294b4ba0b3b1048615605d2a``.

If you are using a spreadsheet to organize your location identifiers, you can
select the usage ID value within the quotation marks or ``&#34;`` ISO codes,
and then copy and paste it into the spreadsheet.

************************
Constructing the LTI URL
************************

To identify the edX content that you want to include in an external LMS, you
provide its URL. This URL has the following format.

  ``https://{host}/lti_provider/courses/{course_id}/{usage_id}``

To construct the LTI URL, you add your course ID and the specific content ID.

Examples of the possible formats for an LTI URL follow.

LTI URLs for a subsection include "sequential", as follows.

  ``https://edx-lti.org/lti_provider/courses/course-v1:edX+DemoX+2014/block-v1:edX+DemoX+2014+type@sequential+block@basic_questions``

  ``https://edx-lti.org/lti_provider/courses/edX/DemoX/2014/i4x:;_;_edX;_DemoX;_sequential;_graded_simulations``

LTI URLs for a unit include "vertical", as follows.

  ``https://edx-lti.org/lti_provider/courses/course-v1:edX+DemoX+Demo_Course/block-v1:edX+DemoX+Demo_Course+type@vertical+block@vertical_3888db0bc286``

  ``https://edx-lti.org/lti_provider/courses/edX/DemoX/2014/i4x:;_;_edX;_DemoX;_vertical;_d6cee45205a449369d7ef8f159b22bdf``

LTI URLs for Text components include "html+block" or "html", as follows.

  ``https://edx-lti.org/lti_provider/courses/course-v1:edX+DemoX+Demo_Course/block-v1:edX+DemoX+Demo_Course+type@html+block@f9f3a25e7bab46e583fd1fbbd7a2f6a0``

  ``https://edx-lti.org/lti_provider/courses/edX/DemoX/2014/i4x:;_;_edX;_DemoX;_html;_2b94658d2eee4d85ae13f83bc24cfca9``

