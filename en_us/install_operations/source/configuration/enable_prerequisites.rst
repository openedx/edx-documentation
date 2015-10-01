.. _Enable Course Prerequisites:

#############################
Enabling Course Prerequisites
#############################

This section describes how to enable course prerequisites in your instance of
Open edX.

.. contents::
   :local:
   :depth: 1

*********
Overview
*********

Course teams can set prerequisites for a course. Learners must complete the
prerequisite courses before participating in the course.

To use this feature on your instance of Open edX, you must configure the
Milestones application, then enable prerequisites in Studio and the Learning
Management System.

For information about prerequisites, see the *Building and Running an
Open edX Course* and *Open edX Learner's* guides.

.. Note::
  Before proceeding, review :ref:`Guidelines for Updating the edX Platform`.

.. include:: configure_milestone_app.rst

*************************************************************************
Enable Prerequisite Courses in Studio and the Learning Management System
*************************************************************************

#. Set the value of ``ENABLE_PREREQUISITE_COURSES`` in the
   ``/cms/envs/common.py`` and ``/lms/envs/common.py`` files to ``True``.

   .. code-block:: python

       # Prerequisite courses feature flag
       'ENABLE_PREREQUISITE_COURSES': True,

#. Save the the ``/cms/envs/common.py`` and ``/lms/envs/common.py`` files.

.. include:: ../../../links/links.rst

