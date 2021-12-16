.. _course_structure:

####################
Course Content Data
####################

For each course, the database files include a
``{org}-{course}-{date}-course_structure-{site}-analytics.json`` JSON file.
Researchers can use this file to gain an overview of a course's content and
investigate course state at a point in time.

This section describes the contents of the ``course_structure`` file.

.. contents::
  :local:
  :depth: 1

.. _Shared Fields:

******************************
Shared Fields
******************************

The following fields are present for all of the objects in the
``course_structure`` file.

* ``category``
* ``children``
* ``metadata``

Descriptions of these fields follow.

.. _Course Structure Category Field:

====================================
Course Structure ``category`` Field
====================================

In the ``course_structure`` JSON file, the root level ``category`` field
identifies core structural elements of a course. Each ``course_structure``
file contains a single ``"category": "course"`` object, and one or more of the
objects for each of the other categories. For each object in the file, the
``category`` field contains one of the following strings.

.. list-table::
   :widths: 25 60
   :header-rows: 1

   * - Category Value
     - Description
   * - chapter
     - The sections defined in the course outline. For more information, see
       :ref:`Course Building Block Data`.
   * - course
     - The dates, settings, and other metadata defined for the course as a
       whole. For more information, see :ref:`Course Data`.
   * - discussion
     - The content-specific discussion components defined for the course. For
       more information, see :ref:`Course Component Data`.
   * - html
     - The Text components defined for the course. For more information, see
       :ref:`Course Component Data`.
   * - problem
     - The problem components defined for the course. For
       more information, see :ref:`Course Component Data`.
   * - sequential
     - The subsections defined in the course outline. For more information,
       see :ref:`Course Building Block Data`.
   * - vertical
     - The units defined in the course outline. For more information, see
       :ref:`Course Building Block Data`.
   * - video
     - The video components defined for the course. For more information, see
       :ref:`Course Component Data`.

The ``category`` file can also contain additional values. These values, such
as ``poll_question``, identify optional components. These components add
different types of exercises or tools to the course.

====================================
Course Structure ``children`` Field
====================================

The ``children`` field is an array. It identifies the modules that a specific
structural element in the course contains. The ``children`` field for the
``"category": "course"`` object lists all of the sections in the course. For
one of the ``"category": "vertical"`` objects, this field lists all of the
HTML, discussion, problem, and video components in that unit.

====================================
Course Structure ``metadata`` Field
====================================

The ``metadata`` field is an object. This field contains key-value pairs
that describe the settings defined for the course and for each of the modules
that it contains.

.. _Course Data:

***************
Course Data
***************

In the ``"category": "course"`` object, the ``children`` field lists all of
the sections defined for the course. In the sample that follows, the edX
DemoX course has five sections, or chapters, defined.

The ``metadata`` field provides information about parameters set for the
course, including dates, pages, textbooks, and advanced setting values. In the
sample that follows, note that the edX DemoX course includes a course-specific
page, or tab, named "edX Community".

A partial list of the ``metadata`` member fields for a course follows. For
information about the settings that course teams define for a course in
Studio, see :ref:`partnercoursestaff:document index`.

.. list-table::
   :widths: 25 60
   :header-rows: 1

   * - ``metadata`` Member Field
     - Description
   * - ``advanced_modules``
     - This array stores values entered for **Advanced Module List** on the
       Studio **Advanced Settings** page.
   * - ``days_early_for_beta``
     - This field stores the number entered for **Days Early for Beta Users**
       on the Studio **Advanced Settings** page.
   * - ``discussion_topics``
     - This object lists the course-wide discussion topics entered for
       **Discussion Topic Mapping** on the Studio **Advanced Settings** page.
   * - ``showanswer``
     - This field stores the string entered for **Show Answer** on the Studio
       **Advanced Settings** page. Valid values are  'always', 'answered',
       'attempted', 'closed', 'finished', 'past_due', or 'never'.
   * - ``start``
     - This field stores the value entered for **Course Start Date** on the
       Studio **Settings & Details** page.
   * - ``tabs``
     - This array contains member objects that describe the tabs, or pages,
       that appear for the course in the learning management system (LMS).
       Course teams can change the order of the default pages, and add custom
       pages, on the Studio **Pages** page.

       The default **Course** page uses the structure defined by the course
       building blocks to deliver the content defined by the course components
       as well as the updates that are defined on the Studio **Course Updates**
       page.

       For more information, see :ref:`partnercoursestaff:Adding Pages to a
       Course`.

===================
Course Data Sample
===================

.. code-block:: json

   {
       "i4x://edX/DemoX/course/1T2015":{
          "category":"course",
          "children":[
             "i4x://edX/DemoX/chapter/1ff96c6155eb40c39140c656cdc2708b",
             "i4x://edX/DemoX/chapter/00d4374f346b4744aa6f4708cdf46d53",
             "i4x://edX/DemoX/chapter/abc5cf5203ee494faf73fa3f55b4485b",
             "i4x://edX/DemoX/chapter/a783b6e59fe24917985a8aa29eeec150",
             "i4x://edX/DemoX/chapter/0cdd0de7b1f740468381c265796f6f63"
          ],
          "metadata":{
             "advertised_start":"4/15/2015",
             "days_early_for_beta":90.0,
             "discussion_topics":{
                "General":{
                   "id":"i4x-edX-DemoX-course-1T2015"
                }
             },
             "display_name":"edX Demonstration Course",
             "end":null,
             "graceperiod":"18000 seconds",
             "start":"2014-08-10T07:00:00Z",
             "tabs":[
                {
                   "name":"Course",
                   "type":"courseware",
                   "course_staff_only": false
                },

                {
                   "name":"Discussion",
                   "type":"discussion",
                   "course_staff_only": false
                },
                {
                   "name":"edX Community",
                   "type":"static_tab",
                   "url_slug":"67e8a9e44dde4e97b2bd33a928b9099e",
                   "course_staff_only": true
                },
                {
                   "name":"Progress",
                   "is_hidden": false,
                   "type":"progress"
                   "course_staff_only": false
                },
                {
                   "name":"Wiki",
                   "is_hidden": true,
                   "type":"wiki",
                   "course_staff_only": false
                }
             ]
          }
       }
    }


.. _Course Building Block Data:

**************************
Course Building Block Data
**************************

In Studio, a course team organizes course content by defining hierarchical
sections, subsections, and units. Internally, the edX code identifies these
building blocks with a ``category`` value of 'chapter', 'sequential', and
'vertical'.

The sample that follows extracts the objects that represent one of the
sections in a course, a subsection that the section contains, and a unit that
the subsection contains from a JSON ``course_structure`` document.

The ``children`` array for each of these types of objects lists identifiers
for objects that it contains.

* Objects with a category of ``chapter`` list all of the sequentials
  (subsections) that they contain.

* Objects with a category of ``sequential`` list all of the verticals (units)
  that they contain.

* Objects with a category of ``vertical`` list all of the components that they
  contain.

The ``metadata`` field provides information about parameters set for the
section, subsection, or unit. A partial list of the ``metadata`` member fields
for a section, subsection, or unit follows. For information about the structure
that course teams can define for a course, see
:ref:`partnercoursestaff:Developing Your Course Index` in the *Building and
Running an edX Course* guide.


.. list-table::
   :widths: 25 60
   :header-rows: 1

   * - ``metadata`` Member Field
     - Description
   * - ``display_name``
     - This field stores the string in the name field for the section,
       subsection, or unit on the Studio **Course Outline** page. Course teams
       can edit the default name that Studio supplies. This name identifies
       this structural element to learners in the LMS and in edX Insights.
   * - ``start``
     - This field stores the value entered for the section, subsection, or
       unit on the Studio **Course Outline** page. Course teams provide these
       optional start dates so that course content is released incrementally
       after the course start date.
   * - ``visible_to_staff_only``
     - This Boolean indicates the setting selected for the **Hide from
       Students** option for the section, subsection, or unit on the Studio
       **Course Outline** page.


======================================
Course Building Block Data Sample
======================================


.. code-block:: none

  "i4x://edX/DemoX/chapter/00d4374f346b4744aa6f4708cdf46d53": {
    "category": "chapter",
    "children": [
      "i4x://edX/DemoX/sequential/9681154b9c0a4baaafb5f4e26bc71550"
    ],
    "metadata": {
      "display_name": "Introduction to edX Studio",
      "start": "2020-08-09T16:00:00Z",
      "visible_to_staff_only": true
    }
  },
  .
  .
  .
  "i4x://edX/DemoX/sequential/547f430ffd414a5fbb4a080fd5eb7566": {
    "category": "sequential",
    "children": [
      "i4x://edX/DemoX/vertical/2ea89cbec5bd4034981a70abff7a82e1",
      "i4x://edX/DemoX/vertical/7405431e9fe14354a39ac52a2973bc1c"
    ],
    "metadata": {
      "display_name": "What Does an edX Course Look Like?"
    }
  },
  .
  .
  .
   "i4x://edX/DemoX/vertical/7405431e9fe14354a39ac52a2973bc1c": {
    "category": "vertical",
    "children": [
      "i4x://edX/DemoX/html/d3bd5215cf044056beb8e6f7f3e3afc4",
      "i4x://edX/DemoX/video/ddf62dd7bff249efa1add6776f1e2ab8"
    ],
    "metadata": {
      "display_name": "Your Course Info"
    }
  },
  .
  .
  .
  "i4x://edX/DemoX/vertical/778671e308e446409c0c797d9d424eae": {
    "category": "vertical",
    "children": [
      "i4x://edX/DemoX/problem/db71da27320a44bdb45df31d0d801e20",
      "i4x://edX/DemoX/discussion/05d808aad49543de997964be3bfac528"
    ],
    "metadata": {
      "display_name": "Exercise Gallery"
    }


.. _Course Component Data:

*********************
Course Component Data
*********************

In Studio, a course team specifies course content by adding components to
units. The core, or basic, types of components that course teams can add have
a ``category`` value of 'discussion', 'html', 'problem', and 'video'. The
sample that follows extracts objects for each of these component types from a
``course_structure`` file.

The ``children`` array is not used for these types of objects.

The ``metadata`` field provides information about parameters set for a
component.

* The ``metadata.display_name`` member field applies to all of the basic
  component types. This name identifies the component to learners in the LMS
  and in edX Insights. Course teams can edit the default name in the Studio
  **Settings** dialog box.

* The other ``metadata`` member fields reflect settings specific to each
  component type. For information about the settings that course teams can
  define for components, see :ref:`partnercoursestaff:Course Components Index`
  in the *Building and Running an edX Course* guide.

======================================
Course Component Data Sample
======================================

.. code-block:: none

  "i4x://edX/DemoX/html/d3bd5215cf044056beb8e6f7f3e3afc4": {
    "category": "html",
    "children": [],
    "metadata": {
      "display_name": "Intro to Video"
    }
  },
  .
  .
  .
  "i4x://edX/DemoX/video/ddf62dd7bff249efa1add6776f1e2ab8": {
    "category": "video",
    "children": [],
    "metadata": {
      "display_name": "Your Course About Page",
      "download_track": true,
      "download_video": true,
      "end_time": "00:07:24",
      "html5_sources": [
        "https://d2f1egay8yehza.cloudfront.net/BERGG101/BERGG101T314-V001800_100.mp4"
      ],
      "sub": "BERGG101T314-V001800_100",
      "youtube_id_1_0": "uxypPaUu8ng"
    }
  },
  .
  .
  .
    "i4x://edX/DemoX/problem/db71da27320a44bdb45df31d0d801e20": {
    "category": "problem",
    "children": [],
    "metadata": {
      "display_name": "Multiple Choice Questions",
      "markdown": "Many edX courses have homework or exercises you need to complete.  Notice the clock image to the left?  That means this homework or exercise needs to be completed for you to pass the course.\n\nAs you go through the question types, notice how edX gives you immediate feedback on your responses - it really helps in the learning process.\n\nWhat color is the open ocean on a sunny day?\n\n[[yellow, (blue), green]]\n\n\nWhich of the following are musical instruments?\n\n[x] a piano\n[ ] a tree\n[x] a guitar\n[ ] a window\n\n\n ",
      "max_attempts": null,
      "rerandomize": "never",
      "showanswer": "never",
      "weight": null
    }
  },
  .
  .
  .
  "i4x://edX/DemoX/discussion/05d808aad49543de997964be3bfac528": {
    "category": "discussion",
    "children": [],
    "metadata": {
      "discussion_category": "Week 2",
      "discussion_id": "7be676c36bba4486aeeabe3ecb5b06e8",
      "discussion_target": "Improve the Question",
      "display_name": "Discussion Space: Improve the Question"
    }
  },


.. include:: ../../../links/links.rst
