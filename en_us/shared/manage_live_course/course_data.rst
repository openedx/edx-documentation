.. _Course Data:

############################
Course Data
############################

After you create a course in Studio, you can access information about it in the
LMS by selecting **Instructor** to access the instructor dashboard.

.. contents::
  :local:
  :depth: 1

*************************************************
Review Course Data
*************************************************

On the Course Info page, you can find the following information.

* Identifying information about the course.

* Whether the course has started or ended.

* The number of sections in the course.

* The defined grade cutoff for passing or failing.

To view this course data, follow these steps.

#. View the live version of your course.

#. Select **Instructor**, and then select **Course Info** if necessary.

   The **Basic Course Information** section of the page that opens lists
   information about the course.

    .. image:: ../../../shared/images/Instructor_Dash_Course_Info.png
     :alt: The basic course information section of the Instructor Dashboard.

Additional data about the course and its learners is available from other pages
in the instructor dashboard, and from Insights.

To access the data visualizations, metrics, and reports that are available in
Insights from the instructor dashboard, select the link in the banner at the
top of each page. For more information, see :ref:`insights:Using edX Insights`.

*************************************************
Sources in Studio of the Basic Course Information
*************************************************

The course data that displays on the instructor dashboard is defined in
Studio, or derived from data that you define in Studio.

* **Organization**: Specified in Studio when you create the course. Becomes
  part of the course URL, and cannot be changed.

* **Course Number**: Specified in Studio when you create the course. Becomes
  part of the course URL, and cannot be changed.

* **Course Name**: Specified in Studio when you create the course. Becomes
  part of the course URL, and cannot be changed. In Studio, this field is
  labeled **Course Run**.

* **Course Display Name**: Specified in Studio when you create the course. In
  Studio, this field is labeled **Course Name**.

  This name can be changed in Studio (not recommended if your course is live):
  From the **Settings** menu select **Advanced Settings**. The value for the
  **Course Display Name** policy key defines the course name that appears in
  the LMS only.

  The illustration that follows shows the information that you enter in Studio
  for a new course, side-by-side with the same information as it appears on the
  **Course Info** page of the instructor dashboard.

.. image:: ../../../shared/images/Course_Info_Comparison.png
   :alt: The Course Name in Studio and the Course Display Name in the LMS are
       boxed; the Course Run in Studio and the Course Name in the LMS are
       circled.

* **Course Start Date**: The date and time that the course is scheduled to
  start. This date can be changed in Studio (not recommended if your course is
  live). For more information, see :ref:`Determine Start and End Dates`.

* **Course End Date**: The date and time that the course is scheduled to end.
  This date can be changed in Studio (not recommended if your course is live).
  For more information, see :ref:`Determine Start and End Dates`.

* **Has the course started**: Derived from the **Course Start Date** value and
  the current date.

* **Has the course ended**: Derived from the **Course End Date** value and the
  current date.

* **Number of sections**: The total number of sections created for the course.
  Includes all course sections, regardless of publication status, release date,
  or other settings that affect whether learners have access to the sections.

* **Grade Cutoffs**: Specified in Studio when you define the cutoff for a
  failing grade. Learners who earn exactly the cutoff value pass the course.
  Grading can be changed in Studio (not recommended if your course is live).
  For more information, see :ref:`Set the Grade Range`.
