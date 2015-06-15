.. _Creating a Custom Course:

########################
Creating a Custom Course
########################

This topic describes custom courses on the edX platform (CCX).

.. contents:: Section Contents
  :local:
  :depth: 1

**************************
Overview
**************************

You can create a custom course in the edX platform (CCX) to reuse course
content. By using a CCX, you can run some or all of an existing course for a
group of students on a new schedule.

A CCX can contain only content from an existing course; you cannot author new
content in a CCX. 

**************************
Custom Courses and Roles
**************************

There are three roles involved in creating and running a CCX. 

* **Instructors** create the existing course and have privileges to create CCX
  Coaches for their course.

* **CCX Coaches** select content from the existing course for the CCX. CCX
  Coaches also enroll learners, set start and due dates for their scheduled
  content, and manage grading policy for the CCX.

* **Learners** take the CCX and view the selected content on the specified
  schedule.

************************************************
Enable Custom Courses for an Existing Course
************************************************

CCX for a course is disabled by default.

You enable CCX in Studio. Ensure you have access to the course in Studio, then
complete the following steps.

#. In Studio, from the **Settings** menu, select **Advanced Settings**.

#. Find the ``Enable CCX`` key and change the value to ``true``.

#. Click ``Save Changes``.

You can now add a CCX Coach.

*******************
Add a CCX Coach
*******************

The first step to create a CCX is to create a CCX Coach in an existing course.
A CCX can have only one XXC coach.

You add a CCX coach through the Instructor Dashboard in the LMS. Ensure you
have Instructor access to the course.

In addition, ensure that the new CCX coach has registered in the LMS and
enrolled in the course.

#. In the LMS, from the **Instructor** tab select **Membership**. 

#. In the **Administration List Management** section, from **Select an
   Administrator Group**, select **CCX Coaches**.

#. Enter the CCX coach's username or email address and select **Add CCX
   Coach**.

When the CCX Coach next logs into the LMS, the **CCX Coach** tab will 
be visible. The CCX Coach dashboard is not accessible by the instructor.

***************************
 Create the Custom Course
***************************

When you have been made the CCX coach for a course, you can then access the
course and create a CCX.

#. In the LMS, select the **CCX Coach** tab. 

#. From the CCX Coach Dashboard, enter the name for your CCX, then select
   **Coach a new Custom Course for edX**.

#. When the CCX is created, you are re-directed to the full CCX Coach
   Dashboard.

.. note:: 
    When entering a CCX name, consider that the name should 
    distinguish your CCX from other CCXs based on the same course.

You can revisit your CCX by opening the original course and selecting 
the ``CCX Coach`` tab.

************************
 The CCX Coach Dashboard
************************

The CCX Coach Dashboard provides the tools for you to manage the CCX. The CCX
Coach Dashboard contains four tabs, described in the following sections.

.. note::
  CCX Coaches don't have the same level of access and control over content that
  course instructors have, and do not have access to the Instructor Dashboard.

============
Schedule Tab
============

On the **Schedule** tab, you select the course content from the original course
that is to be included in the CCX.

Use the drop-down lists to drill down through the course content and
select an items from the content hierarchy. You then add those items in
the order needed.

Select **add all units** to include all of the source course's content.

You can configure each unit to have its own start and due dates. You can select
these before or after you add the unit to the CCX . After units are added, you
can edit their start and due dates by hovering over or selecting that space on
the CCX content hierarchy.

Select **Save changes** to save the content you configured.

==============
Enrollment Tab
==============

The **Enrollment** tab contains controls to invite and manage learners. Select
**Student List Management** to add individual students who are already
registered on the platform.

To have students added in through Batch Enrollment receive an email invitation
to the CCX, select **Notify users by email**.  Students are automatically
enrolled in the CCX when they access the invitation.

=================
Student Admin Tab
=================

You use the **Student Admin** tab to view the gradebook and download student
grades.

==================
Grading Policy Tab
==================

Use the **Grading Policy** tab to modify the grading policy for the CCX.

A CCX coach can modify the grading policy of the underlying 
course for their CCX. 

.. note:: 
    As a CCX coach, you can modify the grading policy of the original course on
    which the CCX was based. Only attempt this if you are confident that you
    understand how your changes will affect grading. Modifying the grading
    policy can make your CCX unusable.

The grading policy is in JSON format. Verify that it is well-formed 
before selecting **Save Grading Policy**.
