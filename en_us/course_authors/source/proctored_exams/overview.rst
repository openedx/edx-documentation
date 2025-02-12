.. _CA_ProctoredExams_Overview:

############################
Proctored Exam Overview
############################

Proctored exams are timed exams that learners take while online proctoring
software monitors their computer, environment, and behavior. When learners
complete a proctored exam, the recording of the exam is examined to
determine whether the learner complied with the :ref:`online proctoring rules
<Online Proctoring Rules>`.

All courses can include proctored exams, but proctored exams are most common
in courses that offer academic credit. Course teams can require that learners
pass proctored exams to earn credit in the course. For information about
offering academic credit, see :ref:`Academic Course Credit`.

Learners must be in the verified enrollment track to take a proctored exam
and earn academic course credit.

Proctored exams on edx.org use proctoring software from third-party vendors. 
A course can use one of two proctoring software products: Software Secure RPNow 
and Verificient Proctortrack.

************************************
Comparison of RPNow and Proctortrack
************************************

RPNow and Proctortrack differ in the learner experience and proctoring review
process.

Proctortrack has a required onboarding process, which learners must complete
several days before they attempt a proctored exam. RPNow has instead an optional
practice exam, which learners can use to become prepared for taking a proctored
exam.

RPNow has a set of standard exam rules, which the course team can supplement
with custom rules. Proctortrack requires you to choose from a collection of
binary exam rules.

RPNow uses a secure browser that continuously uploads proctoring data to an 
RPNow server. This secure browser needs a consistent internet connection with 
at least 500 kbps bandwidth. If a learner's connectivity drops below this level,
or if the secure browser is closed after a learner has begun the exam, the 
exam will end and will be submitted to edX at the point they left off. 

Review Process
==============

Proctoring information collected by RPNow is submitted to Software Secure for
review. If the learner's exam behavior passes review, then the learner receives
their exam grade. If the exam is marked as suspicious by Software Secure, then
edX learner support reviews the exam as well. If the exam is approved by edX
learner support, then the learner receives their exam grade. If the result is
unclear, then the learner's exam is reviewed by the course team for a final
decision.

Proctoring information collected by Proctortrack is reviewed by machine, with
spot-checking by Verificient Proctortrack reviewers. Proctortrack review
decisions are posted on the Proctortrack dashboard for review by the course
team. The course team reviews exams that are marked as failing the proctoring
criteria and makes the final decision about whether to pass or fail the
learner's exam.


**************************************
Criteria for Passing a Proctored Exam
**************************************

Learners must satisfy the following criteria to pass a proctored exam.

* Take the exam as a proctored exam.

  By default, learners must take the exam as a proctored exam. To allow
  students to have the option to take the exam as a proctored exam or
  as an unproctored exam, see :ref:`Allow Opting Out of Proctored Exams`.

  Only learners in the verified enrollment track can have the option to take the
  exam as a proctored exam.

  Verified track learners who do not take the exam as a proctored exam are
  not eligible for course credit.

* Download and install proctoring software.
* Complete identity and exam environment checks.
* Earn a passing grade on the exam.
* Receive a Satisfactory result for their proctoring session review.

For more information about the way that learners experience proctored exams,
see `Taking Timed and Proctored Exams` in the edX Help Center.

.. _Allow Opting Out of Proctored Exams:

***************************************************
Allow Opting Out of Proctored Exams
***************************************************

When a proctored exam opens, by default, verified learners must take the exam
with proctoring.

If you want to allow Verified or Master's learners the option to take proctored exams
without proctoring, please contact your edX partner manager to enable this option.

.. note::
   If a learner opts to take an exam without proctoring, the exam will not be 
   timed either. In effect, learners who opt out of proctoring will have 
   unlimited time to complete the exam and could return to problem sets at 
   any time. You can reduce the ability to view the exam by selecting a due 
   date for the exam.

.. only:: Open_edX

    To enable the option for learners to opt out of proctored exams for a course,
    follow these steps.

    #. In Studio, select **Settings**, then select **Proctored Exam Settings**.

    #. Locate the **Allow Opting Out of Proctored Exams** policy key. The default
       value is ``No``, which requires Verified and Master's learners to take
       proctored exams with proctoring.

    #. Change the value of the setting to ``Yes``.

    #. Select **Submit**.

.. include:: ../../../links/links.rst
