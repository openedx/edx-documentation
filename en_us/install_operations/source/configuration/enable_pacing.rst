.. _Enable Self Paced Courses:

#############################
Enabling Self-Paced Courses
#############################

This topic describes how to enable the self-paced courses feature in your
instance of Open edX.

.. contents::
   :local:
   :depth: 1

*********
Overview
*********

By default, courses are instructor-paced. These courses run on a schedule,
typically four to eight weeks, with new content released each week and set
assignment due dates. You can configure your instance of Open edX so that it
enables self-paced courses. A self-paced course releases content all at once
and is available to complete for three to twelve months after the start date.
In a self-paced course, there are no due dates other than the course end date.

To enable self-paced courses on your instance of Open edX, you must enable the
self-paced course feature in the Learning Management System. Then, course
teams are able to set up a course as either instructor-paced or self-paced in
Studio.

For information about how course teams set course pacing, see the
:ref:`Set Schedule and Pacing` topic in the
*Building and Running an Open edX Course* guide.

.. Note::
  Before proceeding, review :ref:`Guidelines for Updating the Open edX
  Platform`.

*************************************************************************
Enable Self-Paced Courses in the Learning Management System
*************************************************************************

To enable self-paced courses, follow these steps to edit the configurations,
using the Django administration console for your Open edX LMS.

    #. Log in to the Django administration console for the LMS.
    #. In the **Self_Paced** section, locate **Self paced configurations**, and
       then select **Add**.
    #. Select the **Enabled** and **Enable course home page improvements**
       checkboxes.
    #. Select **Save**.

.. include:: ../../../links/links.rst
