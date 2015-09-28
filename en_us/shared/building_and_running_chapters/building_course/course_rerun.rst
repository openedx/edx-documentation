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
   * - Course Updates 
     - Yes.
   * - Advanced Settings
     - Yes.
   * - Grading policy
     - Yes.
   * - Student enrollment data
     - No.
   * - Course team privileges, including admins, discussion moderators, beta
       testers
     - No. Only the user who created the new course has access to it.
   * - Manually created cohort groups
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
course are independent. Changes to either course are not propagated to the
other course. Therefore, you should ensure that the original course content is
as complete as possible before you re-run the course.

For more information, see :ref:`Use Re-Run to Create a Course` and
:ref:`Update the New Course`.

.. _Use Re-Run to Create a Course:

********************************************
Using Re-Run to Create a Course
********************************************

.. only:: Partners

   Only edX Partner Managers have the permissions needed to re-run a course.
   To re-run a course that is hosted on the `edx.org`_ or `edge.edx.org`_
   sites, contact your edX Partner Manager. After your Partner Manager creates
   the new course using the re-run feature, you can complete the steps to
   :ref:`update the new course<Update the New Course>`.

.. only:: Open_edX

   Only global or system administrators have the permissions needed to re-run
   a course. To re-run a course, contact your system administrator. After your
   system administrator creates a new course using the re-run feature, you can
   complete the steps to :ref:`update the new course<Update the New Course>`.

.. note:: Before you re-run a course, ensure that the course content is
   complete. Additions and changes that you make to the original course after
   creating the new course are not propagated to the new course.

.. Comment out the procedure to create rerun, since only Global Admin (i.e.
.. edX internal can do this) Done as part of DOC-2236 (CT, Sept 11, 2015)
   To re-run a course, follow these steps.

   #. Log in to Studio. Your dashboard lists the courses that you have access
      to as a course team member.

   #. Move your cursor over each row in the list of courses. The **Re-Run
      Course** and **View Live** options appear for each course.

      .. image:: ../../../shared/building_and_running_chapters/Images/Rerun_link.png
        :alt: A course listed on the dashboard with the Re-run Course and View 
           Live options shown 
        :width: 600

   #. Locate the course you want to re-run and select **Re-Run Course**. The
      **Create a re-run of a course** page opens with values already supplied
      in the **Course Name**, **Organization**, and **Course Number** fields.

      .. image:: ../../../shared/building_and_running_chapters/Images/rerun_course_info.png
        :alt: The course creation page for a rerun, with the course name, 
           organization, and course number supplied.
        :width: 600

   #. Supply a **Course Run** to indicate when the new course will be offered. 
   
   Together, the course number, the organization, and the course run are used
   to create the URL for the new course. The combination of these three values
   must be unique for the new course. In addition, the total number of
   characters used for the name, organization, number, and run must be 65 or
   fewer.

   5. Select **Create Re-Run**. Your **My Courses** dashboard opens with a status
   message about the course creation process.

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
  
You can use the :ref:`course checklists<Use the Course Checklist>` to work
through the course and verify that it is ready for release. You can also refer
to the :ref:`Launch` topic for tools and ideas that help you prepare the
course for launch.

.. note:: 
  Changes you make in the new course are not propagated to the original course.

.. _edge.edx.org: http://edge.edx.org
.. _edx.org: http://edx.org
