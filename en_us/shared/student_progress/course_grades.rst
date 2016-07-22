.. _Grades:

############################
Learner Grades and Grading
############################

You can review information about how grading is configured for your course, and
access learner grades, at any time after you create the course. You can also
make adjustments to learner grading for a problem, for a single learner or all
learners. For information about the grading data that you can access and the
changes you can make, see the following topics.

.. contents::
 :local:
 :depth: 1

To review learner answers to course problems, you can check the answer
submissions for a specific problem, either for a selected learner or for all
learners. You can also review answer distribution data for all of the problems.
See :ref:`Review_Answers`.

For open response assessments, you can generate an ORA data report that
provides details of each learner's response and of assessments that were
performed on each response. For details, see :ref:`Generate ORA Report`.

For information about how you establish a grading policy and work with the
Problem components in your course, see :ref:`Grading Index` or
:ref:`Working with Problem Components`.

.. _Review_grades:

********************************************************
Review How Grading Is Configured for Your Course
********************************************************

You can review the assignment types that are graded and their respective
weights in the LMS by selecting **Instructor** to access the instructor
dashboard.

You establish a grading policy for your course when you create it in Studio.
While the course is running, you can view an XML representation of the
assignment types in your course and how they are weighted to determine
learners' grades.

..  DOC-290: research this statement before including anything like it: Below the list of graded assignment types and their weights, each *public* subsection and unit that contains an assignment is listed.

#. View the live version of your course.

#. Select **Instructor**, and then select **Data Download** > **Grading
   Configuration**.

   A list of the assignment types in your course displays. In this example,
   Homework is weighted as 0.3 (30%) of the grade.

   .. image:: ../../../shared/images/Grading_Configuration.png
     :alt: XML of course assignment types and weights for grading.

   In Studio, you define this information by selecting **Settings** and then
   **Grading**. For more information, see :ref:`Configure the Assignment
   Types`.

   .. image:: ../../../shared/images/Grading_Configuration_Studio.png
     :alt: Studio example of homework assignment type and grading weight.

.. important:: Any changes that you make to the course grading policy, to
   graded subsections, or to graded components after the course begins will
   affect learners' experiences in the course as well as analysis of its data.
   EdX recommends that you announce any unavoidable changes learners by using,
   for example, the **Home** page. You should also carefully track these
   changes for researchers.

.. _Access_grades:

***********************************************************
Generate a Grade Report for Enrolled Learners (All Courses)
***********************************************************

For any course, you can generate grades and then download a file with the
results for each enrolled learner.

When you initiate calculations to grade learner work, a process starts on the
edX servers. The complexity of your grading configuration and the number of
learners enrolled in your course affect how long this process takes. You can
download a report of the calculated grades in a comma-separated values (.csv)
file when the grading process is complete.

For courses with fewer than 200 learners enrolled, you also have the option to
review learner grades on the instructor dashboard. For more information, see
:ref:`gradebook`.

To generate and download the grade report for the learners who are currently
enrolled in your course, follow these steps.

.. important:: Because the grade report file contains confidential, personally
   identifiable data which might be subject to the Family Educational Rights
   and Privacy Act (FERPA), be sure to follow your institution's data
   stewardship policies when you open or save this file.

#. View the live version of your course.

#. Select **Instructor**, and then select **Data Download**.

#. To start the grading process, select **Generate Grade Report**.

   A status message indicates that the grading process is in progress. This
   process can take some time to complete, but you can navigate away from this
   page and do other work while it runs.

#. To check the progress of the grading process, reload the page in your
   browser and scroll down to the **Pending Tasks** section. The
   status of active tasks is shown in the table.

   When the report is complete, a linked .csv file name becomes available above
   the **Pending Tasks** section. File names are in the format
   ``{course_id}_grade_report_{datetime}.csv``. The most recently generated
   reports appear at the top of the list.

#. To open or save a grade report file, locate and select the link for the
   grade report you requested.

   You can open .csv files in a spreadsheet application to sort, graph, and
   compare data.

.. note:: To prevent the accidental distribution of learner data, you can
   download grade report files only by selecting the links on this page. Do not
   copy these links for reuse elsewhere, as they expire within 5 minutes. The
   links on this page also expire if the page is open for more than 5 minutes.
   If necessary, refresh the page to generate new links.

.. _Interpret the Grade Report:

=============================
Interpreting the Grade Report
=============================

A grade report for your course is a time-stamped .csv file that identifies
each enrolled learner by ID, email address, and username, and provides a
snapshot of their cumulative course scores.

Scores in the grade report are presented by assignment. There is a column for
every assignment that is included in your grading configuration: each
homework, lab, midterm, final, and any other assignment type you added to your
course.

.. note:: The grade report does not include information about individual
   problems within assignments, or include learner answer distributions. For a
   report that shows problem-level information, see :ref:`problem_report`.

The report indicates the enrollment track for each learner. For professional
and verified track learners it also shows whether they have verified their
identity. The report shows whether each learner is eligible to receive a
certificate (determined by whether he has earned a passing grade at the time
the report was requested), whether a certificate has been generated, and the
type of certificate earned.

If your course includes :ref:`cohorts<Cohorts Overview>`, :ref:`content
experiments<Overview of Content Experiments>`, or
:ref:`teams<CA_Teams_Overview>`, the grade report includes additional columns
indicating the name of the cohort, experiment group, or team that each learner
belongs to.

.. image:: ../../../shared/images/Grade_Report.png
  :alt: A course grade report, opened in Excel, showing the grades achieved by
        learners on several homework assignments and the midterm.

The grade report .csv file contains one row of data for each learner, and
columns that provide the following information.

* Learner identifiers, including an internal **id**, **email** address, and
  **username**.

* The overall **grade**, with the total score a learner has currently attained
  in the course. This value is expressed as a decimal: a learner with a grade
  of 0.65 has earned 65% of the credit in the course, and a learner with a
  grade of 1 has earned 100%.

* Each **{assignment type} {number}** defined in your grading configuration,
  with the score that the learner attained for that specific assignment. For
  example, column HW 03 shows the scores for the third homework assignment.

* An **{assignment type} Avg** with each learner's current average score for
  that assignment type: for example, HW Avg.

* If :ref:`cohorts<Cohorts Overview>` are used in the course, a **Cohort Name**
  column indicates the name of the cohort that each learner belongs to,
  including the default cohort. The column is empty for learners who are not
  yet assigned to a cohort.

* If :ref:`content experiments<Overview of Content Experiments>` are used in
  the course, an **Experiment Group** column indicates the name of the
  experiment group that each learner belongs to within a group configuration.
  The column heading includes the name of the group configuration. The column
  is empty for learners who are not assigned to an experiment group. If you
  have more than one experiment group configuration in your course, you see one
  column for each group configuration.

* If :ref:`teams<CA_Teams_Overview>` are enabled in the course, a **Team
  Name** column indicates the name of the team that each learner belongs to. The
  column is empty for learners who have not joined a team.

* The **Enrollment Track** column indicates whether each learner is enrolled in
  the course in the honor code, verified, or professional education track.

* The **Verification Status** column applies only to learners who are enrolled
  in the verified or professional tracks. The value in this column indicates
  whether the verified or professional education learner has verified her
  identity to edX by using a webcam to submit her photo and an official ID.
  The value is "N/A" for learners who are not in the verified or professional
  tracks.

* The **Certificate Eligible** column indicates whether a learner is eligible
  for a certificate for your course. The value in this column is "Y" for
  learners who attained a passing grade before this report was requested, and
  for all whitelisted learners, regardless of grade attained. The value is "N"
  for learners who did not attain a passing grade and for those who live in
  embargoed countries.

* For learners who are eligible to receive a certificate, the **Certificate
  Delivered** column has a value of "Y" when the certificates for a course have
  been generated. The value is "N" for learners who are not eligible to
  receive a certificate.

* The **Certificate Type** column indicates the type of certificate that the
  learner is eligible for, such as "honor" or "verified". If a learner is not
  eligible for a certificate, or if the certificates for a course have not yet
  been generated, the value in this column is "N/A".

.. _problem_report:

*******************************************************************
Generate a Problem Grade Report for Enrolled Learners (All Courses)
*******************************************************************

For any course, you can calculate grades for problems and generate a report
that can be downloaded. The problem grade report for a course shows the number
of points that each learner has earned for each problem, and the number of
possible points for every problem in the course. In addition, the
report shows the final grade score for each learner.

To generate and download the problem grade report for the learners who are
currently enrolled in your course, follow these steps.

.. important:: Because the problem grade report file contains confidential,
   personally identifiable data which might be subject to the Family
   Educational Rights and Privacy Act (FERPA), be sure to follow your
   institution's data stewardship policies when you open or save this file.

#. View the live version of your course.

#. Select **Instructor**, and then select **Data Download**.

#. To start the problem grading process, select **Generate Problem Grade
   Report**.

   A status message indicates that the problem grading process is in progress.
   This process can take some time to complete, but you can navigate away from
   this page and do other work while it runs.

#. To check the progress of the problem grading process, reload the page in
   your browser and scroll down to the **Pending Tasks** section. The status of
   active tasks is shown in the table.

   When the report is complete, a linked .csv file name becomes available above
   the **Pending Tasks** section. File names are in the format
   ``{course_id}_problem_grade_report_{datetime}.csv``. The most recently
   generated reports appear at the top of the list.

#. To open or save a problem grade report file, locate and select the link for
   the problem grade report you requested.

   You can open .csv files in a spreadsheet application to sort, graph, and
   compare data.

.. note:: To prevent the accidental distribution of learner data, you can
   download problem grade report files only by selecting the links on this
   page. Do not copy these links for reuse elsewhere, as they expire within 5
   minutes. The links on this page also expire if the page is open for more
   than 5 minutes. If necessary, refresh the page to generate new links.

.. _Interpret the Problem Grade Report:

======================================
Interpreting the Problem Grade Report
======================================

A problem grade report for your course is a time-stamped .csv file that
identifies each enrolled learner by ID, email address, and username, and
provides a snapshot of earned scores compared with the possible scores for
each problem.

The problem grade report includes two columns for every problem that is
included in your grading configuration. For each homework, lab, midterm, or
final exam problem, there is one column for earned points, and one column for
possible points. In addition, the report shows the final grade score for each
learner, expressed as a decimal.

.. image:: ../../../shared/images/Problem_Grade_Report_Example.png
  :alt: An example problem grade report shown in Excel, showing the decimal
    final grade for learners as well as the earned vs possible points that they
    each achieved on several quiz assignments. A column for a midterm is only
    partially visible.

The .csv file contains one row of data for each learner, and columns that
provide the following information.

* Learner identifiers, including an internal **Student ID**, **Email** address,
  and **Username**.

* The **Final Grade**, with the total score that a learner has currently
  attained in the course. This value is expressed as a decimal: a learner with
  a grade of 0.65 has earned 65% of the credit in the course, and a learner
  with a grade of 1 has earned 100%.

* For each problem (identified by assignment, subsection, and problem name), a
  column showing the number of points actually earned by each learner. If a
  learner has not viewed a problem, the value in this column is "N/A". If
  a learner has not answered a problem, the value in this column is "0".

* For each problem (identified by assignment, subsection, and problem name), a
  column showing the number of points that it is possible to earn for the
  problem. If a learner has not viewed a problem, the value in this column
  is "N/A".

.. _gradebook:

********************************************************
Review Grades for Enrolled Learners (Small Courses)
********************************************************

For courses with enrollments of up to 200 learners, you can review a gradebook
on the instructor dashboard. To review grades for a small course, follow these
steps.

#. View the live version of your course.

#. Select **Instructor**, and then select **Student Admin**. For courses with
   fewer than 200 learners enrolled, this page includes a **Student Gradebook**
   section.

#. Select **View Gradebook**. Grades are calculated and the gradebook displays.

   .. image:: ../../../shared/images/Student_Gradebook.png
     :alt: Course gradebook with rows for learners and columns for assignment
         types.

The gradebook includes the following features.

* You can select the username in each row to review that learner's **Course
  Progress** page. For more information, see :ref:`check_student_progress`.

* There is a column for each **{assignment type} {number}** defined in your
  grading configuration, with the scores that the learner attained for that
  specific assignment.

  The gradebook does not have a scroll bar, but it can be dragged: to see
  columns that are hidden at one side of the grade book, select the gradebook
  and then drag left or right to reveal those columns.

* For assignment types that include more than one assignment, an **{assignment
  type} Avg** column displays each learner's current average score for that
  assignment type.

* The **Total** column presents the total score that each learner has currently
  attained in the course. This value is expressed as a whole number: a learner
  with a grade of 65 has earned 65% of the credit in the course, and a learner
  with a grade of 100 has earned 100%.

* To filter the data that displays you can use the **Search students** option.
  This option is case-sensitive and limits the rows shown in the gradebook to
  usernames that match your entry.


.. _check_student_progress:

****************************************
Check the Progress of a Single Learner
****************************************

To check a single learner's progress, you can locate the specific row on the
grade report or review the learner's **Progress** page. The **Progress** page
includes a chart that plots the score the learner has earned for every graded
assignment and the total grade as of the current date. Below the chart, each
assignment and the score attained are listed.

To review a learner's **Progress** page, you supply an email address or
username. You can check the progress for learners who are either enrolled in,
or who have unenrolled from, the course.

Learners can view a similar chart and assignment list (of their own progress
only) when they are logged in to the course. For more information, see :ref:`A
Students View`.

To view the **Progress** page for a learner, follow these steps.

#. View the live version of your course.

#. Select **Instructor**, and then select **Student Admin**.

#. In the Student-Specific Grade Inspection section, enter the learner's email
   address or username.

#. Select **Student Progress Page**.

   The **Progress** page for the learner displays a chart with the grade for
   each homework, lab, midterm, final, and any other assignment types in your
   course, and the total grade earned for the course to date. The chart does
   not reflect any cohort or experiment group assignments.

   .. image:: ../../../shared/images/Student_Progress.png
    :alt: Progress page chart for a learner: includes a column graph with the
          score achieved for each assignment.

   To learn more about a particular assignment, move the cursor onto the value
   in the chart. A brief description displays.

   .. image:: ../../../shared/images/Student_Progress_mouseover.png
    :alt: Progress page with a tooltip for the X that was graphed for the last
          homework assignment, which indicates that the lowest homework score
          is dropped.

   Below the chart, subsections are listed on the left and the units that
   contain assignments are listed on the right. The learner's individual
   problem scores display.

   .. image:: ../../../shared/images/Student_Progress_list.png
    :alt: Bottom portion of a Progress page for the same learner with the
          score achieved for each problem in the first course subsection.

=============================================
Interpreting the Learner Progress Page
=============================================

The chart of a learner's scores on the **Progress** page and the rows of data
on the grade report present assignment scores in a similar order. However, the
total, cumulative score earned for the course is placed in a different position
on the **Progress** page.

In this example grade report, the indicated learner has a current grade of 0.43
(43%).

.. image:: ../../../shared/images/Grade_Report_example.png
 :alt: A course grade report with a single learner's information indicated by
       a rectangle.

* On each of the first four homework assignments the learner scored 1 (100%),
  but currently has a 0 (0%) on each of the remaining three assignments.

  Notice, however, that the learner's current average score for homework
  assignments is listed as 0.666666667 (67%): in this course, the homework
  assignment with the lowest score is dropped, so this average is over six
  assignments rather than all seven.

* The learner has a score of 0.75 (75%) on the midterm, and a score of 0 (0%)
  on the final.

On the learner's **Progress** page, you see the same information graphically
represented; however, the learner's "total" of 43% is on the far right.

.. image:: ../../../shared/images/Student_Progress.png
 :alt: Progress page for a learner also included on the grade report: includes
       a column graph with the grade achieved for each assignment.

The chart on the **Progress** page includes y-axis labels for the grade ranges
defined for the course. In this example, Pass is set to 60%, so at the end of
the course, learners with a grade of 0.60 or higher can receive certificates.

.. note:: Learner scores on the **Progress** page are a snapshot of the
 current state of the problem score database. They can, at times, be out of
 sync with actual problem scores. For example, asynchronicities can occur if
 the weight of a live problem was changed during an assignment, and not all
 learners have resubmitted their answers for that problem.

.. _A Students View:

=============================================
A Learner's View of Course Progress
=============================================

Learners can check their progress by selecting **Progress** in the course
navigation bar. The learner's progress through the graded part of the course
displays at the top of this page, above the subsection scores. Progress is
visualized as a chart with entries for all the assignments, total percentage
earned in the course so far, and percent needed for each grade cutoff. Here is
an example of a learner's progress through edX101.

.. image:: ../../../shared/images/StudentView_GradeCutoffs.png
 :alt: Image of a learner's Course Progress page with the grade cutoffs legend
       highlighted.

The learner can see from this page that edX101 was graded as a Pass/Fail
course with a cutoff of 34% and that the grading rubric contained one
assignment type, called Learning Sequence, consisting of 11 assignments total.
Furthermore, this particular learner has only submitted correct responses to
two assignments, and her current total percent grade in the course is 6%. By
hovering over each progress bar, learners can get further statistics of how
much each assignment was counted as.

Further down on the **Progress** page is a list of all the subsections in the
course, with the scores recorded for the learner for all problems in the
course. Here is the **Progress** page for the learner in the example above:

.. image:: ../../../shared/images/StudentView_Problems.png
   :width: 800
   :alt: Image of a learner's Course Progress page with problems highlighted.

Note that point scores from graded sections are called "Problem Scores",
while point scores from ungraded sections are called "Practice Scores".

.. _Adjust_grades:

***********************************
Adjusting Grades
***********************************

If you modify a problem or its settings after learners have attempted to answer
it, learners' grades can be affected. For information about making changes to
problems in Studio, see :ref:`Modifying a Released Problem`.

To make adjustments to learner grades, you need the unique location identifier of the modified problem. For more information, see :ref:`find_URL`.

The following sections describe the various ways in which you can adjust
learners' grades when a correction or other change is unavoidable.

.. contents::
 :local:
 :depth: 1








.. _find_URL:

==================================================
Find the Unique Location Identifier for a Problem
==================================================

When you create each of the problems for a course, edX assigns a unique
location to it. To make grading adjustments for a problem, or to view data
about it, you need to specify the problem location.

Location identifiers for problems can be in one of these formats.

* ``location = block-v1:{org}+{course}+{run}+type@problem+block@{id}``, for
  example, ``location = block-v1:edX+BlendedX+1T2015+type@problem+block@72e0f73cdf5c4d648ebec0022854f18b``

* ``location = i4x://{org}/{course}/problem/{id}``, for example,
  ``location = i4x://edX/edX101/problem/680cc746e8ee473490841334f0235635``

Courses created since Fall 2014 typically have usage IDs in the first format,
while older courses have usage IDs in the second format.

To find the unique location identifier for a problem, follow these steps.

#. View the live version of your course.

#. Select **Course**, and then navigate to the unit that contains the
   problem.

#. Display the problem, and find the **Submission History** and **Staff Debug
   Info** options that appear below it.

#. Select **Staff Debug Info**. Information about the problem appears,
   including its **location**.

#. To copy the location of the problem, select the entire value after
   ``location =``, right click, and then select **Copy**.

To close the Staff Debug viewer, click on the browser page outside of the
viewer.

.. _rescore:

==========================================
Rescore Learner Submissions for a Problem
==========================================

Each problem that you create for your course includes the definition of a
correct answer, and might also include a tolerance or acceptable alternatives.
If you decide to make a change to the answers for a problem, you can also
rescore any responses that were already submitted. For a specified problem,
you can rescore the work submitted by a single learner, or rescore the
submissions made by every enrolled learner.

.. note:: You can only rescore problems that have a correct answer defined in
   edX Studio. This procedure cannot be used to rescore open response
   assessment problems, or problems that are scored by an external grader.

   Additionally, errors might occur if you rescore a problem that has multiple
   response fields and you have completed any of the following actions.

   * You removed a response field.
   * You added a response field.
   * You reordered any of the response fields.

.. note:: Do not use this method to rescore open response assessment (ORA)
   problems. For ORA problems, you can :ref:`override a learner assessment
   grade<Override a learner assessment grade>` in Studio.


Rescore a Submission for an Individual Learner
-----------------------------------------------

To rescore a problem for a single learner, you need that learner's username or
email address.

#. View the live version of your course.

#. Select **Course** and navigate to the component that contains the
   problem you want to rescore.

#. Display the problem, and then select **Staff Debug Info**. The Staff Debug
   viewer opens.

#. In the **Username** field, enter the learner's email address or username,
   and then select **Rescore Student Submission**. A message indicates a
   successful adjustment.

#. To close the Staff Debug viewer, click on the browser page outside of the
   viewer.

Rescore Submissions for All Learners
------------------------------------

To specify the problem you want to rescore, you need its location identifier.
See :ref:`find_URL`. To rescore a problem:

#. View the live version of your course.

#. Select **Instructor**, and then select **Student Admin**.

#. In the **Course-Specific Grade Adjustment** section of the page, enter the
   unique problem location, and then select **Rescore ALL students' problem
   submissions**.

#. When a dialog box notifies you that the rescore process is in progress,
   select **OK**.

   This process can take some time to complete for all enrolled learners. The
   process runs in the background, so you can navigate away from this page and
   do other work while it runs.

#. To view the results of the rescore process, select either **Show Background
   Task History for Student** or **Show Background Task History for Problem**.

   A table displays the status of the rescore process for each learner or
   problem.

.. note:: You can use a similar procedure to rescore the submission for a
 problem by a single learner. You work in the **Student-Specific Grade
 Adjustment** section of the page to enter both the learner's email address or
 username and the unique problem identifier, and then select **Rescore Student
 Submission**.

.. _reset_attempts:

=====================================
Reset Learner Attempts for a Problem
=====================================

When you create a problem, you can limit the number of times that a learner
can try to answer that problem correctly. If unexpected issues occur for a
problem, you can reset the value for one particular learner's attempts back to
zero so that the learner can begin work over again. If the unexpected behavior
affects all of the learners in your course, you can reset the number of
attempts for all learners to zero.

.. note:: You cannot use this method with open response assessment (ORA)
   problems. To allow a learner to start an ORA problem again and resubmit
   responses, you must :ref:`delete the learner's state<delete_state>`.

Reset Attempts for an Individual Learner
---------------------------------------------

To reset the number of attempts for a single learner, you need that learner's
username or email address.

#. View the live version of your course.

#. Select **Course** and navigate to the component that contains the
   problem you want to reset.

#. Display the problem, and then select **Staff Debug Info**. The Staff Debug
   viewer opens.

#. In the **Username** field, enter the learner's email address or username,
   and then select **Reset Student Attempts**. A message indicates a successful
   adjustment.

#. To close the Staff Debug viewer, click on the browser page outside of the
   viewer.

Reset Attempts for All Learners
------------------------------------

To reset the number of attempts that all enrolled learners have for a problem,
you need the unique identifier of the problem. For more information, see
:ref:`find_URL`.

To reset attempts for all learners, follow these steps.

#. View the live version of your course.

#. Select **Instructor**, and then select **Student Admin**.

#. To reset the number of attempts for all enrolled learners, you work in the
   **Course-Specific Grade Adjustment** section of the page. Enter the unique
   problem location, and then select **Reset ALL students' attempts**.

#. A dialog opens to indicate that the reset process is in progress. Select
   **OK**.

   This process can take some time to complete. The process runs in the
   background, so you can navigate away from this page and do other work while
   it runs.

#. To view the results of the reset process, select either **Show Background
   Task History for Student** or **Show Background Task History for Problem**.

   A table displays the status of the reset process for each learner or
   problem.

.. note:: You can use a similar procedure to reset problem attempts for a
 single learner. You work in the **Student-Specific Grade Adjustment** section
 of the page to enter both the learner's email address or username and the
 unique problem identifier, and then select **Reset Student Attempts**.

.. _delete_state:

=======================================
Delete a Learner's State for a Problem
=======================================

You can completely delete a learner's database history, or "state", for a
problem. You can only delete learner state for one learner at a time.

For example, you realize that a problem needs to be rewritten after only a few
of your learners have answered it. To resolve this situation, you rewrite the
problem and then delete learner state only for the affected learners so that
they can try again.

To delete a learner's entire history for a problem from the database, you need
that learner's username or email address.

.. important:: Learner state is deleted permanently by this process. This
   action cannot be undone.

   When you delete a learner's state for an open response assessment (ORA)
   problem, the learner will have to start the assignment from the beginning,
   including submitting responses and going through the required assessment
   steps.

You can use either the Staff Debug viewer or the instructor dashboard to delete
learner state.

To use the Staff Debug viewer, follow these steps.

#. View the live version of your course.

#. Select **Course** and navigate to the component that contains the
   problem.

#. Display the problem, and then select **Staff Debug Info**. The Staff Debug
   viewer opens.

#. In the **Username** field, enter the learner's email address or username,
   and then select **Delete Student State**. A message indicates a successful
   adjustment.

#. To close the Staff Debug viewer, click on the browser page outside of the
   viewer.

To use the instructor dashboard, you must first obtain the unique identifier of
the problem. See :ref:`find_URL`.

#. Select **Instructor**, and then select **Student Admin**.

#. In the **Student-Specific Grade Adjustment** section of the page, enter both
   the learner's email address or username and the unique problem identifier,
   and then select **Delete Student State for Problem**.
