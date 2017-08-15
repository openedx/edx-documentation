.. _Enabling and Configuring Cohorts:

############################################
Enabling and Configuring the Cohorts Feature
############################################

This section provides information about setting up cohorts in your course.

.. contents::
  :local:
  :depth: 1

*********
Overview
*********

To use cohorts in your course, you must select a strategy for assigning
your learners to cohorts: automated assignment, manual assignment, or a hybrid
approach. For more information, see :ref:`Options for Assigning Learners to
Cohorts`.

.. note:: Although you can change the assignment method for cohorts at any
  time, you should have a strategy in mind as you design your course, and only
  make changes to cohorts while the course is running if absolutely necessary.

You must also decide whether course-wide and content-specific discussion topics
should be divided by cohort or unified for all learners.

After you decide on a cohort strategy for your course, complete these
configuration steps (as applicable).

#. :ref:`Enable cohorts<Enable Cohorts>`.

#. Determine the method you want to use to assign learners to cohorts.

  * :ref:`Implement an automated assignment strategy<Implementing the Automated
    Assignment Strategy>`

  * :ref:`Implement a manual assignment strategy<Implementing the Manual
    Assignment Strategy>` and :ref:`manually assign enrolled learners <Assign
    Learners to Cohorts Manually>` to the cohorts that you create

  * :ref:`Use a combination of automated and manual assignment<Hybrid
    Assignment>`

3. Optionally, identify the discussion topics that you want to be divided by
   cohort.

   For information about divided discussions, see :ref:`About Divided
   Discussions`.

You complete these procedures on the **Cohorts** and **Discussions** tabs on
the Instructor Dashboard.

.. note:: On the **Cohorts** tab, the number of learners shown next to each
   cohort name in the **Select a cohort** list includes only learners who are
   enrolled in the course. The number does not include preassigned learners
   who either do not yet have an edX account or are not enrolled in your
   course.

For an optimal learner experience, you should make sure that configuration of
the cohort feature is as complete as possible before the start date of your
course. If you need to make changes to the way you have configured cohorts
while your course is running, be aware of the implications of your changes. For
more information, see :ref:`Altering Cohort Configuration`.

.. _Implementing the Automated Assignment Strategy:

***************************************************
Implementing an Automated Assignment Strategy
***************************************************

To implement an automated assignment strategy of learners to cohorts, you
:ref:`enable the cohort feature<Enable Cohorts>` for your course, and
:ref:`create cohorts<Add Cohorts>` that have the **Automatic**
:ref:`assignment method<Changing the Assignment Method of a Cohort>`. To add
learners to these cohorts, you do not need to take any action: the system
automatically and randomly assigns learners to the available automatic cohorts
when they first access any course content or divided discussions. Learners who
access the **Course** page or other course pages such as a **Textbook** page
do not receive a cohort assignment until they view course content or divided
discussions.

.. note:: You can :ref:`add learners manually<Assign Learners to Cohorts Manually>`
    to any cohort, whether it was created as an automated cohort or a
    manual cohort.

For a scenario using an automated assignment strategy, see :ref:`All Automated
Assignment`. For a scenario using a combination of automated and manual
assignment to cohorts, see :ref:`Hybrid Assignment`.

.. _About Auto Cohorts:

=================
Automated Cohorts
=================

The first time a learner views course content on the **Course** or
**Discussion** page, if she is not already assigned to a cohort, she is
randomly assigned to one of the automated cohorts. If no automated cohorts
exist, the system creates a :ref:`default cohort <Default Cohort Group>` and
assigns the learner to this cohort.

.. note:: The default cohort is created to ensure that every learner is
   assigned to a cohort. To avoid having to re-assign learners from the default
   cohort to other cohorts, make sure you create the automated cohorts that you
   want before the course starts.

.. _Implementing the Manual Assignment Strategy:

***************************************************
Implementing a Manual Assignment Strategy
***************************************************

To implement a manual assignment strategy of learners to cohorts, you
:ref:`enable the cohort feature<Enable Cohorts>` for your course, and
:ref:`create cohorts<Add Cohorts>` that have the **Manual** :ref:`assignment
method<Changing the Assignment Method of a Cohort>`. Then, you manually assign
enrolled learners to the appropriate cohorts.

.. note:: It is not a requirement that learners have enrolled in your course
   or registered on edx.org for you to add them to a cohort. For learners who
   have not yet created an edx.org account, you must provide a valid email
   address. For learners who have an edx.org account but have not yet enrolled
   in your course, you can provide either a valid email address or a
   recognized edx.org username.

Manual assignments should be as complete as possible before your course starts.
If learners enroll after your course starts, you should assign new learners to
cohorts as soon as possible. If you need to make changes to the way you have
configured cohorts while your course is running, see :ref:`Altering Cohort
Configuration`.

For a scenario using a manual assignment strategy, see :ref:`All Manual
Assignment`. For a scenario using a combination of automated and manual
assignment to cohorts, see :ref:`Hybrid Assignment`.

.. _Enable Cohorts:

*********************************
Enabling Cohorts in your Course
*********************************

To enable cohorts in your course, follow these steps.

#. In the LMS, select **Instructor**, then select **Cohorts**.

#. Select **Enable Cohorts**.

You can now :ref:`add cohorts<Add Cohorts>` to your course.

.. warning:: Be very careful in deciding to enable the cohort feature in a live
   course, because doing so affects the course experience for learners.
   Learners might no longer have access to course and discussion topics
   that were previously visible to them.

   If you must make changes to cohort configuration while your course is
   running, be sure you understand the consequences of doing so. For details,
   see :ref:`Altering Cohort Configuration`.

.. _Add Cohorts:

****************
Adding Cohorts
****************

After you enable the cohorts feature for your course, you can add cohorts. To
add a cohort to your course, follow these steps.

#. In the LMS, select **Instructor**, then select **Cohorts**.

#. Click **Add Cohort**.

#. Enter a name for the cohort.

   .. note::
    Learners can see the name of the cohort they are assigned to. The message
    "This post is visible only to {cohort name}" appears with each post in
    discussion topics that are divided by cohort. See :ref:`Read the Group
    Indicator in Posts`.

#. Specify whether learners are automatically or manually assigned to this
   cohort.

#. Optionally, select **Select a Content Group** to associate the cohort with a
   :ref:`content group<About Content Groups>`. For information about creating
   cohort-specific course content by associating cohorts with content groups,
   see :ref:`Cohorted Courseware Overview`.

#. Select **Save**.

Continue implementing your cohort strategy by creating additional cohorts as
applicable, and specifying the assignment method for each cohort.

.. note:: By the time your course starts, you must have at least one cohort in
   your course that is automatically assigned. If you have not created at
   least one automated assignment cohort in the course by the time that the
   first learner accesses your course content or a divided discussion topic,
   edX creates a default cohort to which learners are automatically assigned.

For details about adding learners to a cohort by uploading a .csv file, see
:ref:`Assign Learners to Cohort Groups by uploading CSV`.

For a report that includes the cohort assignment for every enrolled
learner, review the learner profile information for your course. See
:ref:`View and download student data`.

.. note:: You cannot delete cohorts, but you can change their names or the way
   in which learners are assigned to them. If you need to make changes to the
   way you have configured cohorts while your course is running, see
   :ref:`Altering Cohort Configuration`.

.. _Assign Learners to Cohorts Manually:

***********************************
Assign Learners to Cohorts Manually
***********************************

If you have implemented a manual assignment strategy for cohorts in your
course, make sure your manual assignments are as complete as possible before
your course starts. If learners enroll after your course starts, you should
assign new learners to cohorts as soon as possible.

.. note:: Making changes to cohort assignments after the course starts can
   affect the course experience for learners. Learners might no longer have
   access to course and discussion topics that were previously visible to
   them. For more information, see :ref:`Altering Cohort Configuration`.

To manually assign learners to cohorts in your course, follow these steps.

#. View the live version of your course. For example, in Studio click **View
   Live**.

#. Select **Instructor**, then select **Cohorts**.

#. Scroll to the **Cohort Management** section at the bottom.

#. From the **Select a cohort** list, select the cohort to which you want to
   manually assign learners.

#. On the **Manage Learners** tab, under **Add learners to this cohort** enter
   the username or email address of a single learner, or enter multiple
   usernames or addresses separated by commas or new lines. You can copy data
   from a .csv file of email addresses or usernames, and paste it into this
   field.

   .. note:: It is not a requirement that learners have enrolled in your
      course or registered on edx.org for you to manually add them to a
      cohort. For learners who have not yet created an edx.org account, you
      must provide a valid email address. For learners who have an edx.org
      account but have not yet enrolled in your course, you can provide either
      a valid email address or a recognized edx.org username.

#. Select **Add Learners**.

   Learners you added who have edX accounts are assigned to the selected
   cohorts. A confirmation message indicates the number of learners who were
   successfully added to the cohort.

   Learners you added who do not yet have edX accounts are listed as
   "Preassigned" to the cohort. When preassigned learners enroll in the
   course, they are automatically added to the cohort.

   If some learners that you listed could not be added to cohorts, an error
   message lists the email addresses or usernames of learners who could not be
   added to the cohort.

.. note:: Because learners can belong to only one cohort, adding a learner to a
   cohort moves them from any cohort they were previously assigned to. The
   confirmation message indicates the number of learners who were moved from
   their previous cohort assignment as a result of your adding them to the
   current cohort.

For a report that includes cohort assignments for your course, review the
learner profile information for your course. See :ref:`View and download
student data`.


.. _Assign Learners to Cohort Groups by uploading CSV:

***************************************************
Assign Learners to Cohorts by Uploading a .csv File
***************************************************

Uploading a .csv file containing a list of learners and the cohorts that you
want to assign them to is another way of assigning learners to cohorts
manually. For details about the other manual assignment method, see
:ref:`Assign Learners to Cohorts Manually`.



Any assignments to cohorts that you specify in the .csv files you upload will
overwrite or change existing cohort assignments. The configuration of your
cohorts should be complete and stable before your course begins. You should
complete manual cohort assignments as soon as possible after any learner
enrolls, especially for enrollments that occur after your course has started.
To understand the effects of changing cohort assignments after your course has
started, see :ref:`Altering Cohort Configuration`.

.. note:: Be aware that the contents of the .csv file are processed row by
   row, from top to bottom, and each row is treated independently. If the same
   learner is assigned to different cohorts in different rows in the
   spreadsheet, the last assignment to be performed is that learner's final
   assignment.

    For example, if in your .csv file Learner A is first assigned to Cohort 1,
    then later in the spreadsheet is assigned to Cohort 2, the end result of
    your .csv upload is that Learner A is assigned to Cohort 2. However, the
    upload results file will include Learner A twice in the "Learners Added"
    count: once when they are added to Cohort 1, and again when they are added
    to Cohort 2. Before submitting a file for upload, check it carefully for
    duplicated learners and other errors.

    If the same learner is assigned to a cohort that they already belong to,
    they are not included in the count of "Learners Added".


The requirements for the .csv file are summarized in this table.

.. list-table::
    :widths: 15 30

    * - **Requirement**
      - **Notes**
    * - Valid .csv file

      - The file must be a properly formatted comma-separated values file:

        * The file extension is .csv.
        * Every row must have the same number of commas, whether or not there
          are values in each cell.

    * - File size
      - The file size of .csv files for upload is limited to a maximum of 2MB.

    * - UTF-8 encoded
      - You must save the file with UTF-8 encoding so that Unicode characters
        display correctly.

        See :ref:`Creating a Unicode Encoded CSV File`.

    * - Header row
      - You must include a header row, with column names that exactly match
        those specified in "Columns" below.

    * - One or two columns identifying learners
      - You must include at least one column identifying learners:
        either "email" or "username", or both.

        To preassign learners who do not yet have edX accounts, you must
        provide their email addresses in an "email" column.

        If both the username and an email address are provided for a learner,
        the email address has precedence. In other words, if an email address
        is present, an incorrect or unrecognized username is ignored.

    * - One column identifying the cohort
      - You must include one column named "cohort" to identify the cohort
        to which you are assigning each learner.

        The specified cohorts must already exist in Studio.

    * -
      - Columns with headings other than "email", "username" and "cohort" are
        ignored.


To manually add learners to cohorts by uploading a .csv file, follow these
steps.

.. note:: To add learners who do not yet have edX accounts to cohorts using a
   .csv file upload, you must provide their email addresses in a column with
   the heading "email". Learners without edX accounts are "preassigned" to
   cohorts; they are not included in the count of learners "added" to cohorts.

#. View the live version of your course. For example, in Studio, select **View
   Live**.

#. Select **Instructor**, then select **Cohorts**.

#. From the **Select a cohort** list, select the cohort to which you are adding
   students.

#. Select **Assign students to cohorts by uploading a CSV file**, then select
   **Browse** to navigate to the .csv file you want to upload.

#. Select **Upload File and Assign Students**. A status message is displayed
   above the **Browse** button.

#. Verify your upload results on the **Data Download** page.

   Under **Reports Available for Download**, locate the link to a .csv file
   with "cohort_results" and the date and time of your upload in the filename.
   The list of available reports is sorted chronologically, with the most
   recently generated files at the top.

The results file provides the following information:

.. list-table::
    :widths: 15 30

    * - **Column**
      - **Description**

    * - Cohort
      - The name of the cohort to which you are assigning learners.

    * - Exists
      - Whether the cohort was found in the system. TRUE/FALSE.

        If the cohort was not found (value is FALSE), no action is taken for
        learners who you assigned to that cohort in the .csv file.

    * - Learners Added
      - The number of learners added to the cohort during the row by row
        processing of the .csv file. This number does not include learners who
        are not enrolled in the course.

    * - Learners Not Found
      - A list of the usernames of learners that could not be matched and who
        were therefore not added to the cohort.

    * - Invalid Email Addresses
      - A list of email addresses that were not valid. These learners could
        not be added to the cohort.

    * - Preassigned Learners
      - The email addresses of learners who do not yet have an edX account but
        who you have preassigned to a cohort using their email addresses.
        These learners are not included in the count of "Learners Added". When
        these preassigned learners create an edX account and enroll in your
        course, they are automatically added to the cohorts that you
        preassigned them to.


For a report that includes the cohort assignment for every enrolled learner,
review the learner profile information for your course. See :ref:`View and
download student data`.


.. _Creating a Unicode Encoded CSV File:

====================================
Creating a Unicode-encoded .csv File
====================================

Make sure the .csv files that you upload are encoded as UTF-8, so that any
Unicode characters are correctly saved and displayed.

.. note:: Some spreadsheet applications (for example, MS Excel) do not allow
   you to specify encoding when you save a spreadsheet as a .csv file. To
   ensure that you are able to create a .csv file that is UTF-8 encoded, use a
   spreadsheet application such as Google Sheets, LibreOffice, or Apache
   OpenOffice.

.. _Altering Cohort Configuration:

*************************************************
Altering Cohort Configuration in a Running Course
*************************************************

The configuration of cohorts should be complete and stable before your course
begins. Manual cohort assignments should be completed as soon as possible after
any learner enrolls, including any enrollments that occur while your course is
running.

If you decide that you must alter cohort configuration after your course starts
and activity in the course discussion begins, be sure that you understand the
consequences of these actions.

* :ref:`Changing Student Cohort Assignments`
* :ref:`Renaming a Cohort`
* :ref:`Deleting a Cohort`
* :ref:`Changing the Assignment Method of a Cohort`
* :ref:`Disabling the Cohort Feature`

.. _Changing Student Cohort Assignments:

***************************************************
Change Learner Cohort Assignments
***************************************************

After your course starts and learners begin to contribute to the course
discussion, each post that they add is visible either to everyone or to the
members of a single cohort. When you change the cohort that a learner is
assigned to, there are three results.

* The learner continues to see the posts that are visible to everyone.

* The learner sees the posts that are visible to his new cohort.

* The learner no longer sees the posts that are visible only to his original
  cohort.

The visibility of a post and its responses and comments does not change, even
if the cohort assignment of its author changes. To a learner, it can seem that
posts have "disappeared".

To verify the cohort assignments for your learners, download the :ref:`student
profile report<View and download student data>` for your course. If changes are
needed, you can :ref:`assign learners<Assign Learners to Cohorts Manually>` to
different cohorts manually in the LMS by selecting **Instructor** and then
**Cohorts**, or :ref:`upload cohort assignment changes<Assign Learners to
Cohort Groups by uploading CSV>` in a .csv file.

.. _Renaming a Cohort:

***************
Rename a Cohort
***************

You can change the name of any cohort, including the system-created default
cohort.

To rename a cohort, follow these steps.

#. View the live version of your course. For example, in Studio select **View
   Live**.

#. Select **Instructor**, then select **Cohorts**.

#. From the **Select a cohort** list, select the cohort whose name you want to
   change.

#. On the **Settings** tab, in the **Cohort Name** field, enter a new name for
   the cohort.

#. Select **Save**. The name for the cohort is updated throughout the LMS and
   the course, including learner-visible views.

.. _Deleting a Cohort:

================
Delete a Cohort
================

You cannot delete cohorts. However, you can :ref:`rename a cohort<Renaming a
Cohort>`, :ref:`change its assignment method<Changing the Assignment Method of
a Cohort>`, or move learners to other cohorts.

If you decide that you must alter cohort configuration after your course starts
and learners begin viewing the course and the discussion topics, be sure that
you understand the consequences of these actions. For more details, see
:ref:`Altering Cohort Configuration`.

.. _Changing the Assignment Method of a Cohort:

******************************************
Changing the Assignment Method of a Cohort
******************************************

Although you can change the assignment method of a cohort at any time after you
create it, you should have a strategy in mind as you design your course, and
only make changes to cohorts while the course is running if absolutely
necessary. Be aware of the implications of changing cohort configuration while
your course is running. For more information, see :ref:`Options for Assigning
Learners to Cohorts` and :ref:`Altering Cohort Configuration`.

.. note:: When your course starts, you must have at least one cohort in your
   course that has automatic assignment. If you have not created at least one
   automated assignment cohort in the course by the time that the first learner
   accesses your course content, edX creates a default cohort to which learners
   are automatically assigned. If the :ref:`default group<Default Cohort
   Group>` is the only automated assignment cohort in your course, you cannot
   change its assignment method to **Manual**.

To change the assignment method of a cohort, follow these steps.

#. View the live version of your course. For example, in Studio select **View
   Live**.

#. Select **Instructor**, then select **Cohorts**.

#. From the **Select a cohort** list, select the cohort whose assignment method
   you want to change.

#. On the **Settings** tab, the current assignment method is selected. Change
   the assignment method by selecting the other option, either **Automatic** or
   **Manual**.

#. Select **Save**.

   The cohort assignment method is updated.

.. note:: Changing the cohort assignment method has no effect on learners who
   are already assigned to this and other cohorts. Learners who access the
   course after you make this change are assigned to cohorts based on the new
   assignment method of this cohort combined with the assignment methods of all
   other cohorts.

.. _Disabling the Cohort Feature:

******************************
Disable Cohorts in Your Course
******************************

.. warning:: Be very careful in deciding to disable the cohort feature if you
   previously had it enabled in a live course, because doing so affects the
   course experience for learners. Course materials and discussion posts that
   were shared only with members of particular cohorts are now visible to all
   learners in the course.

   If you must make changes to the way you have configured cohorts while your
   course is running, be sure you understand the consequences of doing so. For
   details, see :ref:`Altering Cohort Configuration`.

To disable cohorts in your course, follow these steps.

#. In the LMS, select **Instructor**, then select **Cohorts**.

#. Clear the **Enable Cohorts** option.

All course content and discussion posts that were previously divided by cohort
immediately become visible to all students.
