.. _Creating a New Course:

###########################
Creating a New Course
###########################


*******************
Overview
*******************

This chapter describes how to create and set up your course:

* :ref:`Create a New Course`
* :ref:`Edit Your Course`
* :ref:`Use the Course Checklist`
* :ref:`Add Course Team Members`

Another way to create a course is to re-run an existing course. See
:ref:`Rerun a Course`.

You can also :ref:`Export a Course` and :ref:`Import a Course` through Studio.
You can do this when you need to edit the course in XML.

.. _Edge: http://edge.edx.org
.. _edXorg: http://edx.org

.. _Create a New Course:
  
*******************
Create a New Course
*******************

#. Log in to Studio.
#. Click **New Course**.
#. Enter course information as needed and click **Create**.

  .. note::  Enter new course information carefully. This information becomes
   part of the URL for your course. To change the URL after the course is
   created, you must contact edX through the Help site
   (http://help.edge.edx.org). Additionally, because this information becomes
   part of your course URL, the total number of characters in the following
   four fields must be 65 or fewer.

  .. image:: ../../../shared/building_and_running_chapters/Images/new_course_info.png
     :alt: Image of the course creation page

  * For **Course Name**, enter the title of your course. For example, the name
    may be "Sets, Maps, and Symmetry Groups". Use title capitalization for the
    course title.

  * For **Organization**, enter the identifier for your university. For
    example, enter HarvardX or MITx. Do not include spaces or special
    characters.

.. is it ok to include the Harvard and MIT examples?

  * For **Course Number**, enter both a subject abbreviation and a number. For
    example, for public health course number 207, enter **PH207**. For math
    course 101x, enter **Math101x**. Do not include spaces or special
    characters in the course number.

    .. note:: If your course will be open to the world, be sure to include the
     "x". If it is exclusively an on-campus offering, do not include the "x".*

  * For **Course Run**, enter the term in which your course will run. For
    example, enter 2014SOND or T2_2014. Do not include spaces or special
    characters.

    The value that you enter for the run does not affect the course start date
    that you define for the course. See :ref:`Set Important Dates for Your
    Course` for more information.

4. Click **Save.**

The page refreshes to show the empty **Outline** for your new course. The course
identifier appears in the browser address bar as the final part of the URL in
the format ``{key type}:{org}+{course}+{run}``. For example,
``course-v1:edX+DemoX+Demo_2014``.

  .. note::  This course ID format applies to all courses created after January
     14, 2015. Older courses can have course IDs in the format
     ``{org}/{course}/{run}``. For example, ``MITx/6.002x/2012_Fall``.

.. _Edit Your Course:

************************
Edit Your Course
************************

After you create a course, the course opens in Studio automatically and you
can begin editing.

When you return to Studio later, the Studio **My Courses** dashboard page lists
the courses that you create along with any courses for which you have course
staff privileges.

 .. image:: ../../../shared/building_and_running_chapters/Images/open_course.png
  :alt: Image of the course on the Studio dashboard
 
To open a course, click the course name. The Studio **Course Outline** page
appears.

.. _Use the Course Checklist:

************************
Use the Course Checklist
************************

You can use a Course Checklist within Studio to help you work through the tasks
of building a course.

Categories of tasks in the Course Checklist include:

* Getting Started with Studio
* Draft a Rough Course Outline
* Explore edX's Support Tools
* Draft Your Course About Page

From the **Tools** menu, select **Checklists**.

 .. image:: ../../../shared/building_and_running_chapters/Images/checklist.png
  :alt: Image of the course checklist
 

As shown above for the **Add Course Team Members** task, if you hover over a
task, a button is displayed that takes you to the page to complete that task.

You can expand and collapse sections of this page as needed.

You can check tasks as you complete them. Studio saves your changes
automatically. Other course staff can see your changes.

.. _Add Course Team Members:

************************
Add Course Team Members
************************

Course team members are users who help you build your course. Before you can
assign Staff or Admin access to a team member:

* You must be an Admin.

* The team member that you want to add must register a user account and
  activate the account.

* You need the same, registered email address for the team member you want to
  add.

Other course team members can edit the course and perform all tasks except
adding and removing other new team members and granting Admin access.

.. note::  Any course team member can delete content created by other team
 members.

All course team members must be registered with Studio and have an active
account.

To add a course team member:

#. Ensure you have Admin access.
#. Ensure that the new team member has registered with Studio.
#. From the **Settings** menu, select **Course Team**.
#. Click **Add a New Team Member**.
#. Enter the new team member's email address, then click **ADD USER**. 

The new team member can now work on the course in Studio. To preview
the course in the LMS or work on the Instructor Dashboard, the team member
must enroll in the course.

You can also assign privileged roles to users when you work in the LMS.

.. note:: The LMS "Course Staff" role is the same as the Studio "Staff" role, 
 and the LMS "Instructors" role is the same as the Studio "Admin" role.

Regardless of where the role is assigned, these administrative team members
can work on your course in both Studio and the LMS (after enrollment). For
more information about assigning roles while you run your course, see
:ref:`Course_Staffing`.

You can also designate teams of people to beta test your course and to
moderate and manage its discussions by assigning other LMS roles. The beta
testers and discussion administrators must be enrolled in your course, but
they do not need to have Staff or Admin access. For more information, see
:ref:`Beta_Testing` and :ref:`Assigning_discussion_roles`.

