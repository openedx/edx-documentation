.. _Enable Timed Exams:

#############################
Enabling Timed Exams
#############################

This topic describes how to enable the timed exams feature in your instance of
Open edX.

.. contents::
   :local:
   :depth: 1

*********
Overview
*********

Course teams can configure course subsections to limit the amount of time that
learners have to complete problems in that subsection.

To use this feature on your instance of Open edX, you must enable the timed
exams feature in Studio and the Learning Management System.

For information about how course teams set up timed exams, see the
:ref:`Timed Exams` topic in *Building and Running an Open edX
Course*. For information about the learner experience, see
:ref:`openlearners:taking_timed_exams` in the  *Open edX Learner's Guide*.

.. Note::
  Before proceeding, review :ref:`Guidelines for Updating the Open edX
  Platform`.

*************************************************************************
Enable Timed Exams in Studio and the Learning Management System
*************************************************************************

To enable timed exams, you modify the ``lms.yml`` and
``studio.yml`` files, which are located one level above the ``edx-platform``
directory.

#. Set the value of ``ENABLE_SPECIAL_EXAMS`` in the
   ``lms.yml`` and ``studio.yml`` files to ``true``.

   .. code-block:: none

       # Timed exams feature flag
       'ENABLE_SPECIAL_EXAMS': true,

#. Save the  ``lms.yml`` and ``studio.yml`` files.

#. Restart the Studio (CMS) and Learning Management System (LMS) processes so
   that your updates are loaded.

.. include:: ../../../links/links.rst
