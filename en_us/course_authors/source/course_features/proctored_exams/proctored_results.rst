.. _Proctored Session Results:

################################
Using Proctored Session Results
################################

This section provides an overview of how to use the data you receive about
how learners performed in proctoring sessions for proctored exams. For more
information, see :ref:`CA_ProctoredExams_Overview` and
:ref:`Managing Proctored Exams`.

.. contents::
  :local:
  :depth: 1

The proctoring software monitors both the screen activity and webcam view of
learners. When learners complete a proctored exam, their proctoring session
data is uploaded for review by the proctoring service provider. Reviewers
apply defined criteria including the :ref:`Online Proctoring Rules
<CA Online Proctoring Rules>` to decide whether any observed behavior should be
flagged.

Two results are possible for proctoring session reviews.

*  **Satisfactory** - the learner has passed the proctoring review.

*  **Unsatisfactory** - Some suspicious activity has been observed. The
   learner has not passed the proctoring review.

Some learner behavior that is listed in the Online Proctoring Rules is
discouraged but does not impact the integrity of the exam. Violations in these
cases might be flagged but learners with such flags can still receive a
**Satisfactory** result. For example, a learner is discouraged from playing
music or having a TV on in the background while they take their exam, but if
their session recording shows such behavior, it is still possible for them to
receive a **Satisfactory** result for their proctoring session results, as long
as there are no instances of suspicious activity that do seem to indicate
cheating.

Activities that would cause learners to fail their proctoring session review
include not providing a photo ID, using a second computer during the proctored
exam, appearing to read the exam to another person in the room, displaying
nudity or explicit materials or browsing adult-based content. If there is even
one instance of such activity, learners receive an **Unsatisfactory** result
for their proctoring session.


.. _Viewing Proctored Session Results:

************************************
Viewing Proctored Session Results
************************************

At any time after learners have taken the proctored exam in your course, you
can download a .csv file that displays the status of the proctoring session
for participating learners.

.. note:: The Proctored Session Results report only shows the result of
   reviews of the proctored sessions. These results are separate from the
   learners' grades on the exam.

To generate and download a file of proctoring session results, follow these
steps.

.. important:: Because the proctoring session results file contains
   confidential, personally identifiable data, be sure to follow your
   institution's data stewardship policies when you open or save this file.

#. View the live version of your course.

#. In the LMS, select **Instructor**, then select **Data Download**.

#. Select **Generate Proctored Exam Results Report**.

   .. image:: ../../../../shared/images/Proctoring_GenerateCSVExamResults.png
     :alt: The "Generate Proctored Exam Results Report" button in the LMS.
     :width: 400

   A status message indicates that the report generation process is in
   progress. This process can take some time to complete, but you can navigate
   away from this page and do other work while it runs.

#. To check the progress of the report generation, reload the page in your
   browser and scroll down to the **Pending Tasks** section. The status of
   active tasks is shown in the table.

   When the report is complete, a linked .csv file name becomes available
   above the **Pending Tasks** section. File names are in the format
   ``{course_id}_proctored_exam_results_report_{datetime}.csv``. The most
   recently generated reports appear at the top of the list.

#. To open or save a report file, locate and click the link for the report you
   requested.

   .. image:: ../../../../shared/images/Proctoring_CSVExamResultsLink.png
     :alt: The link for a generated proctored exam results report in the
         instructor dashboard.
     :width: 600

   You can open .csv files in a spreadsheet application to sort, graph, and
   compare data.

.. note:: To prevent the accidental distribution of learner data, you can
   download exam result report files only by clicking the links on this page.
   Do not copy these links for reuse elsewhere, as they expire within 5
   minutes. The links on this page also expire if the page is open for more
   than 5 minutes. If necessary, refresh the page to generate new links.


.. _Proctored Session Results File:

**************************************************
Understanding the Proctored Session Results File
**************************************************

The .csv file that you can download to view the status and results of
learners' proctoring sessions contains the following fields.


.. list-table::
   :widths: 30 55
   :header-rows: 1

   * - Column
     - Description
   * - user_email
     - The username or email address that identifies the learner taking the
       proctored exam.
   * - exam_name
     - The name of the proctored exam in the body of the course.
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
     - The status of the proctoring session review. Possible values are
       ``created``, ``ready to start``, ``started``, ``timed out``,
       ``completed``, ``submitted``, ``second review required``, ``verified``,
       ``rejected``, and ``error``. For an explanation of each status, see the
       table below.


The following table describes the possible values in the Status column.

.. list-table::
   :widths: 30 55
   :header-rows: 1

   * - Value in the Status column
     - Description
   * - Created
     - The exam attempt record has been created, but the exam has not yet been
       started.
   * - Ready to Start
     - The exam attempt record has been created. The learner still needs to
       start the exam.
   * - Started
     - The learner has started the proctored exam.
   * - Timed Out
     - The proctored exam has timed out.
   * - Completed
     - The learner has completed the proctored exam.
   * - Submitted
     - The learner has completed the proctored exam and results have been
       submitted for review.
   * - Second Review Required
     - The exam attempt has been reviewed and the review team has
       determined that it requires additional evaluation. The review team will
       perform the second review. Course teams do not need to take any action.
   * - Satisfactory
     - The proctoring session review has been completed, and has passed.
   * - Unsatisfactory
     - The proctoring session review has been completed, and has not passed.
   * - Error
     - The exam is believed to be in error.
