.. _Verified Track Cohorts:

#######################################################################
Using Cohorts to Provide Different Content to Verified Track Learners
#######################################################################

This section provides information about using :ref:`cohorts<Cohorts Overview>`
to provide :ref:`different content <Cohorted Courseware Overview>` to
learners who are in the verified track in your course, compared with learners
in the audit track.

.. note:: Using the cohorts feature in this way requires configuration by edX.
   Let your partner manager know your plans as far in advance of the course
   start as possible.

   If you want to use this feature in a course that is live, and
   verified track learners might already have enrolled, contact your edX
   partner manager to discuss configuration possibilities and how to migrate
   existing verified track learners to the correct cohort.

   In addition, you must be aware of, and follow, the :ref:`requirements
   <Requirements for Verified Track Cohorts>` for using cohorts to deliver
   differentiated content to your verified track learners.

.. note::


.. contents::
  :local:
  :depth: 1

*********
Overview
*********

You can provide differentiated content to the learners in each track using
cohorts and content groups.

.. note:: Although you provide differentiated content to learners in each
   track, the overall grading policy is the same for all learners. In other
   words, the grading policy cannot be different between your audit track and
   your verified track content. You specify differentiated content at the unit
   level in the course, therefore each track has equivalent content with the
   same weight and type per unit.

Use :ref:`cohorts <Cohorts Overview>` in your course to create groups of
learners based on the course track that they are in. Your course can have more
than one cohort for audit track learners (for example, if you want to create
smaller groups of audit track learners), but you must have only one cohort for
verified track learners.

You create two :ref:`content groups <About Content Groups>` to represent the
differentiated content that you intend for audit track learners and verified
track learners.

You :ref:`associate each cohort <Associate Cohorts with Content Groups>` with
either the verified track content group, or the audit track content group.
More than one cohort can be associated with a single content group.

Learners are assigned to cohorts in your course based on the course track that
they enroll in or upgrade to. Each learner can belong to only one cohort.

When learners enroll in your course as audit track learners, they are assigned
to any of the :ref:`automated <About Auto Cohorts>` audit track cohorts in
your course. If you have more than one automated cohort for audit
track learners, learners can be assigned to any one of them. For audit track
cohorts with manual assignment, you must :ref:`manually add them <Assign
Learners to Cohorts Manually>` to the cohort. Learners who are in cohorts
associated with the audit track content group see course content that is
intended for audit track learners.

Learners who enroll in the course as verified track learners are automatically
assigned to the verified track cohort. Learners who initially enrolled as
audit track learners but upgrade to the verified track are also automatically
moved to the verified track cohort. Learners who are in the verified track
cohort see course content that is specified as visible to the verified content
group.

.. Important:: There are several requirements if you use cohorts to provide
   differentiated content to verified track learners.

   * You must have at least one cohort for audit track learners that is
     automatically assigned. Additional cohorts for audit track learners can
     be either automatically or manually assigned.

   * You must have exactly one cohort for verified track learners, and it must
     be manually assigned. You provide the exact case sensitive name of this
     verified track cohort to your partner manager.

   * After your partner manager configures your course for verified track
     cohorting using the verified track cohort name that you provide, you
     cannot disable cohorts, and you cannot rename the special verified track
     cohort.

   For details, see :ref:`Requirements for Verified Track Cohorts`.

For detailed step by step instructions to implement differentiated
content by track in your course, see :ref:`Set Up Differentiated Content By
Track`.


.. _Set Up Differentiated Content By Track:

*******************************************
Setting Up Differentiated Content by Track
*******************************************

To provide :ref:`differentiated content <Cohorted Courseware Overview>` to the
learners in each track using cohorts and content groups, follow these steps.

.. contents::
  :local:
  :depth: 1


.. Important:: You must meet the following requirements if you use cohorts to
   provide differentiated content to verified track learners.

   * The grading policy cannot be different between your audit track and your
     verified track content. You specify differentiated content at the unit level
     in the course, therefore each track has equivalent content with the same
     weight and type per unit.

   * You must have at least one cohort for audit track learners that is
     automatically assigned. Additional cohorts for audit track learners can
     be either automatically or manually assigned.

   * You must have exactly one cohort for verified track learners, and it must
     be manually assigned. You provide the exact case sensitive name of this
     verified track cohort to your partner manager.

   * After your partner manager configures your course for verified track
     cohorting using the verified track cohort name that you provide, you
     cannot disable cohorts, and you cannot rename the special verified track
     cohort.

   For details, see :ref:`Requirements for Verified Track Cohorts`.

.. _Step 1 Create Content Groups:

===============================
Step 1: Create Content Groups
===============================

In Studio, follow these steps to create two :ref:`content groups <About
Content Groups>`.

#. :ref:`Create a content group <Creating Content Groups>` for the content
   that you will offer to audit track learners.

#. Create a content group for the content that you will offer to verified
   track learners.

.. note:: To minimize the possibility of errors, give the content groups names
   that make their purpose obvious and clearly map to the cohorts that will
   use the content. For example, "Verified Track Content" and "Audit Track
   Content".

.. _Step 2 Create Cohorts and Associate Them:

================================================================
Step 2: Create Cohorts and Associate Them With Content Groups
================================================================

In the instructor dashboard in the LMS, follow these steps to set up cohorts.

#. :ref:`Enable cohorts<Enabling and Configuring Cohorts>` in your course.

#. :ref:`Create a cohort <Add Cohorts>` for verified track learners.

   * Specify a name for this cohort.

   .. Important:: When you contact your partner manager in :ref:`Step 4 <Step
      4 Request Configuration Verified Track Cohorts>`, you provide the
      verified track cohort's exact case sensitive name.

      After your partner manager configures your course for verified track
      cohorting using the verified track cohort name that you provide, you
      cannot disable cohorts, and you cannot rename the special verified track
      cohort.

   * Specify **Manual** for the :ref:`cohort assignment method <Options for
     Assigning Learners to Cohorts>`.

   * :ref:`Associate the cohort <Associate Cohorts with Content Groups>` with
     the verified track content group that you created in the previous step.

#. Create one or more cohorts for audit track learners.

   .. Important:: If you create only one cohort for audit track learners, it
      must be automatically assigned. Additional cohorts for audit track
      learners can be either automatically or manually assigned.

   * Specify a name for each of your audit track cohorts.

   * Specify **Automatic** as the assignment method for at least one of your
     audit track cohorts.

   * Associate each of your audit track cohorts with the audit track content
     group that you created in the previous step.

.. _Step 3 Specify Content Groups Visibility:

==============================================================
Step 3: Specify Which Content Groups See What Course Content
==============================================================

In Studio, follow these steps to designate whether content is visible to all
learners, learners in the audit track, or learners in the verified track.


#. Create course content in Studio.

#. Review the flow of content in your course, and mark components as visible
   either to all learners, or to the appropriate content group (and thus to
   the appropriate cohort).

   For details, see :ref:`Specify Components in Courseware as Visible Only to
   Certain Content Groups`.


.. _Step 4 Request Configuration Verified Track Cohorts:

===============================
Step 4: Request Configuration
===============================

#. Ask your partner manager to enable your course for verified track cohorts.

#. Provide the following information with your request.

   * The course ID
   * The name of the verified track cohort

.. Important:: After your partner manager configures your course for verified
   track cohorting using the verified track cohort name that you provide, you
   cannot disable cohorts, and you cannot rename the special verified track
   cohort.

.. _Step 5 Release Course Verified Track Cohorts:

===============================
Step 5: Release Your Course
===============================

When your partner manager confirms that the verified track cohort feature is
enabled, you can release your course.

Learners who enroll in your course are automatically placed in cohorts
depending on the track that they join.

* Learners who enroll in the verified track are automatically placed in the
  verified track cohort.

* Learners who enroll in the audit track are placed in the cohort or cohorts
  that you created for audit track learners.

Learners see content that is specific for their cohort, including any
discussion topics that you specify as cohort-specific. When learners
participate in discussions, any topics that are specified as "cohort-specific"
are divided by cohort, and learners' posts and responses are  shared only with
other learners in the same cohort. For details, see :ref:`Set up Discussions
in Cohorted Courses`.

For information about differentiated content for cohorts, see :ref:`Cohorted
Courseware Overview`.

For information about how grading and content visibility affects learners when
they switch to a different track in your course, see :ref:`Impact of Learners
Switching Tracks`.


.. _Impact of Learners Switching Tracks:

*******************************************
Impacts of Learners Switching Tracks
*******************************************

During the course run, learners might change the track that they are enrolled
in, either upgrading from audit track to verified track, or leaving the
verified track and resuming the course as an audit track learner.

When learners change tracks in a course that has verified track cohorting
enabled, they are automatically assigned to the appropriate cohort upon
upgrading or re-enrolling. For example, if a learner upgrades to the verified
track from the audit track, she is automatically placed in the verified track
cohort. Conversely, when a verified track learner unenrolls from the course
and then re-enrolls in the course as an audit track learner, he is
automatically assigned to one of the automatic audit track cohorts.

Learners' states and grades are retained if they re-enroll in the course using
the same user name and email address. If learners have changed tracks, their
current grades correctly reflect the course content that they have completed
in their current track.

For example, if a verified track learner has taken an exam that was available
only for verified track learners and then unenrolls from the course, and
re-enrolls as an audit track learner, her scores for any undifferentiated content
are retained, but her score for the verified track-specific exam that she
completed would not be retained. Her grade for that part of the course would
be incomplete until she takes the audit track version of the same exam (if the
due date for the exam has not passed).


.. _Requirements for Verified Track Cohorts:

*************************************************
Requirements for Using Verified Track Cohorts
*************************************************

If you use cohorts to deliver different content to verified track learners in
your course, you must follow these requirements.

* The grading policy cannot be different between your audit track and your
  verified track content. You specify differentiated content at the unit level
  in the course, therefore each track has equivalent content with the same
  weight and type per unit.

* You must have at least one cohort for audit track learners that is set up
  with the **Automatic** assignment method. Additional cohorts for audit track
  learners can be either automatically or manually assigned.

  Having at least one automatically assigned cohort for audit track learners
  ensures that learners who enroll in the course can be placed in a cohort
  that receives audit track content, without any manual intervention.

  If you have additional cohorts for audit track learners, they can be either
  manually or automatically assigned, but at least one audit track cohort must
  be automatically assigned.

* You must have exactly one cohort for verified track learners, and it must be
  set up with the **Manual** assignment method.

  You can only have one cohort that will receive verified track content. The
  cohort must be defined as having **Manual** learner assignment. Learners
  are assigned to this cohort automatically by edX when they enroll in or
  upgrade to the verified track for your course.

* Provide the exact, case sensitive name of the cohort you will use for your
  verified track learners to your partner manager. After your course has been
  configured to use verified track cohorting, you will not be able to change the
  name of the verified track cohort, or to disable cohorts in the course.





