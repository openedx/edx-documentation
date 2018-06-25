.. _Rerun a Course:

###################
Re-running a Course
###################

Another way to create a course in Studio is to re-run an existing course. When
you re-run a course, most, but not all, of the original course content is
duplicated to the new course. The original course is not changed in any way.

.. contents::
  :local:
  :depth: 1

.. _Data Duplicated When You Re-Run a Course:

********************************************
Data Duplicated When You Re-Run a Course
********************************************

.. list-table::
   :widths: 45 45
   :header-rows: 1

   * - Type of Content
     - Duplicated to New Course?
   * - Course start date
     - No. Set to midnight on January 1, 2030 (UTC).
   * - All other course dates
     - Yes. You must update all release dates and due dates.
   * - Course structure (sections, subsections, units) and state (published,
       hidden)
     - Yes.
   * - Individual problems and other components
     - Yes.
   * - Files uploaded to the course, including videos and textbooks
     - Yes.
   * - Pages added to the course
     - Yes, including all page content and the defined page order.
   * - Course updates
     - Yes.
   * - Prerequisite course subsection settings
     - No.
   * - Advanced settings
     - Yes.
   * - Grading policy
     - Yes.
   * - Student enrollment data
     - No.
   * - Course team privileges, including admins, discussion moderators, beta
       testers
     - No. Only the user who created the new course has access to it.
   * - Manually created cohorts
     - No.
   * - Student answers, progress, and grading data
     - No.
   * - Certificates
     - Yes.
   * - Discussion posts, responses, comments, and other data
     - No.
   * - Wiki contributions
     - No.

After you create a re-run course, modifications to the original course and the
re-run course are independent. Changes to either course have no effect on the
other course. Therefore, you should ensure that the original course content is
as complete as possible before you re-run the course.

For more information, see :ref:`Re-Run Course` and :ref:`Update the New
Course`.

.. _Re-Run Course:

***************
Re-Run a Course
***************

.. note::
  After the end date for a course has passed, the course moves to the
  **Archived Courses** tab on the Studio dashboard. If the course that you want
  to re-run is not visible on the **Courses** tab, look for the course on the
  **Archived Courses** tab.

.. only:: Partners

 Options for creating a course re-run differ for courses on edx.org and Edge.

 * For courses on edx.org, the course team uses :ref:`Publisher <Pub Creating
   and Announcing a Course>` to re-run courses. For more information about
   how to create a course run, see :ref:`Pub Creating a Course Run`.

 * For courses on Edge, the course team can :ref:`use the course Import and
   Export options <Export and Import the Previous Course>` to re-run a course,
   or your edX project coordinator can :ref:`use the Re-Run Course option <Use
   Re-Run to Create a Course>`.

   .. note::
     A course team member who has course creation privileges must create a new course when you use the **Import** and **Export** options.

     We strongly encourage course teams to use the **Import** and **Export**
     options to create a course re-run. This method takes less time than the
     **Course Re-Run** option because this method does not require action from
     edX.

.. only:: Open_edX

 To re-run a course, the course team can :ref:`use the course Import and Export
 options <Export and Import the Previous Course>`, or a system administrator
 can :ref:`use the Re-Run Course option <Use Re-Run to Create a Course>`. Note
 that the **Import** and **Export** method takes less time than the **Course
 Re-Run** option because this method does not require action from a system
 administrator.

.. _Export and Import the Previous Course:

=====================================
Export and Import the Previous Course
=====================================

.. only:: Partners

 .. note::
   Courses on edx.org must :ref:`use Publisher to re-run courses <Pub Creating
   a Course Run>`.

To use the import and export options to re-run a course, follow these steps.

#. In Studio, open the course that you want to re-run.

#. :ref:`Export your course <Export a Course>`.

#. In Studio, :ref:`create a new course <Creating a New Course>`.

   .. note::
     You must have course creation privileges to create a new course. If you do
     not have course creation privileges, contact a member of the course team
     who has these privileges, or your organization's administrator.

#. In the new course, :ref:`import the content from the previous course <Import
   a Course>`.

#. After the import operation is complete, :ref:`review and update the settings
   and content <Update the New Course>` for the new course.

.. _Use Re-Run to Create a Course:

==============================
Use the Course Re-Run Option
==============================

.. note:: Before you re-run a course, make sure that its settings and content
  are complete. Additions and changes that you make to the original course
  after you create the new course have no effect on the new course.

.. only:: Partners

 .. note::
   Courses on edx.org must :ref:`use Publisher to re-run courses <Pub Creating
   a Course Run>`.

   For courses on Edge, we strongly recommend that you use the **Import** and
   **Export** options.

   To use the **Re-Run Course** option, you must contact your project
   coordinator.


.. only:: Open_edX

  Only global or system administrators have the permissions needed to re-run
  a course. To re-run a course, contact your system administrator. After your
  system administrator creates a new course using the re-run feature, you can
  complete the steps to :ref:`update the new course<Update the New Course>`.

  To re-run a course, users who have the required permissions follow these
  steps.

  #. Sign in to Studio. Your dashboard lists the courses that you have access
     to as a course team member.

  #. Move your cursor over each row in the list of courses. The **Re-Run
     Course** and **View Live** options appear for each course.

  #. Locate the course you want to re-run and select **Re-Run Course**. The
     **Create a re-run of a course** page opens with values already supplied in
     the **Course Name**, **Organization**, and **Course Number** fields.

  #. In the **Course Run** field, indicate when the new course will be offered.

     Together, the course number, the organization, and the course run are used
     to create the URL for the new course. The combination of these three
     values must be unique for the new course. In addition, the total number of
     characters used for the name, organization, number, and run must be 65 or
     fewer.

  #. Select **Create Re-Run**. Your **My Courses** dashboard opens with a
     status message about the course creation process.

     Duplication of the course structure and content takes several minutes. You
     can work in other parts of Studio or in the LMS, or on other web sites,
     while the process runs. The new course appears on your **My Courses**
     dashboard in Studio when configuration is complete.

.. _Update the New Course:

*********************
Update the New Course
*********************

When you create a course by re-running another course, you must carefully
review the settings and content of the new course. To assure a quality
experience for learners, be sure to test the course thoroughly before the
course start date. See :ref:`Testing Your Course Content` and
:ref:`Beta_Testing`.

At a minimum, you must make the following changes to prepare the new
course for release.

* Add course team members, including discussion admins, moderators, and
  community TAs. See :ref:`Add Course Team Members` or :ref:`Course_Staffing`.

* Update course-wide dates, including course and enrollment start and end
  dates. See :ref:`Scheduling Your Course`.

* Change the release dates of course sections, subsections, and units. See
  :ref:`Release Dates`.

* Change the due dates of subsections that are part of your grading policy. See
  :ref:`Set the Assignment Type and Due Date for a Subsection`.

* Delete or edit posts on the **Course Updates** page in Studio. See :ref:`Add
  a Course Update`.

* For a course that includes :ref:`learner cohorts<Enabling and Configuring
  Cohorts>`, set up the cohorts and select a strategy for assigning learners to
  the cohorts.

* For a course that includes drag and drop problems, replace any problems
  created prior to April 2016 with the newer drag and drop problem component,
  which is accessible and mobile ready. For more information about enabling the
  new drag and drop problem type and adding these problems to your course, see
  :ref:`drag_and_drop_problem`.

The following additional changes can also improve the experience of learners
who enroll in the new course run.

* Review the files on the **Files & Uploads** page. To update a file that
  contains references to course-related dates, you must complete the
  following steps.

  1. Locate the source file.
  2. Change course-related dates in the file.
  3. Upload the revised version of the file.

  .. note:: If you use the same file name when you upload a revised file,
   links to that file in course components and course handouts will continue to
   work correctly. If you rename a file and then upload it, you must also
   update all links to the original file name. See :ref:`Add Course Handouts`
   or :ref:`Add a Link to a File`.

* Review the staff biographies and other information on the course About page
  and make needed updates. See :ref:`Planning Course Information` and
  :ref:`Planning Course Run Information`.

* Create initial posts for discussion topics and an "introduce yourself"
  post. See :ref:`Discussions`.

* Add initial wiki articles.

* For a course that includes core problem types, including checkbox, text
  input, or math expression input problems, review the
  :ref:`Markdown-style formatting <Simple Editor>` or :ref:`OLX markup
  <Advanced Editor>` of any problems created before September 2016.
  For more information about the updates that you can make to improve the
  accessibility of these problem types, see the `Release Notes
  <http://edx.readthedocs.io/projects/edx-release-notes/en/latest/studio_index.html#updates-to-capa-problem-types>`_.

* If your course uses prerequisite course subsections to hide course
  subsections until learners complete other, prerequisite subsections,
  configure the prerequisite course subsections. See
  :ref:`configuring_prerequisite_content`.

* If your course includes instructions for learners, verify that the
  instructions reflect the current user interface of the LMS.

  For example, you could revise a description of the problem **Check** button,
  which was accurate before October 2016, to reflect its new label, **Submit**.

  .. only:: Partners

    Another example of a user interface change is for courses on the edx.org
    website. A new **Help** option was added to the LMS in September 2016 to
    provide access to the *EdX Learner's Guide*. When this option was added,
    the previous **Help** option was renamed **Support**.

For more information about tools and ideas that can help you prepare a course
for launch, see :ref:`Launch`.

.. note::
  Changes you make in the new course have no effect on the original course.

.. include:: ../../../links/links.rst
