.. _StaffGraded:

#######################
Staff Graded Assignment
#######################

.. note:: EdX offers provisional support for this tool.

Staff Graded Assignment allows you to assign scores to learners for off-platform activities
or participation, at the assessment level. It provides a text component with instructions
to learners, and a way for you to assign grades.


***************************************
Enable Staff Assignment
***************************************

Before you can add staff graded assignments to your course, you must enable staff graded
assignments in Studio.

To enable staff graded assignments in Studio, you add the ``"edx_sga"`` key to the
**Advanced Module List** on the **Advanced Settings** page. (Be sure to include the
quotation marks around the key value.) For more information, see
:ref:`Enable Additional Exercises and Tools`.

***************************************
Create a Staff Graded Assignment
***************************************

#. Under **Add New Component** select **Advanced** and then select **Staff Graded Assignment**

#. Edit the newly created block, specify **Display Name** and **Maximum Score**

#. After learners complete the assignment you're grading, Grade Learners **(see below.)**



.. _StaffGraded Settings:

=================================
Staff Graded Assignment Settings
=================================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``Display Name`` (optional)
     - The display name for this component.
   * - ``Problem Weight`` (optional)
     - Enter the number of points possible for this component. The default value is 1.0.



.. _StaffGraded Grading:

================
Grading Learners
================

While your course is running, after learners have had a chance to complete the off-platform assignment you’re grading, you can assign learner grades from the LMS Instructor view of the component as follows:

#. **Export scores.** Download a grading CSV and use this as a template to assign scores for this problem. You can use track/cohort filters to limit to grading only a subset of learners. 

#. **(On your own machine) Fill out grades.** Open the CSV in a spreadsheet editor and assign scores to learners via “New Points” field. Leave scores that you don’t want to change blank.

#. **Import scores** Uploading the filled out CSV. Learners will immediately see their grades after import completes. Supports smaller courses - i.e. file sizes up to 4MB. *Note: [Provisionally supported: usage in large courses] To use in larger courses, break up your grade file CSV by rows, and import in separate files -- or use the track & cohort filters to limit to a subset of rows. In this case, keep the header row for each file. This manual approach for larger courses is error prone, so we are making it available as a use-at-your-own-risk feature for advanced users, but don’t explicitly support it.*

#. **Review result** File is uploaded, validated, scores are overwritten for non-blank rows. You’ll get a readout at the bottom of the screen. 

