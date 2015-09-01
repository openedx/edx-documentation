.. _Preparing Content:

#####################################
Preparing Course Content for Reuse
#####################################

.. The following paragraph describes LTI setup for edx.org 
.. Alison, August 2015

.. .. only:: Partners

  .. Direction about using Edge (?)

.. only:: Open_edX

  Before you begin work to reuse the content in an edX course, check with your
  development operations (DevOps) team for information about the edX website to
  use. At some sites, a completely separate open edX instance, with a different
  Studio website, is set up to be the LTI tool provider.

.. contents:: 
   :local:
   :depth: 1

.. _Planning for Content Reuse:

***********************************
Planning for Content Reuse
***********************************

Much of the content that an edX course contains, including all of its HTML and
video components, and many of the exercises and tools that you add as problem
components, can be included in an external LMS without any preparation. The
start and end dates and enrollment dates set for the course are ignored, so the
edX content will remain available without interruption.

However, some edX content can be confusing to learners when it appears in the
context of an external LMS. For example, edX course discussions can identify
learners by their internally assigned edX IDs instead of their usernames. In
addition, optional course features that create groups of learners based on
their IDs, such as content experiments and cohorts, should be disabled.

When you create links from an external LMS to the content of an edX course, you
can select individual components. You can also select units, subsections, or
sections. When you select a unit, subsection, or section, all of its published
content is included in the external LMS. Therefore, edX recommends that you
prepare a course for reuse by removing components and disabling features that
might detract from the learning experience in your external LMS.

.. note:: As a best practice, you should only link to content in edX courses
 that are not running, and that do not have enrolled learners, from an external
 LMS.

This section assumes use of the Studio user interface to complete the
preparation and verification steps for an imported course. However, you can
also complete the necessary changes to the course by editing the XML of the
exported course before you import.

***********************************
Step 1: Create a Duplicate Course
***********************************

To create the duplicate course, follow these steps.

#. Export the course. For more information, see :ref:`Export a Course`. 
   
#. Import the course with a new name. For more information, see :ref:`Import a
   Course`.
   
   .. note:: You might need to import the course into a different Studio 
     website. Be sure to check with your DevOps team. 

*************************************
Step 2: Prepare the Duplicate Course
*************************************

To prepare an edX course for LTI use, you disable features and remove content
that do not provide value in an external LMS. For more information, see
:ref:`Planning for Content Reuse`.

To ensure the best experience for your learners, complete this step before you
create any links to course sections, subsections, or units from an external
learning management system.

.. list-table::
   :widths: 45 45
   :header-rows: 1

   * - EdX Content or Feature
     - Disable or Remove for LTI?
   * - Cohorts
     - Yes
   * - Content Experiment Components
     - Yes
   * - Course-wide Discussions
     - Yes
   * - Discussion Components
     - Yes
   * - HTML Components
     - No
   * - Problem Components
     - No
   * - Randomized Content Block Components
     - Yes
   * - Video Components
     - No

.. check on randomized content blocks, that's an assumption - Alison 22 Aug 15

For information about removing components, see :ref:`Delete a Component`. For
information about disabling cohorts, see :ref:`Disabling the Cohort Feature`.
To remove course-wide discussions, you select **Settings**, and then **Advanced
Settings**, and then delete the contents of the **Discussion Topic Mapping**
policy key. For more information, see :ref:`Create CourseWide Discussion
Topics`.

*******************************
Step 3: Verify Content Status
*******************************

Only edX course content that is published appears in an external LMS.

.. note:: The **Hide from students** setting for sections, subsections, 
 and units does not affect the visibility of content in an external LMS. Only
 the publication status of a unit can prevent content from being included..

To verify that all of the content in your edX course is published, follow these
steps.

#. In Studio, from the **Content** menu select **Outline**. The **Course
   Outline** page opens.

#. Expand each section and subsection.

#. Locate units with "Unpublished units will not be released" or "Unpublished
   changes to live content" below the unit name.

#. For each unpublished unit, make any changes that are necessary to prepare
   the content for publication. Alternatively, delete the unit.

#. Publish the unit. For more information , see :ref:`Publish a Unit`_.
