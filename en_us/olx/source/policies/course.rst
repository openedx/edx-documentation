.. _Course Policies:

#################################
Course Policies
#################################

You create a course policy file to specify metadata about your course.

.. contents::
  :local:
  :depth: 1

*******************************
Create the Course Policy File
*******************************

You define policies for your course in the ``policy.json`` file.

Save the ``policy.json`` file in the ``policy/<course-name>`` directory.

The ``<course-name>`` directory  must match the value of the ``url_name``
attribute in the ``course.xml`` file.

************************************
Course Policy JSON Objects
************************************

  .. list-table::
     :widths: 10 80
     :header-rows: 0

     * - ``start``
       - The start date for the course.  For example: ``"2012-09-05T12:00"``.
     * - ``advertised_start``
       - The start date displayed in the course listing and course about pages.
         For example: ``"2012-09-05T12:00``.
     * - ``disable_policy_graph``
       - Whether the policy graph should be disabled (``true``) or not
         (``false)``.
     * - ``enrollment_start``, ``enrollment_end``
       - The dates in which students can enroll in the course. For example,
         ``"2012-09-05T12:00"``. If not specified, students can enroll any
         time.
     * - ``end``
       - The end date for the course.  For example: ``"2012-11-05T12:00"``.
     * - ``end_of_course_survey_url``
       - The URL for an end of course survey. The link is shown after the
         course is over, next to certificate download links.
     * - ``tabs``
       - Custom pages, or tabs, in the courseware.  See below for details.
     * - ``discussion_blackouts``
       - An array of time intervals during which students cannot create or edit
         discussion posts. For example, you could specify blackout dates during
         exams. For example:

         ``[[""2012-10-29T04:00", "2012-11-03T04:00"], ["2012-12-30T04:00", "2013-01-02T04:00"]]``

         Course team members with the Discussion Moderator, Community TAs, or
         Administrator role are not restricted during blackout periods.

     * - ``show_calculator``
       - Whether the calculator is shown in the course (``true``) or not
         (``false)``.
     * - ``days_early_for_beta``
       - The number of days early that students in the beta-testers group can
         access the course.
     * - ``cohort_config``
       -
          * ``cohorted`` : Boolean.  Set to ``true`` if this course uses
            student cohorts.  If so, all inline discussions are automatically
            cohorted, and top-level discussion topics are configurable via the
            ``cohorted_discussions`` list. Default is ``false``, not cohorted).
          * ``cohorted_discussions``: list of discussion topics that should be
            cohorted.  Any not specified in this list are not cohorted.
          * ``auto_cohort_groups``: ``["group name 1", "group name 2", ...]``
            If ``cohorted`` is ``true``, each student is automatically assigned
            to a random group from this list, creating the group if needed.
     * - ``pdf_textbooks``
       - Have pdf-based textbooks on tabs in the courseware.  See below for
         details.
     * - ``html_textbooks``
       - The addition of HTML-based textbooks on tabs in the courseware has
         been deprecated.



.. disable_policy_graph above had "SUPORTED?" after it, moved to this comment 26 Oct 2015 - Alison

*******************************
Example Course Policy File
*******************************

An example with a few of the settings defined in the course policy file
follows.

.. code-block:: json

    {
      "course/course": {
        "advanced_modules": [
            "poll",
            "survey",
        ],
        "discussion_blackouts": [],
        "discussion_topics": {
            "General": {
                "id": "course"
            }
        "show_calculator": true,
        "show_reset_button": true,
        "start": "2017-10-01T00:30:00Z",
        "tabs": [
            {
                "course_staff_only": false,
                "name": "Home",
                "type": "course_info"
            },
            {
                "course_staff_only": false,
                "name": "Course",
                "type": "courseware"
            },
            {
                "course_staff_only": false,
                "name": "Discussion",
                "type": "discussion"
            },
            {
                "course_staff_only": false,
                "is_hidden": true,
                "name": "Wiki",
                "type": "wiki"
            },
            {
                "course_staff_only": false,
                "name": "Progress",
                "type": "progress"
            },
            {
                "course_staff_only": true,
                "name": "Staff only (Alison)",
                "type": "static_tab",
                "url_slug": "7cf2fccec33541dc81ce5e0e34e2689c"
            }
        ],
        "user_partitions": [
            {
                "active": true,
                "description": "The groups in this configuration can be mapped to cohort groups in the LMS.",
                "groups": [
                    {
                        "id": 1124782865,
                        "name": "Group A",
                        "version": 1
                    },
                    {
                        "id": 254579781,
                        "name": "Group B",
                        "version": 1
                    }
            }
        ]
    }
