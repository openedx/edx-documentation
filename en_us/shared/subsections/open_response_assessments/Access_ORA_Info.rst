.. _Accessing ORA Assignment Information:

##########################################
Accessing Assignment and Student Metrics
##########################################

After your open response assessment assignment has been released, you can access
information about the number of students in each step of the assignment or the
performance of individual students. This information is available in the
**Course Staff Information** section at the end of each assignment. To access
it, open the assignment in the courseware, scroll to the bottom of the
assignment, and then click the black **Course Staff Information** banner.

.. image:: ../../../../shared/building_and_running_chapters/Images/PA_CourseStaffInfo_Collapsed.png
   :alt: The Course Staff Information banner at the bottom of the peer assessment

.. _PA View Metrics for Individual Steps:

************************************************
View Metrics for Individual Steps
************************************************

You can check the number of students who have completed, or are currently
working through, the following steps:

* Submitted responses.
* Completed peer assessments.
* Waiting to assess responses or receive grades.
* Completed self assessments.
* Completed the entire assignment. 

To find this information, open the assignment in the courseware, scroll to the bottom of the assignment, and then click **Course Staff Information**.

The **Course Staff Information** section expands, and you can see the number of students who are currently working through (but have not completed) each step of the problem.

.. image:: ../../../../shared/building_and_running_chapters/Images/PA_CourseStaffInfo_Expanded.png
   :alt: The Course Staff Information box expanded, showing problem status

.. _Access Information for a Specific Student:

***********************************************
Access Information for a Specific Student
***********************************************

You can access information about an individual student's performance on a peer assessment assignment, including:

* The student's response. 
* The peer assessments that other students performed on the student's response, including feedback on individual criteria and on the overall response.
* The peer assessments that the student performed on other students' responses, including feedback on individual criteria and on the overall responses.
* The student's self assessment.

In the following example, you can see the student's response. The response received one peer assessment, and the student completed a peer assessment on one other student's response. The student also completed a self assessment.

.. image:: ../../../../shared/building_and_running_chapters/Images/PA_SpecificStudent.png
   :width: 500
   :alt: Report showing information about a student's response

For an example that shows a student's response with more assessments, see :ref:`Access Student Information`.

Accessing information about a specific student has two steps:

#. Determine the student's course-specific anonymized ID.
#. Access information for that student.

=====================================================
Determine the Student's Course-Specific Anonymized ID
=====================================================

To determine a student's course-specific anonymized ID, you'll need two .csv spreadsheets from the Instructor Dashboard: the grade report (**<course name>_grade_report_<datetime>.csv**) and the list of course-specific anonymized student IDs (**<course name>-anon-ids.csv**).

#. In the LMS, click the **Instructor** tab.
#. On the Instructor Dashboard, click **Data Download**.
#. On the **Data Download** page, locate the **Data Download** section, and then click **Get Student Anonymized IDs CSV**. A spreadsheet named **<course name>-anon-ids.csv** automatically downloads. Click to open the spreadsheet.
#. Scroll down to the **Reports** section, and then click **Generate Grade Report**. 

   The system automatically begins to generate the grade report. When it's finished, a link to the grade report appears in the list below **Reports Available for Download**.

   .. note:: Generating a grade report for a large class may take several hours.

5. When the link to the grade report appears in the **Reports Available for Download** list, click the link to open the spreadsheet.
#. When you have both spreadsheets open, view the **<course name>_grade_report_<datetime>.csv** spreadsheet. Locate the student that you want by username or e-mail address. Make a note of the number in the ID column (column A) for that student. In the following example, the student ID for e-mail address ``amydorrit@example.com`` (username ``lildorrit``) is ``18557``.

   .. image:: ../../../../shared/building_and_running_chapters/Images/PA_grade_report.png
      :width: 500
      :alt: Spreadsheet listing enrolled students and grades

7. Go to the **<course name>-anon-ids.csv** spreadsheet, locate the user ID that you noted in step 6, and then copy the value in the "Course Specific Anonymized user ID" column (**column C**) for the user. The value in column C is the student's anonymized user ID for the course. In the following example, the anonymized user ID for student ID ``18557`` is ``ofouw6265242gedud8w82g16qshsid87``.

   .. image:: ../../../../shared/building_and_running_chapters/Images/PA_anon_ids.png
      :width: 500
      :alt: Spreadsheet listing students' anonymous user IDs

   .. note:: Make sure that you don't copy the value in column B. You need the *course-specific* anonymized user ID from **column C**.

.. _Access Student Information:

=======================================
Access the Student's Information
=======================================

#. In the LMS, go to the peer assessment assignment that you want to see.
#. Scroll to the bottom of the problem, and then click the black **Course Staff Information** banner.
#. Scroll down to the **Get Student Info** box, paste the student's course-specific anonymized user ID in the box, and then click **Submit**.

The student's information appears below the **Get Student Info** box.

The following example shows:

* The student's response. 
* The two peer assessments for the response.
* The two peer assessments the student completed.
* The student's self assessment.

For a larger view, click the image so that it opens by itself in the browser window, and then click anywhere on the image that opens.

.. image:: ../../../../shared/building_and_running_chapters/Images/PA_SpecificStudent_long.png
   :width: 250
   :alt: Report showing information about a student's response