.. _Determining Content Addresses:

#####################################
Determining Content Addresses
#####################################

To include the content of an existing course in another system, you use the edX
LMS to find the location identifiers for the content you want to include. You
then format the identifiers into an LTI URL.

.. contents:: 
   :local:
   :depth: 1

Using an organizational tool, such as a spreadsheet or document, can be
helpful. For example, in one spreadsheet column you can list the names of the
specific components, units, and subsections in your course that you want to use
in an external LMS. Additional columns can contain the course ID and the usage
IDs that correspond to each piece of course content.

********************
Find the Course ID
********************

The identifier for your course can be in one of these formats.

* ``{key type}:{org}+{course}+{run}``, for example, 
  ``course-v1:edX+DemoX+2014``

* ``{org}/{course}/{run}``, for example, ``edX/DemoX/2014``
 
To find the course ID for your course, follow these steps.

#. In the edX LMS, open your course.

#. In the URL, find the course ID.

For example, you open the edX DemoX course to the course info page. The URL is
``https://edx.org/courses/edX/DemoX/2014/info``. From the URL, you determine
that the course ID is ``edX/DemoX/2014``.

The course ID is the same for every piece of course content.

****************************************
Find the Usage ID for Course Content
****************************************

The identifier for a specific component, unit, or subsection in your course can
be in one of these formats.

* ``{key type}:{org}+{course}+{run}+type@{type}@{display name}``, for example, 
  ``block-v1:edX+DemoX+2014+type@sequential+block@basic_questions``

* ``i4x:;_;_{org};_{course};_{type};_{display name}``, for example, 
  ``i4x:;_;_edX;_DemoX;_sequential;_basic_questions``

Internally, different terms are used to indicate components, units, and
subsections, as follows.

.. list-table::
   :widths: 45 45
   :header-rows: 1

   * - EdX Studio
     - Page Source
   * - component
     - {problem, html, video}+block
   * - unit
     - vertical
   * - subsection
     - sequential

To find the usage ID for a component, unit, or subsection, follow these steps.

#. In the edX LMS, open your course.

#. Go to the page that you want to include in an external LMS.

#. Open the HTML source for the page. For example, in a Chrome browser you
   right click on the page, and then select **View Page Source**.

#. Use your browser's Find feature to locate the term ``data-usage-id``. This
   attribute contains the usage ID.

   .. important:: You might need to search beyond the first match to retrieve 
     the usage ID for the content you want to identify. Be sure to check the
     ``data-usage-id`` for sequential, vertical, or problem, html, or video to
     be sure that you specify the content that you want.

For example, you want the usage ID for the Drag and Drop problem in the edX
DemoX course. The Drag and Drop problem is the second problem in the first
homework assignment in Week 1 of the course. You open the course, go to the
problem, and then view the page source. When you search for ``data-usage-id``,
the first match is
``block-v1:edX+DemoX+Demo_Course+type@sequential+block@basic_questions``. This
usage ID value is for the subsection (sequential). You search again, and see a
usage ID for the unit (vertical). The third time you search, you get the usage
ID for the first of the problems (problem+block) in the assignment. You search 
again, and find the usage ID for the second problem in the assignment,
``block-v1:edX+DemoX+Demo_Course+type@problem+block@d2e35c1d294b4ba0b3b1048615605d2a``.

If you are using a spreadsheet or document to organize your location
identifiers, you can select the usage ID value within the quotation marks or
``&#34;`` ISO codes, and then use copy and paste to add it.

************************
Construct the LTI URL
************************

To identify the edX content that you want to include in an external LMS, you
provide its URL. This URL has the following format.

  ``https://edx-lti.org/lti_provider/courses/{course_id}/{usage_id}``

To construct the LTI URL, you add your course ID and the specific content ID. 

Examples of the possible formats for an LTI URL follow.

  ``https://edx-lti.org/lti_provider/courses/course-v1:edX+DemoX+2014/block-v1:edX+DemoX+2014+type@sequential+block@basic_questions``

  ``https://edx-lti.org/lti_provider/courses/edX/DemoX/2014/i4x:;_;_edX;_DemoX;_sequential;_basic_questions``

