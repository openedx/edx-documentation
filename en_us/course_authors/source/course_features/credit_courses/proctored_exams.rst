.. _CA_ProctoredExams:

##########################################
Including Proctored Exams In Your Course
##########################################

This section describes how to create and manage proctored exams in Studio.

.. contents::
 :local:
 :depth: 1

.. _CA_ProctoredExams_Overview:

****************************
Proctored Exam Overview
****************************

Proctored exams are exams with time limits that learners complete while online
proctoring software monitors their computers and behavior for activity that
might be evidence of cheating.

In for-credit courses, course teams can create exams that they designate as
proctored exams, and require that learners pass these exams as one of the
requirements for credit eligibility.

.. note:: Only learners who are enrolled in the verified track see the option
   to take an exam with online proctoring. If you believe that there are
   students who have not yet upgraded to the verified track who should be
   taking proctored exams and qualifying for course credit, you should remind
   them to enroll in the verified track before the deadline for upgrading.

Learners in the verified track can choose to take the exam as proctored and be
eligible for course credit, or take the exam as an open exam and not be
eligible for course credit. For more information about creating proctored
exams in Studio, see :ref:`Create a Proctored Exam`.

You can also :ref:`create a practice proctored exam <Create a Practice
Proctored Exam>` for your course so that learners can become familiar with the
process of installing proctoring software and performing the required checks
ahead of time.

To satisfy the proctored exam requirement for credit eligibility, learners
must take the exam as a proctored exam and receive a **Satisfactory** result
for their proctoring session review as well as a passing grade on the exam
itself. For more information about proctored session review results, see
:ref:`Proctored Exam Session Results`.

For information about for-credit courses and specifying the passing score for
credit eligibility, see :ref:`Academic Course Credit` and :ref:`Specify
Minimum Credit Eligible Grade`.


=====================================================
Learner Requirements for Taking Proctored Exams
=====================================================

.. note:: Learners cannot complete proctored exams using the edX mobile app.

Learners who agree to take an exam with online proctoring must install
proctoring software, which checks that the person taking the exam is the same
person who is taking the course for credit, and also detects any attempts to
cheat on the exam. Learners perform a series of checks on their computer and
test environment and must also provide photo identification before being
allowed to proceed. The proctoring software then runs in the background,
monitoring the test environment and screen activity as the learner takes the
exam.

For more information about the technical requirements for taking a proctored
exam, and edX's :ref:`online proctoring rules <Online Proctoring Rules>`, see
:ref:`Preparing Learners for Proctored Exams`.

.. note:: Course staff should familiarize themselves with edX's :ref:`online
   proctoring rules <Online Proctoring Rules>`, which reflect our proctoring
   software partner's "Closed Book Exam" rules. These strict rules prohibit
   learners from using any tools during the exam, including pencil and
   paper, calculators, or reference books.

   If a particular exam in your course has a less stringent exam policy, or if
   you want to allow a particular tool (for example, a calculator or pencil and
   paper), you can enter custom rules or rule exceptions for your exam. It is
   important that the rules for your exam, if different from the "closed book"
   rules, are communicated to the proctored exam reviewers so that learners'
   exam attempts are not incorrectly disqualified. For more information, see
   :ref:`specifying_exam_rules_and_exceptions`.


.. _Proctored Exam Session Results:

===============================
Proctored Exam Session Results
===============================

When learners complete a proctored exam, either by submitting their answers or
when the time expires for the exam, the proctoring session data is uploaded to
the third party proctoring service provider. A team of reviewers examines the
data to determine whether the learner complied with the :ref:`Online Proctoring
Rules <Online Proctoring Rules>`. When the review is complete, the proctoring
service returns the results for each learner.

Before proctoring session results are available, learners see a **Pending**
result. After their proctoring sessions are available, learners can receive
either a **Satisfactory** or **Unsatisfactory** result.

Learners can check their proctoring session results by returning to the
proctored exam in the course. Their proctoring session review results are
updated there when results are received. In addition, learners can go to their
**Progress** pages, where they can check their proctored exam results as a
part of their overall credit eligibility status.

Course staff can download a report that lists proctoring results for learners
in their course. For more information, see :ref:`Proctored Session Results`.


.. _CA_LearnerExperience_Proctored Exams:

==============================================
The Learner Experience of Proctored Exams
==============================================

Only learners who have signed up for the verified track in your course have
the option of taking proctored exams. When they access a proctored exam,
learners on the verified track can choose to take the exam with online
proctoring, or to take the exam without proctoring and as an open exam with no
time limit.

If learners choose to take the exam without proctoring, they are not eligible
for credit for the exam, and will not be offered the proctored option for that
exam again.

Learners who are not ready to make the choice or take the exam immediately can
defer their decision and return to the exam again at some other time before
the due date.

.. Question for Griff or Julia

.. Do we want to give advice to course staff about planning an adequate due
.. date?  e.g. allow more time than normal for allow proctoring results to come
.. back? Allow time for administrative tasks, especially as edX support needs
.. to be involved in creating extra time allowances. Course staff need to allow
.. enough time to get confirmations back from Support and also to notify
.. students. If resolution of any technical difficulty disputes is needed,
.. students also need adequate time to retake the exam.


Taking a proctored exam
+++++++++++++++++++++++++++++++++

When learners agree to take the exam with online proctoring, they are guided
through the process of installing the proctoring software and performing
system and user checks, including ID verification. They must be ready to take
the exam as soon as the proctoring session setup is completed. For details,
see :ref:`SFD Before Taking Proctored Exam` in the *edX Learner's Guide*.

After learners successfully complete the checks, the proctoring session starts.
Learners are reminded not to close the proctoring software window. They are
prompted to return to the browser window where the course is open, and to
start taking the exam.

A countdown timer is visible at the top of the page during the exam. Warnings
are displayed when there is 20% and 5% of allotted time remaining. For example,
if the allowed time in the exam is 60 minutes, learners see a warning when
there are 12 minutes remaining, and again when there are 3 minutes remaining.

For information about scenarios that learners might encounter while taking
proctored exams, see :ref:`Respond to Learner Concerns about Proctored Exams`
and :ref:`CA_Situations_Learners_Encounter_Proctored_Exams`.


Completing a proctored exam
+++++++++++++++++++++++++++++++++

When learners complete the exam, or when the countdown timer reaches 00:00,
they no longer have access to the exam. Learners are reminded to quit the
proctoring session, and the proctoring software begins the process of
uploading the captured session data.

On the proctored exam page in the LMS, learners see a status of "Pending" for
their proctoring session results until their session data has been reviewed.
They can return to this page in the course or check their **Progress**
pages in the LMS for updates to their proctoring review results.



.. _Preparing Learners for Proctored Exams:

====================================================
Preparing Learners for Proctored Exams
====================================================

Well before the exam is due, provide learners with information about the
grading policy of your course, and make it clear what the requirements are for
earning credit.

Explain what proctored exams are, and provide learners with links to the
Learner's Guide topics about proctored exams, and to edX's :ref:`online
proctoring rules <Online Proctoring Rules>`.

.. note:: Course staff should familiarize themselves with edX's :ref:`Online
   Proctoring Rules <Online Proctoring Rules>`, which reflect our proctoring
   software partner's "Closed Book Exam" rules. These strict rules prohibit
   learners from using any tools during the exam, including pencil and
   paper, calculators, or reference books.

   If a particular exam in your course has a less stringent exam policy, or if
   you want to allow a particular tool (for example, a calculator or pencil and
   paper), you can enter custom rules or rule exceptions for your exam. It is
   important that the rules for your exam, if different from the "closed book"
   rules, are communicated to the proctored exam reviewers so that learners'
   exam attempts are not incorrectly disqualified. For more information, see
   :ref:`specifying_exam_rules_and_exceptions`.

Emphasize that learners must be aware of the requirements before taking the
exam, and that some of the requirements might take some preparation.

You can also create a practice proctored exam that is visible to all learners.
This ungraded exam provides an opportunity for learners to experience the
proctoring software setup process and make sure their computers are compatible
with the software. For more information, see :ref:`Create a Practice Proctored
Exam`.

.. note:: In an actual proctored exam, as soon as learners agree to take the
   exam with online proctoring and start the process of installing the
   proctoring software, they must continue through to taking the exam as soon
   as that process is completed.

The following list represents only some of the requirements listed in the
:ref:`online proctoring rules <Online Proctoring Rules>`.

* System and environment checks that learners are asked to perform for the
  proctoring session include taking a photo of a government-issued photo ID,
  and a photo of themselves, using the webcam on their computer. In addition,
  they must use the webcam to provide a room scan that includes the desk area,
  the area under their desk, and a view around the whole room.

* Learners must sit at a clean desk or table that has been cleared of all
  materials such as phones, books, notebooks, pens, and papers. They cannot
  sit on a bed or couch to take the proctored exam.

* No writing can be visible on the desk or walls in the test environment.

* The computer on which a learner takes the exam must not have a secondary
  monitor connected.

* Once the exam starts and until it ends, the learner cannot leave the room
  for any reason.

* Once the exam starts and until it ends, no other person can enter the room
  for any reason.

* The learner cannot talk to anyone or communicate by any means with another
  person during the exam.

* Learners cannot have music or the television playing in the background during
  the exam. They cannot use headphones, ear buds, or any other type of
  listening equipment.


.. _Enabling Proctored Exams:

**************************************************
Enabling Proctored Exams in Your Course
**************************************************


To enable proctored exams in your course, follow these steps.

#. In Studio, select **Settings**, then select **Advanced Settings**.

#. Locate the **Enable Proctored Exams** policy key. The default value is
   ``false``.

#. Change the value of the setting to ``true``.

#. Select **Save Changes**. You can now create proctored exams in your course.

After you enable this setting for your course, you can perform the
following tasks.

.. contents::
 :local:
 :depth: 1


.. _Create a Proctored Exam:

=================================
Create a Proctored Exam
=================================

To create an exam that includes online proctoring, follow these steps.

.. note:: Proctored exams are always timed exams.

#. Add and :ref:`develop a subsection <Developing Course Subsections>` as you
   would any other subsection.

#. Select the **Configure** icon for the subsection.

   .. image:: ../../../../shared/images/subsections-settings-icon.png
    :alt: A subsection in the course outline with the configure icon indicated.
    :width: 600

   The **Settings** dialog box opens to the **Basic** tab.

#. In the **Grading** section, set the :ref:`assignment type and due date<Set
   the Assignment Type and Due Date for a Subsection>` for the subsection.

#. Select the **Advanced** tab.

#. In the **Set as a Special Exam** section, select **Proctored**.

#. In the **Time Allotted** field, enter the length of time that you want
   learners to have to complete the problems in the subsection. Enter the time
   as HH:MM, where HH is hours and MM is minutes.

#. Optionally, in the **Review Rules** field, enter any additions or exceptions
   to the :ref:`default rules for proctored exams<Online Proctoring Rules>`.
   For more information, see :ref:`specifying_exam_rules_and_exceptions`.

#. Select **Save**.

For information about how learners experience a proctored exam, see
:ref:`CA_LearnerExperience_Proctored Exams`. For information about creating a
practice exam that learners can take, see :ref:`Create a Practice Proctored
Exam`.


.. _Create a Practice Proctored Exam:

===================================
Create a Practice Proctored Exam
===================================

You can add a practice proctored exam to your course so that learners can
confirm that their systems are compatible with the proctoring software and
familiarize themselves with the steps to perform the identity and environment
checks.

.. note:: Unlike actual proctored exams, practice exams are visible to all
   learners, regardless of the track that they are enrolled in.

Practice exams are not linked to credit eligibility requirements and
no monitoring by the proctoring software is actually done, but learners will
be guided through the same steps as in a real proctored exam, to install the
proctoring software, perform the identify checks and room scan.

Learners who have performed the proctoring software installation for a
practice exam are required to perform the same installation step when they
prepare to take an actual proctored exam, to ensure that they are using the
latest version of the proctoring software.

.. note:: Make sure you create the practice exam as an ungraded exam.

To create a practice exam, follow these steps.

#. Add and :ref:`develop a subsection <Developing Course Subsections>` as you
   would any other subsection.

#. Select the **Configure** icon for the subsection.

   .. image:: ../../../../shared/images/subsections-settings-icon.png
    :alt: A subsection in the course outline with the configure icon indicated.
    :width: 600

   The **Settings** dialog box opens to the **Basic** tab.

#. In the **Grading** section, set the :ref:`assignment type and due date<Set
   the Assignment Type and Due Date for a Subsection>` for the subsection.

#. Select the **Advanced** tab.

#. In the **Set as a Special Exam** section, select **Practice Proctored**.

#. In the **Time Allotted** field, enter the length of time that you want
   learners to have to complete the problems in the subsection. Enter the time
   as HH:MM, where HH is hours and MM is minutes.

   For a practice exam, edX recommends that you specify a relatively short
   duration that is appropriate for the number of example problems you
   include in the subsection.

#. Select **Save**.

#. Optionally, add a unit with a text component to the practice exam
   subsection. You can use the text component to provide learners with
   information about the proctored exam in your course.

The practice exam is added to the course, and is visible to all learners
regardless of their enrollment track.

.. _specifying_exam_rules_and_exceptions:

====================================
Specifying Exam Rules and Exceptions
====================================

The team of reviewers who examine exam attempt records determine whether
learners complied with the :ref:`Online Proctoring Rules <Online Proctoring
Rules>`. By default, the team of reviewers uses the standard set of rules for
taking proctored exams.

You can provide custom rules and rule exceptions if the content of an exam
requires them. If your course allows learners to use tools and techniques that
the default rules for proctored exams prohibit, you must provide information
about these rules and exceptions both to your learners and to the team of
reviewers.

To specify custom proctored exam rules and rule exceptions, follow these steps.

#. In Studio, open your course outline and select the subsection for the exam.

#. Select the **Configure** icon to open the **Settings** dialog box.

#. Select the **Advanced** tab.

#. In the **Review Rules**
   field, describe any additional rules or rule exceptions.

   Write clear, English-language descriptions of your exam rules. For example,
   you could enter the following rules.

   ``Allow one blank sheet of paper and a pencil or pen. Allow a hand-held
   calculator on the desk.``

#. Select **Save**.

.. note::
   Your description of the additional rules and rule exceptions must be as
   clear, specific, and easy to understand as possible. If the reviewers do not
   understand your rules and exceptions, they may incorrectly disqualify exam
   attempts. Use uncomplicated sentences and words that a global English-
   speaking audience will understand.

.. _Allow Opting Out of Proctored Exams:

*************************************************************
Allowing Verified Learners to Opt Out of Proctored Exams
*************************************************************

By default, verified learners can choose to take proctored exams without
online proctoring, and accept that they are no longer eligible for course
credit if they make this choice.

If you do not want to give verified learners in your course the choice of
taking proctored exams without proctoring, you can change a setting on the
**Advanced Settings** page in Studio.

==============================================================
Do Not Allow Verified Learners to Opt Out of Proctored Exams
==============================================================

To remove the option for verified learners to opt out of proctored exams in
your course, follow these steps.

#. In Studio, select **Settings**, then select **Advanced Settings**.

#. Locate the **Allow Opting Out of Proctored Exams** policy key. The default
   value is ``true``, which gives verified learners the option of taking
   proctored exams without proctoring.

#. Change the value of the setting to ``false``.

#. Select **Save Changes**.

After you enable this setting for your course, options for taking exams
without proctoring are no longer available to verified learners.


.. _Respond to Learner Concerns about Proctored Exams:

**********************************************************
Responding to Learners' Concerns about Proctored Exams
**********************************************************

In addition to questions that can be answered in the FAQs on edx.org, or by the
:ref:`online proctoring rules <Online Proctoring Rules>`, situations might
arise that require an action by edX Support.

.. contents::
 :local:
 :depth: 1


.. _Requests for Additional Time:

===================================
Handle Requests for Additional Time
===================================

In some situations, for example to accommodate learners with disabilities,
additional time allowances can be provided for specific students. Consult with
your organization's Disability Services resources to decide whether and how a
learner with specific needs can be accommodated for a timed exam.

.. note:: Make sure the learner who has requested additional time does not
   start taking the proctored exam before the additional time has been approved
   and set up.

If it is confirmed that additional time should be allowed for a specific
student to take the exam, follow these steps.

#. Contact edX Support to ask them to set up a time allowance for the learner.

#. Provide edX Support with the learner's username or email address, and the
   amount of additional time that this learner should be allowed to complete
   the exam.

#. When the allowance has been set up, let the learner know their adjusted
   allowed time for the exam.

   When this learner starts taking the exam, the exam timer takes into account
   the adjusted time.


.. _Requests for Special Allowances:

=======================================
Handle Requests for Special Allowances
=======================================

In some situations, for example to accommodate learners with disabilities,
special allowances can be provided for specific students. Consult with your
organization's Disability Services resources to decide whether and how a
learner with specific needs can be accommodated.

.. note:: Make sure the learner who has requested special allowances does not
   start taking the proctored exam before the exemption has been approved and
   set up.

If it is confirmed that a special allowance should be made to the exam
policy for a particular learner, follow these steps.

#. Contact edX Support and ask the support team to set up a special allowance
   for the learner.

#. Provide edX Support with the learner's username or email address and the
   exception to the standard exam policy. For example, "Learner cannot
   see. Allow an additional person in the room to act as a scribe."

#. When the allowance has been set up, let the learner know that their special
   allowance has been granted.

   When the learner's proctored exam results are reviewed, the reviewer is
   aware of the special allowance and takes that into account.


.. _Requests for Retaking a Proctored Exam:

=====================================================
Handle Requests for Retaking a Proctored Exam
=====================================================

Course teams might have to assist learners who have experienced technical
difficulties with online proctoring, or have other reasons to request
permission to retake a proctored exam. Learners can contact edX support to
request that their proctored exam attempts be cleared. Clearing a proctored
exam attempt allows a learner to retake a proctored exam.

.. note:: Deleting a learner's exam attempt clears all submitted answers, and
   the learner experiences the exam as if for the first time, including making
   the choice to take the exam with online proctoring, obtaining an exam code,
   going through the proctoring software setup, and so on.

If a learner needs to retake a proctored exam, follow these steps.

#. Instruct the learner to contact edX Support and request that the support
   team delete the exam attempt.

#. When the exam attempt has been deleted, instruct the learner to
   retake the exam.


.. _Proctored Session Results:

******************************
Proctored Session Results
******************************

The proctoring software monitors both the screen activity and webcam view of
learners. When learners complete a proctored exam, their proctoring session
data is uploaded for review by the proctoring service provider. Reviewers
apply defined criteria including the :ref:`Online Proctoring Rules <Online
Proctoring Rules>` to decide whether any observed behavior should be flagged.

Two results are possible for proctoring session reviews.

*  **Satisfactory** - the learner has passed the proctoring review.

*  **Unsatisfactory** - Some suspicious activity has been observed. The
   learner has not passed the proctoring review.

Some learner behavior that is listed in the Online Proctoring Rules is
discouraged but does not impact the integrity of the exam. Violations in these
cases might be flagged but learners with such flags can still receive a
**Satisfactory** result. For example, a learner is discouraged from playing
music or having a TV on in the background while they take their exam, but if
their session recording shows such behavior, it is still possible for them to
receive a **Satisfactory** result for their proctoring session results, as long
as there are no instances of suspicious activity that do seem to indicate
cheating.

Activities that would cause learners to fail their proctoring session review
include not providing a photo ID, using a second computer during the proctored
exam, appearing to read the exam to another person in the room, displaying
nudity or explicit materials or browsing adult-based content. If there is even
one instance of such activity, learners receive an **Unsatisfactory** result
for their proctoring session.


.. _Viewing Proctored Session Results:

=================================
Viewing Proctored Session Results
=================================

At any time after learners have taken the proctored exam in your course, you
can download a .csv file that displays the status of the proctoring session
for participating learners.

.. note:: The Proctored Session Results report only shows the result of
   reviews of the proctored sessions. These results are separate from the
   learners' grades on the exam.

To generate and download a file of proctoring session results, follow these
steps.

.. important:: Because the proctoring session results file contains
   confidential, personally identifiable data, be sure to follow your
   institution's data stewardship policies when you open or save this file.

#. View the live version of your course.

#. In the LMS, select **Instructor**, then select **Data Download**.

#. Select **Generate Proctored Exam Results Report**.

   .. image:: ../../../../shared/images/Proctoring_GenerateCSVExamResults.png
     :alt: The "Generate Proctored Exam Results Report" button in the LMS.
     :width: 400

   A status message indicates that the report generation process is in
   progress. This process can take some time to complete, but you can navigate
   away from this page and do other work while it runs.

#. To check the progress of the report generation, reload the page in your
   browser and scroll down to the **Pending Tasks** section. The status of
   active tasks is shown in the table.

   When the report is complete, a linked .csv file name becomes available
   above the **Pending Tasks** section. File names are in the format
   ``{course_id}_proctored_exam_results_report_{datetime}.csv``. The most
   recently generated reports appear at the top of the list.

#. To open or save a report file, locate and click the link for the report you
   requested.

   .. image:: ../../../../shared/images/Proctoring_CSVExamResultsLink.png
     :alt: The link for a generated proctored exam results report in the
         instructor dashboard.
     :width: 600

   You can open .csv files in a spreadsheet application to sort, graph, and
   compare data.

.. note:: To prevent the accidental distribution of learner data, you can
   download exam result report files only by clicking the links on this page.
   Do not copy these links for reuse elsewhere, as they expire within 5
   minutes. The links on this page also expire if the page is open for more
   than 5 minutes. If necessary, refresh the page to generate new links.


.. _Proctored Session Results File:

=================================================
Understanding the Proctored Session Results File
=================================================

The .csv file that you can download to view the status and results of
learners' proctoring sessions contains the following fields.


.. list-table::
   :widths: 30 55
   :header-rows: 1

   * - Column
     - Description
   * - user_email
     - The username or email address that identifies the learner taking the
       proctored exam.
   * - exam_name
     - The name of the proctored exam in the body of the course.
   * - attempt_code
     - An identifier for the exam attempt. The attempt code is an
       internal identifier and is included in the report for use in
       troubleshooting.
   * - allowed_time_limit_mins
     - The amount of time in minutes that this learner was allotted for
       completing the exam.
   * - is_sample_attempt
     - Indicates whether this exam attempt was for a practice exam.
   * - started_at
     - The date and time that the learner started to take the proctored exam.
   * - completed_at
     - The date and time that the learner submitted the proctored exam.
   * - status
     - The status of the proctoring session review. Possible values are
       ``created``, ``ready to start``, ``started``, ``timed out``,
       ``completed``, ``submitted``, ``second review required``, ``verified``,
       ``rejected``, and ``error``. For an explanation of each status, see the
       table below.


The following table describes the possible values in the Status column.

.. list-table::
   :widths: 30 55
   :header-rows: 1

   * - Value in the Status column
     - Description
   * - Created
     - The exam attempt record has been created, but the exam has not yet been
       started.
   * - Ready to Start
     - The exam attempt record has been created. The learner still needs to
       start the exam.
   * - Started
     - The learner has started the proctored exam.
   * - Timed Out
     - The proctored exam has timed out.
   * - Completed
     - The learner has completed the proctored exam.
   * - Submitted
     - The learner has completed the proctored exam and results have been
       submitted for review.
   * - Second Review Required
     - The exam attempt has been reviewed and the review team has
       determined that it requires additional evaluation. The review team will
       perform the second review. Course teams do not need to take any action.
   * - Satisfactory
     - The proctoring session review has been completed, and has passed.
   * - Unsatisfactory
     - The proctoring session review has been completed, and has not passed.
   * - Error
     - The exam is believed to be in error.


.. _CA_Situations_Learners_Encounter_Proctored_Exams:

**********************************************************
Situations that Learners Might Encounter
**********************************************************

This section provides information about scenarios that learners might
encounter while they take proctored exams. In general, course teams will have
to decide how to proceed on a case by case basis.

=========================================================
Navigating to Another Part of the Course During an Exam
=========================================================

While they are taking a proctored exam, learners can navigate (using the same
browser session) to other parts of your course.

.. note:: It is a violation of edX's Online Proctoring Rules for learners to
   navigate to websites other than edX.org during the proctored exam.

If learners navigate to other parts of your course, they see an alert message
indicating that the timer on their exam continues to count down. When learners
return to the exam, they resume where they left the exam. The timer has been
continuing to count down during the learner's time away from the exam.


==========================================
Running Out Of Time In an Exam
==========================================

If the timer reaches 00.00 before a learner has completed the exam, the exam
ends, and all answers that the learner has submitted up to that point in time
are submitted for grading.

The proctoring software detects that the edX exam has ended, and prompts
learners to confirm that they want to quit their proctoring session. Learners
must go back to the proctoring software and confirm that they are quitting, so
that the proctoring session ends and the proctoring session data is uploaded
for review.


=======================================================
Closing a Browser Window Before The End of the Exam
=======================================================

Several situations might arise during the exam. This section describes the
result of each of these situations.

In some cases, course team members will have to decide whether the exam
results that were obtained are valid, or whether the exam attempt should be
cleared and the learner given an opportunity to retake the exam. For more
information, see :ref:`Requests for Retaking a Proctored Exam`.


The Proctoring Software Terminates Unexpectedly
+++++++++++++++++++++++++++++++++++++++++++++++++++

If the proctoring software crashes, the LMS alerts learners and stops the
exam. Learners should contact edX Support in this situation.


The edX Browser Terminates Unexpectedly
+++++++++++++++++++++++++++++++++++++++++++++++++++

If the browser in which the edX exam is running crashes, the exam timer for
each learner continues to run. Learners can reopen their exam in a new browser
window and continue their exam, but they will have lost time while the browser
was closed.

.. Question for Chris: how does the proctoring software view such a break in
.. taking the exam?


Learners Close the Proctoring Software Window
+++++++++++++++++++++++++++++++++++++++++++++++

If learners close their proctoring software windows before they have completed
a proctored exam, they see alert messages warning them that they are ending
their exam. If they continue to close the proctoring software window, both the
exam and the proctoring session end.

The exam is stopped in the LMS. Answers in the exam up to the point that the
session ended are submitted for grading, but the proctoring session recording
might not be completely uploaded. Learners should contact edX Support in this
situation.


Learners Close the edX Exam Window
+++++++++++++++++++++++++++++++++++

If learners close the browser in which their edX proctored exam is running
before they have completed the exam, they might not see any alerts, depending
on the browser that they are using. The exam  timer for each learner continues
to run. If learners reopen their exam in a new browser window, they can
continue their exam, but they will have lost time while the browser was
closed.

.. Question for Chris: how does the proctoring software view such a break in
.. taking the exam?
