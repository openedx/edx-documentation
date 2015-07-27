.. _CA_ProctoredExams:

##############################
About Proctored Exams
##############################

This section describes how to create and monitor proctored exams in Studio.

.. contents::
 :local:
 :depth: 1

.. _CA_ProctoredExams_Overview:

****************************
Proctored Exam Overview
****************************

In for-credit courses, course teams can create exams that they designate as
proctored exams. Learners in the Verified track can choose to take the exam as
proctored and be eligible for course credit, or take the exam as a non-
proctored exam and not be eligible for course credit. For more information
about creating proctored exams in Studio, see :ref:`Create a Proctored Exam`.

To earn credit for completing a course, learners must take the exam as a
proctored exam and receive a passing result for their online proctoring
session, in addition to achieving a passing grade in the course.

Learners who agree to take an exam with online proctoring must install
proctoring software, which checks that the person taking the exam is the same
person who is taking the course for credit, and also detects any attempts to
cheat on the exam.  Learners perform a series of checks on their computer and
test environment and must also provide photo identification before being
allowed to proceed. The proctoring software then runs in the background,
monitoring the test environment and screen activity as the learner takes the
exam.

When learners complete a proctored exam, either by submitting their answers or
when the time expires for the exam, proctoring data is uploaded to the third
party proctoring service provider. This data is reviewed for adherence to
edX's Online Proctoring Rules :ref:(ADD LINK), and when the review is complete, a
Pass or Fail result is returned for each learner who took the exam as a
proctored exam.

.. Need to verify how course staff check proctoring results for students.

When proctoring session results become available, course staff can download a
report that lists proctoring results for learners in their course. For more
information, see :ref:`Reviewing Proctoring Results for Learners`.

.. For passing students, is there some visible status change for certificates etc. that is triggered to indicate that they can go ahead with requesting credit? Anything visible in the UI?

Learners with passing grades as well as a Pass result for the proctored exam
are shown as eligible for credit on their Progress pages.

.. any integration points with the credit eligibility doc?


.. _CA_LearnerExperience_Proctored Exams:

==============================================
The Learner Experience of Proctored Exams
==============================================

Only learners who have signed up for the Verified track in your course have
the option of taking proctored exams. When they access a proctored exam,
learners on the Verified track can choose to take the exam with online
proctoring, or to take the exam without proctoring and only as a timed exam.

If learners choose to take the exam without proctoring, they are not eligible
for credit for the exam, and will not be offered the proctored option for that
exam again.

Learners who are not ready to make the choice or take the exam immediately can
defer their decision and return to the exam again at some other time before
the due date.

.. Do we want to give advice to course staff about planning an adequate due date? e.g. allow more time than normal for administrative tasks, especially as edX support needs to be involved in tasks such as creating extra time allowances. Course staff need to allow enough time to get confirmations back from Support and also to notify students. If resolution of any technical difficulty disputes is needed, students also need adequate time to retake the exam.

.. How does the due date interact with the proctoring review process?

When learners agree to take the exam with online proctoring, they are guided
through the process of installing the proctoring software and performing
system and user checks, including ID verification. They must be ready to take
the exam as soon as the proctoring session setup is completed. For details,
see :ref:(REF to STUDENT doc)

Once learners successfully complete the checks, the proctoring session starts.
Learners are reminded not to close the proctoring software window. They are
prompted to return to the browser window where the courseware is open, and to
start taking the exam.

A countdown timer is visible at the top of the courseware page during the
exam. Warnings are displayed when there is 20% and 5% of allotted time
remaining.

When learners complete the exam, or when the countdown timer reaches 00:00,
they no longer have access to the exam. The proctoring software begins the
process of uploading the captured session data. Learners are notified of this
and see a status of "Pending" for their proctoring session results. They can
check their Progress pages in the LMS for updates to the proctoring review
results. If they receive a passing result for proctoring as well as passing
grades for the course, they are shown as being eligible for credit on their
Progress page.


.. _Preparing Learners for Proctored Exams:

====================================================
Preparing Learners for Proctored Exams
====================================================

Well before the exam is due, provide learners with information about the
grading policy of your course, and make it clear what the requirements are for
earning credit.

Explain what proctored exams are, and provide learners with links to
documentation about proctored exams in the Learner's Guide, and to edX's
Online Proctoring Rules. Emphasize that learners must be aware of the
requirements before taking the exam, and that some of the requirements might
take some preparation.

When learners agree to the exam with online proctoring and start the process of
installing the proctoring software, they must continue through to taking the
exam as soon as that process is completed.

The following list represents only some of the requirements listed in the
Online Proctoring Rules.

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


.. _Enabling Timed or Proctored Exams:

**************************************************
Enabling Timed or Proctored Exams in Your Course
**************************************************

To enable timed or proctored exams in your course, follow these steps.

.. note:: Proctored exams are always also timed exams.

#. In Studio, select **Settings**, then select **Advanced Settings**.

#. Scroll down to locate the **Enable Proctored Exams** policy key. The
   default value is ``false``.

#. Change the value of the setting to ``true``.

#. Select **Save Changes** at the bottom of the page. You can now create timed
   or proctored exams in your course.


.. _Create a Proctored Exam:

=================================
Create a Timed or Proctored Exam
=================================

To create an exam that has a time limit for completion or is a proctored exam,
follow these steps. Proctored exams are always also timed exams.

#. In Studio, in your course outline, add a subsection for your exam.

#. Click the Settings icon to open the settings dialog for the exam.

#. Select the **This exam is timed** option, and specify the allotted time for
   the exam in hours and minutes.

#. To specify that the exam is also a proctored exam, select the **This exam
   is proctored** option.

#. Click **Save**.   


.. _Respond to Learner Concerns about Proctored Exams:

**********************************************************
Responding to Learners' Concerns about Proctored Exams
**********************************************************

In addition to questions that can be answered in FAQs or by the edX Online
Proctoring Rules, situations might arise that require an action by edX
Support. 

.. contents::
 :local:
 :depth: 1


===================================
Handle Requests for Additional Time 
===================================

In some situations, for example, to accommodate learners with disabilities,
additional time allowances can be provided for specific students. Consult with
your organization's Disability Services resources to decide whether and how a
learner with specific needs can be accommodated for a proctored exam.

If it is confirmed that additional time should be allowed for a specific
student to take the proctored exam, follow these steps.

#. Contact edX Support to ask them to set up a time allowance for the learner.

#. Provide edX Support with the learner's username or email address, and the
   amount of additional time that this learner should be allowed to complete
   the proctored exam.

#. When the allowance has been set up let the learner know their adjusted
   allowed time for the proctored exam.

   When this learner starts taking the proctored exam, the timer takes into
   account the adjusted time allowed.


=====================================================
Handle Requests for Retaking a Proctored Exam
=====================================================

Course teams might have to manage situations where learners experienced
technical difficulties with online proctoring, or other reasons for requesting
a chance to retake a proctored exam.

If you believe that a learner's request for retaking a proctored exam is
valid, you can ask edX Support to delete the record of a learner's exam
attempt. Doing so clears all previously submitted answers, and the learner
experiences the exam as if for the first time. Provide edX Support with the
learner's username or email address. When the exam attempt has been deleted,
let the learner know that they can take the exam again.


