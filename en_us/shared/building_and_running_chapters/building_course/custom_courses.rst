.. _Creating a Custom Course:

########################
Creating a Custom Course
########################

Custom Courses for edX (CCX) is an edX feature for re-using course
content. CCXs allow course staff to run some or all of
an existing course for a group of students on a new schedule. 
CCXs may only contain content from an existing course; they do 
not function as a course authoring tool. All CCX features are 
configurable in edX Learning Management System by a CCX Coach, 
a role created by a course Instructor. 

There are three roles associated with a CCX. 

-   Instructors created the existing course and have privileges to 
    create CCX Coaches.
-   CCX Coaches select content from the existing course for the CCX.
    Coaches also enroll students, set start and due dates for their
    scheduled content, and manage grading policy for the CCX.
-   Students take the CCX viewing the selected content on the 
    specified schedule.

**************************
 Enabling CCX for a Course
**************************

CCX for a course is disabled by default. It is enabled in Studio.

1. Ensure you have Studio access to the course.
#. Open the course in Studio and navigate to ``Advanced Settings``
   from the ``Settings`` menu.
#. Find the ``Enable CCX`` setting and change it to ``true``.
#. Click ``Save Changes``.

You can now add a CCX Coach.

*******************
 Adding a CCX Coach
*******************

The first step to create a CCX is for an instructor to 
create a CCX Coach in an existing course. At this time, a CCX can 
have only one coach.

1. Ensure you have Instructor access.
#. Ensure that the new CCX Coach has registered with the LMS.
#. From the **instructor** tab select **Membership**. 
#. If the CCX Coach is not already enrolled in the course, enroll
   them now.
#. In the **Administration List Management** section, select **CCX Coaches** 
   from **Select an Administrator Group**.
#. Enter the coach's username or email and select **Add CCX Coach**.

When the CCX Coach next logs into the LMS, the **CCX Coach** tab will 
be visible. The CCX Coach dashboard is not accessible by the instructor.

***************************
 Creating the Custom Course
***************************

1. Ensure that you are a CCX Coach.
#. Select the **CCX Coach** tab. 
#. From the CCX Coach Dashboard, enter the name for your CCX
   and select **Coach a new Custom Course for edX**.
#. Once your CCX is created, you will be re-directed to the 
   full CCX Coach Dashboard.

.. note:: 
    When choosing a CCX name, consider that the name should 
    distinguish your CCX from other CCXs based on the same course.

You can revisit your CCX by opening the original course and clicking 
the ``CCX Coach`` tab.

************************
 The CCX Coach Dashboard
************************

CCX Coaches don't have the same level of access and control over content 
that course instructors have, and do not have access to 
the instructor tab. The CCX Coach dashboard provides the interfaces to 
manage their CCX. The CCX Coach dashboard contains four tabs, described 
in the following sections.

============
Schedule Tab
============

The Schedule tab allows the CCX Coach to select the course content 
from the original course that the CCX will deliver. The drop-downs 
allow the coach to drill down through the course elements to select 
an item from anywhere in the content hierarchy and add those items 
in the sequence of their choice. Select **add all units** to include 
all of the source course's content. 

Each item can optionally have its own start and due dates. These dates
can be selected either before or after items are added to the CCX 
content hierarchy. Once items are added their start and due dates 
can be edited by hovering over or selecting that space on the CCX 
content hierarchy. 

All changes are temporary until **Save changes** is selected.

==============
Enrollment Tab
==============

The Enrollment tab contains controls to invite and manage the 
students for the CCX. Use **Student List Management** to add 
individual students who are already registered on the platform. 
Students added in **Batch Enrollment** will receive an email 
invitation if **Notify users by email** is selected. Students 
are automatically enrolled in the CCX when they accept their 
invitation.

=================
Student Admin Tab
=================

The Student Admin tab contains links to view the gradebook and 
download student grades.

==================
Grading Policy Tab
==================

The Grading Policy tab allows CCX Coaches to modify the grading 
policy. A CCX coach can modify the grading policy of the underlying 
course for their CCX. 

.. note:: 
    Only attempt this if you are confident that you understand 
    how your changes will affect grading. Modifying the grading
    policy can make your CCX unusable.

The grading policy is in JSON format. Verify that it is well-formed 
before selecting **Save Grading Policy**.

*********************
System Administrators
*********************

=====================
What does CCX change?
=====================

CCX makes a number of changes to the edX platform. It is 
outside the scope of this document to describe them in detail, 
but here are a few of the most important.

- CCX exists only in LMS. There is no Studio configuration. 
- CCX makes no changes to the course XML(OLX).
- Once enabled, CCX is available for all courses. 

=======================
System Installation
=======================

Enable CCX by making this change to the edx-platform. 

1. Create or update ``/edx/app/edx_ansible/server-vars.yml`` to include
   the CCX feature flag.

.. code-block:: yaml

   EDXAPP_FEATURES:
     CUSTOM_COURSES_EDX: true

2. Run ``/edx/bin/update``

.. code-block:: bash

   sudo /edx/bin/update edx-platform <your-branch-name>

You can now start lms and use CCX. 

