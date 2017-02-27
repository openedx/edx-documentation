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

After you re-run a course, modifications to the original course and the re-run
course are independent. Changes to either course have no effect on the other
course. Therefore, you should ensure that the original course content is as
complete as possible before you re-run the course.

For more information, see :ref:`Use Re-Run to Create a Course` and
:ref:`Update the New Course`.

.. _Use Re-Run to Create a Course:

********************************************
Use Re-Run to Create a Course
********************************************

.. only:: Partners

   Only edX staff members have the permissions needed to re-run a course. To
   re-run a course that is hosted on the `edx.org`_ or `edX Edge`_ sites,
   contact your edX partner manager. After your partner manager creates the new
   course using the re-run feature, you can complete the steps to
   :ref:`update the new course<Update the New Course>`.

.. only:: Open_edX

   Only global or system administrators have the permissions needed to re-run
   a course. To re-run a course, contact your system administrator. After your
   system administrator creates a new course using the re-run feature, you can
   complete the steps to :ref:`update the new course<Update the New Course>`.

.. note:: Before you re-run a course, make sure that its settings and content
  are complete. Additions and changes that you make to the original course
  after you create the new course have no effect on the new course.

.. only:: Open_edX

  To re-run a course, users who have the required permissions follow these
  steps.

  #. Sign in to Studio. Your dashboard lists the courses that you have access
     to as a course team member.

  #. Move your cursor over each row in the list of courses. The **Re-Run
     Course** and **View Live** options appear for each course.

     .. image:: ../../../shared/images/Rerun_link.png
      :alt: A course listed on the dashboard with the Re-run Course and View
             Live options shown.
      :width: 600

  #. Locate the course you want to re-run and select **Re-Run Course**. The
     **Create a re-run of a course** page opens with values already supplied in
     the **Course Name**, **Organization**, and **Course Number** fields.

     .. image:: ../../../shared/images/rerun_course_info.png
       :alt: The course creation page for a rerun, with the course name,
             organization, and course number supplied.
       :width: 600

  #. Supply a **Course Run** to indicate when the new course will be offered.

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

********************************************
Update the New Course
********************************************

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

* Review the staff biographies and other information on the course summary
  page and make needed updates. See :ref:`The Course About Page`.

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
  subsections until learners complete other, prerequisite subsections, configure the prerequisite course subsections. See :ref:`configuring_prerequisite_content`.

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
