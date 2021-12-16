.. _Preparing Content:

#####################################
Preparing to Reuse Course Content
#####################################

.. only:: Partners

.. note:: This feature was a closed pilot experiment. This feature is not
 supported for new users.

  To make the content of an existing edX course reusable in an external LMS,
  you create a duplicate version of the course. You use the duplicate course
  specifically as a source of content for your external LMS. Based on
  configuration choices your organization makes for using edX as an LTI tool
  provider, you might be asked to create the duplicate course on edX Edge or on
  another host site.

.. only:: Open_edX

  Before you begin work to reuse the content in an Open edX course, check with
  your development operations (DevOps) team for information about the
  website to use. At some sites, a completely separate Open edX instance, with
  a different Studio website, is set up to be the LTI tool provider.

.. contents::
   :local:
   :depth: 1

.. _Planning for Content Reuse:

***********************************
Planning for Content Reuse
***********************************

When you create links to edX course content in your external LMS, you can link
to components individually, to all of the content in a unit, or to all of the
content in a subsection.

As you plan which parts of the course you want to reuse, note the following
considerations.

* Some edX content can be confusing to learners when it appears in the context
  of an external LMS. For example, in some configurations, edX course
  discussions identify learners by their internally assigned edX IDs instead of
  by their usernames. Rather than linking to a subsection or unit that contains
  discussion components, you could plan to either link only to specific
  components or remove the discussion components from the unit or subsection,
  and then use the features available in your external LMS to add discussion
  forums to the course.

* Optional edX course features that create groups of learners based on their
  IDs, such as content experiments and cohorts, are not designed to provide
  results for external use. To use features like these for your course, you
  should plan to set them up in the external LMS.

* To ensure that edX content remains available without interruption, edX course
  content appears in the external LMS regardless of the start, end, or
  enrollment dates that are defined for the edX course.

* To ensure that learners see only edX content that is ready for use, only
  course content that is published appears in an external LMS.

For more information about edX features that might not be suitable for use with
LTI, see :ref:`Select Content in the Duplicate Course`.

The topics that follow assume use of the edX Studio user interface. However,
you can also complete these tasks by exporting the course and then reviewing or
editing its XML before you import.

***********************************
Create the Duplicate Course
***********************************

.. only:: Partners

  Before you create a duplicate course, be sure to check with your DevOps team
  or your edX partner manager to determine the website that hosts your
  organization's courses for LTI use.

.. only:: Open_edX

  Before you create a duplicate course, be sure to check with your DevOps team
  to determine the website that hosts your organization's courses for LTI use.

To create the duplicate course, follow these steps.

#. In Studio, export the original course. For more information, see
   :ref:`Export a Course`.

#. In Studio on your organization's host site for LTI courses, create a course.
   This is the duplicate course.

   .. note:: If your organization uses the same site as the host for both the
    original course and for LTI courses, be sure to give the duplicate course a
    different name or run.

#. In the duplicate course, import the tar.gz file that you exported in step 1.
   For more information, see :ref:`Import a Course`.

.. future: add re-run as an option for sites that host courses for LTI on the same instance (edit from Mark, Phil says re-run should work). - Alison 1 Sep 2015

.. _Select Content in the Duplicate Course:

***************************************
Select Content in the Duplicate Course
***************************************

To select content in your duplicate edX course for reuse in an external LMS,
you use Studio to review the course outline and make note of the components,
units, and subsections you want to include.

Using an organizational tool, such as a spreadsheet, can be helpful. For
example, you can use a spreadsheet column to identify the type of content (for
example, component, unit, subsection), and add their display names to the next
column. Additional columns can contain the values that you use to construct the
addresses for your LTI links. For more information about addressing content,
see :ref:`Determining Content Addresses`.

Optionally, you can streamline the contents of units and subsections by
removing components, or disable course features that you do not plan to use.

.. list-table::
   :widths: 45 45
   :header-rows: 1

   * - EdX Content or Feature
     - Works Well with LTI?
   * - Annotation Problem Components
     - No
   * - Cohorts
     - No
   * - Content Experiment Components
     - No
   * - Course-wide Discussions
     - No
   * - Discussion Components
     - No
   * - Text Components
     - Yes
   * - Internal Links
     - No
   * - Problem Components
     - Yes
   * - Randomized Content Block Problem Components
     - No
   * - Video Components
     - Yes

.. check on randomized content blocks, that's an assumption - Alison 22 Aug 15

For information about removing components, see :ref:`Delete a Component`. For
information about disabling cohorts, see :ref:`Disabling the Cohort Feature`.
To remove course-wide discussions, you select **Settings**, and then **Advanced
Settings**, and then delete the contents of the **Discussion Topic Mapping**
policy key. For more information, see :ref:`Create CourseWide Discussion
Topics`.

*******************************
Verify Content Status
*******************************

Only edX course content that is published appears in an external LMS.

.. note:: The **Hide from students** setting for sections, subsections,
 and units does not affect the visibility of content in an external LMS. Only
 the publication status of a unit can prevent content from being included.

To verify that all of the content in your edX course is published, follow these
steps.

#. In Studio, from the **Content** menu select **Outline**. The **Course
   Outline** page opens.

#. Expand each section and subsection.

#. Locate units with "Unpublished units will not be released" or "Unpublished
   changes to live content" below the unit name.

#. For each unpublished unit, make any changes that are necessary to prepare
   the content for publication. Alternatively, delete the unit.

#. Publish the unit. For more information, see :ref:`Publish a Unit`.
