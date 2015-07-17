####################################
Open edX Birch Release
####################################

This page lists the highlights of the Birch release.

.. note::
 With the :ref:`Open edX Cypress Release`, the Birch release is no longer
 supported. This page remains in these release notes as a record of when new
 features were included in Open edX.

.. contents::
 :depth: 1
 :local:

************************
Split Mongo Modulestore
************************

The edX Platform now supports the **split mongo** modulestore for course data
storage. Split mongo refers to the separation of identity, structure, and
content, and it enables you to use more advanced capabilities in developing and
managing courses. For more information, see the `Open edX Developer's Guide`_.

************************************
Cohorts for Discussions and Content
************************************

You can now define smaller communities of students within the larger, course-
wide community. Learners in a cohort can have private discussions. In addition,
you can create different course experiences, including presenting different
content, for students in different cohorts.

For more information, see `Including Student Cohorts`_ in the *Building and
Running an Open edX Course* guide.

*****************************************
Content Libraries and Randomized Content 
*****************************************

You can now create a content library that contains a pool of components that
can be used in randomized assignments.

For more information, see `Working with Content Libraries`_ in the *Building
and Running an Open edX Course* guide.

********************
Prerequisite Courses
********************

You can now require that students pass a specific course before they enroll in
your course.

For more information, see `Specify Prerequisite Courses`_ in the *Building and
Running an Open edX Course* guide.

********************
Entrance Exams
********************

You can now require that students pass an entrance exam before they access your course materials.

For more information, see `Require an Entrance Exam`_ in the *Building and
Running an Open edX Course* guide.

******************** 
Student Notes
********************

A learner can highlight text and make notes while progressing through a course.
The learner can then review his notes in the body of the course or on a
separate Notes tab.

For more information, see `Student Notes Tool`_ in the *Building and
Running an Open edX Course* guide.

********************
Course Reruns
********************

You can create a new course easily by re-running an existing course. When you
re-run a course, most, but not all, of the original course content is
copied into the new course. 

For more information, see `Rerunning a Course`_ in the *Building and
Running an Open edX Course* guide.

*******************************************
Google Calendar and Google Drive Components
*******************************************

You can embed Google calendars and Google Drive files in your course. Learners
see the calendar or file directly in the courseware. Learners can also interact
with Google Forms files, completing forms or surveys.

For more information, see `Google Calendar Tool`_ and `Google Drive Files
Tool`_ in the *Building and Running an Open edX Course* guide.
 
************************************************** 
Support for Graded Problems in Content Experiments
**************************************************

Content experiments can now include graded problems.

********** 
REST APIs
**********

EdX has built and published documentation for the first versions of several
REST APIs: 

* `Mobile API`_
* `Enrollment API`_
* `Open edX Data Analytics API`_


************** 
Other Changes
**************

In addition to the new features listed above, the Birch release includes many
small changes and bug fixes. See the `edX Release Notes`_ for changes listed
after the Aspen release.

.. include:: links.rst
