.. _pt Proctored Session Results:

###################################################
Viewing Proctored Session Results with Proctortrack
###################################################

To review individual violation videos and screenshots, follow these steps:

#. In the LMS, open the Proctortrack Review Dashboard by navigating to the **edX Instructor Dashboard** 
   -> **Special Exams** tab -> **Review Dashboard**.

#. The Verificient **Proctortrack Review Dashboard** will load inline in the LMS. 

#. Navigate to the **Quiz List** tab and locate the exam you want to review.

#. Click on **View Sessions** to open the list of learners who took the exam

#. Review all learners who are flagged as “Require Attention” as follows.

#. To review an individual learner’s session, click on the learner’s name to pop out 
   their detailed exam results in a new tab. Here you can review their exam data, including Video 
   Monitoring, Online Violations, Verification scans, and Onboarding tabs to understand what infractions 
   (if any) were flagged as suspicious

#. If the suspicious behavior is deemed to be in violation of proctoring rules of your course, 
   select **Fail** to fail the learner and set their grade to 0. Learners will get an email informing them that they did not pass proctoring review, and their grade was set to 0. 

#. If needed, you can later revert this decision by clicking **Pass** to pass the learner and 
   restore their original exam grade.

#. If needed, you can download the violation screenshot and data by clicking the **Export Data arrow**.

To see a summary of proctored exam results, you use the Proctored Exam Results
report. This report is a .csv file that you can download from the instructor
dashboard. You can use this report to view proctoring results for all learners,
or :ref:`determine whether a specific learner has passed the proctoring
review<Determine if Learner Passed Proctoring Review>`.

.. note::
 The Proctored Exam Results report contains information about the proctoring
 review. The report does not include information about the learner's score on
 the exam. A learner might pass the proctoring review but not earn a high
 enough score to pass the exam itself.

For more information about the Proctored Exam Results report, see the following
sections.

.. contents::
  :local:
  :depth: 1

.. _Viewing PT Proctored Session Results:

*********************************************
Download the Proctored Exam Results Report
*********************************************

At any time after learners have taken the proctored exam in your course, you
can download a .csv file that displays the current status of the proctoring
session for participating learners.

To generate and download the Proctored Exam Results report, follow these
steps.

.. important::
   This report contains confidential, personally identifiable data. Be sure to
   follow your institution's data stewardship policies when you open or save
   this report.

#. View the live version of your course.

#. In the LMS, select **Instructor**, then select **Data Download**.

#. In the **Reports** section, select **Generate Proctored Exam Results
   Report**.

   A status message indicates that the report generation process is in
   progress. This process can take some time to complete. You can navigate away
   from this page while the process runs.

#. To check the progress of the report generation, reload the page in your
   browser and scroll to the **Pending Tasks** section. The table shows the
   status of active tasks.

   When the report is complete, a linked .csv file name becomes available in
   the **Reports Available for Download** section. The most recently generated
   reports appear at the top of the list.

   File names are in the following format.

   ``{course_id}_proctored_exam_results_report_{datetime}.csv``

#. To download a report file, select the link for the report you requested.
   The .csv file begins downloading automatically.

.. note::
   To prevent the accidental distribution of learner data, you can download
   exam result report files only by clicking the links on this page. These
   links expire after 5 minutes. If necessary, refresh the page to generate new
   links.

#. When the download is complete, open the .csv files in a spreadsheet
   application to sort, graph, and compare data.

.. _PT Proctored Session Results File:

********************************************
Interpret the Proctored Exam Results Report
********************************************

The Proctored Exam Results report contains the following fields.

.. list-table::
   :widths: 30 55
   :header-rows: 1

   * - Column
     - Description
   * - course_id
     - The ID of the course.
   * - exam_name
     - The name of the proctored exam in the body of the course.
   * - username
     - The username that identifies the learner taking the proctored exam.
   * - email
     - The email address that identifies the learner taking the proctored exam.
   * - attempt_code
     - An identifier for the exam attempt. The attempt code is an
       internal identifier and is included in the report for use in
       troubleshooting.
   * - allowed_time_limit_mins
     - The amount of time in minutes that this learner was allotted for
       completing the exam.
   * - is_sample_attempt
     - Indicates whether this exam attempt was for a practice exam.
   * - started_at
     - The date and time that the learner started to take the proctored exam.
   * - completed_at
     - The date and time that the learner submitted the proctored exam.
   * - status
     - The current status of the proctoring session as a whole. The proctoring
       session encompasses the time from when the learner chooses to take the
       proctored exam until the proctored exam review is complete. If the
       proctored exam review is complete, the value in the ``review_status``
       column affects the value in this column.

       For possible values in the status column and an explanation of each
       value, see :ref:`Proctoring Results Status Column`.

   * - review_status
     - The current status of the proctoring exam review by
       Proctortrack/the course team. If the proctored exam review is
       complete, the value in this column affects the value in the
       ``status`` column.

       For possible values and an explanation of each value, see
       :ref:`Proctoring Results Review Status Column PT`.

   * - Suspicious Count
     - Number of incidents during the exam that Proctortrack marked as
       "Suspicious".
   * - Suspicious Comments
     - The comments that Proctortrack entered for each "Suspicious"
       incident, separated by semicolons (;).
   * - Rules Violation Count
     - Number of incidents during the exam that Proctortrack marked as
       "Rules Violation".
   * - Rules Violation Comments
     - The comments that Proctortrack entered for each "Rules Violation"
       incident, separated by semicolons (;).

.. _Proctoring Results Status Column:

===============================
Values in the ``status`` Column
===============================

The following table describes the possible values in the ``status`` column.

.. list-table::
   :widths: 30 55
   :header-rows: 1

   * - Value
     - Description
   * - completed
     - The learner has completed the proctored exam.
   * - created
     - The exam attempt record has been created, but the exam has not yet been
       started.
   * - declined
     - The learner declined to take the exam as a proctored exam.
   * - error
     - An error has occurred with the exam.
   * - expired
     - The course end date passed before the learner completed the proctored
       exam.
   * - ready_to_start
     - The exam attempt record has been created. The learner still needs to
       start the exam.
   * - ready_to_submit
     - The learner has completed but not yet submitted the proctored exam.
   * - rejected
     - The proctoring session review has been completed, and the learner has
       not passed the review. The learner receives a value of "Unsatisfactory"
       on the learner exam page and in a notification email message.
       Additionally, the learner automatically receives a score of 0 for the
       exam. For most courses, the learner is no longer eligible for academic
       credit.

       This value results from a value of "Suspicious" in the
       :ref:`review_status<Proctoring Results Review Status Column PT>`
       column after a member of the course team marks the exam session
       a failure in the Proctortrack dashboard.

   * - second_review_required
     - The exam attempt has been reviewed and the review team has determined
       that the exam requires additional evaluation. Course teams
       should perform this second round of review, as described
       :ref:`above<pt Proctored Session Results>`

       This status results from a value of "Suspicious" in the
       :ref:`review_status<Proctoring Results Review Status Column PT>` column.

   * - started
     - The learner has started the proctored exam.
   * - submitted
     - The learner has completed the proctored exam and results have been
       submitted for review.
   * - timed_out
     - The proctored exam has timed out.
   * - verified
     - The proctoring session review has been completed, and the learner has
       passed the review. The learner receives a value of "Satisfactory" on the
       learner exam page and in a notification email message.

       This value results from a value of "Clean" or "Rules Violation" in the
       :ref:`review_status<Proctoring Results Review Status Column PT>` column.


.. _Proctoring Results Review Status Column PT:

======================================
Values in the ``review_status`` Column
======================================

After learners complete a proctored exam, a reviewer from the proctoring
service provider reviews the exam according to specific criteria, including the
:ref:`Online Proctoring Rules <Online Proctoring Rules>`. The value in the
``review_status`` column shows the outcome of the proctored exam review.

Additionally, the value in the ``review_status`` column affects the following
information for the course team and for the learner.

* The values in the ``status`` column.
* The proctoring result that is visible on the learner exam page and in the
  email notification that the learner receives.

For example, if the ``review_status`` column has a value of "Clean", the value
in the ``status`` column is "verified". On the learner exam page and in the
email notification, the status of the exam is "Satisfactory".

If the ``review_status`` column has a value of "Suspicious", the value
in the ``status`` column is "second_review_required" or "rejected". If
the ``status`` is "rejected", then on the learner exam page and in the email
notification, the status of the exam is "Unsatisfactory".

The following table describes the possible values in the ``review_status``
column.

.. list-table::
   :widths: 30 20 55
   :header-rows: 1

   * - Value
     - Exam Result
     - Description
   * - Clean
     - Pass
     - No rules violations or suspicious incidents occurred. The learner has
       passed the proctoring review.

       This value causes a value of "verified" in the ``status`` column. The
       learner receives a result of "Satisfactory" for the proctored exam.

   * - Not Reviewed
     - n/a
     - The proctoring review is not yet complete.
   * - Rules Violation
     - Pass
     - An incident occurred that violates proctored exam rules, but the
       incident does not compromise exam integrity. For example, music may be
       playing. The learner has passed the proctoring review.

       This value causes a value of "verified" in the ``status`` column. The
       learner receives a result of "Satisfactory" for the proctored exam.

   * - Suspicious
     - Fail
     - An incident has occurred that directly compromises exam integrity. For
       example, cheating might have occurred. The learner has failed the
       proctoring review.

       This value causes a value of "second_review_required" or
       "rejected" in the ``status`` column. The learner receives a
       result of "Unsatisfactory" for the proctored exam in the latter
       case.  The learner also receives a score of 0 on the exam. In
       most courses, the learner is no longer eligible for academic
       credit.


.. _Determine if Learner Passed Proctoring Review:

*******************************************************
Determine if a Learner Passed the Proctored Exam Review
*******************************************************

To determine whether a specific learner passed the proctored exam review, you
can either view the Proctored Session Results report or view the course as the
learner.

=========================================
View the Proctored Session Results Report
=========================================

#. Download and open the Proctored Session Results report.
#. In the row for the learner, check the ``status`` column.

   * If the value in the column is "verified", the learner passed the review.
   * If the value is "rejected", the learner did not pass the review. The
     learner automatically receives a score of 0 on the exam. Additionally, for
     most courses, the learner is no longer eligible for academic credit.

==============================
View the Course as the Learner
==============================

#. :ref:`View the course as the learner that you want<Roles for Viewing Course
   Content>`.
#. Open the page for the proctored exam.

On the page, the learner's status is visible as "Pending", "Satisfactory", or
"Unsatisfactory".
