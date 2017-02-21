.. _Accessing ORA Assignment Information:

######################################
Accessing Metrics for ORA Assignments
######################################

After you release an open response assessment assignment, you can access
various metrics for the assignment. For example, you can view the number of
learners in each step of the assignment or in possible states such as
"Waiting" or "Completed" within the assignment. In addition to viewing metrics
for the assignment, you can also access assignment details for an individual
learner, or :ref:`generate a report <Generate ORA Report>` containing learner
and response details for ORA assignments in the course.

For information about tasks that you can perform on learner responses in an
ORA assignment, including :ref:`performing a grade override
assessment<Override a learner assessment grade>` or :ref:`cancelling a
learner's submission<Remove a learner response from peer grading>`, see
:ref:`Managing ORA Assignments`.


.. _PA View Metrics for Individual Steps:

************************************************
View ORA Assignment Statistics
************************************************

To view metrics about learners in the assignment, including the number who
are active in each step, follow these steps.

#. Open the ORA assignment in the course.

#. Scroll to the bottom of the assignment and select **View Assignment
   Statistics**.

   You see statistics for the assignment, including the total number of
   responses and the location ID for the assignment.

   In the **Learner Progress** section, for each assessment step in the
   assignment, you can see the number of learners who are currently working
   through (but who have not completed) that step. Only assessment types that
   exist in the assignment are included.

   .. note:: If a Staff Assessment step exists in the assignment, this step
      will always show 0 active learners, because no learner actions are
      required for that step.

   In addition to learners who are active in the assessment steps of the
   assignment, you can see the number of learners who are in the following
   states in the assignment.

     * **Waiting**: Learners who have finished the requirements for a step
       and are waiting for their responses to be assessed by peers or staff.

     * **Done**: Learners who have completed all of their required steps, and
       have received the required number of reviews.

     * **Cancelled**: Learners who have had their responses cancelled.

In the **Dates** section below **Learner Progress**, the release and due dates
for each step in the assignment are shown.

.. image:: ../../../../shared/images/ORA_AssignmentStats.png
   :width: 500
   :alt: The View Assignment Statistics page shows the number of active learners in each step, the number of learners in the Waiting, Done, and Cancelled states, and the start and due dates for each step.


.. _Generate ORA Report:

************************************************
Generate a Report for ORA Assignments
************************************************

To generate a report containing details of the ORA assignments in the course,
follow these steps.

#. View the live version of your course.

#. Select **Instructor**, and then select **Data Download**.

#. In the **Reports** section, select **Generate ORA Data Report**.

   A status message indicates that the ORA data report is being generated. This process might take some time to complete, but you can
   navigate away from this page and do other work while it runs.

   To check the progress of the report generation, reload the page in your
   browser and scroll down to the **Pending Tasks** section. The table shows
   the status of active tasks.

   When the report is complete, a linked .csv file name becomes available above
   the **Pending Tasks** section. File names are in the format
   ``{course_id}_ORA_data_{datetime}.csv``. The most recently generated
   reports appear at the top of the list.

#. To open or save the generated ORA data report, locate and select the link
   for the grade report you requested.

   You can open .csv files in a spreadsheet application to sort, graph, and
   compare data.


.. _Interpret ORA Data Report:

====================================
Interpret the ORA Data Report
====================================

The ORA data report for your course is a time-stamped .csv file that contains
data for all the ORA assignments in your course. For each ORA assignment in
the course, the report provides information that includes each learner's
anonymized ID, response, assessments details and scores, and the final score
for the assignment. For more details about each column in the report, see the
following descriptions.


.. image:: ../../../../shared/images/ORA_Data_Report_Example.png
   :alt: An example ORA data report shown in Excel.


The .csv file contains one row of data for each response from a learner.

* The IDs in the **Submission ID** and **Item ID** columns uniquely identify the
  problem within the course content and the learner's submission for that
  problem.

* The **Anonymized Student ID** column lists an ID for each learner without
  revealing confidential, personally identifiable data such as email addresses
  and usernames.

* The **Date/Time Response Submitted** column displays the date and time that the
  learner submitted her response, in YYYY-MM-DD HH-MM-SS format.

* The **Response** column displays the content of the learner's response.

* The **Assessment Details** column displays the following details for the
  assessments that were performed on the response.

  * The time and date that the assessment was submitted.
  * The type of assessment: self (SE), peer (PE), staff (ST).
  * The ID of the person who performed the assessment.
  * Any text comments about the response that were included in the assessment.

* The **Assessment Scores** column lists the scores that the response received
  in self, peer, or staff assessments.

* The **Date/Time Final Score Given**, **Final Score Points Earned**, and the
  **Final Score Points Possible** columns provide details of the final score
  that the response received. If a response has not received enough
  assessments for the assignment to be considered complete, these columns show
  a value of "None".

* The **Feedback Statements Selected** and **Feedback on Peer Assessments**
  columns together show the information that learners provided in the **Provide
  Feedback on Peer Assessments** section of their ORA assignments. This section
  is available to learners only when all assessments for an assignment have been
  completed, and provides an optional way for learners to comment on their
  experience of the peer assessment process.

  The **Feedback Statements Selected** column displays the text of the
  feedback statements (if any) that the learner selected to describe their
  experience of the peer assessment process. Learners can select either "These
  assessments were useful" or "These assessments were not useful". They can
  also select either or both of "I disagree with one or more of the peer
  assessments of my response" and "Some comments I received were
  inappropriate".

  If a learner also provided a free-form comment in the text field below the
  selectable feedback statements, the text appears in the **Feedback on Peer
  Assessments** column.
