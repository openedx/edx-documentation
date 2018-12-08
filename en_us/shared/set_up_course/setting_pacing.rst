.. _Setting Course Pacing:

######################
Setting Course Pacing
######################

This topic describes how to set your course to follow a typical schedule or to
be a self-paced course.

.. contents::
  :local:
  :depth: 1

***************************
Overview of Course Pacing
***************************

When you create an edX course, you can set the schedule of the course,
including due dates for assignments or exams, or you can allow learners to work
at their own pace. Courses that follow a schedule that you set are known as
instructor-paced courses. Courses that allow learners to submit assignments at
any time before the course ends, without internal due dates, are known as self-
paced courses.

An indicator for the pacing for your course appears on the **Course Outline**
page. By default, courses are instructor-paced.

.. image:: ../../../shared/images/Pacing_COIndicator.png
 :width: 600
 :alt: text

.. note::
    You cannot change the course pacing after the course start date has passed.

*****************************************
Instructor-Paced and Self-Paced Courses
*****************************************

Instructor-paced courses progress at the pace that the course author sets. You
set release dates for content and due dates for assignments, and assignment due
dates are visible in the LMS. Learners cannot access course content before its
release date, and learners must complete assignments by their due dates.

In self-paced courses, learners can access all course materials when the course
begins, and assignments do not have due dates. You do not have the option to
set release dates for course content or due dates for assignments. Due dates do
not appear in the LMS.

.. image:: ../../../shared/images/Pacing_SubSettings.png
 :width: 500
 :alt: Side-by-side comparison of subsection settings for instructor-led and
     self-paced courses, showing release and due date options for the
     instructor-led course.

.. note::
    If you set due dates for assignments or exams and later change the course
    to be self-paced, Studio stores the due dates that you have set. If you
    change the course back to instructor-paced later, Studio restores the due
    dates.

.. only:: Partners

  For more information about the way learners experience instructor-paced and
  self-paced courses, see :ref:`learners:SFD Self Paced`.

.. only:: Open_edX

  For more information about the way learners experience instructor-paced and
  self-paced courses, see :ref:`openlearners:SFD Self Paced`.

***************************
Set Pacing for Your Course
***************************


.. only:: Open_edX

    Before you can use this feature to set up a self-paced course, it must be enabled using the Open edX Django admin panel.
    Follow these steps, or contact your Open edX site administrator for assistance.

    #. Log in to your Open edX Django Admin panel.
    #. In the **Self_Paced** section, locate **Self paced configurations** and then select **Add**.
    #. Check the **Enabled** and **Enable course home page improvements** checkboxes.
    #. Select **Save**.


.. note::
 You cannot change the course pacing after the course start date has passed.

To set the pacing for your course, follow these steps.

#. On the **Settings** menu, select **Schedule & Details**.
#. Scroll down to the **Course Pacing** section.
#. Under **Course Pacing**, select either **Instructor-Paced** or
   **Self-Paced**.
